class WaterAndIonsForceField:
    
    '''
    Only support TIP3P water model, SPCE water model and SPC water model now.
    '''
        
    water_para = {
    'OW':90,
    'HW':91,
    'OW_spc':90,
    'HW_spc':91,
    }

    ion_para = {
    'C0':99,              
    'Cl':104,
    'Na':93, 
    'MG':98, 
    'K':94, 
    'Rb':95,
    'Cs':96,
    'Li':92,
    'Zn':102,
    'Na+':93,
    'Cl-':104,
    }