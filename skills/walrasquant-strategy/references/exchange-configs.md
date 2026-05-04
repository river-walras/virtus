# Exchange Config Reference

Sources: `src/walrasquant/config.py`, `src/walrasquant/exchange/*/constants.py`, and examples under `strategy/`.

## Config Classes

```python
from walrasquant.config import (
    BasicConfig,
    Config,
    LogConfig,
    PrivateConnectorConfig,
    PublicConnectorConfig,
    QueueConfig,
    WebConfig,
    ZeroMQSignalConfig,
)
```

`BasicConfig`:

- `api_key=None`
- `secret=None`
- `testnet=False`
- `passphrase=None`
- Hyperliquid note from source: `api_key` is the real wallet address; `secret` is the agent private key.

`PublicConnectorConfig`:

- `account_type`
- `enable_rate_limit=True`
- `custom_url=None`
- `max_subscriptions_per_client=None`
- `max_clients=None`

`PrivateConnectorConfig`:

- `account_type`
- `enable_rate_limit=True`
- `max_retries=0`
- `delay_initial_ms=100`
- `delay_max_ms=800`
- `backoff_factor=2`
- `max_slippage=0.02`
- `max_subscriptions_per_client=None`
- `max_clients=None`

`LogConfig`:

- `filename=None`; if omitted, `Config.__post_init__` creates `logs/<strategy_id>_<user_id>.log`.
- `level`: `TRACE`, `DEBUG`, `INFO`, `WARNING`, or `ERROR`.
- `name_levels`: optional per-logger overrides.
- `unix_ts=False`, `batch_size=1`.

`Config` required fields:

- `strategy_id`
- `user_id`
- `strategy`
- `basic_config`
- `public_conn_config`

`Config` optional fields:

- `private_conn_config={}`
- `zero_mq_signal_config=None`
- `db_path=".keys/cache.db"`
- `storage_backend=StorageType.SQLITE`
- `cache_sync_interval=60`
- `cache_expired_time=3600`
- `log_config=LogConfig()`
- `web_config=WebConfig()`
- `exit_after_cancel=True`
- `flashduty_integration_key=None`
- `queue_config=QueueConfig(ems_maxsize=100000, sms_maxsize=100000)`

## Secrets And Settings

`walrasquant.constants.settings` loads from:

- `.keys/.secrets.toml`
- `.keys/.secrets.yaml`
- `.keys/.secrets.yml`
- `.keys/settings.toml`
- `.keys/settings.yaml`
- `.keys/settings.yml`

If no secrets file exists outside a Sphinx build, importing `walrasquant.constants` raises `FileNotFoundError`. Strategy files should reference `settings`, not hard-code credentials.

## Exchange Account Types

Import account types from `walrasquant.exchange`.

```python
from walrasquant.exchange import (
    BinanceAccountType,
    BitgetAccountType,
    BybitAccountType,
    HyperLiquidAccountType,
    OkxAccountType,
)
```

OKX:

- Account types: `OkxAccountType.LIVE`, `OkxAccountType.DEMO`.
- `DEMO.is_testnet` is true.
- Demo examples use `settings.OKX.DEMO_1.API_KEY`, `.SECRET`, `.PASSPHRASE`.
- Symbols: `BTCUSDT.OKX`, `BTCUSDT-PERP.OKX`, `SOLUSDT-PERP.OKX`.

Binance:

- Account types: `SPOT`, `MARGIN`, `ISOLATED_MARGIN`, `USD_M_FUTURE`, `COIN_M_FUTURE`, `PORTFOLIO_MARGIN`, `SPOT_TESTNET`, `USD_M_FUTURE_TESTNET`, `COIN_M_FUTURE_TESTNET`.
- Testnet account types are the three `*_TESTNET` values.
- Spot examples use `settings.BINANCE.DEMO.API_KEY` and `BinanceAccountType.SPOT_TESTNET`.
- Futures examples use `settings.BINANCE.FUTURE.TESTNET_1.API_KEY` and `BinanceAccountType.USD_M_FUTURE_TESTNET`.
- Symbols: `BTCUSDT.BINANCE`, `BTCUSDT-PERP.BINANCE`.

Bybit:

- Account types: `SPOT`, `LINEAR`, `INVERSE`, `OPTION`, their `*_TESTNET` variants, `UNIFIED`, `UNIFIED_TESTNET`.
- Public linear testnet examples use `BybitAccountType.LINEAR_TESTNET`.
- Private testnet examples often use `BybitAccountType.UNIFIED_TESTNET`.
- Live linear example uses public `BybitAccountType.LINEAR` and private `BybitAccountType.UNIFIED`.
- Symbols: `BTCUSDT-PERP.BYBIT`, `UNIUSDT-PERP.BYBIT`.

Bitget:

- Account types: `UTA`, `SPOT`, `FUTURE`, `UTA_DEMO`, `SPOT_DEMO`, `FUTURE_DEMO`.
- Demo examples use `settings.BITGET.DEMO.API_KEY`, `.SECRET`, `.PASSPHRASE` and `BitgetAccountType.UTA_DEMO`.
- Symbols: `BTCUSDT-PERP.BITGET`.

Hyperliquid:

- Account types: `HyperLiquidAccountType.MAINNET`, `HyperLiquidAccountType.TESTNET`.
- Testnet examples use `settings.HYPER.TESTNET.API_KEY`, `.SECRET`.
- Symbols: `BTCUSDC-PERP.HYPERLIQUID`.

## Config Templates

OKX demo:

```python
config = Config(
    strategy_id="okx_demo",
    user_id="user_test",
    strategy=Demo(),
    basic_config={
        ExchangeType.OKX: BasicConfig(
            api_key=settings.OKX.DEMO_1.API_KEY,
            secret=settings.OKX.DEMO_1.SECRET,
            passphrase=settings.OKX.DEMO_1.PASSPHRASE,
            testnet=True,
        )
    },
    public_conn_config={
        ExchangeType.OKX: [PublicConnectorConfig(account_type=OkxAccountType.DEMO)]
    },
    private_conn_config={
        ExchangeType.OKX: [PrivateConnectorConfig(account_type=OkxAccountType.DEMO)]
    },
)
```

Binance USD-M futures testnet:

```python
config = Config(
    strategy_id="binance_usdm_demo",
    user_id="user_test",
    strategy=Demo(),
    basic_config={
        ExchangeType.BINANCE: BasicConfig(
            api_key=settings.BINANCE.FUTURE.TESTNET_1.API_KEY,
            secret=settings.BINANCE.FUTURE.TESTNET_1.SECRET,
            testnet=True,
        )
    },
    public_conn_config={
        ExchangeType.BINANCE: [
            PublicConnectorConfig(account_type=BinanceAccountType.USD_M_FUTURE_TESTNET)
        ]
    },
    private_conn_config={
        ExchangeType.BINANCE: [
            PrivateConnectorConfig(account_type=BinanceAccountType.USD_M_FUTURE_TESTNET)
        ]
    },
)
```

Bybit linear testnet with unified private connector:

```python
config = Config(
    strategy_id="bybit_demo",
    user_id="user_test",
    strategy=Demo(),
    basic_config={
        ExchangeType.BYBIT: BasicConfig(
            api_key=settings.BYBIT.TESTNET.API_KEY,
            secret=settings.BYBIT.TESTNET.SECRET,
            testnet=True,
        )
    },
    public_conn_config={
        ExchangeType.BYBIT: [
            PublicConnectorConfig(account_type=BybitAccountType.LINEAR_TESTNET)
        ]
    },
    private_conn_config={
        ExchangeType.BYBIT: [
            PrivateConnectorConfig(account_type=BybitAccountType.UNIFIED_TESTNET)
        ]
    },
)
```

Read the closest existing exchange example before choosing account types.
