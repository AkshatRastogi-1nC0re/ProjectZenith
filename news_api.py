
from newsapi import NewsApiClient

def get_news(topic):
    my_api_key = "64f5513915fa4de9bfc78adcfaa60495"

    news_api = NewsApiClient(api_key=my_api_key)

    data = news_api.get_everything(q=topic, language='en', page_size=20)

    # print(data['articles'][0]['title'])

    list_of_articles = []


    for i in range(15):
        new_dic = {'Title' : data['articles'][i]['title'], 'Content' : data['articles'][i]['description']}
        list_of_articles.append(new_dic)

    # print(list_of_articles)

    list_final = []

    for i in list_of_articles:
        listA = []
        listA.append(i['Title'])
        listA.append(i['Content'])
        list_final.append(listA)

    return list_final
#
# print(get_news("technology in covid 19"))