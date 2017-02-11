package linnal.tdd.potterbook;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

public class TestPriceCalculator {

    ShoppingBasket shoppingBasket;
    PriceCalculator priceCalculator;

    @Before
    public void init(){
        shoppingBasket = new ShoppingBasket();
        priceCalculator = new PriceCalculator(shoppingBasket);
    }

    @Test
    public void shouldReturnRealPriceForASingleBook(){
        shoppingBasket.add(new Book(Series.FIRST, 8));

        float price = priceCalculator.price();

        Assert.assertEquals(8, price, 0.0f);
    }

    @Test
    public void shouldSumPriceForSameBooks(){
        shoppingBasket.add(new Book(Series.FIRST, 8));
        shoppingBasket.add(new Book(Series.FIRST, 8));

        float price = priceCalculator.price();

        Assert.assertEquals(16, price, 0.0f);
    }

    @Test
    public void shouldDiscountFor2DifferentBooks(){
        shoppingBasket.add(new Book(Series.FIRST, 8));
        shoppingBasket.add(new Book(Series.SECOND, 8));

        float price = priceCalculator.price();
        float discount = (16f * 5f/100f);
        float expectedPrice = 16f - discount;

        Assert.assertEquals(expectedPrice, price, 0.0f);
    }

    @Test
    public void shouldDiscountOnlyFor2DifferentBooks(){
        shoppingBasket.add(new Book(Series.FIRST, 8));
        shoppingBasket.add(new Book(Series.FIRST, 8));
        shoppingBasket.add(new Book(Series.SECOND, 8));

        float price = priceCalculator.price();
        float discount = (16f * 5f/100f);
        float expectedPrice = 16f - discount + 8f;

        Assert.assertEquals(expectedPrice, price, 0.0f);
    }

    @Test
    public void multipleDiscountsCaseOne(){
        shoppingBasket.add(new Book(Series.FIRST, 8));
        shoppingBasket.add(new Book(Series.FIRST, 8));
        shoppingBasket.add(new Book(Series.SECOND, 8));
        shoppingBasket.add(new Book(Series.SECOND, 8));
        shoppingBasket.add(new Book(Series.THIRD, 8));
        shoppingBasket.add(new Book(Series.THIRD, 8));
        shoppingBasket.add(new Book(Series.FOURTH, 8));
        shoppingBasket.add(new Book(Series.FIFTH, 8));

        float price = priceCalculator.price();

        Assert.assertEquals(51.6, price, 0.01f);
    }

    @Test
    public void multipleDiscountsCaseTwo(){
        shoppingBasket.add(new Book(Series.FIRST, 8));
        shoppingBasket.add(new Book(Series.FIRST, 8));
        shoppingBasket.add(new Book(Series.FIRST, 8));
        shoppingBasket.add(new Book(Series.SECOND, 8));
        shoppingBasket.add(new Book(Series.SECOND, 8));
        shoppingBasket.add(new Book(Series.THIRD, 8));
        shoppingBasket.add(new Book(Series.THIRD, 8));
        shoppingBasket.add(new Book(Series.THIRD, 8));
        shoppingBasket.add(new Book(Series.THIRD, 8));
        shoppingBasket.add(new Book(Series.FOURTH, 8));
        shoppingBasket.add(new Book(Series.FOURTH, 8));
        shoppingBasket.add(new Book(Series.FIFTH, 8));

        float price = priceCalculator.price();

        Assert.assertEquals(78.79, price, 0.01f);
    }

}
