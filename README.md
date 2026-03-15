#  Data Visualization — M512A

> A complete 7-week data visualization course project covering Matplotlib, Seaborn, Plotly, Dash, and advanced design principles using real-world datasets.

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-blue)
![Seaborn](https://img.shields.io/badge/Seaborn-0.x-teal)
![Plotly](https://img.shields.io/badge/Plotly-6.x-purple)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 👤 Author

**Om Patil**
- GitHub: [@OmPatil2806](https://github.com/OmPatil2806)
- Repository: [Data-_Visualization-M512A-](https://github.com/OmPatil2806/Data-_Visualization-M512A-)

---

## 📁 Repository Structure

```
Data-_Visualization-M512A-/
│
├── week_1_(Matplotlib)/
├── Week_2_(Seaborn)/
├── Week_3_(Plotly)/
├── Week_4_Effective_Visual_(Netflix Movies and TV Shows)/
├── week_5_(Clutter_enemy)/
├── Week_6_(Audience's_Attention)/
└── week_7_(Think_Like_Designer)/
```

---

## 📚 Weekly Breakdown

---

### 📌 [Week 1 — Matplotlib](https://github.com/OmPatil2806/Data-_Visualization-M512A-/tree/main/week_1_(Matplotlib))

| Detail | Info |
|---|---|
| **Topic** | Introduction to Matplotlib |
| **Dataset** | Iris Dataset |
| **Libraries** | NumPy, Pandas, Matplotlib |

**Visualizations Covered:**
- MATLAB-style vs Object-Oriented interface plots
- Histograms for all 4 features
- Bar chart with error bars
- 2×2 subplot grid
- Scatter plots (plain + colored by species)
- Species count bar chart
- 3D scatter plot

**Key Learning:** Understanding Matplotlib's two interfaces and building publication-quality static charts from scratch.

---

### 📌 [Week 2 — Seaborn](https://github.com/OmPatil2806/Data-_Visualization-M512A-/tree/main/Week_2_(Seaborn))

| Detail | Info |
|---|---|
| **Topic** | Statistical Visualization with Seaborn |
| **Dataset** | Titanic Dataset |
| **Libraries** | NumPy, Pandas, Matplotlib, Seaborn |

**Visualizations Covered:**
- Histogram with KDE (Age distribution)
- Bar plot with error bars (Mean Age by Gender)
- Count plots (Pclass, Survival, Gender)
- Joint plot (Age vs Fare)
- Box plots (Fare vs Survival, Age vs Pclass)
- Correlation heatmap
- FacetGrid (Survival by Gender & Class)
- Pair plot
- KDE plot (Age by Gender)
- Violin plot (Age by Gender & Survival)

**Key Learning:** Using Seaborn's high-level API for statistical visualization and discovering survival patterns in the Titanic dataset.

---

### 📌 [Week 3 — Plotly & Dash](https://github.com/OmPatil2806/Data-_Visualization-M512A-/tree/main/Week_3_(Plotly))

| Detail | Info |
|---|---|
| **Topic** | Interactive Visualizations + Dashboard |
| **Dataset** | Gapminder Dataset |
| **Libraries** | NumPy, Pandas, Plotly, Dash |

**Visualizations Covered:**
- GDP distribution histogram
- Life expectancy trend line plot
- GDP vs Life Expectancy bubble chart
- Top 20 countries by GDP (bar chart)
- World choropleth map (Life Expectancy)
- Box plots (Life Expectancy & GDP by Continent)
- CO₂ vs GDP scatter plot
- HDI vs Life Expectancy with trendline
- Services sector bar chart
- Country-level life expectancy trends
- CO₂ consumption trend over time
- HDI distribution histogram
- Continent-wise GDP over time

**Bonus:** Full **Dash dashboard** (`dashboard.py`) with all 15 visualizations in an interactive web app.

**Key Learning:** Building interactive charts with Plotly Express and deploying a multi-panel Dash dashboard.

---

### 📌 [Week 4 — Effective Visuals (Netflix)](https://github.com/OmPatil2806/Data-_Visualization-M512A-/tree/main/Week_4_Effective_Visual_(Netflix%20Movies%20and%20TV%20Shows))

| Detail | Info |
|---|---|
| **Topic** | Effective Data Visualization |
| **Dataset** | Netflix Titles Dataset (8,800+ titles) |
| **Libraries** | NumPy, Pandas, Matplotlib, Seaborn, WordCloud |

**Visualizations Covered:**
- Movies vs TV Shows bar chart
- Content type pie chart
- Content added over time (line + area)
- Top 10 countries (horizontal bar)
- Release year distribution histogram
- Ratings count plot
- Movies vs TV Shows trend over time
- Movie duration histogram with KDE
- Feature correlation heatmap
- Genre word cloud
- Top 15 directors bar chart
- Monthly content additions (stacked bar)

**Key Learning:** Choosing the right chart type for each data question and building a complete narrative from a real streaming platform dataset.

---

### 📌 [Week 5 — Clutter Is Your Enemy (Spotify)](https://github.com/OmPatil2806/Data-_Visualization-M512A-/tree/main/week_5_(Clutter_enemy))

| Detail | Info |
|---|---|
| **Topic** | Decluttering Visualizations |
| **Dataset** | Spotify Tracks Dataset (114,000 tracks) |
| **Libraries** | NumPy, Pandas, Matplotlib, Seaborn, WordCloud |
| **Reference** | [datavizproject.com](https://datavizproject.com/) |

**Concept:** For each topic, a **cluttered version ❌** is created first, followed by a **decluttered version ✅** with a critical evaluation explaining the improvements.

| # | Chart Type | Topic |
|---|---|---|
| 1 | Histogram | Popularity Distribution |
| 2 | Bar Chart | Genre Popularity |
| 3 | Scatter Plot | Energy vs Danceability |
| 4 | Bar Chart | Top Artists by Track Count |
| 5 | Heatmap | Feature Correlations |
| 6 | Box Plot | Popularity by Explicit Content |
| 7 | Violin Plot | Energy by Genre |
| 8 | Word Cloud | Common Track Name Words |

**Key Learning:** Applying Edward Tufte's data-ink ratio principle and using preattentive attributes to eliminate visual noise.

---

### 📌 [Week 6 — Audience's Attention (Global Superstore)](https://github.com/OmPatil2806/Data-_Visualization-M512A-/tree/main/Week_6_(Audience's_Attention))

| Detail | Info |
|---|---|
| **Topic** | Focus the Audience's Attention |
| **Dataset** | Global Superstore 2016 (51,290 orders) |
| **Libraries** | NumPy, Pandas, Matplotlib, Seaborn, Plotly |
| **Reference** | [datavizproject.com](https://datavizproject.com/) |

**Story Arc:** Overall Trend → Category Breakdown → Regional Analysis → Discount & Profit Impact

| # | Chart Type | Insight |
|---|---|---|
| 1 | Area Chart | Quarterly sales & profit trend |
| 2 | Grouped Bar | Annual KPI with profit margin % |
| 3 | Lollipop Chart | Profit by sub-category |
| 4 | Bubble Chart | Sales vs Profit (size = quantity) |
| 5 | Grouped Bar | Profit by Category × Segment |
| 6 | Diverging Bar | Regional profit — winners vs losers |
| 7 | Scatter Plot | Market performance quadrant |
| 8 | Choropleth Map | Country-level profit world map |
| 9 | Scatter Plot | Discount vs Profit relationship |
| 10 | Heatmap | Discount impact by category |
| 11 | Grouped Bar | Ship mode vs profit |
| 12 | Heatmap | Monthly sales calendar |

**Key Learning:** Using preattentive attributes (color, size, position, contrast) to direct viewer attention to the most important business insights.

---

### 📌 [Week 7 — Think Like a Designer (World Happiness)](https://github.com/OmPatil2806/Data-_Visualization-M512A-/tree/main/week_7_(Think_Like_Designer))

| Detail | Info |
|---|---|
| **Topic** | Advanced & Unique Visualization Types |
| **Dataset** | World Happiness Report 2015 (158 countries) |
| **Libraries** | NumPy, Pandas, Matplotlib, Seaborn, Plotly, Squarify, PyWaffle, SciPy |
| **Reference** | [datavizproject.com](https://datavizproject.com/) |

**Only unique chart types from datavizproject.com — no basic bar/line/pie charts.**

| # | Chart Type | Topic |
|---|---|---|
| 1 | Lollipop Chart | Top & Bottom 15 countries |
| 2 | Violin Plot | Score distribution by region |
| 3 | Waffle Chart | Countries by happiness tier |
| 4 | Treemap | Countries sized by happiness score |
| 5 | Choropleth Map | World happiness map |
| 6 | Radar / Spider Chart | Factor profiles by region |
| 7 | Heatmap | Correlation between factors |
| 8 | Parallel Coordinates | Top 20 vs Bottom 20 |
| 9 | Slope Chart | GDP rank vs Freedom rank |
| 10 | Dot Plot | Top GDP countries |
| 11 | Mosaic Plot | Region × Happiness tier |
| 12 | Interactive Parallel Coords | All factors (Plotly) |

**Key Learning:** Thinking like a designer — choosing the right chart type for each data relationship, applying colorblind-safe palettes, and telling a complete data story.

---

## 🛠️ Installation

**Clone the repository:**
```bash
git clone https://github.com/OmPatil2806/Data-_Visualization-M512A-.git
cd Data-_Visualization-M512A-
```

**Install all required libraries:**
```bash
pip install numpy pandas matplotlib seaborn plotly dash wordcloud squarify pywaffle scipy openpyxl nbformat statsmodels
```

**Or using Miniconda (recommended):**
```bash
c:\Users\<username>\miniconda3\python.exe -m pip install numpy pandas matplotlib seaborn plotly dash wordcloud squarify pywaffle scipy openpyxl statsmodels
```

---

## ▶️ Running the Notebooks

1. Navigate to any week's folder
2. Place the dataset CSV/Excel file in the same folder
3. Open Jupyter Notebook:
```bash
jupyter notebook
```
4. Run all cells: **Kernel → Restart & Run All**

**For Week 3 Dash Dashboard:**
```bash
python dashboard.py
```
Then open `http://127.0.0.1:8050` in your browser.

---

## 📦 Datasets Used

| Week | Dataset | Source |
|---|---|---|
| Week 1 | Iris Dataset | Attached CSV |
| Week 2 | Titanic Dataset | Attached CSV |
| Week 3 | Gapminder Dataset | Attached CSV |
| Week 4 | Netflix Titles | Attached CSV |
| Week 5 | Spotify Tracks | Attached CSV |
| Week 6 | Global Superstore 2016 | Attached XLSX |
| Week 7 | World Happiness Report 2015 | Attached CSV |

---

## 🎨 Design Principles Applied

- **Colorblind-safe palettes** (Wong 2011) used throughout
- **Decluttering** — removed chartjunk, unnecessary gridlines, excess colors
- **Preattentive attributes** — color, size, position used to direct attention
- **Data-ink ratio** — every element justifies its presence
- **Storytelling** — each notebook follows a logical narrative arc
- **Interactivity** — Plotly and Dash used for exploratory analysis

---

## 📄 License

This project is for academic purposes under the **M512A Data Visualization** course.

---

