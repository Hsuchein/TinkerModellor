import pandas
import sys
import os

class Top():

    def __init__(self,file_path:str,ifdef):
        self.ifdef = ifdef
        self.include = set()
        self.read_top_file(file_path)
        self.sort_readed()
        print(f'file in {self.include} are included')
        self.process_include()
        pass

    def read_top_file(self,file_name:str,return_split=False):
        
        with open(file_name,'r') as f:
            lines=f.readlines()
            lines[0] = '\n'
        
        self.part={}
        part_name=''
        n=0
        
        for i in lines:

            n+=1
            if i.startswith('\n'):
                part_name=lines[n].strip()
                self.part[part_name]=list()
                continue

            i = i.strip()

            i=list(filter(None,i.split(' ')))
            tem_text=self.part[part_name]
            tem_text.append(i)
            self.part[part_name]=tem_text

        del self.part['']

        if return_split : print('whole file was divide into',*self.part.keys(),sep='\n')

    def sort_readed(self):

        tem_include=set()
        tem_discribe=[]
        self.data={}
        self.system = self.part.pop('[ system ]')

        for i in self.part:

            if self.ifdef in self.part[i][0]:

                [tem_include.add(eval(i[1])) for i in self.part[i][1:-1] if i[0]=='#include']
                
                continue
            
            elif i.startswith(';'):

                tem_discribe+=self.part[i]
                if self.part[i][1][0]=='#include':
                    tem_include.add(eval(self.part[i][1][1]))

                continue
            
            elif i.startswith('#'):continue
            else :
                len_limit = len(self.part[i][2])
                data = [i[:len_limit] for i in self.part[i][2:] if ';' not in i[0]]
                columns=[i for i in self.part[i][1][1:] if '(' not in i][:len_limit]
                try:self.data[i]=pandas.DataFrame(data,columns=columns)
                except:print('error in',i,data[0],columns)


        self.discribe = [' '.join(list(filter(None,i))).removeprefix(';\t') for i in tem_discribe if '\t' in i[0]]
        
        for i in tem_include:
            i=i.split('/')[-1]
            self.include.add(i)
        
        del self.part

    def process_include(self,prepared_itp_path='./amber14sb_parmbsc1.ff'):
        prepared_itp_files=os.listdir(prepared_itp_path)+os.listdir('./')
        for i in self.include:
            if i in prepared_itp_files:print('processing',i)
            else:raise Exception('file',i,'not found')



                    
    
