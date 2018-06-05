import re
from pprint import pprint


class Song:
    def __init__(self, *, title, artist, album, length):
        self.title = title
        self.artist = artist
        self.album = album
        if type(length) is int:
            self.length = self.format_length(length)
        
        else:
            self.length = length
            self.validate_length(self.length)

    @staticmethod
    def format_length(seconds):
        return f'{seconds//3600:02}:{(seconds%3600)//60:02}:{(seconds%3600)%60:02}'


    def validate_length(self, s):
        time = s.split(":")
        if len(time) <= 1:
            raise ValueError('Not a correct input format')

        try:
            sum(int(t) for t in time)
        except:
            raise TypeError('Not numbers')

    def __str__(self):
        return f'{self.artist} - {self.title} from {self.album} - {self.length}'

    def __eq__(self, other):
        return self.title == other.title\
            and self.artist == other.artist\
            and self.album == other.album\
            and self.length == other.length

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        return str(self)

    def to_json(self):
        return self.__dict__

    @classmethod
    def from_json(cls, dictionary):
        return cls(**dictionary)

    def l(self, **kwargs):
        time = self.length.split(':')
        have_hours = len(time) == 3
        if 'seconds' in kwargs.keys() and kwargs['seconds'] is True:
            if not have_hours:
                secs = int(time[0]) * 60 + int(time[1])
            else:
                secs = int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])
            return secs
        if 'minutes' in kwargs.keys() and kwargs['minutes'] is True:
            if not have_hours:
                return int(time[0])
            else:
                return int(time[0]) * 60 + int(time[1])
        if 'hours' in kwargs.keys() and kwargs['hours'] is True:
            if not have_hours:
                return 0
            else:
                return int(time[0])

        return self.length


class PlayList:
    def __init__(self, *, name, repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.songs = []
        if shuffle is True:
            self.unplayed_songs = [i for i in range(0, len(self.songs))]
        self.next = 0

    def add_song(self, song):
        if type(song) is not Song:
            raise TypeError
        self.songs.append(song)

    def remove_song(self, song):
        if type(song) is not Song:
            raise TypeError
        if song in self.songs:
            self.songs.remove(song)

    def add_songs(self, songs):
        for song in songs:
            if type(song) is not Song:
                raise TypeError
        self.songs += songs

    def artists(self):
        artist_histo = {}
        for artist in [song.artist for song in self.songs]:
            if artist in artist_histo.keys():
                artist_histo[artist] += 1
            else:
                artist_histo[artist] = 1

        return artist_histo

    def shuffle_next_song(self):
        from random import randint

        if len(self.unplayed_songs) == 0:
            self.unplayed_songs = [i for i in range(0, len(self.songs))]

        inx = randint(0, len(self.unplayed_songs))
        song = self.songs[inx]
        self.unplayed_songs.remove(inx)

        return song

    def repeat_mode_next_song(self):
        next_song = self.songs[self.next]
        self.next = (self.next + 1) % len(self.songs)
        return next_song

    def next_song(self):
        if len(self.songs) == 0:
            return None
        elif self.shuffle:
            return self.shuffle_next_song()
        elif self.repeat:
            return self.repeat_mode_next_song()
        else:
            if self.next >= len(self.songs):
                return None
            else:
                next_song = self.songs[self.next]
                self.next += 1
                return next_song

    def total_length(self):
        if len(self.songs) == 0:
            return '0:0:0'
        lengths = list(map(lambda x: int(x.l(seconds=True)), self.songs))
        total_secs = sum(lengths)
        return f'{total_secs//3600}:{(total_secs%3600)//60}:{(total_secs%3600)%60}'

    def pprint_playlist(self):
        from tabulate import tabulate

        if len(self.songs) == 0:
            print('Empty playlist')
            return

        songs = []
        headers = ['Artist', 'Name', 'Length']

        for song in self.songs:
            songs.append([song.artist, song.title, song.length])

        print(tabulate(songs, headers=headers, showindex=True))

    def save(self):
        import json
        import os
        from copy import deepcopy

        data = {
            'name': self.name,
            'repeat': self.repeat,
            'shuffle': self.shuffle,
            'songs': [x.to_json() for x in self.songs]
        }

        json_filename = '-'.join(self.name.split(' '))
        json_filename = f'{json_filename}.json'
        with open(f'{os.path.dirname(os.path.abspath(__file__))}/playlist-data/{json_filename}', 'w') as output:
            json.dump(data, output)

        return data

    @staticmethod
    def load(path):
        import json

        with open(path) as file:
            data = json.load(file)
            p = PlayList(name=data['name'], repeat=data['repeat'], shuffle=data['shuffle'])
            p.add_songs([Song.from_json(x) for x in data['songs']])

        return p

    def __eq__(self, other):
        return self.shuffle == other.shuffle\
            and self.repeat == other.repeat\
            and self.name == other.name
