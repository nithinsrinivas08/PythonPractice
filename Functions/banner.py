def bannerText(text, screenWidth = 80) :
    if len(text) > screenWidth - 4 :
        print("EEK!!")
        print("The text is too long to fit in the specified width")
    if text == "*" :
        print("*" * screenWidth)
    else :
        centeredText = text.center(screenWidth - 4)
        outputString = "**{}**".format(centeredText)
        print(outputString)

bannerText("*")
bannerText("Always look on the bright side of life...")
bannerText("If life seems jolly rotten")
bannerText("There's something you've forgotten!")
bannerText("And that's to laugh and smile and dance and sing,")
bannerText(" ")
bannerText("When you're feeling in the dumps,")
bannerText("Don't be silly chumps,")
bannerText("Just purse your lips and whistle - that's the thing!")
bannerText("And... always look on the bright side of life...")
bannerText("*")