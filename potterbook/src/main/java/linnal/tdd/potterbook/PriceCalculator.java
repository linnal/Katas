package linnal.tdd.potterbook;

import java.util.Set;

public class PriceCalculator {

    ShoppingBasket shoppingBasket;

    public PriceCalculator(ShoppingBasket shoppingBasket){
        this.shoppingBasket = shoppingBasket;
    }


    public float price() {

        float price= 0;

        Set<Book> distinctBooks;
        float priceForDistinctBooks;
        float discount;

        while(!shoppingBasket.isEmpty()) {

            distinctBooks = shoppingBasket.distinctBooks();
            priceForDistinctBooks = sumPrices(distinctBooks);
            discount = discount(priceForDistinctBooks, distinctBooks.size());

            price += priceForDistinctBooks - discount;

            shoppingBasket.removeAll(distinctBooks);
        }

        return price;
    }

    private float sumPrices(Set<Book> books){
        float price = 0;

        for(Book book: books){
            price += book.price;
        }

        return price;
    }

    private float discount(float price, int series){
        switch (series){
            case 5:
                return price * 25f/100f;
            case 4:
                return price * 20f/100f;
            case 3:
                return price * 10f/100f;
            case 2:
                return price * 5f/100f;
            default:
                return 0;
        }
    }
}
