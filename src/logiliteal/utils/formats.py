"""
格式化工具
Formatting tools
"""

from .time import get_asctime, get_time, get_weekday, get_date
from .styles import set_color
from .configs import get_config
from .regex import process_color_formatting, process_html_styles, process_links, process_markdown_formats, process_special_tags

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

async def fmt_level_number_to_name(level_number: int | float) -> str:
    """
    格式化日志级别数字为名称
    Format log level number to name\n
    Args:
        level_number (int | float): 日志级别数字
    Returns:
        str: 日志级别名称
    """
    if not level_number in range(0, 50):
        return _level_name_map.get(-1)
    if 0 <= level_number <= 9:
        return _level_name_map.get(0)
    elif 10 <= level_number <= 19:
        return _level_name_map.get(10)
    elif 20 <= level_number <= 29:
        return _level_name_map.get(20)
    elif 30 <= level_number <= 39:
        return _level_name_map.get(30)
    elif 40 <= level_number <= 49:
        return _level_name_map.get(40)
    return _level_name_map.get(-1)

async def fmt_level_name_to_number(level_name: str) -> int:
    """
    格式化日志级别名称为数字
    Format log level name to number\n
    Args:
        level_name (str): 日志级别名称
    Returns:
        int: 日志级别数字
    """
    return _level_name_map.get(level_name.upper(), -1)

async def fmt_level_list(level_number: int | float,
    level_name: str in _level_name_map.keys(),
    ) -> dict:
    """
    格式化日志级别数据字典
    Format log level data dict\n
    Args:
        level_number (int | float): 日志级别数字
        level_name (str): 日志级别名称
    Returns:
        dict: 日志级别数据字典
    """
    return {
            "level_number": level_number,
            "level_nickname": get_config("level_nickname").get(level_name.upper(), level_name),
            "level_name": level_name.upper(),
    }

async def get_level_number(level_list: dict) -> int | float:
    """
    获取日志级别数字
    Get log level number
    Args:
        level_list (dict[str, int | float]): 日志级别数据字典
    Returns:
        int | float: 日志级别数字
    """
    return level_list.get("level_number")

async def get_level_name(level_list: dict) -> str:
    """
    获取日志级别名称
    Get log level name
    Args:
        level_list (dict[str, int | float]): 日志级别数据字典
    Returns:
        str: 日志级别名称
    """
    return level_list.get("level_name", "UNKN")

async def get_level_nickname(level_list: dict) -> str:
    """
    获取日志级别昵称
    Get log level nickname
    Args:
        level_list (dict[str, int | float]): 日志级别数据字典
    Returns:
        str: 日志级别昵称
    """
    return level_list.get("level_nickname", "UNKN")

async def fmt_placeholder(
    message: str = "",
    no_placeholder: bool = False,
    **kwargs
) -> str:
    """
    格式化占位符
    Format placeholder\n
    Args:
        message (str, optional): 日志消息. Defaults to "".
        no_placeholder (bool, optional): 不使用占位符. Defaults to False.
    Returns:
        str: 格式化后的日志消息或原始消息

    """
    if no_placeholder:
        return message
    for key, value in kwargs.items():
        if key in _placeholder:
            message = message.replace(_placeholder[key], str(value))
        else:
            message = message.replace(f"{{{key}}}", str(value))
    return message

async def add_placeholder(key: str, value: str | bytes) -> None:
    """
    添加新的占位符
    Add new placeholder\n
    Args:
        key (str): 占位符键
        value (str | bytes): 占位符值
    """
    global _placeholder
    _placeholder[key] = value

async def get_placeholder(key: str | None = None) -> str | dict[str, str | bytes]:
    """
    获取占位符
    Get placeholder\n
    Args:
        key (str | None, optional): 占位符键. Defaults to None.
    Returns:
        str | dict[str, str | bytes]: 占位符值或占位符字典
    """
    if key is None:
        return _placeholder
    return _placeholder.get(key, "None") if key in _placeholder else "None"

async def remove_placeholder(key: str) -> bool:
    """
    删除占位符
    Remove placeholder\n
    Args:
        key (str): 占位符键
    Returns:
        bool: 删除成功返回True, 删除失败返回False
    """
    try:
        if key in _placeholder:
            del _placeholder[key]
            return True
        else:
            return False
    except Exception:
        return False


async def fmt_regex(message: str,
    no_regex: bool = False,
    no_color: bool = False,
    no_html: bool = False,
    no_link: bool = False,
    no_markdown: bool = False,
    no_special_tags: bool = False,
) -> str:
    """
    格式化正则表达式
    Format regex\n
    Args:
        message (str): 日志消息
    Returns:
        str: 格式化后的日志消息
    """
    if no_regex | (no_color and no_html and no_link and no_markdown and no_special_tags):
        return message

    return await process_color_formatting(
        await process_html_styles(
            await process_links(
                await process_markdown_formats(
                    await process_special_tags(message, no_process=no_special_tags),
                    no_process=no_markdown,
                ),
                no_process=no_link
            ),
            no_process=no_html
        ),
        no_process=no_color
    )

async def fmt_content(
    message: str = "",
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
    Format content\n
    Args:
        message (str): 日志消息
    Returns:
        str: 格式化后的日志消息
    """
    message = await fmt_placeholder(message, no_placeholder=no_placeholder)
    message = await fmt_regex(message, no_regex=no_regex, no_color=no_color, no_html=no_html, no_link=no_link, no_markdown=no_markdown, no_special_tags=no_special_tags)
    return message

async def fmt_console(
    message: str = "",
    no_placeholder: bool = False,
    no_regex: bool = False,
    no_color: bool = False,
    no_html: bool = False,
    no_link: bool = False,
    no_markdown: bool = False,
    no_special_tags: bool = False,
) -> str:
    """
    格式化控制台内容
    Format console content\n
    Args:
        message (str): 日志消息
    Returns:
        str: 格式化后的日志消息
    """
    message = await fmt_placeholder(message, no_placeholder=no_placeholder)
    message = await fmt_regex(message, no_regex=no_regex, no_color=no_color, no_html=no_html, no_link=no_link, no_markdown=no_markdown, no_special_tags=no_special_tags)
    return message

async def fmt_file(
    message: str = "",
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
    Format file content\n
    Args:
        message (str): 日志消息
    Returns:
        str: 格式化后的日志消息
    """
    message = await fmt_placeholder(message, no_placeholder=no_placeholder)
    message = await fmt_regex(message, no_regex=no_regex, no_color=no_color, no_html=no_html, no_link=no_link, no_markdown=no_markdown, no_special_tags=no_special_tags)
    return message