# 方法依据与边界

本Skill将公开方法改造成面向用户的组件复用流程，不声称获得认证、完全遵循所有条款或形成通用可复用性标准。下列链接在2026-10-01设计时核查；运行任务需要当前版本事实时再次核查。

## SEI OAR：研究骨架

来源：[Options Analysis for Reengineering (OAR): A Method for Mining Legacy Assets](https://www.sei.cmu.edu/library/options-analysis-for-reengineering-oar-a-method-for-mining-legacy-assets/)，CMU/SEI-2001-TN-013。

借用：从目标架构和需求出发，识别组件、分析改造、比较采用选项及成本风险，再选择路线。补充阅读：[LSI应用研究](https://www.sei.cmu.edu/library/application-of-options-analysis-for-reengineering-in-a-lead-system-integrator-environment/)。

边界：这是较早的工程方法，不是当前软件供应链安全标准；原始组织/产品线管理流程不适合直接搬进一次模块研究。我们的授权交接、证据标签和隔离验证属于本Skill设计，不宣称是OAR原文规定。

## arc42：把外部质量写成场景

来源：[Quality Requirements](https://docs.arc42.org/section-10/)及[quality scenario说明](https://faq.arc42.org/questions/C-10-2/)。

借用：用触发条件、反应和可判断的结果说明使用、失败和变更要求，避免只写“可靠、可维护”。

边界：不要求用户填写完整架构模板，不把示例阈值当目标需求。只写能改变候选判断的场景。

## ISO/IEC 25010:2023：质量参考模型

来源：[ISO官方公开说明](https://committee.iso.org/standard/78176.html)。

借用：除功能外，按相关性考虑兼容、可靠、安全、维护等质量问题。

边界：本设计仅使用公开模型用途，不依据未取得的完整标准声称逐条符合，不规定评分权重或合格线。抽离判据是本Skill的工程检查，不是ISO评级。

## OpenSSF Scorecard：上游风险信号

来源：[官方仓库](https://github.com/ossf/scorecard)。

借用：安全与维护实践的具体证据，可补充包和源码调查。

边界：不强制安装或运行扫描器；评分不能证明接口匹配、代码安全或可抽离，缺少评分也不能直接淘汰候选。执行工具仍需相应授权。

## Pact：区分契约与功能证明

来源：[Introduction](https://docs.pact.io/)和[Contract Tests vs Functional Tests](https://docs.pact.io/consumer/contract_tests_not_functional_tests)。

借用：从真实消费者需要的交互出发验证接口，并单独验证实现行为与副作用。

边界：这里的Pact是契约测试项目，不是任何目标仓库的内核包。不限HTTP，不强制采用Pact框架；纯内存组件也可用普通测试表达消费者契约。

## FSFE REUSE：文件级来源信息

来源：[REUSE Specification 3.3](https://reuse.software/spec-3.3/)。

借用：抽取文件仍保留明确版权与许可信息，必要时采用SPDX表达。

边界：信息标准化不是许可兼容法律裁定，不强制全仓改造、不用工具通过代替许可核查。

## 已研究的Skill底稿

- [reduce-reinvention](https://github.com/JUNERDD/skills/tree/main/skills/reduce-reinvention)：借鉴采用/适配/包装/抽取的路线比较和反对强制抽象；不引入组织级治理负担。
- [software-architecture-analysis](https://github.com/magnus919/agent-skills/tree/main/software-architecture-analysis)：借鉴耦合与隐含接口调查；不采用其禁止复制源码的特定任务定位。
- [Impeccable extract](https://github.com/pbakaus/impeccable/blob/main/skill/reference/extract.md)：借鉴UI迁移与行为保持检查；不把其项目内重复次数准则套到外部组件采用。

本包指令为本次需求设计的原创表述，链接用于方法溯源，并非复制底稿指令文件。今后复制实际代码或文本时另行核查许可。
