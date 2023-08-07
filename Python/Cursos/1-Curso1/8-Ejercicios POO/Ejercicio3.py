class Factory():
    __tires=0;
    __color='';
    __price=0.0;
    
    def __init__(self,tires,color,price) -> None:
        self.__tires=tires;
        self.__color=color;
        self.__price=price;
        
    def __str__(self) -> str:
        return 'Factory: tires: {}\ncolor: {}\nprice: {}'.format(self.__tires,self.__color,self.__price);
    
class Factory_Motorcycle(Factory):
    
    def __str__(self) -> str:
        return 'Motorcycle '+super().__str__()
    
class Factory_Car(Factory):
    
    def __str__(self) -> str:
        return 'Car '+super().__str__()
    
m=Factory_Motorcycle(12,'black',12.8);
c=Factory_Car(122,'black',12.89);

print(m);
print(c);
    
    
    