from tinkermodellor.model_build.tinkermodellor import tinkermodellor

if __name__ == '__main__':
    
    new= tinkermodellor()
    new(r'/home/wayne/quanmol/TinkerModelling/tinkermodellor/gromacs.gro',r'/home/wayne/quanmol/TinkerModelling/tinkermodellor/gromacs.top')
    new.write_tkmsystem(r'/home/wayne/quanmol/TinkerModelling/gromacs.xyz')