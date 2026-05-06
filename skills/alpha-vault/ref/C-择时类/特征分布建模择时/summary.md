# 特征分布建模择时

- Category: `C-择时类`
- Bundle Dir: `特征分布建模择时`

## Primary Summary

- Notebook: `source/特征分布择时-10cedaa2.ipynb`

# 数据准备

# 信号构造

1. 取得2013年1月4日至2022年2月22日之间沪深两市龙虎榜的数据,选取其中上榜席位为机构席位的信息,并计算当日所有单个席位净流入金额(单个席位买入金额-单个席位卖出金额)的总和,记为全市场机构席位绝对净流入额**IS_NetBuy**;
2. 为了使不同交易日之间的IS_NetBuy可比,在本文对IS_NetBuy做了两市成交额中性化处理即**IS_NetBuy/沪深300指数当日成交金额**，得到全市场机构席位净流入强度**IS_NetBuy_S**,即相对净流入;
3. IS_NetBuy_S就是我们需要分析的择时因子,我们希望能得到可能存在的非线性关系,我们进而绘制出IS_NetBuy_S的期望收益分布图，即计算每日IS_NetBuy_S数据对应的后10日沪深300指数涨跌幅情况,对所得结果按照 **IS_NetBuy_S**从小到大进行排序

## 席位分析期望收益分布

## Notebooks

### `source/特征分布择时-10cedaa2.ipynb`

# 数据准备

# 信号构造

1. 取得2013年1月4日至2022年2月22日之间沪深两市龙虎榜的数据,选取其中上榜席位为机构席位的信息,并计算当日所有单个席位净流入金额(单个席位买入金额-单个席位卖出金额)的总和,记为全市场机构席位绝对净流入额**IS_NetBuy**;
2. 为了使不同交易日之间的IS_NetBuy可比,在本文对IS_NetBuy做了两市成交额中性化处理即**IS_NetBuy/沪深300指数当日成交金额**，得到全市场机构席位净流入强度**IS_NetBuy_S**,即相对净流入;
3. IS_NetBuy_S就是我们需要分析的择时因子,我们希望能得到可能存在的非线性关系,我们进而绘制出IS_NetBuy_S的期望收益分布图，即计算每日IS_NetBuy_S数据对应的后10日沪深300指数涨跌幅情况,对所得结果按照 **IS_NetBuy_S**从小到大进行排序

## 席位分析期望收益分布

## Code Implementation

- `source/__init__-370ddbf0.py`
- `source/get_data-c2e73802.py`
  - Symbols: `check_query_date_params, wrapper, offset_limit, decorator, wrapper, distributed_query, _prepare_format, _check_query_date_params, get_sales_depart_billboard, get_index_daily`
- `source/__init__-7fee6581.py`
- `source/bt_func-414b9ae7.py`
  - Symbols: `netbuy_cross, log, __init__, next, notify_order, add_pandas_data, add_quantile_data, trade_list, __init__, notify_trade, get_analysis, get_backtesting`
- `source/calc_func-5d5320f9.py`
  - Symbols: `HMA, get_exchange_set, calc_netbuy`
- `source/load_config-7e388bbe.py`
- `source/plotting-aa0d93d7.py`
  - Symbols: `plot_indicator, plot_qunatile_signal, plot_hist2d, plot_quantile_group_ret, plot_distribution, plot_trade_flag, plot_algorithm_nav, plot_drawdowns, plot_trade_pnl, plot_underwater, plot_cumulative_returns, plot_orders_on_price`
- `source/timeseries-42ae628a.py`
  - Symbols: `get_max_drawdown_underwater, get_top_drawdowns, get_drawdown_table`
- `source/ts_trade_days-f6a8a04b.py`
  - Symbols: `get_all_trade_days, create_cal, get_trade_days, Tdaysoffset`
- `source/tushare_api-d372f910.py`
  - Symbols: `TuShare, __init__, __getattr__, wrapper`
- `source/utils-272b971a.py`
  - Symbols: `trans2strftime, format_dt, print_table`
