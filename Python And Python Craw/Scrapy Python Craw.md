# Scrapy Python Craw
## Coding Enviroment Building
1. Python enviroment:
<br>https://github.com/GlennOu66304/Data-Sciences/blob/master/Python%20And%20Python%20Craw/1.Python.md

2. Anaconda enviroment:
<br>https://github.com/GlennOu66304/Data-Sciences/blob/master/3.Data%20Analysis%20in%20Python%20Enviroment%20.md

3. Scrapy Installation
```
(base) ztdeMacBook-Air:~ zt$ conda install -c conda-forge scrapy
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /opt/anaconda3

  added / updated specs:
    - scrapy


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    automat-20.2.0             |             py_0          30 KB  conda-forge
    bcrypt-3.1.7               |   py37h9bfed18_1          42 KB  conda-forge
    conda-4.8.3                |   py37hc8dfbb8_1         3.0 MB  conda-forge
    constantly-15.1.0          |             py_0           9 KB  conda-forge
    cssselect-1.1.0            |             py_0          18 KB  conda-forge
    hyperlink-19.0.0           |     pyh9f0ad1d_0          35 KB  conda-forge
    incremental-17.5.0         |             py_0          14 KB  conda-forge
    parsel-1.5.2               |             py_0          14 KB  conda-forge
    pyasn1-0.4.8               |             py_0          53 KB  conda-forge
    pyasn1-modules-0.2.7       |             py_0          60 KB  conda-forge
    pydispatcher-2.0.5         |             py_1          12 KB  conda-forge
    pyhamcrest-2.0.2           |             py_0          29 KB  conda-forge
    python_abi-3.7             |          1_cp37m           4 KB  conda-forge
    queuelib-1.5.0             |     pyh9f0ad1d_0          13 KB  conda-forge
    scrapy-1.6.0               |           py37_0         323 KB
    service_identity-18.1.0    |             py_0          12 KB  conda-forge
    twisted-20.3.0             |   py37h9bfed18_0         5.0 MB  conda-forge
    w3lib-1.20.0               |             py_0          21 KB  conda-forge
    zope.interface-5.1.0       |   py37h9bfed18_0         288 KB  conda-forge
    ------------------------------------------------------------
                                           Total:         9.0 MB

The following NEW packages will be INSTALLED:

  automat            conda-forge/noarch::automat-20.2.0-py_0
  bcrypt             conda-forge/osx-64::bcrypt-3.1.7-py37h9bfed18_1
  constantly         conda-forge/noarch::constantly-15.1.0-py_0
  cssselect          conda-forge/noarch::cssselect-1.1.0-py_0
  hyperlink          conda-forge/noarch::hyperlink-19.0.0-pyh9f0ad1d_0
  incremental        conda-forge/noarch::incremental-17.5.0-py_0
  parsel             conda-forge/noarch::parsel-1.5.2-py_0
  pyasn1             conda-forge/noarch::pyasn1-0.4.8-py_0
  pyasn1-modules     conda-forge/noarch::pyasn1-modules-0.2.7-py_0
  pydispatcher       conda-forge/noarch::pydispatcher-2.0.5-py_1
  pyhamcrest         conda-forge/noarch::pyhamcrest-2.0.2-py_0
  python_abi         conda-forge/osx-64::python_abi-3.7-1_cp37m
  queuelib           conda-forge/noarch::queuelib-1.5.0-pyh9f0ad1d_0
  scrapy             pkgs/main/osx-64::scrapy-1.6.0-py37_0
  service_identity   conda-forge/noarch::service_identity-18.1.0-py_0
  twisted            conda-forge/osx-64::twisted-20.3.0-py37h9bfed18_0
  w3lib              conda-forge/noarch::w3lib-1.20.0-py_0
  zope.interface     conda-forge/osx-64::zope.interface-5.1.0-py37h9bfed18_0

The following packages will be UPDATED:

  conda                       pkgs/main::conda-4.8.3-py37_0 --> conda-forge::conda-4.8.3-py37hc8dfbb8_1


Proceed ([y]/n)? 


Downloading and Extracting Packages
pyasn1-0.4.8         | 53 KB     | ##################################### | 100% 
service_identity-18. | 12 KB     | ##################################### | 100% 
parsel-1.5.2         | 14 KB     | ##################################### | 100% 
incremental-17.5.0   | 14 KB     | ##################################### | 100% 
conda-4.8.3          | 3.0 MB    | ##################################### | 100% 
queuelib-1.5.0       | 13 KB     | ##################################### | 100% 
hyperlink-19.0.0     | 35 KB     | ##################################### | 100% 
zope.interface-5.1.0 | 288 KB    | ##################################### | 100% 
pyhamcrest-2.0.2     | 29 KB     | ##################################### | 100% 
scrapy-1.6.0         | 323 KB    | ##################################### | 100% 
pyasn1-modules-0.2.7 | 60 KB     | ##################################### | 100% 
constantly-15.1.0    | 9 KB      | ##################################### | 100% 
bcrypt-3.1.7         | 42 KB     | ##################################### | 100% 
automat-20.2.0       | 30 KB     | ##################################### | 100% 
pydispatcher-2.0.5   | 12 KB     | ##################################### | 100% 
cssselect-1.1.0      | 18 KB     | ##################################### | 100% 
w3lib-1.20.0         | 21 KB     | ##################################### | 100% 
python_abi-3.7       | 4 KB      | ##################################### | 100% 
twisted-20.3.0       | 5.0 MB    | ##################################### | 100% 
Preparing transaction: done
Verifying transaction: | WARNING conda.core.path_actions:verify(963): Unable to create environments file. Path not writable.
  environment location: /Users/zt/.conda/environments.txt

done
Executing transaction: done
(base) ztdeMacBook-Air:~ zt$ 
```
conda-forge / packages / scrapy
<br>https://anaconda.org/conda-forge/scrapy

## Real life Example to try it.
1.Creating a project:
```
(base) ztdeMacBook-Air:~ zt$ scrapy startproject tutorial
New Scrapy project 'tutorial', using template directory '/opt/anaconda3/lib/python3.7/site-packages/scrapy/templates/project', created in:
    /Users/zt/tutorial

You can start your first spider with:
    cd tutorial
    scrapy genspider example example.com
```
2.run our spider
```
(base) ztdeMacBook-Air:~ zt$ cd /Users/zt/tutorial/tutorial/spiders 
(base) ztdeMacBook-Air:spiders zt$ scrapy crawl quotes
2020-04-25 13:38:30 [scrapy.utils.log] INFO: Scrapy 1.6.0 started (bot: tutorial)
2020-04-25 13:38:30 [scrapy.utils.log] INFO: Versions: lxml 4.5.0.0, libxml2 2.9.9, cssselect 1.1.0, parsel 1.5.2, w3lib 1.20.0, Twisted 20.3.0, Python 3.7.6 (default, Jan  8 2020, 13:42:34) - [Clang 4.0.1 (tags/RELEASE_401/final)], pyOpenSSL 19.1.0 (OpenSSL 1.1.1d  10 Sep 2019), cryptography 2.8, Platform Darwin-17.0.0-x86_64-i386-64bit
2020-04-25 13:38:30 [scrapy.crawler] INFO: Overridden settings: {'BOT_NAME': 'tutorial', 'NEWSPIDER_MODULE': 'tutorial.spiders', 'ROBOTSTXT_OBEY': True, 'SPIDER_MODULES': ['tutorial.spiders']}
2020-04-25 13:38:30 [scrapy.extensions.telnet] INFO: Telnet Password: 774485f2efc44e44
2020-04-25 13:38:30 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.memusage.MemoryUsage',
 'scrapy.extensions.logstats.LogStats']
2020-04-25 13:38:30 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2020-04-25 13:38:30 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2020-04-25 13:38:30 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2020-04-25 13:38:30 [scrapy.core.engine] INFO: Spider opened
2020-04-25 13:38:30 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2020-04-25 13:38:30 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
2020-04-25 13:38:36 [scrapy.core.engine] DEBUG: Crawled (404) <GET http://quotes.toscrape.com/robots.txt> (referer: None)
2020-04-25 13:38:37 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/page/1/> (referer: None)
2020-04-25 13:38:37 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/page/2/> (referer: None)
2020-04-25 13:38:37 [quotes] DEBUG: Saved file quotes-1.html
2020-04-25 13:38:37 [quotes] DEBUG: Saved file quotes-2.html
2020-04-25 13:38:37 [scrapy.core.engine] INFO: Closing spider (finished)
2020-04-25 13:38:37 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 678,
 'downloader/request_count': 3,
 'downloader/request_method_count/GET': 3,
 'downloader/response_bytes': 6081,
 'downloader/response_count': 3,
 'downloader/response_status_count/200': 2,
 'downloader/response_status_count/404': 1,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2020, 4, 25, 5, 38, 37, 617335),
 'log_count/DEBUG': 5,
 'log_count/INFO': 9,
 'memusage/max': 51175424,
 'memusage/startup': 51175424,
 'response_received_count': 3,
 'robotstxt/request_count': 1,
 'robotstxt/response_count': 1,
 'robotstxt/response_status_count/404': 1,
 'scheduler/dequeued': 2,
 'scheduler/dequeued/memory': 2,
 'scheduler/enqueued': 2,
 'scheduler/enqueued/memory': 2,
 'start_time': datetime.datetime(2020, 4, 25, 5, 38, 30, 904122)}
```
3.Extracting data
```
(base) ztdeMacBook-Air:spiders zt$ scrapy shell 'http://quotes.toscrape.com/page/1/'
2020-04-25 13:41:28 [scrapy.utils.log] INFO: Scrapy 1.6.0 started (bot: tutorial)
2020-04-25 13:41:28 [scrapy.utils.log] INFO: Versions: lxml 4.5.0.0, libxml2 2.9.9, cssselect 1.1.0, parsel 1.5.2, w3lib 1.20.0, Twisted 20.3.0, Python 3.7.6 (default, Jan  8 2020, 13:42:34) - [Clang 4.0.1 (tags/RELEASE_401/final)], pyOpenSSL 19.1.0 (OpenSSL 1.1.1d  10 Sep 2019), cryptography 2.8, Platform Darwin-17.0.0-x86_64-i386-64bit
2020-04-25 13:41:28 [scrapy.crawler] INFO: Overridden settings: {'BOT_NAME': 'tutorial', 'DUPEFILTER_CLASS': 'scrapy.dupefilters.BaseDupeFilter', 'LOGSTATS_INTERVAL': 0, 'NEWSPIDER_MODULE': 'tutorial.spiders', 'ROBOTSTXT_OBEY': True, 'SPIDER_MODULES': ['tutorial.spiders']}
2020-04-25 13:41:28 [scrapy.extensions.telnet] INFO: Telnet Password: 8154fc4ff84d0bf9
2020-04-25 13:41:28 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.memusage.MemoryUsage']
2020-04-25 13:41:28 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2020-04-25 13:41:28 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2020-04-25 13:41:28 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2020-04-25 13:41:28 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
2020-04-25 13:41:28 [scrapy.core.engine] INFO: Spider opened
2020-04-25 13:41:36 [scrapy.core.engine] DEBUG: Crawled (404) <GET http://quotes.toscrape.com/robots.txt> (referer: None)
2020-04-25 13:41:36 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/page/1/> (referer: None)
2020-04-25 13:41:37 [asyncio] DEBUG: Using selector: KqueueSelector
[s] Available Scrapy objects:
[s]   scrapy     scrapy module (contains scrapy.Request, scrapy.Selector, etc)
[s]   crawler    <scrapy.crawler.Crawler object at 0x10ed39690>
[s]   item       {}
[s]   request    <GET http://quotes.toscrape.com/page/1/>
[s]   response   <200 http://quotes.toscrape.com/page/1/>
[s]   settings   <scrapy.settings.Settings object at 0x10ed398d0>
[s]   spider     <DefaultSpider 'default' at 0x10f09b450>
[s] Useful shortcuts:
[s]   fetch(url[, redirect=True]) Fetch URL and update local objects (by default, redirects are followed)
[s]   fetch(req)                  Fetch a scrapy.Request and update local objects 
[s]   shelp()           Shell help (print this help)
[s]   view(response)    View response in a browser
2020-04-25 13:41:38 [asyncio] DEBUG: Using selector: KqueueSelector
In [1]: response.css('title')                                                   
Out[1]: [<Selector xpath='descendant-or-self::title' data='<title>Quotes to Scrape</title>'>]

In [2]: response.css('title::text').getall()                                    
Out[2]: ['Quotes to Scrape']

In [3]: response.css('title::text').get()                                       
Out[3]: 'Quotes to Scrape'

In [4]: response.css('title::text')[0].get()                                    
Out[4]: 'Quotes to Scrape'

In [5]: response.css("div.quote")                                               
Out[5]: 
[<Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>,
 <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>,
 <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>,
 <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>,
 <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>,
 <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>,
 <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>,
 <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>,
 <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>,
 <Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>]

In [6]: quote = response.css("div.quote")[0]                                    

In [7]: text = quote.css("span.text::text").get()                               

In [8]: text                                                                    
Out[8]: '“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”'

In [9]: author = quote.css("small.author::text").get()                          

In [10]: author                                                                 
Out[10]: 'Albert Einstein'

In [11]: tags = quote.css("div.tags a.tag::text").getall()                      

In [12]: tags                                                                   
Out[12]: ['change', 'deep-thoughts', 'thinking', 'world']

In [13]: for quote in response.css("div.quote"): 
    ...:     text = quote.css("span.text::text").get() 
    ...:     author = quote.css("small.author::text").get() 
    ...:     tags = quote.css("div.tags a.tag::text").getall() 
    ...:     print(dict(text=text, author=author, tags=tags)) 
    ...:     {'text': '“The world as we have created it is a process of our thin
    ...: king. It cannot be changed without changing our thinking.”', 'author': 
    ...: 'Albert Einstein', 'tags': ['change', 'deep-thoughts', 'thinking', 'wor
    ...: ld']} 
    ...: {'text': '“It is our choices, Harry, that show what we truly are, far m
    ...: ore than our abilities.”', 'author': 'J.K. Rowling', 'tags': ['abilitie
    ...: s', 'choices']} 
    {'text': '“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”', 'author': 'Albert Einstein', 'tags': ['change', 'deep-thoughts', 'thinking', 'world']}
{'text': '“It is our choices, Harry, that show what we truly are, far more than our abilities.”', 'author': 'J.K. Rowling', 'tags': ['abilities', 'choices']}
{'text': '“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”', 'author': 'Albert Einstein', 'tags': ['inspirational', 'life', 'live', 'miracle', 'miracles']}
{'text': '“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”', 'author': 'Jane Austen', 'tags': ['aliteracy', 'books', 'classic', 'humor']}
{'text': "“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”", 'author': 'Marilyn Monroe', 'tags': ['be-yourself', 'inspirational']}
{'text': '“Try not to become a man of success. Rather become a man of value.”', 'author': 'Albert Einstein', 'tags': ['adulthood', 'success', 'value']}
{'text': '“It is better to be hated for what you are than to be loved for what you are not.”', 'author': 'André Gide', 'tags': ['life', 'love']}
{'text': "“I have not failed. I've just found 10,000 ways that won't work.”", 'author': 'Thomas A. Edison', 'tags': ['edison', 'failure', 'inspirational', 'paraphrased']}
{'text': "“A woman is like a tea bag; you never know how strong it is until it's in hot water.”", 'author': 'Eleanor Roosevelt', 'tags': ['misattributed-eleanor-roosevelt']}
{'text': '“A day without sunshine is like, you know, night.”', 'author': 'Steve Martin', 'tags': ['humor', 'obvious', 'simile']}
Out[13]: 
{'text': '“It is our choices, Harry, that show what we truly are, far more than our abilities.”',
 'author': 'J.K. Rowling',
 'tags': ['abilities', 'choices']}
```
Extracting data in our spider:
<br> insert the code sniptes into quotes_spider.py
```
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
```
Run This spider in terminal
```
(base) ztdeMacBook-Air:~ zt$ cd /Users/zt/tutorial/tutorial/spiders 
(base) ztdeMacBook-Air:spiders zt$ scrapy crawl quotes
2020-04-25 13:51:08 [scrapy.utils.log] INFO: Scrapy 1.6.0 started (bot: tutorial)
2020-04-25 13:51:08 [scrapy.utils.log] INFO: Versions: lxml 4.5.0.0, libxml2 2.9.9, cssselect 1.1.0, parsel 1.5.2, w3lib 1.20.0, Twisted 20.3.0, Python 3.7.6 (default, Jan  8 2020, 13:42:34) - [Clang 4.0.1 (tags/RELEASE_401/final)], pyOpenSSL 19.1.0 (OpenSSL 1.1.1d  10 Sep 2019), cryptography 2.8, Platform Darwin-17.0.0-x86_64-i386-64bit
2020-04-25 13:51:08 [scrapy.crawler] INFO: Overridden settings: {'BOT_NAME': 'tutorial', 'NEWSPIDER_MODULE': 'tutorial.spiders', 'ROBOTSTXT_OBEY': True, 'SPIDER_MODULES': ['tutorial.spiders']}
2020-04-25 13:51:08 [scrapy.extensions.telnet] INFO: Telnet Password: 0cd3a2005573585b
2020-04-25 13:51:08 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.memusage.MemoryUsage',
 'scrapy.extensions.logstats.LogStats']
2020-04-25 13:51:08 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2020-04-25 13:51:08 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2020-04-25 13:51:08 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2020-04-25 13:51:08 [scrapy.core.engine] INFO: Spider opened
2020-04-25 13:51:08 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2020-04-25 13:51:08 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6024
2020-04-25 13:51:09 [scrapy.core.engine] DEBUG: Crawled (404) <GET http://quotes.toscrape.com/robots.txt> (referer: None)
2020-04-25 13:51:10 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/page/1/> (referer: None)
2020-04-25 13:51:10 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/page/2/> (referer: None)
2020-04-25 13:51:11 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>
{'text': '“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”', 'author': 'Albert Einstein', 'tags': ['change', 'deep-thoughts', 'thinking', 'world']}
2020-04-25 13:51:11 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>
{'text': '“It is our choices, Harry, that show what we truly are, far more than our abilities.”', 'author': 'J.K. Rowling', 'tags': ['abilities', 'choices']}
2020-04-25 13:51:11 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>
```
Storing the scraped data
```
(base) ztdeMacBook-Air:spiders zt$ scrapy crawl quotes -o quotes.json
2020-04-25 13:52:35 [scrapy.utils.log] INFO: Scrapy 1.6.0 started (bot: tutorial)
2020-04-25 13:52:35 [scrapy.utils.log] INFO: Versions: lxml 4.5.0.0, libxml2 2.9.9, cssselect 1.1.0, parsel 1.5.2, w3lib 1.20.0, Twisted 20.3.0, Python 3.7.6 (default, Jan  8 2020, 13:42:34) - [Clang 4.0.1 (tags/RELEASE_401/final)], pyOpenSSL 19.1.0 (OpenSSL 1.1.1d  10 Sep 2019), cryptography 2.8, Platform Darwin-17.0.0-x86_64-i386-64bit
2020-04-25 13:52:35 [scrapy.crawler] INFO: Overridden settings: {'BOT_NAME': 'tutorial', 'FEED_FORMAT': 'json', 'FEED_URI': 'quotes.json', 'NEWSPIDER_MODULE': 'tutorial.spiders', 'ROBOTSTXT_OBEY': True, 'SPIDER_MODULES': ['tutorial.spiders']}
2020-04-25 13:52:35 [scrapy.extensions.telnet] INFO: Telnet Password: 7394f7de8c2344f2
2020-04-25 13:52:35 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.memusage.MemoryUsage',
 'scrapy.extensions.feedexport.FeedExporter',
 'scrapy.extensions.logstats.LogStats']
2020-04-25 13:52:35 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2020-04-25 13:52:35 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2020-04-25 13:52:35 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2020-04-25 13:52:35 [scrapy.core.engine] INFO: Spider opened
2020-04-25 13:52:35 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2020-04-25 13:52:35 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6024
2020-04-25 13:52:38 [scrapy.core.engine] DEBUG: Crawled (404) <GET http://quotes.toscrape.com/robots.txt> (referer: None)
2020-04-25 13:52:40 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/page/2/> (referer: None)
2020-04-25 13:52:40 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/2/>
{'text': "“This life is what you make it. No matter what, you're going to mess up sometimes, it's a universal truth. But the good part is you get to decide how you're going to mess it up. Girls will be your friends - they'll act like it anyway. But just remember, some come, some go. The ones that stay with you through everything - they're your true best friends. Don't let go of them. Also remember, sisters make the best friends in the world. As for lovers, well, they'll come and go too. And baby, I hate to say it, most of them - actually pretty much all of them are going to break your heart, but you can't give up because if you give up, you'll never find your soulmate. You'll never find that half who makes you whole and that goes for everything. Just because you fail once, doesn't mean you're gonna fail at everything. Keep trying, hold on, and always, always, always believe in yourself, because if you don't, then who will, sweetie? So keep your head high, keep your chin up, and most importantly, keep smiling, because life's a beautiful thing and there's so much to smile about.”", 'author': 'Marilyn Monroe', 'tags': ['friends', 'heartbreak', 'inspirational', 'life', 'love', 'sisters']}
2020-04-25 13:52:40 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/2/>
{'text': '“It takes a great deal of bravery to stand up to our enemies, but just as much to stand up to our friends.”', 'author': 'J.K. Rowling', 'tags': ['courage', 'friends']}
2020-04-25 13:52:40 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/2/>
{'text': "“If you can't explain it to a six year old, you don't understand it yourself.”", 'author': 'Albert Einstein', 'tags': ['simplicity', 'understand']}
2020-04-25 13:52:40 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/2/>
{'text': "“You may not be her first, her last, or her only. She loved before she may love again. But if she loves you now, what else matters? She's not perfect—you aren't either, and the two of you may never be perfect together but if she can make you laugh, cause you to think twice, and admit to being human and making mistakes, hold onto her and give her the most you can. She may not be thinking about you every second of the day, but she will give you a part of her that she knows you can break—her heart. So don't hurt her, don't change her, don't analyze and don't expect more than she can give. Smile when she makes you happy, let her know when she makes you mad, and miss her when she's not there.”", 'author': 'Bob Marley', 'tags': ['love']}
2020-04-25 13:52:40 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/2/>
{'text': '“I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living.”', 'author': 'Dr. Seuss', 'tags': ['fantasy']}
2020-04-25 13:52:40 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/2/>
{'text': '“I may not have gone where I intended to go, but I think I have ended up where I needed to be.”', 'author': 'Douglas Adams', 'tags': ['life', 'navigation']}
2020-04-25 13:52:40 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/2/>
{'text': "“The opposite of love is not hate, it's indifference. The opposite of art is not ugliness, it's indifference. The opposite of faith is not heresy, it's indifference. And the opposite of life is not death, it's indifference.”", 'author': 'Elie Wiesel', 'tags': ['activism', 'apathy', 'hate', 'indifference', 'inspirational', 'love', 'opposite', 'philosophy']}
2020-04-25 13:52:40 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/2/>
{'text': '“It is not a lack of love, but a lack of friendship that makes unhappy marriages.”', 'author': 'Friedrich Nietzsche', 'tags': ['friendship', 'lack-of-friendship', 'lack-of-love', 'love', 'marriage', 'unhappy-marriage']}
2020-04-25 13:52:40 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/2/>
{'text': '“Good friends, good books, and a sleepy conscience: this is the ideal life.”', 'author': 'Mark Twain', 'tags': ['books', 'contentment', 'friends', 'friendship', 'life']}
2020-04-25 13:52:40 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/2/>
{'text': '“Life is what happens to us while we are making other plans.”', 'author': 'Allen Saunders', 'tags': ['fate', 'life', 'misattributed-john-lennon', 'planning', 'plans']}
2020-04-25 13:52:45 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/page/1/> (referer: None)
2020-04-25 13:52:45 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>
{'text': '“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”', 'author': 'Albert Einstein', 'tags': ['change', 'deep-thoughts', 'thinking', 'world']}
2020-04-25 13:52:45 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>
{'text': '“It is our choices, Harry, that show what we truly are, far more than our abilities.”', 'author': 'J.K. Rowling', 'tags': ['abilities', 'choices']}
2020-04-25 13:52:45 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>
{'text': '“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”', 'author': 'Albert Einstein', 'tags': ['inspirational', 'life', 'live', 'miracle', 'miracles']}
2020-04-25 13:52:45 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>
{'text': '“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”', 'author': 'Jane Austen', 'tags': ['aliteracy', 'books', 'classic', 'humor']}
2020-04-25 13:52:45 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>
{'text': "“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”", 'author': 'Marilyn Monroe', 'tags': ['be-yourself', 'inspirational']}
2020-04-25 13:52:45 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>
{'text': '“Try not to become a man of success. Rather become a man of value.”', 'author': 'Albert Einstein', 'tags': ['adulthood', 'success', 'value']}
2020-04-25 13:52:45 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>
{'text': '“It is better to be hated for what you are than to be loved for what you are not.”', 'author': 'André Gide', 'tags': ['life', 'love']}
2020-04-25 13:52:45 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>
{'text': "“I have not failed. I've just found 10,000 ways that won't work.”", 'author': 'Thomas A. Edison', 'tags': ['edison', 'failure', 'inspirational', 'paraphrased']}
2020-04-25 13:52:45 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>
{'text': "“A woman is like a tea bag; you never know how strong it is until it's in hot water.”", 'author': 'Eleanor Roosevelt', 'tags': ['misattributed-eleanor-roosevelt']}
2020-04-25 13:52:45 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>
{'text': '“A day without sunshine is like, you know, night.”', 'author': 'Steve Martin', 'tags': ['humor', 'obvious', 'simile']}
2020-04-25 13:52:45 [scrapy.core.engine] INFO: Closing spider (finished)
2020-04-25 13:52:45 [scrapy.extensions.feedexport] INFO: Stored json feed (20 items) in: quotes.json
2020-04-25 13:52:46 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 678,
 'downloader/request_count': 3,
 'downloader/request_method_count/GET': 3,
 'downloader/response_bytes': 6081,
 'downloader/response_count': 3,
 'downloader/response_status_count/200': 2,
 'downloader/response_status_count/404': 1,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2020, 4, 25, 5, 52, 45, 998985),
 'item_scraped_count': 20,
 'log_count/DEBUG': 23,
 'log_count/INFO': 10,
 'memusage/max': 51412992,
 'memusage/startup': 51408896,
 'response_received_count': 3,
 'robotstxt/request_count': 1,
 'robotstxt/response_count': 1,
 'robotstxt/response_status_count/404': 1,
 'scheduler/dequeued': 2,
 'scheduler/dequeued/memory': 2,
 'scheduler/enqueued': 2,
 'scheduler/enqueued/memory': 2,
 'start_time': datetime.datetime(2020, 4, 25, 5, 52, 35, 924675)}
2020-04-25 13:52:46 [scrapy.core.engine] INFO: Spider closed (finished)
(base) ztdeMacBook-Air:spiders zt$ scrapy crawl quotes -o quotes.csv
2020-04-25 13:54:26 [scrapy.utils.log] INFO: Scrapy 1.6.0 started (bot: tutorial)
2020-04-25 13:54:26 [scrapy.utils.log] INFO: Versions: lxml 4.5.0.0, libxml2 2.9.9, cssselect 1.1.0, parsel 1.5.2, w3lib 1.20.0, Twisted 20.3.0, Python 3.7.6 (default, Jan  8 2020, 13:42:34) - [Clang 4.0.1 (tags/RELEASE_401/final)], pyOpenSSL 19.1.0 (OpenSSL 1.1.1d  10 Sep 2019), cryptography 2.8, Platform Darwin-17.0.0-x86_64-i386-64bit
2020-04-25 13:54:26 [scrapy.crawler] INFO: Overridden settings: {'BOT_NAME': 'tutorial', 'FEED_FORMAT': 'csv', 'FEED_URI': 'quotes.csv', 'NEWSPIDER_MODULE': 'tutorial.spiders', 'ROBOTSTXT_OBEY': True, 'SPIDER_MODULES': ['tutorial.spiders']}
2020-04-25 13:54:26 [scrapy.extensions.telnet] INFO: Telnet Password: 16d2044e20971aec
2020-04-25 13:54:26 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.memusage.MemoryUsage',
 'scrapy.extensions.feedexport.FeedExporter',
 'scrapy.extensions.logstats.LogStats']
2020-04-25 13:54:26 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2020-04-25 13:54:26 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2020-04-25 13:54:26 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2020-04-25 13:54:26 [scrapy.core.engine] INFO: Spider opened
2020-04-25 13:54:26 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2020-04-25 13:54:26 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6024
2020-04-25 13:54:29 [scrapy.core.engine] DEBUG: Crawled (404) <GET http://quotes.toscrape.com/robots.txt> (referer: None)
2020-04-25 13:54:31 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/page/2/> (referer: None)
2020-04-25 13:54:31 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/2/>
{'text': "“This life is what you make it. No matter what, you're going to mess up sometimes, it's a universal truth. But the good part is you get to decide how you're going to mess it up. Girls will be your friends - they'll act like it anyway. But just remember, some come, some go. The ones that stay with you through everything - they're your true best friends. Don't let go of them. Also remember, sisters make the best friends in the world. As for lovers, well, they'll come and go too. And baby, I hate to say it, most of them - actually pretty much all of them are going to break your heart, but you can't give up because if you give up, you'll never find your soulmate. You'll never find that half who makes you whole and that goes for everything. Just because you fail once, doesn't mean you're gonna fail at everything. Keep trying, hold on, and always, always, always believe in yourself, because if you don't, then who will, sweetie? So keep your head high, keep your chin up, and most importantly, keep smiling, because life's a beautiful thing and there's so much to smile about.”", 'author': 'Marilyn Monroe', 'tags': ['friends', 'heartbreak', 'inspirational', 'life', 'love', 'sisters']}
2020-04-25 13:54:31 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/2/>
{'text': '“It takes a great deal of bravery to stand up to our enemies, but just as much to stand up to our friends.”', 'author': 'J.K. Rowling', 'tags': ['courage', 'friends']}
2020-04-25 13:54:31 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/2/>
{'text': "“If you can't explain it to a six year old, you don't understand it yourself.”", 'author': 'Albert Einstein', 'tags': ['simplicity', 'understand']}
2020-04-25 13:54:31 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/2/>
{'text': "“You may not be her first, her last, or her only. She loved before she may love again. But if she loves you now, what else matters? She's not perfect—you aren't either, and the two of you may never be perfect together but if she can make you laugh, cause you to think twice, and admit to being human and making mistakes, hold onto her and give her the most you can. She may not be thinking about you every second of the day, but she will give you a part of her that she knows you can break—her heart. So don't hurt her, don't change her, don't analyze and don't expect more than she can give. Smile when she makes you happy, let her know when she makes you mad, and miss her when she's not there.”", 'author': 'Bob Marley', 'tags': ['love']}
2020-04-25 13:54:31 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/2/>
{'text': '“I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living.”', 'author': 'Dr. Seuss', 'tags': ['fantasy']}
2020-04-25 13:54:31 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/2/>
{'text': '“I may not have gone where I intended to go, but I think I have ended up where I needed to be.”', 'author': 'Douglas Adams', 'tags': ['life', 'navigation']}
2020-04-25 13:54:31 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/2/>
{'text': "“The opposite of love is not hate, it's indifference. The opposite of art is not ugliness, it's indifference. The opposite of faith is not heresy, it's indifference. And the opposite of life is not death, it's indifference.”", 'author': 'Elie Wiesel', 'tags': ['activism', 'apathy', 'hate', 'indifference', 'inspirational', 'love', 'opposite', 'philosophy']}
2020-04-25 13:54:31 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/2/>
{'text': '“It is not a lack of love, but a lack of friendship that makes unhappy marriages.”', 'author': 'Friedrich Nietzsche', 'tags': ['friendship', 'lack-of-friendship', 'lack-of-love', 'love', 'marriage', 'unhappy-marriage']}
2020-04-25 13:54:31 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/2/>
{'text': '“Good friends, good books, and a sleepy conscience: this is the ideal life.”', 'author': 'Mark Twain', 'tags': ['books', 'contentment', 'friends', 'friendship', 'life']}
2020-04-25 13:54:31 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/2/>
{'text': '“Life is what happens to us while we are making other plans.”', 'author': 'Allen Saunders', 'tags': ['fate', 'life', 'misattributed-john-lennon', 'planning', 'plans']}
2020-04-25 13:54:34 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/page/1/> (referer: None)
2020-04-25 13:54:34 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>
{'text': '“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”', 'author': 'Albert Einstein', 'tags': ['change', 'deep-thoughts', 'thinking', 'world']}
2020-04-25 13:54:34 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>
{'text': '“It is our choices, Harry, that show what we truly are, far more than our abilities.”', 'author': 'J.K. Rowling', 'tags': ['abilities', 'choices']}
2020-04-25 13:54:34 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>
{'text': '“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”', 'author': 'Albert Einstein', 'tags': ['inspirational', 'life', 'live', 'miracle', 'miracles']}
2020-04-25 13:54:34 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>
{'text': '“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”', 'author': 'Jane Austen', 'tags': ['aliteracy', 'books', 'classic', 'humor']}
2020-04-25 13:54:34 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>
{'text': "“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”", 'author': 'Marilyn Monroe', 'tags': ['be-yourself', 'inspirational']}
2020-04-25 13:54:34 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>
{'text': '“Try not to become a man of success. Rather become a man of value.”', 'author': 'Albert Einstein', 'tags': ['adulthood', 'success', 'value']}
2020-04-25 13:54:34 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>
{'text': '“It is better to be hated for what you are than to be loved for what you are not.”', 'author': 'André Gide', 'tags': ['life', 'love']}
2020-04-25 13:54:34 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>
{'text': "“I have not failed. I've just found 10,000 ways that won't work.”", 'author': 'Thomas A. Edison', 'tags': ['edison', 'failure', 'inspirational', 'paraphrased']}
2020-04-25 13:54:34 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>
{'text': "“A woman is like a tea bag; you never know how strong it is until it's in hot water.”", 'author': 'Eleanor Roosevelt', 'tags': ['misattributed-eleanor-roosevelt']}
2020-04-25 13:54:34 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>
{'text': '“A day without sunshine is like, you know, night.”', 'author': 'Steve Martin', 'tags': ['humor', 'obvious', 'simile']}
2020-04-25 13:54:34 [scrapy.core.engine] INFO: Closing spider (finished)
2020-04-25 13:54:34 [scrapy.extensions.feedexport] INFO: Stored csv feed (20 items) in: quotes.csv
2020-04-25 13:54:34 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 678,
 'downloader/request_count': 3,
 'downloader/request_method_count/GET': 3,
 'downloader/response_bytes': 6081,
 'downloader/response_count': 3,
 'downloader/response_status_count/200': 2,
 'downloader/response_status_count/404': 1,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2020, 4, 25, 5, 54, 34, 694683),
 'item_scraped_count': 20,
 'log_count/DEBUG': 23,
 'log_count/INFO': 10,
 'memusage/max': 51474432,
 'memusage/startup': 51474432,
 'response_received_count': 3,
 'robotstxt/request_count': 1,
 'robotstxt/response_count': 1,
 'robotstxt/response_status_count/404': 1,
 'scheduler/dequeued': 2,
 'scheduler/dequeued/memory': 2,
 'scheduler/enqueued': 2,
 'scheduler/enqueued/memory': 2,
 'start_time': datetime.datetime(2020, 4, 25, 5, 54, 26, 786715)}
2020-04-25 13:54:34 [scrapy.core.engine] INFO: Spider closed (finished)
(base) ztdeMacBook-Air:spiders zt$ 
```
Then you will be able to see quotes.json and quotes.csv in spider fold

## References Material:
Scrapy Tutorial
<br>http://doc.scrapy.org/en/latest/intro/tutorial.html#crawling
Feed exports
<br>http://doc.scrapy.org/en/latest/topics/feed-exports.html#topics-feed-format-csv
Unknown Command when I enter "scrapy crawl quotes" #3344
<br>https://github.com/scrapy/scrapy/issues/3344
Build a scalable web crawler with Selenium and Python
<br>https://towardsdatascience.com/build-a-scalable-web-crawler-with-selenium-and-pyhton-9c0c23e3ebe5
<br>How To Scrape Amazon Product Data and Prices using Python 3
<br>https://www.scrapehero.com/tutorial-how-to-scrape-amazon-product-details-using-python-and-selectorlib/
<br>How to scrape websites without getting blocked
<br>https://www.scrapehero.com/how-to-prevent-getting-blacklisted-while-scraping/
<br>How to scrape Amazon Reviews using Python
<br>https://www.scrapehero.com/how-to-scrape-amazon-product-reviews/
