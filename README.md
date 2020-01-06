# CaseCompetition_SentimentAnalysis
Sentiment Analysis for PwC case competition

Last year, I took part in PwC case competition.
This competition requires us to conduct a business plan for a PC game company to help them increase user number and prepare for going public. 
At the first beginning, we would like to do a traditional business plan for the PC game company including financial analysis, marketing strategy and so on. However, because I am the leader of my team and we all want to win, then I would like to make a difference and outstand from all other teams. In this situation, I persuade my teammates to apply data analytics into the competition coz we know data is a hot topic in recent year and if we can get some new information using data then I am sure it will attract others.
Because our goal is to attract more users, we need to know MAU and users’ comments. Based on what data we need to collect, sentiment analysis is a good method for us to analyze users’ comments and tableau is a good way to help us better know the change in user number in recent two years.
Our data collection includes 2 parts. We need to download MAU from official website and then we deployed Beautiful Soup to crawl comments from the official website.
The next step is to conduct sentiment analysis. We divide 2016 – 2017 into various time period and use TextBlob to read users’ comments and calculate sentiments respectively.
Finally, we use Tableau to present correlation between Polarity and User number change. We found they are pretty match, which means sentiment could reflect users number change. After data processing, we can move on to find reasons behind it.
Thanks to my teammates’ hard work, in the final presentation, our data analytics part left a great impression on the audience and we won the second price in the competition.
