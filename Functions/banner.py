def bannerText(text, screenWidth = 80) :
    if len(text) > screenWidth - 4 :
        print("EEK!!")
        print("The text is too long to fit in the specified width", 60)
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