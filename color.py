class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def _print(text, color, bold=False, underline=False):
    final_string = ''
    if bold:
        final_string += Color.BOLD
    if underline:
        final_string += Color.UNDERLINE
    final_string += color
    final_string += text
    final_string += Color.END
    print(final_string)

def _error(text):
    text = '\n\t=>' + text + '\n'
    _print(text, Color.RED, True, True)

def _success(text):
    text = '\n\t=>' + text + '\n'
    _print(text, Color.GREEN, True)

def _info(text):
    text = '\n\t=>' + text + '\n'
    _print(text, Color.CYAN)

def _warning(text):
    text = '\n\t=>' + text + '\n'
    _print(text, Color.YELLOW, True, True)
