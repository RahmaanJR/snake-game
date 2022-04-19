import curses
from random import randint

#setting up window "win"
curses.initscr() #screen initialization
win = curses.newwin(20, 60, 0, 0) #y coordinate, x coordinate
win.keypad(1) #enabling keypad to control snake
curses.noecho() #disabling other inputs
curses.curs_set(0) 
win.border(0)
win.nodelay(1)


#snake and food
snake = [(4, 10), (4, 9), (4, 8)] #snake list is storing x & y coordinates which are tuples because they are immutable
food = (randint(1, 14), randint(1, 50)) #place initial food character in a random spot within the specified range within the window
win.addch(food[0], food[1], '$') #add initial food character to window

#game logic
score = 0
ESC = 27 #escape key is defined as key 27 in the curses module
key = curses.KEY_RIGHT #snake begins motion to the right

while key != ESC:

    win.addstr(0, 2, 'Score ' +  str(score) + '')
    win.timeout(150  - (len(snake)) // 5 + len(snake) // 10 % 120) #increasing snake movement speed based on its length

    prev_key = key
    event = win.getch() #get next character
    key = event if event != -1 else prev_key

    if key not in [curses.KEY_LEFT, curses.KEY_UP, curses.KEY_RIGHT, curses.KEY_DOWN, ESC]:
        key = prev_key

    #calculate the next coordinates
    y = snake[0][0]
    x = snake[0][1]

    if key == curses.KEY_DOWN:
        y += 1

    if key == curses.KEY_UP:
        y -= 1

    if key == curses.KEY_LEFT:
        x -= 1

    if key == curses.KEY_RIGHT:
        x += 1

    snake.insert(0, (y, x)) #append 0(n)

    #check if the snake hit the border
    if y == 0: 
        break
    if y == 19: #1 less than max window dimensions set with window initialization
        break 
    if x == 0: 
        break
    if x == 59: #1 less than max window dimensions set with window initialization
        break 

    #check if snake runs over itself
    if snake[0] in snake[1:]: #if the head of the snake intersects with any other current position of the snake
        break 

    if snake[0] == food:
        score += 1
        food = ()

        while food == ():
            food = (randint(1, 18), randint(1, 58))

            if food in snake:
                food = ()

        win.addch(food[0], food[1], '$')

    else:
        last = snake.pop()
        win.addch(last[0], last[1], ' ')

    win.addch(snake[0][0], snake[0][1], 'o')


curses.endwin()
print(f"Final score = {score}")