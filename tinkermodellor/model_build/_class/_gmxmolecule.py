from typing import  List, Union

class GMXMolecule() :

    def __init__(self) -> None :
        #Used for store the molecule information

        #Used for store the molecular name
        self.MoleculeName = None
        #Used for store the molecular type
        self.AtomTypes: list[str] = []
        #Used for store the molecular bond
        self.Bonds: Union[List[int,int], List[str,str]] = []
        #Used for store the molecule Numbers
        self.AtomNums: int = 0
        #Used for store the molecule residue name
        self.AtomResidue: list[str] = []

    def __call__(self, name: str, 
                atomtypes: List[str],
                atomeresiudes: List[str],
                bonds: Union[List[int], List[str]]) -> None :
        """
        Construct the molecule

        Args:
            name(str):          The name of the molecule
            atomtypes(list):    The atom types of the molecule
            bonds(list):        The bonds of the molecule, used for determine the molecule's topology
            atomcrds(list):     The coordinates of the molecule

        Returns:
            None
        """
        self._get_moleculename(name)
        self._get_atomtypes_and_residues(atomtypes,atomeresiudes)
        self._get_bonds(bonds)
        self._check()

    def _get_moleculename(self, name: str) -> None :
        if isinstance(name,str):
            self.MoleculeName = name
        else:
            raise TypeError('MoleculeName must be a string')
        
    def _get_atomtypes_and_residues(self, atomtypes: List[str], atomresidues:List[str]) -> None :
        
        if isinstance(atomtypes,list):
            self.AtomTypes += atomtypes
            print(self.AtomTypes)
        else:
            raise TypeError('AtomTypes must be a string list')
        
        if isinstance(atomresidues,list):
            self.AtomResidue += atomresidues
        else:
            raise TypeError('AtomResidue must be a string list')
        
    def _get_bonds(self, bonds: Union[List[int], List[str]]) -> None :
        if isinstance(bonds,List):
            #create a list for each atom, the index is atom's index, the value is the index of the atom which is bonded to this atom
            list = [[[]] for _ in range(len(self.AtomTypes)+1)]
            print(len(self.AtomTypes))

            #take value from bonds(list), and use the value as the index of list, then append the index of the value to the list
            for i in range(len(bonds)):
                #DEBUG##print(bonds)
                #print(i)
                list[int(bonds[i][0])].append(int(bonds[i][1]))
                list[int(bonds[i][1])].append(int(bonds[i][0]))

            #store the list to self.Bonds
            #print(list)
            self.Bonds = list
        else:
            raise TypeError('Bonds must be a int or str list')

        
    def _check(self) -> None :
        assert len(self.Bonds) == len(self.AtomTypes)+1, f'The length of Bonds({len(self.Bonds)}), AtomTypes({len(self.AtomTypes)}) and AtomCrds must be equal !'
        self.AtomNums = len(self.AtomTypes)



        
