# Component Reuse · 开源组件研究与复用

An Agent Skill for finding and evaluating reusable open-source implementations for a missing capability in your project. Start with the consumer's requirements, investigate actual source boundaries, explain adoption choices, and validate or integrate only with authorization.

一个帮助 Agent 为当前项目寻找、研究和采用开源实现的 Skill。不是把整个仓库总结一遍，也不是看完别人的实现后重新造轮子。

## 适合什么任务

- “这个模块有没有现成实现可以复用？”
- “能不能从这个开源项目里拆出我们需要的组件？”
- “比较一下直接依赖、包装、抽取源码的成本和风险。”

不用于一般仓库导览、项目内部单纯去重，或默认从零实现。

## 工作方式

1. 先看目标项目缺什么、接在哪里；澄清外部需求，每轮最多两个问题，不要求用户设计内部实现。
2. 搜集候选并读源码，检查初始化、依赖、共享状态、生命周期、副作用和许可，不以 README 或星数代替行为证据。
3. 用用户能理解的用途、收益、缺口和代价解释候选；推荐不代替用户选择，候选数量不固定。
4. 经授权做隔离验证，汇报真实结果；接入仍需单独批准。
5. 区分采用部分与自建部分，保留来源、许可证和后续更新办法。

支持直接依赖、薄包装、源码抽取、上游扩展、多个组件组合，也允许结论是自行实现。仅借鉴设计不称为源码复用。

## 安装到 Codex

在已安装 Git 的环境里：

```bash
git clone https://github.com/mmm-05610/component-reuse.git
mkdir -p "$HOME/.codex/skills"
# 目标目录已存在时先比较，不要直接覆盖。
test ! -e "$HOME/.codex/skills/component-reuse" && \
  cp -R component-reuse "$HOME/.codex/skills/component-reuse"
```

启动新的 Codex 会话，确认技能列表包含 `component-reuse`。也可以只复制 `SKILL.md`、`agents/`、`references/` 和 `evals/`，不需要 Git 历史。

其他支持 `SKILL.md` 的 Agent 可按各自的技能目录安装。`agents/openai.yaml` 是 Codex 元数据；自动发现和触发行为在其他 Agent 中尚未验证。

## 使用

显式调用：

```text
使用 $component-reuse 为我们的项目寻找一个可复用的只读代码差异查看组件。
先检查已有接入点，澄清必要需求，比较候选，先不要改代码。
```

也可以自然描述“寻找开源可复用实现”。本包允许 Codex 隐式选择，但是否正确触发需要实际测试，不能只凭安装成功保证。

## 文件结构

```text
SKILL.md                 入口、原则和按阶段读取的路由
agents/openai.yaml       Codex 显示信息与隐式调用策略
references/              需求、调查、比较、验证、来源与方法依据
evals/evaluations.md      行为评估案例和判据
evals/fixtures/          合成组件与消费者
evals/test_fixtures.py    检查夹具事实的六个测试
```

## 当前验证状态

这是初始公开版本，不是已经证明优于其他 Skill 的产品。

- 已检查入口元数据和参考文件组织。
- 六个合成夹具测试可运行：`python3 evals/test_fixtures.py`。
- 上述测试只证明夹具确实具有隐藏初始化、共享状态及生命周期等问题，不证明 Agent 会识别它们。
- 独立 Agent 的真实任务表现、自动触发和跨 Agent 兼容性仍待评估。参见 [评估设计](evals/evaluations.md)。

## 方法和来源

参考 SEI OAR、arc42、ISO/IEC 25010 的公开质量模型、OpenSSF Scorecard、Pact 与 FSFE REUSE。具体借用方式和边界见 [方法依据](references/foundations.md)。本包不声称标准认证或法律合规结论，也不强制使用这些工具。

指令为本项目原创表述。来源链接用于方法溯源，不代表复制上游代码或指令文件；以后实际引入第三方内容时须另行保留其许可。

## 反馈

欢迎通过 GitHub Issues 提供真实任务记录：目标需求、Agent/模型、是否主动触发、候选证据、用户交接和具体失败行为。请移除凭据、私人仓库内容和用户数据。
