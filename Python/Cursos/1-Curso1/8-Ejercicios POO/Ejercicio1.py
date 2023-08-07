class Student():
    __name='';
    __result=0;
    
    def __init__(self,name,result):
        self.__name=name;
        self.__result=result;
    
    def isApproved(self):
        if self.__result>=3:
            return True;
        else:
            return False;
    
    def __str__(self) -> str:
        return 'Student: {} Result: {}'.format(self.__name,self.__result);

s=Student('Lazaro', 4);

print(s);
print(s.isApproved());