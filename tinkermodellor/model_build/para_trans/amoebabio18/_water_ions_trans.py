class WaterAndIonsForceField:
    
    '''
    Only support TIP3P water model, SPCE water model and SPC water model now.
    '''
        
    water_para = {
    'OW':349,
    'HW':350,
    'OW_spc':349,
    'HW_spc':350,
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
    'Na+':352,
    'Cl-':363,
    }
