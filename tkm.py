from tinkermodellor.model_build._tkm import TinkerModellor
import argparse
import os
import parmed as pmd
import time

if __name__ == '__main__':
    print('\n')

    description = 'TinkerModellor: A complicated biological system construction tool for Tinker Simulation Programme'
    usage = 'python tkm.py -c coordination_file -p topology_file -out output_file [options]'
    
    parser = argparse.ArgumentParser(description=description, usage=usage,formatter_class=argparse.RawTextHelpFormatter,)
    
    parser.add_argument('-c',
                        type = str,
                        help ='Coordination_file\nthe path to the coordination file of the system.\n[Support: Amber(.inpcrd/.crd),CHARMM(.crd),GROMACS(.gro)]',
                        required = True)
    
    parser.add_argument('-p',
                        type = str,
                        help = 'Topology_file\nthe path to the topology file of the system.\n[Support: Amber(.prmtop/.top),CHARMM(.psf),GROMACS(.top)]', 
                        required = True)
    
    parser.add_argument('-o', 
                        type = str,
                        default= os.path.join(os.getcwd(),'/TinkerModellor.xyz'),
                        help = 'Output_file\nthe path or name of output file,\n[Default: "./sec_min_hour.xyz"]\n[Format: tinker(.xyz)]', 
                        )
    
    parser.add_argument('-k', 
                        type = bool,
                        default = False,
                        help = 'Keep\nParmed will transformate the input file into GROMACS format,\nit would create temporary files then removed,\nyou can set True to keep it\n[Default: False]', 
                        )
    
    parser.add_argument('-f',
                        type = str,
                        choices = ['A','C','G'],
                        default = 'G' ,
                        help = 'Format\nthe the format of input file system with ,\n{A: Amber, C: CHARMM, G: GROMACS}\n[default: G]', 
                        )
    
''' 
    top_file = '/home/wayne/quanmol/TinkerModellor/test/dataset/1BHZ/gromacs.top'
    gro_file = '/home/wayne/quanmol/TinkerModellor/test/dataset/1BHZ/gromacs.gro'
    out_file = '/home/wayne/quanmol/TinkerModellor/tinker.xyz'
    tkm= TinkerModellor()
    tkm(top_file=top_file,gro_file=gro_file)
    tkm.write_tkmsystem(xyz_path=out_file)



'''  
    args = parser.parse_args()
    top_file = args.Topology_file
    gro_file = args.Coordination_file
    out_file = args.Output_file
    keep = args.Keep
    program = args.Format
    
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
 

