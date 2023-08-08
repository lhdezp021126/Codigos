import random;
import datetime;
import sys;
import time;

print(random.randint(1,10));

print(random.choice([1,2,3,4,5]));
print(random.choices([1,2,3,4,5],k=3));
l=[1,2,3,4,5];
random.shuffle(l);
print(l);

print(datetime.datetime.now());

for i in range(0,101):
    time.sleep(0.5);
    sys.stdout.write('\r{}%'.format(i));
    sys.stdout.flush();
    