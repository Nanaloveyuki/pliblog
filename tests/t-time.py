import sys
from pathlib import Path
import time

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from src.logiliteal.utils.time import get_asctime, get_time, get_date, get_weekday
from src.logiliteal.levels import Logger

log = Logger()

log.info(get_asctime())
log.info(get_time())
log.info(get_date())
log.info(get_weekday())

while True:
    try:
        log.info(get_asctime())
        time.sleep(1)
        log.info("时间分割线")
    except KeyboardInterrupt:
        log.info("测试结束")
        break
