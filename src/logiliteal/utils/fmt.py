"""
py-logiliteal的格式化工具,用于格式化日志输出
py-logiliteal's formatter, used to format log output

"""
# encoding = utf-8
# python 3.13.5

from .configs import get_config
from typing import Any, Optional
from .time import get_asctime, get_time, get_weekday, get_date
from .styles import set_color, set_bg_color
import re

if get_config("time_color") is None:
    time_color = "#28ffb6"
else:
    time_color = get_config("time_color")

def fmt_level(level: str) -> int:
    """
    格式化日志级别
    Format log level
    :param level: 日志级别 Log level
    :return: 格式化后的日志级别 Formatted log level
    """
    level_map = {
        "DEBUG": 0,
        "INFO": 10,
        "WARN": 20,
        "ERRO": 30,
        "CRIT": 40,
        "UNKN": 50
    }
    return level_map.get(level.upper(), 50)

def fmt_level_number(level: int) -> str:
    """
    格式化日志级别数字
    Format log level number
    :param level: 日志级别数字 Log level number
    :return: 格式化后的日志级别 Formatted log level
    """
    if level < 10:
        return "DEBUG"
    elif level < 20:
        return "INFO"
    elif level < 30:
        return "WARN"
    elif level < 40:
        return "ERRO"
    elif level < 50:
        return "CRIT"
    else:
        return "UNKN"

def fmt_placeholder(message: Any, use_date_color: bool = True) -> str:
    """
    格式化占位符
    Format placeholder
    :param message: 消息内容 Message content
    :return: 格式化后的消息 Formatted message
    """
    class SafeDict(dict):
        def __missing__(self, key):
            return f'{{{key}}}'

    if not isinstance(message, str):
        message = str(message)
    if use_date_color:
        message = message.format_map(SafeDict(
            asctime = set_color(get_asctime(),time_color),
            time = set_color(get_time(),time_color),
            weekday = set_color(get_weekday(),time_color),
            date = set_color(get_date(),time_color)
        ))
    else:
        message = message.format_map(SafeDict(
            asctime = get_asctime(),
            time = get_time(),
            weekday = get_weekday(),
            date = get_date(),
        ))
    return message

def fmt_message(message: Any, no_placeholder: bool = False, no_color: bool = False) -> str:
    """
    格式化消息内容
    Format message content
    :param message: 消息内容 Message content
    :return: 格式化后的消息 Formatted message
    """

    def process_color_tags(msg: str) -> str:
        # 优化处理顺序，确保链接和基础格式优先处理
        processed = _process_color_formatting(
            _process_special_tags(
                _process_html_styles(
                    _process_markdown_formats(
                        _process_links(msg)
                    )
                )
            )
        )
        return processed
    if no_color:
        processed_message = str(message)
    else:
        processed_message = process_color_tags(str(message))
    if no_placeholder:
        return processed_message
    else:
        return process_color_tags(fmt_placeholder(processed_message)) if not no_color else fmt_placeholder(processed_message)

def fmt_level_name(level_name: str) -> str:
    if get_config("console_color") != True:
        return level_name
    level_name_nick_map = get_config("level_name")

    if level_name in level_name_nick_map:
        _lnn = level_name_nick_map[level_name]
        level_color_map = get_config("level_color")

        if level_name in level_color_map:
            if level_name == "DEBUG":
                return set_bg_color(set_color(_lnn, level_color_map[level_name]), "#34495e")
            return set_color(_lnn, level_color_map[level_name])
        return set_color(_lnn)
    return "UNKN"

def fmt_console(level: int, message: Any, prefix: str | None = None) -> Optional[str]:
    """
    格式化控制台输出
    Format console output
    :param level: 日志级别 Log level
    :param message: 消息内容 Message content
    :return: 格式化后的消息 Formatted message
    """
    console_level = get_config("console_level")
    if level != -1 and fmt_level(console_level) > level:
        return None
    fmt = get_config("console_format")
    prefix = prefix or ""
    return fmt_placeholder(fmt).format(
        levelname = fmt_level_name(fmt_level_number(level)),
        prefix = fmt_message(prefix, no_placeholder=True),
        message = fmt_message(message, no_placeholder=True)
    )

def fmt_file(level: int, message: Any, prefix: str | None = None) -> Optional[str]:
    """
    格式化文件输出
    Format file output
    :param level: 日志级别 Log level
    :param message: 消息内容 Message content
    :return: 格式化后的消息 Formatted message
    """
    fl = get_config("file_level")
    fmt = get_config("file_format")
    if fmt_level(fl) > level:
        return None
    if prefix is None:
        prefix = ""
    fmt = fmt_placeholder(fmt, use_date_color=False)
    return f"{fmt.format(
        levelname = fmt_level_number(level),
        prefix = fmt_message(prefix, no_placeholder=True, no_color=True),
        message = fmt_message(message, no_placeholder=True, no_color=True)
    )}\n"

def _process_links(text: str) -> str:
    from collections import deque
    
    link_stack = deque()
    placeholder_count = 0
    placeholders = {}

    def replace_link(m):
        nonlocal placeholder_count
        placeholder_count += 1
        if len(m.groups()) == 2 and m.group(2) and not m.group(1).startswith('http'):
            # Markdown链接 [text](url)
            url = m.group(2).strip()
            text = m.group(1)
        else:
            url = m.group(1)
            text = m.group(2)
        placeholder = f"__LINK_PLACEHOLDER_{placeholder_count}__"
        placeholders[placeholder] = (url if url else "#", text)
        link_stack.append(placeholder)
        return placeholder

    text = re.sub(r'<a\s+href="([^"]+)">(.*?)</a>', replace_link, text, flags=re.DOTALL)
    text = re.sub(r'<link\s+href="([^"]+)">(.*?)</link>', replace_link, text, flags=re.DOTALL)
    text = re.sub(r'\[(.*?)\]\((.*?)\)', replace_link, text)

    for placeholder, (url, text_content) in placeholders.items():
        ansi_link = f'\033]8;;{url}\033\\{set_color("\033[4m" + text_content, "#5f93ff")}\033]8;;\033\\'
        text = text.replace(placeholder, ansi_link)
    
    return text

def _process_markdown_formats(text: str) -> str:
    # Markdown粗体 (**text**)
    text = re.sub(r'\*\*(.*?)\*\*', '\033[1m\\g<1>\033[22m', text)
    # Markdown斜体 (*text*)
    text = re.sub(r'\*(.*?)\*', '\033[3m\\g<1>\033[23m', text)
    # Markdown下划线 (__text__)
    text = re.sub(r'__(.*?)__', '\033[4m\\g<1>\033[24m', text)
    # Markdown删除线 (~~text~~)
    text = re.sub(r'~~(.*?)~~', '\033[9m\\g<1>\033[29m', text)
    return text

def _process_html_styles(text: str) -> str:
    text = re.sub(r'<i>([^<]*?)(</i>|$)',
                 lambda m: '\033[3m' + m.group(1) + '\033[23m', text, flags=re.DOTALL)
    text = re.sub(r'<b>([^<]*?)</b>',
                 lambda m: '\033[1m' + m.group(1) + '\033[22m', text)
    text = re.sub(r'<u>([^<]*?)</u>',
                 lambda m: '\033[4m' + m.group(1) + '\033[24m', text)
    text = re.sub(r'<s>([^<]*?)(</s>|$)',
                 lambda m: '\033[9m' + m.group(1) + '\033[29m', text, flags=re.DOTALL)
    return text

def _process_special_tags(text: str) -> str:
    text = re.sub(r'<br>', '\n', text)
    text = re.sub(r'<c>', '\033[0m', text)
    text = re.sub(r'<p>(.*?)</p>', r'\n\033[0m\g<1>\033[0m\n', text, flags=re.DOTALL)
    text = re.sub(r'<p>(.*?)(</p>|$)', r'\n\033[0m\g<1>\033[0m\n', text, flags=re.DOTALL)
    text = re.sub(r'</p>', '\033[0m\n', text)
    return text

def _process_color_formatting(text: str) -> str:
    import re
    
    color_pattern = r'<#([0-9a-fA-F]{6})>'
    close_pattern = r'</>'

    parts = re.split(f'({color_pattern}|{close_pattern})', text)
    result = []
    color_stack = []
    
    for part in parts:
        if part and re.fullmatch(color_pattern, part):
            color = re.match(color_pattern, part).group(1)
            color_stack.append(color)
            continue
        elif part == '</>':
            if color_stack:
                color_stack.pop()
            continue
        elif part:
            if color_stack:
                current_color = color_stack[-1]
                r = int(current_color[0:2], 16)
                g = int(current_color[2:4], 16)
                b = int(current_color[4:6], 16)
                ansi_code = f'\033[38;2;{r};{g};{b}m'
                reset_code = '\033[0m'
                result.append(f'{ansi_code}{part}{reset_code}')
            else:
                result.append(part)

    processed_text = ''.join(result)
    processed_text = re.sub(f'{color_pattern}|{close_pattern}|[0-9a-fA-F]{{6}}', '', processed_text)
    
    return processed_text
