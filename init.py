import crawler as cr

URL = [
    "https://n.news.naver.com/article/003/0010487159",
    "https://n.news.naver.com/article/022/0003554228",
    ]

for i in range(len(URL)):
    cr.crawler(URL[i], i)