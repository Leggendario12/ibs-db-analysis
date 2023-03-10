"""Main Project Settings."""
from __future__ import annotations

import os
from pathlib import Path
from typing import Union, Any

##############################################################################
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)      #
# PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #
##############################################################################
BASE_DIR: Union[Union[str, bytes], Any] = os.path.dirname(
    os.path.dirname(
        os.path.abspath(
            __file__
        )
    )
)

PROJECT_DIR: Path = Path(
    __file__
).parent.parent
