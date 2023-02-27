#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install snscrape')


# In[2]:


get_ipython().system('pip install streamlit')


# In[3]:


get_ipython().system('pip install pymongo')


# In[4]:


get_ipython().system('pip install datetime')


# In[5]:


get_ipython().system(' pip3 install git+https://github.com/JustAnotherArchivist/snscrape.git')


# In[6]:


get_ipython().system('pip install base64')


# In[8]:


get_ipython().run_cell_magic('writefile', 'streamlit.py', 'import streamlit as st\nimport pandas as pd\nimport snscrape.modules.twitter as sntwitter\nimport pymongo\nfrom datetime import date\nimport base64\n\nst.title("Twitter Scraping")\n# Set start and end dates\nstart_date = st.date_input("Start Date")\nend_date = st.date_input("End Date")\n# Creating a text box to enter the hashtag to search for,\nhashtag = st.text_input("Enter hashtag to search for")\n\n# To Check if the user entered a hashtag\nif not hashtag:\n    st.warning("Please enter a hashtag to search for.")\nelse:\n# Twitter search query\n    query = f"#{hashtag} since:{start_date} until:{end_date}"\n\n# Creating a slider for selecting the number of tweets to scrape\n    tweet_count = st.slider("Select number of tweets to scrape", min_value=10, max_value=1000, step=10)\n\n# Scraping Twitter data\n    scraped_tweets = []\n    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):\n        if i >= tweet_count:\n            break\n        scraped_tweets.append({\n            "date": tweet.date,\n            "id": tweet.id,\n            "url": tweet.url,\n            "tweet_count": tweet.replyCount + tweet.retweetCount,\n            "user": tweet.user.username,\n            "reply_count": tweet.replyCount,\n            "retweet_count": tweet.retweetCount,\n            "language": tweet.lang,\n            "source": tweet.sourceLabel,\n            "like_count": tweet.likeCount,\n            "hashtags": [hashtag for hashtag in tweet.hashtags]\n        })\n\n# To Display scraped data in a table\n    if scraped_tweets:\n        df = pd.DataFrame(scraped_tweets)\n        st.write(df)\n    else:\n        st.warning("No tweets were scraped.")\n\n# Create buttons to upload the data to MongoDB and download the data in CSV and JSON formats\n    if scraped_tweets:\n# Connection to MongoDB\n        client = pymongo.MongoClient("mongodb+srv://vijay:9944433644@cluster0.xezi4kc.mongodb.net/?retryWrites=true&w=majority")\n        db = client.scrap\n        scrape = db.tweets\ndef main():\n    if st.button("Upload data to MongoDB"):\n# To Insert the scraped data into MongoDB\n        scrape.insert_one ({\n            \'scrapped word\': hashtag,\n            \'scrapped date\': pd.Timestamp.now().strftime(\'%y-%m-%d\'),\n            \'scrapped data\': scraped_tweets\n})\n        st.success("Data uploaded to MongoDB.")   \n        st.markdown("""---""")\n        \n    if st.button("Download data as CSV"):\n# To Download the scraped data as a CSV file\n        csv = df.to_csv(index=False)\n        b64 = base64.b64encode(csv.encode()).decode()\n        href = f\'<a href="data:file/csv;base64,{b64}" download="{hashtag}_tweets.csv">Download CSV</a>\'\n        st.markdown(href, unsafe_allow_html=True)\n        \n    if st.button("Download data as JSON"):\n# To Download the scraped data as a JSON file\n        json = df.to_json(orient="records")\n        b64 = base64.b64encode(json.encode()).decode()\n        href = f\'<a href="data:file/json;base64,{b64}" download="{hashtag}_tweets.json">Download JSON</a>\'\n        st.markdown(href, unsafe_allow_html=True)\n            \nif __name__ == "__main__":\n    main()')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




