from DB_Connection.db_adapter import *
from models.event import Event
import pyodbc

class BookingSystem:
    def __init__(self):
        self.connection = get_db_connection()

    def display_menu(self):
        print("1. Book Tickets")
        print("2. Cancel Booking")
        print("3. View Event Details")
        print("4. Exit")

    def book_tickets(self):
        num_tickets = int(input("Enter the number of tickets to book: "))
        customer_id = int(input('Enter the customer id: '))
        event_id = input('Enter the event ID: ')
        temp_event = self.get_event_by_id(event_id)
        try:
            # Assuming Event class has a method named 'book_tickets'
            temp_event.book_tickets(customer_id, num_tickets, event_id, temp_event.get_ticket_price())
            print('Ticket Booked Successfully')
        except Exception as e:
            print(f"Error: {e}")

    def get_event_by_id(self, event_id):
        try:
            my_cursor = self.connection.cursor()
            sql = '''
                SELECT * from event where event_id = ?
            '''
            para = (event_id,)
            my_cursor.execute(sql, para)
            row = my_cursor.fetchone()
            if row:
                # Assuming Event class has a constructor that matches the columns returned from the query
                return Event(*row)
            else:
                print("Event not found")
                return None
        except Exception as e:
            print(f'An error occurred: {e}')

    def cancel_booking(self):
        event_id = input('Enter the event ID booking to cancel: ')
        booking_id = input("Enter the booking ID to cancel: ")
        temp_event = self.get_event_by_id(event_id)
        try:
            # Assuming Event class has a method named 'cancel_booking'
            temp_event.cancel_booking(booking_id)
            print('Booking Cancelled Successfully')
        except Exception as e:
            print(f"Error: {e}")

    def view_event_details(self):
        event_id = input("Enter the event ID to view details: ")
        try:
            my_cursor = self.connection.cursor()
            sql = '''
            SELECT * from event where event_id = ?
            '''
            para = (event_id,)
            my_cursor.execute(sql, para)
            row = my_cursor.fetchone()
            if row:
                # Assuming Event class has a constructor that matches the columns returned from the query
                event = Event(*row)
                event.display_event_details()
            else:
                print("Event not found")
        except Exception as e:
            print(f"Error: {e}")
