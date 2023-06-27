def bannerText(text: str =" ", screenWidth : int = 80) -> None:
    """ Print a string centred, with ** either side.
  
    :param text: The string to print.
        An asterisk (*) will result in a row of asterisks.
        The default will print a blank line, with a ** border at
        the left and right edges.
    :param screenWidth: The overall width to print within
        (including the 4 spaces for the ** either side).
    :raises ValueError: if the supplied string is too long to fit.
    """
    if len(text) > screenWidth - 4:
        raise ValueError("String '{0}' is larger than specified width {1}".format(text, screenWidth))
    if text == "*" :
        print("*" * screenWidth)
    else :
        centeredText = text.center(screenWidth - 4)
        outputString = "**{}**".format(centeredText)
        print(outputString)

bannerText("*", 60)
bannerText("Always look on the bright side of life...", 60)
bannerText("If life seems jolly rotten", 60)
bannerText("There's something you've forgotten!", 60)
bannerText("And that's to laugh and smile and dance and sing,", 60)
bannerText(" ", 60)
bannerText("When you're feeling in the dumps,", 60)
bannerText("Don't be silly chumps,", 60)
bannerText("Just purse your lips and whistle - that's the thing!", 60)
bannerText("And... always look on the bright side of life...", 60)
bannerText("*", 60)