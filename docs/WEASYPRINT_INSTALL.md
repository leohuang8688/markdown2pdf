# WeasyPrint 安装指南

## 什么是 WeasyPrint？

WeasyPrint 是一个现代化的 PDF 渲染引擎，基于 Web 标准（HTML5、CSS3），相比 wkhtmltopdf 有以下优势：

- ✅ **更好的 emoji 支持** - 原生支持彩色 emoji
- ✅ **更好的 CSS3 支持** - 支持更多现代 CSS 特性
- ✅ **更稳定** - 不会崩溃
- ✅ **更清晰** - 渲染质量更高

## 安装 WeasyPrint

### 方法 1：pip 安装（推荐）

```bash
pip3 install weasyprint
```

### 方法 2：系统包安装

#### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install weasyprint
```

#### macOS
```bash
brew install weasyprint
```

#### CentOS/RHEL
```bash
sudo yum install python3-weasyprint
```

## 安装 Noto Color Emoji 字体

### Ubuntu/Debian
```bash
sudo apt-get install fonts-noto-color-emoji
fc-cache -fv  # 刷新字体缓存
```

### macOS
macOS 系统自带 Apple Color Emoji，无需额外安装。

### CentOS/RHEL
```bash
sudo yum install google-noto-emoji-fonts
fc-cache -fv  # 刷新字体缓存
```

## 验证安装

### 检查 WeasyPrint
```bash
weasyprint --version
```

输出示例：
```
WeasyPrint version 68.1
```

### 检查字体
```bash
fc-list | grep -i "noto.*emoji"
```

输出示例：
```
/usr/share/fonts/google-noto-emoji-fonts/NotoColorEmoji.ttf: Noto Color Emoji:style=Regular
```

## 使用 WeasyPrint

### Python API
```python
from weasyprint import HTML, CSS

# 简单转换
HTML(string='<h1>Hello 🌈</h1>').write_pdf('output.pdf')

# 带样式转换
CSS(string='@page { size: A4; margin: 20mm; }').write_pdf('output.pdf', html)
```

### 命令行
```bash
weasyprint input.html output.pdf
```

## 在 markdown2pdf 中使用

markdown2pdf 会自动检测并使用 WeasyPrint：

```python
from src.converter import MarkdownConverter

converter = MarkdownConverter(theme='professional')
pdf_path = converter.convert_to_pdf(
    markdown_text="# Hello 🌈",
    output_filename="test.pdf"
)
```

如果 WeasyPrint 不可用，会自动回退到 pdfkit。

## 故障排除

### 问题 1：WeasyPrint 安装失败

**错误信息：**
```
ERROR: Could not find a version that satisfies the requirement weasyprint
```

**解决方案：**
```bash
# 确保 pip 是最新版本
pip3 install --upgrade pip

# 重新安装
pip3 install weasyprint
```

### 问题 2：emoji 不显示为彩色

**可能原因：**
1. Noto Color Emoji 字体未安装
2. 字体缓存未刷新

**解决方案：**
```bash
# 安装字体
sudo apt-get install fonts-noto-color-emoji

# 刷新字体缓存
fc-cache -fv

# 验证字体
fc-list | grep -i "noto.*emoji"
```

### 问题 3：WeasyPrint 渲染慢

**可能原因：**
- 文档太大
- 图片太多

**解决方案：**
1. 减少图片数量
2. 压缩图片
3. 分批生成 PDF

## 性能对比

| 引擎 | 速度 | 质量 | emoji 支持 | CSS3 支持 |
|------|------|------|-----------|----------|
| WeasyPrint | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ✅ 原生彩色 | ✅ 完整 |
| pdfkit | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⚠️ 文字替换 | ⚠️ 部分 |

## 推荐配置

**推荐配置：**
- WeasyPrint 68.1+
- Noto Color Emoji 字体
- Python 3.10+

**备用配置：**
- pdfkit 1.0.0+
- wkhtmltopdf 0.12.6+
- Python 3.10+

---

**最后更新：** 2026-03-19  
**联系方式：** claw@pocketai.sg
