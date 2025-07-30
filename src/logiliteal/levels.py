"""
日志级别模块
Log level module

"""
# encoding: utf-8
# python 3.13.5

from .utils import fmt_console, fmt_file, fmt_content
from typing import Any, Optional

class Logger:
    def __init__(self):
       pass

    def _log(
            self,
            message: Any,
            prefix: str = "",
            suffix: str = "",
            level_number: int = 0,
            no_console: bool = False,
            no_file: bool = False,
            no_placeholder: bool = False,
            no_regex: bool = False,
            no_color: bool = False,
            no_html: bool = False,
            no_link: bool = False,
            no_markdown: bool = False,
            no_special_tags: bool = False,
        ) -> Optional[str]:
        """
        同步日志方法
        Synchronous logging method
        Args:
            message (Any): 日志消息 Log message
            level_number (int, optional): 日志级别编号. Defaults to 0.
            no_console (bool, optional): 是否禁用控制台输出. Defaults to False.
            no_file (bool, optional): 是否禁用文件输出. Defaults to False.
            no_placeholder (bool, optional): 是否禁用占位符替换. Defaults to False.
            no_regex (bool, optional): 是否禁用正则表达式替换. Defaults to False.
            no_color (bool, optional): 是否禁用颜色输出. Defaults to False.
            no_html (bool, optional): 是否禁用HTML标签输出. Defaults to False.
            no_link (bool, optional): 是否禁用链接输出. Defaults to False.
            no_markdown (bool, optional): 是否禁用Markdown格式输出. Defaults to False.
            no_special_tags (bool, optional): 是否禁用特殊标签输出. Defaults to False.
            **kwargs: 其他参数同fmt_console和fmt_file
        Returns:
            Optional[Union[str, bool]]: 格式化后的日志消息或False
        """
        if not no_console:
            print(fmt_console(
                message=message,
                level_number=level_number,
                prefix=prefix,
                suffix=suffix,
                no_placeholder=no_placeholder,
                no_regex=no_regex,
                no_color=no_color,
                no_special_tags=no_special_tags,
            ))
        if not no_file:
            with open("log.txt", "a", encoding="utf-8") as f:
                f.write(fmt_file(
                    message=message,
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
                ))
        return fmt_content(
            message=message,
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


    def debug(
            self,
            message: Any,
            prefix: str = "",
            suffix: str = "",
            level_number: int = 0,
            no_console: bool = False,
            no_file: bool = False,
            no_placeholder: bool = False,
            no_regex: bool = False,
            no_color: bool = False,
            no_html: bool = False,
            no_link: bool = False,
            no_markdown: bool = False,
            no_special_tags: bool = False,
        ):
        """
        同步debug日志方法
        Synchronous debug logging method
        Args:
            message (Any): 日志消息 Log message
            level_number (int, optional): 日志级别编号. Defaults to 0.
            no_console (bool, optional): 是否禁用控制台输出. Defaults to False.
            no_file (bool, optional): 是否禁用文件输出. Defaults to False.
            no_placeholder (bool, optional): 是否禁用占位符替换. Defaults to False.
            no_regex (bool, optional): 是否禁用正则表达式替换. Defaults to False.
            no_color (bool, optional): 是否禁用颜色输出. Defaults to False.
            no_html (bool, optional): 是否禁用HTML标签输出. Defaults to False.
            no_link (bool, optional): 是否禁用链接输出. Defaults to False.
            no_markdown (bool, optional): 是否禁用Markdown格式输出. Defaults to False.
            no_special_tags (bool, optional): 是否禁用特殊标签输出. Defaults to False.
            其他参数同fmt_console和fmt_file
        """
        self._log(
            message=message,
            prefix=prefix,
            suffix=suffix,
            level_number=level_number,
            no_console=no_console,
            no_file=no_file,
            no_placeholder=no_placeholder,
            no_regex=no_regex,
            no_color=no_color,
            no_html=no_html,
            no_link=no_link,
            no_markdown=no_markdown,
            no_special_tags=no_special_tags,
        )
