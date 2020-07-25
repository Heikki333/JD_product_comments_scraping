#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sqlalchemy import create_engine
import pandas as pd
from collections import Counter

# 连接数据库

db_info = {'user':'admin_jh',
    'password':'asjd2has34bd',
    'host':'database-jd-comments-jh.cq0jwbbp8t8f.ap-northeast-1.rds.amazonaws.com',
    'database':'database-JD-comments-jh'
}

engine = create_engine('mysql+pymysql://%(user)s:%(password)s@%(host)s/%(database)s?charset=utf8' % db_info,encoding='utf-8')


# In[ ]:


# 数据上传
df_comments = pd.read_csv('JD_evian_comments_data2.csv')
df_comments.to_sql('JD_comments_table', engine, index=False, if_exists='append')


# In[ ]:


# 数据直接全部下载
actor_asso_already = pd.read_sql_table("JD_comments_table", engine)
actor_asso_already.to_csv('data_all.csv', index=False)


# In[ ]:


# 数据使用关键词下载
with engine.connect() as conn:
    sql = "select * from actor where comment like '%赞%'"
    result = conn.execute(sql)
df_selected = result.fetchall()
df_selected.to_csv('data_selected.csv', index=False)


# In[ ]:
