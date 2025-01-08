import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
data = pd.read_csv('Clean_Dataset.csv')

# 绘制柱状图
plt.bar(data['category'], data['value'])
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Data Visualization')

# 保存图片为 png 格式，可根据需要调整文件名和格式
plt.savefig('visualization_result.png')

# 显示图形（可选，在本地运行时可查看，但在 GitHub 上主要依赖保存的图片文件）
# plt.show()