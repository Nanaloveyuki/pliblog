"""
py-logiliteal - 简易,现代化具有色彩的日志记录器
py-logiliteal's config settings, used to set py-logiliteal's global config
"""
# encoding = utf-8
# python 3.13.5

from .utils import get_config, set_config, reset_config, backup_config, restore_config, init_config
from .utils import get_asctime, get_date, get_time, get_weekday, _get_time
from .utils import fmt_console, fmt_content, fmt_file, fmt_level_list, fmt_level_name_to_number, fmt_level_number_to_name, fmt_placeholder, fmt_regex, add_placeholder, remove_placeholder, get_placeholder
from .utils import set_style, set_color, set_bg_color
from .levels import Logger

logger = Logger()

__all__ = [
    "get_config",
    "set_config",
    "reset_config",
    "backup_config",
    "restore_config",
    "init_config",
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
    "logger",
    "Logger",
]