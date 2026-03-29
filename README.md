# The $1.2M Decision: A/B Testing & Causal Inference

> **Disclaimer:** The dataset used in this project is **100% simulated**. It was generated programmatically to mimic realistic A/B test traffic on an online education platform. No real user data, company data, or production experiment results are used. This project is intended solely as a portfolio demonstration of statistical methodology.

## The Business Problem

An online education platform was eager to launch a "Free Trial Screener" on its course overview page. The idea sounded perfectly logical: by asking users about their weekly time commitment *before* they clicked "Start Free Trial", the platform could filter out low-intent users early. 

The product team hypothesized this friction would increase the *quality* of free trial sign-ups, thereby boosting overall enrollment rates. But intuition is not always reality, and in the EdTech industry, a 1% change in enrollment conversion can translate to millions of dollars. To find out if this feature was actually helping, we ran a 37-day A/B test.

This repository tracks the complete, end-to-end data decision-making flow that saved the company from a costly mistake.

---

## The Decision-Making Flow

### 1. Validating the Test (Sanity Checks)
Before looking at the final conversions, we must ensure the experiment was fair. If the underlying audience split is flawed, the entire test is invalid. We tested pre-treatment invariant metrics (Pageviews and Clicks).
*   **Method:** Welch's t-test and Cohen's d effect size.
*   **Outcome:** Groups were perfectly balanced ($p > 0.05$, $d \approx 0$). The traffic split was fair. We can proceed.

### 2. Guardrail Metric: The Click-Through Rate
Did the new popup accidentally break the page or tank top-of-funnel clicks? 
*   **Method:** Two-Proportion Z-Test (Two-sided).
*   **Outcome:** No significant difference observed ($p = 0.865$). Users clicked the "Start Free Trial" button at the same 8% rate regardless of the screener. 

### 3. Target Metric: The Enrollment Rate (The Moment of Truth)
Here is where the business value lies. Did the feature actually improve enrollment? We ran a formal, one-sided statistical test to check for improvement.

*   **Hypotheses:**
    *   $H_0: p_{new} \le p_{old}$ (The feature does NOT improve enrollment)
    *   $H_1: p_{new} > p_{old}$ (The feature DOES improve enrollment)
*   **Outcome:** Enrollment conversion plummeted from 21.9% to 19.8% (a ~9% relative drop). Because it performed strictly worse, our right-tailed test yielded a p-value of essentially 1.000 ($p \gg 0.05$).

### 4. The Business Takeaway
> **We fail to reject $H_0$ $\\rightarrow$ no significant improvement $\\rightarrow$ do not launch.**

Furthermore, translating this statistical drop into financial impact models showed that launching this feature to 100% of traffic would cost the business an estimated **~$1.2 million per year** in lost revenue.

---

## 🚀 Advanced Statistical Layers

This project goes beyond a standard t-test by incorporating advanced data science methodology designed to protect a business from false conclusions:

1. **Confidence Interval Visualization (Advanced Layer):** Rather than just reporting a p-value, this project explicitly visualizes the 95% Confidence Intervals for treatment effects. It proves visually that the entire range of plausible outcomes for the new feature sits firmly below zero, confirming active harm to the product.
2. **CUPED Variance Reduction:** Demonstrates how to use pre-experiment covariate data (like historic clicks) to tighten confidence interval widths by roughly 30%, increasing statistical power without needing more traffic.
3. **Bayesian Conjugate Modeling:** Uses Beta-Binomial conjugate distributions to definitively answer the business question, revealing there is a **~0% probability** the new feature is better than the control.
4. **The Peeking Pitfall (Monte Carlo Simulation):** A custom simulation proving exactly why "optional stopping" (checking p-values early) is dangerous, showing how it inflates false positive rates by up to 7x.

---

## What's Inside the Notebook

| Section | Topic | Key Output |
|:---|:---|:---|
| §1–3 | Problem & Data Generation | 37-day simulated A/B test, ~20K pageviews/day/group |
| §4–6 | Preprocessing & EDA | Missing data analysis, funnel viz, randomization checks |
| §7 | Power Analysis | Required sample size calculation (24,643 clicks/group) |
| §8 | Frequentist Testing | 1-Sided Z-Tests, P-Values, and CI Visualization |
| §9 | Bayesian A/B Testing | Beta-Binomial conjugate model, posterior visualization |
| §10 | CUPED Variance Reduction | CI width reduced to ~71% of original |
| §11 | Peeking Simulation | Monte Carlo showing false positive inflation |
| §12 | Financial Impact Assessment | ~$1.2M projected annualized revenue loss |

---

## How to Run This Analysis

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Generate the notebook AND execute it with all outputs
python run_and_save.py

# 3. Open in Jupyter (or view directly on GitHub)
jupyter notebook AB_Testing_Experiment_Analysis.ipynb
```

**Alternative (manual):**
```bash
python create_notebook.py
jupyter nbconvert --to notebook --execute --inplace AB_Testing_Experiment_Analysis.ipynb
```

## Tools & Libraries
- **Python 3.8+**
- **NumPy ≥ 1.24**
- **Pandas ≥ 2.0**
- **Matplotlib & Seaborn**
- **SciPy ≥ 1.10**

*(No heavy dependencies like PyMC; the Bayesian engine relies on native SciPy conjugate distributions for high-speed computation.)*
