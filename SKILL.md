{
  "name": "markdown2pdf",
  "description": "Professional Markdown to PDF/PNG converter with colored emoji support. Convert markdown documents to beautiful PDF files and PNG images with customizable themes.",
  "version": "1.0.0",
  "author": "PocketAI for Leo",
  "license": "MIT",
  "repository": "https://github.com/leohuang8688/markdown2pdf",
  "entry": "src/converter.py",
  "type": "skill",
  "category": "document",
  "tags": ["markdown", "pdf", "png", "converter", "document", "openclaw"],
  "commands": [
    {
      "name": "convert",
      "description": "Convert markdown to PDF/PNG with themes",
      "usage": "markdown2pdf convert <input.md> [-f formats] [-t theme] [-o output]",
      "examples": [
        "python3 src/converter.py README.md -t github -f pdf",
        "python3 src/converter.py report.md -t professional -f pdf,png"
      ]
    },
    {
      "name": "themes",
      "description": "List available themes",
      "usage": "markdown2pdf themes",
      "examples": [
        "python3 src/converter.py --list-themes"
      ]
    }
  ],
  "config": {
    "default_theme": "professional",
    "default_formats": ["pdf"],
    "default_width": 1200,
    "default_page_size": "A4",
    "default_margin": "20mm",
    "emoji_support": true,
    "colored_emoji": true
  },
  "dependencies": [
    "markdown>=3.5.0",
    "pdfkit>=1.0.0",
    "imgkit>=1.2.3",
    "wkhtmltopdf>=0.2.0"
  ],
  "features": [
    "Markdown to PDF conversion",
    "Markdown to PNG conversion",
    "5 professional themes",
    "Colored emoji support",
    "Custom CSS support",
    "CLI and API interfaces",
    "OpenClaw integration"
  ],
  "changelog": {
    "1.0.0": {
      "date": "2026-03-16",
      "changes": [
        "Initial release",
        "Markdown to PDF/PNG converter",
        "5 professional themes",
        "Colored emoji replacement",
        "Custom CSS support",
        "CLI and API interfaces",
        "Complete documentation"
      ]
    }
  }
}
