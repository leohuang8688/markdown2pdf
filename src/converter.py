#!/usr/bin/env python3
"""
Markdown to PDF/PNG Converter

A utility to convert markdown content to PDF files and PNG images.
"""

import markdown
import pdfkit
import imgkit
import tempfile
import os
from pathlib import Path
from typing import Optional, Union


class MarkdownConverter:
    """Converter for markdown to PDF and PNG."""
    
    def __init__(self, output_dir: Optional[Path] = None):
        """
        Initialize the converter.
        
        Args:
            output_dir: Output directory for generated files. Defaults to current directory.
        """
        self.output_dir = output_dir or Path.cwd()
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
    def markdown_to_html(self, markdown_text: str) -> str:
        """
        Convert markdown to HTML.
        
        Args:
            markdown_text: Markdown text to convert.
            
        Returns:
            HTML string.
        """
        # Convert markdown to HTML with extensions
        html = markdown.markdown(
            markdown_text,
            extensions=[
                'extra',
                'codehilite',
                'toc',
                'tables',
                'fenced_code'
            ]
        )
        
        # Add basic HTML structure and styling
        html_template = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            color: #333;
        }}
        code {{
            background-color: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }}
        pre {{
            background-color: #f4f4f4;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }}
        pre code {{
            padding: 0;
            background: none;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }}
        th {{
            background-color: #f4f4f4;
            font-weight: bold;
        }}
        blockquote {{
            border-left: 4px solid #ddd;
            margin: 20px 0;
            padding-left: 20px;
            color: #666;
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: #333;
            margin-top: 24px;
            margin-bottom: 16px;
        }}
        a {{
            color: #0366d6;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
    </style>
</head>
<body>
{html}
</body>
</html>
"""
        return html_template
    
    def convert_to_pdf(
        self,
        markdown_text: str,
        output_filename: Optional[str] = None,
        output_dir: Optional[Path] = None
    ) -> Path:
        """
        Convert markdown to PDF.
        
        Args:
            markdown_text: Markdown text to convert.
            output_filename: Output filename. Defaults to 'output.pdf'.
            output_dir: Output directory. Defaults to instance output_dir.
            
        Returns:
            Path to generated PDF file.
        """
        if output_filename is None:
            output_filename = 'output.pdf'
            
        output_path = (output_dir or self.output_dir) / output_filename
        
        # Convert markdown to HTML
        html = self.markdown_to_html(markdown_text)
        
        # Convert HTML to PDF
        pdfkit.from_string(
            html,
            str(output_path),
            options={
                'page-size': 'A4',
                'margin-top': '20mm',
                'margin-right': '20mm',
                'margin-bottom': '20mm',
                'margin-left': '20mm',
                'encoding': 'UTF-8',
                'no-outline': None
            }
        )
        
        return output_path
    
    def convert_to_png(
        self,
        markdown_text: str,
        output_filename: Optional[str] = None,
        output_dir: Optional[Path] = None,
        width: int = 1200
    ) -> Path:
        """
        Convert markdown to PNG image.
        
        Args:
            markdown_text: Markdown text to convert.
            output_filename: Output filename. Defaults to 'output.png'.
            output_dir: Output directory. Defaults to instance output_dir.
            width: Image width in pixels. Defaults to 1200.
            
        Returns:
            Path to generated PNG file.
        """
        if output_filename is None:
            output_filename = 'output.png'
            
        output_path = (output_dir or self.output_dir) / output_filename
        
        # Convert markdown to HTML
        html = self.markdown_to_html(markdown_text)
        
        # Convert HTML to PNG
        imgkit.from_string(
            html,
            str(output_path),
            options={
                'width': width,
                'format': 'png',
                'quality': 100
            }
        )
        
        return output_path
    
    def convert(
        self,
        markdown_text: str,
        output_filename: Optional[str] = None,
        output_dir: Optional[Path] = None,
        formats: list = ['pdf', 'png']
    ) -> dict:
        """
        Convert markdown to multiple formats.
        
        Args:
            markdown_text: Markdown text to convert.
            output_filename: Base output filename (without extension).
            output_dir: Output directory. Defaults to instance output_dir.
            formats: List of formats to convert to. Defaults to ['pdf', 'png'].
            
        Returns:
            Dictionary with paths to generated files.
        """
        if output_filename is None:
            output_filename = 'output'
            
        output_dir = output_dir or self.output_dir
        output_dir.mkdir(parents=True, exist_ok=True)
        
        results = {}
        
        if 'pdf' in formats:
            pdf_path = self.convert_to_pdf(
                markdown_text,
                f'{output_filename}.pdf',
                output_dir
            )
            results['pdf'] = pdf_path
            
        if 'png' in formats:
            png_path = self.convert_to_png(
                markdown_text,
                f'{output_filename}.png',
                output_dir
            )
            results['png'] = png_path
            
        return results


# Convenience functions
def convert_markdown_to_pdf(
    markdown_text: str,
    output_filename: str = 'output.pdf',
    output_dir: Optional[Path] = None
) -> Path:
    """Convert markdown to PDF."""
    converter = MarkdownConverter(output_dir)
    return converter.convert_to_pdf(markdown_text, output_filename)


def convert_markdown_to_png(
    markdown_text: str,
    output_filename: str = 'output.png',
    output_dir: Optional[Path] = None,
    width: int = 1200
) -> Path:
    """Convert markdown to PNG."""
    converter = MarkdownConverter(output_dir)
    return converter.convert_to_png(markdown_text, output_filename, width)


def convert_markdown(
    markdown_text: str,
    output_filename: str = 'output',
    output_dir: Optional[Path] = None,
    formats: list = ['pdf', 'png']
) -> dict:
    """Convert markdown to multiple formats."""
    converter = MarkdownConverter(output_dir)
    return converter.convert(markdown_text, output_filename, output_dir, formats)


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python converter.py <input.md> [output_filename] [formats]")
        print("  formats: comma-separated list of formats (pdf,png)")
        print("  Example: python converter.py input.md output pdf,png")
        sys.exit(1)
    
    input_file = Path(sys.argv[1])
    output_filename = sys.argv[2] if len(sys.argv) > 2 else None
    formats = sys.argv[3].split(',') if len(sys.argv) > 3 else ['pdf', 'png']
    
    with open(input_file, 'r', encoding='utf-8') as f:
        markdown_text = f.read()
    
    results = convert_markdown(
        markdown_text,
        output_filename,
        formats=formats
    )
    
    print("✅ Conversion complete!")
    for format_name, path in results.items():
        print(f"  {format_name.upper()}: {path}")
