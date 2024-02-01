from Genre import Genre
from Song import Song

print('Hello and welcome to the great music site!!!!!!!!')
s = "start"
SongsChasidi = [Song("1", "avi"), Song("2", "gad"), Song("3", "dan")]
SongsLitay = [Song("4", "shimi"), Song("5", "chnoch"), Song("6", "daniel")]
SongsMizrachi = [Song("7", "haim"), Song("8", "david"), Song("9", "isaac")]

dictMusic = {
    "Chasidi": Genre("Chasidi", SongsChasidi),
    "Litay": Genre("Litay", SongsLitay),
    "Mizrachi": Genre("Mizrachi", SongsMizrachi)
}
while s != 'stop':
    try:
        mode = input("ENTER your choise:\n search Song:1\n add Song:2\n show:3")
        if mode == '1':
            try:
                Song = input("enter the Song(1-20)")
                for k, v in dictMusic.items():
                    if v.find_song(Song) is not None:
                        v.songs[0].play_song(v.find_song(Song))
                        break
                    else:
                        print(f"in {k} not found the Song {Song}")
            except:
                print(f"{Song} is not valid")
        else:
            if mode == '2':
                song_name = input('Enter the song name: ')
                singer = input('Enter the singer: ')
                genre_key = input('Enter the genre (Chasidi/Litay/Mizrachi): ')
                new_song = Song(song_name, singer)
                resultNewSong = new_song.add_song()
                try:
                    if resultNewSong != None:
                        dictMusic[genre_key].songs.append(new_song)
                except:
                    print(f"{genre_key} NOT FOUND,TRY AGAIN")
            else:
                if mode == '3':
                    try:
                        show = input(f"show genre:(Chasidi/Litay/Mizrachi)\nshow appearance:1")
                        if show != '1':
                            dictMusic[show].printSongs()
                        else:
                            if show == '1':
                                singer = input("enter singer to show his appearance: ")
                                for i in dictMusic:
                                    for j in dictMusic[i].songs:
                                        if singer == j.nameSinger:
                                            j.printAppearance()
                                    break
                                # print(f"{singer} NOT FOUND, TRY AGAIN")

                    except:
                        print(f"{show} NOT VALID, TRY AGAIN")

    except ValueError as e:
        print(f"value error {e}")
    s = input("To exit enter 'stop'\nTo continue press any key")
print("GOOD LUCK!!!!!")
