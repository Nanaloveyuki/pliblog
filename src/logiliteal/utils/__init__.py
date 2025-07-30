"""
工具函数
Utility functions
"""
# encoding = utf-8
# python 3.13.5

from .configs import get_config, set_config, reset_config, create_backup
from .time import get_asctime, get_date, get_time, get_weekday, _get_time
from .formats import fmt_console, fmt_content, fmt_file, fmt_level_list, fmt_level_name_to_number, fmt_level_number_to_name, fmt_placeholder, fmt_regex, add_placeholder, remove_placeholder, get_placeholder
from .styles import set_color, set_bg_color, set_style
from .env import _placeholder, _level_name_map, DEFAULT_CONFIG

__all__ = [
    "get_config",
    "set_config",
    "reset_config",
    "create_backup",
    "get_asctime",
    "get_date",
    "get_time",
    "get_weekday",
    "_get_time",
    "fmt_console",
    "fmt_content",
    "fmt_file",
    "fmt_level_list",
    "fmt_level_name_to_number",
    "fmt_level_number_to_name",
    "fmt_placeholder",
    "fmt_regex",
    "add_placeholder",
    "remove_placeholder",
    "get_placeholder",
    "set_color",
    "set_bg_color",
    "set_style",
    "_placeholder",
    "_level_name_map",
    "DEFAULT_CONFIG",
]
