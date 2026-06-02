import curses
import random
import time


def matrix_rain(stdscr):
    # Hide the blinking text cursor
    curses.curs_set(0)

    # Enable non-blocking input so we can exit easily
    stdscr.nodelay(True)

    # Get the size of the terminal window
    height, width = stdscr.getmaxyx()

    # Define the characters that will fall
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%&*+-<>?!"

    # Track the current row position of the rain in each column
    # Start them at random negative positions so they don't all fall at once
    columns = [random.randint(-height, 0) for _ in range(width)]

    # Track the falling speed for each column (lower number = faster)
    speeds = [random.randint(1, 3) for _ in range(width)]

    # Frame counter to handle different column speeds
    frame = 0

    while True:
        frame += 1

        # Check if the user pressed 'q' to quit
        key = stdscr.getch()
        if key == ord("q") or key == ord("Q"):
            break

        # Loop through every column on the screen
        for col in range(width):
            # Only move this column if the frame matches its speed
            if frame % speeds[col] == 0:
                current_row = columns[col]

                # 1. Fade out the old character above it (draw a dim green char)
                if current_row - 1 >= 0 and current_row - 1 < height:
                    try:
                        stdscr.addch(
                            current_row - 1,
                            col,
                            random.choice(chars),
                            curses.A_DIM,
                        )
                    except curses.error:
                        pass

                # 2. Draw the leading bright character at the current position
                if current_row >= 0 and current_row < height:
                    try:
                        stdscr.addch(
                            current_row, col, random.choice(chars), curses.A_BOLD
                        )
                    except curses.error: