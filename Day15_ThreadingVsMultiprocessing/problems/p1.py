'''
Problem 1: Multi-threaded Web Scraper
Task: Write a function that uses threads to download the contents of multiple websites concurrently.
You’ll need to define a list of URLs, create a thread for each URL, and fetch the website 
data using the requests library. Use a function fetch_url(url) to simulate downloading content 
for each URL.

Expected Output:
Print the first 100 characters of each site’s content.
'''
from threading import Thread
import requests
def fetch_url(url):
    response = requests.get(url)
    print(f'Content from {url}: ', response.text[:100])

if __name__ == '__main__':
    threads = []

    def thread_scraper(urls):
        for url in urls:
            t = Thread(target=fetch_url, args=(url, ))
            threads.append(t)
            t.start()
        
        for t in threads:
            t.join()
    
    urls = ['https://www.python-engineer.com/', 'https://akatsuki.finance/', 'https://www.google.com/']
    thread_scraper(urls)

'''
result:
Content from https://www.python-engineer.com/:  <!doctype html><html lang=en class=no-js> <head><meta charset=utf-8><meta name=viewport content="wid
Content from https://www.google.com/:  <!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="en-CA"><head><meta cont
Content from https://akatsuki.finance/:  
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Comp
'''