"""
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a triple booking.

A triple booking happens when three events have some non-empty intersection (i.e., some moment is common to all the three events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendarTwo class:

MyCalendarTwo() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.
 
"""
class MyCalendar:
    def __init__(self):
        self.calendar = []  # Tracks single bookings
        self.double_booked = []  # Tracks double bookings

    def book(self, start: int, end: int) -> bool:
        if start is None or end is None or start >= end:
            return False  # Invalid input, treat as unsuccessful booking

        # Check for overlap with double_booked events first (to prevent triple booking)
        for event in self.double_booked:
            if start < event[1] and end > event[0]:
                return False  # Overlap with a double-booked event, booking fails (triple booking)

        # Check for overlap with single bookings to track double bookings
        for event in self.calendar:
            if start < event[1] and end > event[0]:
                # Add overlapping part to double_booked
                self.double_booked.append([max(start, event[0]), min(end, event[1])])

        # Add the event to single bookings if no triple booking found
        self.calendar.append([start, end])
        return True

obj = MyCalendar()
params = []

params.append(obj.book(10, 20))
params.append(obj.book(50, 60))
params.append(obj.book(10, 40))
params.append(obj.book(5, 15))
params.append(obj.book(5, 10))
params.append(obj.book(25, 55))

print(params)