from ._gmxmolecule import GMXMolecule
from typing import List, Union
from ..para_trans.amoebabio18._forcefieldtrans import AmberGAFFTrans


class TinkerModellorSystem() :
        


    def __init__(self, aggressive:bool = True, name:str = None) -> None :
        """
        Used for store the molecule information (Tinker XYZ format)

        Args:
            aggressive(bool):   If true, scripts would try to pair more atom types,
                                and this may results mismatching
        """
        #Used for store the molecular type
        self.AtomTypes: list[str] = [None]
        #Used for store the molecular bond
        self.Bonds: Union[List[int], List[str]] = [None]
        #Used for store the molecule Numbers
        self.AtomNums: int = 0
        #Used for store the molecule coordinates
        self.AtomCrds: Union[List[float],List[str]] = [None]
        
        #Used for store the atomtype transformation (into AMEOBABIO18 force field)
        if aggressive == True:
            print('Aggressive mode is on, this may results atomtype mismatching')
        self.trans = AmberGAFFTrans(Aggressive=aggressive)

        #Set entire system's name
        if name == None:
            self.MoleculeName = 'TinkerModellor Default Name'

        else:
            if isinstance(name,str):
                self.MoleculeName = name
            else:
                raise TypeError('MoleculeName must be a string')
            
    def __call__(self, name: str ='TinkerModellor Default Name', 
                atomcrds: Union[List[float],List[str]] = None,
                molecule_class: GMXMolecule() = None,
                atom_index: list[int] = None) -> None :
        """
        Construct the Tinker XYZ format system
        Args:
            name(str):              The name of the system
            atomcrds(list):         The coordinates of the system
            molecule_class(GMXMolecule()):  The molecule class
            ato,_index(list):       The index of the atom in the system

        Returns:
            None
        """
        assert isinstance(molecule_class,GMXMolecule), 'molecule_class or molecule_index must be provided'
        assert isinstance(atom_index,list), 'molecule_class or molecule_index must be provided'
        assert isinstance(atomcrds,list), 'atomcrds must be a list'

        self._get_top_and_crd(molecule_class,atom_index,atomcrds)
        self._check_and_trans_atomtype()
       
    #Used for store each atom's atomtype, coordinates and topology
    def _get_top_and_crd(self, molecule_class: GMXMolecule(), molecule_index: list[int,int],atomcrds: Union[List[float],List[str]]) -> None :

        #Transfrom the atomtype into AMEOBABIO18 force field
        tinker_atomtype = []
        for element in molecule_class.AtomTypes:
            #DEBUG##print(element)
            trans_type = self.trans(element)
            if trans_type == 'None':
                raise ValueError(f'Atomtype {element} not found in force field')
            else:
                tinker_atomtype.append(self.trans(element))
        self.AtomTypes += tinker_atomtype

        #Transform the topology into Tinker XYZ format with atom index correction
        tinker_bonds = []
        #DEBUG##print(molecule_class.Bonds)
        for element in molecule_class.Bonds[1:]:
            #element might contain more than one bond,like [1,2,10]
            corrected_bond = []
            for number in element[1:]:
                corrected_bond.append([int(number)+int(self.AtomNums)]) 
            tinker_bonds.append(corrected_bond)
        self.Bonds += tinker_bonds

        #int(molecule_index[1])+1 : plus extra 1 is to make sure list contains the last index
        self.AtomCrds += atomcrds[int(molecule_index[0]):int(molecule_index[1])+1]
        
    def _check_and_trans_atomtype(self) -> None :

        #DEBUG##print(len(self.AtomTypes),len(self.AtomCrds),len(self.Bonds),self.AtomTypes[-1])
        assert len(self.Bonds) == len(self.AtomTypes) == len(self.AtomCrds), 'The length of Bonds, AtomTypes and AtomCrds must be equal !'

        #The first item of AtomTypes is None, so minus 1
        self.AtomNums = len(self.AtomTypes)-1