package linnal.tdd.potterbook;

import org.junit.Assert;
import org.junit.Test;

/**
 * Created by linnal on 2/10/17.
 */
public class TestBook {

    @Test
    public void booksOfTheSameSeriesAreEquals(){
        Book first = new Book(Series.FIRST, 8);
        Book second = new Book(Series.FIRST, 8);

        Assert.assertTrue(first.equals(second));
    }
}
