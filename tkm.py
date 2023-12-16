from tinkermodellor.model_build._tkm import TinkerModellor
import argparse
import os
import parmed as pmd
import time

if __name__ == '__main__':
    description = 'TinkerModellor contribute to import larger system into tinker'
    usage = 'python tkm.py -loc loc_file -top top_file -out out_file [options]'
    
    parser = argparse.ArgumentParser(description=description, usage=usage,formatter_class=argparse.RawTextHelpFormatter,)
    
    parser.add_argument('-loc',
                        type = str,
                        help ='location_file\nthe path to the location_file of the system.\n[Support: Amber(.inpcrd),CHARMM(.crd),GROMACS(.gro)]',
                        required = True)
    
    parser.add_argument('-top',
                        type = str,
                        help = 'topology_file\nthe path to location top file of the system.\n[Support: Amber(.prmtop),CHARMM(.psf),GROMACS(.top)]', 
                        required = True)
    
    parser.add_argument('-out', 
                        type = str,
                        default= os.path.join(os.getcwd(),time.ctime().split(' ')[-2].replace(':','_')+'.xyz'),
                        help = 'outfile\ntake current time as default,\n[Default: "./sec_min_hour.xyz"]\n[Format: tinker(.xyz)]', 
                        )
    
    parser.add_argument('--keep', 
                        type = bool,
                        default = False,
                        help = 'keep\nParmed will transfer the input file,\nit creates temporary files then removed,\nyou can choose True to keep it\n[Default: False]', 
                        )
    
    parser.add_argument('--style',
                        type = str,
                        choices = ['A','C','G'],
                        default = 'G' ,
                        help = 'style\nthe style you create the system with ,\n{A: Amber, C: CHARMM, G: GROMACS}\n[default: G]', 
                        )
    
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