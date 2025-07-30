import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from src.logiliteal import logger

logger.debug("这是一条调试信息")
logger.debug("这是**粗体**")
logger.debug("这是*斜体*")
logger.debug("这是__下划线__")
logger.debug("这是~~删除线~~")
logger.debug("这是**粗斜体**")
logger.debug("这是__粗下划线__")
logger.debug("这是~~删除线~~")
logger.debug("这是<#ff0000>红色</>")
logger.debug("这是<#00ff00>绿色</>")
logger.debug("这是<#0000ff>蓝色</>")
logger.debug("这是<#ff0000>嵌<#00ff00>套</></>")
logger.debug("这是<#ff0000>不完全闭合")
logger.debug("这是<#ff0000>样式<c>清理")
logger.debug("这是<b>粗体</b>")
logger.debug("这是<i>斜体</i>")
logger.debug("这是<u>下划线</u>")
logger.debug("这是<s>删除线</s>")
logger.debug("这是<b><i>粗斜体</i></b>")
logger.debug("这是<b><u>粗下划线</u></b>")
logger.debug("这是<b><s>粗删除线</s></b>")
logger.debug("这是前缀", prefix="<#ff0000>111")
logger.debug("这是后缀", suffix="</>")