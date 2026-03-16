---
name: markdown2pdf
description: OpenClaw skill that converts markdown output to PDF files and PNG images. Supports multiple output formats with customizable styling.
---

# Markdown2PDF Skill

**Convert markdown content to PDF files and PNG images for OpenClaw.**

---

## ✨ Features

- 📄 **Markdown to PDF** - Convert markdown to professional PDF documents
- 🖼️ **Markdown to PNG** - Convert markdown to high-quality PNG images
- 🎨 **Custom Styling** - Beautiful default styling with customization options
- 📦 **Multiple Formats** - Convert to multiple formats simultaneously
- 🔧 **Easy to Use** - Simple API and command-line interface
- 🚀 **OpenClaw Integration** - Seamless integration with OpenClaw

---

## 🚀 Quick Start

### Installation

```bash
cd /root/.openclaw/workspace/skills
git clone https://github.com/leohuang8688/markdown2pdf.git
cd markdown2pdf
pip install -r requirements.txt
```

### Usage

```python
from converter import MarkdownConverter

# Initialize converter
converter = MarkdownConverter()

# Convert to PDF
pdf_path = converter.convert_to_pdf("# Hello World")

# Convert to PNG
png_path = converter.convert_to_png("# Hello World")

# Convert to multiple formats
results = converter.convert("# Hello World", formats=['pdf', 'png'])
```

---

## 📖 API

### MarkdownConverter

- `markdown_to_html(markdown_text)` - Convert to HTML
- `convert_to_pdf(markdown_text, output_filename)` - Convert to PDF
- `convert_to_png(markdown_text, output_filename, width)` - Convert to PNG
- `convert(markdown_text, formats)` - Convert to multiple formats

---

## 📁 Structure

```
markdown2pdf/
├── src/converter.py
├── tests/test_converter.py
├── requirements.txt
├── SKILL.md
└── README.md
```

---

## 🧪 Testing

```bash
pytest tests/
```

---

## 📝 License

MIT License

---

## 👨‍💻 Author

PocketAI for Leo
