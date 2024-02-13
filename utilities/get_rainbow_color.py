import colorsys

# Function to return a rainbow color based on the input value
def get_rainbow_color(i):
    hue = i % 360
    hue /= 360
    saturation = 1
    value = 1
    rgb = colorsys.hsv_to_rgb(hue, saturation, value)
    return tuple(int(x * 255) for x in rgb)