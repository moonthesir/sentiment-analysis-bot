from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# --- 1. CONFIGURATION ---
ticker = 'NVDA'
url = f'https://finviz.com/quote.ashx?t={ticker}'

# --- 2. SCRAPE FINVIZ ---
print(f"Scraping news for {ticker}...")
req = Request(url=url, headers={'User-Agent': 'Mozilla/5.0'})
response = urlopen(req)

html = BeautifulSoup(response, features="html.parser")
# Fixed 'findAll' to 'find_all' to verify the deprecation warning
news_table = html.find(id='news-table')

# --- 3. EXTRACT HEADLINES ---
parsed_news = []
for x in news_table.find_all('tr'):
    text = x.a.get_text() 
    date_scrape = x.td.text.split()

    if len(date_scrape) == 1:
        time = date_scrape[0] # Only time given, use previous date
    else:
        date_str = date_scrape[0]
        time = date_scrape[1]
        
        # FIX: Handle "Today" case
        if date_str == 'Today':
            date_str = datetime.now().strftime("%b-%d-%y")
            
        date = date_str
    
    parsed_news.append([date, time, text])

# --- 4. APPLY NLP (VADER) ---
print("Analyzing sentiment...")
analyzer = SentimentIntensityAnalyzer()
columns = ['Date', 'Time', 'Headline']
df = pd.DataFrame(parsed_news, columns=columns)

# Calculate Sentiment
df['Sentiment'] = df['Headline'].apply(lambda x: analyzer.polarity_scores(x)['compound'])

# --- 5. VISUALIZE ---
# Convert date strings to actual Date Objects
df['Date'] = pd.to_datetime(df['Date'], errors='coerce').dt.date

# Calculate average sentiment per day
daily_sentiment = df.groupby('Date')['Sentiment'].mean()

print("\n--- RECENT HEADLINES & SCORES ---")
print(df[['Date', 'Headline', 'Sentiment']].head(5))

plt.figure(figsize=(10, 5))
# Plot simple bar chart
daily_sentiment.plot(kind='bar', color='purple')
plt.title(f'Daily Sentiment Analysis for {ticker}')
plt.ylabel('Sentiment Score (-1 to +1)')
plt.axhline(0, color='black', linewidth=0.8)
plt.tight_layout()
plt.show()
