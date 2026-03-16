---
name: markdown2pdf
description: OpenClaw skill that converts markdown output to PDF files and PNG images. Supports multiple output formats with customizable styling.
---

# Markdown2PDF Skill

**Convert markdown content to PDF files and PNG images for OpenClaw.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

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
# Navigate to skills directory
cd /root/.openclaw/workspace/skills

# Clone the repository
git clone https://github.com/leohuang8688/markdown2pdf.git
cd markdown2pdf

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

#### Python API

```python
from converter import MarkdownConverter

# Initialize converter
converter = MarkdownConverter()

# Convert to PDF
pdf_path = converter.convert_to_pdf("# Hello World\n\nThis is a test.")

# Convert to PNG
png_path = converter.convert_to_png("# Hello World\n\nThis is a test.")

# Convert to multiple formats
results = converter.convert(
    "# Hello World\n\nThis is a test.",
    output_filename="output",
    formats=['pdf', 'png']
)
```

#### Command Line

```bash
# Convert to PDF and PNG
python3 src/converter.py input.md output.pdf pdf,png

# Convert to PDF only
python3 src/converter.py input.md output.pdf pdf

# Convert to PNG only
python3 src/converter.py input.md output.png png
```

---

## 📖 API Reference

### MarkdownConverter Class

#### `__init__(output_dir: Optional[Path] = None)`

Initialize the converter.

**Args:**
- `output_dir`: Output directory for generated files. Defaults to current directory.

#### `markdown_to_html(markdown_text: str) -> str`

Convert markdown to HTML.

**Args:**
- `markdown_text`: Markdown text to convert.

**Returns:**
- HTML string with styling.

#### `convert_to_pdf(markdown_text: str, output_filename: Optional[str] = None, output_dir: Optional[Path] = None) -> Path`

Convert markdown to PDF.

**Args:**
- `markdown_text`: Markdown text to convert.
- `output_filename`: Output filename. Defaults to 'output.pdf'.
- `output_dir`: Output directory. Defaults to instance output_dir.

**Returns:**
- Path to generated PDF file.

#### `convert_to_png(markdown_text: str, output_filename: Optional[str] = None, output_dir: Optional[Path] = None, width: int = 1200) -> Path`

Convert markdown to PNG.

**Args:**
- `markdown_text`: Markdown text to convert.
- `output_filename`: Output filename. Defaults to 'output.png'.
- `output_dir`: Output directory. Defaults to instance output_dir.
- `width`: Image width in pixels. Defaults to 1200.

**Returns:**
- Path to generated PNG file.

#### `convert(markdown_text: str, output_filename: Optional[str] = None, output_dir: Optional[Path] = None, formats: list = ['pdf', 'png']) -> dict`

Convert markdown to multiple formats.

**Args:**
- `markdown_text`: Markdown text to convert.
- `output_filename`: Base output filename (without extension).
- `output_dir`: Output directory. Defaults to instance output_dir.
- `formats`: List of formats to convert to. Defaults to ['pdf', 'png'].

**Returns:**
- Dictionary with paths to generated files.

---

## 🎨 Custom Styling

The converter includes beautiful default styling:

- **Font**: System fonts (Apple System, BlinkMacSystemFont, Segoe UI, Roboto, etc.)
- **Line Height**: 1.6 for readability
- **Code Blocks**: Syntax highlighting with codehilite
- **Tables**: Clean, bordered tables
- **Blockquotes**: Styled with left border
- **Links**: GitHub-style blue links

### Custom CSS

To customize styling, modify the `markdown_to_html` method in `converter.py`:

```python
html_template = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        /* Your custom CSS here */
        body {{
            font-family: Your Font;
        }}
    </style>
</head>
<body>
{html}
</body>
</html>
"""
```

---

## 📁 Project Structure

```
markdown2pdf/
├── src/
│   └── converter.py          # Main converter module
├── tests/
│   └── test_converter.py     # Test suite
├── assets/                    # Assets directory
├── pyproject.toml            # Python project config
├── requirements.txt          # Python dependencies
├── SKILL.md                  # OpenClaw skill definition
└── README.md                 # This file
```

---

## 🧪 Testing

Run the test suite:

```bash
cd /root/.openclaw/workspace/skills/markdown2pdf
pytest tests/
```

### Example Test

```python
import unittest
from src.converter import MarkdownConverter

class TestMarkdownConverter(unittest.TestCase):
    def test_convert_to_pdf(self):
        converter = MarkdownConverter()
        pdf_path = converter.convert_to_pdf("# Test")
        self.assertTrue(pdf_path.exists())
    
    def test_convert_to_png(self):
        converter = MarkdownConverter()
        png_path = converter.convert_to_png("# Test")
        self.assertTrue(png_path.exists())

if __name__ == '__main__':
    unittest.main()
```

---

## 🔧 OpenClaw Integration

### Skill Configuration

In OpenClaw configuration file:

```json
{
  "skills": {
    "markdown2pdf": {
      "enabled": true,
      "output_dir": "/path/to/output"
    }
  }
}
```

### Usage in OpenClaw

```python
from skills.markdown2pdf.src.converter import MarkdownConverter

# Initialize with OpenClaw workspace
converter = MarkdownConverter()

# Convert markdown output
results = converter.convert(
    markdown_text,
    output_filename="output",
    formats=['pdf', 'png']
)
```

---

## 📝 Examples

### Example 1: Simple Conversion

```python
from converter import convert_markdown

markdown = """
# Hello World

This is a **test** document.

## Features

- Feature 1
- Feature 2
- Feature 3
"""

results = convert_markdown(markdown, output_filename="hello")
# Generates: hello.pdf and hello.png
```

### Example 2: Custom Output Directory

```python
from pathlib import Path
from converter import MarkdownConverter

converter = MarkdownConverter(output_dir=Path('/tmp/output'))
pdf_path = converter.convert_to_pdf("# Hello World")
# Generates: /tmp/output/output.pdf
```

### Example 3: Multiple Formats

```python
from converter import MarkdownConverter

converter = MarkdownConverter()
results = converter.convert(
    "# Hello World",
    output_filename="document",
    formats=['pdf', 'png', 'html']
)
# Generates: document.pdf, document.png, document.html
```

---

## 🛠️ Dependencies

- **markdown** - Markdown parsing
- **pdfkit** - HTML to PDF conversion
- **imgkit** - HTML to PNG conversion
- **wkhtmltopdf** - PDF rendering engine

### Install Dependencies

```bash
pip install markdown pdfkit imgkit wkhtmltopdf
```

Or install from requirements.txt:

```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

MIT License - See [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**PocketAI for Leo** - OpenClaw Community

GitHub: [@leohuang8688](https://github.com/leohuang8688/markdown2pdf)

---

## 🙏 Acknowledgments

- **markdown** - Python markdown parser
- **pdfkit** - wkhtmltopdf Python wrapper
- **imgkit** - wkhtmltopdf image Python wrapper
- **wkhtmltopdf** - HTML to PDF/PNG rendering engine

---

**Happy Converting! 📄🖼️**
