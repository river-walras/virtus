# 特征分布建模择时系列之二

- Category: `C-择时类`
- Bundle Dir: `特征分布建模择时系列之二`

## Primary Summary

- Notebook: `source/特征分布建模择时系列之二-3a807a11.ipynb`

# 指标的构建

成交量使用的移动平均线为AMA(移动平均线长度为L)
$$量能指标=\frac{AMA5}{AMA100}$$

指标的具体逻辑可以看研报。

*最开始我的理解是先用移动平均算法计算volume,然后再将计算后的值放入量能指标中;后面发现华创习惯使用HMA,故直接将volume放入公式计算即可。*

- 划分时间
  - 样本内:即在2004-2019年中做研究
  - 样本外:即2020年以后作为测试

## 万得全A指数量能指标 5 个交易日的期望收益分布图

从万得全A的量能指标5日的期望收益分布图可以看出，与龙虎榜机构资金净流入强度指标的V型分布不同在于，量能指标的期望收益分布图呈现出明显的右偏V型形状，类似√型。
依旧是在两端做多,中间做空,其中阈值threahold=1.15(黑线,通过观察分布得出,但是分布于数据历史长度有关,随着窗口不同该参数可能在1.15附近移动),固定阈值1(绿色),尾部反转阈值为$threshold^{-a}$(青色,其中a为极值参数)。

_[embedded image omitted]_

## Notebooks

### `source/特征分布建模择时系列之二-3a807a11.ipynb`

# 指标的构建

成交量使用的移动平均线为AMA(移动平均线长度为L)
$$量能指标=\frac{AMA5}{AMA100}$$

指标的具体逻辑可以看研报。

*最开始我的理解是先用移动平均算法计算volume,然后再将计算后的值放入量能指标中;后面发现华创习惯使用HMA,故直接将volume放入公式计算即可。*

- 划分时间
  - 样本内:即在2004-2019年中做研究
  - 样本外:即2020年以后作为测试

## 万得全A指数量能指标 5 个交易日的期望收益分布图

从万得全A的量能指标5日的期望收益分布图可以看出，与龙虎榜机构资金净流入强度指标的V型分布不同在于，量能指标的期望收益分布图呈现出明显的右偏V型形状，类似√型。
依旧是在两端做多,中间做空,其中阈值threahold=1.15(黑线,通过观察分布得出,但是分布于数据历史长度有关,随着窗口不同该参数可能在1.15附近移动),固定阈值1(绿色),尾部反转阈值为$threshold^{-a}$(青色,其中a为极值参数)。

_[embedded image omitted]_

## Code Implementation

- `source/__init__-cb971926.py`
- `source/bt_func-ea62060f.py`
  - Symbols: `bimodal_distribution_strategy, log, __init__, next, notify_order, trade_list, __init__, notify_trade, get_analysis, StockCommission, _getcommission, get_backtesting`
- `source/calc_func-72bd17e2.py`
  - Symbols: `create_signal, HMA`
- `source/plotting-72197857.py`
  - Symbols: `plot_indicator, plot_qunatile_signal, plot_hist2d, plot_quantile_group_ret, get_distribution_data, get_ticks_from_index, plot_hist_signal_with_cum, plot_distribution, plot_trade_flag, plot_algorithm_nav, plot_drawdowns, plot_trade_pnl`
- `source/timeseries-dfa6f464.py`
  - Symbols: `get_max_drawdown_underwater, get_top_drawdowns, get_drawdown_table`
- `source/utils-0336860f.py`
  - Symbols: `trans2strftime, format_dt, print_table, get_value_frome_traderanalyzerdict`
