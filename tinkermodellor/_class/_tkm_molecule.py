from _tkm_atom import *

class TinkerModellorMolecule() :
    "This is a class for TinkerModellorMolecule , unsupported External calls"

    def __init__(self) -> None :
        self.molecule_name = 'mismatch_or_raw'
        self.atoms_nums = 0
        self.index = 0
        pass

    def Construct_Molecule(self,Top_moleculetype_info:list) :
        '''

        this is a inner_built methods,initial a TinkerModellorMolecule item from 
        a processed top_moleculetype item,which is donated as a list contain all
        lines between two '[ moleculetype ]' line,this information will be extracted:

        'molecule_name', <class 'str'>      atom_name recorded in top file

        'atoms_nums', <class 'int'>         atoms number in molecule  

        'index', <class 'int'>              current iter index for global usage , will return the atoms[index]  

        'part_dict', <class 'dict'>         raw data readed from top file , allow {part_name:information_list}  

        'atoms', <class 'dict'>             all the atoms in the molecule ,allow {atom_A:atom_index_in_molecule,atom_name,res_index,res_name,atom_type_in_res}  

        'bonds', <class 'dict'>             connect between atoms , allow {atom_A:[atom_B,atom_C,atom_D]}  

        Returns:
            None
   
        '''
        
        self.molecule_name = Top_moleculetype_info[0][0]
        self.part_dict = {}
        part_name = ''
        

        for i in Top_moleculetype_info[1:] : 
            
            if i[0] in '[' : # take [ xxxx ] as parts to devide the molecule class
                part_name = i[1]
                self.part_dict[part_name] = []
                continue

            self.part_dict[part_name].append(i)

        # part_dict :
        # {str[part] : list[lines]}
        
        #atoms
        self.atoms = {} 
        for i in self.part_dict['atoms'] :
            self.atoms[int(i[0])] = i[0:5]
        self.atoms_nums = len(self.atoms)

        #bonds
        #ions usually have no [ bonds ] part , set as empty list
        if 'bonds' not in self.part_dict : self.part_dict['bonds'] = []
        
        #create a dict {int[AIIM] : list[]} for all atoms in self.atoms
        self.bonds = dict( (i,[]) for i in range(1,len(self.atoms)+1) )
        
        #update both sides
        for i in self.part_dict['bonds'] :
            
            atom_A = int(i[0])
            atom_B = int(i[1])

            self.bonds[atom_A].append(atom_B)
            self.bonds[atom_B].append(atom_A)

    def __iter__(self) :
        return self
    
    def __next__(self) :
        if self.index == self.atoms_nums :
            self.index = 0
            raise StopIteration
        else :
            self.index += 1
            return [self.atoms[self.index],self.bonds[self.index]]

    def __getitem__(self,key:int) :
        return TinkerModellorAtom(self.atoms[key])

    def __len__(self) :
        return self.atoms_nums


    def __str__(self) -> str:
        return 'molecule_name:{},atoms_num:{}'.format(self.molecule_name,self.atoms_nums)

    def __repr__(self) -> str:
        return 'molecule_name:{},atoms_num:{}'.format(self.molecule_name,self.atoms_nums)



        