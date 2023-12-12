from tinkermodellor.model_build._tkm import TinkerModellor as tkm

if __name__ == '__main__':
    
    new= tkm()
    new(r'/home/wayne/quanmol/TinkerModelling/tinkermodellor/gromacs.gro',r'/home/wayne/quanmol/TinkerModelling/tinkermodellor/gromacs.top')
    new.write_tkmsystem(r'/home/wayne/quanmol/TinkerModelling/gromacs.xyz')