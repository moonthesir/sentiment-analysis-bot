# 🤖 AI Financial Sentiment Analyzer

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![NLP](https://img.shields.io/badge/NLP-VADER-purple)
![Status](https://img.shields.io/badge/Status-Educational-orange)

## 📌 Overview
This project applies **Natural Language Processing (NLP)** to financial markets. It automates the extraction of news headlines from Finviz and quantifies the "market mood" using **VADER (Valence Aware Dictionary and sEntiment Reasoner)**.

Unlike traditional technical analysis (which looks at price), this tool analyzes **Market Sentiment** (human psychology) to gauge whether news coverage is Bullish, Bearish, or Neutral.

## 🧠 How It Works
1.  **Web Scraping (`BeautifulSoup`)**: The bot mimics a browser header (`User-Agent`) to bypass firewalls and scrape the latest news table for a given ticker (e.g., NVDA).
2.  **Data Parsing**: HTML tags are cleaned to extract timestamps and headlines.
3.  **Sentiment Scoring (`VADER`)**: Each headline is passed through a lexicon-based sentiment engine that assigns a compound score:
    * **> 0.05**: Positive (Bullish) 🟢
    * **< -0.05**: Negative (Bearish) 🔴
    * **-0.05 to 0.05**: Neutral ⚪
4.  **Visualization**: A time-series analysis of sentiment trends is plotted using Matplotlib.

## 🛠️ Tech Stack
-   **Python**: Core logic
-   **BeautifulSoup4**: HTML parsing and web scraping
-   **VADER Sentiment**: Lexicon and rule-based sentiment analysis
-   **Pandas**: Dataframe management
-   **Matplotlib**: Sentiment visualization

## 🚀 How to Run
1.  Clone the repo:
    ```bash
    git clone [https://github.com/moonthesir/sentiment-analysis-bot.git](https://github.com/moonthesir/sentiment-analysis-bot.git)
    ```
2.  Install dependencies:
    ```bash
    pip install pandas matplotlib beautifulsoup4 vaderSentiment
    ```
3.  Run the bot:
    ```bash
    python3 sentiment_bot.py
    ```

## 📊 Sample Output
*Sentiment analysis of NVIDIA (NVDA) headlines:*
*(Upload your purple bar chart screenshot here!)*
