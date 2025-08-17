package com.example;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class MainTest {
    @Test
    void testAppRuns() {
        assertTrue(true, "Basic test should pass");
    }

    @Test
    void testAddition() {
        assertEquals(5, 2 + 3, "2+3 should equal 5");
    }
}
