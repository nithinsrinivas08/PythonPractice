#Some ASCI escape sequences for colors and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'
BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

def colorPrint(text : str, effect : str) -> None :
    """
    Print `text` using the ANSI sequence to change color, etc
    
    :param text : The text to print
    :param effect : The effect we want. One of the constants defined 
                    at the start o fthis module
    """

    outputString = "{0},{1},{2}".format(effect, text, RESET)
    print(outputString)

colorPrint("Hello, Red",RED)
print("This should be in the default color")
colorPrint("Hello, Blue", BLUE)
colorPrint("Hello, Yellow", YELLOW)
colorPrint("Hello, Bold", BOLD)
colorPrint("Hello, Underline", UNDERLINE)
colorPrint("Hello, Reverse", REVERSE)
colorPrint("Hello, Black", BLACK)