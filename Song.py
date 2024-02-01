from Singer import Singer
import pygame


class Song(Singer):
    def __init__(self, nameSong, nameSinger):
        super(Song,self).__init__(nameSinger)
        self.nameSong = nameSong
        self.routing = f"Z:/B/חזקיהו שרה/פייתון/pythonProject2/pytonM/{nameSong}.mp3"

    def add_song(self):
        """add routing song to routing file of song"""
        routing_file = open("Z:/B/חזקיהו שרה/פייתון/pythonProject2/SongList.txt", 'r+', encoding='utf-8')
        songs = routing_file.read()
        if self.routing not in songs:
            routing_file.write(self.routing + "\n")
            print("add successful!")
            routing_file.close()
            return 1
        else:
            print("song exist.")
        routing_file.close()
        return None

    def play_song(self, routing):
        """function that play the song if exist in the folder"""
        try:
            pygame.init()
            pygame.mixer.init()

            # Load the MP3 file
            pygame.mixer.music.load(routing)
            # Play the audio
            pygame.mixer.music.play()
            # Wait for user input to stop the song
            while pygame.mixer.music.get_busy():
                user_input = input("Press 'stop' to stop the song: ")
                if user_input.lower() == 'stop':
                    pygame.mixer.music.stop()
                    break
        except:
            print("not exist in folder.Copy the song to the folder 'pytonM'")

    def printSong(self):
        print(f"Name Singer:{self.nameSinger}\nName Song:{self.nameSong}\nRouting:{self.routing}")
