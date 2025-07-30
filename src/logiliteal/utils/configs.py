"""
py-logiliteal的配置设置,用于设置py-logiliteal的全局配置
py-logiliteal's config settings, used to set py-logiliteal's global config

"""
# encoding = utf-8
# python 3.13.5

import json
from .env import DEFAULT_CONFIG, get_config_path
import pathlib
from typing import Any
def init_config(config: dict = DEFAULT_CONFIG, config_path: str = None) -> bool:
    """
    初始化配置
    Init config
    Args:
        config (dict, optional): 配置字典. Defaults to DEFAULT_CONFIG.
        config_path (str, optional): 配置文件路径. Defaults to None.
    Returns:
        bool: 是否成功初始化配置
    """
    if config_path is None:
        config_path = str(get_config_path())
    dump_config = json.dumps(config, indent=4)
    with open(config_path, "w") as f:
        f.write(dump_config)
    return True

def get_config(key: str | None = None) -> Any:
    """
    获取配置
    Get config
    Args:
        key (str | None, optional): 配置键. Defaults to None.
    Returns:
        Any: 配置值
    """
    if not pathlib.Path(str(get_config_path())).exists():
        init_config()
    with open(str(get_config_path()), "r") as f:
        config = json.load(f)
    if key is None:
        return config
    return config.get(key, None)

def set_config(key: str, value: Any) -> bool:
    """
    设置配置
    Set config
    Args:
        key (str): 配置键
        value (Any): 配置值
    Returns:
        bool: 是否成功设置配置
    """
    if not pathlib.Path(str(get_config_path())).exists():
        init_config()
    with open(str(get_config_path()), "r") as f:
        config = json.load(f)
    config[key] = value
    with open(str(get_config_path()), "w") as f:
        json.dump(config, f, indent=4)
    return config.get(key, None) == value

def backup_config(backup_path: str = None) -> bool:
    """
    备份配置
    Backup config
    Args:
        backup_path (str, optional): 备份文件路径. Defaults to None.
    Returns:
        bool: 是否成功备份配置
    """
    if not pathlib.Path(str(get_config_path())).exists():
        init_config()
    if backup_path is None:
        backup_path = str(get_config_path()) + ".backup"
    with open(str(get_config_path()), "r") as f:
        config = json.load(f)
    backup_path = backup_path or str(get_config_path()) + ".backup"
    with open(str(backup_path), "w") as f:
        json.dump(config, f, indent=4)
    return True

def restore_config(backup_path: str = None) -> bool:
    """
    恢复配置
    Restore config
    Args:
        backup_path (str, optional): 备份文件路径. Defaults to None.
    Returns:
        bool: 是否成功恢复配置
    """
    if not pathlib.Path(str(get_config_path())).exists():
        init_config()
    if backup_path is None:
        backup_path = str(get_config_path()) + ".backup"
    with open(str(backup_path), "r") as f:
        config = json.load(f)
    with open(str(get_config_path()), "w") as f:
        json.dump(config, f, indent=4)
    return True

def reset_config() -> bool:
    """
    重置配置
    Reset config
    Returns:
        bool: 是否成功重置配置
    """
    init_config(config=DEFAULT_CONFIG)
    return True
