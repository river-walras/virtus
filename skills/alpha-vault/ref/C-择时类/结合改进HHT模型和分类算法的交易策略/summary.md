# 结合改进HHT模型和分类算法的交易策略

- Category: `C-择时类`
- Bundle Dir: `结合改进HHT模型和分类算法的交易策略`

## Primary Summary

- Notebook: `source/hht_timing-2d8f38bb.ipynb`

# 一、基于 HHT 模型识别价格周期

## 价格周期和希尔伯特变换 (HT)

在金融市场中, 价格波动通常表现出一定的周期性, 即资产价格随时间变化表现出的重复性模式。这些模式可以是短期的日内周期, 也可以是中期的日间周期或长期的趋势周期。价格周期的存在表明市场并非完全随机, 而是存在一定的规律性和可预测性。价格周期反映了市场参与者的集体行为以及市场内外部因素的影响, 理解价格周期对于识别市场趋势、预测价格变动以及制定有效的交易策略非常重要。

那么, 如何识别价格周期和趋势呢? 典型方法有宏观基本面分析、技术分析、 频谱分析、时序预测模型和深度学习等。在这些方法中, 由于频谱分析可以分解出价格运动的幅度、频率和相位,对于周期识别无疑是较为适用的。下面,将基于频谱分析中的希尔伯特变换方法, 理解和识别价格运动的周期。

![](img/0194a840-7e87-7404-ba98-29259e8253d9_4_102_1287_1000_472_0.jpg)

希尔伯特变换(Hilbert Transform, HT)是一种线性变换,其作用是将一个实值信号转换为一个复数信号, 广泛应用于信号处理领域。对于给定的时间序列 $x\left( t\right)$ ,希尔伯特变换产生的复数信号可以表示为
$$z\left( t\right)  = x\left( t\right)  + j\widehat{x}\left( t\right)$$
其中, $j$ 是虚数单位, $\widehat{x}\left( t\right)$ 是 $x\left( t\right)$ 的希尔伯特变换结果。希尔伯特变换的数学表达式可以通过积分形式给出:
$$\widehat{x}\left( t\right)  = \frac{1}{\pi }\mathcal{P}{\int }_{-\infty }^{\infty }\frac{x\left( \tau \right) }{t - \tau }{d\tau }$$
其中, $\mathcal{P}$ 表示柯西主值,这是因为积分在 $t = \tau$ 处是奇异的,需要采用主值的方式来处理。
解析信号 $z\left( t\right)$ 可以分解为幅度和相位的形式:
$$z\left( t\right)  = A\left( t\right) {e}^{{j\theta }\left( t\right) },$$
其中, $A\left( t\right)$ 是信号的瞬时幅度,而 $\theta \left( t\right)$ 是瞬时相位,其分别可以通过如下方式计算:
$$A\left( t\right)  = \left| {z\left( t\right) }\right|  = \sqrt{x{\left( t\right) }^{2} + \widehat{x}{\left( t\right) }^{2}},$$
$$\theta \left( t\right)  = \arg \left( {z\left( t\right) }\right)  = \arctan \left( \frac{\widehat{x}\left( t\right) }{x\left( t\right) }\right) .$$

![](img/0194a840-7e87-7404-ba98-29259e8253d9_5_80_742_742_451_0.jpg)
![](img/0194a840-7e87-7404-ba98-29259e8253d9_5_923_763_509_419_0.jpg)

基于希尔伯特变换得到的瞬时相位,可以识别价格周期和当前所处的趋势。 相位 $\theta \left( t\right)$ 取值范围为 $\left\lbrack  {-\pi ,\pi }\right\rbrack$ ,当 $\theta \left( t\right)  \in  \left\lbrack  {0,\frac{\pi }{2}}\right\rbrack$ 即信号位于复平面的第一象限时,价格可能处于上升早期或刚刚从底部开始回升; 当 $\theta \left( t\right)  \in  \left\lbrack  {\frac{\pi }{2},\pi }\right\rbrack$ 即信号位于复平面的第二象限时,表明价格上升趋势持续,但可能即将到达顶部区域; 当 $\theta \left( t\right)  \in$ $\left\lbrack  {-\pi , - \frac{\pi }{2}}\right\rbrack$ 即信号位于复平面的第三象限时,表明价格开始从高位回落,进入下降趋势; 当 $\theta \left( t\right)  \in  \left\lbrack  {-\frac{\pi }{2},0}\right\rbrack$ 即信号位于复平面的第四象限时,表明价格持续下跌,但可能接近底部。

![](img/0194a840-7e87-7404-ba98-29259e8253d9_6_89_219_843_715_0.jpg)

## 经验模态分解(EMD)及改进算法(VMD)

然而,直接在资产价格上应用希尔伯特变换存在一些问题: 由于希尔伯特变换需要原始信号是窄带稳态信号, 而价格本身是非稳态、非线性的时间序列, 并且包括多种频率成分, 直接对价格数据应用希尔伯特变换可能得到错误结果。正确的做法是:首先对价格信号进行预处理和分解,得到单一频率的稳态信号,然后再应用希尔伯特变换进行分析处理。

经验模态分解(Empirical Mode Decomposition, EMD)是一种信号处理技术,可以将复杂时间序列分解成多个具有单一频率成分的本征模函数(Intrinsic Mode Functions, IMF)和一个剩余趋势项(Residual Trend)。每个 IMF 都是一个本征模,具有单一的瞬时频率,这使得 EMD 非常适合分析非线性和非平稳信号,进而能够让后续的希尔伯特变换分析更加精确。

EMD 的分解过程包括以下步骤:

✓ 识别局部极值:找出原始信号中的所有局部极大值和极小值。

✓ 插值形成包络线:在所有局部极大值之间进行插值形成一个上包络线； 在所有局部极小值之间进行插值形成一个下包络线。

✓ 计算中间包络线:计算上包络线和下包络线的平均值,形成中间包络线。

✓ 筛选过程:从原始信号中减去中间包络线,得到第一个近似的 IMF。

✓ 停止准则:重复步骤 1-4,直到得到的近似 IMF 满足停止准则。通常的停止准则是 IMF 中相邻极大值和极小值之间的平均值趋近于 0 , 且 IMF 中相邻极大值和极小值之间的标准差小于某个阈值。

✓ 重复提取:从剩余信号中重复上述步骤,直到剩余信号成为一个单调函数或满足停止准则。

✓ 最终分解:最终得到一系列 IMF 和一个剩余趋势项(Residual Trend),

后者通常是一个单调函数或一个非常缓慢变化的趋势。

假设原始信号为 $x\left( t\right)$ ,第 $i$ 个 IMF 为 ${IM}{F}_{i}\left( t\right)$ ,剩余趋势项为 $r\left( t\right)$ 。EMD 的目标是将 $x\left( t\right)$ 分解为:
$$x\left( t\right)  = \mathop{\sum }\limits_{{i = 1}}^{N}{IM}{F}_{i}\left( t\right)  + r\left( t\right) ,$$

其中, $N$ 是分解得到的 $\mathsf{{IMF}}$ 的数量。

以沪深 300 指数价格为例, 基于 EMD 可以将价格分解为 9 个 IMF, 分别为从高频到低频的 IMF 信号,分别可以对应价格的短、中、长维度的周期。

## Notebooks

### `source/hht_timing-2d8f38bb.ipynb`

# 一、基于 HHT 模型识别价格周期

## 价格周期和希尔伯特变换 (HT)

在金融市场中, 价格波动通常表现出一定的周期性, 即资产价格随时间变化表现出的重复性模式。这些模式可以是短期的日内周期, 也可以是中期的日间周期或长期的趋势周期。价格周期的存在表明市场并非完全随机, 而是存在一定的规律性和可预测性。价格周期反映了市场参与者的集体行为以及市场内外部因素的影响, 理解价格周期对于识别市场趋势、预测价格变动以及制定有效的交易策略非常重要。

那么, 如何识别价格周期和趋势呢? 典型方法有宏观基本面分析、技术分析、 频谱分析、时序预测模型和深度学习等。在这些方法中, 由于频谱分析可以分解出价格运动的幅度、频率和相位,对于周期识别无疑是较为适用的。下面,将基于频谱分析中的希尔伯特变换方法, 理解和识别价格运动的周期。

![](img/0194a840-7e87-7404-ba98-29259e8253d9_4_102_1287_1000_472_0.jpg)

希尔伯特变换(Hilbert Transform, HT)是一种线性变换,其作用是将一个实值信号转换为一个复数信号, 广泛应用于信号处理领域。对于给定的时间序列 $x\left( t\right)$ ,希尔伯特变换产生的复数信号可以表示为
$$z\left( t\right)  = x\left( t\right)  + j\widehat{x}\left( t\right)$$
其中, $j$ 是虚数单位, $\widehat{x}\left( t\right)$ 是 $x\left( t\right)$ 的希尔伯特变换结果。希尔伯特变换的数学表达式可以通过积分形式给出:
$$\widehat{x}\left( t\right)  = \frac{1}{\pi }\mathcal{P}{\int }_{-\infty }^{\infty }\frac{x\left( \tau \right) }{t - \tau }{d\tau }$$
其中, $\mathcal{P}$ 表示柯西主值,这是因为积分在 $t = \tau$ 处是奇异的,需要采用主值的方式来处理。
解析信号 $z\left( t\right)$ 可以分解为幅度和相位的形式:
$$z\left( t\right)  = A\left( t\right) {e}^{{j\theta }\left( t\right) },$$
其中, $A\left( t\right)$ 是信号的瞬时幅度,而 $\theta \left( t\right)$ 是瞬时相位,其分别可以通过如下方式计算:
$$A\left( t\right)  = \left| {z\left( t\right) }\right|  = \sqrt{x{\left( t\right) }^{2} + \widehat{x}{\left( t\right) }^{2}},$$
$$\theta \left( t\right)  = \arg \left( {z\left( t\right) }\right)  = \arctan \left( \frac{\widehat{x}\left( t\right) }{x\left( t\right) }\right) .$$

![](img/0194a840-7e87-7404-ba98-29259e8253d9_5_80_742_742_451_0.jpg)
![](img/0194a840-7e87-7404-ba98-29259e8253d9_5_923_763_509_419_0.jpg)

基于希尔伯特变换得到的瞬时相位,可以识别价格周期和当前所处的趋势。 相位 $\theta \left( t\right)$ 取值范围为 $\left\lbrack  {-\pi ,\pi }\right\rbrack$ ,当 $\theta \left( t\right)  \in  \left\lbrack  {0,\frac{\pi }{2}}\right\rbrack$ 即信号位于复平面的第一象限时,价格可能处于上升早期或刚刚从底部开始回升; 当 $\theta \left( t\right)  \in  \left\lbrack  {\frac{\pi }{2},\pi }\right\rbrack$ 即信号位于复平面的第二象限时,表明价格上升趋势持续,但可能即将到达顶部区域; 当 $\theta \left( t\right)  \in$ $\left\lbrack  {-\pi , - \frac{\pi }{2}}\right\rbrack$ 即信号位于复平面的第三象限时,表明价格开始从高位回落,进入下降趋势; 当 $\theta \left( t\right)  \in  \left\lbrack  {-\frac{\pi }{2},0}\right\rbrack$ 即信号位于复平面的第四象限时,表明价格持续下跌,但可能接近底部。

![](img/0194a840-7e87-7404-ba98-29259e8253d9_6_89_219_843_715_0.jpg)

## 经验模态分解(EMD)及改进算法(VMD)

然而,直接在资产价格上应用希尔伯特变换存在一些问题: 由于希尔伯特变换需要原始信号是窄带稳态信号, 而价格本身是非稳态、非线性的时间序列, 并且包括多种频率成分, 直接对价格数据应用希尔伯特变换可能得到错误结果。正确的做法是:首先对价格信号进行预处理和分解,得到单一频率的稳态信号,然后再应用希尔伯特变换进行分析处理。

经验模态分解(Empirical Mode Decomposition, EMD)是一种信号处理技术,可以将复杂时间序列分解成多个具有单一频率成分的本征模函数(Intrinsic Mode Functions, IMF)和一个剩余趋势项(Residual Trend)。每个 IMF 都是一个本征模,具有单一的瞬时频率,这使得 EMD 非常适合分析非线性和非平稳信号,进而能够让后续的希尔伯特变换分析更加精确。

EMD 的分解过程包括以下步骤:

✓ 识别局部极值:找出原始信号中的所有局部极大值和极小值。

✓ 插值形成包络线:在所有局部极大值之间进行插值形成一个上包络线； 在所有局部极小值之间进行插值形成一个下包络线。

✓ 计算中间包络线:计算上包络线和下包络线的平均值,形成中间包络线。

✓ 筛选过程:从原始信号中减去中间包络线,得到第一个近似的 IMF。

✓ 停止准则:重复步骤 1-4,直到得到的近似 IMF 满足停止准则。通常的停止准则是 IMF 中相邻极大值和极小值之间的平均值趋近于 0 , 且 IMF 中相邻极大值和极小值之间的标准差小于某个阈值。

✓ 重复提取:从剩余信号中重复上述步骤,直到剩余信号成为一个单调函数或满足停止准则。

✓ 最终分解:最终得到一系列 IMF 和一个剩余趋势项(Residual Trend),

后者通常是一个单调函数或一个非常缓慢变化的趋势。

假设原始信号为 $x\left( t\right)$ ,第 $i$ 个 IMF 为 ${IM}{F}_{i}\left( t\right)$ ,剩余趋势项为 $r\left( t\right)$ 。EMD 的目标是将 $x\left( t\right)$ 分解为:
$$x\left( t\right)  = \mathop{\sum }\limits_{{i = 1}}^{N}{IM}{F}_{i}\left( t\right)  + r\left( t\right) ,$$

其中, $N$ 是分解得到的 $\mathsf{{IMF}}$ 的数量。

以沪深 300 指数价格为例, 基于 EMD 可以将价格分解为 9 个 IMF, 分别为从高频到低频的 IMF 信号,分别可以对应价格的短、中、长维度的周期。

## Code Implementation

- `source/__init__-817d25de.py`
- `source/bt_template-f530c15f.py`
  - Symbols: `update_params, run_template_strategy`
- `source/datafeed-8dd224a2.py`
  - Symbols: `DailyOHLCVUSLFeed`
- `source/engine-a3e9317c.py`
  - Symbols: `StockCommission, _getcommission, cheak_dataframe_cols, BackTesting, __init__, load_data, add_strategy`
- `source/__init__-b3e51bd1.py`
- `source/performance-b6511d41.py`
  - Symbols: `show_trade_stats, get_analyzer_value, format_stat, show_perf_stats, multi_asset_show_perf_stats, multi_strategy_show_perf_stats, multi_strategy_show_trade_stats`
- `source/plotting-8b078cc6.py`
  - Symbols: `plot_cumulative_returns, percentage_formatter`
- `source/plotting_utils-aa92da8a.py`
  - Symbols: `get_strategy_return, trans_minute_to_daily, get_strategy_cumulative_return, check_index_tz, calculate_bin_means`
- `source/rolling-f1bab775.py`
  - Symbols: `Rolling, __init__, _is_classifier, _init_predictions, _init_model, predict, train, _get_train_test_data, run, evaluate, _validate_inputs, get_model`
- `source/utils-6472ed30.py`
  - Symbols: `get_strategy_return, trans_minute_to_daily, get_strategy_cumulative_return, check_index_tz`
- `source/__init__-0b8a45ad.py`
- `source/binary_signal_strategy-35c2a02d.py`
  - Symbols: `calculate_ashare_order_size, BinarySignalStrategy, __init__, log, _calculate_size, handle_signal, next, prenext`
