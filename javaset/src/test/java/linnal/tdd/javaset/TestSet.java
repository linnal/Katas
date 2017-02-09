package linnal.tdd.javaset;

import org.junit.Assert;
import org.junit.Test;

public class TestSet {

    @Test
    public void addingSingleElementIncrisesSize(){
        Set<Object> set = new Set<>();

        set.add("bob");

        Assert.assertEquals(set.size(), 1);
    }
}
