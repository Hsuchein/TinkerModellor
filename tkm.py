from tinkermodellor.model_build._tkm import TinkerModellor
import argparse
import os
import parmed as pmd
import time

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='command line for tinkermodellor', formatter_class=argparse.RawTextHelpFormatter)
    
    parser.add_argument('-l','--location_file',
                        type = str,
                        help ='location_file , the path to the location_file of the system.Support: Amber(.inpcrd),CHARMM(.crd),GROMACS(.gro)',
                        required = True)
    
    parser.add_argument('-t','--topology_file', 
                        type = str,
                        help = 'topology_file,the path to location top file of the system.Support: Amber(.prmtop),CHARMM(.psf),GROMACS(.top)', 
                        required = True)
    
    parser.add_argument('-o','--outfile', 
                        type = str,
                        default= os.path.join(os.getcwd(),time.ctime().split(' ')[-2].replace(':','_')+'.xyz'),
                        help = 'out file path , take current paths concat time as default , as "./sec_min_hour.xyz",Format: tinker(.xyz)', 
                        )
    
    parser.add_argument('-k','--keep', 
                        type = bool,
                        default = False,
                        help = 'Parmed will read the input file and then trans it , which will create two temporary file and will be removed automaticly , you can chioce whether to keep it ', 
                        )
    
    parser.add_argument('-p','--program', 
                        type = str,
                        choices = ['AMBER','CHARMM','GROMACS'],
                        default = 'GROMACS' ,
                        help = 'the program you create the system with , default is GROMACS.', 
                        )
    

    top_file = '/home/wayne/quanmol/TinkerModellor/test/dataset/1BHZ/gromacs.top'
    gro_file = '/home/wayne/quanmol/TinkerModellor/test/dataset/1BHZ/gromacs.gro'
    out_file = '/home/wayne/quanmol/TinkerModellor/tinker.xyz'
    tkm= TinkerModellor()
    tkm(top_file=top_file,gro_file=gro_file)
    tkm.write_tkmsystem(xyz_path=out_file)



'''  
    args = parser.parse_args()
    top_file = args.topology_file
    gro_file = args.location_file
    out_file = args.outfile
    keep = args.keep
    program = args.program
    
    if program == 'GROMACS' :

        tkm= TinkerModellor()
        tkm(top_file=top_file,gro_file=gro_file)
        tkm.write_tkmsystem(xyz_path=out_file)

    if program == 'CHARMM' or program == 'AMBER' :

        charmm = pmd.load_file(args.topology_file,args.location_file)
        charmm.save('./temp.gro')
        charmm.save('./temp.top')

        tkm= TinkerModellor()
        topology_file = './temp.top'
        location_file = './temp.gro'
        tkm(topology_file=top_file,gro_file=location_file)
        tkm.write_tkmsystem(xyz_path=out_file)

        if args.keep == False:
            os.remove('./temp.gro')
            os.remove('./temp.top')
'''  

