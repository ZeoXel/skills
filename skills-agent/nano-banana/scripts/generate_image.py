#!/usr/bin/env python3
"""
Image Generation Script for Nano-Banana API

Generates images from text prompts using the nano-banana-2 API.
"""

import argparse
import json
import os
import sys
import requests


def generate_image(
    prompt: str,
    aspect_ratio: str = "4:3",
    quality: str = "4K",
    model: str = "nano-banana-2",
    api_key: str = None,
    base_url: str = None
):
    """
    Generate an image using nano-banana API.

    Args:
        prompt: Text description of the image to generate
        aspect_ratio: Image aspect ratio (1:1, 4:3, 16:9, etc.)
        quality: Image quality (1K, 2K, 4K)
        model: Model to use (nano-banana, nano-banana-2, nano-banana-hd)
        api_key: API key (defaults to CLAUDE_THIRD_KEY env var)
        base_url: API base URL (defaults to CLAUDE_THIRD_URL env var)

    Returns:
        dict: Response containing image URL and metadata
    """
    # Get API credentials from env if not provided
    if api_key is None:
        api_key = os.environ.get("CLAUDE_THIRD_KEY")
    if base_url is None:
        base_url = os.environ.get("CLAUDE_THIRD_URL", "https://api.bltcy.ai")

    if not api_key:
        raise ValueError("API key not provided. Set CLAUDE_THIRD_KEY environment variable or pass --api-key")

    # Construct API endpoint
    url = f"{base_url.rstrip('/')}/v1/images/generations"

    # Prepare request headers
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Prepare request body
    payload = {
        "model": model,
        "prompt": prompt,
        "aspect_ratio": aspect_ratio,
        "response_format": "url"
    }

    # Add quality parameter for nano-banana-2
    if model == "nano-banana-2":
        payload["image_size"] = quality

    try:
        # Make API request
        response = requests.post(url, headers=headers, json=payload, timeout=60)
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


def main():
    parser = argparse.ArgumentParser(description="Generate images using nano-banana API")
    parser.add_argument("--prompt", required=True, help="Text description of the image")
    parser.add_argument("--aspect-ratio", default="4:3",
                       choices=["1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"],
                       help="Image aspect ratio (default: 4:3)")
    parser.add_argument("--quality", default="4K", choices=["1K", "2K", "4K"],
                       help="Image quality (default: 4K)")
    parser.add_argument("--model", default="nano-banana-2",
                       choices=["nano-banana", "nano-banana-2", "nano-banana-hd"],
                       help="Model to use (default: nano-banana-2)")
    parser.add_argument("--api-key", help="API key (uses CLAUDE_THIRD_KEY env var by default)")
    parser.add_argument("--base-url", help="API base URL (uses CLAUDE_THIRD_URL env var by default)")

    args = parser.parse_args()

    # Generate image
    result = generate_image(
        prompt=args.prompt,
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
