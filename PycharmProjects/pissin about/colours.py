def display_256_foreground_colors():
    """Displays all 256 foreground colors with the corresponding ANSI escape code."""
    for i in range(256):
        # The ANSI escape code to set the color
        ansi_code = f'\033[38;5;{i}m'
        # Print the color and the ANSI code itself
        print(f"{ansi_code}\\033[38;5;{i}m")


display_256_foreground_colors()

