import unittest
from music import Song
from music import PlayList

s = Song(
    title="Odin",
    artist="Manowar",
    album="The Sons of Odin",
    length="3:44"
)
s1 = Song(
    title='In the end',
    artist='Linkin Park',
    album='Hybrid Theory',
    length='1:4:13'
)
s2 = Song(
    title='Numb',
    artist='Linkin Park',
    album='Meteora',
    length='4:7'

)

class SongTests(unittest.TestCase):
    def test_length_works(self):
        print(s.__dict__)
        with self.subTest('with seconds'):
            self.assertEqual(s.l(seconds=True), 224)
            self.assertEqual(s1.l(seconds=True), 3853)

        with self.subTest('with minutes'):
            self.assertEqual(s.l(minutes=True), 3)
            self.assertEqual(s1.l(minutes=True), 64)

        with self.subTest('with hours'):
            self.assertEqual(s.l(hours=True), 0)
            self.assertEqual(s1.l(hours=True), 1)

        with self.subTest('with no keywords'):
            self.assertEqual(s.l(), s.length)
            self.assertEqual(s1.l(), s1.length)

    def test_validate_song_length_input_works(self):
        with self.subTest("Length input is just a number"):
            with self.assertRaises(ValueError):
                s_to_change = Song(
                    title='Odin',
                    artist='Manowar',
                    album='The Sons of Odin',
                    length='23'
                )
        with self.subTest("Length input contains non-ints"):
            with self.assertRaises(TypeError):
                s_to_change = Song(
                    title='Odin',
                    artist='Manowar',
                    album='The Sons of Odin',
                    length='qba:qba'
                )


class PlayListTests(unittest.TestCase):
    def setUp(self):
        self.playlist_shuffle = PlayList(name='shuffle', repeat=False, shuffle=True)
        self.playlist_repeat = PlayList(name='repeat', repeat=True, shuffle=False)
        self.playlist_normal = PlayList(name='normal', repeat=False, shuffle=False)

    def test_add_song_works(self):
        self.playlist_shuffle.add_song(s)
        self.assertEqual(self.playlist_shuffle.songs, [s])

    def test_remove_song_works(self):
        self.playlist_shuffle.add_song(s)
        self.playlist_shuffle.remove_song(s)
        self.playlist_repeat.remove_song(s1)
        self.assertEqual(self.playlist_shuffle.songs, [])

    def test_add_songs_works(self):
        self.playlist_shuffle.add_songs([s, s1])
        self.assertEqual(self.playlist_shuffle.songs, [s, s1])

    def test_artists_work(self):
        self.playlist_normal.add_songs([s, s1])
        self.assertEqual(self.playlist_normal.artists(), {'Manowar': 1, 'Linkin Park': 1})
        self.playlist_normal.add_song(s2)
        self.assertEqual(self.playlist_normal.artists(), {'Manowar': 1, 'Linkin Park': 2})

    def test_next_song_works(self):
        with self.subTest("Without repeat and shuffle"):
            with self.subTest("With empty playlist"):
                self.assertEqual(self.playlist_normal.next_song(), None)
            with self.subTest("With non-empty playlist"):
                self.playlist_normal.add_songs([s, s1])
                self.assertEqual(self.playlist_normal.next_song(), s)
                self.assertEqual(self.playlist_normal.next_song(), s1)
                self.assertEqual(self.playlist_normal.next_song(), None)

        with self.subTest("With repeat playlist"):
            self.assertEqual(self.playlist_repeat.next_song(), None)
            self.playlist_repeat.add_songs([s, s1])
            self.assertEqual(self.playlist_repeat.next_song(), s)
            self.assertEqual(self.playlist_repeat.next_song(), s1)
            self.assertEqual(self.playlist_repeat.next_song(), s)

    def test_total_length(self):
        self.assertEqual(self.playlist_normal.total_length(), '0:0:0')
        self.playlist_normal.add_songs([s, s1])
        self.assertEqual(self.playlist_normal.total_length(), '1:7:57')
        self.playlist_normal.remove_song(s1)
        self.assertEqual(self.playlist_normal.total_length(), '0:3:44')

    def test_pprint(self):
        self.playlist_normal.add_songs([s, s1, s2])
        self.playlist_normal.pprint_playlist()

    def test_json(self):
        import os
        self.playlist_normal.add_songs([s, s1, s2])
        data = self.playlist_normal.save()
        self.assertEqual(
            PlayList.load(f'{os.path.dirname(os.path.abspath(__file__))}/playlist-data/normal.json'),
            self.playlist_normal
        )

if __name__ == "__main__":
    unittest.main()
