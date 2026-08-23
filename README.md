# 🎬 Flink 豆瓣电影实时数据分析 | Flink Douban Movie Real-Time Analytics

> **基于 Apache Flink 的豆瓣电影实时数据分析系统——实时评分流处理、热门电影统计、用户行为分析、情感分析、可视化大屏，打造电影大数据实时洞察平台。**
>
> *Douban movie real-time data analytics system based on Apache Flink — real-time rating stream processing, hot movie statistics, user behavior analysis, sentiment analysis, visualization dashboard, building a movie big data real-time insight platform.*

---

## ⭐ 核心卖点 | Why Star This

| 卖点 | Feature | 一句话 |
|------|---------|--------|
| ⚡ **Flink 实时流** | Flink Stream Processing | 毫秒级实时流处理，Exactly-Once 语义保证 |
| 🎬 **电影数据分析** | Movie Analytics | 评分、评论、用户行为多维度电影数据分析 |
| 🔥 **实时热门榜** | Real-Time Hot Ranking | 实时热门电影排行榜，滑动窗口统计 |
| 😊 **评论情感分析** | Sentiment Analysis | 电影评论文本情感分析，口碑实时监控 |
| 📊 **可视化大屏** | Visualization Dashboard | ECharts 实时数据大屏，电影数据一目了然 |

---

## 🏆 技术栈 | Tech Stack

![Java](https://img.shields.io/badge/Java-8+-orange?logo=openjdk)
![Flink](https://img.shields.io/badge/Flink-1.17+-blue?logo=apacheflink)
![Kafka](https://img.shields.io/badge/Kafka-3.0+-black?logo=apachekafka)
![Redis](https://img.shields.io/badge/Redis-7.0+-red?logo=redis)
![MySQL](https://img.shields.io/badge/MySQL-8.0+-blue?logo=mysql)
![Elasticsearch](https://img.shields.io/badge/Elasticsearch-7.10+-blue?logo=elasticsearch)
![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Vue.js](https://img.shields.io/badge/Vue-3.0+-brightgreen?logo=vuedotjs)
![ECharts](https://img.shields.io/badge/ECharts-5.0+-orange?logo=apacheecharts)
![Docker](https://img.shields.io/badge/Docker-24.0+-blue?logo=docker)

---

## 📊 系统架构 | System Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                        数据采集层 (Data Source)                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐              │
│  │ 豆瓣评分数据   │  │ 豆瓣评论数据   │  │ 用户行为数据   │  ...       │
│  │ (爬虫/API)    │  │ (爬虫/API)    │  │ (埋点/日志)   │              │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘              │
│         └───────────────────┼───────────────────┘                       │
│                             │                                            │
│                    ┌────────▼────────┐                                   │
│                    │   数据模拟器      │                                   │
│                    │ (实时生成数据流)   │                                   │
│                    └────────┬────────┘                                   │
└─────────────────────────────┼───────────────────────────────────────────┘
                              │
┌─────────────────────────────▼───────────────────────────────────────────┐
│                        消息队列层 (Message Queue)                         │
│                    ┌──────────────────────────┐                          │
│                    │      Apache Kafka         │                          │
│                    │  Topics:                   │                          │
│                    │  - ratings (评分流)       │                          │
│                    │  - comments (评论流)      │                          │
│                    │  - user_behavior (行为流) │                          │
│                    └────────────┬─────────────┘                          │
└─────────────────────────────────┼─────────────────────────────────────────┘
                                  │
┌─────────────────────────────────▼─────────────────────────────────────────┐
│                        流处理层 (Stream Processing)                        │
│                    ┌──────────────────────────┐                          │
│                    │      Apache Flink         │                          │
│                    │                           │                          │
│                    │  ┌────────────────────┐  │                          │
│                    │  │ 评分流处理 Job       │  │                          │
│                    │  │ - 实时平均分计算     │  │                          │
│                    │  │ - 评分分布统计       │  │                          │
│                    │  │ - 热门电影排行       │  │                          │
│                    │  └────────────────────┘  │                          │
│                    │                           │                          │
│                    │  ┌────────────────────┐  │                          │
│                    │  │ 评论流处理 Job       │  │                          │
│                    │  │ - 情感分析           │  │                          │
│                    │  │ - 关键词提取         │  │                          │
│                    │  │ - 评论热度统计       │  │                          │
│                    │  └────────────────────┘  │                          │
│                    │                           │                          │
│                    │  ┌────────────────────┐  │                          │
│                    │  │ 用户行为分析 Job     │  │                          │
│                    │  │ - 实时在线人数       │  │                          │
│                    │  │ - 用户活跃度统计     │  │                          │
│                    │  │ - 观影偏好分析       │  │                          │
│                    │  └────────────────────┘  │                          │
│                    └────────────┬─────────────┘                          │
└─────────────────────────────────┼─────────────────────────────────────────┘
                                  │
          ┌───────────────────────┼───────────────────────┐
          │                       │                       │
┌─────────▼─────────┐ ┌─────────▼─────────┐ ┌─────────▼─────────┐
│   Redis (实时缓存)  │ │  MySQL (结果存储)  │ │ Elasticsearch     │
│  - 实时排行榜       │ │  - 历史统计数据     │ │  - 评论全文检索    │
│  - 在线人数         │ │  - 电影信息         │ │  - 日志存储        │
│  - 热门电影         │ │  - 用户画像         │ │  - 数据分析        │
└─────────┬─────────┘ └─────────┬─────────┘ └─────────┬─────────┘
          │                       │                       │
          └───────────────────────┼───────────────────────┘
                                  │
┌─────────────────────────────────▼─────────────────────────────────────────┐
│                        API 服务层 (API Service)                            │
│                    ┌──────────────────────────┐                          │
│                    │   Spring Boot / Flask     │                          │
│                    │  - 实时数据查询 API        │                          │
│                    │  - 历史数据分析 API        │                          │
│                    │  - WebSocket 实时推送      │                          │
│                    └────────────┬─────────────┘                          │
└─────────────────────────────────┼─────────────────────────────────────────┘
                                  │
┌─────────────────────────────────▼─────────────────────────────────────────┐
│                        可视化层 (Visualization)                             │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │              Vue 3 + ECharts 实时数据大屏                         │  │
│  │  实时评分 | 热门榜单 | 情感分析 | 用户行为 | 电影分布             │  │
│  └──────────────────────────────────────────────────────────────────┘  │
└───────────────────────────────────────────────────────────────────────────┘
```

---

## 🚀 快速开始 | Quick Start

```bash
git clone https://github.com/Windyhhh/Flink-Douban-Movie-Analytics.git
cd Flink-Douban-Movie-Analytics

# 1. 启动基础设施
docker-compose up -d kafka redis mysql elasticsearch flink-jobmanager flink-taskmanager

# 2. 创建 Kafka Topics
docker exec -it kafka kafka-topics.sh --create --topic ratings --bootstrap-server localhost:9092 --partitions 3
docker exec -it kafka kafka-topics.sh --create --topic comments --bootstrap-server localhost:9092 --partitions 3
docker exec -it kafka kafka-topics.sh --create --topic user_behavior --bootstrap-server localhost:9092 --partitions 3

# 3. 初始化数据库
mysql -u root -p < sql/init.sql

# 4. 编译 Flink 作业
cd flink-jobs
mvn clean package -DskipTests

# 5. 提交 Flink 作业到集群
flink run -c com.movie.analytics.RatingStreamJob target/flink-douban-movie-1.0.jar
flink run -c com.movie.analytics.CommentStreamJob target/flink-douban-movie-1.0.jar
flink run -c com.movie.analytics.UserBehaviorJob target/flink-douban-movie-1.0.jar

# 6. 启动数据模拟器 (生成实时数据流)
cd ../data-simulator
pip install -r requirements.txt
python simulator.py --rate 1000  # 每秒1000条数据

# 7. 启动 API 服务
cd ../api
pip install -r requirements.txt
python app.py --port 5000

# 8. 启动前端
cd ../frontend
npm install
npm run dev

# 9. 访问系统
# 数据大屏: http://localhost:5173
# Flink Dashboard: http://localhost:8081
# API 文档: http://localhost:5000/api/docs
```

---

## 📂 项目结构 | Project Structure

```
Flink-Douban-Movie-Analytics/
├── flink-jobs/                 # Flink 流处理作业
│   ├── src/main/java/com/movie/analytics/
│   │   ├── RatingStreamJob.java      # 评分流处理
│   │   ├── CommentStreamJob.java     # 评论流处理
│   │   ├── UserBehaviorJob.java      # 用户行为分析
│   │   ├── model/                     # 数据模型
│   │   │   ├── Rating.java
│   │   │   ├── Comment.java
│   │   │   ├── UserBehavior.java
│   │   │   └── MovieStats.java
│   │   ├── source/                    # 数据源
│   │   │   ├── KafkaRatingSource.java
│   │   │   ├── KafkaCommentSource.java
│   │   │   └── KafkaBehaviorSource.java
│   │   ├── sink/                      # 数据汇
│   │   │   ├── RedisSink.java
│   │   │   ├── MySQLSink.java
│   │   │   └── ElasticsearchSink.java
│   │   ├── process/                   # 处理函数
│   │   │   ├── RatingAggregator.java  # 评分聚合
│   │   │   ├── HotMovieFunction.java  # 热门电影
│   │   │   ├── SentimentFunction.java # 情感分析
│   │   │   └── UserActivityFunction.java # 用户活跃度
│   │   ├── window/                    # 窗口函数
│   │   │   ├── SlidingWindowStats.java
│   │   │   └── TumblingWindowStats.java
│   │   └── util/                      # 工具类
│   │       ├── ConfigUtil.java
│   │       └── DateUtil.java
│   ├── src/main/resources/
│   │   └── flink-conf.yaml
│   └── pom.xml
├── data-simulator/             # 数据模拟器
│   ├── simulator.py            # 主模拟器
│   ├── generators/             # 数据生成器
│   │   ├── rating_generator.py
│   │   ├── comment_generator.py
│   │   └── behavior_generator.py
│   ├── kafka_producer.py       # Kafka 生产者
│   ├── data/                   # 样本数据
│   │   ├── movies.csv
│   │   ├── users.csv
│   │   └── comments.txt
│   └── requirements.txt
├── api/                        # API 服务
│   ├── app.py                  # Flask 应用
│   ├── config.py
│   ├── api/                    # API 路由
│   │   ├── realtime.py         # 实时数据
│   │   ├── movies.py           # 电影数据
│   │   ├── stats.py            # 统计分析
│   │   └── websocket.py        # WebSocket 推送
│   ├── services/               # 业务逻辑
│   │   ├── redis_service.py
│   │   ├── mysql_service.py
│   │   └── es_service.py
│   └── requirements.txt
├── frontend/                   # Vue 3 前端
│   ├── src/
│   │   ├── views/              # 页面
│   │   │   ├── Dashboard.vue   # 实时大屏
│   │   │   ├── Movies.vue      # 电影列表
│   │   │   ├── MovieDetail.vue # 电影详情
│   │   │   ├── Ratings.vue     # 评分分析
│   │   │   ├── Comments.vue    # 评论分析
│   │   │   └── Users.vue       # 用户分析
│   │   ├── components/         # 组件
│   │   │   ├── charts/         # 图表组件
│   │   │   │   ├── RealtimeLineChart.vue
│   │   │   │   ├── HotMovieRank.vue
│   │   │   │   ├── SentimentGauge.vue
│   │   │   │   ├── RatingDistribution.vue
│   │   │   │   └── WordCloudChart.vue
│   │   │   ├── MovieCard.vue
│   │   │   └── StatsCard.vue
│   │   ├── api/                # API 调用
│   │   ├── store/              # Pinia
│   │   ├── websocket/          # WebSocket
│   │   └── router/             # 路由
│   └── package.json
├── sql/                        # SQL 脚本
│   ├── init.sql                # 初始化
│   ├── ddl.sql                 # 建表
│   └── analytics.sql           # 分析查询
├── docker-compose.yml          # Docker 编排
├── deploy/                     # 部署脚本
│   ├── submit-flink-jobs.sh
│   ├── start-all.sh
│   └── stop-all.sh
└── README.md
```

---

## 🔬 核心 Flink 作业 | Core Flink Jobs

### 评分流处理 | Rating Stream Processing

```java
// RatingStreamJob.java - 实时评分流处理
package com.movie.analytics;

import com.movie.analytics.model.Rating;
import com.movie.analytics.model.MovieStats;
import com.movie.analytics.source.KafkaRatingSource;
import com.movie.analytics.sink.RedisSink;
import com.movie.analytics.sink.MySQLSink;
import com.movie.analytics.process.RatingAggregator;
import com.movie.analytics.process.HotMovieFunction;
import org.apache.flink.api.common.eventtime.WatermarkStrategy;
import org.apache.flink.api.common.functions.AggregateFunction;
import org.apache.flink.api.java.tuple.Tuple2;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.api.windowing.assigners.SlidingEventTimeWindows;
import org.apache.flink.streaming.api.windowing.assigners.TumblingEventTimeWindows;
import org.apache.flink.streaming.api.windowing.time.Time;
import org.apache.flink.streaming.api.windowing.triggers.ContinuousProcessingTimeTrigger;

import java.time.Duration;

public class RatingStreamJob {
    
    public static void main(String[] args) throws Exception {
        // 1. 获取执行环境
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        env.enableCheckpointing(60000); // 60秒 checkpoint
        env.setParallelism(3);
        
        // 2. 从 Kafka 读取评分数据流
        DataStream<Rating> ratingStream = env
            .addSource(new KafkaRatingSource("ratings"))
            .assignTimestampsAndWatermarks(
                WatermarkStrategy.<Rating>forBoundedOutOfOrderness(Duration.ofSeconds(5))
                    .withTimestampAssigner((rating, timestamp) -> rating.getTimestamp())
            );
        
        // 3. 实时平均分计算 (滑动窗口: 1分钟窗口，10秒滑动)
        DataStream<MovieStats> avgRatingStream = ratingStream
            .keyBy(Rating::getMovieId)
            .window(SlidingEventTimeWindows.of(Time.minutes(1), Time.seconds(10)))
            .aggregate(new RatingAggregator());
        
        // 4. 热门电影排行榜 (滚动窗口: 5分钟)
        DataStream<Tuple2<String, Double>> hotMovieStream = ratingStream
            .keyBy(Rating::getMovieId)
            .window(TumblingEventTimeWindows.of(Time.minutes(5)))
            .aggregate(new RatingCountAggregator())
            .keyBy(tuple -> "all")
            .process(new HotMovieFunction(10)); // Top 10
        
        // 5. 评分分布统计
        DataStream<Tuple2<Integer, Long>> ratingDistribution = ratingStream
            .map(rating -> Tuple2.of(rating.getScore(), 1L))
            .returns(Tuple2.class)
            .keyBy(tuple -> tuple.f0)
            .window(TumblingEventTimeWindows.of(Time.minutes(1)))
            .sum(1);
        
        // 6. 输出结果
        avgRatingStream.addSink(new RedisSink("movie:avg_rating"));
        hotMovieStream.addSink(new RedisSink("movie:hot_rank"));
        ratingDistribution.addSink(new MySQLSink("rating_distribution"));
        
        // 7. 执行作业
        env.execute("Douban Movie Rating Stream Analytics");
    }
    
    /**
     * 评分聚合函数: 计算平均分、评分人数
     */
    public static class RatingAggregator implements AggregateFunction<Rating, RatingAccumulator, MovieStats> {
        
        @Override
        public RatingAccumulator createAccumulator() {
            return new RatingAccumulator();
        }
        
        @Override
        public RatingAccumulator add(Rating rating, RatingAccumulator acc) {
            acc.count++;
            acc.sum += rating.getScore();
            acc.movieId = rating.getMovieId();
            acc.movieName = rating.getMovieName();
            return acc;
        }
        
        @Override
        public MovieStats getResult(RatingAccumulator acc) {
            MovieStats stats = new MovieStats();
            stats.setMovieId(acc.movieId);
            stats.setMovieName(acc.movieName);
            stats.setRatingCount(acc.count);
            stats.setAvgRating(acc.count > 0 ? acc.sum / acc.count : 0.0);
            stats.setTimestamp(System.currentTimeMillis());
            return stats;
        }
        
        @Override
        public RatingAccumulator merge(RatingAccumulator a, RatingAccumulator b) {
            a.count += b.count;
            a.sum += b.sum;
            return a;
        }
    }
    
    /**
     * 评分累加器
     */
    public static class RatingAccumulator {
        public String movieId;
        public String movieName;
        public long count = 0;
        public double sum = 0.0;
    }
}
```

### 评论情感分析 | Comment Sentiment Analysis

```java
// CommentStreamJob.java - 评论流处理与情感分析
package com.movie.analytics;

import com.movie.analytics.model.Comment;
import com.movie.analytics.process.SentimentFunction;
import com.movie.analytics.sink.RedisSink;
import com.movie.analytics.sink.ElasticsearchSink;
import org.apache.flink.api.common.eventtime.WatermarkStrategy;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.api.windowing.assigners.TumblingEventTimeWindows;
import org.apache.flink.streaming.api.windowing.time.Time;

import java.time.Duration;

public class CommentStreamJob {
    
    public static void main(String[] args) throws Exception {
        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        env.enableCheckpointing(60000);
        
        // 1. 读取评论流
        DataStream<Comment> commentStream = env
            .addSource(new KafkaCommentSource("comments"))
            .assignTimestampsAndWatermarks(
                WatermarkStrategy.<Comment>forBoundedOutOfOrderness(Duration.ofSeconds(10))
                    .withTimestampAssigner((comment, ts) -> comment.getTimestamp())
            );
        
        // 2. 情感分析 (调用 Python 情感分析服务)
        DataStream<CommentWithSentiment> sentimentStream = commentStream
            .process(new SentimentFunction());
        
        // 3. 电影口碑统计 (按电影分组，统计情感分布)
        DataStream<MovieSentimentStats> movieSentimentStream = sentimentStream
            .keyBy(CommentWithSentiment::getMovieId)
            .window(TumblingEventTimeWindows.of(Time.minutes(5)))
            .aggregate(new SentimentAggregator());
        
        // 4. 评论关键词提取 (实时热词)
        DataStream<KeywordCount> keywordStream = sentimentStream
            .flatMap(new KeywordExtractor())
            .keyBy(KeywordCount::getKeyword)
            .window(TumblingEventTimeWindows.of(Time.minutes(5)))
            .sum("count")
            .keyBy("all")
            .process(new TopKeywordsFunction(20));
        
        // 5. 输出
        sentimentStream.addSink(new ElasticsearchSink("comments"));
        movieSentimentStream.addSink(new RedisSink("movie:sentiment"));
        keywordStream.addSink(new RedisSink("movie:hot_keywords"));
        
        env.execute("Douban Movie Comment Stream Analytics");
    }
}

// SentimentFunction.java - 情感分析处理函数
public class SentimentFunction extends ProcessFunction<Comment, CommentWithSentiment> {
    
    private transient HttpClient httpClient;
    private static final String SENTIMENT_API = "http://localhost:5000/api/sentiment";
    
    @Override
    public void open(Configuration parameters) {
        httpClient = HttpClient.newHttpClient();
    }
    
    @Override
    public void processElement(Comment comment, Context ctx, Collector<CommentWithSentiment> out) {
        try {
            // 调用情感分析 API
            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(SENTIMENT_API))
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(
                    String.format("{\"text\": \"%s\"}", comment.getContent().replace("\"", "\\\""))
                ))
                .build();
            
            HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());
            JSONObject result = new JSONObject(response.body());
            
            // 构建带情感的评论
            CommentWithSentiment result = new CommentWithSentiment();
            result.setCommentId(comment.getCommentId());
            result.setMovieId(comment.getMovieId());
            result.setUserId(comment.getUserId());
            result.setContent(comment.getContent());
            result.setSentiment(result.getString("sentiment")); // positive/neutral/negative
            result.setSentimentScore(result.getDouble("score"));
            result.setKeywords(result.getJSONArray("keywords").toList());
            result.setTimestamp(comment.getTimestamp());
            
            out.collect(result);
            
        } catch (Exception e) {
            // 异常处理: 默认中性情感
            CommentWithSentiment fallback = new CommentWithSentiment();
            fallback.setCommentId(comment.getCommentId());
            fallback.setMovieId(comment.getMovieId());
            fallback.setContent(comment.getContent());
            fallback.setSentiment("neutral");
            fallback.setSentimentScore(0.5);
            fallback.setTimestamp(comment.getTimestamp());
            out.collect(fallback);
        }
    }
}
```

### 实时热门电影排行 | Real-Time Hot Movie Ranking

```java
// HotMovieFunction.java - 热门电影排行榜
public class HotMovieFunction extends KeyedProcessFunction<String, Tuple2<String, Long>, List<HotMovie>> {
    
    private final int topN;
    private transient ListState<Tuple2<String, Long>> movieState;
    
    public HotMovieFunction(int topN) {
        this.topN = topN;
    }
    
    @Override
    public void open(Configuration parameters) {
        ListStateDescriptor<Tuple2<String, Long>> descriptor = new ListStateDescriptor<>(
            "hot-movies",
            TypeInformation.of(new TypeHint<Tuple2<String, Long>>() {})
        );
        movieState = getRuntimeContext().getListState(descriptor);
    }
    
    @Override
    public void processElement(Tuple2<String, Long> value, Context ctx, Collector<List<HotMovie>> out) throws Exception {
        // 添加到状态
        movieState.add(value);
        
        // 注册定时器 (窗口结束时触发)
        ctx.timerService().registerEventTimeTimer(ctx.timestamp() + 1);
    }
    
    @Override
    public void onTimer(long timestamp, OnTimerContext ctx, Collector<List<HotMovie>> out) throws Exception {
        // 收集所有电影的评分次数
        List<Tuple2<String, Long>> allMovies = new ArrayList<>();
        for (Tuple2<String, Long> movie : movieState.get()) {
            allMovies.add(movie);
        }
        
        // 排序取 Top N
        allMovies.sort((a, b) -> Long.compare(b.f1, a.f1));
        List<HotMovie> topMovies = new ArrayList<>();
        
        for (int i = 0; i < Math.min(topN, allMovies.size()); i++) {
            Tuple2<String, Long> movie = allMovies.get(i);
            HotMovie hotMovie = new HotMovie();
            hotMovie.setRank(i + 1);
            hotMovie.setMovieId(movie.f0);
            hotMovie.setRatingCount(movie.f1);
            hotMovie.setTimestamp(timestamp);
            topMovies.add(hotMovie);
        }
        
        // 清空状态
        movieState.clear();
        
        // 输出排行榜
        out.collect(topMovies);
    }
}
```

---

## 📊 实时数据大屏 | Real-Time Dashboard

```
┌─────────────────────────────────────────────────────────────────────┐
│  🎬 豆瓣电影实时数据分析大屏                📡 数据流: 1,256 条/秒   │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐              │
│  │ 今日评分   │ │ 平均评分   │ │ 在线用户   │ │ 评论数    │              │
│  │  125,680  │ │   7.8    │ │   3,256  │ │  18,520  │              │
│  │ ↑15.2%   │ │ ↑0.3     │ │ ↑256     │ │ ↑12.8%   │              │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘              │
│                                                                     │
│  ┌─────────────────────────────┐ ┌─────────────────────────────┐  │
│  │ 🔥 实时热门电影 Top 10       │ │ 📈 实时评分流 (最近1分钟)     │  │
│  │                             │ │                             │  │
│  │  1. 流浪地球3  █████████ 9856│ │  评分  ████████████████ 8.5 │  │
│  │  2. 满江红    ████████  8542│ │        ██████████████░░ 7.2 │  │
│  │  3. 封神第二部 ███████   7621│ │        ████████████████ 9.1 │  │
│  │  4. 无名      ██████    6854│ │                             │  │
│  │  5. 深海      █████     5987│ │  10:00  10:15  10:30 10:45│  │
│  │  ...                         │ │                             │  │
│  │                             │ └─────────────────────────────┘  │
│  └─────────────────────────────┘                                    │
│                                    ┌─────────────────────────────┐  │
│  ┌─────────────────────────────┐ │ 😊 评论情感分析 (实时)        │  │
│  │ 📊 评分分布                  │ │                             │  │
│  │                             │ │  正面  ████████████  68%    │  │
│  │  5星  ████████████  35%    │ │  中性  ██████        22%    │  │
│  │  4星  ██████████    28%    │ │  负面  ████          10%    │  │
│  │  3星  ██████        18%    │ │                             │  │
│  │  2星  ████          12%    │ │  口碑指数: 82.5 (良好)       │  │
│  │  1星  ██             7%    │ │                             │  │
│  │                             │ └─────────────────────────────┘  │
│  └─────────────────────────────┘                                    │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │ ☁️ 实时热词云 (评论关键词)                                     │   │
│  │                                                               │   │
│  │      剧情    特效    演技    画面    音乐    导演             │   │
│  │         感动    震撼    精彩    深刻    治愈    燃            │   │
│  │            科幻    悬疑    爱情    喜剧    动作                │   │
│  │                                                               │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 🎯 应用场景 | Use Cases

- 🎬 **电影平台**：实时热门电影推荐和口碑监控
- 📊 **数据分析**：电影大数据实时分析和可视化
- 🧪 **流处理教学**：Flink 实时流处理教学项目
- 🏢 **企业监控**：实时数据大屏和业务监控
- 📱 **推荐系统**：基于实时评分的电影推荐
- 📰 **舆情监控**：电影评论情感分析和舆情监控
- 🎓 **课程设计**：大数据专业毕业设计/课程设计
- 💻 **全栈项目**：Flink + Kafka + Vue 全栈开发教学

---

## 📚 参考文献 | References

- Apache Flink Documentation. flink.apache.org 2023.
- "Stream Processing with Apache Flink" by Fabian Hueske, Vasiliki Kalavri. O'Reilly 2019.
- Carbone, P., et al. "Apache Flink: Stream and Batch Processing in a Single Engine." IEEE Data Eng. Bull. 2015.
- Apache Kafka Documentation. kafka.apache.org 2023.
- "Real-Time Data Analytics with Flink and Kafka." 2022.

---

## 📄 License

MIT License — 自由使用、修改和分发。

---

> 💡 **Flink + Kafka + 实时大屏的电影数据分析系统，Star ⭐ 探索实时大数据的魅力！**
