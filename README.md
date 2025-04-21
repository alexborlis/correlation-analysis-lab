# Correlation Analysis Lab

This project performs a correlation analysis on real-world student data from the [Open University Learning Analytics Dataset](https://www.kaggle.com/datasets/mohammadehsani/student-performance-at-open-university).  
It includes a structured Python-based pipeline for data loading, encoding, correlation matrix computation, and heatmap visualization.

## 📁 Project Structure
```
correlation-analysis-lab/
├── data/                   # Contains raw CSV files (ignored if >100MB)
├── reports/                # Generated visualizations and final report
├── src/                   # Python source files
│   ├── main.py             # Main execution script
│   ├── load_data.py        # Loads and inspects the dataset
│   ├── analyze_data.py     # Encodes and computes correlation matrix
│   └── visualize.py        # Visualizes the heatmap
├── .gitignore
├── requirements.txt
└── README.md
```

## 🔧 Setup
```bash
git clone git@github.com:your_username/correlation-analysis-lab.git
cd correlation-analysis-lab
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## ▶️ Run Analysis
```bash
python src/main.py
```

## ✅ Output
- Console logs with details
- Heatmap saved to `reports/correlation_matrix.png`

---

## 📌 Used Dataset
- `studentInfo.csv` from the Open University dataset
- Numerical and categorical variables analyzed
- Categorical variables were one-hot encoded before computing correlation