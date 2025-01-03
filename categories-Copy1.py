#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

# Expense categories
categories = ['Groceries', 'Utilities', 'Rent', 'Transportation', 'Entertainment']

# Monthly expense data (example data in USD)
expenses = [500, 200, 1200, 300, 150]

# Create a Pandas Series
expense_series = pd.Series(expenses, index=categories)

print(expense_series)


# In[ ]:





# In[ ]:




