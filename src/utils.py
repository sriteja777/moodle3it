import config


def color_text(text, color):
    if '\x1b' in color:
        return color + text + config.END_COLOR
    else:
        try:
            letter = color[0]
            if letter.islower():
                letter = letter.upper()
            color = letter + color[1:]
            return config.COLORS[color] + text + config.END_COLOR
        except:
            return text
