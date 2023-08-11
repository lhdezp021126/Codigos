class Criba:
    
    def __init__(self,n):
        self.__primes=[0 for i in range(n+1)];
        
    def startCriba(self):
        for i in range(2,len(self.__primes)):
            if self.__primes[i]==0:
                for j in range(i*2,len(self.__primes),i):
                    self.__primes[j]=1;
                    
    def isprime(self,n):
        return not self.__primes[n];


if __name__=='__main__':
    c=Criba(100);
    c.startCriba();
    print('37 is prime.' if c.isprime(37) else '37 is not prime.');