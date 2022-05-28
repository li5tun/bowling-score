import unittest

from score import BowlingScore


class ScoreTests(unittest.TestCase):
    def test_all_frames_both_strike(self):
        frames = [[10], [10], [10], [10], [10], [10], [10], [10], [10], [10, 10, 10]]
        bowling_score = BowlingScore(frames)
        self.assertEqual(bowling_score.total_score(), 300)


if __name__ == '__main__':
    unittest.main()
