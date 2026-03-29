import numpy as np
from scipy import stats

np.random.seed(42)
n_days = 37

control_pv = np.random.normal(20000, 800, n_days).astype(int)
control_clicks = np.array([np.random.binomial(pv, 0.08) for pv in control_pv])

exp_pv = np.random.normal(20000, 800, n_days).astype(int)
exp_clicks = np.array([np.random.binomial(pv, 0.0815) for pv in exp_pv])

p1 = control_clicks.sum() / control_pv.sum()
p2 = exp_clicks.sum() / exp_pv.sum()

diff = p2 - p1
p_pool = (control_clicks.sum() + exp_clicks.sum()) / (control_pv.sum() + exp_pv.sum())
se = np.sqrt(p_pool * (1 - p_pool) * (1/control_pv.sum() + 1/exp_pv.sum()))
z = diff / se
p_val = 2 * (1 - stats.norm.cdf(abs(z)))

print(f"CTR Control: {p1:.5f}")
print(f"CTR Exp: {p2:.5f}")
print(f"Z: {z:.3f}, p-value: {p_val:.5f}")

c_enr = np.array([np.random.binomial(c, 0.2189) for c in control_clicks[:23]])
e_enr = np.array([np.random.binomial(c, 0.1983) for c in exp_clicks[:23]])
p1_enr = c_enr.sum() / control_clicks[:23].sum()
p2_enr = e_enr.sum() / exp_clicks[:23].sum()
diff_enr = p2_enr - p1_enr
p_pool_enr = (c_enr.sum() + e_enr.sum()) / (control_clicks[:23].sum() + exp_clicks[:23].sum())
se_enr = np.sqrt(p_pool_enr * (1 - p_pool_enr) * (1/control_clicks[:23].sum() + 1/exp_clicks[:23].sum()))
z_enr = diff_enr / se_enr
p_val_enr = 1 - stats.norm.cdf(z_enr)

print(f"ENR Control: {p1_enr:.5f}")
print(f"ENR Exp: {p2_enr:.5f}")
print(f"ENR Z: {z_enr:.3f}, p-value: {p_val_enr:.5f}")
