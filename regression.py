# 用于存放各种复杂的回归方法
"""
@Author: GZK1108:https://github.com/GZK1108?tab=repositories
"""
import numpy as np
import statsmodels.api as sm


def fwls(x, y):
    """
    :param x: 自变量
    :param y: 因变量
    :return: 回归模型
    """
    # ols回归
    model_ols = sm.OLS(y, x).fit()
    # log(e^2)对自变量回归
    log_e2 = np.log(model_ols.resid ** 2)
    model_ols2 = sm.OLS(log_e2, x).fit(cov_type='HAC', use_t=True, cov_kwds={'maxlags': 1})
    # fwls回归
    wls_weight = list(1 / np.exp(model_ols2.fittedvalues))
    model = sm.WLS(y, x, weights=wls_weight).fit()
    return model
