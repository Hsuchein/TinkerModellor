from ._water_ions_trans import WaterAndIonsForceField
from tinkermodellor.para_trans._abc import FroceFieldTrans
from ._gaff import GAFFForceField
from ._amberFF import AmberFF

class AmberGAFFTrans(FroceFieldTrans):
    
    def __init__(self,Aggressive:bool = False):
        """Force Field Transformation Dictionary Initialization

        Args:
            Aggressive(bool):   If true, scripts would try to pair more atom types,
                                and this may results mismatching

        Returns:
            
        """
        
        super().__init__()
        
        self.FFpara = WaterAndIonsForceField.water_para + WaterAndIonsForceField.ion_para + GAFFForceField.gaff_para +AmberFF.amberff_para
        
        if Aggressive:
            self.FFpara += GAFFForceField.unpair_gaff_para + AmberFF.unpair_amberff_para
        

    def __call__(self, atom_type: str) -> str:
        return self._transform_to_tinker(atom_type , self.FFpara )        

    