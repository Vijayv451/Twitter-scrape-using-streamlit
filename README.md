   # overview 
Streamlit is a python package which is used to build the WebGUI applications for machine learning and data science.

  # Twitter Hashtag Scraper
This is a Python program that scrapes Twitter data using the snscrape library and allows users to upload the data to MongoDB and download the data in CSV and JSON formats. It also uses the streamlit library to create a user interface for the program.

  # Installation
To install the required libraries, run the following command:

                        !pip install snscrape streamlit pymongo datetime
                        !pip3 install git+https://github.com/JustAnotherArchivist/snscrape.git

   # Usage
To use the program, run the following command:

                         streamlit run streamlit.py
                         
This will launch the user interface for the program in your web browser.

The program will prompt you to enter a start date, end date, and hashtag to search for on Twitter. You can also select the number of tweets to scrape using a slider.

Once you have entered your search criteria, click the "Scrape" button to scrape Twitter data. The program will display the scraped data in a table on the user interface.

You can then use the "Upload data to MongoDB", "Download data as CSV", and "Download data as JSON" buttons to upload the data to MongoDB or download the data in CSV or JSON formats.

   # Contributing
Contributions to this project are welcome! If you find a bug or have a feature request, please open an issue on the GitHub repository. If you would like to contribute code, please open a pull request.

 # Below code Allows You to Execute Code When the File Runs as a Script         

     if __name__ == "__main__":
             main()
  
 # Execution Result,
  # Result of After running the command in cmd prompt, Local host new tab will appear
    
 ![Screenshot (1)](https://user-images.githubusercontent.com/125632137/221567935-cfb94c29-f2f5-44cd-8741-4f3eabf0e777.png)
 
 ![Screenshot (2)](https://user-images.githubusercontent.com/125632137/221570829-fadaed05-b3c4-4010-a822-cc027dcf081d.png)
 
   # Result of After entered the query
    
 ![Screenshot (3)](https://user-images.githubusercontent.com/125632137/221571905-5acacf37-4647-4f22-a66d-602d4fa50266.png)
 
   # Displayed query uploaded in mongoDB
 ![Screenshot (4)](https://user-images.githubusercontent.com/125632137/221574142-14253be3-4730-41fc-82c1-fcbb00dc79f1.png)
 
 ![Screenshot (7)](https://user-images.githubusercontent.com/125632137/221574279-a807f477-15d9-485a-8b68-d06347e9df6c.png)
 
   # Result of downloaded file on CSV and JSON
     
 ![Screenshot (6)](https://user-images.githubusercontent.com/125632137/221574914-7f949b9a-46e6-4e33-8a19-ff1da8acf458.png)
 
 ![Screenshot (5)](https://user-images.githubusercontent.com/125632137/221575000-e3742c09-b804-451c-b504-203ed7d66dfd.png)

 

  
  

    
 
    
