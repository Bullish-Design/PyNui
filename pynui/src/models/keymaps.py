# Imports ---------------------------------------------------------
import pynvim
from dataclasses import dataclass
from typing import Optional
# Functions -------------------------------------------------------


# Classes ---------------------------------------------------------
@dataclass
class Keymap:
    mode: str
    from_keys: str
    to_keys: str
    description: Optional[str]

    # Return the lua code for the keymap
    def set_keymap(self) -> Any:
        pass


# Misc ------------------------------------------------------------
