# Review Checklist

Use this checklist when reviewing or debugging a WalrasQuant strategy.

## Lifecycle

- `Strategy` subclass has no `async def` methods. Current `Strategy.__init_subclass__` rejects coroutine methods, including decorated strategy web callbacks.
- `__init__` calls `super().__init__()`.
- Subscriptions, `schedule`, and `register_indicator` happen in `on_start`, not `__init__`.
- Strategy script has `Config`, `Engine`, and guarded `engine.start()` / `engine.dispose()`.
- Live processes are not started during review unless the user asked.

## Config

- `basic_config` exchange keys match connector config exchange keys.
- `public_conn_config` exists for market data subscriptions and requests.
- `private_conn_config` exists before using order APIs or `api(account_type)`.
- Account type matches symbol and exchange market type.
- API keys come from `settings`, not literal secrets.
- `LogConfig` filename and level are reasonable.
- `exit_after_cancel` default is understood; it cancels all open orders on dispose.

## Symbols

- Symbol suffix matches `ExchangeType`: `.BINANCE`, `.OKX`, `.BYBIT`, `.BITGET`, `.HYPERLIQUID`.
- Spot symbols have no dash; perps/futures include `-PERP` or another dashed suffix.
- Hyperliquid examples use `BTCUSDC-PERP.HYPERLIQUID`.

## Market Data And Cache

- Timer callbacks check `self.ready` before cache reads.
- Cache reads handle `None`.
- `cache.get_position` and `cache.get_order` unwrap Maybe with `.value_or(None)`.
- Kline code uses `KlineInterval` enum, not a raw string, unless an existing API explicitly accepts strings.
- `on_kline` ignores unconfirmed bars when the logic requires closed candles.

## Orders And Risk

- Amounts are `Decimal`.
- Prices use `price_to_precision`.
- Amounts use `amount_to_precision` or `min_order_amount`.
- Limit/post-only orders include `price`.
- Market orders intentionally use `price=None`.
- Duplicate order prevention exists through stored IDs, `get_open_orders`, position gate, or a signal flag.
- Stored order IDs are cleared on filled, canceled, failed, expired, and cancel-failed paths as appropriate.
- Cancel spelling is correct: `on_canceled_order`, `OrderStatus.CANCELED`, `order.is_canceled`; not `cancelled`.
- `can_trade`, `can_open`, or `close_only` are used for production order submission logic.
- Cancel loops avoid repeatedly canceling the same order; `get_open_orders` excludes cancel-intent orders by default.
- Batch cancel uses `CancelBatchOrder`, not raw strings.
- `modify_order` includes `side`, `price`, and `amount`.
- TP/SL trigger prices include matching order types.

## Indicators

- Indicator names are valid identifiers and not keywords.
- `register_indicator` is in `on_start`.
- Kline indicators have `kline_interval`.
- Warmup indicators have both `warmup_period` and `kline_interval`.
- Access is through `self.indicator.<name>[symbol]` after registration.
- Indicator state is per symbol because `register_indicator` deep-copies the instance.

## Execution Algorithms

- `engine.add_exec_algorithm(...)` is called before `engine.start()`.
- `exec_algorithm_id` matches the registered algorithm ID.
- TWAP has `horizon_secs` and `interval_secs`, and `horizon_secs >= interval_secs`.
- TWAP limit mode has bookl1 subscription if it needs limit pricing.
- Custom algorithms call `mark_complete` when done.

## Web, Signals, Params, Alerts

- ZeroMQ config has matching `on_custom_signal`.
- Web callbacks use `create_strategy_app` and `WebConfig(enabled=True, ...)`.
- Redis params require Redis availability.
- FlashDuty alerts require `flashduty_integration_key`.

## Validation

- Run `python3 -m py_compile <strategy-file>` after edits when imports do not require unavailable secrets.
- If import would fail because `.keys` secrets are missing, at least compile syntax without executing the module where possible.
- Do not run `engine.start()` as validation unless the user explicitly requests a live or testnet run.
