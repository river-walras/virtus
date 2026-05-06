# 另类ETF交易策略：日内动量

- Category: `C-择时类`
- Bundle Dir: `另类ETF交易策略-日内动量`

## Primary Summary

- Notebook: `source/etf_mom_strategy-2c632e29.ipynb`

# 引言

自 1993 年 Jegadeesh 和 Titman 提出并证明动量效应以来, 动量策略被广泛研究与应用。随着高频数据可获得性的增加以及相关技术的进步, 对动量效应的研究也逐渐拓展到日内领域，并被证明同样存在。

学术界对动量效应存在的原因至今仍有诸多争议, 但较有说服力的解释之一是价格对新信息的反应不足。即, 需要一定的时间逐步消化和反应新信息, 从而形成动量。造成反应不足的原因可能有,

1. 处置效应, 即卖出盈利头寸而继续持有亏损头寸。这种行为产生的资金流动可能会减缓利好（利空）消息后，股价的抬升（下跌）速度。

2. 投资者的注意力有限, 或是获取信息的成本较高。

3. 无法快速交易导致价格发现的速度变慢。

Zarattini C, Aziz A 和 Barbon A 在论文《Beat the Market: An Effective Intraday Momentum Strategy for S&P500 ETF (SPY)》中介绍了一种由粘性供需失衡（sticky demand/supply imbalances) 引起的日内动量效应, 并以此为基础, 设计了一个简洁而明确的 ETF 交易策略。本文参考其逻辑，对上证 50、沪深 300、中证 500、中证 1000 进行测试, 发现了相同的规律。

# 数据获取

# 信号构造


## 噪声区域

日内动量策略通常源自买卖双方的力量在一段时间内, 存在持续且显著的不平衡。但由于股票市场的噪声水平较高, 故我们需要定义一个买卖双方力量平衡时, 价格的正常波动区域, 并称之为噪声区域。若价格在噪声区域中波动, 则认为不存在日内趋势。

一种合理的假设是, 当日内走势接近过去若干天相同时间段的平均走势, 则可以认为市场处于供需平衡状态。由此，我们可按如下步骤定义 $\mathrm{t}$ 日的噪声区域。

1. 计算过去 14 天每个分钟时点 hh:mm 的价格位移 (相对开盘价的收益率绝对值):

$$
{\text{ move }}_{t - i,9 : {30} \sim {hh} : {mm}} = \left| {\frac{{\text{ close }}_{t - i,{hh} : {mm}}}{{\text{ open }}_{t - i,9 : {30}}} - 1}\right| ,\;i = 1 \sim {14}
$$

2. 取过去 14 天 hh:mm 时点的位移平均值:

$$
{\sigma }_{t - i,9 : {30} \sim {hh} : {mm}} = \frac{1}{14}\mathop{\sum }\limits_{{i = 1}}^{{14}}{\text{ move }}_{t - i,9 : {30} \sim {hh} : {mm}}
$$

3. 考虑到隔夜跳空缺口往往也预示着某种供需失衡, 因此进一步结合昨收盘价, 将 $\mathrm{t}$ 日 hh:mm 时点的噪声区域的上、下边界分别定义为:

$$
{\text{ UpperBound }}_{t,{hh} : {mm}} = \max \left( {{\text{ open }}_{t,9 : {30}},{\text{ close }}_{t - 1,{15} : {00}}}\right) * \left( {1 + {\sigma }_{t - i,9 : {30} \sim {hh} : {mm}}}\right)
$$

$${\text{ LowerBound }}_{t,{hh} : {mm}} = \min \left( {{\text{ open }}_{t,9 : {30}},{\text{ close }}_{t - 1,{15} : {00}}}\right) * \left( {1 - {\sigma }_{t - i,9 : {30} \sim {hh} : {mm}}}\right)$$

4. 则 $\mathrm{t}$ 日 hh:mm 时点的噪声区域为:

$$
{\text{NoiseArea}}_{t,{hh} : {mm}} = \left\lbrack {{\text{LowerBound}}_{t,{hh} : {mm}},{\text{UpperBound}}_{t,{hh} : {mm}}}\right\rbrack
$$

如果此时的价格位于噪声区域内, 则说明供需处于平衡状态; 当价格突破噪声区域的上边界, 说明存在大量买入需求, 价格可能进一步上升; 当价格突破噪声区域的下边界, 说明存在大量抛售压力, 价格可能进一步下降。

## Notebooks

### `source/etf_mom_strategy-2c632e29.ipynb`

# 引言

自 1993 年 Jegadeesh 和 Titman 提出并证明动量效应以来, 动量策略被广泛研究与应用。随着高频数据可获得性的增加以及相关技术的进步, 对动量效应的研究也逐渐拓展到日内领域，并被证明同样存在。

学术界对动量效应存在的原因至今仍有诸多争议, 但较有说服力的解释之一是价格对新信息的反应不足。即, 需要一定的时间逐步消化和反应新信息, 从而形成动量。造成反应不足的原因可能有,

1. 处置效应, 即卖出盈利头寸而继续持有亏损头寸。这种行为产生的资金流动可能会减缓利好（利空）消息后，股价的抬升（下跌）速度。

2. 投资者的注意力有限, 或是获取信息的成本较高。

3. 无法快速交易导致价格发现的速度变慢。

Zarattini C, Aziz A 和 Barbon A 在论文《Beat the Market: An Effective Intraday Momentum Strategy for S&P500 ETF (SPY)》中介绍了一种由粘性供需失衡（sticky demand/supply imbalances) 引起的日内动量效应, 并以此为基础, 设计了一个简洁而明确的 ETF 交易策略。本文参考其逻辑，对上证 50、沪深 300、中证 500、中证 1000 进行测试, 发现了相同的规律。

# 数据获取

# 信号构造


## 噪声区域

日内动量策略通常源自买卖双方的力量在一段时间内, 存在持续且显著的不平衡。但由于股票市场的噪声水平较高, 故我们需要定义一个买卖双方力量平衡时, 价格的正常波动区域, 并称之为噪声区域。若价格在噪声区域中波动, 则认为不存在日内趋势。

一种合理的假设是, 当日内走势接近过去若干天相同时间段的平均走势, 则可以认为市场处于供需平衡状态。由此，我们可按如下步骤定义 $\mathrm{t}$ 日的噪声区域。

1. 计算过去 14 天每个分钟时点 hh:mm 的价格位移 (相对开盘价的收益率绝对值):

$$
{\text{ move }}_{t - i,9 : {30} \sim {hh} : {mm}} = \left| {\frac{{\text{ close }}_{t - i,{hh} : {mm}}}{{\text{ open }}_{t - i,9 : {30}}} - 1}\right| ,\;i = 1 \sim {14}
$$

2. 取过去 14 天 hh:mm 时点的位移平均值:

$$
{\sigma }_{t - i,9 : {30} \sim {hh} : {mm}} = \frac{1}{14}\mathop{\sum }\limits_{{i = 1}}^{{14}}{\text{ move }}_{t - i,9 : {30} \sim {hh} : {mm}}
$$

3. 考虑到隔夜跳空缺口往往也预示着某种供需失衡, 因此进一步结合昨收盘价, 将 $\mathrm{t}$ 日 hh:mm 时点的噪声区域的上、下边界分别定义为:

$$
{\text{ UpperBound }}_{t,{hh} : {mm}} = \max \left( {{\text{ open }}_{t,9 : {30}},{\text{ close }}_{t - 1,{15} : {00}}}\right) * \left( {1 + {\sigma }_{t - i,9 : {30} \sim {hh} : {mm}}}\right)
$$

$${\text{ LowerBound }}_{t,{hh} : {mm}} = \min \left( {{\text{ open }}_{t,9 : {30}},{\text{ close }}_{t - 1,{15} : {00}}}\right) * \left( {1 - {\sigma }_{t - i,9 : {30} \sim {hh} : {mm}}}\right)$$

4. 则 $\mathrm{t}$ 日 hh:mm 时点的噪声区域为:

$$
{\text{NoiseArea}}_{t,{hh} : {mm}} = \left\lbrack {{\text{LowerBound}}_{t,{hh} : {mm}},{\text{UpperBound}}_{t,{hh} : {mm}}}\right\rbrack
$$

如果此时的价格位于噪声区域内, 则说明供需处于平衡状态; 当价格突破噪声区域的上边界, 说明存在大量买入需求, 价格可能进一步上升; 当价格突破噪声区域的下边界, 说明存在大量抛售压力, 价格可能进一步下降。

## Local Docs

### `source/README-2371aecc.md`

# 说明

原本的PyFolio已经不维护了，这里使用别人维护的一个仓库[stefan-jansen/pyfolio-reloaded: Portfolio and risk analytics in Python (github.com)](https://github.com/stefan-jansen/pyfolio-reloaded)

### `source/README-db415cc1.md`

<!--
 * @Author: Hugo
 * @Date: 2024-08-19 16:37:37
 * @LastEditors: shen.lan123@gmail.com
 * @LastEditTime: 2024-08-19 16:55:00
 * @Description:
-->
# 说面

数据来源于[tushare](https://tushare.pro/document/2?doc_id=109)

## Code Implementation

- `source/SignalMaker-0c7bf856.py`
  - Symbols: `NoiseArea, __init__, calculate_intraday_vwap, calculate_intraday_price_distance, calculate_sigma, calculate_bound, concat_signal, fit`
- `source/__init__-c69c811d.py`
- `source/bt_template-b2dc1373.py`
  - Symbols: `update_params, run_template_strategy`
- `source/datafeed-89a20369.py`
  - Symbols: `ETFDataFeed`
- `source/engine-ec60c860.py`
  - Symbols: `StockCommission, _getcommission, cheak_dataframe_cols, BackTesting, __init__, load_data, add_strategy`
- `source/performance-45dabfae.py`
  - Symbols: `show_perf_stats, multi_asset_show_perf_stats, multi_strategy_show_perf_stats`
- `source/plotting-1f8ac13c.py`
  - Symbols: `plot_cumulative_return, plot_annual_returns, plot_intraday_signal, plot_annual_time_series`
- `source/strategy-6ad043b3.py`
  - Symbols: `round_to_hundred, calculate_ashare_order_size, NoiseRangeStrategy, __init__, log, handle_signal, rebalance, handle_stop_loss, _calculate_size, _close_and_reverse, _open_position, next`
- `source/utils-2c7bbc6d.py`
  - Symbols: `get_strategy_return, trans_minute_to_daily, get_strategy_cumulative_return, check_index_tz`
