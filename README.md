# 📄 Markdown2PDF

**一个专业的 OpenClaw 技能，将 Markdown 文档转换为彩色 PDF 和 PNG 图片，支持 emoji 转彩色文字标签。**

[![Version 1.0.0](https://img.shields.io/badge/version-1.0.0-green.svg)](https://github.com/leohuang8688/markdown2pdf)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

---

## ✨ 核心功能

- 📄 **Markdown 转 PDF** - 专业 PDF 文档生成
- 🖼️ **Markdown 转 PNG** - 高质量 PNG 图片
- 🎨 **5 种专业主题** - default, dark, github, minimal, professional
- 🌈 **彩色 Emoji 支持** - 自动转换为彩色文字标签
- ✨ **自定义 CSS** - 完全控制样式
- 🚀 **CLI 和 API** - 多种使用方式
- 🧩 **OpenClaw 集成** - 无缝集成

---

## 🚀 快速开始

### 安装依赖

```bash
cd ~/.openclaw/workspace/skills/markdown2pdf

# 安装 Python 依赖
pip3 install markdown pdfkit imgkit

# 安装 wkhtmltopdf（必需）
# macOS
brew install wkhtmltopdf

# Ubuntu/Debian
sudo apt-get install wkhtmltopdf

# CentOS/RHEL
sudo yum install wkhtmltopdf
```

### 基本使用

```bash
# 转换为 PDF 和 PNG
python3 src/converter.py input.md

# 只生成 PDF
python3 src/converter.py input.md -f pdf

# 使用主题
python3 src/converter.py input.md -t github -f pdf

# 列出主题
python3 src/converter.py --list-themes
```

---

## 🎨 主题系统

### 可用主题

| 主题 | 描述 | 适用场景 |
|------|------|----------|
| `default` | 现代简洁设计 | 通用文档 |
| `dark` | 深色主题 | 演示、夜间阅读 |
| `github` | GitHub 风格 | 技术文档、README |
| `minimal` | 极简设计 | 优雅文档、出版物 |
| `professional` | 商务风格 | 报告、商业文档 |

### 使用主题

```bash
# 使用 github 主题
python3 src/converter.py README.md -t github -f pdf -o readme

# 使用 professional 主题
python3 src/converter.py report.md -t professional -f pdf
```

---

## 🌈 彩色 Emoji 支持

### 自动转换

markdown2pdf 会自动将 emoji 转换为彩色文字标签，确保在 PDF 中正常显示：

| Emoji | 转换后 | 颜色 |
|-------|--------|------|
| 📊 | [数据] | 🔵 蓝色 |
| 📈 | [趋势↑] | 🟢 绿色 |
| 📉 | [趋势↓] | 🔴 红色 |
| ✅ | [√] | 🟢 绿色 |
| ❌ | [×] | 🔴 红色 |
| ⚠️ | [!] | 🟠 橙色 |
| 🚀 | [启动] | 🔴 红色 |
| ⭐ | ★ | 🟡 金色 |

### 颜色语义

- 🟢 **绿色** - 积极、上涨、成功
- 🔴 **红色** - 消极、下跌、警告
- 🔵 **蓝色** - 中性、信息、数据
- 🟡 **金色** - 重要、亮点、金钱
- 🟠 **橙色** - 注意、警告

---

## 📖 API 使用

### Python API

```python
from src.converter import (
    MarkdownConverter,
    convert_markdown,
    convert_markdown_to_pdf,
    convert_markdown_to_png
)

# 方法 1: 简单转换
pdf_path = convert_markdown_to_pdf(
    markdown_text="# Hello World",
    output_filename="hello.pdf",
    theme="github"
)

# 方法 2: 多格式转换
results = convert_markdown(
    markdown_text="# Document",
    output_filename="doc",
    formats=["pdf", "png"],
    theme="professional"
)

# 方法 3: 高级用法
converter = MarkdownConverter(
    output_dir=Path("./output"),
    theme="dark",
    custom_css=".custom { color: red; }"
)

# 转换为 PDF
pdf_path = converter.convert_to_pdf(
    markdown_text="# My Document",
    output_filename="document.pdf",
    page_size="A4",
    margin="15mm"
)

# 转换为 PNG
png_path = converter.convert_to_png(
    markdown_text="# My Document",
    output_filename="document.png",
    width=1920,
    quality=100
)
```

---

## 🔧 CLI 选项

```
usage: converter.py [-h] [-o OUTPUT] [-f FORMATS] [-t THEME] [-d OUTPUT_DIR]
                   [--width WIDTH] [--page-size PAGE_SIZE] [--margin MARGIN]
                   [--list-themes]
                   input

Convert Markdown to PDF/PNG

positional arguments:
  input                 Input markdown file

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output filename (without extension)
  -f FORMATS, --formats FORMATS
                        Output formats (comma-separated: pdf,png)
  -t THEME, --theme THEME
                        Theme (default, dark, github, minimal, professional)
  -d OUTPUT_DIR, --output-dir OUTPUT_DIR
                        Output directory
  --width WIDTH         PNG width in pixels (default: 1200)
  --page-size PAGE_SIZE
                        PDF page size (default: A4)
  --margin MARGIN       PDF margin (default: 20mm)
  --list-themes         List available themes
```

---

## 📁 项目结构

```
markdown2pdf/
├── src/
│   ├── converter.py          # 主转换器
│   └── emoji_replacer.py     # Emoji 转换工具
├── output/                    # 输出文件
├── tests/
│   └── test_converter.py     # 测试套件
├── pyproject.toml            # Python 项目配置
├── requirements.txt          # Python 依赖
├── README.md                 # 本文档
└── SKILL.md                  # OpenClaw 技能定义
```

---

## 🧪 测试

```bash
# 运行测试
pytest tests/

# 测试转换
python3 src/converter.py test_document.md -t github -f pdf
```

---

## 🎯 使用案例

### 1. 投资分析报告

```bash
python3 src/converter.py stock_analysis.md -t professional -f pdf
```

### 2. 技术文档

```bash
python3 src/converter.py README.md -t github -f pdf,png
```

### 3. 演示文稿

```bash
python3 src/converter.py presentation.md -t dark -f png --width 1920
```

### 4. 商业报告

```bash
python3 src/converter.py business_report.md -t professional -f pdf
```

---

## 🔗 相关项目

- [OpenClaw](https://github.com/openclaw/openclaw) - AI 助手框架
- [wkhtmltopdf](https://wkhtmltopdf.org/) - HTML 转 PDF 引擎
- [markdown](https://pypi.org/project/markdown/) - Markdown 处理库
- [pdfkit](https://pypi.org/project/pdfkit/) - Python PDF 生成库

---

## 🤝 贡献

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

---

## 📝 更新日志

### v1.0.0 (2026-03-16)

**首次正式发布**

#### 核心功能
- ✅ Markdown 转 PDF/PNG 转换器
- ✅ 5 种专业主题支持
- ✅ 彩色 Emoji 转文字标签
- ✅ 自定义 CSS 支持
- ✅ CLI 和 API 接口
- ✅ OpenClaw 技能集成

#### 技术特性
- ✅ 支持多种 Markdown 扩展
- ✅ 高质量 PDF 输出
- ✅ 可配置 PNG 分辨率
- ✅ 批量转换支持
- ✅ 完整的测试套件

#### 文档
- ✅ 完整 README 文档
- ✅ API 使用示例
- ✅ CLI 帮助文档
- ✅ 使用案例说明

---

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

---

## 👨‍💻 作者

**PocketAI for Leo** - OpenClaw Community

GitHub: [@leohuang8688](https://github.com/leohuang8688/markdown2pdf)

---

## 🙏 致谢

- [OpenClaw Team](https://github.com/openclaw/openclaw) - 优秀的框架
- [markdown](https://pypi.org/project/markdown/) - Markdown 处理
- [pdfkit](https://pypi.org/project/pdfkit/) - PDF 生成
- [imgkit](https://pypi.org/project/imgkit/) - 图片生成
- [wkhtmltopdf](https://wkhtmltopdf.org/) - HTML 转 PDF 引擎

---

## 📞 支持

- **问题反馈:** [GitHub Issues](https://github.com/leohuang8688/markdown2pdf/issues)
- **讨论:** [GitHub Discussions](https://github.com/leohuang8688/markdown2pdf/discussions)

---

**Happy Converting! 📄🎨**
