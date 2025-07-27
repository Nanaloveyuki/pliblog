"""
工具函数 / Utility functions
"""
# encoding = utf-8
# python 3.13.5

from .configs import get_config, set_config, reset_config
from .time import get_asctime, get_date, get_time, get_weekday
from .fmt import fmt_console, fmt_placeholder, fmt_message, fmt_level_name

__all__ = [
    "get_config",
    "set_config",
    "reset_config",
    "get_asctime",
    "get_date",
    "get_time",
    "get_weekday",
    "fmt_console",
    "fmt_placeholder",
    "fmt_message",
    "fmt_level_name",
]