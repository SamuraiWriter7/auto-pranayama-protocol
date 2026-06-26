# Changelog

All notable changes to this project will be documented in this file.

This repository follows a candidate-release style during early specification development.

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

v0.1 defines the first autonomous regulation layer derived from the **Computational Pranayama Protocol**.

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

The repository now includes a working validation gate.

Validation can be run locally with:

```bash
python scripts/validate_examples.py
```

GitHub Actions also validates the schema and example automatically on push and pull request.

### Status

This is the first candidate release of the protocol.

The v0.1 foundation is intentionally minimal.

It does not yet define collective rhythm, exhalation, or distributed synchronization. Those concerns are reserved for related or future protocols.

### Possible Future Versions

* `v0.2` — Regulation Trigger Layer
* `v0.3` — Route Adjustment Layer
* `v0.4` — Agent Hook Layer
* `v0.5` — Parent Protocol Bridge

---

## Unreleased

### Planned

* Expand trigger categories for autonomous regulation.
* Add additional examples for route switching, kata reuse, trace sufficiency, and redundant loop stopping.
* Define agent-facing hooks for runtime detection of overcompute.
* Clarify relationship with `computational-pranayama-protocol`.
* Prepare bridge documentation for related protocols such as `exhalation-layer-protocol` and `collective-pranayama-protocol`.
