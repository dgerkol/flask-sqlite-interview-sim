class User:
    def __init__(self, id_AI, full_name, password, real_id):
        self.user = id_AI
        self.name = full_name
        self.password = password
        self.id = real_id
    
    @property
    def data(self):
        return self.__dict__


class Ticket:
    def __init__(self, ticket_id, user_id, flight_id):
        self.ticket = ticket_id
        self.user = user_id
        self.flight = flight_id
    
    @property
    def data(self):
        return self.__dict__


class Flight:
    def __init__(self, flight_id, timestamp, remaining_seats, origin_country_id, dest_country_id):
        self.flight = flight_id
        self.timestamp = timestamp
        self.remaining_seats = remaining_seats
        self.origin = origin_country_id
        self.dest = dest_country_id
    
    @property
    def data(self):
        return self.__dict__


class Country:
    def __init__(self, code_AI, name):
        self.code = code_AI
        self.name = name
    
    @property
    def data(self):
        return self.__dict__



