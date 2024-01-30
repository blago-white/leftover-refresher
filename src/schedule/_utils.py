import os
import pwd


def get_username() -> str:
    return pwd.getpwuid(os.getuid())[0]
