# 🎯 Skills 能力速查表

## 快速对比矩阵

| 维度 | Level 0 | Level 1 | Level 2 | Level 3 | Level 4 | Level 5 |
|------|---------|---------|---------|---------|---------|---------|
| **行数** | 6 | ~50 | ~150 | ~300 | ~800 | 3000+ |
| **Scripts** | 无 | 无 | ✓ | ✓✓ | ✓✓✓ | ✓✓✓✓ |
| **References** | 无 | 无 | 可选 | ✓ | ✓✓ | ✓✓✓✓ |
| **上下文占用** | <0.1% | 0.3% | 1-5% | 3-20% | 10-60% | 50%+ |
| **开发时间** | 5分钟 | 30分钟 | 4小时 | 2天 | 2周 | 2个月 |
| **维护成本** | 无 | 极低 | 低 | 中 | 高 | 极高 |
| **价值** | ⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 🤯 |
| **现实性** | 100% | 100% | 100% | 95% | 80% | 20% |
| **推荐度** | 练习 | 入门 | ✅推荐 | ✅推荐 | 谨慎 | ❌不推荐 |

---

## 典型示例

### Level 0: hello-world
```yaml
---
name: hello-world
description: Say hello enthusiastically
---
Always greet with 3 emojis! 🎉🚀✨
```
**用途：** 改变语气  
**场景：** 几乎无实际价值

---

### Level 1: 品牌规范 (73行)
```yaml
---
name: brand-guidelines
description: Company brand and communication standards
---
# Brand Voice
- Professional but warm
- Use "we" not "I"
- Active voice preferred

# Color Palette
Primary: #0066CC
Secondary: #FF6B35
...
```
**用途：** 标准化输出  
**场景：** 品牌一致性、邮件风格

---

### Level 2: PDF 工具包 (~150行)
```
pdf-toolkit/
├── SKILL.md (150 lines)
└── scripts/
    ├── rotate_pdf.py
    ├── merge_pdfs.py
    └── compress_pdf.py
```
**用途：** 专业工具操作  
**场景：** 文档处理、格式转换

---

### Level 3: 法律合规 (~300行)
```
legal-compliance/
├── SKILL.md (300 lines)
├── scripts/ (5 scripts)
│   ├── generate_nda.py
│   └── analyze_contract.py
└── references/ (30k words)
    ├── gdpr-requirements.md
    └── contract-templates/
```
**用途：** 领域专家系统  
**场景：** 法律文档、合规检查

---

### Level 4: 产品生命周期 (~800行)
```
product-lifecycle/
├── SKILL.md (800 lines)
├── scripts/ (14 scripts, 15k lines)
└── references/ (200k words)
```
**用途：** 完整工作流管理  
**场景：** 产品开发端到端

---

### Level 5: 公司操作系统 (3000行)
```
startup-os/
├── SKILL.md (3000 lines)
├── 9 个子系统/
│   ├── 150+ scripts
│   └── 1000+ references
└── [理论演示，不推荐实践]
```
**用途：** 理论极限展示  
**场景：** 不应该实际使用

---

## 🎯 选择指南

### 你的需求 → 推荐 Level

| 需求 | 推荐 |
|------|------|
| "让 Claude 更友好" | Level 0-1 |
| "自动生成品牌一致的邮件" | Level 1 |
| "批量处理 PDF/Word 文档" | Level 2 |
| "生成法律合同" | Level 3 |
| "管理整个产品开发流程" | Level 4 |
| "让 AI 运营整个公司" | ❌ 拆分成多个 L2-L3 |

---

## 💰 投资回报率 (ROI)

```
ROI = (时间节省 × 单价) / 开发维护成本

Level 1:
开发: 30分钟 → 节省: 1小时/周 → ROI: 回报周期 1个月
示例: 邮件模板 (减少改稿时间)

Level 2:
开发: 4小时 → 节省: 5小时/周 → ROI: 回报周期 1周
示例: PDF 批处理 (每周处理 50+ 文档)

Level 3:
开发: 2天 → 节省: 20小时/周 → ROI: 回报周期 2周
示例: 法律文档生成 (替代初级律师工作)

Level 4:
开发: 2周 → 节省: 100小时/月 → ROI: 回报周期 1个月
示例: 产品管理流程 (节省 PM + 工程协调时间)

Level 5:
开发: 2个月 → 维护: 持续 → ROI: ❓ 可能为负
风险: 过度复杂、难以维护、技术债
```

**最佳投资回报区间：Level 2-3**

---

## 🚀 从 0 到 1 的实践路径

### Week 1: 理解概念
- [ ] 阅读官方 skills 仓库
- [ ] 研究 3-5 个示例 skill
- [ ] 理解 SKILL.md 的结构
- [ ] 了解三层加载机制

### Week 2: 第一个 Skill (Level 1)
- [ ] 选择熟悉的领域（如邮件、文档）
- [ ] 使用 init_skill.py 初始化
- [ ] 编写 50 行的 SKILL.md
- [ ] 测试和迭代

### Week 3: 升级到 Level 2
- [ ] 识别可自动化的任务
- [ ] 添加 scripts/ 目录
- [ ] 编写 Python/Bash 脚本
- [ ] 在 SKILL.md 中引用脚本

### Week 4: 进阶到 Level 3
- [ ] 整理领域知识文档
- [ ] 创建 references/ 目录
- [ ] 设计按需加载策略
- [ ] 优化 SKILL.md（保持简洁）

### Month 2+: 考虑 Level 4
- [ ] 评估是否真的需要
- [ ] 设计完整架构
- [ ] 分模块开发
- [ ] 持续维护和优化

---

## ⚠️ 常见陷阱

### 1. 过度工程
❌ "我要做一个能处理所有事情的 skill！"  
✅ "我要做 3 个专注的 skills，各自做好一件事"

### 2. 忽略上下文成本
❌ 把所有知识都放在 SKILL.md 里  
✅ 核心指令在 SKILL.md，详细文档在 references/

### 3. 忽略维护
❌ 写完就不管了  
✅ Skills 也是代码，需要更新和维护

### 4. 不测试就分发
❌ 直接打包发给用户  
✅ 先用 quick_validate.py 验证，充分测试

---

## 🎓 毕业标准

**你已经掌握 Skills 当你能够：**
- [ ] 独立创建一个 Level 2 skill
- [ ] 理解何时用 scripts vs references
- [ ] 知道如何优化上下文占用
- [ ] 能判断一个想法适合哪个 Level
- [ ] 理解"简洁优于复杂"的原则

**进阶目标：**
- [ ] 创建过 Level 3 的领域专家 skill
- [ ] 为团队维护 5+ 个生产 skills
- [ ] 能设计跨 skill 的协作机制
- [ ] 理解何时不应该用 skill（直接提示词更好）

---

## 📚 推荐学习路径

```
1. 阅读官方规范
   └─> agent_skills_spec.md

2. 研究最简单的示例
   └─> template-skill (6 行)

3. 研究实用的示例
   ├─> brand-guidelines (73 行)
   ├─> canvas-design (129 行)
   └─> mcp-builder (236 行)

4. 研究复杂的示例
   ├─> skill-creator (356 行)
   └─> algorithmic-art (404 行)

5. 研究文档 skills (source-available)
   ├─> docx/
   ├─> pdf/
   ├─> pptx/
   └─> xlsx/

6. 动手实践
   └─> 从你自己的需求开始
```

---

## 🎯 最终建议

**记住这个黄金公式：**

```
Skill 价值 = (重复频率 × 复杂度 × 标准化程度) / 维护成本

高价值 Skill 特征：
✓ 每周使用 > 5 次
✓ 手动做需要 > 30 分钟
✓ 有明确的对错标准
✓ 可以用代码/规则表达
✓ 不需要频繁更新

低价值 Skill 特征：
✗ 偶尔用一次
✗ 每次情况都不同
✗ 依赖人类创造力
✗ 规则经常变化
```

**开始行动：**
现在就从一个简单的 Level 1 skill 开始！
选择一个你每天都会做的重复性任务，
用 50 行 SKILL.md 把它标准化。

祝你创建出有价值的 Skills! 🚀
