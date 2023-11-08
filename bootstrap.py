# 文件用于回归使用bootstrap方法
"""
@Author: GZK1108:https://github.com/GZK1108?tab=repositories
"""
import random
import numpy as np
import statsmodels.api as sm
from sklearn.utils import resample


# 使用这个方法据说最快，随机生成1或者-1
def random_number(lenth):
    # 随机生成lenth长度的数列，每个元素为1或者-1
    return [1 if random.random() < 0.5 else -1 for i in range(lenth)]


# 回归，计算t值，单变量
def cal_ols(x, y):
    x = sm.add_constant(x)
    est = sm.OLS(y, x)
    model = est.fit()
    t_value = model.tvalues[1]

    return t_value


# 本程序适用于单变量回归，采用双侧检验
def residual_bootstrap(X, Y, steps, c):
    """
    :param X: 解释变量，格式为List
    :param Y: 被解释变量，格式为List
    :param steps: 采样次数
    :param c: 置信水平，如0.05
    :return: t检验值的上下限
    """
    # 记录有多少数据
    lenth = len(X)
    # 第一次回归
    X = sm.add_constant(X)
    est = sm.OLS(Y, X)
    model = est.fit()
    pred = model.predict(X)
    epsilon = Y - pred  # 计算残差
    beta = model.params  # 输出回归beta，注意这里包含了截距项
    alpha = beta[0]

    t_list = []
    # 随机采样
    for n in range(steps):
        x, e = resample(X, epsilon, n_samples=round(lenth))
        y = alpha + e  # 这个式子和原假设有关系，y=alpha + beta0*x + e，原假设beta0=0
        t_value = cal_ols(x, y)
        t_list.append(t_value)  # append
    # 排序
    temp = np.sort(t_list, axis=0)

    # 按照置信水平计算临界值，双侧检验
    # 假设c=5%,up_side=1-c/2,down_side=c/2
    up_side = 100 * (1 - c / 2)
    down_side = 100 * (c / 2)
    t_up = np.percentile(temp, up_side)
    t_down = np.percentile(temp, down_side)
    # print(f'在置信度为{c}的条件下，t上下限为：', t_down, t_up)
    return t_down, t_up


# 本程序适用于单变量回归，采用双侧检验
def wild_bootstrap(X, Y, steps, c):
    """
    :param X: 解释变量，格式为List
    :param Y: 被解释变量，格式为List
    :param steps: 采样次数
    :param c: 置信水平，如0.05
    :return: t检验值的上下限
    """
    # 记录有多少数据
    lenth = len(X)
    # 第一次回归
    X = sm.add_constant(X)
    est = sm.OLS(Y, X)
    model = est.fit()
    pred = model.predict(X)
    epsilon = Y - pred  # 计算残差
    beta = model.params  # 输出回归beta，注意这里包含了截距项
    alpha = beta[0]

    t_list = []
    # 随机采样
    for n in range(steps):
        # print('正在进行第', n+1, '次采样')
        x, e = resample(X, epsilon, n_samples=round(lenth))
        v = random_number(lenth)
        y = alpha + e * v  # 这个式子和原假设有关系，y=alpha + beta0*x + e，原假设beta0=0
        t_value = cal_ols(x, y)
        t_list.append(t_value)
    # 排序
    temp = np.sort(t_list, axis=0)

    # 按照置信水平计算临界值，双侧检验
    # 假设c=5%,up_side=1-c/2,down_side=c/2
    up_side = 100 * (1 - c / 2)
    down_side = 100 * (c / 2)
    t_up = np.percentile(temp, up_side)
    t_down = np.percentile(temp, down_side)
    # print(f'在置信度为{c}的条件下，t上下限为：', t_down, t_up)
    return t_down, t_up


# 时间序列的wild bootstrap，因为时间序列特性，和普通的wild bootstrap不同，只适用单变量
def time_series_wb(X, Y, steps, c):
    """
        :param X: 解释变量，格式为dataframe/list
        :param Y: 被解释变量，格式为dataframe/list
        :param steps: 采样次数
        :param c: 置信水平，如0.05
        :return: t检验值的上下限
    """
    # 记录有多少数据
    lenth = len(X)
    # 第一次回归
    X = sm.add_constant(X)
    model = sm.OLS(Y, X).fit()
    pred = model.predict(X)
    epsilon = Y - pred  # 计算残差
    beta = model.params[1]  # 输出回归beta值，beta[0]是常数项

    t_list = []
    # 随机采样
    for n in range(steps):
        print('第', n + 1, '次采样')
        e = resample(epsilon, n_samples=round(lenth)).reset_index(drop=True)
        x = X
        v = random_number(lenth)
        y_star = pred + e * v  # 时间序列的wild bootstrap，y*=y_hat+e*v
        result = sm.OLS(y_star, x).fit()
        beta_star = result.params[1]
        se_star = result.bse[1]
        t_value = (beta_star - beta) / se_star
        # 把t值放入列表
        t_list.append(t_value)
    # 排序
    temp = np.sort(t_list, axis=0)

    # 按照置信水平计算临界值，双侧检验
    # 假设c=5%,up_side=1-c/2,down_side=c/2
    up_side = 100 * (1 - c / 2)
    down_side = 100 * (c / 2)
    t_up = np.percentile(temp, up_side)
    t_down = np.percentile(temp, down_side)
    # print(f'在置信度为{c}的条件下，t上下限为：', t_down, t_up)
    return t_down, t_up
