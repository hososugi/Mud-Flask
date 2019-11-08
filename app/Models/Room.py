

class Room:
    EXITS = {
        'North': 0,
        'East': 2,
        'South': 3,
        'West': 4,
        'Up': 5,
        'North': 6,
    }

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.description = kwargs.get('description', None)
        self.exits = kwargs.get('exits', None)