import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from src import Logger

log = Logger()

log.info("测试信息日志")
log.debug("测试调试日志")