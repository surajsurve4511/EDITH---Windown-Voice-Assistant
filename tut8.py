from GoogleNews import GoogleNews 

def news():
    news =GooglNews(period='1d')
    news.search("India")
    result = news.result()
    #print(result)
    data = pd.DataFrame.from_dict(result)
    data = data.drop(column=["img"])
    print(data.head())
    for i in result:
        print(i["title"])
news()







