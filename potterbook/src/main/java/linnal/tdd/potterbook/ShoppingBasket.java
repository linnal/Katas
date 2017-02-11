package linnal.tdd.potterbook;

import java.util.*;

/**
 * Created by linnal on 2/10/17.
 */
public class ShoppingBasket {

    HashMap<Book, Integer> books = new HashMap<Book, Integer>();

    public void add(Book book) {
        int count = books.getOrDefault(book, 0);
        books.put(book, count + 1);
    }

    public boolean contains(Book book) {
        return books.containsKey(book);
    }

    public int size() {
        int count = 0;
        for(int quantity: books.values()){
            count += quantity;
        }
        return count;
    }

    public boolean remove(Book book) {
        if(isASingleBook(book)){
            books.remove(book);
            return true;
        }

        if(books.containsKey(book)) {
            books.put(book, books.get(book) - 1);
            return true;
        }

        return false;
    }

    public void removeAll(Set<Book> books){
        for(Book book: books){
            remove(book);
        }
    }

    public Set<Book> distinctBooks() {
        Set<Book> setBooks = new HashSet<Book>();
        setBooks.addAll(books.keySet());
        return setBooks;
    }

    public boolean isEmpty(){
        return size() == 0;
    }

    private boolean isASingleBook(Book book){
        return books.containsKey(book) && books.get(book) == 1;
    }

}

