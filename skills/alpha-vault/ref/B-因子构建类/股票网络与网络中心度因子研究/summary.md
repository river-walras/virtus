# 股票网络与网络中心度因子研究

- Category: `B-因子构建类`
- Bundle Dir: `股票网络与网络中心度因子研究`

## Primary Summary

- Notebook: `source/股票网络中心度因子-a304ebff.ipynb`

# 股票网络与网络中心度因子研究

## 1.1 上市公司彼此之间相互关联共同构成复杂股票网络
上市公司之间由于宏观、中观、微观因素的相互影响，共同构成了股票市场网络，股票网络体现了上市公司经济活动产生的相互依存和相互影响关系。
> 同行业的上市公司，由于受到宏观经济周期、行业景气周期的波动影响，存在着一定的同向性趋势;

产业链上下游的上市公司，企业经营业绩之间存在相互影响；

企业的投资、融资活动，并购及担保行为，也使得不同上市公司之间存在关联关系；

二级市场中投资者的持有、买卖行为使得不同股票之间也存在着交易性关联。

## 1.2 股票网络示例
![bo_d54advn7aajc73fv08sg_3_270_319_1614_1347_0.jpg](docs/images/bo_d54advn7aajc73fv08sg_3_270_319_1614_1347_0.jpg)

## 1.3 基于Pearson相关系数构建股票连接网络
股票市场中不同股票之间存在互相影响, 每只股票的价格波动并非单一的受自身的基本面影响，同时也受到其他股票价格波动的影响。如果将股票市场看作一个复杂网络 ，那么不同股票可以视为网络中的节点，两只股票价格波动之间的相关性便是两者之间的连边。

本文中我们使用Pearson相关系数来衡量股票之间价格波动的相关性，进而构建股票连接网络。对于给定股票i和j,令 ${\rho }_{{ij}, t}\left( {\Delta t}\right)$ 表示两只股票的Pearson相关系数，

$$
{\rho }_{{ij}, t}\left( {\Delta t}\right)  = \frac{\operatorname{cov}\left( {{r}_{j},{r}_{j}}\right) }{\sqrt{\operatorname{Var}\left( {r}_{i}\right)  * \operatorname{Var}\left( {r}_{j}\right) }}
$$

将 $t$ 时刻整个样本空间内N只股票的相关系数构成邻接矩阵 ${W}_{t}\left( {\Delta t}\right)  = {\left\{  {\rho }_{{ij}, t}\left( \Delta t\right) \right\}  }_{N * N}$ 。

在此基础之上, 我们计算不同节点之间的距离

$$
{d}_{{ij}, t}\left( {\Delta t}\right)  = \sqrt{2 * \left( {1 - {\rho }_{{ij}, t}\left( {\Delta t}\right) }\right) }
$$

并得到距离矩阵 ${D}_{t}\left( {\Delta t}\right)  = {\left\{  {d}_{{ij}, t}\left( \Delta t\right) \right\}  }_{N * N}$ 。

> ${d}_{{ij}, t}\left( {\Delta t}\right)$ 与 ${\rho }_{{ij}, t}\left( {\Delta t}\right)$ 负相关，邻接矩阵 ${W}_{t}\left( {\Delta t}\right)$ 和距离矩阵 ${D}_{t}\left( {\Delta t}\right)$ 以不同的方式刻画了股票网络连接，将样本空间内的股票联系起来形成了一个全连接的无向加权网络。

## 2.1 [SCC]基于网络视角的股票风险刻画:空间网络中心度因子

> 网络分析方法在金融领域中广泛用于分析系统性风险和描述金融体系稳定性，张自力等(2020)基于网络分析视角，利用股票回报的相关系数构建股票网络，描述股票市场的拓扑结构和系统性风险的传播路径。

> 本文中我们参考上述方法，基于股票平均相关系数来构建股票网络。计算股票i和股票市场组合中其他股票的平均Pearson相关系数:

$$
{\bar{p}}_{i, t} = \frac{1}{N - 1}\mathop{\sum }\limits_{{j = 1, j \neq  i}}^{{N - 1}}\operatorname{cov}\left( {{r}_{i, t},{r}_{j, t}}\right)
$$

由此, 根据前述股票距离的定义, 我们定义股票i和其他股票的平均距离为

$$
{\bar{d}}_{i, t} = \sqrt{2 * \left( {1 - {\bar{p}}_{i, t}}\right) }
$$

- ${\bar{d}}_{i, t}$ 反映了该股票与其他股票的平均距离，该值越小，说明t时刻股票与其他股票的距离越近, 与其他股票互相影响程度越高, 处在网络的相对中心位置。

我们定义空间网络相对中心度(SCC):

$$
{SCC}_{i, t} = \frac{1}{{\bar{d}}_{i, t}^{2}{}^{2}}
$$

## Notebooks

### `source/股票网络中心度因子-a304ebff.ipynb`

# 股票网络与网络中心度因子研究

## 1.1 上市公司彼此之间相互关联共同构成复杂股票网络
上市公司之间由于宏观、中观、微观因素的相互影响，共同构成了股票市场网络，股票网络体现了上市公司经济活动产生的相互依存和相互影响关系。
> 同行业的上市公司，由于受到宏观经济周期、行业景气周期的波动影响，存在着一定的同向性趋势;

产业链上下游的上市公司，企业经营业绩之间存在相互影响；

企业的投资、融资活动，并购及担保行为，也使得不同上市公司之间存在关联关系；

二级市场中投资者的持有、买卖行为使得不同股票之间也存在着交易性关联。

## 1.2 股票网络示例
![bo_d54advn7aajc73fv08sg_3_270_319_1614_1347_0.jpg](docs/images/bo_d54advn7aajc73fv08sg_3_270_319_1614_1347_0.jpg)

## 1.3 基于Pearson相关系数构建股票连接网络
股票市场中不同股票之间存在互相影响, 每只股票的价格波动并非单一的受自身的基本面影响，同时也受到其他股票价格波动的影响。如果将股票市场看作一个复杂网络 ，那么不同股票可以视为网络中的节点，两只股票价格波动之间的相关性便是两者之间的连边。

本文中我们使用Pearson相关系数来衡量股票之间价格波动的相关性，进而构建股票连接网络。对于给定股票i和j,令 ${\rho }_{{ij}, t}\left( {\Delta t}\right)$ 表示两只股票的Pearson相关系数，

$$
{\rho }_{{ij}, t}\left( {\Delta t}\right)  = \frac{\operatorname{cov}\left( {{r}_{j},{r}_{j}}\right) }{\sqrt{\operatorname{Var}\left( {r}_{i}\right)  * \operatorname{Var}\left( {r}_{j}\right) }}
$$

将 $t$ 时刻整个样本空间内N只股票的相关系数构成邻接矩阵 ${W}_{t}\left( {\Delta t}\right)  = {\left\{  {\rho }_{{ij}, t}\left( \Delta t\right) \right\}  }_{N * N}$ 。

在此基础之上, 我们计算不同节点之间的距离

$$
{d}_{{ij}, t}\left( {\Delta t}\right)  = \sqrt{2 * \left( {1 - {\rho }_{{ij}, t}\left( {\Delta t}\right) }\right) }
$$

并得到距离矩阵 ${D}_{t}\left( {\Delta t}\right)  = {\left\{  {d}_{{ij}, t}\left( \Delta t\right) \right\}  }_{N * N}$ 。

> ${d}_{{ij}, t}\left( {\Delta t}\right)$ 与 ${\rho }_{{ij}, t}\left( {\Delta t}\right)$ 负相关，邻接矩阵 ${W}_{t}\left( {\Delta t}\right)$ 和距离矩阵 ${D}_{t}\left( {\Delta t}\right)$ 以不同的方式刻画了股票网络连接，将样本空间内的股票联系起来形成了一个全连接的无向加权网络。

## 2.1 [SCC]基于网络视角的股票风险刻画:空间网络中心度因子

> 网络分析方法在金融领域中广泛用于分析系统性风险和描述金融体系稳定性，张自力等(2020)基于网络分析视角，利用股票回报的相关系数构建股票网络，描述股票市场的拓扑结构和系统性风险的传播路径。

> 本文中我们参考上述方法，基于股票平均相关系数来构建股票网络。计算股票i和股票市场组合中其他股票的平均Pearson相关系数:

$$
{\bar{p}}_{i, t} = \frac{1}{N - 1}\mathop{\sum }\limits_{{j = 1, j \neq  i}}^{{N - 1}}\operatorname{cov}\left( {{r}_{i, t},{r}_{j, t}}\right)
$$

由此, 根据前述股票距离的定义, 我们定义股票i和其他股票的平均距离为

$$
{\bar{d}}_{i, t} = \sqrt{2 * \left( {1 - {\bar{p}}_{i, t}}\right) }
$$

- ${\bar{d}}_{i, t}$ 反映了该股票与其他股票的平均距离，该值越小，说明t时刻股票与其他股票的距离越近, 与其他股票互相影响程度越高, 处在网络的相对中心位置。

我们定义空间网络相对中心度(SCC):

$$
{SCC}_{i, t} = \frac{1}{{\bar{d}}_{i, t}^{2}{}^{2}}
$$

## Local Docs

### `source/README-41367ecc.md`

# 股票网络与网络中心度因子研究

## 项目简介

本项目是**华西证券金融工程专题研究**的复现实现，基于复杂网络理论，通过分析股票间的相关性构建股票网络，并计算网络中心度因子用于选股策略。

**核心研究论文**：华西证券金融工程专题报告（2021年3月）《股票网络与网络中心度因子研究》

### 核心因子

- **SCC（Spatial Centrality Centrality）**：空间网络中心度因子
  - 基于股票间Pearson相关系数的平均距离
  - SCC值越大，股票在网络中越中心

- **TCC（Temporal Centrality Centrality）**：时间网络中心度因子
  - 基于收益率偏离的时间稳定性
  - TCC值越大，股票收益率越稳定

- **CC（Composite Centrality）**：综合网络中心度因子
  - SCC与TCC的1:1合成
  - 综合考虑空间和时间维度的网络中心度

## 项目状态

✅ **核心算法已完成，进入测试验证阶段**

### 已完成功能

- ✅ SCC因子计算（`src/factor_algo.py:calculate_scc`）
- ✅ TCC因子计算（`src/factor_algo.py:calculate_tcc`）
- ✅ CC因子合成（`src/generator.py:get_cc_factor`）
- ✅ 滑动窗口因子生成器（`src/factor_algo.py:generate_factor`）
- ✅ NetworkCentralityFactor类（`src/generator.py`）
- ✅ 因子分析模块（`src/analyze.py`）
  - factor_group_analysis() 便捷函数
  - FactorAnalyzer 分析器类
- ✅ 完整的中文文档（Sphinx规范）
- ✅ 性能优化和错误处理

### 待实现功能

- ⚠️ 单元测试（tests/）
- ⚠️ 回测验证

## 快速开始

### 环境配置

```bash
# 激活Python环境
conda activate [your-environment]

# 安装依赖
pip install pandas numpy qlib alphalens loguru tqdm psutil pytest

# 设置PYTHONPATH
export PYTHONPATH="/data1/hugo/workspace:/data1/hugo/workspace/qlib_ddb:$PYTHONPATH"
```

### 基础使用

```python
import numpy as np
import pandas as pd
from src.factor_algo import calculate_scc, calculate_tcc, generate_factor

# 1. 准备收益率数据
np.random.seed(42)
dates = pd.date_range('2020-01-01', periods=100, freq='D')
stocks = [f'stock_{i:03d}' for i in range(50)]
returns = pd.DataFrame(
    np.random.randn(100, 50) * 0.02,
    index=dates,
    columns=stocks
)

# 2. 计算SCC因子时间序列（20天滑动窗口）
scc_factor = generate_factor(returns, calculate_scc, window=20)

# 3. 计算TCC因子时间序列
tcc_factor = generate_factor(returns, calculate_tcc, window=20)

print(f"SCC因子形状: {scc_factor.shape}")  # (81, 50)
print(f"TCC因子形状: {tcc_factor.shape}")  # (81, 50)
```

### 实际数据示例

```python

### `source/20210316-华西证券-金融工程专题报告-股票网络与网络中心度因子研究-f3ad6f13.md`

股票网络与网络中心度因子研究

曹春晓 SAC NO:S1120520070003

杨国平 SAC NO: S1120520070002

2021年3月14日

请仔细阅读在本报告尾部的重要法律声明

## 目录

1. 基于Pearson相关系数构建股票连接网络

2. 股票网络中心度选股因子构建及测试

3. 风险提示

### 1.1 上市公司彼此之间相互关联共同构成复杂股票网络

上市公司之间由于宏观、中观、微观因素的相互影响，共同构成了股票市场网络，股票网络体现了上市公司经济活动产生的相互依存和相互影响关系。

$>$ 同行业的上市公司，由于受到宏观经济周期、行业景气周期的波动影响，存在着一定的同向性趋势;

> 同行业的上市公司又因为彼此竞争与互补关系，存在一定的互斥趋势；

产业链上下游的上市公司，企业经营业绩之间存在相互影响；

企业的投资、融资活动，并购及担保行为，也使得不同上市公司之间存在关联关系；

二级市场中投资者的持有、买卖行为使得不同股票之间也存在着交易性关联。

### 1.2 股票网络示例

图1: 产业链、投融资、行业等视角构成的股票网络关系

![bo_d54advn7aajc73fv08sg_3_270_319_1614_1347_0.jpg](images/bo_d54advn7aajc73fv08sg_3_270_319_1614_1347_0.jpg)

资料来源:Wind，华西证券研究所

### 1.3 基于Pearson相关系数构建股票连接网络

股票市场中不同股票之间存在互相影响, 每只股票的价格波动并非单一的受自身的基本面影响，同时也受到其他股票价格波动的影响。如果将股票市场看作一个复杂网络 ，那么不同股票可以视为网络中的节点，两只股票价格波动之间的相关性便是两者之间的连边。

本文中我们使用Pearson相关系数来衡量股票之间价格波动的相关性，进而构建股票连接网络。对于给定股票i和j,令 ${\rho }_{{ij}, t}\left( {\Delta t}\right)$ 表示两只股票的Pearson相关系数，

$$
{\rho }_{{ij}, t}\left( {\Delta t}\right)  = \frac{\operatorname{cov}\left( {{r}_{j},{r}_{j}}\right) }{\sqrt{\operatorname{Var}\left( {r}_{i}\right)  * \operatorname{Var}\left( {r}_{j}\right) }}
$$

将 $t$ 时刻整个样本空间内N只股票的相关系数构成邻接矩阵 ${W}_{t}\left( {\Delta t}\right)  = {\left\{  {\rho }_{{ij}, t}\left( \Delta t\right) \right\}  }_{N * N}$ 。

在此基础之上, 我们计算不同节点之间的距离

$$
{d}_{{ij}, t}\left( {\Delta t}\right)  = \sqrt{2 * \left( {1 - {\rho }_{{ij}, t}\left( {\Delta t}\right) }\right) }
$$

并得到距离矩阵 ${D}_{t}\left( {\Delta t}\right)  = {\left\{  {d}_{{ij}, t}\left( \Delta t\right) \right\}  }_{N * N}$ 。

> ${d}_{{ij}, t}\left( {\Delta t}\right)$ 与 ${\rho }_{{ij}, t}\left( {\Delta t}\right)$ 负相关，邻接矩阵 ${W}_{t}\left( {\Delta t}\right)$ 和距离矩阵 ${D}_{t}\left( {\Delta t}\right)$ 以不同的方式刻画了股票网络连接，将样本空间内的股票联系起来形成了一个全连接的无向加权网络。

### 1.4 基于平面最大过滤图(PMFG)简化网络

全连接网络显示了股票网络中所有节点的相关关系，但实际中有些节点相关性可能比较弱，存在较多的噪音和次要信息，我们可以通过最小生成树(MST)或平面最大过滤图 (PMFG) 等方法进行简化网络。

### `source/analyze使用指南-80215700.md`

# analyze.py 使用指南

**版本**: 1.1.0
**更新日期**: 2025-12-25
**作者**: Hugo

## 更新日志

- **v1.1.0** (2025-12-25): 新增灵活的数据过滤控制功能
  - 添加 `filter_suspended` 和 `filter_limit` 参数
  - 支持自定义停牌和涨跌停股票的过滤行为
  - 更新文档和使用示例

- **v1.0.0** (2025-12-24): 初始版本
  - 完整的因子分析功能
  - factor_group_analysis() 便捷函数
  - FactorAnalyzer 分析器类

## 目录

1. [快速开始](#快速开始)
2. [接口对比](#接口对比)
3. [数据过滤控制](#数据过滤控制) ⭐ **新增**
4. [使用场景](#使用场景)
5. [完整示例](#完整示例)
6. [最佳实践](#最佳实践)
7. [常见问题](#常见问题)
8. [API参考](#api参考)

---

## 快速开始

### 5分钟上手示例

```python
from src.analyze import factor_group_analysis

# 1. 准备因子数据（MultiIndex [date, instrument]）
# 假设已经有 factor_data，包含 'scc' 列
factor_data = ...  # 你的因子数据

# 2. 一键分析
pred_label_df, pivot_df = factor_group_analysis(
    factor_data,
    factor_col='scc',      # 因子列名
    group_count=10         # 分10组
)

# 3. 查看结果
print("分组收益：")
print(pivot_df.head())
```

**输出结果**：
```
分组收益：
factor_quantile    1    2    3   ...   10
date
2020-01-21      0.02 0.01 0.00 ... -0.01
2020-01-22      0.01 0.02 0.01 ...  0.00
...
```

---

## 接口对比

### 方式1：便捷函数 `factor_group_analysis()`

**适合**：快速分析、一次性计算

**特点**：
- ✅ **简单**：一行代码完成分析
- ✅ **自动推断**：自动从数据推断股票池和日期范围
- ✅ **零配置**：无需手动创建对象

**示例**：
```python
from src.analyze import factor_group_analysis

# 单次分析
pred_label_df, pivot_df = factor_group_analysis(
    factor_data,
    factor_col='scc',
    group_count=10
)
```

### 方式2：分析器类 `FactorAnalyzer`

**适合**：批量计算、需要更多控制

**特点**：
- ✅ **可重用**：同一实例可分析多个因子
- ✅ **可扩展**：可访问中间步骤，自定义流程
- ✅ **高效**：可重用 data_provider，减少初始化开销

**示例**：
```python
from src.analyze import FactorAnalyzer

# 创建分析器
analyzer = FactorAnalyzer()

# 批量分析多个因子
factors = ['scc', 'tcc', 'cc']
results = {}

for factor_col in factors:
    pred_label_df, pivot_df = analyzer.analyze(
        factor_data[[factor_col]],  # 只传入需要的列
        factor_col=factor_col
    )

### `source/使用指南_网络中心度因子-1e8e886f.md`

# 股票网络中心度因子使用指南

**版本**: 1.0.0
**更新日期**: 2025-12-24
**作者**: Hugo

## 目录

1. [快速开始](#快速开始)
2. [核心算法详解](#核心算法详解)
3. [因子生成器使用](#因子生成器使用)
4. [完整工作流示例](#完整工作流示例)
5. [高级用法](#高级用法)
6. [最佳实践](#最佳实践)
7. [常见问题](#常见问题)
8. [API参考](#api参考)

---

## 快速开始

### 5分钟上手示例

```python
from src.generator import NetworkCentralityFactor

# 1. 初始化因子生成器
factor_engine = NetworkCentralityFactor(
    codes="csi300",              # 沪深300成分股
    start_date="2020-01-01",
    end_date="2023-12-31"
)

# 2. 获取数据
factor_engine.fetch_data()

# 3. 计算因子（一键获取所有因子）
factors = factor_engine.calculate_factors_separately(
    factor_types=['scc', 'tcc', 'cc'],
    window=20
)

# 4. 查看结果
print(f"SCC因子形状: {factors['scc'].shape}")
print(f"TCC因子形状: {factors['tcc'].shape}")
print(f"CC因子形状: {factors['cc'].shape}")

# 5. 清理内存
factor_engine.cleanup_memory()
```

### 运行结果

```
SCC因子形状: (972, 300)  # 972个交易日，300只股票
TCC因子形状: (972, 300)
CC因子形状: (972, 300)
```

---

## 核心算法详解

### 1. SCC因子（空间网络中心度）

#### 原理

SCC因子基于股票间Pearson相关系数的平均距离，反映股票在网络中的中心程度。

**计算公式**：
```
SCC_i = 1 / [2 * (1 - ρ̄_i)]
```

其中 `ρ̄_i` 是股票i与其他所有股票的平均相关系数。

**业务含义**：
- SCC值大：股票与市场中其他股票的相关性强，处于网络中心位置
- SCC值小：股票相对独立，与其他股票相关性弱，处于网络边缘

#### 直接使用核心算法

```python
import numpy as np
from src.factor_algo import calculate_scc

# 准备收益率数据：20天，100只股票
np.random.seed(42)
returns = np.random.randn(20, 100) * 0.02  # shape: (20, 100)

# 计算SCC因子
scc_values = calculate_scc(returns)

print(f"SCC因子值: {scc_values.shape}")  # (100,)
print(f"SCC因子范围: [{scc_values.min():.4f}, {scc_values.max():.4f}]")
```

#### 论文回测结果（全市场）

- IC均值：8.30%
- IC_IR：3.97
- 多空组合年化收益：26.80%
- 最大回撤：-1.79%

### 2. TCC因子（时间网络中心度）

#### 原理

TCC因子基于收益率偏离的时间稳定性，反映股票收益率随时间的波动程度。

**计算公式**：
```
TCC_i = 1 / E[z²]
```

其中 `z` 是收益率相对市场平均的标准化偏离度，`E[z²]` 是时间维度上的平均平方偏离。

**业务含义**：
- TCC值大：股票收益率相对市场平均的偏离小，波动稳定
- TCC值小：股票收益率波动大，与市场平均偏离度高

## Code Implementation

- `source/__init__-f57c5537.py`
- `source/analyze-a5e1da7a.py`
  - Symbols: `factor_group_analysis, FactorAnalyzer, __init__, _infer_parameters, fetch_forward_returns, filter_tradable, merge_data, apply_grouping, analyze`
- `source/data_provider-165a3341.py`
  - Symbols: `QlibConfig, QlibDataProvider, init_qlib_once, __init__, _parse_instruments, get_features, load_data`
- `source/factor_algo-a59fed37.py`
  - Symbols: `calculate_scc, calculate_tcc, generate_factor`
- `source/generator-1fb97f72.py`
  - Symbols: `NetworkCentralityFactor, __init__, fetch_data, get_scc_factor, get_tcc_factor, get_cc_factor, calculate_factors_separately, cleanup_memory, __repr__`
