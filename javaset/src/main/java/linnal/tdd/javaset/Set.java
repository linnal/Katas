package linnal.tdd.javaset;

import java.util.ArrayList;

public class Set<T> {

    ArrayList<T> items = new ArrayList<>();

    public void add(T item) {
        if(contains(item))
            return;
        items.add(item);
    }

    public int size() {
        return items.size();
    }

    public boolean contains(T item) {
        return items.contains(item);
    }

    public void remove(T item) {
        items.remove(item);
    }
}
