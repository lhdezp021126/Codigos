class User:
    
    def system():
        return 'upr-k';
    
    def __init__(self,username,password):
        self.__username=username;
        self.__password=password;
    
    
    def getPassword(self):
        return self.__password;
    
    def setPassword(self,newPassword):
        self.__password=newPassword;
        
user=User('lhdezp','12345678');
print(user.getPassword());
user.setPassword('1234');
print(user.getPassword());
print(User.system());
        