from tinkermodellor import *




if __name__ == "__main__":
    sys=TinkerModellorSystem()
    sys.ConstructSystemFromTopGro(top_file_path='tinkermodellor/gromacs.top',gro_file_path='tinkermodellor/gromacs.gro')
    sys.save_as_Thinker_XYZ('gromacs.xyz')