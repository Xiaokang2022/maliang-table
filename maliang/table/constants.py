"""All constants for main"""

from __future__ import annotations as _

__all__ = (
    "THEME_LIGHT",
    "THEME_DARK",
)

import tksheet

THEME_LIGHT = tksheet.theme_light_blue
THEME_DARK = tksheet.theme_dark

for key, value in THEME_DARK.items():
    if value in ("#000000", "#000", "black"):
        THEME_DARK[key] = "#2B2B2B"
    if value in ("#FFFFFF", "#FFF", "white"):
        THEME_DARK[key] = "#F1F1F1"
