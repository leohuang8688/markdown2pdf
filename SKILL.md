{
  "name": "markdown2pdf",
  "description": "Convert markdown to PDF and PNG with customizable themes. Supports multiple themes (default, dark, github, minimal, professional).",
  "version": "1.0.0",
  "author": "PocketAI for Leo",
  "license": "MIT",
  "repository": "https://github.com/leohuang8688/markdown2pdf",
  "entry": "src/converter.py",
  "commands": [
    {
      "name": "convert",
      "description": "Convert markdown to PDF/PNG",
      "usage": "markdown2pdf convert <input.md> [-f formats] [-t theme] [-o output]"
    },
    {
      "name": "themes",
      "description": "List available themes",
      "usage": "markdown2pdf themes"
    }
  ],
  "config": {
    "default_theme": "default",
    "default_formats": ["pdf", "png"],
    "default_width": 1200,
    "default_page_size": "A4",
    "default_margin": "20mm"
  },
  "dependencies": [
    "markdown",
    "pdfkit",
    "imgkit",
    "wkhtmltopdf"
  ]
}
