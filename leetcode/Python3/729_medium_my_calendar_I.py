"""
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.
A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).
The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.
Implement the MyCalendar class:
MyCalendar() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. 
Otherwise, return false and do not add the event to the calendar.


class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        if start is None or end is None or start >= end:
            return False  # Invalid input, treat as unsuccessful booking
        
        for item in self.calendar:
            # Check for overlap: if the new event starts before the current one ends,
            # and the new event ends after the current one starts
            if start < item[1] and end > item[0]:
                return False  # Overlap found, booking fails
            
        self.calendar.append([start, end])
        return True
"""
from sortedcontainers import SortedList

class MyCalendar:

    def __init__(self):
        self.calendar = SortedList()

    def book(self, start: int, end: int) -> bool:
        if start >= end:
            return False  # Invalid range
        
        idx = self.calendar.bisect_right((start, end))
        
        # Check the event before
        if idx > 0 and self.calendar[idx - 1][1] > start:
            return False
        
        # Check the event after
        if idx < len(self.calendar) and self.calendar[idx][0] < end:
            return False
        
        # If no overlap, insert the event
        self.calendar.add((start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
obj = MyCalendar()
params = []
params.append(obj.book(None, None))

params.append(obj.book(48, 50))
params.append(obj.book(0, 6))
params.append(obj.book(6, 13))
params.append(obj.book(8,13))
params.append(obj.book(15, 23))
params.append(obj.book(49, 50))
params.append(obj.book(45,50))
params.append(obj.book(29, 34))
params.append(obj.book(3, 12))
params.append(obj.book(38, 44))
print(params)

#[null,true,true,true,false,true,true,false,true,false,true]

#Expected: 
#[null,true,true,true,false,true,false,false,true,false,true]