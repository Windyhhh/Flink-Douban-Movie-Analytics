# 🎬 Flink Douban Movie Analytics | 基于 Flink 的豆瓣电影数据分析

> **Real-time and batch analysis of Douban movie data using Apache Flink. Streaming processing of movie ratings, user behavior, genre trends, and recommendation signals. Flink DataStream API + Table API + SQL.**
>
> 基于 Apache Flink 的豆瓣电影数据实时与批量分析。电影评分、用户行为、类型趋势和推荐信号的流式处理。Flink DataStream API + Table API + SQL。

---

## 🌟 Features | 核心特性

- **Apache Flink** — Stream and batch processing
- **Real-time Ratings** — Streaming rating aggregation
- **Genre Analysis** — Movie category trends
- **User Behavior** — Watch patterns, rating habits
- **Recommendation Signals** — Collaborative filtering features
- **Flink SQL** — Table API and SQL queries
- **Window Operations** — Tumbling, sliding, session windows

---

## 🚀 Quick Start | 快速开始

```bash
# Start Flink cluster
start-cluster.sh

# Submit streaming job
flink run -c com.douban.StreamingAnalysis douban-flink.jar --stream ratings

# Batch analysis
flink run -c com.douban.BatchAnalysis douban-flink.jar --input movies.csv

# SQL queries
flink run -c com.douban.SqlAnalysis douban-flink.jar
```

---

## 📊 Analysis | 分析内容

| Analysis | Type | Description |
|----------|------|-------------|
| **Top Rated Movies** | Batch | Highest rated films by genre/year |
| **Rating Distribution** | Stream | Real-time rating histogram |
| **Genre Trends** | Batch | Popularity trends over years |
| **User Activity** | Stream | Active users, rating frequency |
| **Similar Movies** | Batch | Content-based similarity |
| **Hot Movies** | Stream | Trending in time windows |

---

## 📄 License | 许可证

MIT License.

[GitHub](https://github.com/Windyhhh/Flink-Douban-Movie-Analytics)
