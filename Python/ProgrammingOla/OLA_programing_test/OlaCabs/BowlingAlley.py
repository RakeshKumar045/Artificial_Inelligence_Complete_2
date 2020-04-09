import unittest


class BowlingGame(object):
    def __init__(self):
        self.min_roll = 0
        self.max_roll = 10

        self.rolls = []
        self.strike_indexes = []
        self.spare_indexes = []
        self.current_roll_index = 0
        self.current_lane_remaining = self.max_roll
        self.current_lane_rolls = []
        self.lanes_completed = 0

    def roll(self, pins):

        if self.lanes_completed == 10:
            raise IndexError("10 frames completed. No more rolling allowed.")

        if pins < self.min_roll:
            raise ValueError("Can't roll less than {}".format(self.min_roll))

        if pins > self.max_roll:
            raise ValueError("Can't roll more than {}".format(self.max_roll))

        if pins > self.current_lane_remaining:
            raise ValueError("Not enough pins remaining to support roll")

        self.rolls.append(pins)
        self.current_lane_rolls.append(pins)
        self.current_lane_remaining -= pins
        self.current_roll_index = len(self.rolls) - 1

        frame_rolls = len(self.current_lane_rolls)

        if self.lanes_completed == 9:

            if frame_rolls == 1:
                if self.current_lane_remaining == 0:
                    self.current_lane_remaining = self.max_roll
            elif frame_rolls == 2:
                if self.current_lane_remaining == 0:
                    self.current_lane_remaining = self.max_roll
                else:
                    if self.current_lane_rolls[0] != 10:
                        self.lanes_completed += 1
            else:
                self.lanes_completed += 1

        else:

            if (self.current_lane_remaining == 0) or (frame_rolls == 2):

                self.lanes_completed += 1

                if self.current_lane_remaining == 0:

                    if frame_rolls == 1:
                        self.strike_indexes.append(self.current_roll_index)
                    else:
                        self.spare_indexes.append(self.current_roll_index)

                self.current_lane_rolls = []
                self.current_lane_remaining = self.max_roll

    def score(self):

        if self.lanes_completed != 10:
            raise IndexError("Cannot score incomplete game.")

        for strike in self.strike_indexes:
            value = sum(self.rolls[strike:strike + 3])
            self.rolls[strike] = value

        for spare in self.spare_indexes:
            value = sum(self.rolls[spare - 1:spare + 2])
            self.rolls[spare] = value
            self.rolls[spare - 1] = 0

        return sum(self.rolls)


class BowlingTest(unittest.TestCase):

    def roll(self, rolls):
        [self.game.roll(roll) for roll in rolls]

    def roll_and_score(self, rolls):
        self.roll(rolls)
        return self.game.score()

    def test_score(self):
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        score = self.roll_and_score(rolls)

        print("Score : ", score)

        # self.assertEqual(score, 0)

    def test_score_second(self):
        rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10,
                 10, 6]

        score = self.roll_and_score(rolls)
        print("Score : ", score)

        # self.assertEqual(score, 26)

    def test_score_third(self):
        rolls = [3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6, 3, 6]

        score = self.roll_and_score(rolls)
        print("Score : ", score)

        # self.assertEqual(score, 90)

    def test_points_scored_in_the_roll_after_a_spare_are_counted_twice(self):
        rolls = [6, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        score = self.roll_and_score(rolls)

        self.assertEqual(score, 16)

        print("Score : ", score)

    def setUp(self):
        self.game = BowlingGame()
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == '__main__':
    unittest.main()
