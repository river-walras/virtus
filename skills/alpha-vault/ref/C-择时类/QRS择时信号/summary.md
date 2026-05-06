# QRS择时信号

- Category: `C-择时类`
- Bundle Dir: `QRS择时信号`

## Primary Summary

- Notebook: `source/QRS-de4486d4.ipynb`

# 信号构建

信号并非用支撑位与阻力位作突破或反转交易的阈值，而是更关注市场参与者们对于阻力位与支撑位的定位一致性。因此一个简单想法是利用类似$\frac{\delta(high)}{\delta(low)}$的值来描述支撑位与阻力位的相对强度，即最低价每变动 1 的时候，最高价变动的幅度。实际上， $\frac{\delta(high)}{\delta(low)}$是连接高低价格平面上的两点 (low[0], high[0]) 与 (low[1], high[1]) 的斜率。由于市场量价本身噪音的存在，仅计算两点得到的斜率数据包含了太多的噪音。我们考虑通过最近 N 个 (low, high) 的数据点来得到信噪相对较高的最高最低价相对变化程度。
使用线性回归，建立如下般最高价与最低价之间的线性模型：
$$hight_{t}=\alpha+\beta*low_{t}+\epsilon$$

式中拟合出的$\beta$值即是用以刻画支撑与阻力强度对比的代理指标，表明最近一段时期， 最低价每波动 1 个点位，最高价相应会波动$\beta$个点位。因此，$\beta$越大，表明支撑强度相 比阻力强度越显著，市场越容易上行，牛市中大概率对应后市加速上涨的走势，熊市中 则对应后市止跌企稳的走势；同理，$\beta$越小，表明阻力相对支撑的强度更甚，在牛市中 可能预示着即将见顶，在熊市中则对应后市大概率加速深跌。

QRS指标的构建中信号项(signal)部分：$zscore(\beta)$，惩罚项(Regulation)部分$R^{2}$ 。实际上在普通线性回归里，$\beta$有简单的解析解：$\beta = \frac{std(y)}{std(x)} ∗ 𝑐𝑜𝑟𝑟(y, x)$；而 $R^{2}$则 为：$R^{2} = corr(y, x)^{2}$ 。由此我们可以发现，整个指标实际上可以仅由三个简单数据决定： 最高价序列的波动率、最低价序列的波动率、最高级与最低价的相关系数。而原始指标 值可以转写为：

$$zscore(\frac{std(y)}{std(x)}*corr(y,x))*corr(y,x)^{2}$$

其中 y 是最高价序列，x 是最低价序列。

检查历史上不同β值下指数后续的预期收益率。以N=18计算的β为例，我们以 0.01 为 间隔将历史β值划分成不同子样本，计算每个子样本内β值对应的沪深300、中证500等指数10日后收益率的均值，作为该β取值范围对应的未来指数预期收益率。

β取值与沪深 300 指数 10 天后预期收益率的相关系数为0.56(研报中为0.25)。如果考虑到有些β的取值区间内样本数太少，我们可以只统计样本数量至少为5个的取值区间。在限定了样本数量后，β取值与沪深 300 指数 10 天后预期收益率的相关系数为0.57(研报中为0.63)。

## Notebooks

### `source/QRS-de4486d4.ipynb`

# 信号构建

信号并非用支撑位与阻力位作突破或反转交易的阈值，而是更关注市场参与者们对于阻力位与支撑位的定位一致性。因此一个简单想法是利用类似$\frac{\delta(high)}{\delta(low)}$的值来描述支撑位与阻力位的相对强度，即最低价每变动 1 的时候，最高价变动的幅度。实际上， $\frac{\delta(high)}{\delta(low)}$是连接高低价格平面上的两点 (low[0], high[0]) 与 (low[1], high[1]) 的斜率。由于市场量价本身噪音的存在，仅计算两点得到的斜率数据包含了太多的噪音。我们考虑通过最近 N 个 (low, high) 的数据点来得到信噪相对较高的最高最低价相对变化程度。
使用线性回归，建立如下般最高价与最低价之间的线性模型：
$$hight_{t}=\alpha+\beta*low_{t}+\epsilon$$

式中拟合出的$\beta$值即是用以刻画支撑与阻力强度对比的代理指标，表明最近一段时期， 最低价每波动 1 个点位，最高价相应会波动$\beta$个点位。因此，$\beta$越大，表明支撑强度相 比阻力强度越显著，市场越容易上行，牛市中大概率对应后市加速上涨的走势，熊市中 则对应后市止跌企稳的走势；同理，$\beta$越小，表明阻力相对支撑的强度更甚，在牛市中 可能预示着即将见顶，在熊市中则对应后市大概率加速深跌。

QRS指标的构建中信号项(signal)部分：$zscore(\beta)$，惩罚项(Regulation)部分$R^{2}$ 。实际上在普通线性回归里，$\beta$有简单的解析解：$\beta = \frac{std(y)}{std(x)} ∗ 𝑐𝑜𝑟𝑟(y, x)$；而 $R^{2}$则 为：$R^{2} = corr(y, x)^{2}$ 。由此我们可以发现，整个指标实际上可以仅由三个简单数据决定： 最高价序列的波动率、最低价序列的波动率、最高级与最低价的相关系数。而原始指标 值可以转写为：

$$zscore(\frac{std(y)}{std(x)}*corr(y,x))*corr(y,x)^{2}$$

其中 y 是最高价序列，x 是最低价序列。

检查历史上不同β值下指数后续的预期收益率。以N=18计算的β为例，我们以 0.01 为 间隔将历史β值划分成不同子样本，计算每个子样本内β值对应的沪深300、中证500等指数10日后收益率的均值，作为该β取值范围对应的未来指数预期收益率。

β取值与沪深 300 指数 10 天后预期收益率的相关系数为0.56(研报中为0.25)。如果考虑到有些β的取值区间内样本数太少，我们可以只统计样本数量至少为5个的取值区间。在限定了样本数量后，β取值与沪深 300 指数 10 天后预期收益率的相关系数为0.57(研报中为0.63)。

## Code Implementation

- `source/__init__-14215c0e.py`
- `source/bt_template-b5330fc7.py`
  - Symbols: `update_params, run_template_strategy`
- `source/datafeed-32ffa640.py`
  - Symbols: `DailyOHLCVUSLFeed`
- `source/engine-34c79941.py`
  - Symbols: `StockCommission, _getcommission, cheak_dataframe_cols, BackTesting, __init__, load_data, add_strategy`
- `source/__init__-bf0bc5ce.py`
  - Symbols: `concat_signal_vs_forward_returns, concat_ohlc_vs_signal, calc_signal_bins_corr, _calc_corr`
- `source/performance-7eae409f.py`
  - Symbols: `show_trade_stats, get_analyzer_value, format_stat, show_perf_stats, multi_asset_show_perf_stats, multi_strategy_show_perf_stats, multi_strategy_show_trade_stats`
- `source/plotting-9a981dba.py`
  - Symbols: `plot_signal_vs_forward_returns, displot_signal, displot_signal_vs_forward_returns, plot_cumulative_return, plot_annual_returns, plot_intraday_signal, plot_annual_time_series`
- `source/plotting_utils-4877432c.py`
  - Symbols: `get_strategy_return, trans_minute_to_daily, get_strategy_cumulative_return, check_index_tz, calculate_bin_means`
- `source/utils-2e922ffe.py`
  - Symbols: `get_strategy_return, trans_minute_to_daily, get_strategy_cumulative_return, check_index_tz`
- `source/__init__-d035efc4.py`
- `source/rsrs_strategy-b945f951.py`
  - Symbols: `calculate_ashare_order_size, RSRSStrategy, __init__, log, _calculate_size, handle_signal, next, prenext, RSRSTwoSidetrategy, __init__, log, _calculate_size`
