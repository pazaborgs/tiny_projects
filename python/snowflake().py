from turtle import Screen, Turtle


def koch(n):
    if n == 0:
        return 'F'
    else:
        mid = koch(n-1)
        return mid + 'L' + mid + 'R' + mid + 'L' + mid
    
def draw_koch(n):
    s = Screen()
    t = Turtle()
    t.speed(6)
    directions = koch(n)
    for i in range(3):
        for move in directions:
            if move == 'F':
                t.forward(300/3**n)
            if move == 'L':
                t.lt(60)
            if move == 'R':
                t.rt(120)
        t.rt(120)
   
