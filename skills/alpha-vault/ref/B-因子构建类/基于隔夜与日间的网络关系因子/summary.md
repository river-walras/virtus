# 基于隔夜与日间的网络关系因子

- Category: `B-因子构建类`
- Bundle Dir: `基于隔夜与日间的网络关系因子`

## Primary Summary

- Notebook: `source/因子分析-017f83ba.ipynb`

# 独立

# 因子分析

## 未来收益均使用C2C

## Notebooks

### `source/因子分析-017f83ba.ipynb`

# 独立

# 因子分析

## 未来收益均使用C2C

## Local Docs

### `source/README-33c7e315.md`

# 基于隔夜与日间的网络关系因子

本项目实现了基于论文《A tug of war across the market: overnight-vs-daytime lead-lag networks and clustering-based portfolio strategies》的d-LE-SC算法，用于检测金融市场中的领先-滞后关系并构建基于聚类的投资组合策略。

## 🚀 快速开始

### 环境配置
```bash
# 1. 进入项目目录
cd QuantsPlaybook/B-因子构建类/基于隔夜与日间的网络关系因子

# 2. 安装依赖
pip install -r requirements.txt

# 3. 设置DolphinDB连接（如需使用真实数据）
export DOLPHINDB_URI="dolphindb://your_username:your_password@your_host:8848"
```

### 批量因子计算
```bash
# 运行主脚本，自动计算所有组合的因子
python loade_factor.py
```

### 自定义因子计算
```python
from factor_pipeline import FactorPipeline

pipeline = FactorPipeline(
    codes="ashares",
    start_dt="2020-01-01",
    end_dt="2025-10-27",
    window=60,
    network_type="preclose_lead_close",
    correlation_method="spearman"
)

final_factor_df = pipeline.run()
```

---

## 📊 项目状态

- **🎯 当前主入口**: `loade_factor.py` (批量因子计算和保存)
- **⭐ 核心流水线**: `factor_pipeline.py` (FactorPipeline类实现)
- **🚀 GPU加速**: `dlesc_clustering.py` (PyTorch + CUDA支持)
- **📋 开发参考**: `test_main.py` (学习和调试参考)
- **🔧 测试工具**: `test_random_seed_fix.py` (随机种子可复现性测试)

## 项目概述

该研究通过将日收益率分解为隔夜和日间成分，构建有向网络来捕捉股票间隔夜投机与日间价格修正之间的领先-滞后关系。我们开发了专门的d-LE-SC（directed Likelihood Estimation Spectral Clustering）算法来识别有向领先-滞后网络中的领导者股票组和滞后股票组。

## 核心特性

- **d-LE-SC算法实现**: 基于PyTorch的高效实现，支持GPU加速
- **多种网络构建**: 支持隔夜-领先-日间、日间-领先-隔夜、收盘-领先-收盘等网络类型
- **相关性方法选择**: 支持Pearson和Spearman两种相关性计算方法，适应不同数据特征
- **多数据源支持**: 支持模拟数据和qlib真实金融数据
- **组合策略构建**: 基于聚类结果构建多空投资组合
- **因子化改造**: 适合A股市场的因子计算模块，支持多种因子化方案
- **高效工具函数**: 包含内存优化的滑动窗口等实用工具
- **回测分析**: 完整的策略回测框架和性能评估
- **可视化分析**: 丰富的图表展示分析结果

## 项目结构

```
基于隔夜与日间的网络关系因子/
├── 核心代码文件
│   ├── loade_factor.py          # 🎯 主入口脚本（批量因子计算）
│   ├── factor_pipeline.py       # ⭐ FactorPipeline流水线实现
│   ├── dlesc_clustering.py      # 🚀 GPU加速d-LE-SC算法
│   ├── qlib_data_provider.py    # ⭐ qlib数据提供者
│   ├── lead_lag_network.py      # ⭐ 网络构建和相关性计算

### `source/A-tug-of-war-across-the-market-overnight-vs-daytime-lead-lag-networks-and-clustering-based-portfolio-strategies-c3686d4f.md`

# A tug of war across the market: overnight-vs-daytime lead-lag networks and clustering-based portfolio strategies

Yutong Lu ${}^{*1}$ , Ning Zhang ${}^{1}$ , Gesine Reinert ${}^{1,2}$ , and Mihai Cucuringu ${}^{1,2,3,4}$

${}^{1}$ Department of Statistics, University of Oxford

${}^{2}$ The Alan Turing Institute

${}^{3}$ Oxford-Man Institute of Quantitative Finance, University of Oxford

${}^{4}$ Department of Mathematics, University of California Los Angeles

September 16, 2025

## Abstract

In this research, we show that the tug of war is not only at individual stock level but also a networked trading behaviour across the entire market. By decomposing daily returns into overnight and daytime components, we construct directed networks to capture the lead-lag relations between overnight speculations and daytime price corrections, and vice versa, across stocks. We originate a novel clustering-based framework to construct portfolios to capture the cross-stock tug of war. In order to identify disjoint leader and lagger groups in directed lead-lag networks, we develop a specialized spectral clustering algorithm. By generating trading signals exclusively from the leader stocks to predict and trade lagger stocks, we isolate pure cross-stock interactions from autocorrelation within individual stocks. Our empirical results support the conclusion that both noise traders and arbitrageurs trade at the portfolio level and disseminate the tug of war across stocks. With backtests spanning from 2000-01-03 to 2024-12-31, the cross-stock lead-lag portfolios generate remarkable returns and significant alphas on top of portfolios representing firm-level tug-of-war reversals and other the pricing factors. Moreover, the performance of cross-stock lead-lag portfolios grow in recent years, while the stock-specific reversals decay.

### `source/基于隔夜与日间的网络关系因子-d4b899e6.md`

# 基于隔夜与日间的网络关系因子

作者: Yutong Lu、Ning Zhang、Gesine Reinert、Mihai Cucuringu

从个股“拔河”到全市场的“网络拔河”

"拔河效应" (tug of war) 最早由 Lou et al. (2019) 提出，指股票的隔夜收益与日间收益呈现显著负相关:

股票若在隔夜阶段上涨，往往在当日交易时段下跌。研究认为，这反映了两类投资者的冲突:噪声交易者在夜间推动价格偏离，而机构套利者在白天进行修正。

然而，已有文献几乎都停留在单一股票层面。在现实市场中，投资者的交易决策常常是组合化的、板块化的，套利与投机活动可能在多个股票间扩散。那么，这种“拔河”是否也在股票之间发生？是否存在一种“跨股票的网络拔河”现象？

本文正是围绕这一问题展开。作者指出:

“拔河”不仅存在于个股时间序列中，更体现为全市场的网络化行为。

研究目标是:通过构建跨股票的有向相关网络，揭示不同股票之间的Lead-Lag(领先-滞后)关系，并进一步设计基于聚类的投资组合策略，捕捉这种市场层面的动态互动。

研究思路:从网络构建到策略设计的三步框架

作者设计了一个清晰的三步框架，核心思想是一一

隔夜收益预测日间收益，通过网络视角捕捉跨股票信息流动。

收益分解:隔夜 vs. 日间

首先，将每日收益拆分为“隔夜”和“日间”两部分:

$$
\begin{gather} {r}_{i, t}^{cc} = \frac{{P}_{\text{close }, i, t}}{{P}_{\text{close }, i, t - 1}} - 1 \\ {r}_{i, t}^{day} = \frac{{P}_{\text{close }, i, t}}{{P}_{\text{open }, i, t}} - 1,\;{r}_{i, t}^{\text{overnight }} = \frac{1 + {r}_{i, t}^{cc}}{1 + {r}_{i, t}^{day}} - 1 \end{gather}
$$

通过这种分解，作者能够独立观察夜间与日间价格变动对后续市场的影响。

网络构建:跨股票 Lead-Lag 结构

对任意两只股票 $\mathrm{i}\text{、}\mathrm{j}$ ，定义:

$$
{\rho }_{i, j}^{\left( \text{overnight } \rightarrow  \text{ day }\right) } = \operatorname{Corr}\left( {{r}_{i, t}^{\text{overnight }},{r}_{j, t}^{\text{day }}}\right)
$$

这一定义反映股票 i 的隔夜收益是否能预测股票 j 的日间收益。由此形成一个有向加权矩阵 $\mathrm{M}\_ \mathrm{t}$ ，矩阵元素越大，表示“信息传递”越强。矩阵的不对称性自然捕捉了“谁领先、谁跟随”的市场结构。

![bo_d46kdbbef24c73d5p5cg_2_535_66_593_480_0.jpg](images_v/bo_d46kdbbef24c73d5p5cg_2_535_66_593_480_0.jpg)

Figure 1: A lead-lag network.

This figure visualizes the overnight-lead-daytime network on 2001-01-03, with adjacency matrix $\left| {\mathbf{M}}_{{2001} - {01} - {03}}^{\text{overnight-lead-daytime }}\right|$ . Each element represents the absolute value of pairwise correlations between overnight return and the subsequent daytime return. Lighter color indicates higher correlation.

## 聚类与投资组合构建

网络建立后，作者采用定向谱聚类算法 d-LE-SC (directed Likelihood Estimation Spectral Clustering) , 将股票划分为两组:

## Code Implementation

- `source/DeltaLag-bb794bca.py`
  - Symbols: `DeltaLag, __init__, forward`
- `source/__init__-0078c149.py`
- `source/dlesc_clustering-f7c3bb0b.py`
  - Symbols: `_is_convergence_error, DLESCClustering, __init__, _setup_random_generators, _compute_hermitian_matrix, _compute_top_eigenvector, _kmeans_pytorch, _cluster_embeddings, _compute_flows, _update_eta, _determine_lead_lag_direction, fit_single`
- `source/__init__-bacccb3d.py`
- `source/factor_computation-b1372480.py`
  - Symbols: `LeadLagFactorCalculator, __init__, compute_lead_lag_scores, sorted_values, generate_trading_signal, select_top_and_bottom_stocks, compute_factor_values`
- `source/factor_pipeline-4e7c20ae.py`
  - Symbols: `FactorPipeline, __init__, _prepare_data, run, _validate_correlation_method`
- `source/lead_lag_network-f30a0069.py`
  - Symbols: `ParallelConfig, __init__, _get_system_resources, _auto_adjust_n_jobs, _compute_pearson_matrix, _compute_spearman_matrix, compute_rolling_lead_lag, _assess_memory_safety, _safe_parallel_compute, _streaming_compute, LeadLagNetworkBuilder, __init__`
- `source/loade_factor-4bb4349b.py`
  - Symbols: `to_abbr, load_factor`
- `source/qlib_data_provider-fe4b858f.py`
  - Symbols: `QlibConfig, QlibDataProvider, init_qlib_once, __init__, _parse_instruments, _fetch_and_pivot_features, daily_return_df, daytime_return_df, overnight_return_df, get_trade_days`
- `source/utils-c2d145b2.py`
  - Symbols: `SlidingWindowError, InputTooShortError, __init__, InvalidWindowError, sliding_window`
