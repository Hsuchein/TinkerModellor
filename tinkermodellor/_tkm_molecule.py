class TinkerModellorMolecule() :

    def __init__(self) -> None :
        self.molecule_name = 'mismatch_or_raw'
        self.atoms_nums = 0
        pass

    def Construct_Molecule(self,Top_moleculetype_info:list) :
        '''
        this is a inner_built methods,initial a TinkerModellorMolecule item from 
        a processed top_moleculetype item,which is donated as a list contain all
        lines between two '[ moleculetype ]' line,this information will be extracted:
        ## atom information --> self.atoms[dict]:
        {int[atom_index_in_molecule(AIIM)]:list[str[AIIM],str[atom_type],str[residue_index],str[residue],str[atom_type_in_residue]]}
        ## bonds(topology) --> self.bonds[dict]:
        {int[AIIM]:list[int[connected_AIIM],...]}
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

    def __str__(self) -> str:
        return 'molecule_name:{},atoms_num:{}'.format(self.molecule_name,self.atoms_nums)

    def __repr__(self) -> str:
        return 'molecule_name:{},atoms_num:{}'.format(self.molecule_name,self.atoms_nums)



        
