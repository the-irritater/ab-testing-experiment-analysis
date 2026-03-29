# Web Feature A/B Testing: Causal Inference and Statistical Decision-Making

> **Disclaimer:** The dataset used in this project is 100% simulated. It was generated programmatically to mimic realistic A/B test traffic on an online education platform. No real user data, company data, or production experiment results are used. This project is intended solely as a portfolio demonstration of statistical methodology.

## At a Glance

This project analyzes an A/B test for a "Free Trial Screener" feature on an online education platform. The goal is to determine whether the feature improves conversion quality or creates unnecessary friction in the enrollment funnel.

Using simulated experiment data, the analysis applies both Frequentist and Bayesian methods, validates randomization, checks statistical power, demonstrates CUPED variance reduction, and translates the result into business impact.

**Final recommendation: DO NOT LAUNCH.**

- CTR shows no meaningful improvement.
- Enrollment rate drops by about 9%.
- Estimated annual revenue impact is approximately **$1.2M in losses**.

## Short Problem Statement

An online education platform introduced a pre-enrollment screening step before users could start a free trial. The product team believed this would improve enrollment quality by filtering out low-intent users. This project tests whether that assumption is statistically and commercially valid.

## Why This Project Matters

Recruiters and hiring managers usually want to see more than charts and p-values. They want to know whether you can connect data analysis to product decisions. This project demonstrates:

- Clear experiment framing tied to a business question
- Strong statistical reasoning, not just dashboarding
- Ability to validate assumptions before interpreting results
- Communication of findings in product and revenue terms
- End-to-end reproducibility through code and notebook automation

## Business Takeaway

An online education platform tested a "Free Trial Screener" feature designed to improve enrollment quality. This analysis applies six complementary statistical techniques to the A/B test data and reaches a clear verdict:

- The feature does not improve Click-Through Rate (CTR).
- It significantly reduces enrollment rate by approximately 9%.
- Launching it would cost an estimated **~$1.2 million per year** in lost revenue.

This project demonstrates how rigorous experimentation methodology, including power analysis, Frequentist and Bayesian testing, variance reduction, and pitfall awareness, protects businesses from costly mistakes.

## What a Recruiter Can Infer From This Project

- I can design and evaluate experiments, not just report metrics.
- I understand statistical significance, practical significance, and business significance.
- I know how to check randomization, power, and common A/B testing pitfalls.
- I can present technical work in a structured, decision-oriented way.
- I can package analysis into a reproducible project suitable for collaboration or review.

## Overview

This project implements an end-to-end A/B testing framework covering the full experimentation lifecycle. The Jupyter notebook walks through each step with detailed explanations, code, visualizations, and interpretations.

| Field | Details |
|:---|:---|
| **Project** | A/B Test Experiment Analysis with Causal Inference |
| **Dataset** | Simulated online course platform traffic (synthetic, not real) |
| **Author** | Sanman |
| **Date** | March 2026 |
| **Tools** | Python, NumPy, Pandas, SciPy, Matplotlib, Seaborn |

## Key Questions Answered

1. Was the A/B test properly randomized?
2. Was the sample size large enough to detect a meaningful effect?
3. Did the feature improve CTR?
4. Did the feature improve enrollment conversion?
5. What is the Bayesian probability that the experiment is actually better?
6. What would be the financial impact of launching the feature?

## What's Inside the Notebook

| Section | Topic | Key Output |
|:---|:---|:---|
| 1-2 | Problem statement and objectives | Six clearly defined analytical goals |
| 3 | Dataset overview and synthetic generation | 37-day simulated A/B test with about 20K pageviews/day/group |
| 4 | Data preprocessing | Missing data analysis and analysis-ready filtering |
| 5 | Randomization check | Welch's t-test and Cohen's d confirm group balance |
| 6 | Exploratory data analysis | Boxplots, daily trends, and funnel comparison |
| 7 | Power analysis | Required sample size calculation: 24,643 clicks/group |
| 8 | Frequentist hypothesis testing | Two-proportion z-tests for CTR and enrollment |
| 9 | Bayesian A/B testing | Beta-Binomial posterior estimation and visualization |
| 10 | CUPED variance reduction | Confidence interval width reduced to about 71% of original |
| 11 | Peeking simulation | Monte Carlo demonstration of false positive inflation |
| 12 | Financial impact assessment | About $1.2M projected annual revenue loss |
| 13 | Conclusion and recommendations | Final decision, root-cause hypotheses, next steps |

## Statistical Methods Used

| Method | Purpose | Key Result |
|:---|:---|:---|
| Power analysis | Determine required sample size | 24,643 clicks/group for 80% power |
| Welch's t-test and Cohen's d | Validate randomization balance | Groups balanced, p > 0.05 and \|d\| < 0.2 |
| Two-proportion z-test (CTR) | Test click-through rate difference | Not significant |
| Two-proportion z-test (Enrollment) | Test enrollment rate difference | Significant negative effect, p < 0.001 |
| Bayesian Beta-Binomial | Estimate posterior probability of improvement | Approximately 0% chance experiment is better |
| CUPED | Tighten confidence intervals | CI width reduced to about 71% of original |
| Monte Carlo peeking simulation | Quantify false positive inflation | About 7x inflation from frequent peeking |

## How to Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Generate the notebook and execute it with outputs
python run_and_save.py

# 3. Open the notebook
jupyter notebook AB_Testing_Experiment_Analysis.ipynb
```

**Alternative (manual):**

```bash
python create_notebook.py
jupyter nbconvert --to notebook --execute --inplace AB_Testing_Experiment_Analysis.ipynb
```

## Project Structure

```text
ab-testing-experiment-analysis/
|-- AB_Testing_Experiment_Analysis.ipynb   # Generated and executed notebook
|-- create_notebook.py                     # Builds the notebook programmatically
|-- run_and_save.py                        # Generate -> execute -> save
|-- requirements.txt                       # Python dependencies
|-- README.md                              # Project documentation
`-- .gitignore                             # Git ignore rules
```

## Dependencies

- Python 3.8+
- NumPy >= 1.24
- Pandas >= 2.0
- Matplotlib >= 3.7
- Seaborn >= 0.12
- SciPy >= 1.10
- Jupyter >= 1.0

No heavy dependencies like PyMC or TensorFlow are required. The Bayesian analysis uses SciPy's Beta distribution directly.

## Portfolio Value

This project is especially relevant for roles involving:

- Data Analyst
- Product Analyst
- Experimentation Analyst
- Business Analyst
- Junior Data Scientist

It highlights practical experimentation skills that are useful in product, growth, edtech, and conversion optimization contexts.

## License

This project is for educational and portfolio purposes.
