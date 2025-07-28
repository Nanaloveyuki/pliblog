import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from src.logiliteal import Logger

log = Logger()

log.info("测试信息日志")
log.debug("测试调试日志")
log.warn("测试警告日志")
log.error("测试错误日志")
log.critical("测试严重错误日志")