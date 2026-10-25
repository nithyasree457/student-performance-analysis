# Student Performance Analysis

## Project Overview

Student Performance Analysis is a data analysis and visualization project developed to explore student academic performance across Mathematics, Reading, and Writing subjects.

The project uses Python, Pandas, Matplotlib, and Streamlit to analyze student marks and present useful insights through an interactive dashboard.

## Objectives

* Analyze student academic performance.
* Calculate average scores across subjects.
* Compare performance based on gender.
* Analyze test preparation course performance.
* Identify students scoring below 50 in Mathematics.
* Present insights through an interactive dashboard.

## Technologies Used

* Python
* Pandas
* Matplotlib
* Streamlit

## Dataset

The project uses the Students Performance dataset.

The dataset contains student demographic information, test preparation details, and Mathematics, Reading, and Writing scores.

## Dashboard Features

* Student performance overview.
* Gender filter.
* Test preparation filter.
* Dynamic KPI cards.
* Subject performance visualization.
* Gender performance comparison.
* Test preparation analysis.
* Student performance insights.
* Interactive dataset display.
* Filtered dataset download.

## Project Structure

```text
student-performance-analysis/
│
├── data/
│   └── StudentsPerformance.csv
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Move into the project folder:

```bash
cd student-performance-analysis
```

Install required libraries:

```bash
pip install -r requirements.txt
```

Run the dashboard:

```bash
streamlit run app.py
```

## Analysis

The project explores student performance across three subjects.

It also compares average scores based on gender and test preparation course completion.

The dashboard allows users to filter the dataset and explore student performance interactively.

## Conclusion

This project demonstrates how Python-based data analysis and visualization can be used to explore academic performance and communicate descriptive insights through an interactive dashboard.

The findings represent patterns in the dataset and should not be interpreted as proof of causation.
