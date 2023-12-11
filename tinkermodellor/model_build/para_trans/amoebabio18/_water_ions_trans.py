class WaterAndIonsForceField:
    
    '''
    Only support TIP3P water model, SPCE water model and SPC water model now.
    '''
        
    water_para = {
    'OW':82,
    'HW':11,
    'OW_spc':82,
    'HW_spc':11,
    }

    ion_para = {
    'C0':200,              
    'Cl':170,
    'Na':110, 
    'MG':120, 
    'K':190, 
    'Rb':370,
    'Cs':550,
    'Li':30,
    'Zn':300,
    'Na+':110,
    'Cl-':170,
    }