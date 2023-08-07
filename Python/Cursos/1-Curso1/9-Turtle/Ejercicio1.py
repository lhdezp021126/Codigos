import turtle;

s=turtle.Screen();
t=turtle.Turtle();

t.fd(100);
t.rt(90);
t.fd(100);
t.rt(90);
t.fd(100);
t.rt(90);
t.fd(100);
t.rt(90);

def up():
    t.goto(t.pos()[0],t.pos()[1]+20);
def down():
    t.goto(t.pos()[0],t.pos()[1]-20);
def left():
    t.goto(t.pos()[0]-20,t.pos()[1]);
def rigth():
    t.goto(t.pos()[0]+20,t.pos()[1]);

s.listen()
s.onkeypress(up,'Up');
s.onkeypress(down,'Down');
s.onkeypress(rigth,'Right');
s.onkeypress(left,'Left');



while True:
    s.update();
    

turtle.done();

