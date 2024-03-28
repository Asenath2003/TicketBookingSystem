from typing import Set

class BookingSystem(ABC):
    def __init__(self):
        self.events: Set[Event] = set()

    def create_event(self, event_name: str, date: str, time: str, total_seats: int, ticket_price: float, event_type: str, venue: Venue) -> Event:
        event = Event(event_name, datetime.strptime(date, '%Y-%m-%d').date(), time, venue, total_seats, total_seats, ticket_price, event_type)
        self.events.add(event)
        return event

    def book_tickets(self, event_name: str, num_tickets: int, array_of_customer: List[Customer]):
        for event in self.events:
            if event.event_name == event_name:
                if event.available_seats >= num_tickets:
                    event.available_seats -= num_tickets
                    for _ in range(num_tickets):
                        array_of_customer.append(Customer())
                    print(f"{num_tickets} tickets booked for the event: {event_name}")
                    return
                else:
                    print("Not enough available seats.")
                    return
        print(f"Event '{event_name}' not found.")

    # Implement other methods similarly
