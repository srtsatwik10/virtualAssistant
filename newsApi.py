import requests
import main
import json
from newsapi import NewsApiClient

# url = "https://newsapi.org/v2/everything?q=tesla&from=2023-05-16&sortBy=publishedAt&apiKey=4e10e7e073d74242a5b70865b608132e"

# Init
def headlines(keyword):
    newsapi = NewsApiClient(api_key='4e10e7e073d74242a5b70865b608132e')

    # /v2/top-headlines
    if(keyword=="science" or keyword=="technology"):
        top_headlines = newsapi.get_top_headlines(q=f'{keyword}',
                                                  # sources='',
                                                  category=f'{keyword}',
                                                  language='en',
                                                  )
    else:
        top_headlines = newsapi.get_top_headlines(q=f'{keyword}',
                                      # sources='',
                                      category=f'{keyword}',
                                      language='en',
                                      country='in')

        # /v2/top-headlines/sources
        sources = newsapi.get_sources()
        # print(type(top_headlines))
        # print(type(top_headlines['articles']))
    newslist = top_headlines['articles']
    for i in range(2):
        i+=1
        main.say(newslist[i]['description'])














# politics- the hindu
# sports - the hindu
# business-economics times
# international-bbc
# entertainment-screenrant
# health- the hindu









# # /v2/everything
# all_articles = newsapi.get_everything(q='bitcoin',
#                                       sources='bbc-news,the-verge',
#                                       domains='bbc.co.uk,techcrunch.com',
#                                       from_param='2017-05-01',
#                                       to='2023-06-06',
#                                       language='en',
#                                       sort_by='relevancy',
#                                       page=1)
