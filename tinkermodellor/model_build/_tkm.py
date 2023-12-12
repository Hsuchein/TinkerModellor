from ._class._gmxmolecule import GMXMolecule
from ._class._tkm_system import TinkerModellorSystem
import re


#This is the regular expression for specific part in topology file

#this is the regular expression for capturing the charge part in protein top file
#but protein top file has two different patterns for charge part
#(ions&water)              1                  Na+                           1                 Na+                Na+                1            1.00000000        22.990000                        ; qtot 1.000000
#(ligand)                  1                  ca                            1                 MOL                C                  1            0.00000000        12.010736
#(protein)                33                  C                           248                 GLU                C                 33            0.5366            12.01
#(protein)                34                  O                           248                 GLU                O                 34           -0.5819            16                               ; qtot 0
#                      <- group 1 -> <------------grp 2------------> <-------------------------------------------------------------- grp 3 -------------------------------------------------------> <--------------- grp 4 --------------->
#
ATOMTYPE_PATTERN = r"(\s*[0-9]+\s*)([0-9]?[a-zA-Z][0-9a-zA-Z]*-?\+?)(\*?\s*[0-9]+\s*[0-9]?[a-zA-Z][0-9a-zA-Z]*-?\+?\s*[0-9]?[a-zA-Z][0-9a-zA-Z]*-?\+?\s*[0-9]+\s*-?[0-9]+\.[0-9]+\s*[0-9]+\.*[0-9]*)(\s*;\s*[a-z]*\s*-?[0-9]*.[0-9]*\s*\n)?"


#[ bonds ]
#;                    ai          aj     funct         c0         c1         c2         c3
#                     17          20     1            0.14650 272713.120000
#                 <-- grp 1 --><grp 2 ><---------------grp 3--------------->
BOND_PATTERN = r"\s*([0-9]+)\s*([0-9]*)(\s*1\s*[0-9].[0-9]*\s[0-9]*.[0-9]*\n)"

#[ molecules ]
#;                     Compound               mols
#                      system1                1
#                      Na+                    10
#                      WAT                    9971
#                 <-------- grp 1 ---------><grp 2 >
MOLECULES_PATTERN = r"([A-Za-z0-9]*-?\+?\s*)([0-9]+\n)?"

class TinkerModellor:

    def __init__(self) -> None:
        pass

    def __call__(self,gro_file:str ,top_file:str):
        self.build_tkmsystem(gro_file,top_file)


    #read top file
    def _read_top_file(self,top_path:str):
        
        with open(top_path,'r') as f:
            lines=f.readlines()

        #Used for store the different molecules
        #Once read a new molecule, the it would be append to self.moleculestype.
        self.moleculetype = [GMXMolecule()]

        #To control whether the has already appeared
        molecules_flag= False

        #To record each moleculetype's number in entire system
        self.moleculetype_num = []

        #Used for counting how many moleculetypes have been read
        molecule_type_count = 0 

        for line in lines:
            #A new molecule start (according to the GMX top file format)
            #GMX topology file format description: https://manual.gromacs.org/current/reference-manual/topologies/topology-file-formats.html

            
            if '[ moleculetype ]' in line:
                #DEBUG##print("Detect a new moleculetype")
                
                #To add items into moleculetype(GMXMolecule)
                if molecule_type_count > 0:
                    #print(atomtype_read)
                    #print(molecule_type_count)
                    #print(bond_read)
                    self.moleculetype[molecule_type_count](f'TKM{molecule_type_count}',atomtype_read,bond_read)
      
                #Build a new GMXMolecule class to store a new moleculetype
                molecule_type_count += 1
                self.moleculetype.append(GMXMolecule())    
                atomtype_read = []
                bond_read = []
                continue

            #Only when the molecule type is not empty, the program would read the information
            if molecule_type_count > 0 and molecules_flag == False:

                #To match the ATOMTYPE_PATTERN
                match_atomtype = re.fullmatch(ATOMTYPE_PATTERN,line)
                if match_atomtype:
                    atomtype_read.append(match_atomtype.group(2))
                #To match the BOND_PATTERN
                match_bond = re.fullmatch(BOND_PATTERN,line)
                if match_bond:
                    #DEBUG##print(line)
                    bond_read.append([int(match_bond.group(1)),int(match_bond.group(2))])
            
            
            if '[ molecules ]' in line:
                self.moleculetype[molecule_type_count](f'TKM{molecule_type_count}',atomtype_read,bond_read)
                molecules_flag =True

            if molecules_flag and re.fullmatch(MOLECULES_PATTERN,line):

                self.moleculetype_num.append(line.strip().split(' ')[-1])
                print(f"Detect a new molecule, and it has {self.moleculetype_num[-1]} molecules")
                
        

    def _read_gro_file(self,gro_path):

        with open(gro_path,'rt') as f:#read gro file
            lines = f.readlines()
            #To record the entire system's atom numbers
            self.system_atom_nums = int(lines[1])

        #To record the entire system's coordinates
        self.coordinates = [None]
        for line in lines[2:-1]:
            line = line.strip().split('  ')#split into 5-6 items
            self.coordinates.append([float(i)*10 for i in line[-3:]])

    def build_tkmsystem(self,gro_path:str, top_path:str):

        self._read_top_file(top_path)
        assert len(self.moleculetype)-1 == len(self.moleculetype_num), f'Number of Moleculetypes({len(self.moleculetype)}) in [ molecules ] Must Be Equal To Number({len(self.moleculetype_num)}) of [ moleculetype ]'

        self._read_gro_file(gro_path)

        self.system = TinkerModellorSystem()
        #According to self.moleculetype to rebuild the Tinker XYZ format file
        #DEBUG##print(len(self.moleculetype_num))
        count = 0
        while count < len(self.moleculetype_num):
            print("index is", self.system.AtomNums+1,self.system.AtomNums+self.moleculetype[count+1].AtomNums)
            print("moleculetype is", self.moleculetype[count+1].MoleculeName, self.moleculetype[count+1].AtomTypes)
            for i in range(int(self.moleculetype_num[count])):
                self.system(atomcrds=self.coordinates,molecule_class=self.moleculetype[count+1],atom_index=[self.system.AtomNums+1,self.system.AtomNums+self.moleculetype[count+1].AtomNums])
            count +=1
        #DEBUG##print(self.system.AtomCrds)
    
    def write_tkmsystem(self,xyz_path:str):
        self.system.write(xyz_path)

if __name__ == '__main__':
    
    new= tinkermodellor()
    new(r'/home/wayne/quanmol/TinkerModelling/tinkermodellor/gromacs.gro',r'/home/wayne/quanmol/TinkerModelling/tinkermodellor/gromacs.top')

