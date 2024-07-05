# TITLE:Fishing

# AUTHOR:Blaire Carson

# DATE DUE:1/28/21

# DATE SUBMITTED:1/28/21

# COURSE TITLE:Game Design

# MEETING TIME(S):N/A

# DESCRIPTION:You click squares to randomly catch fish. Some squares have higher chances of catching fish than others.
    
# HONOR CODE:I have neither given nor received any unauthorized aid on this assignment. Alaina B Carson

# HOWTO: Open in proccessing and click run.

# INPUT FILE:N/A

# OUTPUT FILE:N/A

# BIBLIOGRAPHY:https://py.processing.org/tutorials/

# TUTORS:N/A

# COMMENTS:There are some surprises so feel free to explore!



#global variables
s = 0
m = ""
bait = 20
fish = 0
jewlrey = 0



def setup():
  size(1000,1000)
  frameRate(30)
  c = color(10,10,100)
  background(c)
  textAlign(CENTER)
  
  textSize(50)
  text("The Fishing Game",500,200)
  textSize(30)
  text("Click squares to fish. You need to go home with at least 3 fish.",500,300)
  text("But be careful, you have limited bait!",500,350)
  text("Some squares are more likely to have fish then others. Good Luck!",500,400)
  text("Click to start.",500,500)
  


def draw():
    global screen, jewlrey, m
    if s == 1:
        Screen()
    if s == 2:
        fishScreen(m)
    if s == 3:
        loseScreen(jewlrey)
    if s == 4:
        winScreen()
    
    
    
def mouseClicked():
    global s, m, bait, fish
    if s == 0:
        s = 1
    elif s == 1:
        l = Location()
        #print(l)
        if l != None:
            m = Fish(l)
            s = 2
    elif s == 2:
        s = 1
    if fish == 3:
        s = 4
    elif bait == 0:
        s = 3
        
       
         
def Location():    
    rects = [100,200,300,400,500,600,700,800]
    for j in rects:
        for i in rects:
            x = i
            y = j
            #print(x,y)
            if mouseX > x and mouseX < x+100 and mouseY > y and mouseY < y+100:
                l = [x,y]
                return l
      
                
                                    
def winScreen():
    c = color(255,255,255)
    background(c)
    c = color(0,0,0)
    fill(c)
    textSize(50)
    text("You Win!",500,300)
    textSize(30)
    text("You caught enough fish! You can go home now.",500,500)
    
    
    
def loseScreen(jewlrey):
    
    if jewlrey == 1:
        c = color(10,10,100)
        background(c)
        c = color(255,255,255)
        fill(c)
        textSize(50)
        text("You lost?",500,300)
        textSize(30)
        text("You didn't bring home enough fish,",500,500)
        text("but you more than made up for it with that necklace!",500,550)
    else:
        c = color(0,0,0)
        background(c)
        c = color(255,255,255)
        fill(c)
        textSize(50)
        text("You lost...",500,300)
        textSize(30)
        text("You didn't bring home enough fish. Your wife will not be happy...",500,500)
        
    
    
def fishScreen(message):
    c = color(255,255,255)
    background(c)
    c = color(0,0,0)
    fill(c)
    textSize(50)
    text(message,500,300)
    textSize(30)
    text("Click to keep fishing.",500,500)
       
      
                
def Screen():
    c = color(100,100,100)
    background(c)
    
    c = color(255,255,255)
    fill(c)
    rect(825,40,150,50)
    rect(25,40,150,50)
    c = color(0,0,0)
    fill(c)
    t = "Bait: " + str(bait)
    countF = "Fish: " + str(fish)
    #print(t)
    text(t,900,75)
    text(countF,100,75)
    shade = 100
    for i in [100,200,300,400,500,600,700]:
        c = color(10,10,shade)
        Row(i,c)
        shade = shade + 10    
    c = color(10,100,10)
    Row(800,c)
    
  
  
def Fish(l):
    global jewlrey, bait, fish
    bait = bait - 1
    x = l[0]
    #print(x)
    y = l[1]
    #print(y)
    f = "" 
    r = 10
    treasure = False
    land = False
    if y == 100:
        r = int(random(3))
    elif y == 200:
        r = int(random(4))
    elif y == 300:
        r = int(random(4))
    elif y == 400:
        r = int(random(5))
    elif y == 500:
        r = int(random(5))
    elif y == 600:
        r = int(random(6))
    elif y == 700:
        r = int(random(6))
    elif y == 800:
        if x == 300:
            treasure = True
        elif x >= 100 and x < 300:
            land = True
        elif x >= 400 and x <= 800:
            land = True

    if r == 0:
        f = "You caught a fish!"
        fish = fish + 1
    elif r == 3:
        f = "Ew. You reeled in trash."
    elif treasure == True:
        f = "Wow! You found a necklace!"
        jewlrey = 1
    elif land == True:
        f = "Why are you fishing on land?"
    else:
        f = "No luck. Your hook is empty."
    #print(f)
    return f
        
    
        
def Row(z,c):
    rects = [[100,z],[200,z],[300,z],[400,z],[500,z],[600,z],[700,z],[800,z]]
    fill(c)
    for i in rects:
        j = rects.index(i)
        x = rects[j][0]
        y = rects[j][1]
        rect(x,y,100,100)
