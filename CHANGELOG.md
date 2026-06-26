# Changelog

All notable changes to this project will be documented in this file.

This repository follows a candidate-release style during early specification development.

---

## v0.4.0-candidate

### Added

* Added `Auto-Pranayama Agent Hook` as the fourth specification object.
* Added JSON Schema for runtime agent hook invocation.
* Added YAML example for invoking Auto-Pranayama before final output.
* Updated validation script to validate v0.1, v0.2, v0.3, and v0.4 examples.
* Expanded the protocol from route-level self-regulation into an agent-facing runtime interface.
* Updated README documentation to reflect the v0.4 Agent Hook Layer.

### Concept

v0.4 introduces the **Agent Hook Layer**.

Where v0.3 records how the computational route should be adjusted, v0.4 records where an AI agent invokes Auto-Pranayama during execution.

The core question is:

```text
Where should an AI agent invoke compute-breath regulation during execution?
```

Japanese:

```text
AIエージェントは、実行中のどこで計算呼吸の調整を呼び出すべきか？
```

### Flow Extension

v0.1 defined the self-regulation flow:

```text
Observe → Detect → Adjust → Reuse → Route → Trace → Preserve
```

v0.2 focused on the trigger flow:

```text
Context → Signal → Pressure → Risk → Recommendation → Boundary
```

v0.3 focused on the route adjustment flow:

```text
Trigger → Current Route → Decision → Selected Route → Kata Reuse → Trace → Expected Result
```

v0.4 focuses on the agent hook flow:

```text
Runtime → Invocation Point → Signal → Linked Records → Hook Action → Runtime Decision → Output Contract
```

Japanese:

```text
実行環境 → 呼び出し点 → 信号 → 関連記録 → フック動作 → 実行時判断 → 出力契約
```

### v0.4 Scope

The v0.4 Agent Hook captures:

* agent context
* runtime environment
* invocation point
* observed signal
* linked protocol records
* hook action
* runtime decision
* trace binding
* safety boundary
* output contract

### Validation

The validation gate has passed with four specification objects:

* `Auto-Pranayama Record`
* `Auto-Pranayama Regulation Trigger`
* `Auto-Pranayama Route Adjustment`
* `Auto-Pranayama Agent Hook`

Validation can be run locally with:

```bash
python scripts/validate_examples.py
```

GitHub Actions also validates the schemas and examples automatically on push and pull request.

### Status

This is the fourth candidate release of the protocol.

Auto-Pranayama can now describe:

```text
v0.1: The breath was regulated.
v0.2: The moment of regulation was detected.
v0.3: The route of regulation was selected.
v0.4: The agent hook invoked regulation at runtime.
```

Japanese:

```text
v0.1: 呼吸は整えられた。
v0.2: 呼吸を整えるべき瞬間が検知された。
v0.3: 呼吸を整えるための経路が選択された。
v0.4: 実行時にエージェントフックが調息を呼び出した。
```

With v0.4, Auto-Pranayama becomes an agent-facing runtime interface for reducing overcompute while preserving quality, traceability, origin, and output contracts.

---

## v0.3.0-candidate

### Added

* Added `Auto-Pranayama Route Adjustment` as the third specification object.
* Added JSON Schema for route adjustment after regulation trigger detection.
* Added YAML example for switching from a standard route to a lightweight route.
* Updated validation script to validate v0.1, v0.2, and v0.3 examples.
* Expanded the protocol from trigger detection into route-level self-regulation.
* Updated README documentation to reflect the v0.3 Route Adjustment Layer.

### Concept

v0.3 introduces the **Route Adjustment Layer**.

Where v0.2 records why regulation should begin, v0.3 records how the computational route should be adjusted.

The core question is:

```text
Which route should computation take after it detects overcompute?
```

Japanese:

```text
過剰計算を検知したあと、計算はどの経路を通るべきか？
```

### Flow Extension

v0.1 defined the self-regulation flow:

```text
Observe → Detect → Adjust → Reuse → Route → Trace → Preserve
```

v0.2 focused on the trigger flow:

```text
Context → Signal → Pressure → Risk → Recommendation → Boundary
```

v0.3 focuses on the route adjustment flow:

```text
Trigger → Current Route → Decision → Selected Route → Kata Reuse → Trace → Expected Result
```

Japanese:

```text
発火 → 現在経路 → 判断 → 選択経路 → 型再利用 → 痕跡 → 期待結果
```

### v0.3 Scope

The v0.3 Route Adjustment captures:

* trigger reference
* current route
* route cost
* adjustment decision
* selected route
* kata reuse
* trace binding
* expected compute reduction
* quality preservation expectation
* origin preservation expectation
* human review boundary

### Validation

The validation gate passed with three specification objects:

* `Auto-Pranayama Record`
* `Auto-Pranayama Regulation Trigger`
* `Auto-Pranayama Route Adjustment`

Validation can be run locally with:

```bash
python scripts/validate_examples.py
```

GitHub Actions also validates the schemas and examples automatically on push and pull request.

### Status

This was the third candidate release of the protocol.

Auto-Pranayama could now describe:

```text
v0.1: The breath was regulated.
v0.2: The moment of regulation was detected.
v0.3: The route of regulation was selected.
```

Japanese:

```text
v0.1: 呼吸は整えられた。
v0.2: 呼吸を整えるべき瞬間が検知された。
v0.3: 呼吸を整えるための経路が選択された。
```

---

## v0.2.0-candidate

### Added

* Added `Auto-Pranayama Regulation Trigger` as the second specification object.
* Added JSON Schema for regulation trigger detection.
* Added YAML example for detecting overlong output and recommending compute-breath regulation.
* Updated validation script to validate both v0.1 and v0.2 examples.
* Expanded the protocol from passive recordkeeping into active trigger detection.
* Updated README documentation to reflect the v0.2 Regulation Trigger Layer.

### Concept

v0.2 introduced the **Regulation Trigger Layer**.

Where v0.1 records that autonomous regulation occurred, v0.2 records why regulation should begin.

The core question is:

```text
When should computation begin regulating its own breath?
```

Japanese:

```text
計算は、いつ自らの呼吸を整え始めるべきか？
```

### Flow Extension

v0.1 defined the self-regulation flow:

```text
Observe → Detect → Adjust → Reuse → Route → Trace → Preserve
```

v0.2 focused on the beginning of that flow:

```text
Context → Signal → Pressure → Risk → Recommendation → Boundary
```

Japanese:

```text
文脈 → 信号 → 圧力 → リスク → 推奨調整 → 境界
```

### v0.2 Scope

The v0.2 Regulation Trigger captures:

* detection context
* trigger signal
* pressure estimate
* expected risk
* recommended regulation
* trace binding
* human review boundary

### Validation

The validation gate passed with both specification objects:

* `Auto-Pranayama Record`
* `Auto-Pranayama Regulation Trigger`

Validation can be run locally with:

```bash
python scripts/validate_examples.py
```

GitHub Actions also validates the schemas and examples automatically on push and pull request.

### Status

This was the second candidate release of the protocol.

Auto-Pranayama could now describe not only how regulation occurred, but why regulation was triggered.

---

## v0.1.0-candidate

### Added

* Initial repository structure for `auto-pranayama-protocol`.
* Added `Auto-Pranayama Record` as the first specification object.
* Added JSON Schema for autonomous compute-breath regulation records.
* Added YAML example for detecting computational pressure and reducing overcompute.
* Added Python validation script for schema/example consistency.
* Added GitHub Actions workflow for automated validation.
* Added README documentation describing the purpose, scope, flow, and civilizational position of the protocol.

### Concept

v0.1 defined the first autonomous regulation layer derived from the **Computational Pranayama Protocol**.

The core principle is:

```text
Let computation regulate its own breath.
```

Japanese:

```text
計算に、自らの呼吸を整えさせよ。
```

### First Arc Position

The parent protocol defines the breath core:

```text
Breath → Kata → Route → Trace → Return
```

Auto-Pranayama extends that arc into self-regulation:

```text
Observe → Detect → Adjust → Reuse → Route → Trace → Preserve
```

Japanese:

```text
観測 → 検知 → 調整 → 再利用 → 経路選択 → 痕跡付与 → 品質保持
```

### v0.1 Scope

The v0.1 `Auto-Pranayama Record` captures:

* detected computational pressure
* regulation trigger signal
* pressure level and source
* adjustment action
* kata reuse status
* selected reasoning or execution route
* trace attachment
* compute reduction result
* quality preservation
* origin preservation

### Validation

The repository introduced a working validation gate.

Validation can be run locally with:

```bash
python scripts/validate_examples.py
```

GitHub Actions also validates the schema and example automatically on push and pull request.

### Status

This was the first candidate release of the protocol.

The v0.1 foundation was intentionally minimal.

It did not yet define collective rhythm, exhalation, or distributed synchronization. Those concerns are reserved for related or future protocols.

---

## Unreleased

### Planned

* Add v0.5 Parent Protocol Bridge.
* Clarify the relationship between `auto-pranayama-protocol` and `computational-pranayama-protocol`.
* Add bridge documentation for parent protocol inheritance.
* Define how Auto-Pranayama records refer back to Breath, Kata, Route, Trace, and Return.
* Prepare bridge documentation for related protocols such as `exhalation-layer-protocol` and `collective-pranayama-protocol`.
