# 技术分析算法框架与实战

- Category: `C-择时类`
- Bundle Dir: `技术分析算法框架与实战`

## Primary Summary

- Notebook: `source/技术分析算法框架与实战_20220221-0efadb75.ipynb`

# 论文介绍

《Foundations of Technical Analysis》
>Andrew W Lo、Harry Mamaysky和王江提出了一种系统化和自动化的方法，使用非参数核回归方法来进行模式识别，并将该方法应用于1962年至 1996 年的美股数据，以评估技术分析的有效性。通过将股票收益的无条件经验分布与条件分布（给定特定的技术指标，例如：头肩底形态、双底形态）作比较，发现在 31 年的样本期 间内，部分技术指标确实提供了有用的信息，具有实用价值。
>与基本面分析不同，技术分析一直以来饱受争议。然而一些学术研究表明，技术分析能从市场价格中提取 有用的信息。例如，Lo and MacKinlay (1988, 1999)证实了每周的美股指数并非随机游走，过去的价格可以在某种 程度上预测未来收益。技术分析和传统金融工程的一个重要区别在于，技术分析主要通过观察图表进行，而量化金融则依赖于相对完善的数值法。因此，技术分析利用几何工具和形态识别，而量化金融运用数学分析和概率统计。随着近年来金融工程、计算机技术和数值算法等领域的突破，金融工程可以逐步取代不那么严谨的技术分析。技术分析虽饱受质疑却仍能占据一席之地，归功于其视觉分析模式更贴近直观认知，而且在过去，要进行技术分析，首先要认识到价格过程是非线性的，且包含一定的规律和模式。为了定量地捕捉这种规 律，我们首先假定价格过程尚未有严格的算法取代传统的技术分析，如今，成熟的统计算法能够取代传统的几何画图，让技术分析继续以 更新、更严谨的方式服务投资者，同时金融工程领域在分析范式上也得到了丰富。

# 形态识别算法
## 核估计方法

假定价格过程${P_t}$有如下表达形式:

$$P_t=m(X_t)+\epsilon_t,t=1,\dots,T$$

其中$X_t$是状态变量,$m(X_t)$是任意固定但位置的非线性函数,$\epsilon$为白噪声。

为了识别模式,我们令状态变量等于时间$X_{t}=t$,此时,需要用一个光滑函数$\hat{m}(.)$.近似价格过程为了与核回归估计文献中的符号保持一致，我们仍将状态变量记为$X_{t}$。

$\hat{m}(.)$,还需要一个形态识别的算法,以自动识别指数指标。一旦有了算法,就可以应用于不同时段的资产价格,从而评估不同技术指标的有效性。

## 平滑估计量

$\hat{m}=\frac{1}{T}\sum^{T}_{t=1}w_{t}(x)P_{t}$
其中离x较近的$X_t$对应的$P_t$拥有较大的权重$w_{t}(x)$。对于距离的选择，太宽会导致估计量过于平滑而无法显示出$m(⋅)$真正的特性，太窄又会导致估计量的波动较大，无法排除噪声的影响。因此需要通过选择合适的权重$w_{t}(x)$来平衡以上两点。

## 核回归

对于核回归估计量，权重$w_{t}(x)$是通过核密度函数$K(x)$构造的:

$$K(x) \ge 0,\int{K(\mu)}du=1$$

我们可以通过一个参数$h \gt 0$来调整核函数的离散程度,令:

$$K_{h}(x)\equiv\frac{1}{h}K(\mu / h),\int{K_{h}(\mu)du}=1$$

然后定义如下权重系数:

$$w_{t,h}(x) \equiv K_{h}(x-X_{t})/g_{h}(x)$$
$$g_{h}(x) \equiv \frac{1}{T}\sum^{T}_{t=1}K_{h}(x-X_t)$$

其中,平滑系数h也称为带宽,h越大,用于计算加权均值的样本窗口宽度越大。带宽的选取对于任一局部平均方法都很关键，将在下一小节中进行详细讨论。

将上式代入,得到$m(x)$的估计$\hat{m}_{h}(x)$,称为Nadaraya-Waston核估计:

$$\hat{m}_{h}(x)=\frac{1}{T}\sum^{T}_{t=1}w_{t,h}(x)Y_t=\frac{\sum^{T}_{t=1}K_{h}(x-X)Y_t}{\sum^{T}_{t=1}K_{h}(x-X_t)}$$

在特定条件下可以证明，当样本量增大，$\hat{m}_{h}(x)$以多种方式渐进收敛于$m(x)$。该收敛性质对许多核函数都成立，本文将使用最常用的高斯核：

$$K_{h}(x)=\frac{1}{h\sqrt{2\pi}}e^{-x^{2}/2h^{2}}$$

### 带宽(bw)的选择

通过最小化如下函数来选取合适的h:

$$CV(h)=\frac{1}{T}\sum^{T}_{t=1}(P_t-\hat{m}_{h,t})^2$$

其中:

$\hat{m}_{h,t}=\frac{1}{T}\sum^{T}_{t=1}w_{r,h}Y_{r}$

估计量$\hat{m}_{h,t}$是剔除第t个观测得到的估计量，而上式是所有$\hat{m}_{h,t}$的均方误差。对给定的带宽h，CV(h)衡量了核回归估计量的拟合能力。通过最小化CV(h),我们得到的估计量具有一些统计上的优良性质，例如最小渐进均方误差。但由此得到的带宽往往偏大，即基于最小化CV(h) 的$\hat{m}(⋅)$ 给远距离样本过多的权重，导致过渡平滑，丢失了局部信息。经过不断的试验，我们发现最优带宽应取0.3*$h^{*}$,其中$h^{*}=\mathop{argmin}_{h}CV(X)$

### 形态识别算法

1. 头肩形态（头肩顶和头肩底）

$$
HS = 
    \begin{cases}
        E_1\ is\ maximum,  \\
        E_3 > E_1,E_3>E_4, \\ 
        E_1,E_5 \in{[98.5\%,101.05\%]*\frac{E_1+E_5}{2}},\\
        E_2,E_4 \in{[98.5\%,101.05\%]*\frac{E_2+E_5}{2}},\\
    \end{cases}
$$


$$
IHS = 
    \begin{cases}
        E_1\ is\ minimum,  \\
        E_3 < E_1,E_3<E_4, \\ 
        E_1,E_5 \in{[98.5\%,101.05\%]*\frac{E_1+E_5}{2}},\\
        E_2,E_4 \in{[98.5\%,101.05\%]*\frac{E_2+E_5}{2}},\\
    \end{cases}
$$

2. 发散形态（顶部发散和底部发散）
$$
BTOP = 
    \begin{cases}
        E_1\ is\ maximum,  \\
        E_1 < E_3 <E_5, \\ 
        E_2>E_4,\\
    \end{cases}
$$

$$
BBOP = 
    \begin{cases}
        E_1\ is\ minimum,  \\
        E_1 > E_3 > E_5, \\ 
        E_2<E_4,\\
    \end{cases}
$$

3. 三角形

$$
TTOP = 
    \begin{cases}
        E_1\ is\ maximum,  \\
        E_1 > E_3 > E_5, \\ 
        E_2 <> E_4,\\
    \end{cases}
$$

$$
TBOP = 
    \begin{cases}
        E_1\ is\ minimum,  \\
        E_1 <> E_3 < E_5, \\ 
        E_2 > E_4,\\
    \end{cases}
$$

4. 矩形

$$
RTOP = 
    \begin{cases}
        E_1\ is\ maximum,  \\
        |E_i - \frac{E_1 + E_3 + E_4}{3}| < 0.75\% * \frac{E_1+E_2+E_3}{3},i \in {1,3,5} \\
        |E_i - \frac{E_2 + E_4}{2}| < 0.75\% * \frac{E_2+E_4}{2},i \in {2,4},\\
        min(E_1,E_3,E_5) > max(E_2,E_4)
    \end{cases}
$$

$$
RBOP = 
    \begin{cases}
        E_1\ is\ minimum,  \\
        |E_i - \frac{E_1 + E_3 + E_4}{3}| < 0.75\% * \frac{E_1+E_2+E_3}{3},i \in {1,3,5} \\
        |E_i - \frac{E_2 + E_4}{2}| < 0.75\% * \frac{E_2+E_4}{2},i \in {2,4},\\
        min(E_1,E_3,E_5) < max(E_2,E_4)
    \end{cases}
$$

## Notebooks

### `source/技术分析算法框架与实战_20220221-0efadb75.ipynb`

# 论文介绍

《Foundations of Technical Analysis》
>Andrew W Lo、Harry Mamaysky和王江提出了一种系统化和自动化的方法，使用非参数核回归方法来进行模式识别，并将该方法应用于1962年至 1996 年的美股数据，以评估技术分析的有效性。通过将股票收益的无条件经验分布与条件分布（给定特定的技术指标，例如：头肩底形态、双底形态）作比较，发现在 31 年的样本期 间内，部分技术指标确实提供了有用的信息，具有实用价值。
>与基本面分析不同，技术分析一直以来饱受争议。然而一些学术研究表明，技术分析能从市场价格中提取 有用的信息。例如，Lo and MacKinlay (1988, 1999)证实了每周的美股指数并非随机游走，过去的价格可以在某种 程度上预测未来收益。技术分析和传统金融工程的一个重要区别在于，技术分析主要通过观察图表进行，而量化金融则依赖于相对完善的数值法。因此，技术分析利用几何工具和形态识别，而量化金融运用数学分析和概率统计。随着近年来金融工程、计算机技术和数值算法等领域的突破，金融工程可以逐步取代不那么严谨的技术分析。技术分析虽饱受质疑却仍能占据一席之地，归功于其视觉分析模式更贴近直观认知，而且在过去，要进行技术分析，首先要认识到价格过程是非线性的，且包含一定的规律和模式。为了定量地捕捉这种规 律，我们首先假定价格过程尚未有严格的算法取代传统的技术分析，如今，成熟的统计算法能够取代传统的几何画图，让技术分析继续以 更新、更严谨的方式服务投资者，同时金融工程领域在分析范式上也得到了丰富。

# 形态识别算法
## 核估计方法

假定价格过程${P_t}$有如下表达形式:

$$P_t=m(X_t)+\epsilon_t,t=1,\dots,T$$

其中$X_t$是状态变量,$m(X_t)$是任意固定但位置的非线性函数,$\epsilon$为白噪声。

为了识别模式,我们令状态变量等于时间$X_{t}=t$,此时,需要用一个光滑函数$\hat{m}(.)$.近似价格过程为了与核回归估计文献中的符号保持一致，我们仍将状态变量记为$X_{t}$。

$\hat{m}(.)$,还需要一个形态识别的算法,以自动识别指数指标。一旦有了算法,就可以应用于不同时段的资产价格,从而评估不同技术指标的有效性。

## 平滑估计量

$\hat{m}=\frac{1}{T}\sum^{T}_{t=1}w_{t}(x)P_{t}$
其中离x较近的$X_t$对应的$P_t$拥有较大的权重$w_{t}(x)$。对于距离的选择，太宽会导致估计量过于平滑而无法显示出$m(⋅)$真正的特性，太窄又会导致估计量的波动较大，无法排除噪声的影响。因此需要通过选择合适的权重$w_{t}(x)$来平衡以上两点。

## 核回归

对于核回归估计量，权重$w_{t}(x)$是通过核密度函数$K(x)$构造的:

$$K(x) \ge 0,\int{K(\mu)}du=1$$

我们可以通过一个参数$h \gt 0$来调整核函数的离散程度,令:

$$K_{h}(x)\equiv\frac{1}{h}K(\mu / h),\int{K_{h}(\mu)du}=1$$

然后定义如下权重系数:

$$w_{t,h}(x) \equiv K_{h}(x-X_{t})/g_{h}(x)$$
$$g_{h}(x) \equiv \frac{1}{T}\sum^{T}_{t=1}K_{h}(x-X_t)$$

其中,平滑系数h也称为带宽,h越大,用于计算加权均值的样本窗口宽度越大。带宽的选取对于任一局部平均方法都很关键，将在下一小节中进行详细讨论。

将上式代入,得到$m(x)$的估计$\hat{m}_{h}(x)$,称为Nadaraya-Waston核估计:

$$\hat{m}_{h}(x)=\frac{1}{T}\sum^{T}_{t=1}w_{t,h}(x)Y_t=\frac{\sum^{T}_{t=1}K_{h}(x-X)Y_t}{\sum^{T}_{t=1}K_{h}(x-X_t)}$$

在特定条件下可以证明，当样本量增大，$\hat{m}_{h}(x)$以多种方式渐进收敛于$m(x)$。该收敛性质对许多核函数都成立，本文将使用最常用的高斯核：

$$K_{h}(x)=\frac{1}{h\sqrt{2\pi}}e^{-x^{2}/2h^{2}}$$

### 带宽(bw)的选择

通过最小化如下函数来选取合适的h:

$$CV(h)=\frac{1}{T}\sum^{T}_{t=1}(P_t-\hat{m}_{h,t})^2$$

其中:

$\hat{m}_{h,t}=\frac{1}{T}\sum^{T}_{t=1}w_{r,h}Y_{r}$

估计量$\hat{m}_{h,t}$是剔除第t个观测得到的估计量，而上式是所有$\hat{m}_{h,t}$的均方误差。对给定的带宽h，CV(h)衡量了核回归估计量的拟合能力。通过最小化CV(h),我们得到的估计量具有一些统计上的优良性质，例如最小渐进均方误差。但由此得到的带宽往往偏大，即基于最小化CV(h) 的$\hat{m}(⋅)$ 给远距离样本过多的权重，导致过渡平滑，丢失了局部信息。经过不断的试验，我们发现最优带宽应取0.3*$h^{*}$,其中$h^{*}=\mathop{argmin}_{h}CV(X)$

### 形态识别算法

1. 头肩形态（头肩顶和头肩底）

$$
HS = 
    \begin{cases}
        E_1\ is\ maximum,  \\
        E_3 > E_1,E_3>E_4, \\ 
        E_1,E_5 \in{[98.5\%,101.05\%]*\frac{E_1+E_5}{2}},\\
        E_2,E_4 \in{[98.5\%,101.05\%]*\frac{E_2+E_5}{2}},\\
    \end{cases}
$$


$$
IHS = 
    \begin{cases}
        E_1\ is\ minimum,  \\
        E_3 < E_1,E_3<E_4, \\ 
        E_1,E_5 \in{[98.5\%,101.05\%]*\frac{E_1+E_5}{2}},\\
        E_2,E_4 \in{[98.5\%,101.05\%]*\frac{E_2+E_5}{2}},\\
    \end{cases}
$$

2. 发散形态（顶部发散和底部发散）
$$
BTOP = 
    \begin{cases}
        E_1\ is\ maximum,  \\
        E_1 < E_3 <E_5, \\ 
        E_2>E_4,\\
    \end{cases}
$$

$$
BBOP = 
    \begin{cases}
        E_1\ is\ minimum,  \\
        E_1 > E_3 > E_5, \\ 
        E_2<E_4,\\
    \end{cases}
$$

3. 三角形

$$
TTOP = 
    \begin{cases}
        E_1\ is\ maximum,  \\
        E_1 > E_3 > E_5, \\ 
        E_2 <> E_4,\\
    \end{cases}
$$

$$
TBOP = 
    \begin{cases}
        E_1\ is\ minimum,  \\
        E_1 <> E_3 < E_5, \\ 
        E_2 > E_4,\\
    \end{cases}
$$

4. 矩形

$$
RTOP = 
    \begin{cases}
        E_1\ is\ maximum,  \\
        |E_i - \frac{E_1 + E_3 + E_4}{3}| < 0.75\% * \frac{E_1+E_2+E_3}{3},i \in {1,3,5} \\
        |E_i - \frac{E_2 + E_4}{2}| < 0.75\% * \frac{E_2+E_4}{2},i \in {2,4},\\
        min(E_1,E_3,E_5) > max(E_2,E_4)
    \end{cases}
$$

$$
RBOP = 
    \begin{cases}
        E_1\ is\ minimum,  \\
        |E_i - \frac{E_1 + E_3 + E_4}{3}| < 0.75\% * \frac{E_1+E_2+E_3}{3},i \in {1,3,5} \\
        |E_i - \frac{E_2 + E_4}{2}| < 0.75\% * \frac{E_2+E_4}{2},i \in {2,4},\\
        min(E_1,E_3,E_5) < max(E_2,E_4)
    \end{cases}
$$

## Local Docs

### `source/README-101bfdd1.md`

<!--
 * @Author: your name
 * @Date: 2022-03-25 09:45:19
 * @LastEditTime: 2022-03-25 09:47:56
 * @LastEditors: Please set LastEditors
 * @Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 * @FilePath: \undefinedc:\Users\Administrator\OneDrive\Knight_Analyze\build_timing_signal\README.md
-->
# 说明

1. Approximation
   1. 基于点位效率理论的个股趋势预测研究的点位划分
   2. 与势的量化研究
2. 形态识别
3. 过往择时信号生成,详见代码

## Code Implementation

- `source/_imports-f52caa12.py`
- `source/Approximation-64e32288.py`
  - Symbols: `_approximation_method, estimate_sign, Approximation, __init__, fit, transform, Mask_dir_peak_valley, __init__, fit, transform, Except_dir, __init__`
- `source/__init__-b578ea69.py`
- `source/technical_analysis_patterns-b5eb49ad.py`
  - Symbols: `rolling_windows, calc_smooth, find_argrelextrema, find_price_patterns, _pattern_HS, _pattern_IHS, _pattern_BTOP, _pattern_BBOT, _pattern_TTOP, _pattern_TBOP, _pattern_RTOP, _pattern_RBOT`
- `source/timing_signal-c538372a.py`
  - Symbols: `RSRS, __init__, calc_basic_rsrs, calc_zscore_rsrs, calc_revise_rsrs, calc_right_skewed_rsrs, calc_insensitivity_rsrs, calc_LLT_MA, calc_OLSTL, _func, FRAMA, HMA`
- `source/main-66843ea7.py`
  - Symbols: `load_data, get_last_patterns, pattern_recognition, block_zx_level2_pattern`
- `source/plotting-069c245a.py`
  - Symbols: `plot_ohlc, get_holidays, get_marker, plot_subplots`
- `source/technical_analysis_patterns-2988a5c5.py`
  - Symbols: `rolling_windows, calc_smooth, find_price_argrelextrema, find_price_patterns, _pattern_HS, _pattern_IHS, _pattern_BTOP, _pattern_BBOT, _pattern_TTOP, _pattern_TBOP, _pattern_RTOP, _pattern_RBOT`
