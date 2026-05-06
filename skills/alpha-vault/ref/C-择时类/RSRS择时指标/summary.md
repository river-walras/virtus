# RSRS择时指标

- Category: `C-择时类`
- Bundle Dir: `RSRS择时指标`

## Primary Summary

- Notebook: `source/RSRS-60f0f606.ipynb`

# <font color=DarkMagenta>阻力支撑相对强弱概念</font>

在技术分析中，阻力位与支撑位经常被市场参与者提及并给出自己认为 的阻力支撑点位。阻力位与支撑位的概念很容易理解，顾名思义，**支撑位**即:<u>是指标的价格在下跌时可能遇到的支撑，是交易者认为买方力量开始反超卖方使得价格在此止跌或反弹上涨的价位</u>；**阻力位**则<u>是指在标的价格上涨时可 能遇到的压力，是交易者认为卖方力量开始反超买方而使得价格难以继续上涨或就此回调下跌的价位</u>。

## <font color=DarkMagenta>支撑位与阻力位的常用方式</font>

## Notebooks

### `source/RSRS-60f0f606.ipynb`

# <font color=DarkMagenta>阻力支撑相对强弱概念</font>

在技术分析中，阻力位与支撑位经常被市场参与者提及并给出自己认为 的阻力支撑点位。阻力位与支撑位的概念很容易理解，顾名思义，**支撑位**即:<u>是指标的价格在下跌时可能遇到的支撑，是交易者认为买方力量开始反超卖方使得价格在此止跌或反弹上涨的价位</u>；**阻力位**则<u>是指在标的价格上涨时可 能遇到的压力，是交易者认为卖方力量开始反超买方而使得价格难以继续上涨或就此回调下跌的价位</u>。

## <font color=DarkMagenta>支撑位与阻力位的常用方式</font>

### `source/RSRS改进-f892220e.ipynb`

# 总结

将RSRS指标构造融入收益率波动的信息，使得指标值能达到在震荡市场上钝化的效果，从而减少策略在震荡期间的误判次数。实证结果表明，钝化RSRS 指标 能提高各宽基指数的择时效果，使得择时策略在全样本与近年均有较好表现。在中证 500 与创业板指上，将样本点加权与钝化操作结合的成交额加权回归钝化RSRS 指标效果更佳。

# RSRS指标新的构建方式

通过改变指标本身表达形式而非回归方法，以改变RSRS择时指标。

先看原始RSRS择时指标的表达形式:

$RSRS=z\_score(\hat{\beta})*R^{2}$

其中，计算标准分$z\_score(\hat{\beta})$所用的周期为M。而这里我们在乘$R^2$的原因是当回归结果的$R^2$较小时，说明回归模型的解释力度较弱，此时标准分乘以$R^2$后数值会被往零点的方向压缩，由于策略仅在指标值绝对值大于一定阈值 后才会发出，因而指标值实际上在此时是被钝化了。

延续这个思路，既然我们观察到RSRS择时策略最近在震荡市内表现不 够稳定，那么在市场没有明确趋势的时候让指标值钝化能不能减小指标误判 的风险，从而提升指标的择时效果呢？考虑到收益率的波动率往往能够一定程度上体现市场当前的震荡水平，我们对RSRS 择时指标做出如下调整：

$RSRS=z\_score(\hat{\beta})*R^{4*quantile(std(return),M)}$

其中，quantile(std(return),M)表示当前市场收益率波动在过去M日的历史动率中所处的分位数大小。由于𝑅大于0小于 1，当分位数越大时，震荡水平越高，此时 RSRS 指标将得到更大的钝化效果。

为了方便区分新的RSRS指标与原始的RSRS指标，我们将新的指标命名为钝化RSRS指标。

计算收益率标准差的分位数中需要两个参数，一个是用最近多少天的收 益率数据来计算标准差，一个是用多少个标准差数据来计算分位数。为了尽量与$z\_score(\hat{\beta})$在信息来源上保持一致，这两个参数的值即选用与$z\_score(\hat{\beta})$时一样的N与M。


使用下面函数获取quantile(std(return),M)
```
def _cal_ret_quantile(self) -> np.array:

        # 计算收益波动
        ret_std = self.price_df['ret'].rolling(self.N).std()
        ret_quantile = ret_std.rolling(self.M).apply(
            lambda x: x.rank(pct=True)[-1], raw=False)

        return ret_quantile.values
```

这里提供了一个RSRS的回测框架

```

hs = rsrs()
# 加载
# 信号名称列表：RSRS, 标准分RSRS, 修正标准分RSRS, 右偏修正标准分RSRS, 钝化RSRS,成交额加权钝化RSRS
hs.init_from_config(指数代码,回测开始日,回测结束日,freq={回测信号名称:(N,M),...})

# 回测
hs.backtest({回测信号名称:开仓阈值})

# 输出完整报告：净值图+风险指标数据
hs.summary()

# 单独查看净值图
hs.plot_net_value()

# 单独查看风险指标
hs.report()

```

**get_RSRS**:计算各种RSRS

_regression:计算OLS回归及WLS回归所需数据
- _cal_ols:计算ols
- _cal_wls:计算wls
    - _cal_vol_weights:计成交量权重
