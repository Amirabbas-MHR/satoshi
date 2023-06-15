from requests import get
from random import sample

class Alphav_news:
    """Object to get news from Alphavantage."""
    def __init__(self):
        self.api_key = "1AJ0L3L8WFNU49ZM"
        
    def create_url(self, tickers, topics, count):
        """Create URL for Alphavantage API."""
        url = f'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={tickers}&topics={topics}&apikey={self.api_key}'
        return url
    
    def summery_view(self, text, n):
        """returns the text with the first n characters (will not cut the words) and adds ... to the end"""
        splitted_text = text.split()
        number_of_chars = 0
        for k, word in enumerate(splitted_text):
            number_of_chars += len(word) + 1
            if number_of_chars >= n:
                return ' '.join(splitted_text[:k]) + '...'
        return text

    def get_news(self, tickers='CRYPTO:BTC,FOREX:USD', topics='', count=5, summerize=True):
        """Get news from Alphavantage. 
        returns feed with keys:
        'title', 'url', 'time_published',
        'authors', 'summary', 'banner_image',
        'source', 'category_within_source',
        'source_domain', 'topics',
        'overall_sentiment_score',
        'overall_sentiment_label',
        'ticker_sentiment'
        """
        url = self.create_url(tickers='', topics='finance', count=count)
        respond = get(url)
        status = respond.status_code
        
        result = respond.json()
        feed = sample(result['feed'], k=count)
        if summerize:
            for item in feed:
                item['summary'] = self.summery_view(item['summary'], 220) #TODO maybe text length should be configurable
                item['title'] = self.summery_view(item['title'], 80)
        if status == 200: #if get request is successfull, returns the feed
            return feed
        return 0 


if __name__ == '__main__':
    news = Alphav_news()
    feed = news.get_news()