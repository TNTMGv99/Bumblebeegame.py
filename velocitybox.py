import pgzrun  

WIDTH = 500
HEIGHT  = 500

box = Rect((200, 400), (20, 20))

vx = 1
vy = 1

def draw():
    screen.clear()
    screen.draw.filled_rect(box, "red")

def update():
    global vx, vy
    box.x += vx
    box.y+=vy
    if box.right > WIDTH or box.left < 0:
        vx = -vx
    if box.bottom > HEIGHT or box.top < 0:
        vy = -vy

pgzrun.go()