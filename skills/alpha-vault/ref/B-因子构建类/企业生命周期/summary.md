# 企业生命周期

- Category: `B-因子构建类`
- Bundle Dir: `企业生命周期`

## Primary Summary

- Notebook: `source/企业生命周期测试-d82c6aa1.ipynb`

# 一、探索生命周期划分方法

根据企业生命周期理论，企业如同一个生命有机体，一般会经历导入、成长、成熟和 衰退等阶段，处于不同生命周期阶段的企业具有不同的特征。从投资者的角度来看， 针对处于不同阶段的企业，对其投资价值的考察标准应当也有所不同。本文就这一问 题，尝试分析处在各个不同生命周期的企业群体中的因子的有效性，从而更好地运用 因子投资的方法来筛选出具有超额收益的个股。首先，我们需要对上市公司进行生命周期的划分,常见的生命周期划分方法如下。

_[embedded image omitted]_

## 1.1 行业周期定位法
行业周期定位法，顾名思义，就是根据行业所处的生命周期来判断业内企业的生命周期。 例如，如果判断银行行业处于成熟阶段，那么所有银行企业都被划分入成熟这一阶段。 这样的划分方法相对简单直接，但同时存在两个缺点。一方面，主观判断容易对划分结 果形成较大影响，无法进行有效的历史回溯，进而无从通过实证研究验证相关逻辑。另 一方面，这种划分方式更偏静态，忽视了企业本身所处生命周期的动态变化。此外，同 一行业下的企业可能所处的经营周期是不同的，即使是在成熟的行业中，也可能存在初创企业正处在导入期。

## 1.2 变量分析法

变量分析法可分为单变量分析法和综合指标分析法。例如，DeAngelo（2006）采用留 存收益/净资产（或者总资产）作为划分企业生命周期的依据，根据研究股利支付行为来 判断企业所在阶段。Anthony（1992）、Chiung-Ju Liang（2011）、孙建强等（2003） 宋常和刘司慧（2011）等人都通过诸如营销费用率、销售增长率、高管持股比率、公司 年龄和运营能力等指标，通过设定打分标准给每个指标进行打分，而后利用公司得分所在区间来判断生命周期。


这一类生命周期定位法可以综合考虑多个指标，但存在的缺陷也显而易见，在得分的 设计标准上过于主观，我们需要人为构建单个财务指标的得分标准，以及总得分映射 到生命周期不同阶段的标准。并且，哪些指标需要被考虑，指标间是否等价，也同样
需要制定者做出主观判断。

## 1.3 象限划分法

本文我们将提出一种新的企业生命周期划分法，即以ROE为横轴、营收增长1为纵轴构 建二维坐标系，并根据企业所处象限来划分其经验生命周期。这样划分的逻辑较为直观 和清楚，符合投资者惯用的投资理念，并且可以刻画出生命周期变化是一个连续的过程。 具体来说，当企业从导入期介入某一产业，企业初始的营业收入基数较低，因此营收增 长率处于较高的阶段；但其资本回报率较低，ROE 处在较低的水平，此时企业处于导 入期，即坐标系的左上方。随后，经过一定时期的发展，企业持续高增长，带动资本回报率上升，ROE 水平有所提升。此时企业处于成长期，即坐标系的右上方。而当企业渗透率和竞争格局达到较为稳定时，必然面临增长率放缓的情况，此时企业就由成长期 转入成熟期，位于坐标系的右下方。而当企业由于自身或产业原因，盈利能力出现下滑
时，则进入了衰退期，即坐标系的左下方。

_[embedded image omitted]_

这里说一下细节：

1. **ROE为ROE_TTM,营收增长为三年复合营收增长率(回归法)**;
2. **未修正的象限使用的两个指标的中位数确定；**
3. **修正的象限为营收对ROE做的回归拟合**

## Notebooks

### `source/企业生命周期测试-d82c6aa1.ipynb`

# 一、探索生命周期划分方法

根据企业生命周期理论，企业如同一个生命有机体，一般会经历导入、成长、成熟和 衰退等阶段，处于不同生命周期阶段的企业具有不同的特征。从投资者的角度来看， 针对处于不同阶段的企业，对其投资价值的考察标准应当也有所不同。本文就这一问 题，尝试分析处在各个不同生命周期的企业群体中的因子的有效性，从而更好地运用 因子投资的方法来筛选出具有超额收益的个股。首先，我们需要对上市公司进行生命周期的划分,常见的生命周期划分方法如下。

_[embedded image omitted]_

## 1.1 行业周期定位法
行业周期定位法，顾名思义，就是根据行业所处的生命周期来判断业内企业的生命周期。 例如，如果判断银行行业处于成熟阶段，那么所有银行企业都被划分入成熟这一阶段。 这样的划分方法相对简单直接，但同时存在两个缺点。一方面，主观判断容易对划分结 果形成较大影响，无法进行有效的历史回溯，进而无从通过实证研究验证相关逻辑。另 一方面，这种划分方式更偏静态，忽视了企业本身所处生命周期的动态变化。此外，同 一行业下的企业可能所处的经营周期是不同的，即使是在成熟的行业中，也可能存在初创企业正处在导入期。

## 1.2 变量分析法

变量分析法可分为单变量分析法和综合指标分析法。例如，DeAngelo（2006）采用留 存收益/净资产（或者总资产）作为划分企业生命周期的依据，根据研究股利支付行为来 判断企业所在阶段。Anthony（1992）、Chiung-Ju Liang（2011）、孙建强等（2003） 宋常和刘司慧（2011）等人都通过诸如营销费用率、销售增长率、高管持股比率、公司 年龄和运营能力等指标，通过设定打分标准给每个指标进行打分，而后利用公司得分所在区间来判断生命周期。


这一类生命周期定位法可以综合考虑多个指标，但存在的缺陷也显而易见，在得分的 设计标准上过于主观，我们需要人为构建单个财务指标的得分标准，以及总得分映射 到生命周期不同阶段的标准。并且，哪些指标需要被考虑，指标间是否等价，也同样
需要制定者做出主观判断。

## 1.3 象限划分法

本文我们将提出一种新的企业生命周期划分法，即以ROE为横轴、营收增长1为纵轴构 建二维坐标系，并根据企业所处象限来划分其经验生命周期。这样划分的逻辑较为直观 和清楚，符合投资者惯用的投资理念，并且可以刻画出生命周期变化是一个连续的过程。 具体来说，当企业从导入期介入某一产业，企业初始的营业收入基数较低，因此营收增 长率处于较高的阶段；但其资本回报率较低，ROE 处在较低的水平，此时企业处于导 入期，即坐标系的左上方。随后，经过一定时期的发展，企业持续高增长，带动资本回报率上升，ROE 水平有所提升。此时企业处于成长期，即坐标系的右上方。而当企业渗透率和竞争格局达到较为稳定时，必然面临增长率放缓的情况，此时企业就由成长期 转入成熟期，位于坐标系的右下方。而当企业由于自身或产业原因，盈利能力出现下滑
时，则进入了衰退期，即坐标系的左下方。

_[embedded image omitted]_

这里说一下细节：

1. **ROE为ROE_TTM,营收增长为三年复合营收增长率(回归法)**;
2. **未修正的象限使用的两个指标的中位数确定；**
3. **修正的象限为营收对ROE做的回归拟合**

## Code Implementation

- `source/__init__-652cf0bb.py`
- `source/composition_factor-a2c210e4.py`
  - Symbols: `compute_forward_returns, calc_information_coefficient, src_ic, calc_ols, _ols, src_ols, _build_halflife_wight, _explicit_solutions_icir, _opt_icir, _target_cov_func, _target_ledoit_func, fac_eqwt`
- `source/ipca-4f3d5a55.py`
  - Symbols: `InstrumentedPCA, __init__, fit, get_factors, fit_path, predict, predict_panel, predict_portfolio, score, BS_Walpha, BS_Wbeta, BS_Wdelta`
- `source/__init__-0cbd878b.py`
- `source/_imports-ce04e4d3.py`
- `source/analyze_func-be92414b.py`
  - Symbols: `get_information_table, analyze_factor_res, __init__, get_calc, calc_ic, get_factor_res, get_factor_res2namedtuple, value_at_risk, perf_stats, get_com_returns, get_com_frame, get_factor_target_group_returns`
- `source/get_dataset-fab4ca5b.py`
  - Symbols: `get_data, _dump_dichotomy, _dump_quadrant, _dump_factor, _dump_price, load_data`
- `source/my_factor-c9a38c8e.py`
  - Symbols: `calc_ols_growth, calc_growth, StandardScaler, quadrant, calc, VolAvg, calc, VolCV, calc, RealizedSkewness, calc, ILLIQ`
- `source/my_scr-b65ee2d5.py`
  - Symbols: `_get_dichotomy_dic, _get_quadrant_dic, get_daily_quadrant, get_daily_dichotomy, get_dichotomy, get_quadrant, get_pricing, get_freq_price, trans2frame, _func, get_factors, calc_group_ic`
- `source/plotting-8f802b08.py`
  - Symbols: `highlight_max, highlight_min, plotting_dichotomy_res, GridFigure, __init__, next_row, next_cell, close`
- `source/utils-0653d484.py`
  - Symbols: `get_max_factor_name, rolling_windows, calculate_best_chunk_size, get_factor_columns`
