# Source Map

Use this file to decide what to inspect before writing or changing a strategy. If WalrasQuant is installed from pip and no repo source is available, inspect the installed package in site-packages or use the concrete references bundled in this skill.

## Framework Source Or Installed Package Modules

- `src/walrasquant/strategy.py`: `Strategy` lifecycle and all strategy-facing helpers.
- `src/walrasquant/config.py`: `Config`, `BasicConfig`, `PublicConnectorConfig`, `PrivateConnectorConfig`, `LogConfig`, `ZeroMQSignalConfig`, `WebConfig`, `QueueConfig`.
- `src/walrasquant/engine.py`: engine build/start/dispose flow, execution algorithm registration, web app binding, connection policy.
- `src/walrasquant/constants.py`: common enums: `ExchangeType`, `OrderSide`, `OrderType`, `TimeInForce`, `TriggerType`, `BookLevel`, `KlineInterval`, `DataType`, `StorageType`, `ParamBackend`.
- `src/walrasquant/schema.py`: strategy data models: `BookL1`, `BookL2`, `Trade`, `Kline`, `FundingRate`, `IndexPrice`, `MarkPrice`, `Ticker`, `Order`, `Position`, `BatchOrder`, `CancelBatchOrder`, `KlineList`.
- `src/walrasquant/core/cache.py`: cache read APIs and parameter storage used by strategies.
- `src/walrasquant/indicator.py`: `Indicator`, `IndicatorProxy`, `RingBuffer`, warmup mechanics.
- `src/walrasquant/execution/algorithm.py`: custom execution algorithm base class.
- `src/walrasquant/execution/algorithms/twap.py`: bundled `TWAPExecAlgorithm`.
- `src/walrasquant/web/app.py`: strategy-aware FastAPI callbacks.

## Exchange Source

- `src/walrasquant/exchange/__init__.py`: exports account type enums.
- `src/walrasquant/exchange/binance/constants.py`: `BinanceAccountType`.
- `src/walrasquant/exchange/okx/constants.py`: `OkxAccountType`.
- `src/walrasquant/exchange/bybit/constants.py`: `BybitAccountType`.
- `src/walrasquant/exchange/bitget/constants.py`: `BitgetAccountType`.
- `src/walrasquant/exchange/hyperliquid/constants.py`: `HyperLiquidAccountType`.
- `src/walrasquant/exchange/*/exchange.py`: symbol to account-type mapping and public connector validation.
- `src/walrasquant/exchange/*/connector.py`: supported market data subscriptions and request helpers.
- `src/walrasquant/exchange/*/ems.py`: precision, min order amount, submit routing, REST vs WS support.
- `src/walrasquant/exchange/*/oms.py`: order status parsing, websocket order responses, account/position/balance events.

## Example Strategy Files

- Basic order/cancel: `strategy/okx/buy_and_cancel.py`, `strategy/binance/buy_and_cancel.py`, `strategy/bybit/buy_and_cancel.py`, `strategy/bitget/buy_and_sell.py`, `strategy/hyperliquid/buy_and_cancel.py`.
- Websocket order path: Bybit, Bitget, Hyperliquid examples use `create_order_ws` and `cancel_order_ws`.
- Batch orders: `strategy/*/place_batch_orders.py`, `strategy/*/buy_and_batch_cancel.py`.
- Order modification: `strategy/*/modify_order.py`.
- Cancel all: `strategy/*/cancel_all_orders.py`.
- Kline subscription and request: `strategy/*/subscribe_klines.py`, `strategy/*/request_klines.py`.
- Book level 2: `strategy/okx/subscribe_bookl2.py`, `strategy/bybit/subscribe_bookl2.py`.
- Funding rate: `strategy/*/subscribe_funding_rate.py`.
- Indicators: `strategy/bybit/demo_indicator.py`, `strategy/bybit/warmup_moving_average_example.py`, `strategy/okx/simple_mm.py`.
- Timer and waiting: `strategy/binance/sleep_demo.py`, `strategy/okx/simple_mm.py`.
- Custom signals: `strategy/*/signal_server.py`, `strategy/*/custom_signal.py`.
- Params: `strategy/binance/set_params.py`, `strategy/binance/use_params.py`.
- Alerts: `strategy/binance/send_alert.py`.
- FastAPI web callback: `strategy/binance/web_callback.py`.
- TWAP algorithm: `strategy/okx/place_twap_order.py`.
