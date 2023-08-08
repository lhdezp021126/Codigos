def generator():
    """Generate the number pars in range(1,101)"""
    l=[i for i in range(1,101)];
    for e in l:
        yield e if e%2==0 else 0;
        
for e in generator():
    print(e);
print(generator.__doc__);