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

## how to use

### 1. Terminal

you can run the executed file locally with the following command in the terminal.

```sh
    python tkm.py -loc loc_file -top top_file -out out_file [options]
```

#### options

- **-h** --help  
    show this help message and exit

- **-loc**  
    location_file  
    the path to the location_file of the system.  
    *[Support: Amber(.inpcrd),CHARMM(.crd),GROMACS(.gro)]*

- **-top**  
    topology_file  
    the path to the location of the top file of the system.  
    *[Support: Amber(.prmtop),CHARMM(.psf),GROMACS(.top)]*

- **-out**  
    out file path  
    take current time as default,  
    *[Default: "./sec_min_hour.xyz"]*  
    *[Format: tinker(.xyz)]*

- **--keep**  
    *Parmed* will transfer the input file,  
    it creates temporary files then removed,  
    you can choose True to keep it.  
    *[Default: False]*

- **--style {A,C,G}**  
    the style you create the system with,  
    *[Support:{A: Amber, C: CHARMM, G: GROMACS}]*  
    *[default: G]*

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
