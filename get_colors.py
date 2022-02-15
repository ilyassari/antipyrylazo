import colorgram

def get_color_list(image):
    colors = colorgram.extract(image, 40)
    rgb_colors = list()
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        if not (r > 230 and g > 230 and b > 230):
            rgb_colors.append((r, g, b))
    return rgb_colors

