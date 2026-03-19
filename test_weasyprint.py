#!/usr/bin/env python3
"""
测试 WeasyPrint emoji 支持
"""

from weasyprint import HTML, CSS
from pathlib import Path
import tempfile

# 创建测试 HTML
html_content = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Emoji 测试</title>
    <style>
        @page {
            size: A4;
            margin: 20mm;
        }
        body {
            font-family: "Noto Color Emoji", "Apple Color Emoji", "Segoe UI Emoji", sans-serif;
            font-size: 24px;
            line-height: 1.6;
        }
        h1 {
            font-size: 32px;
            color: #2c3e50;
        }
    </style>
</head>
<body>
    <h1>🚀 Emoji 字体测试</h1>
    
    <h2>📊 数据图表</h2>
    <p>📊 📈 📉</p>
    
    <h2>✅ 状态符号</h2>
    <p>✅ ❌ ⚠️</p>
    
    <h2>⬆️ 方向箭头</h2>
    <p>⬆️ ⬇️ ➡️ ⬅️</p>
    
    <h2>☀ 天气符号</h2>
    <p>☀ ☁ ❄</p>
    
    <h2>★ 符号</h2>
    <p>★ ☆ ♥ ♦</p>
    
    <h2>❶ 数字</h2>
    <p>❶ ❷ ❸ ❹ ❺</p>
    
    <h2>🅰 字母</h2>
    <p>🅰 🅱 🅾 🅿</p>
    
    <h2>🔴 彩色圆形</h2>
    <p>🔴 🟢 🔵 🟡 🟠</p>
    
    <p style="margin-top: 50px; color: #666;">
        如果以上 emoji 显示为彩色，说明 WeasyPrint 配置成功！✅
    </p>
</body>
</html>
"""

# 生成 PDF
output_path = Path('/tmp/weasyprint_emoji_test.pdf')

try:
    html = HTML(string=html_content)
    html.write_pdf(str(output_path))
    
    print(f'✅ WeasyPrint PDF 生成成功！')
    print(f'📍 文件位置：{output_path}')
    print(f'📊 文件大小：{output_path.stat().st_size/1024:.1f}K')
except Exception as e:
    print(f'❌ WeasyPrint PDF 生成失败：{e}')
