from enum import Enum

__long_names__ = ['Null',
                  'Person Opens Facility Door',
                  'Person Closes Facility Door',
                  'Person Enters Through Structure',
                  'Person Exits Through Structure',
                  'Person Opens Vehicle Door',
                  'Person Closes Vehicle Door',
                  'Person Enters Vehicle',
                  'Person Exits Vehicle',
                  'Person Opens Trunk',
                  'Person Closes Trunk',
                  'Person Loads Vehicle',
                  'Person Unloads Vehicle',
                  'People Talking',
                  'Person Talking on Phone',
                  'Person Texting on Phone',
                  'Riding',
                  'Vehicle Turning Left',
                  'Vehicle Turning Right',
                  'Vehicle U-Turn',
                  'Person Sitting Down',
                  'Person Standing Up',
                  'Person Reading Document',
                  'Object Transfer',
                  'Person Picks Up Object',
                  'Person Sets Down Object',
                  'Person Heavy Carry',
                  'Hand Interaction',
                  'Person-Person Embrace',
                  'Person Purchasing',
                  'Person-Laptop Interaction',
                  'Vehicle Stopping',
                  'Vehicle Starting',
                  'Vehicle Reversing',
                  'Vehicle Picks Up Person',
                  'Vehicle Drops Off Person',
                  'Abandon Package',
                  'Theft']


class ActivityType(Enum):
    """
    Activity Types for DIVA
    """
    NULL = 0
    PERSON_OPENS_FACILITY_DOOR = 1
    PERSON_CLOSES_FACILITY_DOOR = 2
    PERSON_ENTERS_THROUGH_STRUCTURE = 3
    PERSON_EXITS_THROUGH_STRUCTURE = 4
    PERSON_OPENS_VEHICLE_DOOR = 5
    PERSON_CLOSES_VEHICLE_DOOR = 6
    PERSON_ENTERS_VEHICLE = 7
    PERSON_EXITS_VEHICLE = 8
    PERSON_OPENS_TRUNK = 9
    PERSON_CLOSES_TRUNK = 10
    PERSON_LOADS_VEHICLE = 11
    PERSON_UNLOADS_VEHICLE = 12
    PEOPLE_TALKING = 13
    PERSON_TALKING_ON_PHONE = 14
    PERSON_TEXTING_ON_PHONE = 15
    RIDING = 16
    VEHICLE_TURNING_LEFT = 17
    VEHICLE_TURNING_RIGHT = 18
    VEHICLE_U_TURN = 19
    PERSON_SITTING_DOWN = 20
    PERSON_STANDING_UP = 21
    PERSON_READING_DOCUMENT = 22
    OBJECT_TRANSFER = 23
    PERSON_PICKS_UP_OBJECT = 24
    PERSON_SETS_DOWN_OBJECT = 25
    PERSON_HEAVY_CARRY = 26
    HAND_INTERACTION = 27
    PERSON_PERSON_EMBRACE = 28
    PERSON_PURCHASING = 29
    PERSON_LAPTOP_INTERACTION = 30
    VEHICLE_STOPPING = 31
    VEHICLE_STARTING = 32
    VEHICLE_REVERSING = 33
    VEHICLE_PICKS_UP_PERSON = 34
    VEHICLE_DROPS_OFF_PERSON = 35
    ABANDON_PACKAGE = 36
    THEFT = 37

    @property
    def long_name(self):
        return __long_names__[int(self.value)]

    @classmethod
    def from_long_name(cls, long_name: str) -> 'ActivityType':
        return ActivityType(__long_names__.index(long_name))
