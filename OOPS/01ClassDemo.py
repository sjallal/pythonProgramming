class Computer:
    def __init__(self, name, os, mem, ram):
        self.name = name
        self.os = os
        self.mem = mem
        self.ram = ram
    def getInfo(self):
        print('name of the Computer is: ',self.name)
        print('os is: ',self.os)
        print('memeory is: ',self.mem)
        print('ram is: ',self.ram)
comp1 = Computer('hp', 'linux', '1TB', '8TB')
comp1.getInfo() #""" OR, Computer.getInfo(comp1) """

comp2 = Computer('sony', 'windows', '500GB', '4TB')
comp2.getInfo() #""" OR, Computer.getInfo(comp2) """
