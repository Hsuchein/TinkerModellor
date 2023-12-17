# TinkerModelling

## Description

text  
**[needs to be written]**

## Installation

### System Requirements

- Python 3.9+

### Methods  

There are several ways to install TinkerModelling.

- download the zip file from the repository and extract it. open the terminal and go to the folder where you extracted the zip file. then run the code below in the terminal.

```sh
python ./setup.py install
pip install -r requirements.txt
```

- open the terminal and then use the code below to clone this git and then use setup.py to install.
  
```sh
git clone https://github.com/Hsuchein/TinkerModellor.git
cd TinkerModellor
python ./setup.py install
```

- open the terminal and then use the code below to download via pip.

``` sh
pip install tinkermodellor parmed numpy
```

## Testing

To automatically run the TinkerModelling tests, execute the following code in the terminal:

``` sh
pytest test
```

## Usage

### Command Line Usage

#### The general usage of the command is as follows:
``` python
python tkm.py -c coordination_file -p topology_file -out output_file [options]
```

#### Arguments
-c: Path to the coordination file. Supported formats: Amber(.inpcrd/.crd), CHARMM(.crd), GROMACS(.gro). This argument is required.
-p: Path to the topology file. Supported formats: Amber(.prmtop/.top), CHARMM(.psf), GROMACS(.top). This argument is required.
-o: Output file path or name. Default is "./TinkerModellor.xyz". The format is tinker(.xyz).
-k: Option to keep temporary files created during GROMACS format conversion. Set to True to keep. Default is False.
-f: Input file format. Options: {A: Amber, C: CHARMM, G: GROMACS}. Default is GROMACS.
-a: Aggressive atomtype matching mode. May result in atomtype mismatching but can match irregular atomtypes. Default is True.

#### Example
Here is an example of how to use the command:
``` python
python tkm.py -c my_coordination_file.gro -p my_topology_file.top -o my_output_file.xyz -f G -a True
```
This command will run the TinkerModellor with a GROMACS coordination file my_coordination_file.gro and topology file my_topology_file.top, and it will output the result to my_output_file.xyz. The input file format is set to GROMACS, and the aggressive atomtype matching mode is enabled

### Packge Usage

``` python
# in python
import tinkermodellor as tkm
new= tkm()
new('gromacs.gro',gromacs.top')
new.write_tkmsystem('gromacs.xyz')
```

## Authors and Contributors

The following people have contributed directly to the coding and validation efforts in Tinkermodellor. And a special thanks to all of you who helped improve this project either by providing feedback, bug reports, or other general comments!

Xujian Wang |   <Hsuchein0126@outlook.com>

Haodong Liu |   <haodonliu@foxmail.com>

## License

**it under the terms of the BSD 3-Clause License** Redistribution and use in source and binary forms, with or without modification, are permitted provided that the
following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions, and the following
disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions, and the following
disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote
products derived from this software without specific prior written permission.

see more information in the license file.

## Citation

Please site the website if you use this software in your research:
<https://github.com/Hsuchein/TinkerModellor>

## Reference

**Parmed**  <https://github.com/ParmEd/ParmEd>
