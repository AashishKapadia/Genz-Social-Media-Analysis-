# 📱 Gen Z Social Media Analysis

> A comprehensive data analysis of social media usage patterns among Generation Z across 7 countries — covering platform preference, addiction levels, usage purpose, mental health correlations, and behavioural trends.

---

## 📌 Project Overview

This project analyses **1,000,000+ Gen Z user records** sourced from Kaggle to uncover how Generation Z interacts with social media globally. The analysis spans platform preferences, addiction classifications, daily usage hours by purpose, night-time behaviour, gender distribution, and mental health impact scores.

The project demonstrates a full end-to-end data pipeline:
**Data Collection → Python Cleaning → Tableau Visualisation → Word Reporting**

---

## 👤 Author

**Aashish Kapadia**
📅 Date: May 2026

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| Python (Pandas) | Data cleaning, null handling, deduplication |
| Tableau Public | Interactive visualisations (14 charts) |
| Microsoft Word | Report writing and documentation |
| Kaggle | Dataset source |

---

## 📂 Project Structure

```
genz-social-media-analysis/
│
├── data/
│   ├── genz_social_media_usage_1M.csv      # Raw dataset (Kaggle)
│   └── genz-social-cleaned.csv             # Cleaned dataset (output of Python script)
│
├── scripts/
│   └── genz-social.py                      # Python data cleaning script
│
├── report/
│   └── Genz_Social_Media_Analysis_Report.pdf  # Full analysis report with all 14 visualisations
│
└── README.md
```

---

## 📊 Dataset Overview

| Metric | Value |
|--------|-------|
| Total Records | 1,000,000+ |
| Columns | 14 |
| Countries | 7 (India, USA, Canada, UK, Germany, Brazil, Australia) |
| Platforms | 5 (Instagram, YouTube, TikTok, Twitter, Snapchat) |
| Null Values | 0 (after cleaning) |
| Duplicates | Removed |

---

## 🧹 Data Cleaning (Python)

The script `genz-social.py` performs the following steps:

```python
import pandas as pd

df = pd.read_csv('genz_social_media_usage_1M.csv')

# Exploratory checks
df.head(), df.tail(), df.info(), df.describe()

# Null handling — fill numeric nulls with column mean
df.fillna(df.select_dtypes(include='number').mean(), inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Save cleaned file
df.to_csv('genz-social-cleaned.csv', index=False)
```

---

## 📈 Visualisations (14 Charts in Tableau)

| # | Chart Title | Chart Type | Key Finding |
|---|-------------|------------|-------------|
| 1 | Platform Popularity | Radial / Donut | Instagram #1 with 2,99,927 users |
| 2 | Addiction Level Distribution | Bar Chart | Medium addiction dominant — 5,89,843 users |
| 3 | Gender vs Addiction Level | Grouped Bar | Male & Female nearly identical across all tiers |
| 4 | Usage Purpose | Bar Chart | Entertainment leads with 4,00,000+ users |
| 5 | Users By Country | Horizontal Bar | India leads with 3,50,321 users |
| 6 | Gender Distribution | Pie Chart | Female 48.01%, Male 47.96%, Other 4.03% |
| 7 | Avg Session Minutes by Platform | Bar Chart | Instagram highest at 7M+ minutes |
| 8 | Screen Time Before Sleep | Bar Chart | Medium addiction group scrolls most before sleep |
| 9 | Mental Health Score by Platform | Bar Chart | Instagram scores 2.15M — highest mental health impact |
| 10 | Platforms Used by Gender | Treemap | Dark blue = Instagram domination for both genders |
| 11 | Daily Usage Hours by Purpose | Bar Chart | Entertainment = 14,00,000 hrs/day |
| 12 | Addiction Level by Country | Horizontal Bar | India dominates all 3 addiction tiers |
| 13 | Platform Preference by Country | Bubble Chart | YouTube India = single largest bubble globally |
| 14 | Night Usage by Country | Bar Chart | India leads at 3,50,000 night sessions |

---

## 🔑 Key Findings

### 1. 🇮🇳 India is the Defining Market
India leads every metric — users (3,50,321), night usage (3,50,000), and all addiction tiers. With growing internet penetration and a massive Gen Z population, India will shape global social media trends for the coming decade.

### 2. 📸 Instagram Dominates — But YouTube Rules India
Globally, Instagram leads in users, session time (7L+ mins), and mental health scores (2.15M). However, YouTube India is the single largest country-platform bubble in the entire dataset — video content has overtaken image-social for Indian Gen Z.

### 3. 🎮 Entertainment Dominates, But Education Is Surprisingly Strong
Entertainment commands 14 lakh daily hours — 1.6× more than Socializing. Yet Education at 7 lakh daily hours nearly matches Socializing (8.8L), showing Gen Z also uses social media as a genuine learning tool.

### 4. ⚠️ Medium Addiction is the Norm — But High Is a Crisis
58.9% of users fall in the Medium addiction tier. However, 1,58,937 High-addiction users represent a significant at-risk group — concentrated in India (55K) and USA (28K), the same countries leading night-time usage.

### 5. ⚖️ Gender is Almost Perfectly Equal
Across all platforms, the Female/Male split stays within 0.1–0.3% of each other (48.01% / 47.96%). Gen Z has truly democratised social media use across gender lines — a defining generational characteristic.

---

## 📊 Summary Statistics

| Metric | Value |
|--------|-------|
| Total Users | 10,00,000 |
| High Addiction | 1,58,937 (15.89%) |
| Medium Addiction | 5,89,843 (58.9%) |
| Low Addiction | 2,51,220 (25.1%) |
| Top Platform | Instagram — 2,99,927 users |
| Top Country | India — 3,50,321 users |
| Top Purpose | Entertainment — 14,00,000 hrs/day |
| Avg Daily Usage | 3.51 hours |
| Countries Covered | 7 |

---

## 🚀 How to Run

1. Clone this repository:
```cmd
git clone https://github.com/yourusername/genz-social-media-analysis.git
cd genz-social-media-analysis
```

2. Install dependencies:
```cmd
pip install pandas
```

3. Run the cleaning script:
```cmd
python scripts/genz-social.py
```

4. Open the cleaned CSV in Tableau Public to explore the visualisations, or refer to the PDF report for all 14 pre-built charts.

---

## 📁 Dataset Source

- **Platform:** [Kaggle](https://www.kaggle.com/)
- **Dataset:** Gen-Z Social Media Usage Dataset
- **Records:** 1,000,000+
- **Columns:** 14 (User ID, Country, Platform, Gender, Addiction Level, Purpose, Daily Usage Hours, Night Usage, Mental Health Score, Session Minutes, Age, etc.)

---

## 📋 Future Scope

- Per-capita normalisation to compare countries fairly beyond absolute counts
- Time-series analysis if longitudinal data becomes available
- Machine learning model to predict addiction level from usage patterns
- Dashboard deployment on Tableau Public for interactive public access
- Expansion to include more countries and newer platforms (Threads, BeReal)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

- Dataset provided by **Kaggle**
- Visualisations built using **Tableau Public**
- Data cleaning powered by **Python (Pandas)**

---

> ⭐ If you found this analysis useful, consider starring the repository!
