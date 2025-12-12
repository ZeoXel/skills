#!/usr/bin/env python3
"""
Image Editing Script for Nano-Banana API

Edits existing images based on text instructions using the nano-banana API.
"""

import argparse
import json
import os
import sys
import requests
from pathlib import Path


def edit_image(
    prompt: str,
    image_path: str,
    aspect_ratio: str = "4:3",
    quality: str = "4K",
    model: str = "nano-banana-2",
    api_key: str = None,
    base_url: str = None
):
    """
    Edit an image using nano-banana API.

    Args:
        prompt: Text instructions for editing the image
        image_path: Path or URL to the source image
        aspect_ratio: Output image aspect ratio (1:1, 4:3, 16:9, etc.)
        quality: Image quality (1K, 2K, 4K)
        model: Model to use (nano-banana, nano-banana-2, nano-banana-hd)
        api_key: API key (defaults to CLAUDE_THIRD_KEY env var)
        base_url: API base URL (defaults to CLAUDE_THIRD_URL env var)

    Returns:
        dict: Response containing edited image URL and metadata
    """
    # Get API credentials from env if not provided
    if api_key is None:
        api_key = os.environ.get("CLAUDE_THIRD_KEY")
    if base_url is None:
        base_url = os.environ.get("CLAUDE_THIRD_URL", "https://api.bltcy.ai")

    if not api_key:
        raise ValueError("API key not provided. Set CLAUDE_THIRD_KEY environment variable or pass --api-key")

    # Construct API endpoint
    url = f"{base_url.rstrip('/')}/v1/images/edits"

    # Prepare request headers
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    # Prepare multipart form data
    files = {}
    data = {
        "model": model,
        "prompt": prompt,
        "aspect_ratio": aspect_ratio,
        "response_format": "url"
    }

    # Add quality parameter for nano-banana-2
    if model == "nano-banana-2":
        data["image_size"] = quality

    # Handle image input (file path or URL)
    if image_path.startswith(('http://', 'https://')):
        # If it's a URL, pass it as a string parameter
        data["image"] = image_path
    else:
        # If it's a local file, upload it
        image_file = Path(image_path)
        if not image_file.exists():
            return {
                "success": False,
                "error": f"Image file not found: {image_path}"
            }

        # Open and add file to multipart form
        files["image"] = (image_file.name, open(image_file, "rb"), "image/png")

    try:
        # Make API request
        if files:
            response = requests.post(url, headers=headers, data=data, files=files, timeout=60)
        else:
            response = requests.post(url, headers=headers, data=data, timeout=60)

        response.raise_for_status()

        result = response.json()
        return {
            "success": True,
            "data": result
        }

    except requests.exceptions.RequestException as e:
        return {
            "success": False,
            "error": str(e),
            "details": getattr(e.response, 'text', None) if hasattr(e, 'response') else None
        }
    finally:
        # Close any open file handles
        for file in files.values():
            if hasattr(file[1], 'close'):
                file[1].close()


def main():
    parser = argparse.ArgumentParser(description="Edit images using nano-banana API")
    parser.add_argument("--prompt", required=True, help="Text instructions for editing")
    parser.add_argument("--image", required=True, help="Path or URL to the source image")
    parser.add_argument("--aspect-ratio", default="4:3",
                       choices=["1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"],
                       help="Output aspect ratio (default: 4:3)")
    parser.add_argument("--quality", default="4K", choices=["1K", "2K", "4K"],
                       help="Image quality (default: 4K)")
    parser.add_argument("--model", default="nano-banana-2",
                       choices=["nano-banana", "nano-banana-2", "nano-banana-hd"],
                       help="Model to use (default: nano-banana-2)")
    parser.add_argument("--api-key", help="API key (uses CLAUDE_THIRD_KEY env var by default)")
    parser.add_argument("--base-url", help="API base URL (uses CLAUDE_THIRD_URL env var by default)")

    args = parser.parse_args()

    # Edit image
    result = edit_image(
        prompt=args.prompt,
        image_path=args.image,
        aspect_ratio=args.aspect_ratio,
        quality=args.quality,
        model=args.model,
        api_key=args.api_key,
        base_url=args.base_url
    )

    # Output result as JSON
    print(json.dumps(result, indent=2, ensure_ascii=False))

    # Exit with appropriate code
    sys.exit(0 if result["success"] else 1)


if __name__ == "__main__":
    main()
