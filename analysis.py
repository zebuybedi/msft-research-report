# analysis.py

import pandas as pd
import matplotlib.pyplot as plt

# Sample data for analysis
financial_data = {
    'Quarter': ['Q1', 'Q2', 'Q3', 'Q4'],
    'Revenue': [40.0, 45.0, 50.0, 55.0]
}

def plot_revenue(data):
    df = pd.DataFrame(data)
    plt.plot(df['Quarter'], df['Revenue'], marker='o')
    plt.title('Microsoft Revenue by Quarter')
    plt.xlabel('Quarter')
    plt.ylabel('Revenue in Billion $')
    plt.grid(True)
    plt.show()

plot_revenue(financial_data)
