package com.xp.test

/**
 * Created by linnal on 4/5/16.
 */
class Game {

    var rolls = Array(21, {i -> 0})
    var currentRoll = 0

    fun roll(pins: Int) {
        rolls[currentRoll++] = pins
    }

    fun score(): Int {
        var score = 0
        var indexFrame = 0;

        for(frame in 1..10){

            if(isStrike(indexFrame)){
                score += 10 + strikeBonus(indexFrame)
                indexFrame++
            }else{
                score += if(isSpare(indexFrame)) 10 + spareBonus(indexFrame) else sumOfBallsInFrame(indexFrame)
                indexFrame += 2
            }
        }

        return score
    }

    fun isSpare(indexframe : Int): Boolean = rolls.get(indexframe) + rolls.get(indexframe+1) == 10
    fun isStrike(indexframe : Int): Boolean = rolls.get(indexframe) == 10
    fun sumOfBallsInFrame(indexframe : Int): Int = rolls.get(indexframe) + rolls.get(indexframe+1)
    fun spareBonus(indexframe : Int): Int = rolls.get(indexframe+2)
    fun strikeBonus(indexframe : Int): Int = rolls.get(indexframe+1) + rolls.get(indexframe+2)
}