from abc import ABC, abstractmethod

class Event(ABC):
    def __init__(self, event_name, event_date, event_time, venue_name, total_seats, available_seats, ticket_price, event_type):
        self.event_name = event_name
        self.event_date = event_date
        self.event_time = event_time
        self.venue_name = venue_name
        self.total_seats = total_seats
        self.available_seats = available_seats
        self.ticket_price = ticket_price
        self.event_type = event_type

    @abstractmethod
    def display_event_details(self):
        pass

    @abstractmethod
    def book_tickets(self, num_tickets):
        pass

    @abstractmethod
    def cancel_tickets(self, num_tickets):
        pass

    @abstractmethod
    def get_available_seats(self):
        pass

class Movie(Event):
    def __init__(self, event_name, event_date, event_time, venue_name, total_seats, available_seats, ticket_price, event_type):
        super().__init__(event_name, event_date, event_time, venue_name, total_seats, available_seats, ticket_price, event_type)

    def display_event_details(self):
        print("Movie Details:")
        print(f"Event Name: {self.event_name}")
        print(f"Date: {self.event_date}")
        print(f"Time: {self.event_time}")
        print(f"Venue: {self.venue_name}")
        print(f"Available Seats: {self.available_seats}")
        print(f"Ticket Price: {self.ticket_price}")

    def book_tickets(self, num_tickets):
        if self.available_seats >= num_tickets:
            self.available_seats -= num_tickets
            print(f"{num_tickets} tickets booked for the movie: {self.event_name}")
        else:
            print("Not enough available seats.")

    def cancel_tickets(self, num_tickets):
        self.available_seats += num_tickets
        print(f"{num_tickets} tickets cancelled for the movie: {self.event_name}")

    def get_available_seats(self):
        return self.available_seats

class Concert(Event):
    def __init__(self, event_name, event_date, event_time, venue_name, total_seats, available_seats, ticket_price, event_type):
        super().__init__(event_name, event_date, event_time, venue_name, total_seats, available_seats, ticket_price, event_type)

    def display_event_details(self):
        print("Concert Details:")
        print(f"Event Name: {self.event_name}")
        print(f"Date: {self.event_date}")
        print(f"Time: {self.event_time}")
        print(f"Venue: {self.venue_name}")
        print(f"Available Seats: {self.available_seats}")
        print(f"Ticket Price: {self.ticket_price}")

    def book_tickets(self, num_tickets):
        if self.available_seats >= num_tickets:
            self.available_seats -= num_tickets
            print(f"{num_tickets} tickets booked for the concert: {self.event_name}")
        else:
            print("Not enough available seats.")

    def cancel_tickets(self, num_tickets):
        self.available_seats += num_tickets
        print(f"{num_tickets} tickets cancelled for the concert: {self.event_name}")

    def get_available_seats(self):
        return self.available_seats

class Sport(Event):
    def __init__(self, event_name, event_date, event_time, venue_name, total_seats, available_seats, ticket_price, event_type):
        super().__init__(event_name, event_date, event_time, venue_name, total_seats, available_seats, ticket_price, event_type)

    def display_event_details(self):
        print("Sport Event Details:")
        print(f"Event Name: {self.event_name}")
        print(f"Date: {self.event_date}")
        print(f"Time: {self.event_time}")
        print(f"Venue: {self.venue_name}")
        print(f"Available Seats: {self.available_seats}")
        print(f"Ticket Price: {self.ticket_price}")

    def book_tickets(self, num_tickets):
        if self.available_seats >= num_tickets:
            self.available_seats -= num_tickets
            print(f"{num_tickets} tickets booked for the sport event: {self.event_name}")
        else:
            print("Not enough available seats.")

    def cancel_tickets(self, num_tickets):
        self.available_seats += num_tickets
        print(f"{num_tickets} tickets cancelled for the sport event: {self.event_name}")

    def get_available_seats(self):
        return self.available_seats

class BookingSystem(ABC):
    @abstractmethod
    def create_event(self):
        pass

    @abstractmethod
    def book_tickets(self):
        pass

    @abstractmethod
    def cancel_tickets(self):
        pass

    @abstractmethod
    def get_available_seats(self):
        pass

class TicketBookingSystem(BookingSystem):
    def __init__(self):
        self.events = []

    def create_event(self, event):
        self.events.append(event)
        print(f"{event.event_name} created successfully.")

    def book_tickets(self, event_name, num_tickets):
        for event in self.events:
            if event.event_name == event_name:
                event.book_tickets(num_tickets)
                return
        print(f"Event '{event_name}' not found.")

    def cancel_tickets(self, event_name, num_tickets):
        for event in self.events:
            if event.event_name == event_name:
                event.cancel_tickets(num_tickets)
                return
        print(f"Event '{event_name}' not found.")

    def get_available_seats(self, event_name):
        for event in self.events:
            if event.event_name == event_name:
                return event.get_available_seats()
        print(f"Event '{event_name}' not found.")

# Main method for user interaction
if __name__ == "__main__":
    ticket_booking_system = TicketBookingSystem()
    while True:
        print("\nTicket Booking System Menu:")
        print("1. Create Event")
        print("2. Book Tickets")
        print("3. Cancel Tickets")
        print("4. Get Available Seats")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            event_name = input("Enter the event name: ")
            event_date = input("Enter the event date: ")
            event_time = input("Enter the event time: ")
            venue_name = input("Enter the venue name: ")
            total_seats = int(input("Enter the total number of seats: "))
            available_seats = int(input("Enter the available number of seats: "))
            ticket_price = float(input("Enter the ticket price: "))
            event_type = input("Enter the event type (Movie/Concert/Sport): ")

    if event_type.lower() == "movie":
        event = Movie(event_name, event_date, event_time, venue_name, total_seats, available_seats, ticket_price, event_type)
    elif event_type.lower() == "concert":
        event = Concert(event_name, event_date, event_time, venue_name, total_seats, available_seats, ticket_price, event_type)
    elif event_type.lower() == "sport":
        event = Sport(event_name, event_date, event_time, venue_name, total_seats, available_seats, ticket_price, event_type)
    else:
        print("Invalid event type. Event not created.")
       
    
    ticket_booking_system.create_event(event)
