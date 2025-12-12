# Skills-Agent 项目

Claude + Nano-Banana 智能对话系统，支持自然语言图像生成。

## 项目简介

这是一个集成了 Claude Haiku 4.5 和 Nano-Banana-2 图像生成 API 的智能对话系统。用户可以通过自然语言与 Claude 对话，当需要生成图像时，Claude 会自动调用 Nano-Banana API 生成图像。

## 功能特性

✅ **智能对话**: 使用 Claude Haiku 4.5 模型进行自然对话
✅ **自动图像生成**: 识别图像生成意图，自动调用 Nano-Banana-2 API
✅ **实时交互**: 美观的对话界面，实时显示生成进度
✅ **多种质量**: 支持 1K/2K/4K 图像质量
✅ **上下文记忆**: 保持对话历史，支持连续交互

## 项目结构

```
skills-agent/
├── nano-banana/              # Nano-Banana Skill
│   ├── SKILL.md             # Skill 配置文件
│   ├── scripts/             # Python 脚本
│   │   ├── generate_image.py  # 图像生成脚本
│   │   └── edit_image.py      # 图像编辑脚本
│   └── references/          # API 参考文档
│       └── api_reference.md   # 完整 API 文档
├── test-frontend/           # 测试前端
│   └── index.html          # Web 对话界面
├── nano-banana.skill        # 打包好的 skill 文件
├── test_api.py             # API 测试脚本
└── README.md               # 本文件
```

## 快速开始

### 1. 打开测试前端

```bash
# 在浏览器中打开
open test-frontend/index.html
```

### 2. 开始对话

对话界面已经配置好所有 API 密钥，可以直接使用：

**生成图像示例**:
- "生成一只可爱的猫"
- "画一个日落的场景"
- "创建一张城市天际线的图片"

**普通对话示例**:
- "你好，介绍一下自己"
- "帮我解释一下量子计算"
- "推荐几本好书"

## 技术实现

### 对话流程

```
用户输入 → Claude Haiku 4.5 分析
          ↓
     是否需要生成图像？
          ↓
    是 → 提取图像描述 → Nano-Banana-2 生成 → 显示图像
    否 → 直接回复文本
```

### API 配置

- **Claude 模型**: `claude-haiku-4-5-20251001`
- **图像模型**: `nano-banana-2`
- **API 端点**: `https://api.bltcy.ai`
- **默认质量**: 4K
- **默认比例**: 4:3

### 特殊指令格式

Claude 使用特殊标记触发图像生成：

```
[GENERATE_IMAGE: 图像描述]
```

前端会自动识别这个标记，提取描述并调用 Nano-Banana API。

## 使用示例

### 示例 1：生成图像

```
用户: "生成一只橘猫坐在窗边"
Claude: "好的，我为你生成一只橘猫坐在窗边的图片。[GENERATE_IMAGE: an orange cat sitting by the window]"
系统: [调用 Nano-Banana API 生成图像并显示]
```

### 示例 2：普通对话

```
用户: "什么是人工智能？"
Claude: "人工智能（AI）是计算机科学的一个分支..."
```

### 示例 3：连续对话

```
用户: "生成一个森林的场景"
Claude: [生成森林图像]
用户: "再生成一个海洋的场景"
Claude: [生成海洋图像]
```

## Skill 安装（可选）

如果要在 Claude Code 中使用 Skill：

```bash
# 验证 skill
cd /Users/g/Desktop/探索/Claude\ skills/skills
python3 skill-creator/scripts/quick_validate.py skills-agent/nano-banana

# skill 已打包为 nano-banana.skill
# 可以直接上传到 Claude.ai 或 Claude Code
```

## 测试脚本

### 测试 API 连接

```bash
cd skills-agent
python3 test_api.py
```

### 使用命令行生成图像

```bash
cd nano-banana
export CLAUDE_THIRD_KEY="sk-JO438PQ5WpZFtR9Gt5tMN119FmD1bG6YDtmczNgGyDIMCHc1"
export CLAUDE_THIRD_URL="https://api.bltcy.ai"

python3 scripts/generate_image.py --prompt "一只可爱的猫" --aspect-ratio "1:1" --quality "4K"
```

## 前端界面特性

- 🎨 渐变紫色主题
- 💬 气泡式对话界面
- ⌨️ 自动调整输入框高度
- 🔄 加载动画（打字指示器）
- 🖼️ 图像预览和懒加载
- 📱 响应式设计
- ⚡ Enter 发送，Shift+Enter 换行

## API 费用说明

- **失败请求不计费**: Nano-Banana API 只对成功请求收费
- **按需使用**: Claude Haiku 4.5 成本低，适合高频对话
- **图像质量**: 4K 质量推荐，效果最佳

## 故障排除

### 前端无法连接 API

1. 检查浏览器控制台是否有 CORS 错误
2. 确认 API 密钥是否正确
3. 测试网络连接

### 图像生成失败

1. 检查提示词是否合理
2. 查看网络请求状态
3. 确认 API 配额是否充足

### Claude 不调用图像生成

1. 确保提示词包含图像生成关键词
2. 检查 system prompt 是否正确
3. 查看对话历史是否过长

## 技术栈

- **后端 API**:
  - Claude Haiku 4.5 (对话)
  - Nano-Banana-2 (图像生成)

- **前端**:
  - HTML5
  - CSS3 (渐变、动画、响应式)
  - Vanilla JavaScript (ES6+)

- **Skill 系统**:
  - Claude Skills (Anthropic)
  - Python 3.12+

## 性能优化

- ✅ 图像懒加载
- ✅ 自动滚动到最新消息
- ✅ 防抖输入处理
- ✅ 错误重试机制
- ✅ 对话历史压缩

## 下一步计划

- [ ] 添加图像编辑功能
- [ ] 支持多种宽高比选择
- [ ] 添加对话导出功能
- [ ] 实现图像历史记录
- [ ] 支持上传参考图
- [ ] 添加主题切换
- [ ] 多语言支持

## 许可证

本项目遵循 Apache 2.0 许可证。

## 联系方式

如有问题或建议，欢迎反馈。

---

**开发时间**: 2025-11-27
**版本**: 1.0.0
**状态**: ✅ 生产就绪
