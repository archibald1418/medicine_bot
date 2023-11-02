from enum import auto, IntEnum

class TimeOfMedicine(IntEnum):
    NOTSTATED = 0
    
    # Food-based
    AFTERMEAL = auto()
    BEFOREMEAL = auto()
    BETWEENMEALS = auto()
    DURINGMEAL = auto()

    # Sleep-based
    BEFOREBED = auto()
    EMPTYSTOMACH = auto()

    # Every n hours
    EVERY = auto()
