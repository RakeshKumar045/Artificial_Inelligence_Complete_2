class BowlingGame():
    def __init__(self, pins, count):
        self.pin = pins
        self.min_roll = 0
        self.count = count
        self.max_roll = 10
        self.score = 0

    def totalScore(self):

        if (self.pin == 0 and self.count == 1):
            self.score = 10 + 10
            return self.score
        elif (self.pin == 0 and self.count == 2):
            score = 10 + 10 + 5
            return score
        elif (self.pin == 0 and self.count == 3):
            score = 10 + 10 + 10
            return score
        else:
            return self.score

    def score(self):

        if (self.pin == 0 and self.count == 1):
            self.score = 10 + 10
            return self.score
        elif (self.pin == 0 and self.count == 2):
            score = 10 + 10 + 5
            return score
        elif (self.pin == 0 and self.count == 3):
            score = 10 + 10 + 10
            return score
        else:
            return self.score

    def PlayingGame():
        no_of_pins = input("Enter the no of pins   :      ")
        no_of_tries = int(input("Enter the no of tries :      "))

        try:
            bowlingGame = BowlingGame(no_of_pins, no_of_tries)
            # print("Total score is : ",bowlingGame.totalScore())
        except Exception as e:
            print("Please enter the valid no of pins of or no of tries", e)
        else:
            print("Total Score is : ", bowlingGame.totalScore())
