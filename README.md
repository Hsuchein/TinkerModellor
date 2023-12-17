# TinkerModelling

## Description

text

## Installing TinkerModelling

Firstly, you can to download it through git or zip file
``` sh
# in terminal
git clone git@github.com:Hsuchein/TinkerModellor.git
```
.Then go into the TinkerModellor folder, construct environment for TinkerModellor by conda
``` sh
cd TinkerModellor.
conda env create -n TinkerModellor -f env.yml
conda activate TinkerModellor
```

Additionally, TinkerModellor is based on ParmEd programme. Hence, you also need to install ParmEd
``` sh
git clone git@github.com:ParmEd/ParmEd.git
cd ParmEd
pip install .
```
Ultimately, install the TinkerModellor
``` sh
cd TinkerModellor
pip install .
```

## Testing ParmEd

all the code based on python above 3.6

In order to automatically run the TinkerModelling tests, execute the following:

``` sh
# in terminal
## Testing TinkerModelling
pytest test
```

## how to use

you can run the excute file locally with the following command in cmd

```sh
# in cmd
python tkm.py -g gro_file -t top_file -o 
outfile_name -k [True/False] -p [CHARMM/GROMACS]
```

**Paras:**  

for *GROMACS_FILE* :  
**-p** GROMACS  
**-g** gro_file_path  
**-t** top_file_path  
**-o** outfile_name

for *CHARMM_FILE* :  

**-p** CHARMM  
Parmed is prepared to transfer the *CHARMM_FILE* into temporary *GROMACS_FILE*  
**-t** prmtop_file  
**-g** crd_file  
**-k** [True/False]  
you can set parameter **k** to decide whether keeping the temporary files or not.  

or you can run the following command in cmd to use **TinkerModelling** as a lib

``` sh
# in cmd
pip install tinkermodellor
```

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

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following
disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following
disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote
products derived from this software without specific prior written permission.

see more information in the license file.

## Citation

If you use this software in your research, you can cite the following paper:  
**ref**

## Reference

**Parmed**  <https://github.com/ParmEd/ParmEd>
