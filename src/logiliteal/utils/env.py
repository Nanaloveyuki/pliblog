"""
环境变量或常量与配置文件
"""

# 默认配置
DEFAULT_CONFIG = {
    "file_level": "DEBUG",
    "file_name": "latest.log",
    "file_path": "./logs",
    "file_format": "{asctime} {levelname} | {prefix}{message}{suffix}",
    "file_encoding": "utf-8",
    "enable_console": True,
    "enable_file": True,
    "console_color": True,
    "console_level": "DEBUG",
    "console_format": "{set_color(time, await get_config('time_color'))} {levelname} | {prefix}{message}{suffix}",
    "console_encoding": "utf-8",
    "asctime_format": "%Y-%m-%d %H:%M:%S",
    "time_format": "%H:%M:%S",
    "date_format": "%Y-%m-%d",
    "weekday_format": "%A",
    "level_nickname": {"DEBUG": "DEBUG", "INFO": "INFO", "WARN": "WARN", "ERRO": "ERRO", "CRIT": "CRIT"},
    "level_color": {"DEBUG": "#c1d5ff", "INFO": "#c1ffff", "WARN": "#fff600", "ERRO": "#ffa000", "CRIT": "#ff8181"},
    "time_color": "#28ffb6",
}

# 占位符
_placeholder: dict[str, str | bytes] = {
    "asctime": "{get_asctime()}",
    "time": "{get_time()}",
    "weekday": "{get_weekday()}",
    "date": "{get_date()}",
    "levelname": "{await fmt_level_number_to_name(level_number)}",
    "level_number": "{await fmt_level_name_to_number(levelname)}",
    "message": "{message}",
    "prefix": "{prefix}",
    "suffix": "{suffix}",
}

# 日志级别映射
_level_name_map: dict[str, int | float] = {
    "DEBUG": 0,
    "INFO": 10,
    "WARN": 20,
    "ERRO": 30,
    "CRIT": 40,
    "UNKN": -1,
}