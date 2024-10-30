import data
import hw2
import unittest
from  data import Point, Duration, Song


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle1(self):
        point1 = Point(2, 10)
        point2 = Point(10, 2)
        rectangle = hw2.create_rectangle(point1, point2)
        self.assertEqual(rectangle.top_left.x, 2)
        self.assertEqual(rectangle.top_left.y, 10)
        self.assertEqual(rectangle.bottom_right.x, 10)
        self.assertEqual(rectangle.bottom_right.y, 2)

    def test_create_rectangle2(self):
        point1 = Point(12, 23)
        point2 = Point(23, 84)
        rectangle = hw2.create_rectangle(point1, point2)
        self.assertEqual(rectangle.top_left.x, 12)
        self.assertEqual(rectangle.top_left.y, 84)
        self.assertEqual(rectangle.bottom_right.x, 23)
        self.assertEqual(rectangle.bottom_right.y, 23)

    # Part 2
    def test_shorter_duration_than1(self):
        duration1 = Duration(1, 30)  # 1 hour, 30 minutes
        duration2 = Duration(2, 13)  # 2 hours
        result = hw2.shorter_duration_than(duration1, duration2)
        self.assertTrue(result)
    def test_shorter_duration_than2(self):
        duration1 = Duration(2, 13)  # 1 hour, 30 minutes
        duration2 = Duration(1, 24)  # 2 hours
        result = hw2.shorter_duration_than(duration1, duration2)
        self.assertFalse(result)
    # Part 3
    def test_songs_shorter_than1(self):
        song1 = Song("Artist A", "Song A", Duration(1, 30))
        song2 = Song("Artist B", "Song B", Duration(2, 0))
        song3 = Song("Artist C","Song C", Duration(3, 45))

        songs = [song1, song2, song3]

        duration = Duration(2, 0)
        result = hw2.songs_shorter_than(songs, duration)

        self.assertEqual(len(result), 1)


    def test_songs_shorter_than2(self):
        song1 = Song("Artist A", "Song A", Duration(12, 20))
        song2 = Song("Artist B", "Song B", Duration(23, 7))
        song3 = Song("Artist C","Song C", Duration(34, 45))

        songs = [song1, song2, song3]

        duration = Duration(34, 0)

        result = hw2.songs_shorter_than(songs, duration)

        self.assertEqual(len(result), 2)

# Part 4
    def test_running_time1(self):
        song1 = Song("Artist A", "Song A", Duration(4, 30))
        song2 = Song("Artist B", "Song B", Duration(3, 40))
        song3 = Song("Artist C", "Song C", Duration(3, 29))
        song4 = Song("Artist D", "Song D", Duration(3, 58))

        songs = [song1, song2, song3, song4]

        playlist = [0, 2, 1, 3, 0]
        result = hw2.running_time(songs, playlist)

        expected = Duration(20, 7)
        self.assertEqual(result, expected)
    def test_running_time2(self):
        song1 = Song("Artist A", "Song A", Duration(6, 42))
        song2 = Song("Artist B", "Song B", Duration(2, 56))
        song3 = Song("Artist C", "Song C", Duration(4, 21))
        song4 = Song("Artist D", "Song D", Duration(3, 12))

        songs = [song1, song2, song3, song4]

        playlist = [2, 2, 0, 1, 3]
        result = hw2.running_time(songs, playlist)

        expected = Duration(21, 32)
        self.assertEqual(result, expected)
    # Part 5
    def test_validate_route1(self):
        city_links = [["A", "B"], ["B", "C"], ["C", "D"]]
        city_names = ["A", "B", "C", "D"]
        result = hw2.validate_route(city_links, city_names)
        expected = True
        self.assertEqual(result, expected)
    def test_validate_route2(self):
        city_links = [["A", "B"], ["B", "C"]]
        city_names = ["A", "D"]
        result = hw2.validate_route(city_links, city_names)
        expected = False
        self.assertEqual(result, expected)

# Part 6
    def test_longest_repetition1(self):
        lst = [1, 1, 2, 2, 2, 3, 3]
        result = hw2.longest_repetition(lst)
        expected = 2
        self.assertEqual(result, expected)
    def test_longest_repetition2(self):
        lst = [2, 1, 2, 2, 3, 3, 3]
        result = hw2.longest_repetition(lst)
        expected = 4
        self.assertEqual(result, expected)



if __name__ == '__main__':
    unittest.main()
