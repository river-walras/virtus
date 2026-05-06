# 时变夏普

- Category: `C-择时类`
- Bundle Dir: `时变夏普`

## Primary Summary

- Notebook: `source/Tsharpe-34a0c921.ipynb`

# Tsharpe模型演变过程

Robert Whitelaw（1994）中设定模型：
>four explanatory variables-the Baa-Aaa spread,the commercial paper-Treasury spread,the one-year Treasury yield,and the dividend yield

$$r_{t,t+r}=X_t\beta+u_{r+r}$$
$$\sqrt{\frac{\pi}{2}}|\hat{u}_{t+r}|=X_t\gamma+\epsilon_{t+r}$$

Robert Whitelaw（1997）中设定模型：

>The Baa-Aaa spread, the dividend yield, and the one-year yield are used in the mean equation, and the one-year yield and the commercialpaper-Treasury spread are used in the volatility equation.

$$R_{t+1}-R_{ft}=X_1t\beta_1+\epsilon_{1t+1}$$
$$\sqrt{\frac{\pi}{2}}|\epsilon_{1t+1}|=X_2t\beta_2+\epsilon_{2t+1}$$


***国信证券对上述解释变量做了更中国化的改变，具体如下：***

两个等式分别表达了对收益率和其波动性的回归。其中$R_{t+1}$指数收益,$R_{ft}$表示无风险利率,$X_{1t}$表示t期的[M1同比增长率,指数市盈率]和一年期国债利率组成的向量,而$X_{2t}$表示由在t期的一年期国债利率和[国债一年期即期收益率]组成的向量。


可以看到1994年模型与1997年模型的**不同**是：1994年两步回归时$X_t$表示的是同一解释变量；而1997年将解释变量拆成了两组分别为$X_1y$,$X_2t$;
**相同点：**都是将第一步回归后的残差带入第二步中作为被解释的变量。

在执行完两步回归后得到$\beta_1$,$\beta_2$后通过下述公式获取estimated conditional Sharpe ratio：

$$\hat{S}_t=\frac{X_{1t}\hat{\beta}_1}{X_{2t}\hat{\beta}_2}$$

# 构建数据提取函数

## Notebooks

### `source/Tsharpe-34a0c921.ipynb`

# Tsharpe模型演变过程

Robert Whitelaw（1994）中设定模型：
>four explanatory variables-the Baa-Aaa spread,the commercial paper-Treasury spread,the one-year Treasury yield,and the dividend yield

$$r_{t,t+r}=X_t\beta+u_{r+r}$$
$$\sqrt{\frac{\pi}{2}}|\hat{u}_{t+r}|=X_t\gamma+\epsilon_{t+r}$$

Robert Whitelaw（1997）中设定模型：

>The Baa-Aaa spread, the dividend yield, and the one-year yield are used in the mean equation, and the one-year yield and the commercialpaper-Treasury spread are used in the volatility equation.

$$R_{t+1}-R_{ft}=X_1t\beta_1+\epsilon_{1t+1}$$
$$\sqrt{\frac{\pi}{2}}|\epsilon_{1t+1}|=X_2t\beta_2+\epsilon_{2t+1}$$


***国信证券对上述解释变量做了更中国化的改变，具体如下：***

两个等式分别表达了对收益率和其波动性的回归。其中$R_{t+1}$指数收益,$R_{ft}$表示无风险利率,$X_{1t}$表示t期的[M1同比增长率,指数市盈率]和一年期国债利率组成的向量,而$X_{2t}$表示由在t期的一年期国债利率和[国债一年期即期收益率]组成的向量。


可以看到1994年模型与1997年模型的**不同**是：1994年两步回归时$X_t$表示的是同一解释变量；而1997年将解释变量拆成了两组分别为$X_1y$,$X_2t$;
**相同点：**都是将第一步回归后的残差带入第二步中作为被解释的变量。

在执行完两步回归后得到$\beta_1$,$\beta_2$后通过下述公式获取estimated conditional Sharpe ratio：

$$\hat{S}_t=\frac{X_{1t}\hat{\beta}_1}{X_{2t}\hat{\beta}_2}$$

# 构建数据提取函数
