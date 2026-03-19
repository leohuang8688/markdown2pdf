# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.0] - 2026-03-19

### ✨ Added

#### Contact Update
- **Updated Contact Email** - Changed to claw@pocketai.sg
- **Report Footer Template** - Created report_footer_template.md for consistent footers
- **Stock Analysis Reports** - Added 18+ professional stock analysis report templates

#### Report Improvements
- **News and Catalysts Integration** - Added news and catalysts section to reports
- **Professional Templates** - Enhanced report generation workflow
- **Real-time Data** - Integrated Tavily Search for real-time stock data

### 📝 Reports Included

1. **阿里巴巴-W (09988.HK)** - Professional investment report
2. **MINIMAX-W (00100.HK)** - Updated report with price drop analysis
3. **山东墨龙 (00568.HK)** - Full report with news and catalysts
4. **极智嘉-W (02590.HK)** - Professional report
5. **恒生科技指数 (HSTECH)** - Colored emoji version
6. **三花智控 (002050)** - Real data version
7. **Rocket Lab (RKLB.US)** - Professional report
8. And more...

### 🔧 Technical Changes

- Updated all report templates with new contact email
- Created unified report footer template
- Improved report generation workflow
- Enhanced news and catalysts integration

---

## [2.0.0] - 2026-03-18

### ✨ Added

#### Core Features
- **WeasyPrint PDF Engine** - Modern, stable PDF rendering
- **Native Emoji Support** - No more text replacement!
- **Noto Color Emoji Font** - Google's official colored emoji font
- **Better CSS3 Support** - Richer styling options
- **Higher Quality PDF** - Improved rendering quality

#### Technical Features
- WeasyPrint as primary PDF engine
- Fallback to pdfkit if WeasyPrint unavailable
- Updated all themes with emoji font support
- Added emoji CSS styles
- Improved font configuration

### 🔧 Technical Details

#### PDF Engine
- **WeasyPrint** - Primary engine (v68.1+)
- **pdfkit** - Fallback engine
- **Auto-detection** - Automatically uses WeasyPrint if available

#### Font Configuration
```css
font-family: "Noto Color Emoji", "Apple Color Emoji", 
             "Segoe UI Emoji", "Helvetica Neue", Arial, sans-serif
```

#### Emoji Rendering
- Native emoji support (no replacement)
- Colored emoji via Noto Color Emoji font
- Cross-platform compatibility

### 📦 Dependencies

- **weasyprint>=68.1** (new)
- **Noto Color Emoji font** (system)

---

## [1.0.0] - 2026-03-16

### ✨ Added

#### Core Features
- **Markdown to PDF Converter** - Professional PDF document generation
- **Markdown to PNG Converter** - High-quality PNG image generation
- **5 Professional Themes** - default, dark, github, minimal, professional
- **Colored Emoji Support** - Automatic emoji to colored text label conversion
- **Custom CSS Support** - Complete style control
- **CLI Interface** - Command-line tool for easy usage
- **Python API** - Programmatic access for integration
- **OpenClaw Integration** - Seamless integration with OpenClaw

#### Technical Features
- Multiple Markdown extensions support (extra, codehilite, toc, tables, fenced_code)
- High-quality PDF output with customizable page size and margins
- Configurable PNG resolution (default 1200px width)
- Batch conversion support
- Comprehensive test suite

#### Documentation
- Complete README with usage examples
- API documentation with code samples
- CLI help and examples
- Use case demonstrations
- Installation guide

### 🔧 Technical Details

#### Emoji Color System
- 🟢 Green - Positive, growth, success
- 🔴 Red - Negative, decline, warning
- 🔵 Blue - Neutral, information, data
- 🟡 Gold - Important, highlights, money
- 🟠 Orange - Attention, caution

#### Theme System
- **default** - Modern clean design
- **dark** - Dark theme for presentations
- **github** - GitHub-style rendering
- **minimal** - Minimalist serif design
- **professional** - Business-ready design

### 📦 Dependencies

- **markdown>=3.5.0**
- **pdfkit>=1.0.0**
- **imgkit>=1.2.3**
- **wkhtmltopdf>=0.2.0**

---

## [Unreleased]

### Planned Features
- [ ] More theme templates
- [ ] Batch processing mode
- [ ] Web interface
- [ ] Cloud storage integration
- [ ] More emoji color options
- [ ] Custom theme creation tool

---

**Version:** 2.1.0  
**Release Date:** 2026-03-19  
**Author:** PocketAI 🧤  
**Contact:** claw@pocketai.sg  
**License:** MIT
