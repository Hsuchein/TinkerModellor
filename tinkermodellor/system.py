import time
from _class._tkm_molecule import *
from para_trans.amoebabio18._forcefieldtrans import AmberGAFFTrans

class System():
    def __init__(self) -> None:
        self.trans = AmberGAFFTrans(Aggressive=True)
        self.describe = ''

    def ConstructSystemFromTopGro(self,top_file_path,gro_file_path):
        
        self.read_top_file(file_path=top_file_path)
        self.read_gro_file(File_path=gro_file_path)

    def save_as_Thinker_XYZ(self,file_path):

        index = 1
        self.atom_type_dict = {}
        self.system_atoms = {}
        current_index = 0

        for molecule_item in self.molecules:

            molecule,molecule_nums = self.molecules_dict[molecule_item],self.molecules[molecule_item]
            

            for _ in range(molecule_nums):
                

                for atom in molecule:

                    atom_index,atom_name,res_index,res_name,atom_type_in_res = atom[0]
                    connect = [i+current_index for i in atom[1]]

                    if len(connect) > 5:print(connect)

                    x,y,z = self.location[index-1]
                    
                    try : atom_type_in_FF = self.trans(atom_name)
                    
                    except : 
                        atom_type_in_FF = 'unc'
                        print('atomtype {} not found in force field'.format(atom_name))
                    
                    self.system_atoms[index] = (index,atom_name,x,y,z,atom_type_in_FF,connect)
                    
                    self.atom_type_dict[index] = atom_type_in_FF
                    
                    index += 1

                current_index += len(molecule)


        with open(file_path,'wt') as f:
            
            if self.describe == '' : self.describe = 'generate by tinkermodellor '+time.ctime().replace('  ',' ')

            f.write('{:>6}{:10}{:<}\n'.format(self.system_atoms_num,'',self.describe))

            for index in self.system_atoms:

                connect = self.connect_format(self.system_atoms[index][-1])
                
                index,atom_name,x,y,z,atom_type_in_FF = self.system_atoms[index][:-1]

                lines = '{0:>6}  {1:<6}{2:<12.6f}{3:<12.6f}{4:<12.6f}{5:>4}{6:}\n'.format(index,atom_name,x,y,z,atom_type_in_FF,connect)
                f.write(lines)


    def connect_format(self,connect:list):
        txt = ''
        for i in connect:
            txt += '{:>6}'.format(self.atom_type_dict[i])
        return txt

    def read_top_file(self,file_path:str):
        
        with open(file_path,'r') as f:#read top file
            lines=f.readlines()

        self.holding_pool = []
        temp_contain = []
        temp_discribe = []

        for line in lines:
            line = line.strip()

            if '[ moleculetype ]' in line or '[ molecules ]' in line or '[ exclusions ]' in line:#如果在这两行就更新并重置临时容器
                self.holding_pool.append(temp_contain)
                temp_contain = []
                temp_discribe = []
                continue

            if line :
                if line.startswith((';','#')) : temp_discribe.append(line)
                else : 
                    line = list(filter(None,line.split(' ')))
                    temp_contain.append(line) # skip empty line
        
        self.molecules = {}
        for i in temp_contain: # the last temp_contain is the [ molecules ] part
            self.molecules[i[0]] = int(i[1]) # record the molecules in the system

        self.molecules_dict = {}
        for i in self.holding_pool:
            if i[0][0] in self.molecules:
                molecule = self.molecules_dict[i[0][0]] = TinkerModellorMolecule()
                molecule.Construct_Molecule(i)
        
        del self.holding_pool

        self.system_atoms_num = 0
        for i in self.molecules:
            self.system_atoms_num += self.molecules_dict[i].atoms_nums*self.molecules[i]
        

    def read_gro_file(self,File_path):

        with open(File_path,'rt') as f:#read gro file
            lines = f.readlines()
            assert self.system_atoms_num == int(lines[1])

        self.location = []
        for line in lines[2:-1]:
            line = line.strip().split('  ')#split into 5-6 items
            self.location.append([float(i) for i in line[-3:]])





sys=System()
sys.ConstructSystemFromTopGro(top_file_path='tinkermodellor/gromacs.top',gro_file_path='tinkermodellor/gromacs.gro')
sys.save_as_Thinker_XYZ('tinkermodellor/gromacs.xyz')