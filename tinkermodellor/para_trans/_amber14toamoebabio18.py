from ._abc import FroceFieldTrans
from ._water_ions_trans import WaterAndIonsForceField

class Amber14ToAmoebaBio18GMX(FroceFieldTrans):

    _water_dict = WaterAndIonsForceField.water_para
    _ion_dict = WaterAndIonsForceField.ion_para
    
    def __init__(self):
        super.__init__()
    
    def __call__(self, *args, **kwds):
        pass