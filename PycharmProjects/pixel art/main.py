from PIL import Image

# Colors corresponding to the layout
colors = {
    'S': (255, 224, 189),  # Skin tone
    'H': (34, 34, 34),     # Hair (black)
    'L': (255, 223, 186),  # Hair highlights (light brown)
    'C': (0, 0, 255),      # Clothes (blue)
    'T': (255, 0, 0),      # Top (red)
    'B': (0, 255, 0),      # Bottom (green)
    'F': (255, 255, 255),  # Feet (white)
    'BKG': (255, 255, 255), # Background (white)
    'E': (0, 0, 0),        # Eyes (black)
    'M': (255, 0, 0),      # Mouth (red)
    'P': (255, 192, 203),  # Pants (pink)
    'S1': (160, 82, 45),   # Shoes (brown)
}


def generate_image(layout):
    width = len(layout[0])
    height = len(layout)
    image = Image.new('RGB', (width, height))

    # Loop through the layout and assign pixel colors
    for y in range(height):
        for x in range(width):
            color_code = layout[y][x]
            image.putpixel((x, y), colors.get(color_code, (0, 0, 0)))  # Default to black if no color is found

    return image


# Example layout (to be replaced with the actual layout you want)

layout = [
    ['BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG'],
    ['BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'S', 'S', 'S', 'BKG', 'BKG'],
    ['BKG', 'BKG', 'BKG', 'S', 'S', 'S', 'S', 'S', 'BKG', 'BKG'],
    ['BKG', 'BKG', 'S', 'S', 'H', 'H', 'S', 'S', 'BKG', 'BKG'],
    ['BKG', 'S', 'S', 'H', 'B', 'B', 'H', 'S', 'S', 'BKG'],
    ['S', 'S', 'H', 'B', 'B', 'B', 'B', 'H', 'S', 'S'],
    ['S', 'S', 'H', 'B', 'B', 'B', 'B', 'H', 'S', 'S'],
    ['BKG', 'S', 'S', 'S', 'B', 'B', 'S', 'S', 'BKG', 'BKG'],
    ['BKG', 'BKG', 'BKG', 'S', 'S', 'S', 'BKG', 'BKG', 'BKG', 'BKG'],
    ['BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG', 'BKG'],
]





# Generate the image
image = generate_image(layout)

# Save the image to a file if needed
image.save('image3.png')
