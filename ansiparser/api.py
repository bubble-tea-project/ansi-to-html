"""
ansiparser.api
~~~~~~~~~~~~~~

This module implements the ansiparser API.
"""

from collections import deque

from . import screen_parser


def new_screen(height=24,width=80) -> screen_parser.ScreenParser:
    """Initialize the ScreenParser for a new screen."""
    
    return screen_parser.ScreenParser(screen_height=height,screen_width=width)


def from_screen(parsed_screen: deque) -> screen_parser.ScreenParser:
    """Initialize the ScreenParser from an existing parsed screen."""

    screen_parser_class = screen_parser.ScreenParser()
    screen_parser_class.from_parsed_screen(parsed_screen)

    return screen_parser_class
