def decorator(function):
    def wrapper():
        print('********');
        function();
        print('********');
    return wrapper;

@decorator
def helloWolrd():
    print('hello world'); 
    
