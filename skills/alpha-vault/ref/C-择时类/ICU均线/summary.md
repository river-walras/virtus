# ICU均线

- Category: `C-择时类`
- Bundle Dir: `ICU均线`

## Primary Summary

- Notebook: `source/ICU_MA-3a3acc3b.ipynb`

# ICU均线构造

中泰写的有点绕，应该是使用**重复中位数（RM）下的稳健回归**

与研报给出的构造对比

![avatar](img/ma.png)

# 回测

开仓条件

价格上穿短期 ICU 均线则买入，当价格从上往下穿均线时卖出平仓

$$\begin{cases} Buy_{t}\ if\ Price_{t} > ICUMVG_{t}\ and\ Price_{t-1} < ICUMVG_{t-1} \\
sell_{t}\ if\ Price_{t} < ICUMVG_{t}\ and\ Price_{t-1} > ICUMVG_{t-1}\end{cases}$$

以沪深 300 绝对收益择时策略为例，展示计算流程：
1. 利用过去5个交易日数据滚动计算ICU均线
2. **每日临近收盘计算交易信号，出现信号立刻以收盘价买入.**

但这里我们使用backtrader框架进行寻参

回测设置
1. 滑点万1
2. 双边手续费,佣金万3,印花税千1
3. 根据研报给出的回测规则T日信号T日close买入

## Notebooks

### `source/ICU_MA-3a3acc3b.ipynb`

# ICU均线构造

中泰写的有点绕，应该是使用**重复中位数（RM）下的稳健回归**

与研报给出的构造对比

![avatar](img/ma.png)

# 回测

开仓条件

价格上穿短期 ICU 均线则买入，当价格从上往下穿均线时卖出平仓

$$\begin{cases} Buy_{t}\ if\ Price_{t} > ICUMVG_{t}\ and\ Price_{t-1} < ICUMVG_{t-1} \\
sell_{t}\ if\ Price_{t} < ICUMVG_{t}\ and\ Price_{t-1} > ICUMVG_{t-1}\end{cases}$$

以沪深 300 绝对收益择时策略为例，展示计算流程：
1. 利用过去5个交易日数据滚动计算ICU均线
2. **每日临近收盘计算交易信号，出现信号立刻以收盘价买入.**

但这里我们使用backtrader框架进行寻参

回测设置
1. 滑点万1
2. 双边手续费,佣金万3,印花税千1
3. 根据研报给出的回测规则T日信号T日close买入

## Code Implementation

- `source/__init__-9d62c3dc.py`
- `source/backtest-a386442a.py`
  - Symbols: `add_price, StockCommission, _getcommission, get_backtest, runstrat, _get_rets`
- `source/bt_icu_ind-f2b19d65.py`
  - Symbols: `IcuMaInd, __init__, next`
- `source/bt_strategy-80829277.py`
  - Symbols: `CrossOverStrategy, log, __init__, next, notify_order`
- `source/icu_ma-ba44e475.py`
  - Symbols: `siegelslopes_ma, calc_icu_ma`
