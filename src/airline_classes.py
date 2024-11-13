class Flight:

    def __init__(self):
        self.flight_id = 0
        self.aircraft_id = 0
        self.pilot_id = 0
        self.flight_origin = ''
        self.flight_destination = ''
        self.flight_status = ''

    # Attributte setters
    def set_flight_id(self, flight_id):
        self.flight_id = flight_id

    def set_aircraft_id(self, aircraft_id):
        self.aircraft_id = aircraft_id

    def set_pilot_id(self, pilot_id):
        self.pilot_id = pilot_id

    def set_flight_origin(self, flight_origin):
        self.flight_origin = flight_origin

    def set_flight_destination(self, flight_destination):
        self.flight_destination = flight_destination

    def set_flight_status(self, flight_status):
        self.flight_status = flight_status

    # Attributte getters
    def get_flight_id(self):
        return self.flight_id

    def get_aircraft_id(self):
        return self.aircraft_id

    def get_pilot_id(self):
        return self.pilot_id

    def get_flight_origin(self):
        return self.flight_origin

    def get_flight_destination(self):
        return self.flight_destination

    def get_flight_status(self):
        return self.flight_status

    # String representation of the object
    def __str__(self):
        return (str(self.flight_id) + "\n" +
                str(self.aircraft_id) + "\n" +
                str(self.pilot_id) + "\n" +
                self.flight_origin + "\n" +
                self.flight_destination + "\n" +
                self.flight_status)


class Aircraft:

    def __init__(self):
        self.aircraft_id = 0
        self.aircraft_name = ''
        self.aircraft_type = ''
        self.aircraft_capacity = ''
        self.aircraft_status = ''

    # Attributte setters
    def set_aircraft_id(self, aircraft_id):
        self.aircraft_id = aircraft_id

    def set_aircraft_name(self, aircraft_name):
        self.aircraft_name = aircraft_name

    def set_aircraft_type(self, aircraft_type):
        self.aircraft_type = aircraft_type

    def set_aircraft_capacity(self, aircraft_capacity):
        self.aircraft_capacity = aircraft_capacity

    def set_aircraft_status(self, aircraft_status):
        self.aircraft_status = aircraft_status

    # Attributte getters
    def get_aircraft_id(self):
        return self.aircraft_id

    def get_aircraft_name(self):
        return self.aircraft_name

    def get_aircraft_type(self):
        return self.aircraft_type

    def get_aircraft_capacity(self):
        return self.aircraft_capacity

    def get_aircraft_status(self):
        return self.aircraft_status

    # String representation of the object
    def __str__(self):
        return (str(self.aircraft_id) + "\n" +
                self.aircraft_name + "\n" +
                self.aircraft_type + "\n" +
                str(self.aircraft_capacity) + "\n" +
                self.aircraft_status)


class Pilot:

    def __init__(self):
        self.pilot_id = 0
        self.first_name = ''
        self.last_name = ''
        self.date_of_birth = ''
        self.pilot_license = ''
        self.contact_number = ''

    # Attributte setters
    def set_pilot_id(self, pilot_id):
        self.pilot_id = pilot_id

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_date_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth

    def set_pilot_license(self, pilot_license):
        self.pilot_license = pilot_license

    def set_contact_number(self, contact_number):
        self.contact_number = contact_number

    # Attributte getters
    def get_pilot_id(self):
        return self.pilot_id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_date_of_birth(self):
        return self.date_of_birth

    def get_pilot_license(self):
        return self.pilot_license

    def get_contact_number(self):
        return self.contact_number

    # String representation of the object
    def __str__(self):
        return (str(self.pilot_id) + "\n" +
                self.first_name + "\n" +
                self.last_name + "\n" +
                self.date_of_birth + "\n" +
                self.pilot_license + "\n" +
                self.contact_number)
