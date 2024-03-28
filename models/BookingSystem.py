from abc import ABC, abstractmethod
from typing import List
from datetime import datetime
from models.event import event
from models.customer import customer
from models.venue import venue

class BookingSystem(ABC):
    def __init__(self):
        self.events = []

    @abstractmethod
    def create_event(self, event_name: str, date: str, time: str, total_seats: int, ticket_price: float, event_type: str, venue: venue) -> event:
        pass

    @abstractmethod
    def calculate_booking_cost(self, num_tickets: int) -> float:
        pass

    @abstractmethod
    def book_tickets(self, event_name: str, num_tickets: int, array_of_customer: List[customer]):
        pass

    @abstractmethod
    def cancel_booking(self, booking_id: int):
        pass

    @abstractmethod
    def get_available_no_of_tickets(self) -> int:
        pass

    @abstractmethod
    def get_event_details(self) -> event:
        pass

class TicketBookingSystem(BookingSystem):
    def create_event(self, event_name: str, date: str, time: str, total_seats: int, ticket_price: float, event_type: str, venue: venue) -> event:
        event = event(event_name, datetime.strptime(date, '%Y-%m-%d').date(), time, venue, total_seats, total_seats, ticket_price, event_type)
        self.events.append(event)
        return event

    def calculate_booking_cost(self, num_tickets: int) -> float:
        # Assuming ticket price is fixed for all events
        return num_tickets * self.events[0].ticket_price  # Assuming all events have the same ticket price

    def book_tickets(self, event_name: str, num_tickets: int, array_of_customer: List[customer]):
        for event in self.events:
            if event.event_name == event_name:
                if event.available_seats >= num_tickets:
                    event.available_seats -= num_tickets
                    # Create customer objects and store in array_of_customer
                    for _ in range(num_tickets):
                        array_of_customer.append(customer())
                    print(f"{num_tickets} tickets booked for the event: {event_name}")
                    return
                else:
                    print("Not enough available seats.")
                    return
        print(f"Event '{event_name}' not found.")

    def cancel_booking(self, booking_id: int):
        # Implementation to cancel booking and update available seats
        pass

    def get_available_no_of_tickets(self) -> int:
        total_available_tickets = sum(event.available_seats for event in self.events)
        return total_available_tickets

    def get_event_details(self) -> event:
        # Assuming returning details of the first event in the list
        return self.events[0]


if __name__ == "__main__":
    ticket_booking_system = TicketBookingSystem()
    array_of_customer = []

    while True:
        print("\nTicket Booking System Menu:")
        print("1. Create Event")
        print("2. Book Tickets")
        print("3. Cancel Booking")
        print("4. Get Available Seats")
        print("5. Get Event Details")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            event_name = input("Enter event name: ")
            date = input("Enter event date (YYYY-MM-DD): ")
            time = input("Enter event time: ")
            total_seats = int(input("Enter total seats: "))
            ticket_price = float(input("Enter ticket price: "))
            event_type = input("Enter event type: ")
            venue = input("Enter venue: ")
            ticket_booking_system.create_event(event_name, date, time, total_seats, ticket_price, event_type, venue)
            print("Event created successfully.")

        elif choice == "2":
            event_name = input("Enter event name: ")
            num_tickets = int(input("Enter number of tickets to book: "))
            ticket_booking_system.book_tickets(event_name, num_tickets, array_of_customer)

        elif choice == "3":
            # Implement cancel booking functionality
            pass

        elif choice == "4":
            available_seats = ticket_booking_system.get_available_no_of_tickets()
            print(f"Total available seats: {available_seats}")

        elif choice == "5":
            event_details = ticket_booking_system.get_event_details()
            print("Event Details:")
            print(event_details)

        elif choice == "6":
            print("Exiting the Ticket Booking System.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")
