# Python
## Coding Enviroment Building:

1.install a python3
<br>Download the latest version for Mac OS X
<br>https://www.python.org/downloads/

2.Test python 3 in your Computer 
```
$ python3 --version
```
3.Launch Pyhton3
```
ztdeMacBook-Air:~ zt$ python3
Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```
4. Run a python file in Terminal:
```
$ python3 my-first-script.py
```
5.Doc Check in Dash.

## Python in Real Life using
### Pyhton Craw Skill:
#### Request
1. Explore the page structure:
Open a website and go to the "view" oprinion in the bar sections. then chooose " developer and view source "
option.

2.install the request package
```
ztdeMacBook-Air:~ zt$ pip3 install requests
Collecting requests
  Downloading https://files.pythonhosted.org/packages/1a/70/1935c770cb3be6e3a8b78ced23d7e0f3b187f5cbfab4749523ed65d7c9b1/requests-2.23.0-py2.py3-none-any.whl (58kB)
     |████████████████████████████████| 61kB 47kB/s 
Collecting idna<3,>=2.5 (from requests)
  Downloading https://files.pythonhosted.org/packages/89/e3/afebe61c546d18fb1709a61bee788254b40e736cff7271c7de5de2dc4128/idna-2.9-py2.py3-none-any.whl (58kB)
     |████████████████████████████████| 61kB 3.9MB/s 
Collecting chardet<4,>=3.0.2 (from requests)
  Downloading https://files.pythonhosted.org/packages/bc/a9/01ffebfb562e4274b6487b4bb1ddec7ca55ec7510b22e4c51f14098443b8/chardet-3.0.4-py2.py3-none-any.whl (133kB)
     |████████████████████████████████| 143kB 77kB/s 
Collecting certifi>=2017.4.17 (from requests)
  Downloading https://files.pythonhosted.org/packages/57/2b/26e37a4b034800c960a00c4e1b3d9ca5d7014e983e6e729e33ea2f36426c/certifi-2020.4.5.1-py2.py3-none-any.whl (157kB)
     |████████████████████████████████| 163kB 91kB/s 
Collecting urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 (from requests)
  Downloading https://files.pythonhosted.org/packages/e1/e5/df302e8017440f111c11cc41a6b432838672f5a70aa29227bf58149dc72f/urllib3-1.25.9-py2.py3-none-any.whl (126kB)
     |████████████████████████████████| 133kB 4.0MB/s 
Installing collected packages: idna, chardet, certifi, urllib3, requests
Successfully installed certifi-2020.4.5.1 chardet-3.0.4 idna-2.9 requests-2.23.0 urllib3-1.25.9
```
3. Crwal a websit to try:
<br>The Lumberjack Song
<br>https://en.wikipedia.org/wiki/The_Lumberjack_Song
```
ztdeMacBook-Air:~ zt$ python3
Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
>>> response = requests.get('https://en.wikipedia.org/wiki/Dead_Parrot_sketch')
>>> print(response.text)

<!DOCTYPE html>
<html class="client-nojs" lang="en" dir="ltr">
<head>
<meta charset="UTF-8"/>
<title>Dead Parrot sketch - Wikipedia</title>
<script>document.documentElement.className="client-js";RLCONF={"wgBreakFrames":!1,"wgSeparatorTransformTable":["",""],"wgDigitTransformTable":["",""],"wgDefaultDateFormat":"dmy","wgMonthNames":["","January","February","March","April","May","June","July","August","September","October","November","December"],"wgRequestId":"XpzO@ApAMM8AAQuBppEAAAAT","wgCSPNonce":!1,"wgCanonicalNamespace":"","wgCanonicalSpecialPageName":!1,"wgNamespaceNumber":0,"wgPageName":"Dead_Parrot_sketch","wgTitle":"Dead Parrot sketch","wgCurRevisionId":950916040,"wgRevisionId":950916040,"wgArticleId":19161,"wgIsArticle":!0,"wgIsRedirect":!1,"wgAction":"view","wgUserName":null,"wgUserGroups":["*"],"wgCategories":["CS1 maint: ref=harv","CS1: Julian–Gregorian uncertainty","Use dmy dates from May 2011","Articles with hAudio microformats","CS1 maint: BOT: original-url status unknown","1969 in British television","Death in fiction","Fictional parrots","Monty Python sketches","Retailing in fiction"],
.....................................
>>> print(type(response.text))
<class 'str'>

```
Requests: HTTP for Humans
<br>https://requests.readthedocs.io/en/master/


#### Beautifulsoup:
1.install a Beautifulsoup package:
```
ztdeMacBook-Air:~ zt$ pip3 install --upgrade pip
Collecting pip
  Downloading https://files.pythonhosted.org/packages/54/0c/d01aa759fdc501a58f431eb594a17495f15b88da142ce14b5845662c13f3/pip-20.0.2-py2.py3-none-any.whl (1.4MB)
     |████████████████████████████████| 1.4MB 173kB/s 
Installing collected packages: pip
  Found existing installation: pip 19.2.3
    Uninstalling pip-19.2.3:
      Successfully uninstalled pip-19.2.3
Successfully installed pip-20.0.2
ztdeMacBook-Air:~ zt$ pip3 install beautifulsoup4
Collecting beautifulsoup4
  Downloading beautifulsoup4-4.9.0-py3-none-any.whl (109 kB)
     |████████████████████████████████| 109 kB 87 kB/s 
Collecting soupsieve>1.2
  Downloading soupsieve-2.0-py2.py3-none-any.whl (32 kB)
Installing collected packages: soupsieve, beautifulsoup4
Successfully installed beautifulsoup4-4.9.0 soupsieve-2.0
ztdeMacBook-Air:~ zt$ 
```
Unable to install beautifulsoup4 in python on Mac Os
<br>https://stackoverflow.com/questions/49703657/unable-to-install-beautifulsoup4-in-python-on-mac-os
Installing Beautiful Soup
<br>https://www.crummy.com/software/BeautifulSoup/bs4/doc/#problems-after-installation

2.Crwal a websit to try: (Partner with request package)
```
ztdeMacBook-Air:~ zt$ python3
Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from bs4 import BeautifulSoup
>>> response = requests.get('https://en.wikipedia.org')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'requests' is not defined
>>> import requests
>>> response = requests.get('https://en.wikipedia.org')
>>> html = response.text
>>> print(html)

<!DOCTYPE html>
<html class="client-nojs" lang="en" dir="ltr">
<head>
<meta charset="UTF-8"/>
<title>Wikipedia, the free encyclopedia</title>
<script>document.documentElement.className="client-js";RLCONF={"wgBreakFrames":!1,"wgSeparatorTransformTable":["",""],"wgDigitTransformTable":["",""],"wgDefaultDateFormat":"dmy","wgMonthNames":["","January","February","March","April","May","June","July","August","September","October","November","December"],"wgRequestId":"XqBuewpAEKAAAPIlmJQAAAAN","wgCSPNonce":!1,"wgCanonicalNamespace":"","wgCanonicalSpecialPageName":!1,"wgNamespaceNumber":0,"wgPageName":"Main_Page","wgTitle":"Main Page","wgCurRevisionId":951809097,"wgRevisionId":951809097,"wgArticleId":15580374,"wgIsArticle":!0,"wgIsRedirect":!1,"wgAction":"view","wgUserName":null,"wgUserGroups":["*"],"wgCategories":[],"wgPageContentLanguage":"en","wgPageContentModel":"wikitext","wgRelevantPageName":"Main_Page","wgRelevantArticleId":15580374,"wgIsProbablyEditable":!1,"wgRelevantPageIsProbablyEditable":!1,"wgRestrictionEdit":["sysop"],"wgRestrictionMove":["sysop"],"wgIsMainPage":!0,"wgMediaViewerOnClick":!0,
...........................................................................................................................
>>> soup.title
<title>Wikipedia, the free encyclopedia</title>

>>> soup.p
<p><b><a href="/wiki/Henry_Conwell" title="Henry Conwell">Henry Conwell</a></b> (<abbr title="circa">c.</abbr><span style="white-space:nowrap;"> 1748</span> – 1842) was an Irish-born <a href="/wiki/Bishop_in_the_Catholic_Church" title="Bishop in the Catholic Church">Catholic bishop</a> in the United States. After serving as a priest in Ireland for more than four decades, he was installed as the second <a href="/wiki/Roman_Catholic_Archdiocese_of_Philadelphia" title="Roman Catholic Archdiocese of Philadelphia">bishop of Philadelphia</a> in 1819.
>>> soup.p.a
<a href="/wiki/Henry_Conwell" title="Henry Conwell">Henry Conwell</a>
>>> 
```
Beautiful Soup Documentation
<br>https://www.crummy.com/software/BeautifulSoup/bs4/doc/#problems-after-installation

1.Python Basics Cheat sheet
<br>https://s3.amazonaws.com/assets.datacamp.com/blog_assets/PythonForDataScience.pdf

5.Doc Check in Dash.

## References:

1.Udacity Video Content:
<br>Introduction to Python Programming
<br>https://classroom.udacity.com/courses/ud1110
<br>2.Introduction to Python
<br>https://learn.datacamp.com/courses/intro-to-python-for-data-science
<br>3.Data Scientist with Python
<br>https://learn.datacamp.com/career-tracks/data-scientist-with-python

2.Book:

<br>1.Fluent Python, 2nd Edition
<br>https://learning.oreilly.com/library/view/fluent-python-2nd/9781492056348/titlepage01.html
<br>2.Learning Python
<br>http://index-of.es/Python/O'Reilly%20-%20Learning%20Python.pdf
<br>3. Learn Python By the Hard Way
<br>https://drive.google.com/file/d/0B3Vviv8oZBzNa0h2cmlPcjZSMnc/view
<br>https://drive.google.com/file/d/0B-hV1HrMP8j1OWpEWXBXbUJsNms/view
<br>https://files.meetup.com/18552511/Learn%20Python%20The%20Hard%20Way%203rd%20Edition%20V413HAV.pdf
