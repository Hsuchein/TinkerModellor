import time
import os
from _tkm_molecule import *


class TinkerModellorSystem():
    
    '''
    This is the aggregation class for TinkerModellor ,which concat all information extract from top and gro(gmx)
    use ConstructSystemFromTopGro to init a system
    use save_as_Thinker_XYZ to create a xyz file
    '''

    def __init__(self,transfer_module) :
        #need to init!
        self.trans = transfer_module()
        self.describe = ''


    def ConstructSystemFromTopGro(self,top_file_path:str,gro_file_path:str,structure_model:str="gmx"):

        assert os.path.exists(top_file_path) , 'FileNotFoundError '+top_file_path+' not exist,current path is '+os.getcwd()
        assert os.path.exists(gro_file_path) , 'FileNotFoundError '+gro_file_path+' not exist,current path is '+os.getcwd()
        
        self.read_top_file(file_path=top_file_path)
        self.read_gro_file(File_path=gro_file_path)

    def save_as_Thinker_XYZ(self, file_path):
        """
        This function saves the system as a Thinker XYZ file.

        :param file_path: The path to the output file.
        """
        # Initialize dictionaries and sets to store data
        index =  1
        self.atom_type_dict = {}
        self.system_atoms = {}
        self.missing_pool = set()
        current_index = 0

        # Iterate through each molecule in the system
        for molecule_item in self.molecules:

            # Get the molecule and its number of instances
            molecule, molecule_nums = self.molecules_dict[molecule_item], self.molecules[molecule_item]

            # Iterate through each instance of the molecule
            for _ in range(molecule_nums):

                # Iterate through each atom in the molecule
                for atom in molecule:

                    # Get the atom index, name, residue index, residue name, and atom type in the residue
                    atom_index, atom_name, res_index, res_name, atom_type_in_res = atom[0]

                    # Get the connectivity of the atom
                    connect = [i + current_index for i in atom[1]]

                    # If the number of connections is greater than 5, print the connectivity list
                    if len(connect) > 5:
                        print(connect)

                    # Get the coordinates of the atom
                    x, y, z = self.location[index - 1]

                    # Translate the atom name to the corresponding atom type in the force field
                    try:
                        atom_type_in_FF = self.trans(atom_name)
                    except:
                        atom_type_in_FF = 'unc'
                        self.missing_pool.add(atom_name)

                    # Add the atom to the system_atoms dictionary
                    self.system_atoms[index] = (index, atom_name, x, y, z, atom_type_in_FF, connect)

                    # Add the atom type to the atom_type_dict
                    self.atom_type_dict[index] = atom_type_in_FF

                    # Increment the index
                    index += 1

                # Increment the current index by the number of atoms in the molecule
                current_index += len(molecule)

        # Print a list of missing atom types in the force field
        for i in self.missing_pool:
            print('atomtype {} not found in force field'.format(i))

        # Write the Thinker XYZ file
        with open(file_path, 'wt') as f:
            if self.describe == '':
                self.describe = 'generate by tinkermodellor ' + time.ctime().replace('  ', ' ')

            f.write('{:>6}{:10}{:<}\n'.format(self.system_atoms_num, '', self.describe))

            # Iterate through each atom in the system_atoms dictionary
            for index in self.system_atoms:

                # Get the connectivity of the atom
                connect = self.connect_format(self.system_atoms[index][-1])

                # Get the index, atom name, and coordinates of the atom
                index, atom_name, x, y, z, atom_type_in_FF = self.system_atoms[index][:-1]

                # Write the atom to the Thinker XYZ file
                lines = '{0:>6}  {1:<6}{2:<12.6f}{3:<12.6f}{4:<12.6f}{5:>4}{6:}\n'.format(index, atom_name, x, y, z, atom_type_in_FF, connect)
                f.write(lines)

        print('create xyz at ', os.path.abspath(file_path))


    def connect_format(self,connect:list):
        txt = ''
        for i in connect:
            txt += '{:>6}'.format(self.atom_type_dict[i])
        return txt

    def read_top_file(self, file_path: str):
        """
        This function reads a topology file and processes the information to store it in the class variables.

        :param file_path: The path to the topology file.
        """
        # Open the file for reading
        with open(file_path, 'r') as f:
            lines = f.readlines()

        # Initialize class variables
        self.holding_pool = []
        temp_contain = []
        temp_discribe = []

        # Iterate through the lines in the file
        for line in lines:
            line = line.strip()

            # Check if the line is part of the [moleculetype], [molecules], or [exclusions] section
            if '[ moleculetype ]' in line or '[ molecules ]' in line or '[ exclusions ]' in line:
                # If so, add the current temp_contain and temp_discribe to the holding_pool
                self.holding_pool.append(temp_contain)
                temp_contain = []
                temp_discribe = []
                continue

            # If the line is not empty or commented, process it
            if line:
                if line.startswith((';', '#')):
                    temp_discribe.append(line)
                else:
                    # Split the line into a list and skip empty elements
                    line = list(filter(None, line.split(' ')))
                    temp_contain.append(line)

        # The last temp_contain is the [molecules] section, so store the molecules in the system
        self.molecules = {}
        for i in temp_contain:
            self.molecules[i[0]] = int(i[1])

        # Initialize a dictionary to store the molecules
        self.molecules_dict = {}
        for i in self.holding_pool:
            if i[0][0] in self.molecules:
                molecule = self.molecules_dict[i[0][0]] = TinkerModellorMolecule()
                molecule.Construct_Molecule(i)

        # Remove the holding_pool to free up memory
        del self.holding_pool

        # Calculate the total number of atoms in the system
        self.system_atoms_num = 0
        for i in self.molecules:
            self.system_atoms_num += self.molecules_dict[i].atoms_nums * self.molecules[i]
        

    def read_gro_file(self, File_path):
        '''
        This function reads a .gro file and stores the coordinates of the system's atoms in the 'location' attribute.

        param: File_path: The path to the .gro file to be read.
        type: File_path: str
        return: None
        '''

        # Open the file in read text mode and read its lines
        with open(File_path, 'rt') as f:
            lines = f.readlines()

        # Check if the number of atoms in the file matches the expected number of atoms
        assert self.system_atoms_num == int(lines[1])

        # Initialize an empty list to store the coordinates of the system's atoms
        self.location = []

        # Iterate through the lines of the file starting from the third line (excluding the first two lines and the last line)
        for line in lines[2:-1]:
            # Split the line into a list of items, removing any extra whitespace
            line = line.strip().split('  ')

            # Append the last three items of the list (i.e., the x, y, and z coordinates) to the 'location' list as floats
            self.location.append([float(i) for i in line[-3:]])





