def gameTotalScore(rollList):
    score_sum = 0
    roll_sum = 0
    first_bonus = 10
    second_bonus = 5
    third_bonus = 0
    for ind, val in enumerate(rollList):
        if (val % 2 == 0 and val == 10):
            score_sum = score_sum + first_bonus
            roll_sum = roll_sum + val
        elif (val % 2 == 1 and val > 6 and val < 10):
            if (rollList[ind - 1] != 10):
                score_sum = score_sum + second_bonus
                roll_sum = roll_sum + val
        else:
            score_sum = score_sum + third_bonus
            roll_sum = roll_sum + val
    return score_sum, roll_sum


roll_value = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10]
roll_value1 = [7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10]
total_score, total_roll = gameTotalScore(roll_value1)
print("Total Score : ", total_score, "   Total No of Roll  : ", total_roll)
