# Implementation of data visualization for expense tracking using Matplotlib
# Users can view spending patterns over time

import matplotlib.pyplot as plt
import numpy as np

categories = ['Food', 'Transportation', 'Housing', 'Entertainment']
expenses = {
    'January': [200, 150, 300, 100],
    'February': [250, 180, 320, 120],
    'March': [280, 200, 350, 150]
}

for category in categories:
    amounts = [expenses[month][categories.index(category)] for month in expenses.keys()]
    plt.plot(list(expenses.keys()), amounts, label=category)

plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Monthly Expenses')
plt.legend()
plt.show()
