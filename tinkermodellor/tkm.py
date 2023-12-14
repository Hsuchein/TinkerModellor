from tinkermodellor.model_build.tinkermodellor import tinkermodellor
import argparse
import os
import parmed as pmd
import time

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='command line for tinkermodellor', formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('--grofile',
                        '-g', 
                        type = str,
                        help = 'grofile,the path to gro file you want to process , prmtop when program is CHARMM',
                        required = True)

    parser.add_argument('--topfile', 
                        '-t', 
                        type = str,
                        help = 'topfile,the path to top file you want to process,which should be ralted to gro file , inpcrd when program is CHARMM', 
                        required = True)

    parser.add_argument('--outfile', 
                        '-o', 
                        type = str,
                        default= os.path.join(os.getcwd(),time.ctime().split(' ')[-2].replace(':','_')+'.xyz'),
                        help = 'out file path , take current paths concat time as default', 
                        )

    parser.add_argument('--keep', 
                        '-k', 
                        type = bool,
                        default = False,
                        help = 'if the file create by CHARMM , Parmed will be operated to trans the file , which will create a temporary file and will be removed automaticly , you can chioce whether to keep it', 
                        )

    parser.add_argument('--program', 
                        '-p', 
                        type = str,
                        choices = ['AMBER','CHARMM'],
                        default = 'A',
                        help = 'project,the program you creat the file before', 
                        )

    args = parser.parse_args()
    top_file = args.topfile
    gro_file = args.grofile
    out_file = args.outfile
    keep = args.keep
    program = str(args.program[0]).upper()

    if program == 'A':

        tkm= tinkermodellor()
        tkm(top_file=top_file,gro_file=gro_file)
        tkm.write_tkmsystem(xyz_path=out_file)

    if program == 'C':

        charmm = pmd.load_file(args.topfile,args.grofile)
        charmm.save('./temp.gro')
        charmm.save('./temp.top')

        tkm= tinkermodellor()
        top_file = './temp.top'
        gro_file = './temp.gro'
        tkm(top_file=top_file,gro_file=gro_file)
        tkm.write_tkmsystem(xyz_path=out_file)

        if args.keep == False:
            os.remove('./temp.gro')
            os.remove('./temp.top')