class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top = top
        self.current = current
        pass
    def up(self):
        """Makes the elevator go up one floor."""
        if self.current < self.top:
            self.current += 1
        pass
    def down(self):
        """Makes the elevator go down one floor."""
        if self.current > self.bottom:
            self.current -= 1
        pass
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        self.current = floor
        pass
    def __str__(self):
        """Displays current floor when class printed"""
        return "Current floor: {}".format(self.current)
elevator = Elevator(-1, 10, 0)
