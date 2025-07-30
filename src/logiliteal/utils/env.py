"""
环境变量或常量与配置文件
Environment variables, constants and configuration files

"""
# encoding = utf-8
# python 3.13.5

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
    "console_format": "{time} {levelname} | {prefix}{message}{suffix}",
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
    "asctime": "{set_color(get_asctime(), get_config('asctime_color') or '#c1ffff')}",
    "time": "{set_color(get_time(), get_config('time_color') or '#28ffb6')}",
    "weekday": "{get_weekday()}",
    "date": "{get_date()}",
    "levelname": "{fmt_level_number_to_name(level_number)}",
    "level_number": "{level_number}",
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

def get_venv_path() -> str:
    """
    获取虚拟环境路径
    Get virtual environment path
    """
    from os import path
    from sys import prefix
    return str(path.dirname(prefix))

def get_project_path() -> str:
    """
    获取项目路径
    Get project path
    """
    from os import path
    from sys import prefix
    return str(path.dirname(path.dirname(prefix)))

def get_config_path() -> str:
    """
    获取配置文件路径
    Get config file path
    """
    from os import path
    from sys import prefix
    return str(path.join(path.dirname(path.dirname(prefix)), "config.json"))

def get_log_path() -> str:
    """
    获取日志文件路径
    Get log file path
    """
    from os import path
    from sys import prefix
    return str(path.join(path.dirname(path.dirname(prefix)), "logs"))
    