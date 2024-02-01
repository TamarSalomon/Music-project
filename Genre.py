from Song import Song


class Genre:
    def __init__(self, ganre, arrSong):
        self.ganre = ganre
        self.songs = [song for song in arrSong]

    def find_song(self, nameS):
        """search song in certain genre"""
        for i in self.songs:
            if nameS == i.nameSong:
                return i.routing
        return None

    def printSongs(self):
        """print the array song for this genre"""
        ps = lambda song: song.printSong()
        for i in self.songs:
            ps(i)
