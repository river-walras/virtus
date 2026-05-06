# 金股增强策略

- Category: `B-因子构建类`
- Bundle Dir: `金股增强策略`

## Primary Summary

- Notebook: `source/金股增强策略-acae35f7.ipynb`

# 数据介绍

金股数据说明:end_date为金股的截至日(即券商推荐的金股有效期),write_date为公告日(即对应券商在微信公众号、研报等推送的时间),通过write_date我们可以看到金股组合大多数是在上月低和当月出发布出来。

**\统计分析时next_return使用的是$\frac{close}{close_{t-1}}-1$与end_date对齐的方式进行统计分析。**

由下图可知道**平均write_date日在每月的第3-4个交易日即全部发布完毕,所以在回测时在每月的第三个交易日进行调仓轮动。**

# 金股推荐历史量化处理

使用Beta分布定量记录分析师金股推荐历史。假设，对于分析师的真实选股能力，没有先验知识。因此，每个分析师初始的Beta分布中，α = β = 1，此情况下，分析师推荐成功率在[0,1]上均匀分布。当分析师推荐金股成功时，即推荐月份的股票涨幅>0时，参数𝛼更新为𝛼 + 1。反之，当推荐失败时，参数𝛽更新为𝛽 + 1。

Beta 分布的期望:
$\mu=E(x)=\frac{\alpha}{\alpha+\beta}$

# 基于推荐成功概率分布构建金股组合

1. 股票池：当月所有券商推荐的金股，无其它筛选条件。
2. 组合构建流程：
    - 获取当月所有券商推荐的金股及推荐金股的分析师信息；
    - 查询金股数据库，获取当月推荐金股的每一位分析师的定量指标；
    - 对分析师定量指标进行排序，分为 5 组，并构建相应的 5 个等权金股组合；
    - 每月末重复上述操作并调仓；
    - 回测时段：2020 年 1 月至 2022 年 8 月
    - 调仓周期：月度调仓

## Notebooks

### `source/金股增强策略-acae35f7.ipynb`

# 数据介绍

金股数据说明:end_date为金股的截至日(即券商推荐的金股有效期),write_date为公告日(即对应券商在微信公众号、研报等推送的时间),通过write_date我们可以看到金股组合大多数是在上月低和当月出发布出来。

**\统计分析时next_return使用的是$\frac{close}{close_{t-1}}-1$与end_date对齐的方式进行统计分析。**

由下图可知道**平均write_date日在每月的第3-4个交易日即全部发布完毕,所以在回测时在每月的第三个交易日进行调仓轮动。**

# 金股推荐历史量化处理

使用Beta分布定量记录分析师金股推荐历史。假设，对于分析师的真实选股能力，没有先验知识。因此，每个分析师初始的Beta分布中，α = β = 1，此情况下，分析师推荐成功率在[0,1]上均匀分布。当分析师推荐金股成功时，即推荐月份的股票涨幅>0时，参数𝛼更新为𝛼 + 1。反之，当推荐失败时，参数𝛽更新为𝛽 + 1。

Beta 分布的期望:
$\mu=E(x)=\frac{\alpha}{\alpha+\beta}$

# 基于推荐成功概率分布构建金股组合

1. 股票池：当月所有券商推荐的金股，无其它筛选条件。
2. 组合构建流程：
    - 获取当月所有券商推荐的金股及推荐金股的分析师信息；
    - 查询金股数据库，获取当月推荐金股的每一位分析师的定量指标；
    - 对分析师定量指标进行排序，分为 5 组，并构建相应的 5 个等权金股组合；
    - 每月末重复上述操作并调仓；
    - 回测时段：2020 年 1 月至 2022 年 8 月
    - 调仓周期：月度调仓

## Local Docs

### `source/金股组合增强-分析师推荐成功率因子-1502c6c9.md`

# 金股组合增强——分析师推荐成功率因子



## 结论

- 根据分析师金股推荐成功概率分布，构建金股增强组合。组合年化收益率 **25.73%**，夏普比 **0.979**，卡玛比 1.02

## 逻辑

使用Beta分布定量记录分析师金股推荐历史。假设，对于分析师的真实选股能力，没有先验知识。因此，每个分析师初始的Beta分布中，α = β = 1，此情况下，分析师推荐成功率在[0,1]上均匀分布。当分析师推荐金股成功时，即推荐月份的股票涨幅>0时，参数𝛼更新为𝛼 + 1。反之，当推荐失败时，参数𝛽更新为𝛽 + 1。

Beta分布概率密度函数:
$$
f(x;\alpha,\beta)=\frac{x^{\alpha-1}(1-x)^{\beta-1}}{\int_{0}^{1}u^{\alpha-1}(1-u)^{\beta-1}du}
$$
Beta 分布的期望:
$$
\mu=E(x)=\frac{\alpha}{\alpha+\beta}
$$
通过上式计算分析师推荐成功概率选出高概率分析师推荐的股票构建组合

## 回测结果

2020年至今回测结果如下

![image-20220922223228602](C:\Users\华思远\AppData\Roaming\Typora\typora-user-images\image-20220922223228602.png)

每月持仓数量在20-35只左右(如下图)

![image-20220922222612628](C:\Users\华思远\AppData\Roaming\Typora\typora-user-images\image-20220922222612628.png)

每月收益情况

![image-20220922223614394](C:\Users\华思远\AppData\Roaming\Typora\typora-user-images\image-20220922223614394.png)

历史前十大持仓

![image-20220922223633203](C:\Users\华思远\AppData\Roaming\Typora\typora-user-images\image-20220922223633203.png)

持仓收益前十

![image-20220922223654732](C:\Users\华思远\AppData\Roaming\Typora\typora-user-images\image-20220922223654732.png)

## 推荐成功率分析师TOP10

![image-20220922223813423](C:\Users\华思远\AppData\Roaming\Typora\typora-user-images\image-20220922223813423.png)

9月所推股票(**部分不是全部**)

![image-20220922223856508](C:\Users\华思远\AppData\Roaming\Typora\typora-user-images\image-20220922223856508.png)

## Code Implementation

- `source/__init__-875bf51d.py`
- `source/core-02dadba5.py`
  - Symbols: `get_stock_industry_name, _get_dict_values, offset_limit_func, get_sw1_price, PrepareData, __init__, init_data, get_forward_returns, full_data, _add_tradeday_monthend, get_author_proba, transform2stock_group`
- `source/utlis-33f87d11.py`
  - Symbols: `load_gold_stock_csv, view_author_stock, TradeDays, __init__, tradeday_of_month, get_tradedays_of_month, get_tradedays_month_end, get_tradedays_month_begin, _MonthEndOrMonthBegin, _tradedaysofmonth, _trans2frame`
