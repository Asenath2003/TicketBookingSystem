def book_tickets(availabletickets, no_of_booking_tickets):
    if available_tickets >= no_of_booking_tickets:
        remaining_tickets = available_tickets - no_of_booking_tickets
        print("Tickets booked!!")
    else:
        print("Tickets unavailable")

available_tickets = int(input("Enter the number of available tickets: "))
no_of_booking_tickets = int(input("Enter the number of tickets you want to book: "))

book_tickets(available_tickets, no_of_booking_tickets)
