Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('C://Users//tanis//Downloads//Video_Game_Sales_Dashboard.csv')
df['critic_score'] = pd.to_numeric(df['critic_score'], errors='coerce')
df['year'] = pd.to_numeric(df['year'], errors='coerce')
df = df.dropna(subset=['year'])
df['year'] = df['year'].astype(int)

# Objective 1: Top 10 Best-Selling Games
plt.figure(figsize=(12, 8))
top_games = df.groupby('title')['total_sales'].sum().nlargest(10).sort_values()
top_games.plot(kind='barh', color='skyblue')
plt.title('Top 10 Best-Selling Video Games', fontsize=16)
plt.xlabel('Total Sales (in millions)', fontsize=12)
plt.ylabel('Game Title', fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('top_10_games.png')
plt.show()

# Objective 2: Sales Distribution by Region
region_sales = df[['na_sales', 'jp_sales', 'pal_sales', 'other_sales']].sum()
plt.figure(figsize=(10, 10))
plt.pie(region_sales, labels=region_sales.index, autopct='%1.1f%%', 
        colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'], startangle=90)
plt.title('Global Sales Distribution by Region', fontsize=16)
plt.tight_layout()
plt.savefig('sales_by_region.png')
plt.show()

# Objective 3: Genre Popularity Over Time
genre_yearly = df.groupby(['year', 'genre'])['total_sales'].sum().unstack()
plt.figure(figsize=(14, 8))
for genre in genre_yearly.columns:
    plt.plot(genre_yearly.index, genre_yearly[genre], label=genre, linewidth=2)
plt.title('Genre Popularity Over Time', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Total Sales (in millions)', fontsize=12)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('genre_over_time.png')
plt.show()

# Objective 4: Critic Score vs Sales
plt.figure(figsize=(12, 8))
sns.scatterplot(data=df, x='critic_score', y='total_sales', hue='genre', 
                palette='viridis', alpha=0.7, s=100)
plt.title('Critic Score vs Total Sales', fontsize=16)
plt.xlabel('Critic Score (out of 10)', fontsize=12)
plt.ylabel('Total Sales (in millions)', fontsize=12)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('score_vs_sales.png')
plt.show()

# Objective 5: Console Sales Comparison
... console_sales = df.groupby('console')['total_sales'].sum().nlargest(10).sort_values()
... plt.figure(figsize=(12, 8))
... console_sales.plot(kind='barh', color='lightgreen')
... plt.title('Top 10 Consoles by Total Sales', fontsize=16)
... plt.xlabel('Total Sales (in millions)', fontsize=12)
... plt.ylabel('Console', fontsize=12)
... plt.grid(axis='x', linestyle='--', alpha=0.7)
... plt.tight_layout()
... plt.savefig('console_sales.png')
... plt.show()
... 
... # Objective 6: Yearly Sales Trend
... yearly_sales = df.groupby('year')['total_sales'].sum()
... plt.figure(figsize=(14, 8))
... yearly_sales.plot(kind='area', color='purple', alpha=0.5)
... plt.title('Yearly Video Game Sales Trend', fontsize=16)
... plt.xlabel('Year', fontsize=12)
... plt.ylabel('Total Sales (in millions)', fontsize=12)
... plt.grid(True, linestyle='--', alpha=0.7)
... plt.tight_layout()
... plt.savefig('yearly_trend.png')
... plt.show()
... 
... # Objective 7: Top Developers by Sales
... top_devs = df.groupby('developer')['total_sales'].sum().nlargest(10).sort_values()
... plt.figure(figsize=(12, 8))
... top_devs.plot(kind='barh', color='orange')
... plt.title('Top 10 Developers by Total Sales', fontsize=16)
... plt.xlabel('Total Sales (in millions)', fontsize=12)
... plt.ylabel('Developer', fontsize=12)
... plt.grid(axis='x', linestyle='--', alpha=0.7)
... plt.tight_layout()
... plt.savefig('top_developers.png')
... plt.show()
... 
... # Objective 8: Genre Sales Distribution
... genre_sales = df.groupby('genre')['total_sales'].sum().sort_values()
... plt.figure(figsize=(10, 10))
... plt.pie(genre_sales, labels=genre_sales.index, autopct='%1.1f%%',
...         wedgeprops=dict(width=0.4), startangle=90)
... plt.title('Sales Distribution by Genre', fontsize=16)
... plt.tight_layout()
... plt.savefig('genre_donut.png')
... plt.show()
... 
... # Objective 9: Sales Correlation Matrix
... corr_matrix = df[['na_sales', 'jp_sales', 'pal_sales', 'other_sales', 'total_sales']].corr()
... plt.figure(figsize=(10, 8))
... sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
... plt.title('Sales Region Correlation Matrix', fontsize=16)
... plt.tight_layout()
... plt.savefig('correlation_matrix.png')
