# Schema, Cache, Constants, And Indicators

Sources: `src/walrasquant/schema.py`, `src/walrasquant/core/cache.py`, `src/walrasquant/constants.py`, `src/walrasquant/indicator.py`.

## Symbols And Instrument IDs

WalrasQuant symbols are strings ending with an exchange suffix:

- Spot: `BTCUSDT.BINANCE`, `BTCUSDT.OKX`.
- Linear perp or future: `BTCUSDT-PERP.BINANCE`, `BTCUSDT-PERP.OKX`, `BTCUSDT-PERP.BYBIT`, `BTCUSDT-PERP.BITGET`.
- Hyperliquid perp example: `BTCUSDC-PERP.HYPERLIQUID`.
- `InstrumentId.from_str(symbol)` splits the symbol into `id`, `symbol`, `exchange`, and `type`.
- If the symbol prefix contains `-` and the prefix before the dash ends with `USD`, type is inverse; otherwise with `-` it is linear; without `-` it is spot.

## Common Constants

```python
from walrasquant.constants import (
    BookLevel,
    DataType,
    ExchangeType,
    KlineInterval,
    OrderSide,
    OrderType,
    ParamBackend,
    StorageType,
    TimeInForce,
    TriggerType,
)
```

Core enum values:

- `ExchangeType`: `BINANCE`, `OKX`, `BYBIT`, `HYPERLIQUID`, `BITGET`.
- `OrderSide`: `BUY`, `SELL`.
- `OrderType`: `MARKET`, `LIMIT`, `TAKE_PROFIT_MARKET`, `TAKE_PROFIT_LIMIT`, `STOP_LOSS_MARKET`, `STOP_LOSS_LIMIT`, `POST_ONLY`.
- `TimeInForce`: `GTC`, `IOC`, `FOK`.
- `TriggerType`: `LAST_PRICE`, `MARK_PRICE`, `INDEX_PRICE`.
- `BookLevel`: `L5`, `L10`, `L20`, `L50`, `L200`, `L400`, `L1000`.
- `DataType`: `BOOKL1`, `BOOKL2`, `TRADE`, `KLINE`, `VOLUME_KLINE`, `MARK_PRICE`, `FUNDING_RATE`, `INDEX_PRICE`.
- `StorageType`: `SQLITE`, `POSTGRESQL`, `MEMORY`.
- `ParamBackend`: `MEMORY`, `REDIS`.

`KlineInterval` values:

- `SECOND_1`, `MINUTE_1`, `MINUTE_3`, `MINUTE_5`, `MINUTE_15`, `MINUTE_30`
- `HOUR_1`, `HOUR_2`, `HOUR_4`, `HOUR_6`, `HOUR_8`, `HOUR_12`
- `DAY_1`, `DAY_3`, `WEEK_1`, `MONTH_1`, `VOLUME`
- Each interval exposes `.seconds`, `.milliseconds`, `.microseconds`, `.nanoseconds`.

## Market Data Models

`BookL1` fields:

- `exchange`, `symbol`, `bid`, `ask`, `bid_size`, `ask_size`, `timestamp`.
- Properties: `mid`, `spread`, `weighted_mid`.

`BookL2` fields:

- `exchange`, `symbol`, `bids`, `asks`, `timestamp`.
- `bids` and `asks` contain `BookOrderData(price, size)`.
- Properties: `mid`, `spread`, `best_bid`, `best_ask`, `best_bid_size`, `best_ask_size`, `weighted_mid`.

Other data:

- `Trade`: `exchange`, `side`, `symbol`, `price`, `size`, `timestamp`.
- `Kline`: `exchange`, `symbol`, `interval`, `open`, `high`, `low`, `close`, optional volume fields, `start`, `timestamp`, `confirm`.
- `FundingRate`: `exchange`, `symbol`, `rate`, `timestamp`, `next_funding_time`.
- `IndexPrice`: `exchange`, `symbol`, `price`, `timestamp`.
- `MarkPrice`: `exchange`, `symbol`, `price`, `timestamp`.
- `Ticker`: `exchange`, `symbol`, `last_price`, `timestamp`, `volume`, `volumeCcy`.

`KlineList`:

- Returned by `request_klines` and `request_index_klines`.
- `.values` returns klines sorted by timestamp.
- `.df` returns a pandas DataFrame indexed by UTC date.

## Orders And Positions

`Order` important fields:

- `exchange`, `symbol`, `status`, `oid`, `eid`, `amount`, `filled`, `timestamp`, `type`, `side`, `time_in_force`, `price`, `trigger_price`, `average`, `last_filled_price`, `last_filled`, `remaining`, `fee`, `fee_currency`, `cost`, `cum_cost`, `reduce_only`, `position_side`, `reason`.

`Order` properties:

- Status: `success`, `is_filled`, `is_pending`, `is_accepted`, `is_partially_filled`, `is_partially_canceled`, `is_canceling`, `is_cancel_failed`, `is_canceled`, `is_expired`, `is_closed`, `is_opened`, `on_flight`.
- Side/type: `is_buy`, `is_sell`, `is_maker`, `is_taker`, `is_post_only`, `is_ioc`, `is_fok`, `is_gtc`.
- WalrasQuant uses `canceled` with one `l`: `OrderStatus.CANCELED`, `order.is_canceled`, and `on_canceled_order`. Do not use `cancelled` spellings in strategy code.

`Position` fields and properties:

- Fields: `symbol`, `exchange`, `signed_amount`, `entry_price`, `side`, `unrealized_pnl`, `realized_pnl`.
- Properties: `amount`, `is_opened`, `is_closed`, `is_long`, `is_short`.

`BatchOrder`:

- `symbol`, `side`, `type`, `amount`, optional `price`, `time_in_force`, `reduce_only`, `kwargs`.

`CancelBatchOrder`:

- `symbol`, `oid`, `kwargs`.

## Cache Reads

Public data:

- `self.cache.bookl1(symbol) -> BookL1 | None`
- `self.cache.bookl2(symbol) -> BookL2 | None`
- `self.cache.trade(symbol) -> Trade | None`
- `self.cache.kline(symbol, interval) -> Kline | None`
- `self.cache.funding_rate(symbol) -> FundingRate | None`
- `self.cache.index_price(symbol) -> IndexPrice | None`
- `self.cache.mark_price(symbol) -> MarkPrice | None`

Private data:

- `self.cache.get_position(symbol).value_or(None) -> Position | None`
- `self.cache.get_all_positions(exchange=None) -> dict[str, Position]`
- `self.cache.get_order(oid).value_or(None) -> Order | None`
- `self.cache.get_symbol_orders(symbol, in_mem=True) -> set[str]`
- `self.cache.get_open_orders(symbol=None, exchange=None, include_canceling=False) -> set[str]`
- `self.cache.get_balance(account_type) -> AccountBalance`
- `self.cache.get_inflight_orders(symbol) -> set[str]`

Open-order reads require either `symbol` or `exchange`. By default `get_open_orders` excludes orders already marked with cancel intent.

Parameter storage:

- `get_param(key, default=None, param_backend=ParamBackend.MEMORY)`
- `set_param(key, value, param_backend=ParamBackend.MEMORY)`
- `get_all_params(param_backend=ParamBackend.MEMORY)`
- `clear_param(key=None, param_backend=ParamBackend.MEMORY)`
- `redis` property exposes a Redis client after availability check.

## Indicator Base Class

`Indicator` constructor:

```python
Indicator(params=None, name=None, warmup_period=None, kline_interval=None)
```

Name rules:

- Valid Python identifier.
- Must not start with `_`.
- Must not be a Python keyword.
- Must match letters, digits, and underscores, starting with a letter.

Implement handlers as needed:

- `handle_bookl1(self, bookl1)`
- `handle_bookl2(self, bookl2)`
- `handle_kline(self, kline)`
- `handle_trade(self, trade)`
- `handle_index_price(self, index_price)`
- `handle_funding_rate(self, funding_rate)`
- `handle_mark_price(self, mark_price)`
- `value` property.

Warmup:

- `requires_warmup` is true when both `warmup_period` and `kline_interval` are set.
- `is_warmed_up` is true after enough historical confirmed klines are processed.
- `Strategy.register_indicator` automatically deep-copies the indicator per symbol and performs kline warmup when needed.
- Access registered indicators as `self.indicator.<indicator_name>[symbol]`.

`RingBuffer`:

- `RingBuffer(length)`
- `append(val)`
- `get_as_numpy_array()`
- `get_last_value()`
- `is_full` flag.
