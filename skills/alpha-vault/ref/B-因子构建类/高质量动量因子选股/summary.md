# 高质量动量因子选股

- Category: `B-因子构建类`
- Bundle Dir: `高质量动量因子选股`

## Primary Summary

- Notebook: `source/高质量动量选股-1d8f4706.ipynb`

# <center>动量因子</center>

# 动量策略的一点历史

## 三大互补选股维度

1、`Momentum:`**当价格沿着过去的轨迹继续运动时**（即价格上涨的还会涨，价格下跌的还会跌），我们能够获得收益；  

2、`Value:`**当价格恢复到之前的某种均衡状态时**（即价格围绕基本面价值往复运动），我们能够获得收益；  

3、`Carry:`**当价格不发生变化时**，我们能够获得收益。股东分红收益。

注：假如我们买入一支股票并一直持有，如果股票价格不变，那么我们获得的收益就是该股票的分红。股息率（diviedend yield）就是Carry收益率。

## 动量策略的发展  

+ `1967年`，Robert Levy在*Journal of Finance* 发表了Relative Strength as a Criterion for Investment Selection 的文章（当年动量一词还未被造出）；


+ `1970s开始`，有效市场假说（EMH）被提出并成为主流；**动量现象的研究被极大地抑制**。随着人们对市场理解的加深以及价值投资的巨大成功，EMH不再权威，但动量任然被认为是‘一种黑色艺术、一种巫术魔力’；


+ `1993年`，Jegadeesh和Titman在*Journal of Finance* 发表了一篇里程碑式的文章，题为Return to Buying Winners and Selling Losers:Implications for Stock Market Efficiency；


+ `2008年`，EMH之父Eugene Fama在美国金融协会的采访中承认了动量的存在；


+ `2013年`，Asness等人在*Journal of Finance* 发表了影响深远的Value and Momentum Everywhere。  

## Momentum和Value无处不在

**核心论文**

+ Asness, C. S., T. J. Moskowitz, and L. H. Pedersen (2013). Value and Momentum Everywhere.Journal of Finance,Vol.68(3),929–985.
+ Gray,W.R.and J.R.Vogel (2016).Quantitative Momentum,a Practitioner’s Guide to Building a Momentum-Based Stock Selection System.John Wiley & Sons,Inc.,Hoboken,New Jersey.

# 基础版动量策略

## 策略出发点

1、`在中国股市中，反转强于动量`，且海外流行的动量选股方法（即使用t-12月到t-1月之间的收益率选股）并不好使。

2、在构造动量因子时，应该`注意其在市值因子上的暴露`。  

## 构造动量因子 

使用过去60个交易日风险调整后的涨跌幅作为动量因子（它和市值因子的相关性仅为0.085），其计算公式如下所示：  

### $$r_{60}-3000*\sigma ^{2}$$

其中$r_{60}$为60日涨跌幅，即60个交易日内的收益率;$\sigma$为60个交易日内收益率的标准差，代表风险。

## 策略思想  

1、回测期：2010年1月1日至2020年12月31日；  

2、调仓日：按月调仓，每月末按收盘价买卖股票；  

3、股票池：中证500成分股；剔除ST股票；剔除由于停牌等原因而无法买卖的股票；  

4、交易模型：

+ 每月末更新动量指标并重新对股票排名，新股理想仓位为1%，等权配置；


+ 将中证500成分股按因子排名分为5组，由于因子值越大越好，按由小到大排名，组别越大的组合越好，即G5组优于G1组；


**备注：**由于按日调仓需提取的日度数据量较为庞大，此处且先采用按月调仓的策略来传递高质量动量选股思想和呈现选股效果。

## Notebooks

### `source/高质量动量选股-1d8f4706.ipynb`

# <center>动量因子</center>

# 动量策略的一点历史

## 三大互补选股维度

1、`Momentum:`**当价格沿着过去的轨迹继续运动时**（即价格上涨的还会涨，价格下跌的还会跌），我们能够获得收益；  

2、`Value:`**当价格恢复到之前的某种均衡状态时**（即价格围绕基本面价值往复运动），我们能够获得收益；  

3、`Carry:`**当价格不发生变化时**，我们能够获得收益。股东分红收益。

注：假如我们买入一支股票并一直持有，如果股票价格不变，那么我们获得的收益就是该股票的分红。股息率（diviedend yield）就是Carry收益率。

## 动量策略的发展  

+ `1967年`，Robert Levy在*Journal of Finance* 发表了Relative Strength as a Criterion for Investment Selection 的文章（当年动量一词还未被造出）；


+ `1970s开始`，有效市场假说（EMH）被提出并成为主流；**动量现象的研究被极大地抑制**。随着人们对市场理解的加深以及价值投资的巨大成功，EMH不再权威，但动量任然被认为是‘一种黑色艺术、一种巫术魔力’；


+ `1993年`，Jegadeesh和Titman在*Journal of Finance* 发表了一篇里程碑式的文章，题为Return to Buying Winners and Selling Losers:Implications for Stock Market Efficiency；


+ `2008年`，EMH之父Eugene Fama在美国金融协会的采访中承认了动量的存在；


+ `2013年`，Asness等人在*Journal of Finance* 发表了影响深远的Value and Momentum Everywhere。  

## Momentum和Value无处不在

**核心论文**

+ Asness, C. S., T. J. Moskowitz, and L. H. Pedersen (2013). Value and Momentum Everywhere.Journal of Finance,Vol.68(3),929–985.
+ Gray,W.R.and J.R.Vogel (2016).Quantitative Momentum,a Practitioner’s Guide to Building a Momentum-Based Stock Selection System.John Wiley & Sons,Inc.,Hoboken,New Jersey.

# 基础版动量策略

## 策略出发点

1、`在中国股市中，反转强于动量`，且海外流行的动量选股方法（即使用t-12月到t-1月之间的收益率选股）并不好使。

2、在构造动量因子时，应该`注意其在市值因子上的暴露`。  

## 构造动量因子 

使用过去60个交易日风险调整后的涨跌幅作为动量因子（它和市值因子的相关性仅为0.085），其计算公式如下所示：  

### $$r_{60}-3000*\sigma ^{2}$$

其中$r_{60}$为60日涨跌幅，即60个交易日内的收益率;$\sigma$为60个交易日内收益率的标准差，代表风险。

## 策略思想  

1、回测期：2010年1月1日至2020年12月31日；  

2、调仓日：按月调仓，每月末按收盘价买卖股票；  

3、股票池：中证500成分股；剔除ST股票；剔除由于停牌等原因而无法买卖的股票；  

4、交易模型：

+ 每月末更新动量指标并重新对股票排名，新股理想仓位为1%，等权配置；


+ 将中证500成分股按因子排名分为5组，由于因子值越大越好，按由小到大排名，组别越大的组合越好，即G5组优于G1组；


**备注：**由于按日调仓需提取的日度数据量较为庞大，此处且先采用按月调仓的策略来传递高质量动量选股思想和呈现选股效果。
