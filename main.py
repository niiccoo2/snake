import random

WIDTH: int = 10
HEIGHT: int = 10

def draw_board(apple_location: list):
    # multiply everything in the x axis by two to make it look better
    MULTIPLY: int = 2
    print("-"*(WIDTH+2)*MULTIPLY)
    for y in range(HEIGHT):
        print(f"|{' '*(MULTIPLY-1)}", end="")
        for x in range(WIDTH):
            print('O'*MULTIPLY) if [x, y] == apple_location else print(' '*MULTIPLY)
            # need to finish writing logic to spawn apples.
        print(f"|{' '*(MULTIPLY-1)}{' '*10*MULTIPLY}{' '*(MULTIPLY-1)}|")
        print(f"|{' '*(MULTIPLY-1)}{(' '*10*MULTIPLY)}{' '*(MULTIPLY-1)}|")
    print("-"*(WIDTH+2)*MULTIPLY)

def pick_apple_location():
    x = 2*random.randint(1, WIDTH)
    y = random.randint(1, HEIGHT)
    return [x, y]

if __name__ == "__main__":
    draw_board(pick_apple_location())