class Person:
    __first_name='';#El doble guion bajo al inicio encapsula los atributos
    __last_name='';
    
    def __init__(self,first_name,last_name):
        self.__first_name=first_name;
        self.__last_name=last_name;
    
    def __str__(self) -> str:
        return 'Preson: {}  {}'.format(self.__first_name,self.__lastname);

class Programmer(Person):
    
    def speak(self):
        print('I love programming');
        
    def __str__(self) -> str:
        return 'I am programmer and my name is {} {}'.format(self._Person__first_name,self._Person__last_name);
    
p=Programmer('Lazaro','Hernandez');
print(p);

print(p._Person__first_name);

p.speak();