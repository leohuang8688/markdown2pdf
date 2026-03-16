#!/usr/bin/env python3
"""
Markdown to PDF/PNG Converter with Custom Themes

A utility to convert markdown content to PDF files and PNG images with customizable themes.
"""

import markdown
import pdfkit
import imgkit
import tempfile
import os
import json
from pathlib import Path
from typing import Optional, Union, Dict, Any
from datetime import datetime


class Theme:
    """Theme configuration for markdown conversion."""
    
    THEMES = {
        'default': {
            'font_family': '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, sans-serif',
            'max_width': '800px',
            'line_height': '1.6',
            'text_color': '#333',
            'heading_color': '#333',
            'link_color': '#0366d6',
            'code_bg': '#f4f4f4',
            'pre_bg': '#f4f4f4',
            'border_color': '#ddd',
            'blockquote_border': '#ddd',
            'blockquote_color': '#666',
            'background': '#ffffff'
        },
        'dark': {
            'font_family': '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, sans-serif',
            'max_width': '800px',
            'line_height': '1.6',
            'text_color': '#e0e0e0',
            'heading_color': '#ffffff',
            'link_color': '#58a6ff',
            'code_bg': '#2d2d2d',
            'pre_bg': '#2d2d2d',
            'border_color': '#444',
            'blockquote_border': '#555',
            'blockquote_color': '#aaa',
            'background': '#1a1a1a'
        },
        'github': {
            'font_family': '-apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif',
            'max_width': '980px',
            'line_height': '1.5',
            'text_color': '#24292e',
            'heading_color': '#1b1f23',
            'link_color': '#0366d6',
            'code_bg': '#f6f8fa',
            'pre_bg': '#f6f8fa',
            'border_color': '#e1e4e8',
            'blockquote_border': '#dfe2e5',
            'blockquote_color': '#6a737d',
            'background': '#ffffff'
        },
        'minimal': {
            'font_family': 'Georgia, serif',
            'max_width': '700px',
            'line_height': '1.8',
            'text_color': '#2c3e50',
            'heading_color': '#2c3e50',
            'link_color': '#3498db',
            'code_bg': '#ecf0f1',
            'pre_bg': '#ecf0f1',
            'border_color': '#bdc3c7',
            'blockquote_border': '#3498db',
            'blockquote_color': '#7f8c8d',
            'background': '#ffffff'
        },
        'professional': {
            'font_family': '"Helvetica Neue", Arial, sans-serif',
            'max_width': '850px',
            'line_height': '1.6',
            'text_color': '#333333',
            'heading_color': '#2c3e50',
            'link_color': '#2980b9',
            'code_bg': '#f8f9fa',
            'pre_bg': '#f8f9fa',
            'border_color': '#dee2e6',
            'blockquote_border': '#6c757d',
            'blockquote_color': '#6c757d',
            'background': '#ffffff'
        }
    }
    
    @classmethod
    def get(cls, theme_name: str = 'default') -> Dict[str, str]:
        """Get theme configuration."""
        return cls.THEMES.get(theme_name, cls.THEMES['default'])
    
    @classmethod
    def list_themes(cls) -> list:
        """List available themes."""
        return list(cls.THEMES.keys())


class MarkdownConverter:
    """Converter for markdown to PDF and PNG with theme support."""
    
    def __init__(
        self,
        output_dir: Optional[Path] = None,
        theme: str = 'default',
        custom_css: Optional[str] = None
    ):
        """
        Initialize the converter.
        
        Args:
            output_dir: Output directory for generated files. Defaults to current directory.
            theme: Theme name to use. Options: default, dark, github, minimal, professional.
            custom_css: Custom CSS to add/override theme styles.
        """
        self.output_dir = output_dir or Path.cwd()
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.theme = Theme.get(theme)
        self.custom_css = custom_css or ''
        
    def generate_css(self) -> str:
        """Generate CSS from theme configuration."""
        theme = self.theme
        
        css = f"""
        body {{
            font-family: {theme['font_family']};
            line-height: {theme['line_height']};
            max-width: {theme['max_width']};
            margin: 0 auto;
            padding: 20px;
            color: {theme['text_color']};
            background-color: {theme['background']};
        }}
        code {{
            background-color: {theme['code_bg']};
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            color: {theme['text_color']};
        }}
        pre {{
            background-color: {theme['pre_bg']};
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            border: 1px solid {theme['border_color']};
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
            border: 1px solid {theme['border_color']};
            padding: 8px;
            text-align: left;
        }}
        th {{
            background-color: {theme['code_bg']};
            font-weight: bold;
        }}
        blockquote {{
            border-left: 4px solid {theme['blockquote_border']};
            margin: 20px 0;
            padding-left: 20px;
            color: {theme['blockquote_color']};
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: {theme['heading_color']};
            margin-top: 24px;
            margin-bottom: 16px;
            font-weight: 600;
        }}
        a {{
            color: {theme['link_color']};
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        img {{
            max-width: 100%;
            height: auto;
        }}
        hr {{
            border: none;
            border-top: 1px solid {theme['border_color']};
            margin: 30px 0;
        }}
        """
        
        if self.custom_css:
            css += f"\n{self.custom_css}\n"
        
        return css
    
    def markdown_to_html(self, markdown_text: str, title: str = 'Document') -> str:
        """
        Convert markdown to HTML.
        
        Args:
            markdown_text: Markdown text to convert.
            title: Document title.
            
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
                'fenced_code',
                'nl2br'
            ]
        )
        
        css = self.generate_css()
        
        # Add HTML structure with theme
        html_template = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>{css}</style>
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
        output_dir: Optional[Path] = None,
        title: str = 'Document',
        page_size: str = 'A4',
        margin: str = '20mm'
    ) -> Path:
        """
        Convert markdown to PDF.
        
        Args:
            markdown_text: Markdown text to convert.
            output_filename: Output filename. Defaults to 'output.pdf'.
            output_dir: Output directory. Defaults to instance output_dir.
            title: Document title.
            page_size: Page size (A4, Letter, etc.).
            margin: Page margin.
            
        Returns:
            Path to generated PDF file.
        """
        if output_filename is None:
            output_filename = 'output.pdf'
            
        output_path = (output_dir or self.output_dir) / output_filename
        
        # Convert markdown to HTML
        html = self.markdown_to_html(markdown_text, title)
        
        # Convert HTML to PDF
        pdfkit.from_string(
            html,
            str(output_path),
            options={
                'page-size': page_size,
                'margin-top': margin,
                'margin-right': margin,
                'margin-bottom': margin,
                'margin-left': margin,
                'encoding': 'UTF-8',
                'no-outline': None,
                'print-media-type': None
            },
            verbose=False,
            quiet=True
        )
        
        return output_path
    
    def convert_to_png(
        self,
        markdown_text: str,
        output_filename: Optional[str] = None,
        output_dir: Optional[Path] = None,
        title: str = 'Document',
        width: int = 1200,
        quality: int = 100
    ) -> Path:
        """
        Convert markdown to PNG image.
        
        Args:
            markdown_text: Markdown text to convert.
            output_filename: Output filename. Defaults to 'output.png'.
            output_dir: Output directory. Defaults to instance output_dir.
            title: Document title.
            width: Image width in pixels.
            quality: Image quality (1-100).
            
        Returns:
            Path to generated PNG file.
        """
        if output_filename is None:
            output_filename = 'output.png'
            
        output_path = (output_dir or self.output_dir) / output_filename
        
        # Convert markdown to HTML
        html = self.markdown_to_html(markdown_text, title)
        
        # Convert HTML to PNG
        imgkit.from_string(
            html,
            str(output_path),
            options={
                'width': width,
                'format': 'png',
                'quality': quality,
                'quiet': True
            }
        )
        
        return output_path
    
    def convert(
        self,
        markdown_text: str,
        output_filename: Optional[str] = None,
        output_dir: Optional[Path] = None,
        formats: list = ['pdf', 'png'],
        title: str = 'Document',
        **kwargs
    ) -> Dict[str, Path]:
        """
        Convert markdown to multiple formats.
        
        Args:
            markdown_text: Markdown text to convert.
            output_filename: Base output filename (without extension).
            output_dir: Output directory. Defaults to instance output_dir.
            formats: List of formats to convert to. Defaults to ['pdf', 'png'].
            title: Document title.
            **kwargs: Additional arguments for conversion.
            
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
                output_dir,
                title,
                **kwargs
            )
            results['pdf'] = pdf_path
            
        if 'png' in formats:
            png_path = self.convert_to_png(
                markdown_text,
                f'{output_filename}.png',
                output_dir,
                title,
                **kwargs
            )
            results['png'] = png_path
            
        return results
    
    @staticmethod
    def list_themes() -> list:
        """List available themes."""
        return Theme.list_themes()


# Convenience functions
def convert_markdown_to_pdf(
    markdown_text: str,
    output_filename: str = 'output.pdf',
    output_dir: Optional[Path] = None,
    theme: str = 'default'
) -> Path:
    """Convert markdown to PDF with theme."""
    converter = MarkdownConverter(output_dir, theme)
    return converter.convert_to_pdf(markdown_text, output_filename)


def convert_markdown_to_png(
    markdown_text: str,
    output_filename: str = 'output.png',
    output_dir: Optional[Path] = None,
    theme: str = 'default',
    width: int = 1200
) -> Path:
    """Convert markdown to PNG with theme."""
    converter = MarkdownConverter(output_dir, theme)
    return converter.convert_to_png(markdown_text, output_filename, width=width)


def convert_markdown(
    markdown_text: str,
    output_filename: str = 'output',
    output_dir: Optional[Path] = None,
    formats: list = ['pdf', 'png'],
    theme: str = 'default'
) -> Dict[str, Path]:
    """Convert markdown to multiple formats with theme."""
    converter = MarkdownConverter(output_dir, theme)
    return converter.convert(markdown_text, output_filename, output_dir, formats)


if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Convert Markdown to PDF/PNG',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python converter.py input.md
  python converter.py input.md -f pdf -t github
  python converter.py input.md -f png,pdf -o output -t dark
        """
    )
    
    parser.add_argument('input', help='Input markdown file')
    parser.add_argument('-o', '--output', help='Output filename (without extension)')
    parser.add_argument('-f', '--formats', default='pdf,png', help='Output formats (comma-separated: pdf,png)')
    parser.add_argument('-t', '--theme', default='default', help='Theme (default, dark, github, minimal, professional)')
    parser.add_argument('-d', '--output-dir', help='Output directory')
    parser.add_argument('--width', type=int, default=1200, help='PNG width in pixels')
    parser.add_argument('--page-size', default='A4', help='PDF page size')
    parser.add_argument('--margin', default='20mm', help='PDF margin')
    parser.add_argument('--list-themes', action='store_true', help='List available themes')
    
    args = parser.parse_args()
    
    if args.list_themes:
        print("Available themes:")
        for theme in MarkdownConverter.list_themes():
            print(f"  - {theme}")
        exit(0)
    
    input_file = Path(args.input)
    if not input_file.exists():
        print(f"❌ Error: File '{input_file}' not found")
        exit(1)
    
    with open(input_file, 'r', encoding='utf-8') as f:
        markdown_text = f.read()
    
    output_dir = Path(args.output_dir) if args.output_dir else None
    formats = args.formats.split(',')
    
    converter = MarkdownConverter(output_dir, args.theme)
    
    try:
        results = converter.convert(
            markdown_text,
            args.output,
            formats=formats,
            width=args.width,
            page_size=args.page_size,
            margin=args.margin
        )
        
        print("✅ Conversion complete!")
        for format_name, path in results.items():
            print(f"  {format_name.upper()}: {path}")
    except Exception as e:
        print(f"❌ Error during conversion: {e}")
        exit(1)
