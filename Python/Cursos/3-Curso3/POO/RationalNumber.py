class RationalNumber:
    
    def __init__(self,numerator=1,denominator=1):
        self.__numerrator=numerator;
        self.__denminator=denominator;
    
    def __del__(self):
        pass;
    
if __name__=='__main__':
    
    rn=RationalNumber(2,3);
    print(rn);
    del rn;
    print(rn);