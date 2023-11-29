class Gro():
    def __init__(self,file_path):

        with open(file_path,'rt') as f:
            self.file = f.readlines()
            first_line = self.file[0].strip().split('   ')
        
        self.date , self.system = first_line[0], first_line[1]

        self.location = {}

        for i in self.file[2:-1]:
            line = i.strip().split('  ')
            identifier = ''.join([str(i) for i in line[1:-3]]).strip().replace(' ', '')
            self.location[identifier] = [float(i) for i in line[-3:]]
