#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from selenium import webdriver 
import random
import time
import datetime
import csv


# In[2]:


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome(chrome_options=chrome_options)

# driver = webdriver.Chrome()


# In[3]:


starting_url = "https://item.jd.com/1384071.html"
driver.get(starting_url)


# In[4]:


time.sleep(2)
xpath_comment_section = "/html[@class='root61 js no-touch svg inlinesvg svgclippaths no-ie8compat js no-touch svg inlinesvg svgclippaths no-ie8compat']/body[@class='clothing cat-1-1320 cat-2-5019 cat-3-15051 cat-4-22110 item-1384071 JD JD-2']/div[@class='w'][5]/div[@class='detail']/div[@id='detail']/div[@class='tab-main large']/ul/li[5]"
comment_section = driver.find_elements_by_xpath(xpath_comment_section)
comment_section[0].click()


# In[5]:


output_file = 'JD_evian_comments_data2.csv'
columns = ['user_name', 'member', 'rating', 'comment', 'type', 'likes_num', 'comments_num' 'post_time', 'collect_time']
with open(output_file, 'w', encoding='utf-8') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(columns)
    


# In[ ]:


posts_num = 10000
pages_num = posts_num//10

total_count = 0
for i in range(pages_num):
    for i in range(10):
        xpath_user_name = "/html[@class='root61 js no-touch svg inlinesvg svgclippaths no-ie8compat js no-touch svg inlinesvg svgclippaths no-ie8compat']/body[@class='clothing cat-1-1320 cat-2-5019 cat-3-15051 cat-4-22110 item-1384071 JD JD-2']/div[@class='w'][5]/div[@class='detail']/div[@id='comment']/div[@class='mc']/div[@class='J-comments-list comments-list ETab']/div[@class='tab-con']/div[@id='comment-0']/div[@class='comment-item'][%d]/div[@class='user-column']/div[@class='user-info']"%(i+1)
        user_name = driver.find_elements_by_xpath(xpath_user_name)
        try:
            user_name = user_name[0].text
        except:
            user_name = float('nan')

        xpath_member = "/html[@class='root61 js no-touch svg inlinesvg svgclippaths no-ie8compat js no-touch svg inlinesvg svgclippaths no-ie8compat']/body[@class='clothing cat-1-1320 cat-2-5019 cat-3-15051 cat-4-22110 item-1384071 JD JD-2']/div[@class='w'][5]/div[@class='detail']/div[@id='comment']/div[@class='mc']/div[@class='J-comments-list comments-list ETab']/div[@class='tab-con']/div[@id='comment-0']/div[@class='comment-item'][%d]/div[@class='user-column']/div[@class='user-level']/a[@class='comment-plus-icon']"%(i+1)
        member = driver.find_elements_by_xpath(xpath_member)
        try:
            member = member[0].text
        except:
            member = '非会员'

        rating = -1
        for k in range(5):
            xpath_star = "/html[@class='root61 js no-touch svg inlinesvg svgclippaths no-ie8compat js no-touch svg inlinesvg svgclippaths no-ie8compat']/body[@class='clothing cat-1-1320 cat-2-5019 cat-3-15051 cat-4-22110 item-1384071 JD JD-2']/div[@class='w'][5]/div[@class='detail']/div[@id='comment']/div[@class='mc']/div[@class='J-comments-list comments-list ETab']/div[@class='tab-con']/div[@id='comment-0']/div[@class='comment-item'][%d]/div[@class='comment-column J-comment-column']/div[@class='comment-star star%d']"%(i+1, k+1)
            try:
                star = driver.find_elements_by_xpath(xpath_star)[0]
                rating = k+1
                break
            except:
                pass

        xpath_comment = "/html[@class='root61 js no-touch svg inlinesvg svgclippaths no-ie8compat js no-touch svg inlinesvg svgclippaths no-ie8compat']/body[@class='clothing cat-1-1320 cat-2-5019 cat-3-15051 cat-4-22110 item-1384071 JD JD-2']/div[@class='w'][5]/div[@class='detail']/div[@id='comment']/div[@class='mc']/div[@class='J-comments-list comments-list ETab']/div[@class='tab-con']/div[@id='comment-0']/div[@class='comment-item'][%d]/div[@class='comment-column J-comment-column']/p[@class='comment-con']"%(i+1)
        comment = driver.find_elements_by_xpath(xpath_comment)
        try:
            comment = comment[0].text
        except:
            comment = float('nan')

        xpath_type = "/html[@class='root61 js no-touch svg inlinesvg svgclippaths no-ie8compat js no-touch svg inlinesvg svgclippaths no-ie8compat']/body[@class='clothing cat-1-1320 cat-2-5019 cat-3-15051 cat-4-22110 item-1384071 JD JD-2']/div[@class='w'][5]/div[@class='detail']/div[@id='comment']/div[@class='mc']/div[@class='J-comments-list comments-list ETab']/div[@class='tab-con']/div[@id='comment-0']/div[@class='comment-item'][%d]/div[@class='comment-column J-comment-column']/div[@class='comment-message']/div[@class='order-info']/span[1]"%(i+1)
        type_item = driver.find_elements_by_xpath(xpath_type)
        try:
            type_item = type_item[0].text
        except:
            type_item = float('nan')

        xpath_likes = "/html[@class='root61 js no-touch svg inlinesvg svgclippaths no-ie8compat js no-touch svg inlinesvg svgclippaths no-ie8compat']/body[@class='clothing cat-1-1320 cat-2-5019 cat-3-15051 cat-4-22110 item-1384071 JD JD-2']/div[@class='w'][5]/div[@class='detail']/div[@id='comment']/div[@class='mc']/div[@class='J-comments-list comments-list ETab']/div[@class='tab-con']/div[@id='comment-0']/div[@class='comment-item'][%d]/div[@class='comment-column J-comment-column']/div[@class='comment-message']/div[@class='comment-op']/a[@class='J-nice']"%(i+1)
        likes = driver.find_elements_by_xpath(xpath_likes)
        try:
            likes = likes[0].text
        except:
            likes = float('nan')

        xpath_comments = "/html[@class='root61 js no-touch svg inlinesvg svgclippaths no-ie8compat js no-touch svg inlinesvg svgclippaths no-ie8compat']/body[@class='clothing cat-1-1320 cat-2-5019 cat-3-15051 cat-4-22110 item-1384071 JD JD-2']/div[@class='w'][5]/div[@class='detail']/div[@id='comment']/div[@class='mc']/div[@class='J-comments-list comments-list ETab']/div[@class='tab-con']/div[@id='comment-0']/div[@class='comment-item'][%d]/div[@class='comment-column J-comment-column']/div[@class='comment-message']/div[@class='comment-op']/a[3]"%(i+1)
        comments = driver.find_elements_by_xpath(xpath_comments)
        try:
            comments = comments[0].text
        except:
            comments = float('nan')

        xpath_time = "/html[@class='root61 js no-touch svg inlinesvg svgclippaths no-ie8compat js no-touch svg inlinesvg svgclippaths no-ie8compat']/body[@class='clothing cat-1-1320 cat-2-5019 cat-3-15051 cat-4-22110 item-1384071 JD JD-2']/div[@class='w'][5]/div[@class='detail']/div[@id='comment']/div[@class='mc']/div[@class='J-comments-list comments-list ETab']/div[@class='tab-con']/div[@id='comment-0']/div[@class='comment-item'][%d]/div[@class='comment-column J-comment-column']/div[@class='comment-message']/div[@class='order-info']/span[4]"%(i+1)
        post_time = driver.find_elements_by_xpath(xpath_time)
        try:
            post_time = post_time[0].text
        except:
            post_time = float('nan')

        collect_time = datetime.datetime.now()

        data = [user_name, member, rating, comment, type_item, likes, comments, post_time, collect_time]
        with open(output_file, 'a', encoding='utf-8') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(data)
            total_count += 1
        if total_count%100 == 0:
            print(total_count)
        
    sucess = False
    try_time = 0
    while sucess==False and try_time<=10:
        try:
            xpath_next = "/html[@class='root61 js no-touch svg inlinesvg svgclippaths no-ie8compat js no-touch svg inlinesvg svgclippaths no-ie8compat']/body[@class='clothing cat-1-1320 cat-2-5019 cat-3-15051 cat-4-22110 item-1384071 JD JD-2']/div[@class='w'][5]/div[@class='detail']/div[@id='comment']/div[@class='mc']/div[@class='J-comments-list comments-list ETab']/div[@class='tab-con']/div[@id='comment-0']/div[@class='com-table-footer']/div[@class='ui-page-wrap clearfix']/div[@class='ui-page']/a[@class='ui-pager-next']"
            next_page = driver.find_elements_by_xpath(xpath_next)
            next_page[0].click()
            sucess = True
            time.sleep(0.8+random.random()/2)
        except:
            try_time += 1
            time.sleep(1+random.random())
print('All done!')


# In[ ]:




