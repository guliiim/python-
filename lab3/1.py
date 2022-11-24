class task:
    def getstring(self,string):
        self.name=string
        
    def printstring(self):
        s=self.name.upper()
        print(s)
        
x=task()
x.getstring('aaa')
x.printstring()