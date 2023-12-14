from tinkermodellor.model_build._tkm import TinkerModellor as tkm

if __name__ == '__main__':
    
    new= tkm()
    new(r'/media/wayne/datastorage/data/tinker/ncs/steep.gro',r'/media/wayne/datastorage/data/tinker/ncs/gromacs.top')
    new.write_tkmsystem(r'/media/wayne/datastorage/data/tinker/ncs/steep.xyz')