---
name: walrasquant-strategy
description: Help write, modify, review, and debug WalrasQuant trading strategy files. Use when Codex needs to create or edit strategy scripts under the strategy directory, subclass walrasquant.strategy.Strategy, wire Config and Engine, use subscriptions, event handlers, schedules, indicators, cache access, order APIs, precision helpers, execution algorithms, or wq process commands for WalrasQuant strategies.
---

# WalrasQuant Strategy

## Overview

Use this skill to produce WalrasQuant strategy code for the installed `walrasquant` package. Prefer source-grounded framework APIs and concrete examples over generic trading-bot patterns.

## Workflow

1. Inspect the closest existing example before editing:
   - Exchange examples live under `strategy/binance/`, `strategy/bitget/`, `strategy/bybit/`, `strategy/hyperliquid/`, and `strategy/okx/`.
   - Core strategy API lives in `src/walrasquant/strategy.py`.
   - If local source is unavailable because WalrasQuant was installed from pip, infer from this skill's references and inspect the installed package with Python or site-packages paths when needed.
2. Identify the requested mode:
   - Event-driven: subscribe in `on_start`, implement `on_bookl1`, `on_bookl2`, `on_trade`, `on_kline`, or funding/price handlers.
   - Timer-driven: call `self.schedule(...)` in `on_start` and implement a synchronous function.
   - External signal: configure `ZeroMQSignalConfig` and implement `on_custom_signal`.
   - Execution algorithm: register the algorithm on `engine` and call `create_algo_order`.
3. Implement a complete runnable strategy script when the user asks for a new strategy:
   - Include imports, constants from `walrasquant.constants.settings`, a `Strategy` subclass, `Config`, `Engine`, and a guarded `engine.start()` / `engine.dispose()` block.
   - Put exchange-specific account types and symbols in the same style as existing examples.
4. Validate cheaply before finishing:
   - Run `python3 -m py_compile <strategy-file>` for edited strategy files when possible.
   - Avoid starting a live strategy unless the user explicitly asks.

## Guardrails

- Do not define `async def` methods on a `Strategy` subclass. `Strategy.__init_subclass__` rejects coroutine methods.
- Always call `super().__init__()` in the strategy constructor.
- Put subscriptions, `schedule(...)`, and `register_indicator(...)` in `on_start`, not `__init__`, because these APIs require the strategy to be registered by the engine.
- Use `Decimal("...")` for order amounts and prices supplied directly.
- Convert prices with `self.price_to_precision(symbol, px)` and amounts with `self.amount_to_precision(...)` or `self.min_order_amount(...)`.
- Check `self.ready` before timer-driven cache reads, and check `self.can_trade`, `self.can_open`, or `self.close_only` before submitting orders when connection state matters.
- Prefer `create_order_ws` / `cancel_order_ws` for websocket order paths when the matching exchange example uses websocket trading.
- Track active order IDs in strategy state and clear them in order handlers when fills, cancels, or failures arrive.
- Use WalrasQuant's American spelling for cancel hooks and properties: `on_canceled_order`, `OrderStatus.CANCELED`, `order.is_canceled`. Do not write `on_cancelled_order`, `CANCELLED`, or `is_cancelled` in strategy code.
- Use `self.log` instead of `print` inside strategy logic unless matching a tiny demo.
- Keep secrets in `settings.<EXCHANGE>...`; do not hard-code API keys.

## Reference

Load only the reference files needed for the task:

- `references/source-map.md`: source files and example files to inspect first.
- `references/strategy-api.md`: concrete `Strategy` lifecycle, handlers, subscription, order, timing, params, precision, and alert APIs.
- `references/schema-cache.md`: market data schemas, order and position fields, cache access, symbols, constants, and indicators.
- `references/exchange-configs.md`: exchange account types, settings paths, symbol forms, and config templates.
- `references/execution-web-signals.md`: TWAP/custom execution algorithms, ZeroMQ custom signals, FastAPI callbacks, process commands.
- `references/patterns.md`: ready-to-adapt strategy implementation patterns.
- `references/review-checklist.md`: bug checklist for reviewing WalrasQuant strategy code.
