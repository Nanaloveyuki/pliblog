#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试颜色优先级处理功能
"""
import sys
import os
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.logiliteal.utils.fmt import fmt_message

def test_color_priority():
    """测试颜色优先级"""
    print("=== 颜色优先级测试 ===")
    
    # 测试1: 基本颜色标签
    test1 = "<#ff0000>红色文本</>"
    print(f"基本颜色: {test1}")
    print(f"结果: {fmt_message(test1)}")
    print()
    
    # 测试2: 嵌套颜色（内层优先级高）
    test2 = "<#ff0000>外层<#00ff00>内层</>外层</>"
    print(f"嵌套颜色: {test2}")
    print(f"结果: {fmt_message(test2)}")
    print()
    
    # 测试3: 颜色重叠测试（最后边颜色为主）
    test3 = "<#ff0000>颜色重叠<#0000ff>测<#ff00c2>试</></></>"
    print(f"颜色重叠: {test3}")
    print(f"结果: {fmt_message(test3)}")
    print()
    
    # 测试4: 多层嵌套
    test4 = "<#ff0000>1<#00ff00>2<#0000ff>3<#ffff00>4</>3</>2</>1</>"
    print(f"多层嵌套: {test4}")
    print(f"结果: {fmt_message(test4)}")
    print()
    
    # 测试5: 未闭合标签（忽略）
    test5 = "<#ff0000>未闭合标签"
    print(f"未闭合标签: {test5}")
    print(f"结果: {fmt_message(test5)}")
    print()

if __name__ == "__main__":
    test_color_priority()