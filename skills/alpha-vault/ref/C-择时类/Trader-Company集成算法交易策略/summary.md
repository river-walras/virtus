# Trader-Company集成算法交易策略

- Category: `C-择时类`
- Bundle Dir: `Trader-Company集成算法交易策略`

## Primary Summary

- Notebook: `source/Trader_Company-af718850.ipynb`

# 交易员

"交易员"代表了一系列上述 Alpha 的叠加,定义如下:
$$\hat{r_{i}[t+1]}=\sum^{M}_{j=1}w_{j}A_{j}(O_{j}(r_{P_{j}}[t-D_{j}],r_{Q_{j}}[t-F_{j}])) \tag{Eq.1}$$

其中：
- M为交易员所拥有的Alpha数（或其参考的指标数）； 
- $W_{j}$为每一指标的权重； $A_{j}$为该项的激活函数，$A_{j}(x)$表达式可为 x, tanh(x), exp(x), sign(x), ReLU(x)等； 
- $O_{𝑗}$为二元操作符，$𝑂_{𝑗}(𝑥, 𝑦)$表达式可为 x+y, x-y, xy, x, y, max(x,y), min(x,y), x>y, x<y,Corr(x,y); 
- $𝑃_{𝑗}$、$𝑄_{𝑗}$为该项所参考的股票标识，$𝐷_{𝑗}$、$𝐹_{𝑗}$为相应的延迟参数。
- $\theta$代表上述一系列超参数。

|参数|参数解释|取值|
|--|--|--|
|M|每位交易员表达式最大项数,见Eq.1|10|
|$A_{j}(x)$|每一项的激活函数,见Eq.1|x, tanh(x), exp(x),sign(x), ReLU(x)|
|$O_{j}(x)$|一项的二元操作符，见 Eq.1|x+y, x-y, xy, x, y, max(x,y), min(x,y), x>y, x<y,Corr(x,y)|
|$P_{j}$,$Q_{j}$|为预测第j只股票下一期收益所参考的股票|参考股票池内的所有股票|
|$F_{j}$,$D_{j}$|延迟参数,见Eq.1|整数𝑙~ 𝑚𝑎𝑥_𝑙𝑎𝑔 + 𝑙,即 1~10|
|max_lag|数据延迟最大取值|10|
|l|交易延迟量，即观察到数据后不可能立马进行交易，需要再等待𝑙时间|1|
|N|一个投资公司所拥有的交易员数量|100|
|Q|每次投资公司对排名靠后的 Q% 名交易员进行教育或淘汰|50%|
|time_window|投资公司在教育或淘汰交易员时，参考 其过去 time_window时间段内的累积收益|100|

# 投资公司

由于所有Alpha的超额收益均为短暂的，且没有交易员能长期持续跑赢市场，因此 参照现实市场引入“投资公司”这一角色。对于一家拥有N个交易员的投资公司，其最终形成的投资决策需要综合反应 N个交易员的观点。记第n个交易员对第i只股票t+1 时刻收益率的预测值为$\hat{r}^{n}_{i}[t+1]$ ,则投资公司对第i只股票t+1时刻的预测值可形式化地表示为：
$$\hat{r}_{i}=Aggregate(\hat{r}^{1}_{i}[t+1],\dots,\hat{r}^{n}_{i}[t+1],\dots,\hat{r}^{N}_{i}[t+1]) \tag{Eq.2}$$

其中𝐴𝑔𝑔𝑟𝑒𝑔𝑎𝑡𝑒可通过计算
1. N 个交易员预测的平均值，
2. 一段时间内预测准 确率前 50%的交易员的预测平均值
3. 通过神经网络等对交易员预测值进行训练等。

交易员过去一段时间的历史业绩通过以下方式计算：
$$C_{i}[t]=\sum^{t}_{u=0}sign(\hat{r}_{i}[u+1]*r_{i}[u+1]) \tag{Eq.3}$$

其中$C_{i}[t]$为交易员t时间段内的累积业绩，$\hat{r}_{i}[u+1]$为u+1时刻的预测收益率，sign()为符号函数，$\hat{r}_{i}[u+1]$为u+1时刻的实际收益率。当交易员预测 t+1时刻收益率为正时， 以 t 时刻收盘价买入，并在 t+1时刻收盘价卖出；当交易员预测 t+1时刻收益率为负时， 以 t时刻收盘价卖出，并在 t+1时刻收盘价买回。交易员方向预测准确时获得正收益，方 向预测错误时获得负收益，其获取的收益大小仅取决于市场涨跌幅，与预测值本身大小 无关。
投资公司定期对交易员一段时间内的预测准确率进行复盘跟踪，对排名靠后的交易员进行“教育”（即使用最小二乘法优化表达式Eq.1中的权重）。 如交易员被“教育”后仍然表现不佳，则将其淘汰，并基于表现较好的交易员产生新的交易员：以过去一段时间业绩较好的交易员拟合高斯混合分布，并从中抽样产生新晋交易员的参数。对上述过程进行重复迭代即完整的“交易员-投资公司”交易策略模型。

# 一些关键性结论

>First, the pruning step seems quite important (cf. TC w/o prune). Regarding the scores for the pruning, using the MSE instead of the cumulative returns dete-riorates the performance (cf. TC MSE). Second, we can see that introducing the education step also improves the overall performance (cf. TC w/o educate). Otherwise Companies may discard Traders that have possibly good formulae. Lastly, using multimodal distribution in the generation step (Algorithm 3) is quite important.If we instead use a unimodal distribution (cf. TC unimodal), the performance is substantially deteriorated. A possible reason is that a unimodal distribution concentrates around the means of discrete indices, which does not make sense.

## Notebooks

### `source/Trader_Company-af718850.ipynb`

# 交易员

"交易员"代表了一系列上述 Alpha 的叠加,定义如下:
$$\hat{r_{i}[t+1]}=\sum^{M}_{j=1}w_{j}A_{j}(O_{j}(r_{P_{j}}[t-D_{j}],r_{Q_{j}}[t-F_{j}])) \tag{Eq.1}$$

其中：
- M为交易员所拥有的Alpha数（或其参考的指标数）； 
- $W_{j}$为每一指标的权重； $A_{j}$为该项的激活函数，$A_{j}(x)$表达式可为 x, tanh(x), exp(x), sign(x), ReLU(x)等； 
- $O_{𝑗}$为二元操作符，$𝑂_{𝑗}(𝑥, 𝑦)$表达式可为 x+y, x-y, xy, x, y, max(x,y), min(x,y), x>y, x<y,Corr(x,y); 
- $𝑃_{𝑗}$、$𝑄_{𝑗}$为该项所参考的股票标识，$𝐷_{𝑗}$、$𝐹_{𝑗}$为相应的延迟参数。
- $\theta$代表上述一系列超参数。

|参数|参数解释|取值|
|--|--|--|
|M|每位交易员表达式最大项数,见Eq.1|10|
|$A_{j}(x)$|每一项的激活函数,见Eq.1|x, tanh(x), exp(x),sign(x), ReLU(x)|
|$O_{j}(x)$|一项的二元操作符，见 Eq.1|x+y, x-y, xy, x, y, max(x,y), min(x,y), x>y, x<y,Corr(x,y)|
|$P_{j}$,$Q_{j}$|为预测第j只股票下一期收益所参考的股票|参考股票池内的所有股票|
|$F_{j}$,$D_{j}$|延迟参数,见Eq.1|整数𝑙~ 𝑚𝑎𝑥_𝑙𝑎𝑔 + 𝑙,即 1~10|
|max_lag|数据延迟最大取值|10|
|l|交易延迟量，即观察到数据后不可能立马进行交易，需要再等待𝑙时间|1|
|N|一个投资公司所拥有的交易员数量|100|
|Q|每次投资公司对排名靠后的 Q% 名交易员进行教育或淘汰|50%|
|time_window|投资公司在教育或淘汰交易员时，参考 其过去 time_window时间段内的累积收益|100|

# 投资公司

由于所有Alpha的超额收益均为短暂的，且没有交易员能长期持续跑赢市场，因此 参照现实市场引入“投资公司”这一角色。对于一家拥有N个交易员的投资公司，其最终形成的投资决策需要综合反应 N个交易员的观点。记第n个交易员对第i只股票t+1 时刻收益率的预测值为$\hat{r}^{n}_{i}[t+1]$ ,则投资公司对第i只股票t+1时刻的预测值可形式化地表示为：
$$\hat{r}_{i}=Aggregate(\hat{r}^{1}_{i}[t+1],\dots,\hat{r}^{n}_{i}[t+1],\dots,\hat{r}^{N}_{i}[t+1]) \tag{Eq.2}$$

其中𝐴𝑔𝑔𝑟𝑒𝑔𝑎𝑡𝑒可通过计算
1. N 个交易员预测的平均值，
2. 一段时间内预测准 确率前 50%的交易员的预测平均值
3. 通过神经网络等对交易员预测值进行训练等。

交易员过去一段时间的历史业绩通过以下方式计算：
$$C_{i}[t]=\sum^{t}_{u=0}sign(\hat{r}_{i}[u+1]*r_{i}[u+1]) \tag{Eq.3}$$

其中$C_{i}[t]$为交易员t时间段内的累积业绩，$\hat{r}_{i}[u+1]$为u+1时刻的预测收益率，sign()为符号函数，$\hat{r}_{i}[u+1]$为u+1时刻的实际收益率。当交易员预测 t+1时刻收益率为正时， 以 t 时刻收盘价买入，并在 t+1时刻收盘价卖出；当交易员预测 t+1时刻收益率为负时， 以 t时刻收盘价卖出，并在 t+1时刻收盘价买回。交易员方向预测准确时获得正收益，方 向预测错误时获得负收益，其获取的收益大小仅取决于市场涨跌幅，与预测值本身大小 无关。
投资公司定期对交易员一段时间内的预测准确率进行复盘跟踪，对排名靠后的交易员进行“教育”（即使用最小二乘法优化表达式Eq.1中的权重）。 如交易员被“教育”后仍然表现不佳，则将其淘汰，并基于表现较好的交易员产生新的交易员：以过去一段时间业绩较好的交易员拟合高斯混合分布，并从中抽样产生新晋交易员的参数。对上述过程进行重复迭代即完整的“交易员-投资公司”交易策略模型。

# 一些关键性结论

>First, the pruning step seems quite important (cf. TC w/o prune). Regarding the scores for the pruning, using the MSE instead of the cumulative returns dete-riorates the performance (cf. TC MSE). Second, we can see that introducing the education step also improves the overall performance (cf. TC w/o educate). Otherwise Companies may discard Traders that have possibly good formulae. Lastly, using multimodal distribution in the generation step (Algorithm 3) is quite important.If we instead use a unimodal distribution (cf. TC unimodal), the performance is substantially deteriorated. A possible reason is that a unimodal distribution concentrates around the means of discrete indices, which does not make sense.

### `source/Trader_Company-bf2c23ae.ipynb`

# 高斯分布

# 高斯混合

# 贝叶斯

## Code Implementation

- `source/TC-de0b5395.py`
  - Symbols: `ParamsFactory, __init__, create_funcs_params, transform_params2func, _transform_int2func, transform_params2int, _transform_funcs2int, _parameter_bounds_check, trans_funcs2dict, reverse_dict, GenerationFitParams, __init__`
- `source/activation_funcs-fb2c29eb.py`
  - Symbols: `identity, tanh, sign, ReLU, Exp`
- `source/binary_operators-bfed3be5.py`
  - Symbols: `operators_max, operators_min, operators_add, operators_diff, operators_multiple, get_x, get_y, x_is_greater_than_y, Corr`
- `source/utils-1527d69f.py`
  - Symbols: `calc_least_squares, rolling_window, calculate_best_chunk_size`
- `source/activation_funcs-28175a21.py`
  - Symbols: `identity, tanh, sign, ReLU, Exp`
- `source/binary_operators-7d55c015.py`
  - Symbols: `operators_max, operators_min, operators_add, operators_diff, operators_multiple, get_x, get_y, x_is_greater_than_y, Corr`
- `source/company-48bfc309.py`
  - Symbols: `Company, __init__, fit, educate, predict, prune_and_generate, get_bad_trader_flag, aggregate, _get_trader_prediction, _get_mse, _get_stack_params, _get_stack_factor_num`
- `source/trader-4d38be09.py`
  - Symbols: `Trader, __init__, get_params, _transform_funcs2int, reset_params, calc_bulk_factors, calc_factors, get_y_pred, learn, get_current_predict, evaluation, calc_returns`
- `source/utils-9fa8ce57.py`
  - Symbols: `core_vector_formula, create_vector_formulae, core_formula, create_formulae, calc_ols_func, rolling_window, create_empty_lists, double_loop`
