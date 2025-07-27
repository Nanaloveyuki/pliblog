"""
pliblog - 简易,现代化具有色彩的日志记录器 / Easy, Modern and colorful Logger
"""
# encoding = utf-8
# python 3.13.5

from .utils import get_config, set_config, reset_config

__all__ = [
    "get_config",
    "set_config",
    "reset_config"
]