# Nano-Banana API Reference

Complete API documentation for nano-banana image generation and editing.

## API Endpoints

### 1. Image Generation - `/v1/images/generations`

Generate new images from text prompts.

**Endpoint:** `POST /v1/images/generations`

**Headers:**
```
Authorization: Bearer {YOUR_API_KEY}
Content-Type: application/json
```

**Request Body:**
```json
{
  "model": "nano-banana-2",
  "prompt": "a beautiful sunset over mountains",
  "aspect_ratio": "16:9",
  "response_format": "url",
  "image_size": "4K"
}
```

**Parameters:**

| Parameter | Type | Required | Description | Values |
|-----------|------|----------|-------------|--------|
| `model` | string | Yes | Model to use | `nano-banana`, `nano-banana-2`, `nano-banana-hd` |
| `prompt` | string | Yes | Text description of image | Any text |
| `aspect_ratio` | string | No | Image aspect ratio | `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9` |
| `response_format` | string | No | Response format | `url` (recommended), `b64_json` |
| `image_size` | string | No | Quality level (nano-banana-2 only) | `1K`, `2K`, `4K` |
| `image` | array | No | Reference images (URLs or base64) | Array of image URLs or base64 strings |

**Response:**
```json
{
  "created": 1234567890,
  "data": [
    {
      "url": "https://example.com/generated-image.png"
    }
  ]
}
```

---

### 2. Image Editing - `/v1/images/edits`

Edit existing images based on text instructions.

**Endpoint:** `POST /v1/images/edits`

**Headers:**
```
Authorization: Bearer {YOUR_API_KEY}
```

**Request Body (multipart/form-data):**

| Field | Type | Required | Description | Values |
|-------|------|----------|-------------|--------|
| `model` | string | Yes | Model to use | `nano-banana`, `nano-banana-2`, `nano-banana-hd` |
| `prompt` | string | Yes | Text editing instructions | Any text |
| `image` | file/string | Yes | Source image file or URL | Image file or URL |
| `aspect_ratio` | string | No | Output aspect ratio | `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9` |
| `response_format` | string | No | Response format | `url` (recommended), `b64_json` |
| `image_size` | string | No | Quality level (nano-banana-2 only) | `1K`, `2K`, `4K` |

**Response:**
```json
{
  "created": 1234567890,
  "data": [
    {
      "url": "https://example.com/edited-image.png"
    }
  ]
}
```

---

## Models

### nano-banana
Standard quality image generation based on Gemini 2.5 Flash Image Preview.

### nano-banana-2 (Recommended)
Enhanced version with support for quality levels (1K, 2K, 4K) and improved optimization.

### nano-banana-hd
High-definition 4K quality output.

---

## Aspect Ratios

| Ratio | Description | Common Use Cases |
|-------|-------------|------------------|
| `1:1` | Square | Social media posts, avatars, icons |
| `4:3` | Standard landscape | Default photos, presentations |
| `3:4` | Standard portrait | Portrait photos, mobile screens |
| `16:9` | Widescreen | Video thumbnails, banners, desktop wallpapers |
| `9:16` | Vertical video | Mobile stories, TikTok, Instagram Reels |
| `2:3` | Portrait photo | Standard portrait photography |
| `3:2` | Landscape photo | Standard landscape photography |
| `4:5` | Portrait social | Instagram portrait posts |
| `5:4` | Landscape social | Social media landscape posts |
| `21:9` | Ultrawide | Cinematic, panoramic views |

---

## Quality Levels (nano-banana-2 only)

- **1K** - Low quality, faster generation
- **2K** - Medium quality, balanced speed
- **4K** - High quality, best results (recommended)

---

## Error Handling

**Failed requests do not consume API credits.**

Common error responses:

```json
{
  "error": {
    "message": "Invalid aspect ratio",
    "type": "invalid_request_error",
    "code": "invalid_parameter"
  }
}
```

---

## Best Practices

1. **Use nano-banana-2** - Recommended for best quality and features
2. **Set quality to 4K** - Unless speed is critical
3. **Choose appropriate aspect ratios** - Match the content type
4. **Use URL format** - More efficient than base64
5. **Provide clear prompts** - Detailed descriptions yield better results
6. **Reference images** - Use for style consistency

---

## Differences from Gemini 2.5 Flash Image Preview

- **Returns URLs instead of base64** - More efficient
- **DALL-E compatible format** - Easy migration from OpenAI
- **Aspect ratio support** - Flexible output sizes
- **Optimized for image generation** - Better prompts handling
- **Failed requests don't charge** - Cost-effective
