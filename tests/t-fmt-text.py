import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from src.logiliteal.levels import Logger

log = Logger()

log.info("<i>html斜体</i>")
log.info("<b>html加粗</b>")
log.info("<u>html下划线</u>")
log.info("<s>html删除线</s>")
log.info("<p>html段落</p>")
log.info("<a href=\"https://www.baidu.com\">html超链接</a>")
log.info("**Markdown加粗**")
log.info("*Markdown斜体*")
log.info("`Markdown代码块`")
log.info("~~Markdown删除线~~\n")
log.info("[md超链接](https://www.baidu.com)")
log.info("--测试<i>重复--")
log.info("<#ff0000>颜色重叠<#0000ff>测<#ff00c2>试</></></>")
log.info("<a href=\"https://www.baidu.com\">超<link href=\"https://www.bing.cn\">链接[重叠](https://www.360.com)</link></a>")

"""
while True:
    try:
        log.info(get_asctime())
        time.sleep(1)
    except KeyboardInterrupt:
        log.info("测试结束")
        break
"""