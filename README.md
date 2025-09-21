# Dataset Analysis with Pandas & NumPy

**Project:** Basic exploratory data analysis and statistics on a small dataset using Python.

**Files**
- `Task_2.py` — main analysis script (prints/exports exploration & statistics).
- `user_profiles.csv` — dataset used for the analysis (small, public).
- `README.md` — this file.
- `requirements.txt` — Python dependencies (optional).
- `.gitignore` — files/folders to exclude from Git (optional).

---

## Project overview
This project demonstrates how to explore and analyze a dataset using **Pandas** and **NumPy**.  
Main tasks performed by `Task_2.py`:
1. Load the dataset (`user_profiles.csv`).
2. Show head of the data (`data.head()`).
3. Show schema and types (`data.info()`).
4. Produce descriptive statistics (`data.describe()`).
5. Calculate mean, median, mode, and standard deviation for each numeric column.
6. Compute correlation matrix (`data.corr()`).
7. (Optional) Save key outputs (summary tables, correlation matrix) to CSV files.

---

## Dataset
`user_profiles.csv` — replace this description with the real dataset description and column list.  
Example columns (update if different): `user_id, age, country, signup_date, purchase_count, revenue`.

---

## Requirements
Install the minimal dependencies:
```bash
pip install pandas numpy
