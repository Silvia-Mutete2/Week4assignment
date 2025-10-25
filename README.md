# AI in Software Engineering — Week 4 Assignment

**Author:** Silvia Mutete  
**Course:** Bachelor of Business Information Technology (BBIT) — Kiriri Women’s University of Science & Technology

---

## Overview

This repository contains solutions for Week 4: AI in Software Engineering. It includes theoretical analysis, practical implementations (automation and predictive modeling), ethical reflection, and a short bonus proposal.

## Contents

Files in this repository:

```
AI_Software_Engineering_Assignment/
│
├── task1_sorting.py         # Sorting function (AI-assisted) and examples
├── task1_analysis.txt      # 200-word performance comparison of AI vs manual coding
│
├── task2_selenium.py       # Selenium automated login tests (valid/invalid)
├── task2_results.png       # Sample/placeholder result image
├── task2_summary.txt       # 150-word summary of Task 2
│
├── task3_predictive.ipynb  # Notebook: synthetic ML pipeline (train, eval, save model)
├── task3_metrics.txt       # Accuracy and F1 metrics from the notebook
├── task3_ethics.md         # Ethical reflection for Task 3
│
└── bonus_proposal.pdf      # Short proposal (explainability + monitoring)
```

## Part 1 — Theoretical Analysis (30%)

- AI-driven code generation: overview, benefits, limitations (security, incorrect logic, bias).
- Supervised vs Unsupervised approaches for bug detection (table in deliverables).
- Importance of bias mitigation in personalization.
- Case study: AIOps for automating deployment pipelines (RCA and predictive risk scoring).

## Part 2 — Practical Implementation (60%)

Task highlights:

- Task 1: AI-Powered Code Completion — `task1_sorting.py` and `task1_analysis.txt`.
- Task 2: Automated Testing — `task2_selenium.py` (Selenium-based automated login tests).
  - A lightweight headless script is included; install `selenium` and `webdriver-manager` (see below).
- Task 3: Predictive Analytics — `task3_predictive.ipynb` demonstrates a minimal classification pipeline using scikit-learn.

## Part 3 — Ethics (10%)

See `task3_ethics.md` for ethical considerations: provenance & consent, bias & fairness, transparency, and misuse risk. Tools referenced: IBM AI Fairness 360 (AIF360).

## Bonus: Innovation Challenge (10%)

Proposal: SmartDocGen — an AI system for automated software documentation generation. See `bonus_proposal.pdf`.

## Tools & Libraries Used

- GitHub Copilot / Tabnine — AI code assistance
- Selenium / webdriver-manager — automated browser testing
- scikit-learn, pandas, numpy — data preprocessing and ML
- Jupyter Notebook — model analysis and evaluation
- ReportLab (optional) — PDF generation
- IBM AIF360 — fairness assessment

## Setup & Run (quick)

1. Create or activate a Python 3.8+ environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Selenium script (example):

```bash
python task2_selenium.py
```

4. Open and run the notebook:

```bash
jupyter notebook task3_predictive.ipynb
```

## Notes and Recommendations

- The Selenium script includes a fallback to `webdriver-manager` — if you see "Missing Python package 'selenium'", install the packages above.
- Replace placeholder URLs and selectors in `task2_selenium.py` with your application-specific values.
- For production ML, replace synthetic data with the real dataset and add cross-validation, fairness checks, and model monitoring.

## Contact

Author: Silvia Mutete — Kiriri Women’s University of Science & Technology

---

If you want any section expanded (visuals, PDF generation, CI, or a properly formatted proposal PDF), tell me what to add and I’ll update the repo.
