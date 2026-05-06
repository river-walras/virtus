# 行业有效量价因子与行业轮动策略

- Category: `B-因子构建类`
- Bundle Dir: `行业有效量价因子与行业轮动策略`

## Primary Summary

- Notebook: `source/行业有效量价因子与行业轮动策略ETF-7bc1a2b4.ipynb`

# 数据获取并转换

# 初始化qlib

# 训练模型实例化

## Notebooks

### `source/行业有效量价因子与行业轮动策略ETF-7bc1a2b4.ipynb`

# 数据获取并转换

# 初始化qlib

# 训练模型实例化

## Code Implementation

- `source/__init__-dd3214ed.py`
- `source/core-737a2fd6.py`
  - Symbols: `Factor_Calculator, __init__, fit, transform, second_order_mom, diff_period_mom, amount_std, volume_std, turnover_pct, long_short, long_short_pct, price_vol_rank_cov`
- `source/factor_expr-da289f16.py`
  - Symbols: `VolumePriceFactor192, __init__, get_label_config, get_feature_config, parse_config_to_fields, VolumePriceFactor10, get_feature_config`
- `source/opt_func-89fbba86.py`
  - Symbols: `calculate_best_chunk_size, search_factor_params, opt_strat, _get_err_msg_value, _func2search_para, mult_opt_strat`
- `source/plotting-550ba226.py`
  - Symbols: `plot_ts_icir, plot_group_cumulative, plot_group_distribution, plot_qlib_factor_dist, plot_factor_dist`
