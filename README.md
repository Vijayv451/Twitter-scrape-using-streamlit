   #overview 
Streamlit is a python package which is used to build the WebGUI applications for machine learning and data science.


%%writefile streamlit.py
import streamlit as st
import pandas as pd
import snscrape.modules.twitter as sntwitter
import pymongo
from datetime import date
import base64

st.title("Twitter Scraping")
# Set start and end dates
start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")
# Creating a text box to enter the hashtag to search for,
hashtag = st.text_input("Enter hashtag to search for")

# To Check if the user entered a hashtag
if not hashtag:
    st.warning("Please enter a hashtag to search for.")
else:
# Twitter search query
    query = f"#{hashtag} since:{start_date} until:{end_date}"

# Creating a slider for selecting the number of tweets to scrape
    tweet_count = st.slider("Select number of tweets to scrape", min_value=10, max_value=1000, step=10)

# Scraping Twitter data
    scraped_tweets = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i >= tweet_count:
            break
        scraped_tweets.append({
            "date": tweet.date,
            "id": tweet.id,
            "url": tweet.url,
            "tweet_count": tweet.replyCount + tweet.retweetCount,
            "user": tweet.user.username,
            "reply_count": tweet.replyCount,
            "retweet_count": tweet.retweetCount,
            "language": tweet.lang,
            "source": tweet.sourceLabel,
            "like_count": tweet.likeCount,
            "hashtags": [hashtag for hashtag in tweet.hashtags]
        })

# To Display scraped data in a table
    if scraped_tweets:
        df = pd.DataFrame(scraped_tweets)
        st.write(df)
    else:
        st.warning("No tweets were scraped.")

# Create buttons to upload the data to MongoDB and download the data in CSV and JSON formats
    if scraped_tweets:
# Connection to MongoDB
        client = pymongo.MongoClient("mongodb+srv://vijay:9944433644@cluster0.xezi4kc.mongodb.net/?retryWrites=true&w=majority")
        db = client.scrap
        scrape = db.tweets
def main():
    if st.button("Upload data to MongoDB"):
# To Insert the scraped data into MongoDB
        scrape.insert_one ({
            'scrapped word': hashtag,
            'scrapped date': pd.Timestamp.now().strftime('%y-%m-%d'),
            'scrapped data': scraped_tweets
})
        st.success("Data uploaded to MongoDB.")   
        st.markdown("""---""")
        
    if st.button("Download data as CSV"):
# To Download the scraped data as a CSV file
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="{hashtag}_tweets.csv">Download CSV</a>'
        st.markdown(href, unsafe_allow_html=True)
        
    if st.button("Download data as JSON"):
# To Download the scraped data as a JSON file
        json = df.to_json(orient="records")
        b64 = base64.b64encode(json.encode()).decode()
        href = f'<a href="data:file/json;base64,{b64}" download="{hashtag}_tweets.json">Download JSON</a>'
        st.markdown(href, unsafe_allow_html=True)
        
 # It Allows You to Execute Code When the File Runs as a Script         
if __name__ == "__main__":
    main()
  
 #execution Result,
    Result of After running the command in cmd prompt, Local host new tab will appear,
 ![Screenshot (1)](https://user-images.githubusercontent.com/125632137/221567935-cfb94c29-f2f5-44cd-8741-4f3eabf0e777.png)
 ![Screenshot (2)](https://user-images.githubusercontent.com/125632137/221570829-fadaed05-b3c4-4010-a822-cc027dcf081d.png)
    Result of After entered the queru
 ![Screenshot (3)](https://user-images.githubusercontent.com/125632137/221571905-5acacf37-4647-4f22-a66d-602d4fa50266.png)
     Displayed query uploaded in mongoDB
 ![Screenshot (4)](https://user-images.githubusercontent.com/125632137/221574142-14253be3-4730-41fc-82c1-fcbb00dc79f1.png)
 ![Screenshot (7)](https://user-images.githubusercontent.com/125632137/221574279-a807f477-15d9-485a-8b68-d06347e9df6c.png)
     Result of downloaded file on CSV and JSON
 ![Screenshot (6)](https://user-images.githubusercontent.com/125632137/221574914-7f949b9a-46e6-4e33-8a19-ff1da8acf458.png)
 ![Screenshot (5)](https://user-images.githubusercontent.com/125632137/221575000-e3742c09-b804-451c-b504-203ed7d66dfd.png)

 

  
  

    
 
    
