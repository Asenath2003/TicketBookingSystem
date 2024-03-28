from datetime import date, time
from models.event import event

class Movie(event):
    def __init__(self, event_name, event_date, event_time,
                 venue_name, total_seats, ticket_price, event_type,
                 genre, actor_name, actress_name):
        super().__init__(event_name, event_date, event_time,
                         venue_name, total_seats, ticket_price, event_type)
        self._genre = genre
        self._actor_name = actor_name
        self._actress_name = actress_name


    def display_event_details(self):
        super().display_event_details()
        print(f"Genre: {self._genre}")
        print(f"Actor: {self._actor_name}")
        print(f"Actress: {self._actress_name}")


if __name__ == "__main__":
    movie = Movie("Music concert", date(2024, 3, 15), time(18, 30), "Concert Hall A", 500, 50.00, "Concert", "Melody", "ABC", "XYZ")
    #movie.display_event_details()