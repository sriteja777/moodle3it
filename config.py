import sys
COLORS = {
    'Black': '\x1b[0;30m',
    'Blue': '\x1b[1;34m',
    'Green': '\x1b[0;32m',
    'Cyan': '\x1b[0;36m',
    'Red': '\x1b[1;31m',
    'Purple': '\x1b[0;35m',
    'Brown': '\x1b[0;33m',
    'Gray': '\x1b[0;37m',
    'Pink': '\x1b[38;5;200m',
    'Dark Gray': '\x1b[1;30m',
    'Light Blue': '\x1b[1;34m',
    'Light Green': '\x1b[1;32m',
    'Light Cyan': '\x1b[1;36m',
    'Light Red': '\x1b[1;31m',
    'Light Purple': '\x1b[1;35m',
    'Yellow': '\x1b[1;33m',
    'Light Grey': '\x1b[1;37m',
    'Bridge Color': '\x1b[48;5;130m',
    'Bullets Color': '\x1b[38;5;208m',
    'Extras Bridge': '\x1b[38;5;82m',
    'Water Color': '\x1b[48;5;39m',
    'Fish Color': '\x1b[38;5;130m',
    'Moving Bridges': '\x1b[48;5;94m'
}

LINUX = False
WINDOWS = False
if sys.platform.system() == "Windows":
    CLEAR_COMMAND = "cls"
    WINDOWS = True
else:
    CLEAR_COMMAND = "clear"


END_COLOR = '\033[0m'
COURSE_COLOR = COLORS['Brown']
LINK_COLOR = COLORS['Blue']
ERROR_COLOR = COLORS['Red']
FILE_COLOR = COLORS['Cyan']