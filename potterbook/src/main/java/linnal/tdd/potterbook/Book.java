package linnal.tdd.potterbook;

/**
 * Created by linnal on 2/10/17.
 */


public class Book {

    Series series;
    int price;

    public Book(Series series, int price) {
        this.series = series;
        this.price = price;
    }

    @Override
    public boolean equals(Object obj) {
        Book otherBook = (Book) obj;
        return otherBook.series == series;
    }

    @Override
    public int hashCode() {
        return series.hashCode();
    }

}
