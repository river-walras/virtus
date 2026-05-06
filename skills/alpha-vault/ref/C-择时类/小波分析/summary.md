# 小波分析

- Category: `C-择时类`
- Bundle Dir: `小波分析`

## Primary Summary

- Notebook: `source/小波分析择时-e9a7e41e.ipynb`

# 一、小波分析

小波分析理论是目前科学界和工程界讨论和研究最多的课题之一，它包含了丰富的数学内容，又具有巨大的应用潜力。小波分析是在 Fourier 分析的基础上发展起来的，是调和分析近半个世纪以来的结晶。其基本思想是将一般函数（信号）表示为规范正交小波基的线性叠加，核心内容是小波变换。由于小波变换在时域和频域具有良好的局部化性质，能自动调整时、频窗口，以适应实际分析需要，因而已成为许多工程学科应用的有力工具。

小波分析属时频分析的一种，主要依据下面三步来实现(Python开源库pywt是专门做小波分析的库)：

1. Decomposition——将信号序列分解为N层小波   
2. Denoise——对于分解得到的小波，选择阈值并进行去噪处理(要注意的是不是对每个小波都要处理，一般选择几个进行处理)
3. Reconstruction——将去噪后的小波，和未处理的小波，重构得到处理后的信号

**关于小波的选择及阈值处理的总结**

《量化投资：策略与技术》
>综合来看，dbN（即Daubechies系列小波）、 symN（Symlets系列小波）、coifN（Coiflet系列小波）都比较合适，并且对于股价序列等相对 比较平缓的序列可选择消失矩阶数稍高一点， 即对应小波序列N取4～8都是可以的。但对收益率数据， 因其奇异点密度非常大，消失矩不能高， 建议不要超过4，即db2 ～ db4比较恰当。

>对股票价格等数据而言，其信号频率较少地与噪声重叠因此可以选用sqtwolog和heursure准则，使去噪效果更明显。 
但对收益率这样的高频数据，尽量采用保守的 rigrsure 或 minimaxi 准则来确定阈值，以保留较多的信号。


《平安证券-量化择时选股系列报告二：水致清则鱼自现_小波分析与支持向量机择时研究》
>采用 Symlets小波 + rigrsure法选择阈值 + 软约束方法 对 上证指数进行的处理

《国信证券-基于小波分析和支持向量机的指数预测模型》
>采用 选择小波Daubechies小波系(db4)并确定分解层次为 4 层 + sqtwolog阀值估计准则 +软约束方法 对沪深300进行的处理

## Notebooks

### `source/小波分析择时-e9a7e41e.ipynb`

# 一、小波分析

小波分析理论是目前科学界和工程界讨论和研究最多的课题之一，它包含了丰富的数学内容，又具有巨大的应用潜力。小波分析是在 Fourier 分析的基础上发展起来的，是调和分析近半个世纪以来的结晶。其基本思想是将一般函数（信号）表示为规范正交小波基的线性叠加，核心内容是小波变换。由于小波变换在时域和频域具有良好的局部化性质，能自动调整时、频窗口，以适应实际分析需要，因而已成为许多工程学科应用的有力工具。

小波分析属时频分析的一种，主要依据下面三步来实现(Python开源库pywt是专门做小波分析的库)：

1. Decomposition——将信号序列分解为N层小波   
2. Denoise——对于分解得到的小波，选择阈值并进行去噪处理(要注意的是不是对每个小波都要处理，一般选择几个进行处理)
3. Reconstruction——将去噪后的小波，和未处理的小波，重构得到处理后的信号

**关于小波的选择及阈值处理的总结**

《量化投资：策略与技术》
>综合来看，dbN（即Daubechies系列小波）、 symN（Symlets系列小波）、coifN（Coiflet系列小波）都比较合适，并且对于股价序列等相对 比较平缓的序列可选择消失矩阶数稍高一点， 即对应小波序列N取4～8都是可以的。但对收益率数据， 因其奇异点密度非常大，消失矩不能高， 建议不要超过4，即db2 ～ db4比较恰当。

>对股票价格等数据而言，其信号频率较少地与噪声重叠因此可以选用sqtwolog和heursure准则，使去噪效果更明显。 
但对收益率这样的高频数据，尽量采用保守的 rigrsure 或 minimaxi 准则来确定阈值，以保留较多的信号。


《平安证券-量化择时选股系列报告二：水致清则鱼自现_小波分析与支持向量机择时研究》
>采用 Symlets小波 + rigrsure法选择阈值 + 软约束方法 对 上证指数进行的处理

《国信证券-基于小波分析和支持向量机的指数预测模型》
>采用 选择小波Daubechies小波系(db4)并确定分解层次为 4 层 + sqtwolog阀值估计准则 +软约束方法 对沪深300进行的处理

## Code Implementation

- `source/小波分析_svm-98592c1f.py`
  - Symbols: `initialize, set_params, set_variables, set_backtest, before_trading_start, set_slip_fee, DenoisingThreshold, __init__, CalSqtwolog, CalRigrsure, CalMinmaxi, GetCrit`
- `source/小波分析_希伯特变换-f58f8887.py`
  - Symbols: `initialize, set_params, set_variables, set_backtest, before_trading_start, set_slip_fee, DenoisingThreshold, __init__, CalSqtwolog, CalRigrsure, CalMinmaxi, GetCrit`
