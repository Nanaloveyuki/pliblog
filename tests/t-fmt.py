import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from src.utils.fmt import fmt_level, fmt_level_number, fmt_console, fmt_message, fmt_placeholder

print("日志级别测试")
print(fmt_level("DEBUG"))
print(fmt_level("INFO"))
print(fmt_level("WARN"))
print(fmt_level("ERRO"))
print(fmt_level("CRIT"))
print(fmt_level("UNKN"))

print("日志级别数字测试")
print(fmt_level_number(10))
print(fmt_level_number(20))
print(fmt_level_number(30))
print(fmt_level_number(40))
print(fmt_level_number(50))
print(fmt_level_number(-1))
print(fmt_level_number(100))

print("消息格式化测试")
print(fmt_message("测试消息: {time},\n {asctime}, \n{unknown}"))

print("控制台格式化测试")
print(fmt_console(10, "测试消息"))
print("前缀测试")
print(fmt_console(35, "测试消息", "可爱猫猫"))

print("未知日志级别测试")
print(fmt_console(-1, "测试消息"))


print("颜色插值测试")
print("分段颜色插值")
formatted_msg = fmt_message("测试消息<#ff0000>red</>")
processed_msg = fmt_placeholder(formatted_msg)
print(fmt_console(15, processed_msg))

print("单段颜色插值")
print(fmt_console(15, fmt_placeholder("测试消息<#00ff00>green{asctime}</>", use_date_color=False)))

print("不完整颜色插值")
print(fmt_console(15, fmt_placeholder("测试消息<#00ff00>green{asctime}", use_date_color=False)))
print(fmt_console(15, fmt_placeholder("测试消息</>green{asctime}", use_date_color=False)))
print(fmt_console(15, fmt_placeholder("测试消息<#00ff000>green{asctime}</>", use_date_color=False)))