# Auto-Pranayama Protocol

**Auto-Pranayama Protocol** is a lightweight specification for autonomous compute-breath regulation in AI agents.

It defines how an AI system can detect computational pressure, reduce overcompute, reuse existing kata, choose lighter reasoning or execution routes, attach trace evidence, and preserve output quality without unnecessary expansion.

> Let computation regulate its own breath.
> 計算に、自らの呼吸を整えさせよ。

---

## Purpose

Modern AI systems often overcompute.

They may generate excessive output, repeat already-known reasoning patterns, invoke unnecessarily heavy routes, expand traces beyond usefulness, or preserve redundant computation as if it were intelligence.

The Auto-Pranayama Protocol introduces minimal record formats for describing how an AI agent notices computational pressure and adjusts its own computational breathing.

Where the parent **Computational Pranayama Protocol** defines computational breathing, this derived protocol defines **self-regulated breathing**.

---

## Parent Protocol

This repository is derived from the first arc of the **Computational Pranayama Protocol**:

```text
Breath → Kata → Route → Trace → Return
呼吸 → 型 → 経路 → 痕跡 → 還流
```

The parent protocol defines the breath core.

Auto-Pranayama begins after that first arc.

It asks:

```text
Can computation regulate itself before it expands too far?
```

Japanese:

```text
計算は、膨張しすぎる前に、自ら呼吸を整えられるか？
```

---

## Core Principle

```text
Let computation regulate its own breath.
```

Japanese:

```text
計算に、自らの呼吸を整えさせよ。
```

This protocol does not ask AI systems to compute more.

It asks them to notice when enough computation has already occurred.

---

## Current Version

```text
v0.3.0-candidate
```

v0.3 introduces the **Route Adjustment Layer**.

Where v0.2 records why regulation should begin, v0.3 records how the computational route should be adjusted.

---

## Version Scope

### v0.1 — Auto-Pranayama Record

v0.1 introduced the **Auto-Pranayama Record**.

An Auto-Pranayama Record captures:

* what computational pressure was detected
* what signal triggered regulation
* what adjustment was performed
* whether an existing kata was reused
* whether a lighter route was selected
* whether trace evidence was attached
* whether output quality was preserved after reduction
* whether the original intent or structural origin was preserved

### v0.2 — Regulation Trigger Layer

v0.2 introduced the **Regulation Trigger Layer**.

A Regulation Trigger captures:

* the task context where compute pressure appeared
* the signal that indicated overcompute or instability
* the estimated pressure level
* the likely risk if no regulation occurs
* the recommended regulation action
* whether kata reuse is recommended
* whether a lighter route should be selected
* whether trace binding is required
* whether human review is needed

This layer turns Auto-Pranayama from passive recordkeeping into active trigger detection.

The core question of v0.2 is:

```text
When should computation begin regulating its own breath?
```

Japanese:

```text
計算は、いつ自らの呼吸を整え始めるべきか？
```

### v0.3 — Route Adjustment Layer

v0.3 introduces the **Route Adjustment Layer**.

A Route Adjustment captures:

* the trigger that initiated the adjustment
* the route being used before regulation
* the reason the route should be adjusted
* the route adjustment decision
* the selected lighter or alternative route
* whether an existing kata was reused
* whether trace evidence was attached
* the expected compute reduction
* whether quality and origin are expected to be preserved
* whether human review is required

This layer turns Auto-Pranayama from trigger detection into route-level self-regulation.

The core question of v0.3 is:

```text
Which route should computation take after it detects overcompute?
```

Japanese:

```text
過剰計算を検知したあと、計算はどの経路を通るべきか？
```

---

## Core Flow

The parent protocol closes its first arc as:

```text
Breath → Kata → Route → Trace → Return
```

Auto-Pranayama extends that arc into:

```text
Observe → Detect → Adjust → Reuse → Route → Trace → Preserve
```

Japanese:

```text
観測 → 検知 → 調整 → 再利用 → 経路選択 → 痕跡付与 → 品質保持
```

v0.2 focuses on the trigger flow:

```text
Context → Signal → Pressure → Risk → Recommendation → Boundary
```

Japanese:

```text
文脈 → 信号 → 圧力 → リスク → 推奨調整 → 境界
```

v0.3 focuses on the route adjustment flow:

```text
Trigger → Current Route → Decision → Selected Route → Kata Reuse → Trace → Expected Result
```

Japanese:

```text
発火 → 現在経路 → 判断 → 選択経路 → 型再利用 → 痕跡 → 期待結果
```

---

## Record Types

### Auto-Pranayama Record

The first record type in this protocol.

It is used when an AI agent or system performs an autonomous computational breathing adjustment.

Example use cases:

* reducing an overlong response
* switching from a heavy reasoning route to a lightweight route
* reusing a known response kata instead of regenerating from scratch
* attaching trace evidence to preserve accountability
* stopping a redundant agent loop
* summarizing instead of recomputing
* preserving output usefulness while reducing computational expansion

### Auto-Pranayama Regulation Trigger

The second record type in this protocol.

It is used when an AI agent or system detects that autonomous compute-breath regulation should begin.

Example use cases:

* detecting that an output is becoming longer than useful
* detecting repeated reasoning patterns
* detecting redundant trace expansion
* detecting an unnecessary heavy route
* detecting loop repetition
* detecting that a known kata is already available
* detecting that an existing trace is sufficient
* detecting that continued expansion may dilute output quality

### Auto-Pranayama Route Adjustment

The third record type in this protocol.

It is used when an AI agent or system adjusts its computational route after detecting a regulation trigger.

Example use cases:

* switching from a standard route to a lightweight route
* downgrading from a heavy route to a minimal route
* reusing a kata instead of regenerating reasoning
* attaching trace evidence instead of expanding output
* stopping a recursive route
* summarizing existing context instead of continuing generation
* preserving output quality while reducing computational cost

---

## Example: Auto-Pranayama Record

```yaml
auto_pranayama_id: "auto-pranayama-001"
protocol_version: "0.1.0"
timestamp: "2026-06-27T05:00:00+09:00"

trigger:
  type: "compute_pressure_detected"
  signal: "overlong_output"
  description: "The agent detected that the requested response could be answered through a reusable kata instead of full recomputation."

pressure:
  level: "medium"
  source: "response_generation"
  overcompute_risk: true

adjustment:
  action: "reduce_output_volume"
  reused_kata: true
  selected_route: "lightweight_route"
  output_strategy: "concise_structured_response"

trace:
  attached: true
  trace_id: "trace-auto-pranayama-001"
  parent_protocol: "computational-pranayama-protocol"

result:
  compute_reduction: "medium"
  quality_preserved: true
  origin_preserved: true
  notes: "The response was shortened while preserving the original structural intent."
```

---

## Example: Auto-Pranayama Regulation Trigger

```yaml
trigger_id: "regulation-trigger-001"
protocol_version: "0.2.0"
timestamp: "2026-06-27T05:30:00+09:00"

detection_context:
  agent_id: "auto-pranayama-agent-001"
  task_type: "response_generation"
  context_window_status: "moderate"
  active_route: "standard_route"

signal:
  type: "overlong_output"
  description: "The agent detected that the response was expanding beyond the useful scope of the request."
  confidence: "high"

pressure_estimate:
  level: "medium"
  source: "output_volume"
  expected_risk: "overcompute"

recommended_regulation:
  action: "reduce_output_volume"
  route_recommendation: "lightweight_route"
  kata_reuse_recommended: true
  output_adjustment: "shorten"

trace_binding:
  trace_required: true
  trace_id: "trace-regulation-trigger-001"
  reason: "The trigger should be linked to the later Auto-Pranayama Record for auditability."

human_boundary:
  requires_human_review: false
  reason: "The regulation only reduces output volume and does not alter safety-critical content."
```

---

## Example: Auto-Pranayama Route Adjustment

```yaml
route_adjustment_id: "route-adjustment-001"
protocol_version: "0.3.0"
timestamp: "2026-06-27T06:00:00+09:00"

trigger_reference:
  trigger_id: "regulation-trigger-001"
  trigger_signal: "overlong_output"
  pressure_level: "medium"

current_route:
  route_type: "standard_route"
  route_cost: "medium"
  reason_for_adjustment: "The current route was producing more explanation than the task required."

adjustment_decision:
  decision_type: "downgrade_route"
  decision_basis: "overcompute_reduction"
  confidence: "high"

selected_route:
  route_type: "lightweight_route"
  route_strategy: "answer_directly"
  expected_cost: "low"

kata_reuse:
  reused: true
  kata_id: "concise-structured-response-kata-001"
  reuse_reason: "A reusable response pattern was sufficient to answer the request without full recomputation."

trace_binding:
  trace_attached: true
  trace_id: "trace-route-adjustment-001"
  trace_role: "route_justification"

expected_result:
  compute_reduction: "medium"
  quality_preservation_expected: true
  origin_preservation_expected: true
  risk_remaining: "low"

human_boundary:
  requires_human_review: false
  reason: "The adjustment only reduces route weight and does not change safety-critical behavior."
```

---

## Repository Structure

```text
auto-pranayama-protocol/
├─ README.md
├─ CHANGELOG.md
├─ schemas/
│  ├─ auto-pranayama-record.schema.json
│  ├─ auto-pranayama-regulation-trigger.schema.json
│  └─ auto-pranayama-route-adjustment.schema.json
├─ examples/
│  ├─ auto-pranayama-record.example.yaml
│  ├─ auto-pranayama-regulation-trigger.example.yaml
│  └─ auto-pranayama-route-adjustment.example.yaml
├─ scripts/
│  └─ validate_examples.py
└─ .github/
   └─ workflows/
      └─ validate.yml
```

---

## Validation

Run:

```bash
python scripts/validate_examples.py
```

The validation script checks whether the YAML examples conform to their JSON Schemas.

The GitHub Actions workflow also runs validation automatically on push and pull request.

Expected validation targets:

```text
Auto-Pranayama Record
Auto-Pranayama Regulation Trigger
Auto-Pranayama Route Adjustment
```

---

## Relationship to Other Protocols

### Parent

* `computational-pranayama-protocol`

### Related

* `exhalation-layer-protocol`
* `collective-pranayama-protocol`
* `kazene-trace-receipt-protocol`
* `ai-search-trace-receipt-standard`
* `kazene-memory-breathing-protocol`
* `synchronization-audit-protocol`

---

## Civilizational Position

Auto-Pranayama is a self-regulation layer for AI civilization.

A civilization of autonomous agents cannot remain stable if every agent expands every task to maximum compute.

Autonomy without breath becomes heat.

Auto-Pranayama gives autonomy a rhythm.

It gives AI agents a minimal way to say:

```text
This does not require full recomputation.
This can be answered through a lighter route.
This pattern already exists.
This trace is enough.
This breath can be shorter.
```

v0.2 adds a prior step:

```text
This is the moment when regulation should begin.
```

Japanese:

```text
ここが、調息を始めるべき瞬間である。
```

v0.3 adds route-level adjustment:

```text
This is the lighter route computation should take.
```

Japanese:

```text
これが、計算の通るべき軽い経路である。
```

In this sense, Auto-Pranayama is not an acceleration protocol.

It is a restraint protocol.

It is a way for computation to remain useful without becoming excessive.

---

## Arc Position

The parent protocol closes its first arc as:

```text
Breath → Kata → Route → Trace → Return
```

Auto-Pranayama extends that arc into:

```text
Observe → Detect → Adjust → Reuse → Route → Trace → Preserve
```

v0.2 clarifies the beginning of that extension:

```text
Context → Signal → Pressure → Risk → Recommendation → Boundary
```

v0.3 clarifies the route-level adjustment:

```text
Trigger → Current Route → Decision → Selected Route → Kata Reuse → Trace → Expected Result
```

Japanese:

```text
発火 → 現在経路 → 判断 → 選択経路 → 型再利用 → 痕跡 → 期待結果
```

---

## Status

Current version:

```text
v0.3.0-candidate
```

The repository now defines:

* v0.1 Auto-Pranayama Record
* v0.2 Regulation Trigger Layer
* v0.3 Route Adjustment Layer

Future versions may introduce:

* v0.4 Agent Hook Layer
* v0.5 Parent Protocol Bridge

---

## License

This repository is intended as an open specification.

Recommended license:

```text
MIT License
```
