#!/usr/bin/env python
# coding: utf-8

# #### Задание 1 
# #### Импортируйте библиотеку Pandas и дайте ей псевдоним pd. Создайте датафрейм authors со столбцами author_id и author_name, в которых соответственно содержатся данные: [1, 2, 3] и ['Тургенев', 'Чехов', 'Островский'].
# #### Затем создайте датафрейм book cо столбцами author_id, book_title и price, в которых соответственно содержатся данные: 
# [1, 1, 1, 2, 2, 3, 3], 
# ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
# [450, 300, 350, 500, 450, 370, 290].
# 

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


autors = pd.DataFrame({'autor_id':[1, 2, 3], 'autor_name':['Тургенев', 'Чехов', 'Островский']}, columns=['autor_id', 'autor_name'])


# In[3]:


autors


# In[4]:


book = pd.DataFrame({'autor_id':[1, 1, 1, 2, 2, 3, 3], 'book_title':['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'], 'price':[450, 300, 350, 500, 450, 370, 290]}, columns=['autor_id', 'book_title', 'price'])


# In[6]:


book


# #### Задание 2
# #### Получите датафрейм authors_price, соединив датафреймы authors и books по полю author_id.
# 

# In[7]:


autors_price = pd.merge(autors, book, on = 'autor_id', how = 'inner')


# In[8]:


autors_price


# #### Задание 3
# #### Создайте датафрейм top5, в котором содержатся строки из authors_price с пятью самыми дорогими книгами.
# 

# In[10]:


top5 = autors_price.nlargest(5, 'price')


# In[11]:


top5


# #### Задание 4
# #### Создайте датафрейм authors_stat на основе информации из authors_price. В датафрейме authors_stat должны быть четыре столбца:
# author_name, min_price, max_price и mean_price,
# в которых должны содержаться соответственно имя автора,минимальная, максимальная и средняя цена на книги этого автора.
# 

# In[86]:


autors_stat_1 = autors_price.groupby('autor_name').agg({'price':'max'})


# In[87]:


autors_stat_1


# In[88]:


autors_stat_1 = autors_stat_1.reset_index()
autors_stat_1 = autors_stat_1.rename(columns={'price':'max_price'})


# In[89]:


autors_stat_1


# In[90]:


autors_stat_2 = autors_price.groupby('autor_name').agg({'price':'min'})


# In[91]:


autors_stat_2


# In[92]:


autors_stat_2 = autors_stat_2.reset_index()
autors_stat_2 = autors_stat_2.rename(columns={'price':'min_price'})


# In[93]:


autors_stat_2


# In[94]:


autors_stat_3 = autors_price.groupby('autor_name').agg({'price':'mean'})


# In[95]:


autors_stat_3


# In[96]:


autors_stat_3 = autors_stat_3.reset_index()
autors_stat_3 = autors_stat_3.rename(columns={'price':'mean_price'})


# In[97]:


autors_stat_3


# In[101]:


autors_stat = pd.concat([autors_stat_1, autors_stat_2, autors_stat_3], axis = 0, ignore_index=True)


# In[102]:


autors_stat


# In[ ]:




