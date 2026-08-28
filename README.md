<div align="center">

# 🎬 Flink-Douban-Movie-Analytics

### Apache Flink analytics on Douban movie data.

Stream processing, ratings analysis and recommendation-oriented statistics on Douban movie data.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Apache Flink](https://img.shields.io/badge/Flink-1.14-E6526F?logo=apacheflink&logoColor=white)](https://flink.apache.org/)

</div>

---

**Flink-Douban-Movie-Analytics** analyzes **Douban movie data** with **Apache Flink** — stream processing over ratings, play counts and genres, producing recommendation-oriented aggregate statistics.

> [!NOTE]
> 中文项目：Apache Flink 豆瓣电影数据分析——流处理、评分、推荐相关统计。

---

## Quickstart

```bash
git clone https://github.com/Windyhhh/Flink-Douban-Movie-Analytics.git
cd Flink-Douban-Movie-Analytics

# Open the notebook and run cells
jupyter notebook
```

Output aggregates (genre averages, year trends, play-rating correlation, top favorites) land in `output/`.

---

## Features

- **Flink stream processing** — ratings and play-count analytics.
- **Recommendation-oriented** — top favorites, genre avg ratings, correlations.
- **Reproducible** — notebook + datasets + reports included.

---

## Project Structure

```
Flink-Douban-Movie-Analytics/
├── data/douban_2.csv          # dataset
├── output/                    # generated aggregates
├── reports/                   # experiment reports
└── docs/                      # task & usage notes
```

---


## Results

<div align="center">
  <img src="visualizations/3_演员影响力.png" alt="Top actor influence" width="70%"/>
  <img src="visualizations/4_类型组合偏好.png" alt="Genre combination preference" width="70%"/>
</div>

---
## License

MIT — free to use, modify and distribute.
