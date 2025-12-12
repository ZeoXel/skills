# 🚀 Level 4：完整产品开发生命周期系统

```yaml
---
name: product-lifecycle-manager
description: |
  Complete product development lifecycle management for tech companies.
  Handles the entire flow from idea to production:
  - PRD creation from stakeholder interviews
  - Technical design doc generation
  - Task breakdown with JIRA integration
  - Code implementation guidance
  - QA test case generation
  - Go-to-market material creation
  - Post-launch analytics dashboards

  Triggers when user mentions: product planning, feature development,
  launch preparation, or any phase of product lifecycle.
---

# 🎯 Product Lifecycle Manager

## 完整能力矩阵

### Phase 1: Discovery & Planning (Week 1-2)

**输入：** "我们想为 SaaS 产品添加 SSO 功能"

**自动化流程：**

```python
# 1. 利益相关者访谈模板生成
python scripts/generate_stakeholder_questions.py \
  --feature "SSO" \
  --stakeholders "CEO,CTO,销售VP,客户成功总监,5个企业客户"

# 输出：
# - 15 个问题给 CEO（商业价值、定价策略）
# - 12 个问题给 CTO（技术债务、安全风险）
# - 8 个问题给销售（客户需求紧急度、竞品对比）
# - 客户访谈指南（20 个问题）

# 2. 访谈记录分析
python scripts/analyze_interviews.py \
  --transcripts interviews/*.txt \
  --output analysis.json

# AI 提取：
# - 关键需求（按优先级）
# - 痛点频次统计
# - 愿付价格范围
# - 时间敏感度

# 3. PRD 生成
python scripts/generate_prd.py \
  --analysis analysis.json \
  --template enterprise-feature \
  --output PRD_SSO.md
```

**生成的 PRD 包含：**
- Executive Summary（自动生成 ROI 预测）
- User Stories（从访谈中提取）
- Success Metrics（基于行业基准）
- Technical Requirements（从现有架构分析）
- Security & Compliance（SAML 2.0, OAuth 2.0 标准）
- Rollout Plan（分阶段发布策略）
- Risk Matrix（自动识别 15+ 风险点）

---

### Phase 2: Technical Design (Week 3)

```python
# 4. 架构分析
python scripts/analyze_codebase.py \
  --repo /path/to/repo \
  --feature "SSO" \
  --output arch_analysis.json

# 分析内容：
# - 现有认证流程（代码路径追踪）
# - 数据库 schema 变更需求
# - API 端点设计建议
# - 第三方依赖评估（SAML 库对比）
# - 向后兼容性影响

# 5. 技术设计文档生成
python scripts/generate_tech_design.py \
  --prd PRD_SSO.md \
  --arch arch_analysis.json \
  --output TECH_DESIGN_SSO.md
```

**生成的技术设计包含：**
- System Architecture Diagrams（Mermaid 格式）
- Database Schema Changes（带迁移脚本）
- API Contract Specifications（OpenAPI 3.0）
- Security Threat Model（STRIDE 分析）
- Performance Benchmarks（预期 QPS、延迟）
- Monitoring & Alerting Setup

---

### Phase 3: Implementation Planning (Week 4)

```python
# 6. 任务拆解（智能依赖分析）
python scripts/break_down_tasks.py \
  --design TECH_DESIGN_SSO.md \
  --team team_config.yaml \
  --output tasks.json

# 输出 45 个任务：
# Backend (18 tasks):
#   ├─ [BE-1] SAML 库集成 (3 SP, 前置：无)
#   ├─ [BE-2] SSO 配置表设计 (2 SP, 前置：无)
#   ├─ [BE-3] SAML 请求处理 endpoint (5 SP, 前置：BE-1, BE-2)
#   └─ ...
# Frontend (12 tasks):
#   ├─ [FE-1] SSO 登录按钮 UI (1 SP, 前置：设计稿)
#   └─ ...
# DevOps (8 tasks):
# QA (7 tasks):

# 7. JIRA 自动创建（可选）
python scripts/sync_to_jira.py \
  --tasks tasks.json \
  --project PROD \
  --epic "SSO Implementation"

# 创建：
# - 1 个 Epic
# - 45 个 Story/Task（带依赖关系链接）
# - 自动分配给合适的工程师（基于技能矩阵）
# - Sprint 建议（3 个 sprint，每个 2 周）
```

---

### Phase 4: Implementation Guidance (Week 5-10)

**实时支持：**

```yaml
# 工程师问：
User: "如何实现 SAML Response 的签名验证？"

Claude (skill-powered):
├─ 读取 references/saml-implementation-guide.md
├─ 检索项目中已有的签名验证代码模式
├─ 生成代码：
│   ```python
│   from signxml import XMLVerifier
│
│   def verify_saml_response(saml_response_xml, idp_cert):
│       # 基于你们项目的错误处理模式
│       try:
│           verifier = XMLVerifier()
│           verified = verifier.verify(
│               saml_response_xml,
│               x509_cert=idp_cert,
│               # 项目标准：启用时间戳检查
│               validate_schema=True
│           )
│           # 项目标准：结构化日志
│           logger.info("saml.signature.verified",
│                      user_id=extract_user_id(verified))
│           return verified
│       except SignatureError as e:
│           # 项目标准：安全日志 + 告警
│           security_logger.error("saml.signature.invalid",
│                                error=str(e))
│           raise AuthenticationError("Invalid SAML signature")
│   ```
└─ 附加：单元测试模板 + 安全测试 checklist
```

---

### Phase 5: QA Automation (Week 11-12)

```python
# 8. 测试用例生成
python scripts/generate_test_cases.py \
  --design TECH_DESIGN_SSO.md \
  --code src/auth/sso/ \
  --output test_cases.md

# 生成 87 个测试用例：
# Functional Tests (45):
#   ├─ Happy path: Standard SAML login
#   ├─ Error: Expired SAML assertion
#   ├─ Error: Invalid signature
#   ├─ Edge: Multiple IdP configurations
#   └─ ...
# Security Tests (22):
#   ├─ XML signature wrapping attack
#   ├─ Replay attack detection
#   └─ ...
# Performance Tests (12):
# Integration Tests (8):

# 9. 自动化测试代码生成
python scripts/generate_test_code.py \
  --test-cases test_cases.md \
  --framework pytest \
  --output tests/test_sso.py

# 生成 1500+ 行测试代码，包括：
# - Fixtures（mock IdP responses）
# - Parametrized tests（覆盖多种 IdP）
# - Security tests（OWASP 标准）
```

---

### Phase 6: Go-to-Market (Week 13-14)

```python
# 10. 营销材料生成
python scripts/generate_gtm_materials.py \
  --prd PRD_SSO.md \
  --competitors competitors.yaml \
  --output gtm/

# 生成内容：
# ├─ Feature Announcement Blog Post (800 words)
# ├─ Sales One-Pager (1 page PDF)
# ├─ Product Demo Script (15 min walkthrough)
# ├─ FAQ Document (28 questions)
# ├─ Pricing Tier Recommendations
# ├─ Customer Communication Email Templates (3 versions)
# └─ Social Media Posts (Twitter, LinkedIn - 10 posts)

# 11. 客户沟通自动化
python scripts/segment_customers.py \
  --feature "SSO" \
  --output customer_segments.json

# 分段：
# - High Priority (已要求 SSO 功能): 234 customers → 个性化邮件
# - Enterprise Tier (可能感兴趣): 89 customers → 通用公告
# - SMB (暂时不相关): 1,245 customers → 不发送

# 12. 邮件个性化生成
python scripts/personalize_emails.py \
  --segment high_priority \
  --template feature_launch \
  --data customer_data.json

# 每封邮件包含：
# - 客户名称 + 历史请求引用
# - "还记得你在 2024-03-15 提到过......"
# - 个性化价值主张（基于客户行业）
# - 专属早期访问链接
```

---

### Phase 7: Post-Launch Analytics (Week 15+)

```python
# 13. 监控仪表板自动配置
python scripts/setup_monitoring.py \
  --feature "SSO" \
  --metrics metrics_config.yaml

# 自动创建 Grafana dashboards：
# - SSO 登录成功率（目标 >99.5%）
# - SAML 响应时间 P50/P95/P99
# - IdP 故障检测（15+ IdP 提供商）
# - 错误类型分布
# - 用户迁移率（密码 → SSO）

# 14. A/B 测试分析
python scripts/analyze_feature_adoption.py \
  --feature "SSO" \
  --period "30 days" \
  --output adoption_report.md

# 生成报告：
# - Adoption Rate: 23% → 67% (目标 80%)
# - User Satisfaction: NPS +12
# - Support Tickets: -34% (认证相关)
# - Revenue Impact: +$47k MRR (新客户 + upsell)
# - Recommendations:
#   ├─ 加速推广到剩余 33% 企业客户
#   ├─ 优化 IdP Okta 的配置流程（卡点）
#   └─ 增加 Azure AD 多租户支持（10 个客户请求）
```

---

## 🗂️ 完整技能包结构

```
product-lifecycle-manager/
├── SKILL.md (800 lines)
├── scripts/ (14 个脚本)
│   ├── 1_discovery/
│   │   ├── generate_stakeholder_questions.py
│   │   └── analyze_interviews.py
│   ├── 2_planning/
│   │   ├── generate_prd.py
│   │   └── risk_analysis.py
│   ├── 3_design/
│   │   ├── analyze_codebase.py
│   │   ├── generate_tech_design.py
│   │   └── diagram_generator.py
│   ├── 4_implementation/
│   │   ├── break_down_tasks.py
│   │   └── sync_to_jira.py
│   ├── 5_qa/
│   │   ├── generate_test_cases.py
│   │   └── generate_test_code.py
│   ├── 6_gtm/
│   │   ├── generate_gtm_materials.py
│   │   ├── segment_customers.py
│   │   └── personalize_emails.py
│   └── 7_analytics/
│       ├── setup_monitoring.py
│       └── analyze_feature_adoption.py
├── references/ (参考文档库)
│   ├── prd-templates/
│   │   ├── enterprise-feature.md
│   │   ├── consumer-feature.md
│   │   └── platform-feature.md
│   ├── tech-design-patterns/
│   │   ├── authentication-patterns.md
│   │   ├── api-design-standards.md
│   │   └── security-checklists/
│   ├── industry-benchmarks/
│   │   ├── saas-metrics.yaml
│   │   ├── adoption-curves.json
│   │   └── pricing-research.csv
│   └── compliance/
│       ├── gdpr-requirements.md
│       ├── sox-controls.md
│       └── iso27001-checklist.md
├── assets/ (模板和素材)
│   ├── document-templates/
│   │   ├── prd-template.docx
│   │   ├── tech-design-template.md
│   │   ├── one-pager-template.pptx
│   │   └── 37 other templates...
│   ├── diagram-styles/
│   │   ├── architecture-theme.json
│   │   └── flowchart-styles.css
│   └── brand-assets/
│       ├── logos/
│       ├── fonts/
│       └── color-palettes.yaml
└── integrations/ (第三方集成配置)
    ├── jira-config.yaml
    ├── slack-webhooks.json
    ├── grafana-dashboards/
    └── email-templates/

Total:
- 45 Python scripts (~15,000 lines)
- 120 reference documents (~200k words)
- 87 templates
- Total package size: ~50 MB
```

---

## 🎯 理论效能

**传统流程：**
```
产品经理: 2 周（PRD）
架构师: 1 周（设计）
项目经理: 3 天（任务拆解）
5 工程师: 6 周（实现）
QA: 2 周（测试）
产品营销: 1 周（GTM）
总计: ~12 周，~300 人时
```

**Skill 辅助流程：**
```
产品经理 + Skill: 3 天（PRD，自动化访谈分析）
架构师 + Skill: 2 天（设计，自动化架构分析）
项目经理 + Skill: 2 小时（任务拆解，自动化）
5 工程师 + Skill: 4 周（实时代码指导）
QA + Skill: 3 天（自动化测试生成）
产品营销 + Skill: 1 天（自动化材料生成）
总计: ~5 周，~120 人时

节省: 60% 时间，$$$万美元
```

---

## ⚡ 实际工作流示例

**完整对话流程：**

```
[Week 1, Monday 9:00 AM]
PM: "我需要为 SSO 功能做 PRD，我们有 3 个竞品已经有这个功能了"

Claude (product-lifecycle-manager skill):
好的！我会帮你完成完整的 PRD 流程。让我先分析一下：

1. 我看到你提到了竞品。让我先研究一下市场现状：
   📊 正在分析 3 个竞品的 SSO 实现...

2. 我需要和关键利益相关者做访谈。我已经生成了访谈指南：
   - CEO 访谈（15 个问题）- 估计 30 分钟
   - CTO 访谈（12 个问题）- 估计 45 分钟
   - 5 个企业客户访谈（20 个问题）- 估计 各 30 分钟

   📎 访谈指南已保存到 interviews/guide.md

3. 完成访谈后，把录音转录文本发给我，我会自动分析。

[Week 1, Friday 4:00 PM]
PM: "访谈都做完了，这是 7 份转录 [附件]"

Claude:
收到！正在分析...

✅ 分析完成！关键发现：
- **紧急度**: 9/10 (2 个大客户威胁流失)
- **收入机会**: $180k-$250k ARR
- **实现复杂度**: Medium-High
- **必需的 IdP 支持**: Okta (5 requests), Azure AD (3), Google (2)

📄 完整 PRD 已生成: PRD_SSO_v1.0.md (12 pages)

关键章节：
1. Executive Summary (包含 ROI 预测: 18 个月回本)
2. User Stories (从访谈中提取了 23 个)
3. Technical Requirements (已标记 SAML 2.0 + OAuth 2.0)
4. 风险矩阵 (识别了 17 个风险，3 个高优先级)

需要我继续进入技术设计阶段吗？

[Week 2, Monday]
PM: "PRD 已批准，请继续"

Claude:
太好了！开始技术设计...

🔍 正在分析你们的代码库...
   - 找到现有认证模块: src/auth/
   - 检测到使用 JWT tokens
   - 数据库: PostgreSQL with users table

🏗️ 生成技术设计文档...
   ✅ 完成！TECH_DESIGN_SSO.md (28 pages)

   包含：
   - 系统架构图（3 个 Mermaid 图表）
   - 数据库变更（5 个新表 + 迁移脚本）
   - API 规范（8 个新 endpoint，OpenAPI 3.0）
   - 安全威胁模型（STRIDE 分析，12 个威胁）

📋 任务拆解完成: 45 个任务
   - Backend: 18 tasks (38 story points)
   - Frontend: 12 tasks (18 story points)
   - DevOps: 8 tasks (12 story points)
   - QA: 7 tasks (10 story points)

   建议: 3 个 sprint (各 2 周)

要我在 JIRA 中创建这些任务吗？

[... 5 周后 ...]

[Week 7, Thursday]
PM: "功能开发完成，准备发布，帮我准备 GTM 材料"

Claude:
明白！开始准备上市材料...

📝 生成内容：
   ✅ Feature Announcement Blog (850 words, SEO optimized)
   ✅ Sales One-Pager (PDF, 已套用品牌模板)
   ✅ Demo Script (15 分钟演示流程)
   ✅ FAQ (28 个问题，来自客户访谈)
   ✅ Pricing建议 (增加 $50/月到 Enterprise tier)

📧 客户沟通：
   - 高优先级客户 (234人): 已生成个性化邮件
     示例: "Hi Sarah, 还记得您在 3月提到的 SSO 需求吗? 🎉"
   - Enterprise 客户 (89人): 通用公告邮件

   要我发送这些邮件吗？(需要你的批准)

📊 监控设置：
   ✅ Grafana dashboard created
   ✅ 7 个关键指标正在跟踪
   ✅ Alerts configured (失败率 > 1%)

准备就绪！要安排发布时间吗？
```

---

**价值：** ⭐⭐⭐⭐⭐
- 压缩 12 周 → 5 周
- 标准化最佳实践
- 减少人为错误
- 可重复流程
