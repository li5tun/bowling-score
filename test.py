import unittest

from score import BowlingScore


class ScoreTests(unittest.TestCase):
    def test_all_frames_both_strike(self):
        frames = [[10], [10], [10], [10], [10], [10], [10], [10], [10], [10, 10, 10]]
        bowling_score = BowlingScore(frames)
        self.assertEqual(bowling_score.total_score(), 300)

    def test_partial_frames_are_strike(self):
        frames = [[9, 0], [10], [10], [9, 0], [10], [10], [10], [10], [9, 0], [10, 10, 10]]
        bowling_score = BowlingScore(frames)
        self.assertEqual(bowling_score.total_score(), 213)

    def test_all_frames_both_spare(self):
        frames = [[9, 1], [9, 1], [9, 1], [9, 1], [9, 1], [9, 1], [9, 1], [9, 1], [9, 1], [9, 1, 0]]
        bowling_score = BowlingScore(frames)
        self.assertEqual(bowling_score.total_score(), 181)

    def test_all_frames_both_spare_except_10th(self):
        frames = [[9, 1], [9, 1], [9, 1], [9, 1], [9, 1], [9, 1], [9, 1], [9, 1], [9, 1], [8, 1]]
        bowling_score = BowlingScore(frames)
        self.assertEqual(bowling_score.total_score(), 179)

    def test_open_frames(self):
        frames = [[8, 1], [8, 1], [8, 1], [8, 1], [8, 1], [8, 1], [8, 1], [8, 1], [8, 1], [8, 1]]
        bowling_score = BowlingScore(frames)
        self.assertEqual(bowling_score.total_score(), 90)

    def test_mixing_frames(self):
        frames = [[10], [8, 1], [9, 1], [8, 1], [10], [8, 1], [8, 1], [9, 1], [8, 1], [10, 9, 9]]
        bowling_score = BowlingScore(frames)
        self.assertEqual(bowling_score.total_score(), 147)


if __name__ == '__main__':
    unittest.main()
