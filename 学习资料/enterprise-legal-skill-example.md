# 🏢 Level 3 示例：企业法律合规助手

```yaml
---
name: legal-compliance-us
description: |
  Enterprise legal compliance assistant for US tech companies.
  Triggers when user needs help with:
  - NDA drafting and review
  - Privacy policy generation (GDPR, CCPA compliant)
  - Terms of Service updates
  - Open source license compliance checking
  - Contract risk analysis
  - Employment agreement templates
---

# Legal Compliance Assistant

## Core Capabilities

### 1. NDA Generation
Generate customized NDAs based on:
- Mutual vs. Unilateral
- Jurisdiction (50 states + federal)
- Industry-specific clauses (tech, healthcare, finance)
- Term duration
- Permitted disclosures

**Template Selection:**
```bash
scripts/select_template.py --type nda --mutual true --state CA --industry tech
```

**Output:** Word document with tracked changes enabled, comment boxes for attorney review

---

### 2. Privacy Policy Generator

**Process:**
1. Questionnaire (30 questions about data practices)
2. Compliance matrix generation
3. Policy drafting with jurisdiction-specific sections
4. Cross-reference checker (policy ↔ actual code behavior)

**Data Sources:**
- `references/gdpr-requirements.md` (124 articles)
- `references/ccpa-compliance-checklist.md`
- `references/state-privacy-laws.json` (15 states)

**Example:**
```python
# Analyze codebase for data collection
python scripts/analyze_data_flows.py /path/to/codebase

# Generate policy
python scripts/generate_privacy_policy.py \
  --regions US,EU,CA \
  --industry saas \
  --analysis data_flows.json \
  --output policy.docx
```

---

### 3. Open Source License Compliance

**Capability:** Scan dependencies → Flag conflicts → Suggest alternatives

```python
# Scan project
python scripts/license_scanner.py package.json

# Output:
# ⚠️  GPL-3.0 dependency 'foo' conflicts with MIT project license
# 📋 Recommendations:
#    1. Replace with 'bar' (MIT, similar functionality)
#    2. Dual-license project as MIT/GPL-3.0
#    3. Contact foo maintainers for license exception
```

---

### 4. Contract Risk Analyzer

**Input:** Upload contract PDF
**Output:** Risk report with severity levels

```yaml
High Risk (3 issues):
  - Unlimited liability clause (Section 8.3)
  - Auto-renewal without cap (Section 12.1)
  - Broad IP assignment (Section 6.2)

Medium Risk (5 issues):
  - 90-day payment terms (Section 4.2)
  - Vendor lock-in provisions (Section 10.1)
  ...

Suggested Redlines:
  1. Section 8.3: Cap liability at 12 months of fees
  2. Section 12.1: Add 3-year maximum auto-renewal
  ...
```

---

## Bundled Resources

```
legal-compliance-us/
├── SKILL.md (300 lines)
├── scripts/
│   ├── select_template.py
│   ├── generate_privacy_policy.py
│   ├── analyze_data_flows.py
│   ├── license_scanner.py
│   ├── contract_risk_analyzer.py
│   └── redline_generator.py (6 scripts, ~3000 lines total)
├── references/
│   ├── gdpr-requirements.md (15k words)
│   ├── ccpa-compliance-checklist.md (8k words)
│   ├── state-privacy-laws.json
│   ├── license-compatibility-matrix.md
│   └── contract-risk-patterns.yaml (5 files, ~30k words)
├── assets/
│   ├── templates/
│   │   ├── nda-mutual-tech.docx
│   │   ├── nda-unilateral-tech.docx
│   │   ├── privacy-policy-saas.docx
│   │   └── tos-b2b-saas.docx (47 templates)
│   └── styles/
│       └── legal-document.css
└── LICENSE.txt
```

**Total Size:** ~2.5 MB
**Token Cost (if all loaded):** ~150k tokens
**Actual Cost:** ~5k tokens (SKILL.md only, resources loaded on-demand)

---

## Usage Flow

```
User: "我需要一份面向加州客户的 B2B SaaS 隐私政策"

Claude:
├─ [Level 1] Metadata 匹配 → 触发 legal-compliance-us skill
├─ [Level 2] 加载 SKILL.md → 理解隐私政策生成流程
├─ [Questionnaire] 询问 30 个数据实践问题
├─ [Level 3] 按需加载:
│   ├─ references/ccpa-compliance-checklist.md
│   ├─ assets/templates/privacy-policy-saas.docx
│   └─ 执行 scripts/generate_privacy_policy.py
└─ [Output] 生成 12 页 CCPA 合规的隐私政策文档
```

---

## 能力边界

✅ **能做：**
- 生成标准法律文档（基于模板）
- 识别常见法律风险模式
- 提供合规清单和建议
- 自动化重复性法律工作

❌ **不能做：**
- 替代律师的专业判断
- 处理复杂诉讼策略
- 提供具有法律约束力的意见
- 预测法庭判决结果

---

**价值：** ⭐⭐⭐⭐
- 节省：初级律师 20-40 小时/月
- 成本：$8k-$15k/月 → $0
- 质量：标准化 + 人工审核
