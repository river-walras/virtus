# C-VIX中国版VIX编制手册

- Category: `C-择时类`
- Bundle Dir: `C-VIX中国版VIX编制手册`

## Primary Summary

- Notebook: `source/VIX-b2c97899.ipynb`

本篇算法来源：
>《20180707_东北证券_金融工程_市场波动风险度量：vix与skew指数构建与应用》

## VIX、STEW与上证50的关系

## VIX、STEW与沪深300的关系

## Notebooks

### `source/VIX-b2c97899.ipynb`

本篇算法来源：
>《20180707_东北证券_金融工程_市场波动风险度量：vix与skew指数构建与应用》

## VIX、STEW与上证50的关系

## VIX、STEW与沪深300的关系

### `source/中国版VIV-fb166427.ipynb`

# VIX计算方法

白皮书具体步骤:

[CBOE Volatility Index](http://www.cboe.com/micro/vix/vixwhite.pdf)

[CBOE Skew Index](http://www.cboe.com/micro/skew/documents/skewwhitepaperjan2011.pdf)

$$\sigma^2=\frac{2}{T}\sum^{n}_{i=1}\frac{\Delta K_i}{K^{2}_{i}}e^{rT}Q(K_i)-\frac{1}{T}(\frac{F}{K_0}-1)^2$$

CBOE白皮书对无风险收益率的描述是:
>The risk-free interest rates, $R_1$ and $R_2$, are yields based on U.S. Treasury yield curve rates (commonly referred to as“Constant Maturity Treasury” rates or CMTs), to which a cubic spline is applied to derive yields on the expiration dates ofrelevant SPX options. 

所有在这里我用的SHIBOR利率,具体处理见**GetShiBor**函数

# VIX择时

>波动率VIX指数是跟踪市场波动性的指数，一般通过标的期权的隐含波动率计算得来，以芝加哥期权交易所的VIX指数为例，如标的期权的隐含波动率越高，则VIX指数相应越高，一般而言，该指数反映出投资者愿意付出多少成本去对冲投资风险。业内认为，当VIX越高时，表示市场参与者预期后市波动程度会更加激烈，同时也反映其不安的心理状态；相反，VIX越低时，则反映市场参与者预期后市波动程度会趋于缓和的心态。因此，VIX又被称为投资人恐慌指标（The Investor Fear Gauge）。

**策略思路**


- 当VIX指数快速上升时，表示市场恐慌情绪蔓延，产生卖出信号
- 当VIX指数快速下降时，恐慌情绪有所舒缓，产生买入信号

实际回测时:卖出买入信号均用来买卖华夏上证50ETF基金

具体信号构造：
1. 计算VIX的快慢均线 
2. 死叉买入 金叉卖出

## Code Implementation

- `source/__init__-d43224e8.py`
- `source/get_jq_data-0edf8726.py`
  - Symbols: `get_opt_basic, offset_limit_func, get_opt_all_price, calc_maturity, prepare_data`
- `source/get_shibor-13d19ae9.py`
  - Symbols: `query_china_shibor_all, _load_csv, get_shibor_data, get_interpld_shibor, _interpld_fun`
- `source/utils-7090b495.py`
  - Symbols: `trans_ser2datetime`
- `source/bt_func-1fa98117.py`
  - Symbols: `add_pandas_data, vix_over_quantile_bound_strategy, log, __init__, next, notify_order, trade_list, __init__, notify_trade, get_analysis, get_backtesting, analysis_rets`
- `source/calc_func-bfa3dde7.py`
  - Symbols: `_get_near_or_next_options, _build_strike_matrix, _get_min_strike_diff, calc_delta_k_table, _get_median_price_table, _get_free_rate, calc_F, calc_sigma, calc_vix, calc_weight, _get_sigma, calc_epsilons`
- `source/plotting-3df19fc2.py`
  - Symbols: `plot_indicator, plot_qunatile_signal, plot_quantreg_res, plot_hist2d, plot_group_ret, plot_trade_flag, plot_algorithm_nav, get_strat_ret`
- `source/utils-789e598d.py`
  - Symbols: `load_csv, print_table`
