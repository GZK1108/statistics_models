# statistics_models
A repository for statistics_models

---

## Bootstrap
There are three bootstrap ideas in financial analysis:
(1) residual bootstrap(RB),
(2) pairs bootstrap(PB),
(3) wild bootstrap (WB)

+ RB
  1. $(x_i,y_i)(i=1,2,...,n)$    satisfy the relation: $y_i=\alpha+\beta x_i+\varepsilon_i$. Estimate $\hat{\alpha},\hat{\beta}$ by OLS, and calculate residuals: $\hat{\varepsilon}=Y-X\hat{\theta}=(\hat{\varepsilon_1},...,\hat{\varepsilon_n})$
  2. Randomly sampling $(\hat{\varepsilon_1^{\ast}},..., \hat{\varepsilon_n^{\ast}})$ from $(\hat{\varepsilon_1},...,\hat{\varepsilon_n})$ with replacement. Then we can gain $(x_i,y_i^{\ast})(i=1,...,n)$ by $y_i^{\ast}=\hat{\alpha}+\beta_0x_i+\tilde{\varepsilon_i^{\ast}}$. Note $\beta_0$ is $H_0:\beta=\beta_0$
  3. Estimate $\hat{\theta^*}  = ( X ^ { \prime } X ) ^ { - 1 } ( X ^ { \prime } Y ^ * )$ and $se ( \hat{\beta ^ { \ast }} ) = \sqrt { \sigma ^ { 2 } ( X ^ { \prime } X  ) ^ { - 1 }_{22} } = \sqrt { s ^ { \ast 2 } ( X ^ { \prime } X) ^ { - 1 }_{22} }$ by OLS, which $s ^ { \ast 2 } = \hat{\varepsilon} ^ { \ast \prime } \hat{\varepsilon} ^ { \ast } / ( n - 2 )$ and $\hat{\varepsilon} ^ { \ast } = Y ^ { \ast } - X \hat{\theta} ^ { \ast }$.
  4. Constructing Test Statistics Containing Hypothesis $H_0:\beta=\beta_0$ $$t^{\ast}=\frac{\hat{\beta}^{\ast}-\beta_0}{se(\hat{\beta^{\ast}})}$$
  5. Then repeat steps 2-4 N times to get estimators: $\hat{\beta^{\ast}_1},...,\hat{\beta ^ {\ast}_N}$ and t-test $t^{\ast}_1,...t^{\ast}_N$. Sort $t^{\ast}_1,...,t^{\ast}_N$ from smallest to largest. Then get left critical value $t^{\ast}_{\alpha/2}=t^{\ast}_{2.5\% \ast N}$ and right critical value $t^{\ast}_{1-\alpha/2}=t^{\ast}_{97.5\% \ast N}$ in $\alpha=5\%$. It is said that we get accept domain: $(t^{\ast}_{\alpha /2},t^{\ast}_{1-\alpha /2})=(t^{\ast}_{2.5 \% \ast N},t^{\ast}_{97.5 \% \ast N})$ with $H_0:\beta=\beta_0 $. Of course, reject domain is its complementary set.
  6. Test: There is a set of real data $(x_i,y_i )( i=1,...,n ) $ satisfying the relation $y_i=\alpha+\beta x_i+u_i$. Estimate $\hat{\alpha},\tilde{\beta}\ \ and \ \ \tilde{t}=\frac{\tilde{\beta}-\beta_0}{se(\tilde{\beta})}$. If $t _ { 2.5\% * N } ^ { \ast } \lt \tilde{t} \lt t _ { 97.5\% * N }^{\ast}$, don't reject $H_0$, else reject $H_0$.

+ PB: Heteroskedasticity robustness
  
+ WB: Heteroskedasticity robustness

Be careful bootstrap is different in time-series data.
