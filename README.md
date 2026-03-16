# 📄 Markdown2PDF

**An OpenClaw skill that converts markdown output to PDF files and PNG images with customizable themes.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

---

## ✨ Features

- 📄 **Markdown to PDF** - Convert markdown documents to professional PDF files
- 🖼️ **Markdown to PNG** - Convert markdown to high-quality PNG images
- 🎨 **Multiple Themes** - 5 built-in themes (default, dark, github, minimal, professional)
- 🎯 **Customizable** - Custom CSS support for complete control
- 🚀 **Fast & Easy** - Simple CLI interface
- 🧩 **OpenClaw Integration** - Seamless integration with OpenClaw
- 📱 **Responsive** - Output looks great on all devices

---

## 🚀 Quick Start

### Installation

```bash
# Clone to OpenClaw skills directory
cd ~/.openclaw/workspace/skills
git clone https://github.com/leohuang8688/markdown2pdf.git
cd markdown2pdf

# Install dependencies
pip install -r requirements.txt

# Install wkhtmltopdf (required for PDF/PNG generation)
# macOS
brew install wkhtmltopdf

# Ubuntu/Debian
sudo apt-get install wkhtmltopdf

# Windows
# Download from https://wkhtmltopdf.org/downloads.html
```

### Basic Usage

```bash
# Convert to PDF and PNG (default)
python3 src/converter.py input.md

# Convert to PDF only
python3 src/converter.py input.md -f pdf

# Convert to PNG only
python3 src/converter.py input.md -f png

# Use dark theme
python3 src/converter.py input.md -t dark

# Specify output filename
python3 src/converter.py input.md -o my-document

# Use github theme and output to specific directory
python3 src/converter.py input.md -t github -o output -d ./docs
```

---

## 🎨 Available Themes

### `default`
Clean, modern design with system fonts. Perfect for general use.

### `dark`
Dark theme with light text. Easy on the eyes, great for presentations.

### `github`
GitHub-style rendering. Familiar look for developers.

### `minimal`
Minimalist design with serif fonts. Elegant and professional.

### `professional`
Business-ready design. Perfect for reports and documentation.

### List Themes

```bash
python3 src/converter.py --list-themes
```

---

## 📖 API Usage

### Python API

```python
from src.converter import MarkdownConverter, convert_markdown, convert_markdown_to_pdf

# Basic conversion
results = convert_markdown(
    markdown_text="# Hello World",
    output_filename="output",
    formats=["pdf", "png"],
    theme="github"
)

# PDF only
pdf_path = convert_markdown_to_pdf(
    markdown_text="# Document",
    output_filename="doc.pdf",
    theme="professional"
)

# Advanced usage with custom settings
converter = MarkdownConverter(
    output_dir=Path("./output"),
    theme="dark",
    custom_css=".custom { color: red; }"
)

# Convert to multiple formats
results = converter.convert(
    markdown_text="# My Document",
    output_filename="document",
    formats=["pdf", "png"],
    width=1920,  # PNG width
    page_size="Letter",  # PDF page size
    margin="15mm"  # PDF margin
)
```

### CLI Options

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
  --width WIDTH         PNG width in pixels
  --page-size PAGE_SIZE
                        PDF page size
  --margin MARGIN       PDF margin
  --list-themes         List available themes
```

---

## 📁 Project Structure

```
markdown2pdf/
├── src/
│   └── converter.py          # Main converter with theme support
├── tests/
│   └── test_converter.py     # Test suite
├── assets/                    # Theme assets and templates
├── pyproject.toml            # Python project configuration
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── SKILL.md                  # OpenClaw skill definition
```

---

## 🧪 Testing

```bash
# Run tests
pytest tests/

# Test with sample markdown
echo "# Test Document\n\nThis is a **test**." > test.md
python3 src/converter.py test.md -t github
```

---

## 🎯 Use Cases

### 1. **Documentation**
Convert your markdown documentation to professional PDFs for distribution.

### 2. **Presentations**
Create beautiful PNG images from markdown for slides or social media.

### 3. **Reports**
Generate formatted reports from markdown notes.

### 4. **Blog Posts**
Preview how your blog posts will look before publishing.

### 5. **README Files**
Convert GitHub README files to PDF for offline reading.

---

## 🔧 Configuration

### OpenClaw Integration

In your OpenClaw configuration:

```json
{
  "skills": {
    "markdown2pdf": {
      "enabled": true,
      "config": {
        "default_theme": "github",
        "default_formats": ["pdf"],
        "output_dir": "./documents"
      }
    }
  }
}
```

### Environment Variables

```bash
export MARKDOWN2PDF_THEME=github
export MARKDOWN2PDF_OUTPUT_DIR=./output
export MARKDOWN2PDF_FORMATS=pdf,png
```

---

## 📊 Examples

### Example 1: Simple Conversion

```bash
# Convert README to PDF
python3 src/converter.py README.md -f pdf -t github
```

### Example 2: Batch Conversion

```bash
# Convert all markdown files in directory
for file in *.md; do
    python3 src/converter.py "$file" -f pdf -t professional
done
```

### Example 3: Custom Styling

```python
from src.converter import MarkdownConverter

custom_css = """
h1 { color: #2c3e50; border-bottom: 2px solid #3498db; }
.codehilite { background: #f8f8f8; padding: 10px; }
"""

converter = MarkdownConverter(
    theme='minimal',
    custom_css=custom_css
)

converter.convert_to_pdf(
    markdown_text="# Custom Styled Document",
    output_filename='custom.pdf'
)
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

- [markdown](https://pypi.org/project/markdown/) - Markdown processing
- [pdfkit](https://pypi.org/project/pdfkit/) - PDF generation
- [imgkit](https://pypi.org/project/imgkit/) - Image generation
- [wkhtmltopdf](https://wkhtmltopdf.org/) - HTML to PDF engine
- OpenClaw Team - For the amazing framework

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/leohuang8688/markdown2pdf/issues)
- **Discussions**: [GitHub Discussions](https://github.com/leohuang8688/markdown2pdf/discussions)

---

**Happy Converting! 📄🖼️**
