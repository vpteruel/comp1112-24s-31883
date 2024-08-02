import requests
import time

def fetch_url(url):
    response = requests.get(url)
    return response.text

start_time = time.time()

content1 = fetch_url('https://www.geeksforgeeks.org/')
content2 = fetch_url('https://news.ycombinator.com/')

print("Elapsed time:", time.time() - start_time)
