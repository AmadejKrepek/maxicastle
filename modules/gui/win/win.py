def define_window(root):
    # Set the window size
    window_width = 1000  # Set the width as desired
    window_height = 800  # Set the height as desired

    # Set minimum width and height
    root.minsize(width=400, height=300)

    # Get the screen width and height for centering the window
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the position to center the window
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    # Set the window size and position
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")