from enum import Enum

VERSION = 1.0
RESIZABLE_THE_WINDOW = False

class WINDOW_SIZES:
    class MAIN_WINDOW:
        WIDTH = 1080
        HEIGHT = 700

class BUILD_TYPE(Enum):
    MAIN = 1
    DEBUG_BUG_TRACK = 2

class FONTS_WEIGHT:
    HEADING = ("Arial", 26, "bold")

class NAME_WINDOWS():
    MAIN = f"FLASH-OOU (Only once use) v{VERSION}"