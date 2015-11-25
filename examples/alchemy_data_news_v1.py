import json
from watson_developer_cloud import AlchemyDataNewsV1

alchemy_data_news = AlchemyDataNewsV1(api_key='YOUR API KEY')

#News about last 30 days with max results of 40
results2 = alchemy_data_news.get_news_documents(start='now-1d', end='now', max_results='40')
print(json.dumps(results2, indent=2))

#News about last 30 days with max results of 10
results3 = alchemy_data_news.get_news_documents(start='now-7d', end='now', max_results='10')
print(json.dumps(results3, indent=2))

#News about last 30 days with max results of 20
results4 = alchemy_data_news.get_news_documents(start='now-30d', end='now', max_results='20')
print(json.dumps(results4, indent=2))

#News about last 30 days with max results of 999
results5 = alchemy_data_news.get_news_documents(start='now-2d', end='now', max_results='999')
print(json.dumps(results5, indent=2))

#Get count of articles over the past 30 days
results6 = alchemy_data_news.get_news_documents(start='now-30d', end='now')
print(json.dumps(results6, indent=2))

#Get count of articles over the past 12 hours
results7 = alchemy_data_news.get_news_documents(start='now-12h', end='now')
print(json.dumps(results7, indent=2))

#Get a time series count of articles over the past 7 days divided into 24 hour buckets
results8 = alchemy_data_news.get_news_documents(start='now-7d', end='now', time_slice='24h')
print(json.dumps(results8, indent=2))
