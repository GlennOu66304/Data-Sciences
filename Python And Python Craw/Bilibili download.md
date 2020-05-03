# Bilibili download.
## 1. Url extract downlaod:
哔哩哔哩视频下载在线工具
<br>https://www.guoxingjun.com/video/bilibili

## 2.Youtube Video Download
<br>https://github.com/GlennOu66304/Other/blob/master/Youtube%20Video%20Download/Youtube%20Video%20Download.md
```
zhanghuiqiao@zhanghuiqiaodeMacBook-Pro ~ % youtube-dl "https://www.bilibili.com/video/BV127411t7WJ"
[BiliBili] 127411t7WJ: Downloading webpage
[BiliBili] 127411t7WJ: Downloading video info page
[download] Destination: 【经典女星】每天一遍，防止早恋。-127411t7WJ.flv
[download] 100% of 15.97MiB in 00:19
```
You will find video file in /Users/zhanghuiqiao This location

## 3.Craw download Method
### 1. clone file into local 
Data-Sciences/Python And Python Craw/Bilibili_video_download-master/
<br>https://github.com/GlennOu66304/Data-Sciences/tree/master/Python%20And%20Python%20Craw/Bilibili_video_download-master
### 2. Move to spider file:
```
zhanghuiqiao@zhanghuiqiaodeMacBook-Pro ~ % cd /Users/zhanghuiqiao/Downloads/Bilibili_video_download-master  
```
### 3. install certain package requirements.txt :
```
zhanghuiqiao@zhanghuiqiaodeMacBook-Pro Bilibili_video_download-master % pip3 install -r requirements.txt                                     
Requirement already satisfied: moviepy==0.2.3.2 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from -r requirements.txt (line 1)) (0.2.3.2)
Requirement already satisfied: requests==2.18.4 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from -r requirements.txt (line 2)) (2.18.4)
Collecting imageio==2.1.2 (from moviepy==0.2.3.2->-r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/68/31/55cad23b6bd32afee6e4c7eec2f15266665879f8eaf812e3b843205d41ad/imageio-2.1.2.zip
Requirement already satisfied: tqdm==4.11.2 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from moviepy==0.2.3.2->-r requirements.txt (line 1)) (4.11.2)
Requirement already satisfied: decorator==4.0.11 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from moviepy==0.2.3.2->-r requirements.txt (line 1)) (4.0.11)
Requirement already satisfied: numpy in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from moviepy==0.2.3.2->-r requirements.txt (line 1)) (1.18.3)
Requirement already satisfied: certifi>=2017.4.17 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from requests==2.18.4->-r requirements.txt (line 2)) (2020.4.5.1)
Requirement already satisfied: urllib3<1.23,>=1.21.1 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from requests==2.18.4->-r requirements.txt (line 2)) (1.22)
Requirement already satisfied: chardet<3.1.0,>=3.0.2 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from requests==2.18.4->-r requirements.txt (line 2)) (3.0.4)
Requirement already satisfied: idna<2.7,>=2.5 in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from requests==2.18.4->-r requirements.txt (line 2)) (2.6)
Requirement already satisfied: pillow in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from imageio==2.1.2->moviepy==0.2.3.2->-r requirements.txt (line 1)) (7.1.2)
Installing collected packages: imageio
  Found existing installation: imageio 2.4.1
    Uninstalling imageio-2.4.1:
ERROR: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied: '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/imageio-2.4.1-py3.8.egg-info/PKG-INFO'
Consider using the `--user` option or check the permissions.

WARNING: You are using pip version 19.2.3, however version 20.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
```
### 4. install certain package imageio:
```
zhanghuiqiao@zhanghuiqiaodeMacBook-Pro Bilibili_video_download-master % pip3 install imageio 
Requirement already satisfied: imageio in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (2.4.1)
Requirement already satisfied: numpy in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from imageio) (1.18.3)
Requirement already satisfied: pillow in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (from imageio) (7.1.2)
WARNING: You are using pip version 19.2.3, however version 20.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
```
### 5. Run Spider file to downlaod the Bilibili Video:
```
zhanghuiqiao@zhanghuiqiaodeMacBook-Pro Bilibili_video_download-master % python3 /Users/zhanghuiqiao/Downloads/Bilili/bilibili_video_download_bangumi.py
******************************B站番剧视频下载小助手******************************
[提示]: 1.如果您想下载720P60,1080p+,1080p60质量的视频,请将35行代码中的SESSDATA改成你登录大会员后得到的SESSDATA,普通用户的SESSDATA最多只能下载1080p的视频
       2.若发现下载的视频质量在720p以下,请将35行代码中的SESSDATA改成你登录后得到的SESSDATA(有效期一个月),而失效的SESSDATA就只能下载480p的视频
请输入您要下载的B站番剧的完整链接地址(例如:https://www.bilibili.com/bangumi/play/ep267692):https://www.bilibili.com/bangumi/play/ep269835
请输入1或2 - 1.只下载当前一集 2.下载此番剧的全集:1
请输入您要下载视频的清晰度(1080p60:116;1080p+:112;1080p:80;720p60:74;720p:64;480p:32;360p:16; **注意:1080p+,1080p60,720p60都需要带入大会员的cookie中的SESSDATA才行,普通用户的SESSDATA最多只能下载1080p的视频):
请输入116或112或80或74或64或32或16:116
[[54841483, 96869009, '第10话 捕鱼猫和老大']]
[下载番剧标题]:第10话 捕鱼猫和老大
['http://upos-sz-mirrorkodo.bilivideo.com/upgcxcode/09/90/96869009/96869009-1-32.flv?e=ig8euxZM2rNcNbN1hwdVhoMghWdVhwdEto8g5X10ugNcXBlqNxHxNEVE5XREto8KqJZHUa6m5J0SqE85tZvEuENvNo8g2ENvNo8i8o859r1qXg8xNEVE5XREto8GuFGv2U7SuxI72X6fTr859r1qXg8gNEVE5XREto8z5JZC2X2gkX5L5F1eTX1jkXlsTXHeux_f2o859IB_&uipk=5&nbs=1&deadline=1588504409&gen=playurl&os=kodobv&oi=1928708268&trid=3897376371ab4579b55d894828559f25u&platform=pc&upsig=a360f598d470f67a46792b5bc5ae0e69&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&mid=0&logo=80000000']
[正在下载第1话视频,请稍等...]:第10话 捕鱼猫和老大
['第10话 捕鱼猫和老大']####################################] Speed: 199.925K
[视频合并完成]:第10话 捕鱼猫和老大
下载总耗时136.91秒,约2.27分钟
```
### 6.You will find Video file in bilibili_video folder.

### 7.Play Video in IINA FLV Video palyer
IINA
<br>https://iina.io/
<br>Mac 上好用的视频播放器有哪些？
<br>https://www.zhihu.com/question/19552878

## References:
Henryhaohao/Bilibili_video_download
<br>https://github.com/Henryhaohao/Bilibili_video_download

<br>Comments For Spider code from Henryhaohao/Bilibili_video_download, You need to change the imageio code part to 
```
import imageio
imageio.plugins.ffmpeg.download()
from moviepy.editor import *
```
To make sure the py file is running withought error.(Comment from Zulko in issue FFMPEG not downloaded
#493)
<br>FFMPEG not downloaded #493
<br>https://github.com/Zulko/moviepy/issues/493

<br>如何下载b站的视频？
<br>https://www.zhihu.com/question/310725414

