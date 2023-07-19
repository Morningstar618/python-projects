import colorgram


def extract_color(image, color_range):
    colors = colorgram.extract(image, color_range)
    color_list = []

    for i in range(color_range):
        rgb_color = colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b
        color_list.append(tuple(rgb_color))

    return color_list