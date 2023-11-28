from ._water_ions_trans import WaterAndIonsForceField
from tinkermodellor.para_trans._abc import FroceFieldTrans
from ._gaff import GAFFForceField

class Amber14SBGAFFTrans(FroceFieldTrans):
    waterpara = WaterAndIonsForceField.water_para
    ionpara = WaterAndIonsForceField.ion_para

    
    def __init__(self,Aggressive:bool = False):
        """Force Field Transformation Dictionary Initialization

        Args:
            Aggressive(bool):   If true, scripts would try to pair more atom types,
                                and this may results mismatching

        Returns:
            
        """
        
        super().__init__()
        
        self.FFpara = WaterAndIonsForceField.water_para + WaterAndIonsForceField.ion_para + GAFFForceField.gaff_para
        
        if Aggressive:
            self.FFpara += GAFFForceField.unpair_gaff_para
        

    def __call__(self, atom_type: str) -> str:
        return self._transform_to_tinker(atom_type , self.FFpara )        

    