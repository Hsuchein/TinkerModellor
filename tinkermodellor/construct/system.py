from read_top import Top
from read_gro import Gro

class ConstructSystemFromTopGro():
    def __init__(self,top_file_path,gro_file_path,ifdef_in_top='NORMAL') -> None:
        self.top=Top(file_path=top_file_path,ifdef=ifdef_in_top)
        self.gro=Gro(file_path=gro_file_path)
        self.match()
        
    def match (self):
        "match top atoms with gro locations"
        self.atoms = self.top.data['[ atoms ]']
        self.atoms['identifier'] =self.atoms['atom']+self.atoms['nr']
        self.atoms['locations'] = self.atoms['identifier'].apply(lambda x: self.gro.location[x])
        print(self.atoms)

sys=ConstructSystemFromTopGro(top_file_path='./topol.top',gro_file_path='./cg.gro')