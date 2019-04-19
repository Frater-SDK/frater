from enum import Enum

__long_names__ = ['Null', 'Open_Trunk', 'Closing_Trunk', 'Opening', 'Closing',
                  'Loading', 'Unloading', 'Entering', 'Exiting', 'Transport_HeavyCarry',
                  'Pull', 'Talking', 'specialized_talking_phone', 'specialized_texting_phone',
                  'Riding', 'activity_carrying']


class ActivityType(Enum):
    """
    Activity Types for DIVA
    """
    NULL = 0
    OPEN_TRUNK = 1
    CLOSE_TRUNK = 2
    OPEN = 3
    CLOSE = 4
    LOAD = 5
    UNLOAD = 6
    ENTER = 7
    EXIT = 8
    TRANSPORT = 9
    PULL = 10
    TALK = 11
    TALK_PHONE = 12
    TEXT_PHONE = 13
    RIDE = 14
    CARRY = 15
    TURN_LEFT = 16
    TURN_RIGHT = 17
    U_TURN = 18

    # subgroups
    PVI = {ENTER, EXIT, OPEN, CLOSE, OPEN_TRUNK, CLOSE_TRUNK, LOAD, UNLOAD}

    @property
    def long_name(self):
        return __long_names__[int(self.value)]

    @classmethod
    def from_long_name(cls, long_name: str) -> 'ActivityType':
        return ActivityType(__long_names__.index(long_name))
