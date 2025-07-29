import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from src.logiliteal import Logger

log = Logger()

i = 0

while i < 20000:
    log.info(f"**md** | <#ff0000>测试--重--复~~日志~~: {i}")
    i += 1