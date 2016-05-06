package com.xp.test

import org.junit.Assert
import org.junit.Test

/**
 * Created by linnal on 4/5/16.
 */
class BowlingGameTest {

    var g = Game()

    @Test fun testGutterGame(){
        rollMany(20, 0)
        Assert.assertEquals(0, g.score())
    }

    @Test fun testAllOnes(){
        rollMany(20, 1)
        Assert.assertEquals(20, g.score())
    }

    @Test fun testOneSpare(){
        rollSpare()
        g.roll(3)
        rollMany(17, 0)
        Assert.assertEquals(16, g.score())
    }

    @Test fun testOneStrike(){
        rollStrike()
        g.roll(3);
        g.roll(4);
        rollMany(16, 0);
        Assert.assertEquals(24, g.score());
    }

    @Test fun testPerfectGame(){
        rollMany(12,10);
        Assert.assertEquals(300, g.score());
    }

    fun rollMany(n: Int, pins: Int){
        for( i in 1..n){
            g.roll(pins)
        }
    }

    fun rollSpare(){
        g.roll(5)
        g.roll(5)
    }

    fun rollStrike(){
        g.roll(10);
    }

}