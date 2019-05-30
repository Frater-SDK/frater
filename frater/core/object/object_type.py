from enum import Enum

__long_names__ = ['Null', 'Person', 'Vehicle', 'Door', 'Prop',
                  'Push_Pulled_Object', 'Other', 'Bike', 'Parking_Meter', 'Tree']


class ObjectType(Enum):
    """
    Object Types for DIVA
    """
    NULL = 0  # Null
    PERSON = 1  # Person
    VEHICLE = 2  # Vehicle
    DOOR = 3  # Door
    PROP = 4  # Prop
    PULLED_OBJECT = 5  # Pushed_Pulled_Object
    OTHER = 6  # Other
    BIKE = 7  # Bike
    PARKING_METER = 8  # Parking_Meter
    TREE = 9

    # sub groups
    TRANSPORT_OBJECTS = {PROP, PULLED_OBJECT, OTHER}
    INTERACT_OBJECTS = {PROP, PULLED_OBJECT, OTHER, PARKING_METER}
    RIDING_OBJECTS = {BIKE}

    @property
    def long_name(self):
        return __long_names__[int(self.value)]

    @classmethod
    def from_long_name(cls, long_name: str) -> 'ObjectType':
        return ObjectType(__long_names__.index(long_name))
