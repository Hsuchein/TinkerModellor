# TinkerModelling

## Badges

![(Build/Test Status)](Tests/badge.svg)  
**[need to be append after finishing pytest]**

## Description

text  
**[needs to be written]**

## Installation

### System Requirements

- Python 3.6+

### Methods  

There are several ways to install TinkerModelling.

- download the zip file from the repository and extract it. open the terminal and go to the folder where you extracted the zip file. then run the code below in the terminal.

```sh
python ./setup.py install
```

- open the terminal and then use the code below to clone this git and then use setup.py to install.
  
```sh
git clone https://github.com/Hsuchein/TinkerModellor.git
cd TinkerModellor
python ./setup.py install
```

- open the terminal and then use the code below to download via pip.

``` sh
pip install tinkermodelling
```

## Testing

To automatically run the TinkerModelling tests, execute the following code in the terminal:

``` sh
pytest test
```

## how to use

### 1. Terminal

you can run the executed file locally with the following command in the terminal.

```sh
    python tkm.py -l location_file -t topology_file -o 
    outfile_name -k [True/False] -p [CHARMM/GROMACS/AMBER]
```

#### options

- **-h** --help  

    show this help message and exit

- **-l** LOCATION_FILE, **--location_file** LOCATION_FILE  

    location_file , the path to the location_file of the system.  

    *Support:* AMBER(.inpcrd),CHARMM(.crd),GROMACS(.gro)

- **-t** TOPOLOGY_FILE, **--topology_file** TOPOLOGY_FILE  

    topology_file, the path to the location of the top file of the system.  

    *Support:* AMBER(.prmtop),CHARMM(.psf),GROMACS(.top)

- **-o** OUTFILE, **--outfile** OUTFILE  

    out file path, take current paths concat time as default, as './sec_min_hour.xyz'.

    *Format:* TINKER(.xyz)

- **-k** KEEP, **--keep** KEEP  

    *Parmed* will read the input file and then transfer it, which will create two temporary files and will be removed automatically, you can choose whether to keep it.

    *Support:* True/False

- **-p** {AMBER,CHARMM,GROMACS}, **--program** {AMBER,CHARMM,GROMACS}

    the program you create the system with, the default is GROMACS.

    *Support:* AMBER/CHARMM/GROMACS

### 2. Python API

you can  use *TinkerModelling* as a lib too.

``` python
import tinkermodellor as tkm
new= tkm()
new('gromacs.gro','gromacs.top')
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

If you use this software in your research, you can cite the following paper:  

**[need to be append]**

## Reference

**Parmed**  <https://github.com/ParmEd/ParmEd>
