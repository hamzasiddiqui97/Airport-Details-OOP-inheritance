class Airplane:
    def __init__(self, passenger_id, passenger_name, seat_no, flight_time):
        self.passenger_id = passenger_id
        self.passenger_name = passenger_name
        self.seat_no = seat_no
        self.flight_time = flight_time

    def airplane_details(self):
        print("About Airplane")


class PIA(Airplane):
    def __init__(self, passenger_id, passenger_name, seat_no, flight_time, plane_class):
        Airplane.__init__(self, passenger_id, passenger_name, seat_no, flight_time)
        self.plane_class = plane_class

    def pia_details(self):
        print("Your id: ", self.passenger_id, "\nName :", self.passenger_name.title(), "\nSeat #: ", self.seat_no,
              "\nClass: ", self.plane_class.title(), "\nTimings: ", self.flight_time)
        print(20 * "-")


class Shaheen(Airplane):
    def __init__(self, passenger_id, passenger_name, seat_no, flight_time, plane_class, special_discount,
                 type_of_ticket):
        Airplane.__init__(self, passenger_id, passenger_name, seat_no, flight_time)
        self.plane_class = plane_class
        self.special_discount = special_discount
        self.type_of_ticket = type_of_ticket

    def shaheen_details(self):
        print("Your id: ", self.passenger_id, "\nName :", self.passenger_name.title(), "\nSeat #: ", self.seat_no,
              "\nClass: ", self.plane_class.title(), "\nSpeacial 'Shaheen Airways' Discount: ", self.special_discount,
              "\nTimings: ", self.flight_time, "\nType: ", self.type_of_ticket.title())
        print(20 * "-")


pia_object = PIA(100400, 'hamza siddiqui', 1075421, '01:00', 'Business Class')
pia_object.pia_details()
shaheen_object = Shaheen(91023456712, 'haris ahmed', 9002341, '22:00', 'Economy Class', "20%", 'Return ticket')
shaheen_object.shaheen_details()


