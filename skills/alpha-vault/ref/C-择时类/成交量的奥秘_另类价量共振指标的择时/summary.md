# 成交量的奥秘_另类价量共振指标的择时

- Category: `C-择时类`
- Bundle Dir: `成交量的奥秘_另类价量共振指标的择时`

## Primary Summary

- Notebook: `source/另类价量共振指标择时-140110e5.ipynb`

# 价量共振

## 价量共振指标的择时系统构建

1. 成交量使用的移动平均线为 AMA，收盘价使用的移动平均线为 BMA(移动平均线长度为L);
2. 价能=$\frac{BMA_{today}}{BMA_{Today-N}}$，当日的BMA除以前N个交易日的BMA;
3. 量能=$\frac{AMA_{5}}{AMA_{Long}}$，5 日的AMA除以长期的AMA;
4. 价量共振指标=价能×量能，价能乘以量能
5. 当价量共振指标大于 Threshold 则做多，否则平仓

## 市场划分条件下的择时系统

1. 当5日均线高于90日均线，市场划分为多头市场；当5日均线小于90日均线，市场划分为空头市场;
2. 当前为多头市场下，若价量共振指标大于Threshold1则做多，否则以Threshold1平仓。当前为空头市场下， 若价量共振指标大于Threshold2则做多，否则以Threshold2平仓;

**参数**

AMA长期移动平均线长度为 100，BMA移动平均线长度为 50，N=3，Threshold1=1.125，Threshold2=1.275

# 申万行业

## 申万行业指数择时情况

**使用pandas批量生成信号**

## Notebooks

### `source/另类价量共振指标择时-140110e5.ipynb`

# 价量共振

## 价量共振指标的择时系统构建

1. 成交量使用的移动平均线为 AMA，收盘价使用的移动平均线为 BMA(移动平均线长度为L);
2. 价能=$\frac{BMA_{today}}{BMA_{Today-N}}$，当日的BMA除以前N个交易日的BMA;
3. 量能=$\frac{AMA_{5}}{AMA_{Long}}$，5 日的AMA除以长期的AMA;
4. 价量共振指标=价能×量能，价能乘以量能
5. 当价量共振指标大于 Threshold 则做多，否则平仓

## 市场划分条件下的择时系统

1. 当5日均线高于90日均线，市场划分为多头市场；当5日均线小于90日均线，市场划分为空头市场;
2. 当前为多头市场下，若价量共振指标大于Threshold1则做多，否则以Threshold1平仓。当前为空头市场下， 若价量共振指标大于Threshold2则做多，否则以Threshold2平仓;

**参数**

AMA长期移动平均线长度为 100，BMA移动平均线长度为 50，N=3，Threshold1=1.125，Threshold2=1.275

# 申万行业

## 申万行业指数择时情况

**使用pandas批量生成信号**

## Local Docs

### `source/README-90890d7d.md`

# 说明

jp文档为研究文档

app.py为streamlit构建的应用

在cmd命令中进入到文件目录后,启动程序

```
$ streamlit run app.py
```



## 板块下的标的信号状态

 汇总当日行业指数的信号情况

- 红圈为当日有开仓
- 中空红圈表示当日有持仓还未平仓的
- 白圈为没有开仓
- 红叉表示当日平仓

![image-20221115143313847](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20221115143313847.png)

**板块下的信号状态->信号标记**

*标记当期有持仓及才开仓的行业指数*

![image-20221115143448679](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20221115143448679.png)

**板块下的信号状态->排名**

![image-20221115143555820](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20221115143555820.png)

**板块下的信号状态->累计收益一览**

*择时信号在各个行业指数上的过往表现情况*

![image-20221115143622709](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20221115143622709.png)

## 侧边栏

![image-20221115144134093](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20221115144134093.png)

选择不同的标的**风险收益情况、交易分析**根据所选则的标的进行回测

### 风险收益情况

![localhost_8501_](D:\Downloads\localhost_8501_.png)

![localhost_8501_ (1)](D:\Downloads\localhost_8501_ (1).png)

![localhost_8501_ (2)](D:\Downloads\localhost_8501_ (2).png)

### 交易分析

![localhost_8501_](D:\Downloads\localhost_8501_.png)

![localhost_8501_ (1)](D:\Downloads\localhost_8501_ (1).png)

## Code Implementation

- `source/app-8069525b.py`
  - Symbols: `query_data2st, transform_status_table2st, block_risk_report, block_trade_report, block_status`
- `source/__init__-abd0db92.py`
- `source/backtest_engine-8e247102.py`
  - Symbols: `TradeRecord, __init__, notify_trade, stop, get_trade_record, get_analysis, StockCommission, _getcommission, get_backtesting`
- `source/bt_strategy-83705e7f.py`
  - Symbols: `VM_Indicator, __init__, Shake_Filter, __init__, VM_Strategy, log, __init__, notify_order, next`
- `source/create_signal-19ed0639.py`
  - Symbols: `HMA, calc_volume_momentum, get_trendshake_filter, get_signal, bulk_signal, get_signal_status, _check_muliindex`
- `source/load_excel_data-32a8430c.py`
  - Symbols: `query_data, _check_codes, _check_fields, query_sw_classify, query_stock_index_classify, load_excel`
- `source/performance-c60ed7c2.py`
  - Symbols: `_adjust_returns, information_ratio, strategy_performance`
- `source/plotly_chart-f998736c.py`
  - Symbols: `_get_holidays, add_shape_to_ohlc, plot_candlestick, plot_orders_on_price, plotl_order_on_ohlc, plotly_table, GridPlotly, _plotly_add_nav`
- `source/tear-b4b07897.py`
  - Symbols: `get_transactions_frame, get_trade_flag, get_backtest_report, create_trade_report_table, analysis_rets, analysis_trade`
- `source/timeseries-3f13f11e.py`
  - Symbols: `get_max_drawdown_underwater, get_top_drawdowns, gen_drawdown_table`
- `source/utils-0df9b91e.py`
  - Symbols: `trans2strftime, get_value_from_traderanalyzerdict, transform_status_table, renormalize, min_rel_rescale, max_rel_rescale`
- `source/vectorbt_style_plotting-a616079d.py`
  - Symbols: `make_figure, _plot_orders, _plot_position, _plot_end_markers, plot_against, plot_position, plot_orders, plot_cumulative, plot_underwater, plot_pnl, _plot_scatter, plot_drawdowns`
