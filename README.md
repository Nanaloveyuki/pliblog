## 安装
暂无安装包, 请使用release发布版或直接clone代码到本地

## 文档
暂无文档, 请查看代码注释

## 示例
```python
# 导入
from pliblog import Logger
# 或 import pliblog(不推荐)

# 实例化
logger = Logger()

#使用功能
logger.info("这是一条信息日志")

logger.warn("这是一条带有前缀的警告日志", prefix="114514")

logger.critical("这是一条带有前缀并且日志等级不同的严重错误日志", prefix="114514", level=55)
```