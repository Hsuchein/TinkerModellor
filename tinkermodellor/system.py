from _tkm_molecule import *

class System():
    def __init__(self) -> None:
        self.prepared_itp_path = 'data/para/gromacs/amber14sb_parmbsc1.ff'

    def ConstructSystemFromTopGro(self,top_file_path,gro_file_path):
        
        self.read_top_file(file_path=top_file_path)
        self.read_gro_file(File_path=gro_file_path)


        


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
        for i in temp_contain:#the last temp_contain is the [ molecules ] part
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
        

    def read_gro_file(self,File_path,Aggressive = False):

        with open(File_path,'rt') as f:#read gro file
            lines = f.readlines()
            assert self.system_atoms_num == int(lines[1])
        
        self.identifier_res_location = []

        self.location = []
        for line in lines[2:-1]:
            line = line.strip().split('  ')#split into 5-6 items
            self.location.append([float(i) for i in line[-3:]])





sys=System()
sys.ConstructSystemFromTopGro(top_file_path='tinkermodellor/gromacs.top',gro_file_path='tinkermodellor/gromacs.gro')