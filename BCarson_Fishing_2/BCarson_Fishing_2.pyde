#global variables
s = 0
bait = 20


def setup():
  size(1000,1000)
  c = color(10,10,100)
  background(c)
  textAlign(CENTER)
  
  textSize(50)
  text("The Fishing Game",500,200)
  textSize(30)
  text("Click squares to fish. You need to go home with at least 3 fish.",500, 250)
  text("But be careful, You have limited bait!",500,300)
  text("Click to start.",500,500)
  

def draw():
    global screen
    if s == 1:
        Screen()
    
def mouseClicked():
    global s
    if s == 0:
        s = 1
        
def Screen():
    c = color(0,0,0)
    fill(c)
    t = "Bait: " + str(bait)
    text(t,900,10)
    c = color(100,100,100)
    background(c)
    c = color(10,10,100)
    Row(100,c)
    c = color(10,10,110)
    Row(200,c)
    c = color(10,10,120)
    Row(300,c)
    c = color(10,10,130)
    Row(400,c)
    c = color(10,10,140)
    Row(500,c)
    c = color(10,10,150)
    Row(600,c)
    c = color(10,10,160)
    Row(700,c)
    c = color(10,100,10)
    Row(800,c)
    
def Row(z,c):
    rects = [[100,z],[200,z],[300,z],[400,z],[500,z],[600,z],[700,z],[800,z]]
    fill(c)
    for i in rects:
        print(i)
        j = rects.index(i)
        print(j)
        x = rects[j][0]
        y = rects[j][1]
        rect(x,y,100,100)
