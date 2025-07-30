"""
格式化工具
Formatting tools

"""
# encoding = utf-8
# python 3.13.5

from .time import get_asctime, get_time, get_weekday, get_date
from .styles import set_color
from .configs import get_config
from .regex import process_color_formatting, process_html_styles, process_links, process_markdown_formats, process_special_tags
from .env import _placeholder, _level_name_map, DEFAULT_CONFIG
from typing import Any
import re

class SafeDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._placeholder = _placeholder

    def __getitem__(self, key):
        return super().__getitem__(key).format(**self)

def fmt_level_number_to_name(level_number: int | float) -> str:
    """
    格式化日志级别数字为名称
    Format log level number to name
    Args:
        level_number (int | float): 日志级别数字
    Returns:
        str: 日志级别名称
    """
    if not level_number in range(0, 50):
        return _level_name_map.get(-1, "UNKNOWN")
    if 0 <= level_number <= 9:
        return _level_name_map.get(0, "DEBUG")
    elif 10 <= level_number <= 19:
        return _level_name_map.get(10, "INFO")
    elif 20 <= level_number <= 29:
        return _level_name_map.get(20, "WARNING")
    elif 30 <= level_number <= 39:
        return _level_name_map.get(30, "ERROR")
    elif 40 <= level_number <= 49:
        return _level_name_map.get(40, "CRITICAL")
    return _level_name_map.get(-1, "UNKNOWN")

def fmt_level_name_to_number(level_name: str) -> int:
    """
    格式化日志级别名称为数字
    Format log level name to number
    Args:
        level_name (str): 日志级别名称
    Returns:
        int: 日志级别数字
    """
    return _level_name_map.get(level_name.upper(), -1)

def fmt_level_list(level_number: int | float) -> dict:
    """
    格式化日志级别数据字典
    Format log level data dict
    Args:
        level_number (int | float): 日志级别数字
    Returns:
        dict: 日志级别数据字典
    """
    level_name = fmt_level_number_to_name(level_number) or "UNKNOWN"
    level_nickname_config = get_config("level_nickname") or {}
    return {
            "level_number": level_number,
            "level_nickname": level_nickname_config.get(level_name.upper(), level_name),
            "level_name": level_name.upper(),
    }

def get_level_number(level_list: dict) -> int | float:
    """
    获取日志级别数字
    Get log level number
    Args:
        level_list (dict[str, int | float]): 日志级别数据字典
    Returns:
        int | float: 日志级别数字
    """
    return level_list.get("level_number")

def get_level_name(level_list: dict) -> str:
    """
    获取日志级别名称
    Get log level name
    Args:
        level_list (dict[str, int | float]): 日志级别数据字典
    Returns:
        str: 日志级别名称
    """
    return level_list.get("level_name", "UNKN")

def get_level_nickname(level_list: dict) -> str:
    """
    获取日志级别昵称
    Get log level nickname
    Args:
        level_list (dict[str, int | float]): 日志级别数据字典
    Returns:
        str: 日志级别昵称
    """
    return level_list.get("level_nickname", "UNKN")

def fmt_placeholder(
    message: str = "",
    level_number: int = 0,
) -> str:
    """
    格式化占位符
    Format placeholder
    Args:
        message (str, optional): 日志消息. Defaults to "".
    Returns:
        str: 格式化后的日志消息或原始消息
    """
    # 创建上下文字典，包含所有可能用到的函数和变量
    context = {
        'level_number': level_number,
        'fmt_level_list': fmt_level_list,
        'fmt_level_number_to_name': fmt_level_number_to_name,
        'get_config': get_config,
        'set_color': set_color,
        'get_asctime': get_asctime,
        'get_time': get_time,
        'get_date': get_date,
        'get_weekday': get_weekday,
    }
    
    # 替换所有占位符
    for key, value in _placeholder.items():
        placeholder = f"{{{key}}}"
        if placeholder in message:
            if isinstance(value, str) and '{' in value and '}' in value:
                try:
                    # 解析并执行占位符中的表达式
                    expr = value.strip('{}')
                    evaluated_value = eval(expr, {}, context)
                    message = message.replace(placeholder, str(evaluated_value))
                except Exception as e:
                    # 添加详细的错误信息以帮助调试
                    error_msg = f"{{ERROR: {type(e).__name__} - {str(e)} - Expr: {expr}}}"
                    message = message.replace(placeholder, error_msg)
            else:
                message = message.replace(placeholder, str(value))
    
    return message.format(**SafeDict(level_list=fmt_level_list(level_number)))

def add_placeholder(key: str, value: str | bytes) -> None:
    """
    添加新的占位符
    Add new placeholder
    Args:
        key (str): 占位符键
        value (str | bytes): 占位符值
    """
    global _placeholder
    _placeholder[key] = value

def get_placeholder(key: str | None = None) -> str | dict[str, str | bytes]:
    """
    获取占位符
    Get placeholder
    Args:
        key (str | None, optional): 占位符键. Defaults to None.
    Returns:
        str | dict[str, str | bytes]: 占位符值或占位符字典
    """
    if key is None:
        return _placeholder
    return _placeholder.get(key, "None") if key in _placeholder else "None"

def remove_placeholder(key: str) -> bool:
    """
    删除占位符
    Remove placeholder
    Args:
        key (str): 占位符键
    Returns:
        bool: 删除成功返回True, 删除失败返回False
    """
    global _placeholder
    try:
        if key in _placeholder:
            del _placeholder[key]
            return True
        else:
            return False
    except Exception:
        return False

def fmt_regex(
        message: str,
        no_regex: bool = False,
        no_color: bool = False,
        no_html: bool = False,
        no_link: bool = False,
        no_markdown: bool = False,
        no_special_tags: bool = False,
    ) -> str:
    """
    格式化正则表达式
    Format regex
    Args:
        message (str): 日志消息
    Returns:
        str: 格式化后的日志消息
    """
    if no_regex | (no_color and no_html and no_link and no_markdown and no_special_tags):
        return message

    return process_color_formatting(
        process_html_styles(
            process_links(
                process_markdown_formats(
                    process_special_tags(message, no_process=no_special_tags),
                    no_process=no_markdown,
                ),
                no_process=no_link
            ),
            no_process=no_html
        ),
        no_process=no_color
    )

def fmt_content(
        message: str = "",
        prefix: str = "",
        suffix: str = "",
        level_number: int = 0,
        no_placeholder: bool = False,
        no_regex: bool = False,
        no_color: bool = False,
        no_html: bool = False,
        no_link: bool = False,
        no_markdown: bool = False,
        no_special_tags: bool = False,
    ) -> str:
    """
    格式化内容
    Format content
    Args:
        message (str): 日志消息
    Returns:
        str: 格式化后的日志消息
    """
    if not no_placeholder:
        message = fmt_placeholder(message, level_number=level_number)
    if not no_regex | no_html and not no_link and not no_markdown and not no_special_tags and no_color:
        message = fmt_regex(message, no_regex=no_regex, no_color=no_color, no_html=no_html, no_link=no_link, no_markdown=no_markdown, no_special_tags=no_special_tags)
    return f"{prefix}{message}{suffix}\n"


def fmt_console(
    message: Any,
    level_number: int | float,
    prefix: str = "",
    suffix: str = "",
    no_placeholder: bool = False,
    no_regex: bool = False,
    no_color: bool = False,
    no_html: bool = False,
    no_markdown: bool = False,
    no_link: bool = False,
    no_special_tags: bool = False
) -> str:
    """
    格式化控制台日志
    Format console log
    Args:
        message (Any): 日志消息
        prefix (str, optional): 前缀
        suffix (str, optional): 后缀
        level_number (int, optional): 日志级别数字
        no_placeholder (bool, optional): 是否不处理占位符
        no_regex (bool, optional): 是否不处理正则
        no_color (bool, optional): 是否不处理颜色
        no_html (bool, optional): 是否不处理HTML
        no_link (bool, optional): 是否不处理链接
        no_markdown (bool, optional): 是否不处理Markdown
        no_special_tags (bool, optional): 是否不处理特殊标签
    Returns:
        str: 格式化后的控制台日志
    """
    # 获取基础配置
    fmt_cfg = get_config("console_format") or DEFAULT_CONFIG["console_format"]
    level_name = fmt_level_number_to_name(level_number).upper()
    
    # 处理所有占位符和格式化
    placeholders = {
        'asctime': get_asctime(),
        'time': get_time(),
        'date': get_date(),
        'weekday': get_weekday(),
        'levelname': level_name,
        'level_number': str(level_number),
        'prefix': prefix,
        'suffix': suffix,
        'message': str(message)
    }
    
    # 替换格式字符串中的占位符
    # 初始化颜色配置
    color_config = {
        'time_color': get_config('time_color') or DEFAULT_CONFIG['time_color'],
        'level_colors': get_config('level_color') or DEFAULT_CONFIG['level_color']
    }

    # 处理时间相关占位符的颜色
    time_placeholders = ['asctime', 'time', 'date', 'weekday']
    for placeholder in time_placeholders:
        if placeholder in placeholders:
            placeholders[placeholder] = set_color(placeholders[placeholder], color_config['time_color'])

    # 处理日志级别颜色
    if 'levelname' in placeholders:
        level_name = placeholders['levelname']
        level_color = color_config['level_colors'].get(level_name, DEFAULT_CONFIG['level_color']['DEBUG'])
        placeholders['levelname'] = set_color(level_name, level_color)

    # 替换占位符
    for key, value in placeholders.items():
        fmt_cfg = fmt_cfg.replace(f'{{{key}}}', str(value))
    
    # 应用内容格式化
    formatted_content = fmt_content(
        fmt_cfg,
        no_placeholder=no_placeholder,
        no_regex=no_regex,
        no_color=no_color,
        no_html=no_html,
        no_markdown=no_markdown,
        no_link=no_link,
        no_special_tags=no_special_tags,
    )
    # 处理前缀和后缀
    if prefix:
        # 清理前缀中的颜色标签
        clean_prefix = re.sub(r'<#([0-9a-fA-F]{6})>|</>', '', prefix)
        formatted_content = f"{set_color(clean_prefix, color_config['time_color'])}{formatted_content}"
    if suffix:
        # 清理后缀中的颜色标签
        clean_suffix = re.sub(r'<#([0-9a-fA-F]{6})>|</>', '', suffix)
        formatted_content = f"{formatted_content}{set_color(clean_suffix, color_config['time_color'])}"
    return formatted_content

def fmt_file(
        message: str = "",
        prefix: str = "",
        suffix: str = "",
        level_number: int = 0,
        no_placeholder: bool = False,
        no_regex: bool = True,
        no_color: bool = False,
        no_html: bool = False,
        no_link: bool = False,
        no_markdown: bool = False,
        no_special_tags: bool = False,
    ) -> str:
    """
    格式化文件内容
    Format file content
    Args:
        message (str): 日志消息
    Returns:
        str: 格式化后的日志消息
    """
    fmt_cfg = get_config("file_format") if get_config("file_format") else "{asctime} {levelname} | {prefix}{message}{suffix}"
    fmt_cfg = fmt_content(
        message=message,
        prefix=prefix,
        suffix=suffix,
        level_number=level_number,
        no_placeholder=no_placeholder,
        no_regex=no_regex,
        no_color=no_color,
        no_html=no_html,
    )
    return fmt_content(
        message=fmt_cfg,
        prefix=prefix,
        suffix=suffix,
        level_number=level_number,
        no_placeholder=no_placeholder,
        no_regex=no_regex,
        no_color=no_color,
        no_html=no_html,
        no_link=no_link,
        no_markdown=no_markdown,
        no_special_tags=no_special_tags,
    )
