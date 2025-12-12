#!/usr/bin/env python3
"""
简单的 API 测试脚本
"""

import os
import requests

# 配置
API_KEY = "sk-JO438PQ5WpZFtR9Gt5tMN119FmD1bG6YDtmczNgGyDIMCHc1"
BASE_URL = "https://api.bltcy.ai"

def test_generation():
    url = f"{BASE_URL}/v1/images/generations"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "nano-banana-2",
        "prompt": "a cute cat",
        "aspect_ratio": "1:1",
        "response_format": "url",
        "image_size": "4K"
    }

    print(f"正在调用 API: {url}")
    print(f"请求数据: {payload}")

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        print(f"\n状态码: {response.status_code}")
        print(f"响应: {response.text}")

        if response.status_code == 200:
            result = response.json()
            print("\n✅ 成功！")
            if 'data' in result and len(result['data']) > 0:
                print(f"图像 URL: {result['data'][0].get('url', 'N/A')}")
        else:
            print(f"\n❌ 失败: {response.status_code}")

    except Exception as e:
        print(f"\n❌ 错误: {e}")

if __name__ == "__main__":
    test_generation()
