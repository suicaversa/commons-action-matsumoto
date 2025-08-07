# OGP Thumbnail Setup

This document explains how to set up the horizontal thumbnail image for the top page.

## Current Status

- The HTML file (`index.html`) already has proper OGP meta tags configured
- It expects an image at `assets/ogp-image.png` with dimensions 1200x630 pixels
- A vertical logo image has been provided that needs to be converted to horizontal format

## Files Created

1. `create_ogp_image.py` - Python script to convert the vertical image to horizontal format
2. `generate_thumbnail.html` - HTML preview of how the thumbnail should look
3. `assets/ogp-image.svg` - SVG version of the horizontal thumbnail

## How to Create the Horizontal Thumbnail

### Option 1: Use Python Script (Recommended)
```bash
python3 create_ogp_image.py
```

This will create `assets/ogp-image.png` with the proper 1200x630 dimensions.

### Option 2: Manual Creation
1. Open `generate_thumbnail.html` in a browser
2. Take a screenshot of the thumbnail area (1200x630 pixels)
3. Save it as `assets/ogp-image.png`

### Option 3: Use Browser Console
1. Open `generate_thumbnail.html` in a browser
2. Open browser console (F12)
3. Run: `generateThumbnail()`
4. This will download the PNG file
5. Move the downloaded file to `assets/ogp-image.png`

## Design Specifications

- Dimensions: 1200x630 pixels (OGP standard)
- Background: Light gray (#f8f9fa)
- Yellow circle: #e6ff33, centered
- Text: Bold black Arial, centered
- Layout: "COMMONS" above, "ACTION" in center (overlapping circle), "MATSUMOTO." below

## Current OGP Configuration

The following meta tags are already configured in `index.html`:

```html
<meta property="og:image" content="https://commons-action-matsumoto.jp/assets/ogp-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:image" content="https://commons-action-matsumoto.jp/assets/ogp-image.png">
```

Once the PNG file is created and placed in the `assets/` folder, the thumbnail will automatically appear when the site is shared on social media platforms.