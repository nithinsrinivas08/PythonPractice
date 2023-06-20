from demo import albums
SONGSLIST = 3
SONGLIST = 1
while True :
    print("Please choose your album (invalid choice exists) : ")
    for i, (t,a,y,s) in enumerate(albums) :
        print("{} : ,{}".format(i+1,t))
    choice = int(input())
    if 1 <= choice <= len(albums):
        songsList = albums[choice -1][SONGSLIST]
    else :
        break
    print("Please Choose your song : ")
    for i, (trackNumber, song) in enumerate(songsList) :
        print("{}: {}".format(i +1, song))
    songChoice = int(input())
    if 1<=songChoice<=len(songsList) :
        title = songsList[songChoice -1][SONGLIST]
    else :
        break

    print("Playing {}".format(title))
    print("="*20)