
# CrowdWisdomTask Sentiment Analysis Project

## Project Overview
This project is a Python-based backend script that uses CrewAI to perform sentiment analysis on tweets from specific users on X (formerly Twitter). It evaluates the sentiment of the tweets and generates a report for each user. The assignment is designed to assess qualifications for the CrowdWisdomTrading FullStack Intern position.


## Features
- Scrapes data for specified X users (simulated in this project).
- Analyzes sentiment and generates a contextual report for each user.
- Saves results in a JSON file.
- Generates a sentiment analysis report in **PDF format**.

---

## Technical Requirements
- **Programming Language:** Python  
- **Framework/Tools Used:**
  - CrewAI
  - TextBlob (for sentiment analysis)
  - FPDF (for PDF generation)
  - Requests and BeautifulSoup4 (for data scraping/simulation)
- **Environment:** Developed using VS Code.

---

## Project Workflow
1. **Agent 1: X Data Collector**
   - Simulates scraping tweets for specific users.
   - Collects:
     - Username
     - Number of followers
     - Average tweets per day
     - Tweets (content and replies)
   - Saves the data in a structured JSON file.

2. **Agent 2: Sentiment Analyzer**
   - Analyzes the sentiment of the tweets using the TextBlob library.
   - Generates a user-specific report in PDF format, including:
     - Follower count
     - Average tweets per day
     - Sentiment analysis score.


## **Installation Instructions**
1. Clone or download this repository to your local machine.
2. Ensure Python 3.8+ is installed.  
3. Install the required dependencies by running:
   bash
   pip install -r requirements.txt
   
4. Download the TextBlob corpora:
   bash
   python -m textblob.download_corpora
   


## How to Run the Project
1. Open the project folder in VS Code.
2. Run the script in the terminal:
   bash
   python main.py
   
3. Outputs:
   - A data.json file with simulated scraped data.
   - A report.pdf file containing the sentiment analysis.


## **File Structure**
```
CrowdWisdomTask/
│
├── main.py             # Main Python script
├── requirements.txt    # List of dependencies
├── data.json           # JSON file with scraped data
├── report.pdf          # Generated sentiment analysis report
└── README.md           # Project description


## Sample Output
### Data (JSON Format):
json
[
    {
        "username": "creator1",
        "followers": 5000,
        "avg_tweets_per_day": 10,
        "tweets": [
            {
                "tweet_id": "creator1_tweet_1",
                "content": "This is a sample tweet.",
                "replies": 15
            }
        ]
    }
]


### Report (PDF Format):
- Username: creator1  
- Followers: 5000  
- Average Tweets Per Day: 10  
- Sentiment Score: 0.75  




## Future Improvements
- Real-time scraping from X using APIs (if API keys are available).
- Add error handling and logging for better debugging.
- Integrate other social media platforms like YouTube for a combined report.

