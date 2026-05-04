# Strategy API Reference

Source: `src/walrasquant/strategy.py`.

## Lifecycle Rules

- Subclass `Strategy`.
- Call `super().__init__()` in `__init__`.
- Do not define `async def` methods on the `Strategy` subclass. `Strategy.__init_subclass__` rejects coroutine methods.
- Initialize pure Python state in `__init__`.
- Put subscriptions, indicator registration, and schedules in `on_start`, because the strategy is registered by `Engine` before `on_start` runs.
- Use `on_stop` for cleanup.
- `Engine.start()` calls `_build`, initializes cache, starts connectors, starts execution algorithms, starts custom signal receiver, calls strategy `on_start`, starts the APScheduler, then waits.
- `Engine.dispose()` stops execution algorithms, calls `on_stop`, optionally cancels all open orders, disconnects connectors, syncs cache, shuts down logging and web app bindings.

## Built-In Strategy Attributes After Registration

These are available after `Engine(config)` registers the strategy:

- `self.log`: logger named after the strategy class.
- `self.cache`: `AsyncCache`.
- `self.clock`: `LiveClock`.
- `self.indicator`: `IndicatorProxy`.
- `self.ready`: proxy for subscription manager readiness.
- `self.connection_status`: `ConnectionPolicyState | None`.
- `self.can_open`: true when market data and trading data required websockets are OK.
- `self.can_trade`: true when trading data required websockets are OK.
- `self.close_only`: true when only closing/reducing should be allowed.

## Handlers

Data handlers:

- `on_bookl1(self, bookl1: BookL1)`
- `on_bookl2(self, bookl2: BookL2)`
- `on_trade(self, trade: Trade)`
- `on_kline(self, kline: Kline)`
- `on_funding_rate(self, funding_rate: FundingRate)`
- `on_index_price(self, index_price: IndexPrice)`
- `on_mark_price(self, mark_price: MarkPrice)`
- `on_balance(self, balance: AccountBalance)`
- `on_connection_status(self, status: ConnectionPolicyState)`

Order handlers:

- `on_pending_order(self, order: Order)`
- `on_accepted_order(self, order: Order)`
- `on_partially_filled_order(self, order: Order)`
- `on_filled_order(self, order: Order)`
- `on_canceling_order(self, order: Order)`
- `on_expired_order(self, order: Order)`
- `on_canceled_order(self, order: Order)`
- `on_failed_order(self, order: Order)`
- `on_cancel_failed_order(self, order: Order)`

Spelling guardrail:

- Use `canceled` with one `l` in strategy-facing code.
- Correct: `on_canceled_order`, `OrderStatus.CANCELED`, `order.is_canceled`.
- Incorrect: `on_cancelled_order`, `OrderStatus.CANCELLED`, `order.is_cancelled`.
- Some exchange-native APIs may use `cancelled`; convert to WalrasQuant names at the strategy layer.

Custom signal handler:

- Define `on_custom_signal(self, signal)` when `Config.zero_mq_signal_config` is set.

## Subscriptions

Call subscription methods in `on_start`.

- `subscribe_bookl1(symbols, ready_timeout=60, ready=True)`
- `subscribe_bookl2(symbols, level: BookLevel, ready_timeout=60, ready=True)`
- `subscribe_trade(symbols, ready_timeout=60, ready=True)`
- `subscribe_kline(symbols, interval: KlineInterval, ready_timeout=60, ready=True, use_aggregator=False, build_with_no_updates=True)`
- `subscribe_volume_kline(symbols, volume_threshold: float, volume_type="DEFAULT", ready_timeout=60, ready=True)`
- `subscribe_funding_rate(symbols, ready_timeout=60, ready=True)`
- `subscribe_index_price(symbols, ready_timeout=60, ready=True)`
- `subscribe_mark_price(symbols, ready_timeout=60, ready=True)`

Matching unsubscribe methods:

- `unsubscribe_bookl1(symbols)`
- `unsubscribe_bookl2(symbols, level)`
- `unsubscribe_trade(symbols)`
- `unsubscribe_kline(symbols, interval, use_aggregator=False)`
- `unsubscribe_volume_kline(symbols, volume_threshold, volume_type="DEFAULT")`
- `unsubscribe_funding_rate(symbols)`
- `unsubscribe_index_price(symbols)`
- `unsubscribe_mark_price(symbols)`

Use `ready=True` for normal event-driven strategies. For timer strategies, still guard cache reads with `if not self.ready: return`.

## Requests

These methods synchronously run public connector async requests through the task manager:

- `request_ticker(symbol, account_type=None) -> Ticker`
- `request_all_tickers(account_type) -> dict[str, Ticker]`
- `request_klines(symbol | list[str], interval, limit=None, start_time=None, end_time=None, account_type=None) -> KlineList`
- `request_index_klines(symbol | list[str], interval, limit=None, start_time=None, end_time=None, account_type=None) -> KlineList`

`start_time` and `end_time` may be `datetime`; they are converted to milliseconds.

## Precision And Market Helpers

- `market(symbol) -> BaseMarket`
- `tick_sz(symbol) -> float`
- `lot_sz(symbol) -> float`
- `min_order_amount(symbol, px=None) -> Decimal`
- `amount_to_precision(symbol, amount, mode="round") -> Decimal`
- `price_to_precision(symbol, price, mode="round") -> Decimal`
- `linear_info(exchange, base=None, quote=None, exclude=None) -> list[str]`
- `spot_info(exchange, base=None, quote=None, exclude=None) -> list[str]`
- `future_info(exchange, base=None, quote=None, exclude=None) -> list[str]`
- `inverse_info(exchange, base=None, quote=None, exclude=None) -> list[str]`

`min_order_amount` needs either `px` or cached `bookl1(symbol)` so it can evaluate cost-based minimums.

## Orders

Single order:

- `create_order(symbol, side, type, amount, price=None, time_in_force=TimeInForce.GTC, reduce_only=False, account_type=None, **kwargs) -> str`
- `create_order_ws(symbol, side, type, amount, price=None, time_in_force=TimeInForce.GTC, reduce_only=False, account_type=None, **kwargs) -> str`

Cancellation:

- `cancel_order(symbol, oid, account_type=None, **kwargs) -> str`
- `cancel_order_ws(symbol, oid, account_type=None, **kwargs) -> str`
- `cancel_all_orders(symbol, account_type=None) -> str`

Batch:

- `create_batch_orders(orders: list[BatchOrder], account_type=None) -> list[str]`
- `cancel_batch_orders(orders: list[CancelBatchOrder], account_type=None) -> list[str]`

Modify:

- `modify_order(symbol, oid, side, price, amount, account_type=None, **kwargs) -> str`
- `side`, `price`, and `amount` are required.

TP/SL:

- `create_tp_sl_order(symbol, side, type, amount, price=None, time_in_force=TimeInForce.GTC, tp_order_type=None, tp_trigger_price=None, tp_price=None, tp_trigger_type=TriggerType.LAST_PRICE, sl_order_type=None, sl_trigger_price=None, sl_price=None, sl_trigger_type=TriggerType.LAST_PRICE, account_type=None, **kwargs) -> str`
- If a TP trigger price is set, `tp_order_type` is required.
- If an SL trigger price is set, `sl_order_type` is required.

Execution algorithm order:

- `create_algo_order(symbol, side, amount, exec_algorithm_id, exec_params, reduce_only=False, account_type=None) -> str`
- `cancel_algo_order(oid, exec_algorithm_id)`
- `get_algo_order(oid, exec_algorithm_id) -> ExecAlgorithmOrder | None`

Order coding rules:

- Use `Decimal("...")` for amounts and direct numeric order inputs.
- Use `price_to_precision` for prices before limit/post-only submission.
- Use `amount_to_precision` or `min_order_amount` for sizes.
- Store returned order IDs when later cancellation, modification, or state tracking is needed.
- Use `self.cache.get_open_orders(symbol=...)` or stored IDs to avoid duplicate live orders.
- Use `create_order_ws` and `cancel_order_ws` when the exchange example uses websocket trading.

## Scheduling, Timers, Waiting, And Stop

APScheduler wrapper:

- `schedule(func, trigger="interval", **kwargs)`
- Triggers: `"interval"`, `"cron"`, `"date"`.
- Interval kwargs: `seconds`, `minutes`, `hours`, `days`, `weeks`.
- Cron kwargs: `second`, `minute`, `hour`, `day`, `month`, `year`.
- Date kwargs: `run_date`.
- Pass callback args with `args=(...)` and `kwargs={...}`.

Clock timer:

- `set_timer(callback, interval: timedelta, name=None, start_time=None, stop_time=None)`

Other:

- `wait(seconds=0, milliseconds=0, microseconds=0)` uses high-precision sleep.
- `stop()` sends SIGINT after a short wait so queued messages can process.

## Params

Strategy parameter helpers use `self.cache` and support memory or Redis:

- `param(name, value=None, default=None, backend="memory")`
- `clear_param(name=None, backend="memory")`

Examples:

```python
self.param("mode", "normal")
mode = self.param("mode", default="normal")
self.param("signal", {"BTCUSDT-PERP.BINANCE": 0.01}, backend="redis")
self.clear_param("signal")
```

Redis requires Redis to be running and configured.

## Direct API And Alerts

Private connector API proxy:

- `api(account_type)` returns a synchronous proxy to the private API client.
- `api_fire(account_type)` returns a fire-and-forget API proxy.

Alerts:

- `send_alert(event_status, title_rule, alert_key=None, description=None, labels=None, images=None)`
- `alert_ok(...)`
- `alert_info(...)`
- `alert_warning(...)`
- `alert_critical(...)`

`Config.flashduty_integration_key` must be set for FlashDuty delivery.
