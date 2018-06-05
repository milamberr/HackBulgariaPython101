from music import PlayList, Song
from mutagen.mp3 import MP3


class MusicCrawler:
    def __init__(self, path):
        self.path = path

    def generate_playlist(self):
        from os import listdir
        from os.path import isfile, join

        onlyfiles = []
        for f in listdir(self.path):
            file_name = join(self.path, f)
            if isfile(file_name):
                onlyfiles.append(file_name)

        playlist = PlayList(name='New Playlist', repeat=True, shuffle=False)

        for file in onlyfiles:
            playlist.add_song(self.generate_song(file))

        return playlist

    @staticmethod
    def generate_song(full_path):
        audio = MP3(full_path)
        return Song(
            title=audio['TIT2'],
            artist=audio['TPE1'],
            album=audio['TALB'],
            length=int(audio.info.length)
        )


def main():
    p = MusicCrawler('/home/ivan/HackPython/week5/music_library/Linkin Park - One More Light [2017] (320)')
    playlist = p.generate_playlist()
    playlist.pprint_playlist()


if __name__ == '__main__':
    main()
