from typing import Any
from tinkermodellor._class._gmxmolecule import GMXMolecule
from tinkermodellor._class._tkm_system import TinkerModellorSystem
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
BOND_PATTERN = r"(\s*[0-9]*\s*)([0-9]*)(\s*1\s*[0-9].[0-9]*\s[0-9]*.[0-9]*)"

#[ molecules ]
#;                     Compound               mols
#                      system1                1
#                      Na+                    10
#                      WAT                    9971
#                 <-------- grp 1 ---------><grp 2 >
MOLECULES_PATTERN = r"([A-Za-z0-9]*-?\+?\s*)([0-9]+)"

class tinkermodellor:

    def __init__(self) -> None:
        pass

    def __call__(self,gro_file:str ,top_file:str):
        self.build_tkmsystem(gro_file,top_file)


    #read top file
    def read_top_file(self,top_path:str):
        
        with open(top_path,'r') as f:
            lines=f.readlines()

        #Used for store the different molecules
        #Once read a new molecule, the it would be append to self.moleculestype.
        self.moleculetype = []

        #To control whether the has already appeared
        molecules_flag= False

        #To record each moleculetype's number in entire system
        self.moleculetype_num = []

        for line in lines:
            #A new molecule start (according to the GMX top file format)
            #GMX topology file format description: https://manual.gromacs.org/current/reference-manual/topologies/topology-file-formats.html

            molecule_type_count = 0 
            if '[ moleculetype ]' in line:
                
                #To add items into moleculetype(GMXMolecule)
                if molecule_type_count > 0:
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
                    bond_read.append(list(match_bond.group(1),match_bond.group(2)))
            
            
            if '[ molecules ]' in line:
                self.moleculetype[molecule_type_count](f'TKM{molecule_type_count}',atomtype_read,bond_read)
                molecules_flag =True

            if molecules_flag and re.fullmatch(MOLECULES_PATTERN,line):
                self.moleculetype_num.append(line.strip()[-1])
                
                
        

    def read_gro_file(self,gro_path):

        with open(gro_path,'rt') as f:#read gro file
            lines = f.readlines()
            #To record the entire system's atom numbers
            self.system_atom_nums = int(lines[1])

        #To record the entire system's coordinates
        self.coordinates = []
        for line in lines[2:-1]:
            line = line.strip().split('  ')#split into 5-6 items
            self.coordinates.append([float(i) for i in line[-3:]])

    def build_tkmsystem(self,gro_path:str, top_path:str):

        self.read_top_file(top_path)
        assert len(self.moleculetype) == len(self.moleculetype_num), 'Number of Moleculetypes in [ molecules ] Must Be Equal To Number of [ moleculetype ]'

        self.read_gro_file(gro_path)

        system = TinkerModellorSystem()
        #According to self.moleculetype to rebuild the Tinker XYZ format file
        for count in len(self.moleculetype_num):
            for i in int(self.moleculetype_num):
                system(self.coordinates,self.moleculetype[count],[system.AtomNums+1,system.AtomNums+self.moleculetype[count].AtomNums])

if __name__ == '__main__':
    new= tinkermodellor()
    new(r'/home/wayne/quanmol/TinkerModelling/tinkermodellor/gromacs.gro',r'/home/wayne/quanmol/TinkerModelling/tinkermodellor/gromacs.top')

