package linnal.tdd.potterbook;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;


public class TestShoppingBasket {

    ShoppingBasket shoppingBasket;

    @Before
    public void createBasket(){
        shoppingBasket = new ShoppingBasket();
    }

    @Test
    public void addFirstBookToTheBasket(){
        Book book = new Book(Series.FIRST, 8);
        shoppingBasket.add(book);

        Assert.assertTrue(shoppingBasket.contains(book));
    }

    @Test
    public void addSecondBookToTheBasket(){
        Book book = new Book(Series.SECOND, 8);
        shoppingBasket.add(book);

        Assert.assertTrue(shoppingBasket.contains(book));
    }

    @Test
    public void addSecondBookTwiceToTheBasket(){
        Book book = new Book(Series.SECOND, 8);
        shoppingBasket.add(book);
        shoppingBasket.add(book);

        Assert.assertTrue(shoppingBasket.contains(book));
        Assert.assertEquals(2, shoppingBasket.size());
    }

    @Test
    public void decreaseSizeWhenRemovingBookFromTheBasket(){
        Book first = new Book(Series.FIRST, 8);
        Book second = new Book(Series.SECOND, 8);
        shoppingBasket.add(first);
        shoppingBasket.add(first);
        shoppingBasket.add(second);

        Assert.assertEquals(3, shoppingBasket.size());

        shoppingBasket.remove(first);
        Assert.assertEquals(2, shoppingBasket.size());
    }

    @Test
    public void removingFromEmptyBasketHasNoAffect(){
        shoppingBasket.remove(new Book(Series.FIRST, 8));

        Assert.assertEquals(0, shoppingBasket.size());
    }

    @Test
    public void instancesOfTheSameBookSeriesShouldCountAsTheSameBook(){
        shoppingBasket.add(new Book(Series.FIRST, 8));
        shoppingBasket.add(new Book(Series.FIRST, 8));

        Assert.assertEquals(2, shoppingBasket.size());
        Assert.assertEquals(1, shoppingBasket.distinctBooks().size());
    }
}
