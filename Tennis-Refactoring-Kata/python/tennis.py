# -*- coding: utf-8 -*-

class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0


class TennisGame1:

    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.p1points += 1
        else:
            self.p2points += 1

    def is_equal(self):
        return self.p1points==self.p2points

    def equal_result(self):
        return {
            0 : "Love-All",
            1 : "Fifteen-All",
            2 : "Thirty-All",
        }.get(self.p1points, "Deuce")

    def greater_equal_to_four(self):
        return self.p1points>=4 or self.p2points>=4

    def get_best_player(self, difference):
        return self.player1Name if difference > 0 else self.player2Name

    def advantage_player(self, difference):
        return "Advantage " + self.get_best_player(difference)

    def winner_player(self, difference):
        return "Win for " + self.get_best_player(difference)

    def default(self):
        data = {
            0 : "Love",
            1 : "Fifteen",
            2 : "Thirty",
            3 : "Forty",
        }
        return "{}-{}".format(data[self.p1points], data[self.p2points])




    def score(self):
        if self.is_equal():
            return self.equal_result()
        if self.greater_equal_to_four():
            difference = self.p1points-self.p2points
            if abs(difference) == 1:
                return self.advantage_player(difference)
            return self.winner_player(difference)
        return self.default()











class TennisGame2:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.setP1Score()
        else:
            self.setP2Score()

    def get_score_descr(self, points):
        result = ""
        if (points==0):
            result = "Love"
        elif (points==1):
            result = "Fifteen"
        elif (points==2):
            result = "Thirty"
        elif (points==3):
            result = "Forty"
        return result

    def score(self):
        result = ""
        P1res = ""
        P2res = ""

        if (self.p1points == self.p2points):
            if(self.p1points < 3):
                result = self.get_score_descr(self.p1points)
                result += "-All"
            else:
                result = "Deuce"

        elif (self.p1points < 4 or self.p2points < 4):
            P1res = self.get_score_descr(self.p1points)
            P2res = self.get_score_descr(self.p2points)
            result = P1res + "-" + P2res


        if (self.p1points > self.p2points and self.p2points >= 3):
            result = "Advantage " + self.player1Name
        elif (self.p2points > self.p1points and self.p1points >= 3):
            result = "Advantage " + self.player2Name

        if (self.p1points>=4 and self.p2points>=0 and (self.p1points-self.p2points)>=2):
            result = "Win for " + self.player1Name
        elif (self.p2points>=4 and self.p1points>=0 and (self.p2points-self.p1points)>=2):
            result = "Win for " + self.player2Name
        return result



    def setP1Score(self):
        self.p1points +=1


    def setP2Score(self):
        self.p2points +=1











class TennisGame3:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1Points = 0
        self.p2Points = 0

    def won_point(self, n):
        if n == self.player1Name:
            self.p1Points += 1
        else:
            self.p2Points += 1

    def score(self):
        if (self.p1Points < 4 and self.p2Points < 4) and (self.p1Points + self.p2Points < 6):
            score_descr = ["Love", "Fifteen", "Thirty", "Forty"]
            s = score_descr[self.p1Points]
            return s + "-All" if (self.p1Points == self.p2Points) else s + "-" + score_descr[self.p2Points]
        else:
            if (self.p1Points == self.p2Points):
                return "Deuce"
            s = self.player1Name if self.p1Points > self.p2Points else self.player2Name
            return "Advantage " + s if ((self.p1Points-self.p2Points)*(self.p1Points-self.p2Points) == 1) else "Win for " + s
