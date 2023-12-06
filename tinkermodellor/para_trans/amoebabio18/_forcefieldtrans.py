from ._water_ions_trans import WaterAndIonsForceField
from para_trans._abc import FroceFieldTrans
from ._gaff import GAFFForceField
from ._amberFF import AmberFF

class AmberGAFFTrans(FroceFieldTrans):
    
    def __init__(self,Aggressive:bool = True):
        """
        Force Field Transformation Dictionary Initialization

        Args:
            Aggressive(bool):   If true, scripts would try to pair more atom types,
                                and this may results mismatching

        Returns:
            
        """
        
        super().__init__()
        self.aggressive = Aggressive
        self.FFpara = {}
        supported_FFpara = [WaterAndIonsForceField.water_para,WaterAndIonsForceField.ion_para,GAFFForceField.gaff_para,AmberFF.amberff_para]
        
        for i in supported_FFpara:
            self.FFpara.update(i) 
        
        if self.aggressive:
            additional_FFpara = [GAFFForceField.unpair_gaff_para,AmberFF.unpair_amberff_para]
            for i in additional_FFpara : self.FFpara.update(i)
        

    def __call__(self, atom_type: str) -> str:
        return self._transform_to_tinker(atom_type,self.FFpara)        

    