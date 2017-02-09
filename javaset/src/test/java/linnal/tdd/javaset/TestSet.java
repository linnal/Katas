package linnal.tdd.javaset;

import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;


public class TestSet {

    Set<Object> set;

    @Before
    public void initializeSet(){
        set = new Set<>();
    }

    @Test
    public void addingSingleElementIncrisesSize(){
        set.add("bob");

        Assert.assertEquals(set.size(), 1);
    }

    @Test
    public void addingMultipleElementsIncreasesSize(){
        set.add("bob");
        set.add("alice");

        Assert.assertEquals(set.size(), 2);
    }

    @Test
    public void setContainsAddedElements(){
        set.add("bob");
        set.add("alice");

        Assert.assertTrue(set.contains("bob"));
        Assert.assertTrue(set.contains("alice"));
    }

    @Test
    public void emptySetDoesNotContainAnything(){
        Assert.assertFalse(set.contains("bob"));
    }

    @Test
    public void setContainsOnlyAddedElements(){
        set.add("bob");
        set.add("alice");

        Assert.assertTrue(set.contains("bob"));
        Assert.assertTrue(set.contains("alice"));
        Assert.assertFalse(set.contains("silvia"));
    }

    @Test
    public void deleteExistingElementInSet(){
        set.add("bob");
        set.add("alice");
        set.remove("bob");

        Assert.assertEquals(1, set.size());
        Assert.assertTrue(set.contains("alice"));
        Assert.assertFalse(set.contains("bob"));
    }

    @Test
    public void elementsAreAddedOnlyOnce(){
        set.add("bob");
        set.add("bob");

        Assert.assertEquals(1, set.size());
    }

    @Test
    public void setCanContainPersonObject(){
        Person bob = new Person("bob", 23);
        Person alice = new Person("alice", 23);
        set.add(bob);
        set.add(alice);

        Assert.assertEquals(2, set.size());
    }

    @Test
    public void setCanNotContainSamePersonObjectMoreThanOnce(){
        Person bob = new Person("bob", 23);
        set.add(bob);
        set.add(bob);

        Assert.assertEquals(1, set.size());
        Assert.assertTrue(set.contains(bob));
    }
}
