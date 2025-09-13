"""APIs for tksheet"""

from __future__ import annotations as _

__all__ = (
    "TkTable",
)

import typing

import tksheet
from maliang.theme import manager

from . import constants


class TkTable(tksheet.Sheet):
    """A tkinter widget for displaying a table."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.theme(manager.get_color_mode())
        manager.register_event(self.theme)

    def theme(self, value: typing.Literal["light", "dark"]) -> None:
        """Change the color theme of the table.

        * `value`: theme name
        """
        if value == "light":
            self.set_options(**constants.THEME_LIGHT, redraw=False)
        else:
            self.set_options(**constants.THEME_DARK, redraw=False)
        self.MT.recreate_all_selection_boxes()
        self.set_refresh_timer(True)
        self.TL.redraw()
