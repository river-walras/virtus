# Execution Algorithms, Web Callbacks, Signals, Alerts, And Processes

Sources: `src/walrasquant/execution/*`, `src/walrasquant/web/app.py`, `src/walrasquant/config.py`, `src/walrasquant/engine.py`.

## Built-In TWAP

Register the algorithm on the engine before `engine.start()`:

```python
from walrasquant.execution import TWAPExecAlgorithm

engine = Engine(config)
engine.add_exec_algorithm(algorithm=TWAPExecAlgorithm())
```

Create an algo order from a strategy:

```python
self.create_algo_order(
    symbol=self.symbol,
    side=OrderSide.BUY,
    amount=Decimal("2"),
    exec_algorithm_id="TWAP",
    exec_params={
        "horizon_secs": 100,
        "interval_secs": 10,
        "n_tick_sz": 1,
        "use_limit": True,
    },
    reduce_only=True,
)
```

TWAP required params:

- `horizon_secs`
- `interval_secs`

TWAP optional params:

- `use_limit=False`
- `n_tick_sz=0`

TWAP source behavior:

- Rejects missing required params.
- Rejects `horizon_secs < interval_secs`.
- Splits total amount by floor precision.
- Falls back to one full execution when slice size is below `min_order_amount`.
- In `use_limit` mode, reads `cache.bookl1(symbol)` and offsets by `n_tick_sz * tick_sz`.
- Uses market order fallback if no book data.

## Custom Execution Algorithms

Subclass `ExecAlgorithm` from `src/walrasquant/execution/algorithm.py` and implement:

```python
def on_order(self, exec_order: ExecAlgorithmOrder):
    ...
```

Useful inherited methods:

- `spawn_market(exec_order, quantity, time_in_force=TimeInForce.GTC, reduce_only=None, **kwargs)`
- `spawn_market_ws(...)`
- `spawn_limit(exec_order, quantity, price, time_in_force=TimeInForce.GTC, reduce_only=None, post_only=False, **kwargs)`
- `spawn_limit_ws(...)`
- `spawn_batch_orders(exec_order, orders)`
- `cancel_spawned_order(exec_order, spawned_oid)`
- `cancel_spawned_order_ws(exec_order, spawned_oid, **kwargs)`
- `get_algo_order(primary_oid)`
- `mark_complete(exec_order)`
- `set_timer(name, interval, callback, start_time=None, stop_time=None)`
- `cancel_timer(name)`
- `amount_to_precision`, `price_to_precision`, `min_order_amount`, `tick_sz`, `lot_sz`, `cache`, `get_market`.

Optional hooks:

- `on_start`, `on_stop`, `on_reset`, `on_cancel`
- `on_spawned_order_pending`, `on_spawned_order_accepted`, `on_spawned_order_partially_filled`, `on_spawned_order_filled`, `on_spawned_order_canceled`, `on_spawned_order_failed`
- `on_execution_complete`

`ExecAlgorithmConfig` fields:

- `exec_algorithm_id=None`
- `log_events=True`
- `log_commands=True`

## ZeroMQ Custom Signals

Receiver config:

```python
import zmq
from zmq.asyncio import Context
from walrasquant.config import ZeroMQSignalConfig

context = Context()
socket = context.socket(zmq.SUB)
socket.connect("ipc:///tmp/zmq_data_test")
socket.setsockopt(zmq.SUBSCRIBE, b"")

config = Config(
    ...,
    zero_mq_signal_config=ZeroMQSignalConfig(socket=socket),
)
```

Strategy:

```python
def on_custom_signal(self, signal):
    self.log.info(f"signal={signal}")
```

`Engine` raises an `EngineBuildError` if `zero_mq_signal_config` is set and the strategy has no `on_custom_signal`.

## FastAPI Strategy Callbacks

Use `create_strategy_app` from `walrasquant.web`.

```python
from typing import Any
from walrasquant.web import create_strategy_app

class WebStrategy(Strategy):
    web_app = create_strategy_app(title="Strategy Callback")

    def __init__(self):
        super().__init__()
        self.signal_enabled = False

    @web_app.post("/toggle")
    def on_web_cb(self, payload: dict[str, Any]) -> dict[str, Any]:
        self.signal_enabled = payload.get("enabled", not self.signal_enabled)
        self.log.info(f"payload={payload}")
        return {"enabled": self.signal_enabled}
```

Config:

```python
from walrasquant.config import WebConfig

config = Config(
    ...,
    web_config=WebConfig(enabled=True, host="127.0.0.1", port=6666, log_level="error"),
)
```

Notes:

- Current `Strategy.__init_subclass__` rejects coroutine methods defined on the strategy class. Use synchronous `def` for web callbacks unless the framework source is changed.
- `StrategyFastAPI` can wrap async endpoints in general, but the strategy subclass guard currently prevents async strategy methods.
- `Engine` starts the web interface only if `web_config.enabled` and user routes exist.

## Alerts

Config:

```python
config = Config(
    ...,
    flashduty_integration_key=settings.config.flashduty_key,
)
```

Strategy:

```python
self.alert_info("message title", "dedupe:key")
self.alert_warning("warning title", alert_key="risk:warning")
self.alert_ok("recovered", alert_key="risk:warning")
self.alert_critical("critical title", description="details")
```

## Direct API Calls

Use sparingly and prefer strategy helpers for normal trading:

```python
res = self.api(OkxAccountType.LIVE).get_api_v5_finance_staking_defi_offers(ccy="SOL")
self.api_fire(account_type).some_private_call(...)
```

`api` and `api_fire` access private connectors, so the corresponding private connector must exist in `Config.private_conn_config`.

## Process Commands

Common `wq` process commands:

```bash
wq start strategy/okx/buy_and_cancel.py
wq start strategy/okx/buy_and_cancel.py -s okx_buy_and_sell -u user_test
wq ls
wq log okx_buy_and_sell.user_test
wq log okx_buy_and_sell.user_test -F
wq log okx_buy_and_sell.user_test -d 3
wq stop okx_buy_and_sell.user_test
wq restart okx_buy_and_sell.user_test
wq delete okx_buy_and_sell.user_test
```

Do not start live processes unless the user explicitly asks.
