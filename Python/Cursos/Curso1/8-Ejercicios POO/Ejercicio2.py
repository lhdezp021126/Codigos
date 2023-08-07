from numpy import subtract


class Calculator():
    __number1=0;
    __number2=0;
    
    def __init__(self,number1,number2):
        self.__number1=number1;
        self.__number2=number2;
    
    def sum(self):
        return self.__number1+self.__number2;
    def subtract(self):
        return self.__number1-self.__number2;
    def multiplication(self):
        return self.__number1*self.__number2;
    def division(self):
        return self.__number1/self.__number2;
    
    def __str__(self) -> str:
        return 'Sum {} \nSubtract {} \nMultiplication {}\nDivision {}'.format(self.sum(),self.subtract(),self.multiplication(),self.division());

c=Calculator(2,1);

print(c);