# MLT_TSMOM

- Category: `D-组合优化`
- Bundle Dir: `MLT_TSMOM`

## Primary Summary

- Notebook: `source/mlt_tsmom-f000db63.ipynb`

## 传统动量策略
$$r^{TSMOM,i}_{t,t+1}=sgn(r^{i}_{t-252,t})\frac{\sigma_{tgt}}{\sigma^{i}_{t}}r^{i}_{t,t+1} \tag{1}$$
$$sgn(x):=\begin{cases}1\ if\ x>0,\\
                       0\ if\ x=0, \\
                      -1\ if\ x<0
            \end{cases} \tag{2}$$

其中:
$r^{i}_{t-252,t}$为资产i,t时刻过去一年的收益率;$r^{i}_{t,t+1}$为资产i,t时刻的收益率;$\sigma_{tgt}$目标年化波动率;$\sigma^{i}_{t}$资产i的历史波动率,计算窗口期为60日,使用指数衰减权重计算。

最终资产组合可以表达为:
$$r^{TSMOM}_{t,t+1}=\frac{1}{S_t}\sum^{S_t}_{i=1}r^{TSMOM,i}_{t,t+1} \tag{3}$$

其中:$S_t$为组合在t时刻的标的数量

## 模型架构
[![avatar](https://github.com/hugo2046/QuantsPlaybook/blob/04bb714d9f4af2d6489407b8564926685f69a24b/D-%E7%BB%84%E5%90%88%E4%BC%98%E5%8C%96/MLT_TSMOM/img/mtl%20model.png)](https://github.com/hugo2046/QuantsPlaybook/blob/78ecc7a236e164ee297317ce85a773a0cfcaf190/D-%E7%BB%84%E5%90%88%E4%BC%98%E5%8C%96/MLT_TSMOM/img/mtl%20model.png)

## 时序动量组合

从上文的基于*目标波动率*的传统时序动量策略可以看出,确定每只股票权重有两个因素:动量的方向和股票的波动率。在主要任务钟,我们直接预测股票权重,那么组合的收益率就由上面的上式变为以下等式:
$$r^{\rho}_{t,t+1}=\frac{\sigma_{tgt}}{S_t}\sum^{S_t}_{i=1}\omega^{i}_{t-1,t}r^{i}_{t,t+1} \tag{4}$$

为了控制交易换手,加入惩罚项:

$$r^{\rho}_{t,t+1}=\frac{\sigma_{tgt}}{S_t}\sum^{S_t}_{i=1}\omega^{i}_{t-1,t}r^{i}_{t,t+1}-\tau|\omega^{i}_{t-1,t}-\omega^{i}_{t-2,t-1}| \tag{5}$$

其中:$\tau$为交易手续费,默认设置为3bps,$|\omega^{i}_{t-1,t}-\omega^{i}_{t-2,t-1}|$为资产组合S在t时刻到t+1时刻的权重变化

目标函数(损失函数):
$$L_{SharpeRatio}=-\frac{\mathbb{E}[r^{\rho}]}{\sigma_{r^{\rho}}} \tag{6}$$


## 特征生成

1. Close-to-close volatility estimator,$\sigma_{ctc}$
2. Parkinson volatility estimator, $\sigma_{\rho}$ (Parkinson, 1980)
3. Garman-Klass volatility estimator, $\sigma_{gk}$ (Garman & Klass, 1980)
4. Rogers-Satchell volatility estimator, $\sigma_{rs}$ (Rogers & Satchell, 1991)
5. Yang-Zhang volatility estimator, $\sigma_{yz}$ (Yang & Zhang, 2000)

### 公式

公式参考:
> Exploring the predictability of range-based volatility estimators using RNNs

[volatility-trading](https://github.com/jasonstrimpel/volatility-trading/tree/master/volatility/models)

Close-to-close volatility:$\sqrt{\frac{1}{N-1}\sum^{T}_{i=1}(ln(\frac{c_i}{c_{i-1}}-\overline{\frac{c_t}{c_{t-1}}})^2)}$

Parkinson volatility:$\sqrt{\frac{1}{4Tln2}\sum^{T}_{i=1}(ln\frac{h_{i}}{l_{i}})^2}$

Garman-Klass Volatility:$\sqrt{\frac{1}{T}\sum^{T}_{i=1}(0.5*ln(\frac{h_{i}}{l_{i}})^2-(2ln(2)-1)ln(\frac{c_i}{o_{i}})^2)}$

Rogers-Satchell Volatility:$\sqrt{\frac{1}{T}\sum^{T}_{i=1}(ln(\frac{h_i}{o_i})(ln(\frac{h_i}{o_i})-ln(\frac{c_i}{o_i}))+ln(\frac{l_i}{o_i})(ln(\frac{l_i}{o_i})-ln(\frac{c_i}{o_i}))}$

Yang-Zhang volatility:

$\sqrt{\frac{1}{N-1}\sum^{T}_{i=1}(ln(\frac{o_i}{c_{i-1}})-\overline{ln(\frac{o_i}{c_{i-1}})})^2+\frac{k}{N-1}\sum^{T}_{i=1}(ln(\frac{c_i}{o_{i-1}})-\overline{ln(\frac{c_i}{o_{i-1}})})^2+(1-k)V_{RS}}$

其中:
$k=\frac{0.34}{1.34+\frac{N+1}{N-1}}$

$V_{RS}=\frac{1}{N}\sum^{N}_{i=1}(ln(\frac{h_i}{o_i})(ln(\frac{h_i}{o_i})-ln(\frac{c_i}{o_i}))+ln(\frac{l_i}{o_i})(ln(\frac{l_i}{o_i})-ln(\frac{c_i}{o_i})))$

$o_{i},c_{i},h_{i},l_{i}$分别为i时刻的OHLC数据

特征部分的损失函数就是最小化已实现波动率与预测波动率之间的负相关系数:
$$L_{corr(y,\hat{y})}=-\frac{S_{y,\hat{y}}}{S_{y}*S_{\hat{y}}} \tag{7}$$

整体任务的损失函数

$$L_{total}=-\mu\frac{\mathbb{E}[r^{\rho}]}{\sigma_{r^{\rho}}}+\lambda\sum_{h \in H}-\frac{S_{y_{h},\hat{y_{h}}}}{S_{y_{h}}\cdot S_{\hat{y_h}}}$$

其中$\mu$和$\lambda$为权重,取值在[0,1]之间,$\mu+\lambda=1$,这里进行简单处理$\mu=0.5,\lambda=0.5$

## Notebooks

### `source/mlt_tsmom-f000db63.ipynb`

## 传统动量策略
$$r^{TSMOM,i}_{t,t+1}=sgn(r^{i}_{t-252,t})\frac{\sigma_{tgt}}{\sigma^{i}_{t}}r^{i}_{t,t+1} \tag{1}$$
$$sgn(x):=\begin{cases}1\ if\ x>0,\\
                       0\ if\ x=0, \\
                      -1\ if\ x<0
            \end{cases} \tag{2}$$

其中:
$r^{i}_{t-252,t}$为资产i,t时刻过去一年的收益率;$r^{i}_{t,t+1}$为资产i,t时刻的收益率;$\sigma_{tgt}$目标年化波动率;$\sigma^{i}_{t}$资产i的历史波动率,计算窗口期为60日,使用指数衰减权重计算。

最终资产组合可以表达为:
$$r^{TSMOM}_{t,t+1}=\frac{1}{S_t}\sum^{S_t}_{i=1}r^{TSMOM,i}_{t,t+1} \tag{3}$$

其中:$S_t$为组合在t时刻的标的数量

## 模型架构
[![avatar](https://github.com/hugo2046/QuantsPlaybook/blob/04bb714d9f4af2d6489407b8564926685f69a24b/D-%E7%BB%84%E5%90%88%E4%BC%98%E5%8C%96/MLT_TSMOM/img/mtl%20model.png)](https://github.com/hugo2046/QuantsPlaybook/blob/78ecc7a236e164ee297317ce85a773a0cfcaf190/D-%E7%BB%84%E5%90%88%E4%BC%98%E5%8C%96/MLT_TSMOM/img/mtl%20model.png)

## 时序动量组合

从上文的基于*目标波动率*的传统时序动量策略可以看出,确定每只股票权重有两个因素:动量的方向和股票的波动率。在主要任务钟,我们直接预测股票权重,那么组合的收益率就由上面的上式变为以下等式:
$$r^{\rho}_{t,t+1}=\frac{\sigma_{tgt}}{S_t}\sum^{S_t}_{i=1}\omega^{i}_{t-1,t}r^{i}_{t,t+1} \tag{4}$$

为了控制交易换手,加入惩罚项:

$$r^{\rho}_{t,t+1}=\frac{\sigma_{tgt}}{S_t}\sum^{S_t}_{i=1}\omega^{i}_{t-1,t}r^{i}_{t,t+1}-\tau|\omega^{i}_{t-1,t}-\omega^{i}_{t-2,t-1}| \tag{5}$$

其中:$\tau$为交易手续费,默认设置为3bps,$|\omega^{i}_{t-1,t}-\omega^{i}_{t-2,t-1}|$为资产组合S在t时刻到t+1时刻的权重变化

目标函数(损失函数):
$$L_{SharpeRatio}=-\frac{\mathbb{E}[r^{\rho}]}{\sigma_{r^{\rho}}} \tag{6}$$


## 特征生成

1. Close-to-close volatility estimator,$\sigma_{ctc}$
2. Parkinson volatility estimator, $\sigma_{\rho}$ (Parkinson, 1980)
3. Garman-Klass volatility estimator, $\sigma_{gk}$ (Garman & Klass, 1980)
4. Rogers-Satchell volatility estimator, $\sigma_{rs}$ (Rogers & Satchell, 1991)
5. Yang-Zhang volatility estimator, $\sigma_{yz}$ (Yang & Zhang, 2000)

### 公式

公式参考:
> Exploring the predictability of range-based volatility estimators using RNNs

[volatility-trading](https://github.com/jasonstrimpel/volatility-trading/tree/master/volatility/models)

Close-to-close volatility:$\sqrt{\frac{1}{N-1}\sum^{T}_{i=1}(ln(\frac{c_i}{c_{i-1}}-\overline{\frac{c_t}{c_{t-1}}})^2)}$

Parkinson volatility:$\sqrt{\frac{1}{4Tln2}\sum^{T}_{i=1}(ln\frac{h_{i}}{l_{i}})^2}$

Garman-Klass Volatility:$\sqrt{\frac{1}{T}\sum^{T}_{i=1}(0.5*ln(\frac{h_{i}}{l_{i}})^2-(2ln(2)-1)ln(\frac{c_i}{o_{i}})^2)}$

Rogers-Satchell Volatility:$\sqrt{\frac{1}{T}\sum^{T}_{i=1}(ln(\frac{h_i}{o_i})(ln(\frac{h_i}{o_i})-ln(\frac{c_i}{o_i}))+ln(\frac{l_i}{o_i})(ln(\frac{l_i}{o_i})-ln(\frac{c_i}{o_i}))}$

Yang-Zhang volatility:

$\sqrt{\frac{1}{N-1}\sum^{T}_{i=1}(ln(\frac{o_i}{c_{i-1}})-\overline{ln(\frac{o_i}{c_{i-1}})})^2+\frac{k}{N-1}\sum^{T}_{i=1}(ln(\frac{c_i}{o_{i-1}})-\overline{ln(\frac{c_i}{o_{i-1}})})^2+(1-k)V_{RS}}$

其中:
$k=\frac{0.34}{1.34+\frac{N+1}{N-1}}$

$V_{RS}=\frac{1}{N}\sum^{N}_{i=1}(ln(\frac{h_i}{o_i})(ln(\frac{h_i}{o_i})-ln(\frac{c_i}{o_i}))+ln(\frac{l_i}{o_i})(ln(\frac{l_i}{o_i})-ln(\frac{c_i}{o_i})))$

$o_{i},c_{i},h_{i},l_{i}$分别为i时刻的OHLC数据

特征部分的损失函数就是最小化已实现波动率与预测波动率之间的负相关系数:
$$L_{corr(y,\hat{y})}=-\frac{S_{y,\hat{y}}}{S_{y}*S_{\hat{y}}} \tag{7}$$

整体任务的损失函数

$$L_{total}=-\mu\frac{\mathbb{E}[r^{\rho}]}{\sigma_{r^{\rho}}}+\lambda\sum_{h \in H}-\frac{S_{y_{h},\hat{y_{h}}}}{S_{y_{h}}\cdot S_{\hat{y_h}}}$$

其中$\mu$和$\lambda$为权重,取值在[0,1]之间,$\mu+\lambda=1$,这里进行简单处理$\mu=0.5,\lambda=0.5$

## Local Docs

### `source/README-92cf7420.md`

# 说明

## 数据获取

这里我们使用[tushare]([Tushare数据](https://tushare.pro/))获取的标的为:黄金ETF(518880.SH)、纳指ETF(513100.SH)、创业板ETF(159915.SZ)、沪深300ETF(510300.SH),时间范围2014-01-01至2023-08-02,价格数据后复权。

可以cd到项目目录下使用该命令获取默认数据(价格数据为后复权)

```bash
python get_data.py dump_all
```

如要获取其他数据可以使用

```bash
python get_data.py dump_all --codes "510300.SH" --start_dt "2023-01-01" --end_dt "2023-08-02"
```

使用时需要修改ts_data_service文件中的config，将tushare的token改为自己的

**data文件中也含有所需数据**

## 模型

具体参看mlt_tsmom.ipynb文件

## Code Implementation

- `source/get_data-970209e0.py`
  - Symbols: `get_etf_price, main`
- `source/__init__-990470ea.py`
- `source/core-88339afb.py`
  - Symbols: `MTL_TSMOM, __init__, log, train_model, validation_model, predict_data, loop, fit, get_backtest_returns, get_loss_score, plot_pred_nan_num`
- `source/data_processor-cf499af1.py`
  - Symbols: `load_csv, preparer_data, _zscore_standardize, get_multi_cols, get_dataset, DataProcessor, __init__, generate, build_dataset`
- `source/general-07cd262a.py`
  - Symbols: `calc_sharpe_ratio, calc_corrcoef, share_loss, corrcoef_loss, calc_volatility, calc_parkinson_volatility, calc_garmanklass_volatility, calc_rogers_satchell_volatility, calc_yangzhang_volatility, rolling_windows, get_estimator, generate_features`
- `source/module-ebd9e4b3.py`
  - Symbols: `CustomDataset, __init__, __len__, __getitem__, MainTaskNN, __init__, forward, AuxTaskNN, __init__, forward, LSTMEncoder, __init__`
- `source/optimize_multi_model-454d0e1c.py`
  - Symbols: `optimize_multi_hyperparameters, objective`
- `source/utils-d583407c.py`
  - Symbols: `format_dt, reduce_dimensions, expand_dimensions, trans2tensor, plot_pred_nan_num, all_nan`
- `source/__init__-24029e02.py`
- `source/config-50ed4012.py`
- `source/core-8a94a00c.py`
  - Symbols: `distributed_query`
- `source/trade_cal-fd84ab93.py`
  - Symbols: `get_trade_cal_frame, get_all_trade_days, get_trade_days`
- `source/tushare_api-b1c13329.py`
  - Symbols: `TuShare, __init__, __getattr__, wrapper`
- `source/utils-6282b185.py`
  - Symbols: `str2date, format_date`
