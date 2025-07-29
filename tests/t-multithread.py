import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from src.logiliteal import Logger

log = Logger()

import threading
import time
import random

# 定义线程测试函数
def thread_logger(thread_id: int):
    """
    线程日志测试函数
    Thread logger test function
    Args:
        thread_id (int): 线程ID Thread ID
    """
    for i in range(10):
        log.info(f"线程{thread_id}的第{i+1}条日志消息", no_file=True)
        time.sleep(random.uniform(0.01, 0.05))

if __name__ == "__main__":
    threads = []
    for i in range(10):
        thread = threading.Thread(target=thread_logger, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    log.info("所有线程日志记录完成", no_file=True)