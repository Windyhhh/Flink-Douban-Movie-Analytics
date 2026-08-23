"""
豆瓣电影数据可视化脚本
生成所有8个分析任务的图表
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
import matplotlib.font_manager as fm
import warnings
warnings.filterwarnings('ignore')

# 查找并设置中文字体
def get_chinese_font():
    """获取系统中可用的中文字体 - 优先使用简体中文字体"""
    # Windows系统常见简体中文字体（按优先级排序）
    font_candidates = [
        'Microsoft YaHei',  # 微软雅黑 - 最佳选择
        'SimHei',           # 黑体
        'SimSun',           # 宋体
        'KaiTi',            # 楷体
        'FangSong',         # 仿宋
        'STSong',           # 华文宋体
        'STHeiti',          # 华文黑体
    ]

    # 获取系统所有字体
    available_fonts = [f.name for f in fm.fontManager.ttflist]

    print(f"系统中找到 {len(available_fonts)} 个字体")

    # 查找第一个可用的简体中文字体
    for font in font_candidates:
        if font in available_fonts:
            print(f"✓ 使用中文字体: {font}")
            return font

    print("⚠ 未找到推荐的中文字体，使用默认字体")
    return 'sans-serif'

# 设置中文字体和样式
chinese_font = get_chinese_font()

# 先设置seaborn样式
sns.set_style("whitegrid")
sns.set_palette("husl")

# 然后强制设置中文字体（必须在seaborn之后）
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'SimSun', 'KaiTi']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 10

# 清除matplotlib字体缓存
import matplotlib as mpl
mpl.rcParams['font.family'] = 'sans-serif'

print(f"✓ 字体配置完成: {plt.rcParams['font.sans-serif'][0]}")

# 创建输出目录
os.makedirs('visualizations', exist_ok=True)

print("开始生成可视化图表...")

# ==================== 图表1：年度电影产量趋势 ====================
print("\n[1/8] 生成年度电影产量趋势图...")
try:
    df1 = pd.read_csv('output/year_count.csv', names=['year', 'count'])
    df1 = df1.sort_values('year')
    
    fig, ax = plt.subplots(figsize=(14, 6))
    
    # 绘制折线图
    ax.plot(df1['year'], df1['count'], linewidth=2.5, color='#2E86AB', 
            marker='o', markersize=5, markerfacecolor='#A23B72', 
            markeredgewidth=0, alpha=0.8)
    
    # 填充区域
    ax.fill_between(df1['year'], df1['count'], alpha=0.2, color='#2E86AB')
    
    # 标注峰值
    peak_idx = df1['count'].idxmax()
    peak_year = df1.loc[peak_idx, 'year']
    peak_count = df1.loc[peak_idx, 'count']
    ax.annotate(f'峰值: {peak_year}年\n{peak_count}部',
                xy=(peak_year, peak_count),
                xytext=(peak_year-5, peak_count+300),
                arrowprops=dict(arrowstyle='->', color='red', lw=2),
                fontsize=12, color='red', weight='bold',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7))
    
    ax.set_title('豆瓣电影年度产量趋势分析 (1900-2019)', fontsize=16, weight='bold', pad=20)
    ax.set_xlabel('年份', fontsize=13)
    ax.set_ylabel('电影数量（部）', fontsize=13)
    ax.grid(True, alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    plt.savefig('visualizations/1_年度产量趋势.png', dpi=300, bbox_inches='tight')
    print("✓ 已保存: visualizations/1_年度产量趋势.png")
    plt.close()
except Exception as e:
    print(f"✗ 错误: {e}")

# ==================== 图表2：评分人数区间分布 ====================
print("\n[2/8] 生成评分人数区间分布图...")
try:
    df2 = pd.read_csv('output/play_count_range.csv', names=['range', 'count'])
    
    # 定义区间顺序
    range_order = ['0-100', '100-1K', '1K-10K', '10K-100K', '100K-500K', '>500K']
    df2['range'] = pd.Categorical(df2['range'], categories=range_order, ordered=True)
    df2 = df2.sort_values('range')
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # 左图：柱状图
    colors = sns.color_palette("YlOrRd", len(df2))
    bars = ax1.bar(df2['range'], df2['count'], color=colors, 
                   edgecolor='black', linewidth=1.5, alpha=0.8)
    
    # 添加数值标签
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                 f'{int(height):,}',
                 ha='center', va='bottom', fontsize=11, weight='bold')
    
    ax1.set_title('评分人数区间分布（柱状图）', fontsize=15, weight='bold')
    ax1.set_xlabel('评分人数区间', fontsize=12)
    ax1.set_ylabel('电影数量', fontsize=12)
    ax1.tick_params(axis='x', rotation=30)
    ax1.grid(axis='y', alpha=0.3, linestyle='--')
    
    # 右图：饼图
    colors_pie = sns.color_palette("Set2", len(df2))
    wedges, texts, autotexts = ax2.pie(df2['count'], labels=df2['range'], 
                                         autopct='%1.1f%%',
                                         colors=colors_pie, startangle=90,
                                         textprops={'fontsize': 10, 'weight': 'bold'})
    
    ax2.set_title('评分人数区间占比（饼图）', fontsize=15, weight='bold')
    
    plt.tight_layout()
    plt.savefig('visualizations/2_评分人数分布.png', dpi=300, bbox_inches='tight')
    print("✓ 已保存: visualizations/2_评分人数分布.png")
    plt.close()
except Exception as e:
    print(f"✗ 错误: {e}")

# ==================== 图表3：热门演员影响力 ====================
print("\n[3/8] 生成热门演员影响力图...")
try:
    df3 = pd.read_csv('output/artist_count.csv', names=['artist', 'count'])
    df3 = df3.sort_values('count', ascending=False).head(15)
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    colors = sns.color_palette("viridis", len(df3))
    bars = ax.barh(range(len(df3)), df3['count'], color=colors, 
                   edgecolor='black', linewidth=1.2, alpha=0.8)
    
    # 设置y轴标签
    ax.set_yticks(range(len(df3)))
    ax.set_yticklabels(df3['artist'], fontsize=11)
    
    # 添加数值标签
    for i, bar in enumerate(bars):
        width = bar.get_width()
        ax.text(width + 1, bar.get_y() + bar.get_height()/2,
                f'{int(width)}部',
                ha='left', va='center', fontsize=10, weight='bold')
    
    ax.set_title('热门演员出演电影数量 TOP15', fontsize=16, weight='bold', pad=20)
    ax.set_xlabel('出演电影数量', fontsize=13)
    ax.set_ylabel('演员姓名', fontsize=13)
    ax.invert_yaxis()
    ax.grid(axis='x', alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    plt.savefig('visualizations/3_演员影响力.png', dpi=300, bbox_inches='tight')
    print("✓ 已保存: visualizations/3_演员影响力.png")
    plt.close()
except Exception as e:
    print(f"✗ 错误: {e}")

# ==================== 图表4：电影类型组合偏好 ====================
print("\n[4/8] 生成电影类型组合偏好图...")
try:
    df4 = pd.read_csv('output/genre_count.csv', names=['genre', 'count'])
    df4 = df4.sort_values('count', ascending=False).head(20)
    
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # 使用渐变色
    colors = plt.cm.coolwarm(np.linspace(0.2, 0.8, len(df4)))
    bars = ax.bar(range(len(df4)), df4['count'], color=colors, 
                  edgecolor='black', linewidth=1.5, alpha=0.8)
    
    # 设置x轴标签
    ax.set_xticks(range(len(df4)))
    ax.set_xticklabels(df4['genre'], rotation=45, ha='right', fontsize=10)
    
    # 添加数值标签
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}',
                ha='center', va='bottom', fontsize=9)
    
    ax.set_title('电影类型组合数量 TOP20', fontsize=16, weight='bold', pad=20)
    ax.set_xlabel('类型组合', fontsize=13)
    ax.set_ylabel('电影数量', fontsize=13)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    plt.savefig('visualizations/4_类型组合偏好.png', dpi=300, bbox_inches='tight')
    print("✓ 已保存: visualizations/4_类型组合偏好.png")
    plt.close()
except Exception as e:
    print(f"✗ 错误: {e}")

# ==================== 图表5：电影类型平均评分 ====================
print("\n[5/8] 生成电影类型平均评分图...")
try:
    df5 = pd.read_csv('output/genre_avg_rating.csv', names=['genre', 'avg_rating', 'count'])
    df5 = df5.sort_values('avg_rating', ascending=False).head(15)

    fig, ax = plt.subplots(figsize=(12, 8))

    # 绘制散点图（气泡大小代表电影数量）
    scatter = ax.scatter(df5['avg_rating'], range(len(df5)),
                        s=df5['count']/5,  # 调整气泡大小
                        c=df5['avg_rating'], cmap='RdYlGn',
                        alpha=0.6, edgecolors='black', linewidth=1.5)

    # 设置y轴标签
    ax.set_yticks(range(len(df5)))
    ax.set_yticklabels(df5['genre'], fontsize=11)

    # 添加颜色条
    cbar = plt.colorbar(scatter, ax=ax)
    cbar.set_label('平均评分', fontsize=12)

    # 添加数值标签
    for idx, row in df5.iterrows():
        y_pos = df5.index.get_loc(idx)
        ax.text(row['avg_rating'] + 0.05, y_pos,
                f"{row['avg_rating']:.2f}分 ({int(row['count'])}部)",
                va='center', fontsize=9)

    ax.set_title('电影类型平均评分 TOP15\n（气泡大小代表电影数量）',
                 fontsize=16, weight='bold', pad=20)
    ax.set_xlabel('平均评分', fontsize=13)
    ax.set_ylabel('电影类型', fontsize=13)
    ax.set_xlim(7.5, 9.5)
    ax.grid(axis='x', alpha=0.3, linestyle='--')
    ax.invert_yaxis()

    plt.tight_layout()
    plt.savefig('visualizations/5_类型平均评分.png', dpi=300, bbox_inches='tight')
    print("✓ 已保存: visualizations/5_类型平均评分.png")
    plt.close()
except Exception as e:
    print(f"✗ 错误: {e}")

# ==================== 图表6：收藏量TOP20 ====================
print("\n[6/8] 生成收藏量TOP20图...")
try:
    df6 = pd.read_csv('output/top_favorites.csv', names=['name', 'artist', 'favorites'])
    df6 = df6.head(20)

    fig, ax = plt.subplots(figsize=(14, 10))

    # 绘制水平柱状图
    colors = sns.color_palette("rocket", len(df6))
    bars = ax.barh(range(len(df6)), df6['favorites'], color=colors,
                   edgecolor='black', linewidth=1.2, alpha=0.8)

    # 设置y轴标签（电影名+演员）
    labels = [f"{row['name']}\n({row['artist']})" for idx, row in df6.iterrows()]
    ax.set_yticks(range(len(df6)))
    ax.set_yticklabels(labels, fontsize=9)

    # 添加数值标签
    for i, bar in enumerate(bars):
        width = bar.get_width()
        ax.text(width + 10000, bar.get_y() + bar.get_height()/2,
                f'{int(width):,}',
                ha='left', va='center', fontsize=9, weight='bold')

    ax.set_title('收藏量最高的电影/音乐 TOP20', fontsize=16, weight='bold', pad=20)
    ax.set_xlabel('收藏量（评分人数）', fontsize=13)
    ax.invert_yaxis()
    ax.grid(axis='x', alpha=0.3, linestyle='--')

    plt.tight_layout()
    plt.savefig('visualizations/6_收藏量TOP20.png', dpi=300, bbox_inches='tight')
    print("✓ 已保存: visualizations/6_收藏量TOP20.png")
    plt.close()
except Exception as e:
    print(f"✗ 错误: {e}")

# ==================== 图表7：年度平均播放量趋势 ====================
print("\n[7/8] 生成年度平均播放量趋势图...")
try:
    df7 = pd.read_csv('output/year_avg_play.csv', names=['year', 'avg_play'])
    df7 = df7.sort_values('year')

    fig, ax = plt.subplots(figsize=(14, 6))

    # 绘制面积图
    ax.fill_between(df7['year'], df7['avg_play'], alpha=0.3, color='#3498db')
    ax.plot(df7['year'], df7['avg_play'], linewidth=2.5, color='#2c3e50',
            marker='o', markersize=5, markerfacecolor='#e74c3c',
            markeredgewidth=0, alpha=0.8)

    # 标注最高点
    max_idx = df7['avg_play'].idxmax()
    max_year = df7.loc[max_idx, 'year']
    max_play = df7.loc[max_idx, 'avg_play']
    ax.annotate(f'最高: {max_year}年\n{max_play:.0f}人',
                xy=(max_year, max_play),
                xytext=(max_year+3, max_play+5000),
                arrowprops=dict(arrowstyle='->', color='red', lw=2),
                fontsize=11, color='red', weight='bold',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7))

    ax.set_title('年度平均评分人数趋势', fontsize=16, weight='bold', pad=20)
    ax.set_xlabel('年份', fontsize=13)
    ax.set_ylabel('平均评分人数', fontsize=13)
    ax.grid(True, alpha=0.3, linestyle='--')

    plt.tight_layout()
    plt.savefig('visualizations/7_年度平均播放量.png', dpi=300, bbox_inches='tight')
    print("✓ 已保存: visualizations/7_年度平均播放量.png")
    plt.close()
except Exception as e:
    print(f"✗ 错误: {e}")

# ==================== 图表8：播放量-评分关联分析 ====================
print("\n[8/8] 生成播放量-评分关联分析图...")
try:
    df8 = pd.read_csv('output/play_rating_correlation.csv',
                     names=['play_range', 'avg_rating', 'count'])

    # 定义区间顺序
    range_order = ['0-100', '100-1K', '1K-10K', '10K-100K', '100K-500K', '>500K']
    df8['play_range'] = pd.Categorical(df8['play_range'], categories=range_order, ordered=True)
    df8 = df8.sort_values('play_range')

    fig, ax1 = plt.subplots(figsize=(12, 6))

    # 左轴：平均评分（折线图）
    color1 = 'tab:red'
    ax1.set_xlabel('评分人数区间', fontsize=13)
    ax1.set_ylabel('平均评分', fontsize=13, color=color1)
    line = ax1.plot(df8['play_range'], df8['avg_rating'], color=color1,
                    linewidth=3, marker='o', markersize=10,
                    markerfacecolor='#e74c3c', markeredgewidth=2,
                    markeredgecolor='white', label='平均评分')
    ax1.tick_params(axis='y', labelcolor=color1)
    ax1.set_ylim(6, 9)

    # 在折线上添加数值标签
    for idx, row in df8.iterrows():
        x_pos = df8.index.get_loc(idx)
        ax1.text(x_pos, row['avg_rating'] + 0.1,
                f"{row['avg_rating']:.2f}",
                ha='center', fontsize=10, weight='bold', color=color1)

    # 右轴：电影数量（柱状图）
    ax2 = ax1.twinx()
    color2 = 'tab:blue'
    ax2.set_ylabel('电影数量', fontsize=13, color=color2)
    bars = ax2.bar(range(len(df8)), df8['count'], alpha=0.3,
                   color=color2, label='电影数量', edgecolor='black', linewidth=1)
    ax2.tick_params(axis='y', labelcolor=color2)

    # 在柱状图上添加数值标签
    for i, bar in enumerate(bars):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height):,}',
                ha='center', va='bottom', fontsize=9, weight='bold', color=color2)

    # 设置x轴
    ax1.set_xticks(range(len(df8)))
    ax1.set_xticklabels(df8['play_range'], rotation=30, ha='right')

    # 标题
    ax1.set_title('评分人数与平均评分的关联分析\n（展示马太效应）',
                  fontsize=16, weight='bold', pad=20)

    # 图例
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=11)

    # 添加网格
    ax1.grid(True, alpha=0.3, linestyle='--', axis='y')

    plt.tight_layout()
    plt.savefig('visualizations/8_播放量评分关联.png', dpi=300, bbox_inches='tight')
    print("✓ 已保存: visualizations/8_播放量评分关联.png")
    plt.close()
except Exception as e:
    print(f"✗ 错误: {e}")

print("\n" + "="*60)
print("✓ 所有图表生成完成！")
print("="*60)
print("\n生成的图表文件：")
print("  1. visualizations/1_年度产量趋势.png")
print("  2. visualizations/2_评分人数分布.png")
print("  3. visualizations/3_演员影响力.png")
print("  4. visualizations/4_类型组合偏好.png")
print("  5. visualizations/5_类型平均评分.png")
print("  6. visualizations/6_收藏量TOP20.png")
print("  7. visualizations/7_年度平均播放量.png")
print("  8. visualizations/8_播放量评分关联.png")
print("\n请将这些图片插入到实验报告的对应位置。")
print("="*60)

