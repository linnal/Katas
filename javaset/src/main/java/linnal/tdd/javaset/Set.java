package linnal.tdd.javaset;

public class Set<T>  {
    int size = 0;

    public void add(T item) {
        size += 1;
    }

    public int size() {
        return size;
    }

}
