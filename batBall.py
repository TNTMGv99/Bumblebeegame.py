import pgzrun

WIDTH = 500
HEIGHT = 500

ball = Rect((150, 400), (60, 20))
bat = Rect((200, 480), (60, 20))
vx = 2
vy = 5
score=0
def draw():
    global score
    screen.clear()
    screen.draw.filled_rect(ball, "red")
    screen.draw.filled_rect(bat, "white")
    screen.draw.text("Score :"+str(score),(20,20),color="blue")

def update():

    global vx, vy,score
    ball.x += vx
    ball.y += vy
    if ball.right > WIDTH or ball.left < 0:
        vx = -vx
    if ball.colliderect(bat) or ball.top < 0:
        vy = -vy
        score=score+1
        if score>=20:
            vx=0
            vy=0
    if ball.bottom > HEIGHT:
        exit()
    if(keyboard.right):
        bat.x += 4
    elif(keyboard.left):
        bat.x -= 4
    if score>200:
       score=0
       vx = 2
       vy = 5
    if(keyboard.right):
        bat.x -+ 3
    elif(keyboard.left):
        bat.x -= 3
    if score>=20:
        vx=0
        vy=0
    if score>=400:
        score=0
        vx = 2
        vy = 5
    if(keyboard.right):
        bat.x -+ 2
    elif(keyboard.left):
        bat.x -= 2
    if score>=15:
        vx=0
        vy=0
    if score>500:
        score=0
        vx=2
        vy=5
    if(keyboard.right):
        bat.x -+ 1
    elif(keyboard.left):
        bat.x -= 1
    

    

        


pgzrun.go()