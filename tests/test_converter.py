#!/usr/bin/env python3
"""
Test suite for Markdown2PDF Converter
"""

import unittest
import tempfile
from pathlib import Path
from src.converter import MarkdownConverter, convert_markdown, convert_markdown_to_pdf, convert_markdown_to_png


class TestMarkdownConverter(unittest.TestCase):
    """Test cases for MarkdownConverter class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_dir = Path(tempfile.mkdtemp())
        self.converter = MarkdownConverter(self.test_dir)
        self.test_markdown = """
# Test Document

This is a **test** document.

## Features

- Feature 1
- Feature 2
- Feature 3

## Code Example

```python
def hello():
    print("Hello World")
```

## Table

| Column 1 | Column 2 |
|----------|----------|
| Data 1   | Data 2   |
"""
    
    def tearDown(self):
        """Tear down test fixtures."""
        import shutil
        shutil.rmtree(self.test_dir)
    
    def test_markdown_to_html(self):
        """Test markdown to HTML conversion."""
        html = self.converter.markdown_to_html(self.test_markdown)
        self.assertIn('<h1>Test Document</h1>', html)
        self.assertIn('<strong>test</strong>', html)
        self.assertIn('<ul>', html)
    
    def test_convert_to_pdf(self):
        """Test conversion to PDF."""
        pdf_path = self.converter.convert_to_pdf(
            self.test_markdown,
            'test.pdf'
        )
        self.assertTrue(pdf_path.exists())
        self.assertTrue(pdf_path.stat().st_size > 0)
    
    def test_convert_to_png(self):
        """Test conversion to PNG."""
        png_path = self.converter.convert_to_png(
            self.test_markdown,
            'test.png'
        )
        self.assertTrue(png_path.exists())
        self.assertTrue(png_path.stat().st_size > 0)
    
    def test_convert_multiple_formats(self):
        """Test conversion to multiple formats."""
        results = self.converter.convert(
            self.test_markdown,
            'test',
            formats=['pdf', 'png']
        )
        self.assertIn('pdf', results)
        self.assertIn('png', results)
        self.assertTrue(results['pdf'].exists())
        self.assertTrue(results['png'].exists())
    
    def test_custom_output_dir(self):
        """Test custom output directory."""
        custom_dir = self.test_dir / 'custom'
        pdf_path = self.converter.convert_to_pdf(
            self.test_markdown,
            'test.pdf',
            custom_dir
        )
        self.assertTrue(pdf_path.parent == custom_dir)
    
    def test_custom_width(self):
        """Test custom PNG width."""
        png_path = self.converter.convert_to_png(
            self.test_markdown,
            'test.png',
            width=800
        )
        self.assertTrue(png_path.exists())


class TestConvenienceFunctions(unittest.TestCase):
    """Test cases for convenience functions."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_dir = Path(tempfile.mkdtemp())
        self.test_markdown = "# Test\n\nTest content."
    
    def tearDown(self):
        """Tear down test fixtures."""
        import shutil
        shutil.rmtree(self.test_dir)
    
    def test_convert_markdown_to_pdf(self):
        """Test convert_markdown_to_pdf function."""
        pdf_path = convert_markdown_to_pdf(
            self.test_markdown,
            'test.pdf',
            self.test_dir
        )
        self.assertTrue(pdf_path.exists())
    
    def test_convert_markdown_to_png(self):
        """Test convert_markdown_to_png function."""
        png_path = convert_markdown_to_png(
            self.test_markdown,
            'test.png',
            self.test_dir
        )
        self.assertTrue(png_path.exists())
    
    def test_convert_markdown(self):
        """Test convert_markdown function."""
        results = convert_markdown(
            self.test_markdown,
            'test',
            self.test_dir,
            formats=['pdf', 'png']
        )
        self.assertIn('pdf', results)
        self.assertIn('png', results)


if __name__ == '__main__':
    unittest.main()
