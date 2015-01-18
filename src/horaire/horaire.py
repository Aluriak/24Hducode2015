
import datetime



class Horaire():
    """
    Save only hours and minutes.
    Provide some counts.
    Take silently count of passed day
    """

    def __init__(self, h=0, m=0):
        self.h, self.m = h, m
        self.days = 0 # incremented when a day pass
        self._normalize()


    def __add__(self, othr):
        """
        add to another Horaire object.
        return a new object in all cases.
        """
        assert(isinstance(othr, Horaire))
        return Horaire(self.h + othr.h, self.m + othr.m)


    def __eq__(self, othr):
        """
        Return True iff othr have the same h and m 
        attributes
        """
        return self.h == othr.h and self.m == othr.m


    def __str__(self):
        return str(self.h) + ':' + str(self.m)


    def add_minutes(self, minutes):
        """
        Return new Horaire object that have minutes more minutes.
        """
        return self + Horaire(m=minutes)

    
    def is_after(self, othr):
        """
        Return True iff self is after (more hour, more minutes) othr,
        or equal to it.
        """
        assert(isinstance(othr, Horaire))
        if self.h > othr.h:
            return True
        elif self.h == othr.h and self.m >= self.h:
            return True
        return False

    
    def is_before(self, othr):
        """
        Return True iff self is before (less hour, less minutes) othr,
        or equal to it.
        """
        assert(isinstance(othr, Horaire))
        if self.h < othr.h:
            return True
        elif self.h == othr.h and self.m <= self.h:
            return True
        return False
        

    def _normalize(self):
        """
        normalize self for have at most 24h and 59mn
        """
        self.h += self.m // 60
        self.m %= 60
        self.days += self.h // 24
        self.h %= 24


    def as_minutes(self):
        """Return self as an amount of minutes (integer)"""
        return self.h * 60 + self.m


    @staticmethod
    def from_server_dialect(server_dialect):
        """
        from given time format (returned by server):
            2015-03-18T04:44:00+00:00
        creat and return a new Horaire object
        """
        time = datetime.datetime.strptime(server_dialect, '%Y-%m-%dT%H:%M:%S+00:00')
        return Horaire(h=time.hour, m=time.minute)


    @staticmethod
    def from_schedules_dialect(schedules_dialect):
        """
        from given time format (used by schedules):
            44:00:00
        creat and return a new Horaire object
        """
        time = datetime.datetime.strptime(schedules_dialect, '%H:%M:%S')
        return Horaire(h=time.hour, m=time.minute)


    def to_server_dialect(self, day, month, year):
        """
        return self in this time format (expected by server for move):
            2015-03-18 04:44:00
        """
        # TODO use arrow module for add self.day to day properly
        return datetime.datetime(year=year, month=month, day=self.day+day, hour=self.h, minute=self.m).strftime('%d %a %H:%M:%S %Y')






if __name__ == '__main__':
    h1 = Horaire(4, 30)
    h2 = Horaire(4, 30)
    assert((h1 + h2) == Horaire(9, 0))
    print(h1.as_minutes())
    print(h1.to_server_dialect(2, 11, 2015))
    print(Horaire.from_server_dialect('2015-03-18T04:44:00+00:00'))
    print(Horaire.from_schedules_dialect('04:44:05'))





# here are defined many useless functions

def add_minutes(travel_time, minutes):
    """
    Wait for a datetime like 
        HH:MM:SS
    and add the given integer minutes as minutes
    finally, return the new time
    """
    travel_time = datetime.datetime.strptime(datetime.datetime.strptime(travel_time, '%Y-%m-%d %H:%M:%S').strftime('%H:%M:%S'), '%H:%M:%S')
    minutes     = datetime.datetime.strptime(str(minutes), '%M')
    minutes     = datetime.timedelta(hours=minutes.hour, minutes=minutes.minute, seconds=minutes.second)
    #print(minutes, minutes.__class__)
    #print(travel_time, travel_time.__class__)
    #print(minutes + travel_time)
    return minutes + travel_time




def date_to_minute(travel_time):
    """
    Wait for a datetime like 
        HH:MM:SS
    and return this date in minute
    """
    travel_time = datetime.datetime.strptime(datetime.datetime.strptime(travel_time, '%Y-%m-%d %H:%M:%S').strftime('%H:%M:%S'), '%H:%M:%S')
    return travel_time.hour*60 + travel_time.minute



def minute_to_date(minutes):
    """
    Take integer as minute number
    Return an equivalent datetime like 
        HH:MM:SS
    """
    travel_time = datetime.datetime.strptime(datetime.datetime.strptime(travel_time, '%H:%M:%S').strftime('%H:%M:%S'), '%H:%M:%S')
    return travel_time.hour*60 + travel_time.minute


