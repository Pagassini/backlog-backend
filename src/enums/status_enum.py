from enum import Enum

class StatusEnum(str, Enum):
    FINISHED = "finished"
    PLAYING = "playing"
    DROPPED = "dropped"
    COMPLETED = "completed"