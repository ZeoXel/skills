---
name: nano-banana
description: AI image generation and editing using nano-banana-2 API. Use this skill when users request to generate images from text prompts, edit existing images, or create visual content. Supports various aspect ratios (1:1, 4:3, 16:9, etc.) and quality levels (1K, 2K, 4K). Use for requests like "generate an image of...", "create a picture of...", "edit this image to...", or any visual content creation tasks.
---

# Nano-Banana Image Generation & Editing

This skill enables AI-powered image generation and editing using the nano-banana-2 API, which is optimized for image generation based on Gemini 2.5 Flash Image Preview.

## Overview

Nano-banana provides two main capabilities:
1. **Image Generation** - Create images from text prompts
2. **Image Editing** - Modify existing images based on text instructions

## Key Features

- Support for multiple aspect ratios (1:1, 4:3, 3:4, 16:9, 9:16, 2:3, 3:2, 4:5, 5:4, 21:9)
- Quality options: 1K, 2K, 4K (nano-banana-2 only)
- Returns image URLs (not base64)
- Failed requests don't incur charges
- Supports reference images for guided generation

## Quick Start

### Generate an Image

Use the generation script for creating new images:

```bash
python scripts/generate_image.py --prompt "a beautiful sunset over mountains" --aspect-ratio "16:9" --quality "4K"
```

### Edit an Image

Use the edit script for modifying existing images:

```bash
python scripts/edit_image.py --prompt "add a rainbow to the sky" --image "/path/to/image.jpg" --aspect-ratio "16:9"
```

## Workflow

### When to Use Image Generation vs Editing

**Use Generation (`/v1/images/generations`)** when:
- Creating new images from scratch
- User provides only text description
- No reference image is provided

**Use Editing (`/v1/images/edits`)** when:
- Modifying existing images
- User provides an image to edit
- User wants to add/remove/change elements in an image

## Usage Guidelines

### 1. Image Generation Workflow

1. Parse user's image description
2. Determine appropriate aspect ratio (default: 4:3)
3. Set quality level (default: 4K for nano-banana-2)
4. Call the generation script with parameters
5. Return the generated image URL to user

### 2. Image Editing Workflow

1. Identify the source image from user input
2. Parse the editing instructions
3. Determine output aspect ratio
4. Call the edit script with image and prompt
5. Return the edited image URL to user

### 3. Aspect Ratio Selection

Choose based on content type:
- **1:1** - Square images (social media posts, avatars)
- **4:3 / 3:4** - Standard photos (default)
- **16:9 / 9:16** - Widescreen/mobile (videos, banners)
- **2:3 / 3:2** - Portrait/landscape photography
- **21:9** - Ultrawide cinematic

## Scripts

### scripts/generate_image.py

Generates images from text prompts using the nano-banana API.

**Parameters:**
- `--prompt` (required) - Text description of the image
- `--aspect-ratio` (optional) - Image aspect ratio (default: 4:3)
- `--quality` (optional) - Image quality: 1K, 2K, or 4K (default: 4K)
- `--model` (optional) - Model to use (default: nano-banana-2)
- `--api-key` (optional) - API key (uses CLAUDE_THIRD_KEY env var by default)
- `--base-url` (optional) - API base URL (uses CLAUDE_THIRD_URL env var by default)

**Returns:** JSON with image URL

### scripts/edit_image.py

Edits existing images based on text instructions.

**Parameters:**
- `--prompt` (required) - Text instructions for editing
- `--image` (required) - Path or URL to the source image
- `--aspect-ratio` (optional) - Output aspect ratio (default: 4:3)
- `--quality` (optional) - Image quality: 1K, 2K, or 4K (default: 4K)
- `--model` (optional) - Model to use (default: nano-banana-2)
- `--api-key` (optional) - API key (uses CLAUDE_THIRD_KEY env var by default)
- `--base-url` (optional) - API base URL (uses CLAUDE_THIRD_URL env var by default)

**Returns:** JSON with edited image URL

## Reference Documentation

For detailed API specifications and parameters, see:
- [API Reference](references/api_reference.md) - Complete nano-banana API documentation

## Error Handling

- If generation fails, the script will return an error message
- Failed requests don't consume API credits
- Check that API key and base URL are properly configured
- Verify image file paths are valid for editing operations

## Examples

**Example 1: Simple Generation**
```
User: "Generate an image of a cat sitting on a window"
→ Run: scripts/generate_image.py --prompt "a cat sitting on a window" --aspect-ratio "4:3" --quality "4K"
```

**Example 2: Widescreen Generation**
```
User: "Create a panoramic view of a city skyline at night"
→ Run: scripts/generate_image.py --prompt "panoramic city skyline at night" --aspect-ratio "21:9" --quality "4K"
```

**Example 3: Image Editing**
```
User: "Edit this image to add snow falling"
→ Run: scripts/edit_image.py --prompt "add falling snow" --image "/path/to/image.jpg" --aspect-ratio "16:9"
```
