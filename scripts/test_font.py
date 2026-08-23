"""
测试中文字体显示
"""
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 查找中文字体
print("正在查找系统中的中文字体...")
chinese_fonts = []
for font in fm.fontManager.ttflist:
    if any(keyword in font.name for keyword in ['YaHei', 'Hei', 'Song', 'Kai', 'Ming']):
        chinese_fonts.append(font.name)
        print(f"  - {font.name}")

if chinese_fonts:
    print(f"\n找到 {len(chinese_fonts)} 个中文字体")
    selected_font = chinese_fonts[0]
    print(f"使用字体: {selected_font}")
else:
    print("未找到中文字体")
    selected_font = 'sans-serif'

# 设置字体
plt.rcParams['font.sans-serif'] = [selected_font, 'Microsoft YaHei', 'SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 创建测试图表
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot([1, 2, 3, 4], [1, 4, 2, 3], marker='o', linewidth=2, markersize=8)
ax.set_title('中文字体测试 - 豆瓣电影数据分析', fontsize=16, fontweight='bold')
ax.set_xlabel('年份', fontsize=12)
ax.set_ylabel('电影数量', fontsize=12)
ax.grid(True, alpha=0.3)

# 添加中文标注
ax.text(2, 3.5, '这是中文标注测试', fontsize=12, 
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.savefig('visualizations/test_chinese_font.png', dpi=300, bbox_inches='tight')
print(f"\n测试图片已保存: visualizations/test_chinese_font.png")
print("请打开图片检查中文是否正常显示")
plt.close()

