import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from src.logiliteal.utils.configs import get_config, set_config, reset_config

print(f"\n配置更换测试")
set_config("file_level", "DEBUG")
fl = get_config("file_level")
print(fl)

set_config("file_level", "INFO")
fl = get_config("file_level")
print(fl)

print(f"\n配置重置测试")
print(reset_config())

print(f"\n配置重置后测试")
fl = get_config("file_level")
print(fl)

print(f"\n未指定配置读取测试")
print(get_config())