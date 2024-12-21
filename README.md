# Parrot Web Database
![](PWD_ct.svg)  
一个基于web网页实现的伪数据库  
为Parrot_X系列程序客户端提供数据  
仅此而已！
>由于一些格式显示问题，如果您使用的是Edge浏览器，请关闭翻译后阅读本文  
# 锚点引导：
[数据库信息调用](#数据库信息调用)
## 数据库信息调用
要获取PWD数据库中的信息  
需通过github.io页面访问：  

squirrel963.github.io/parrot_web_database/`你需要的数据名称`/index.md
## 对于Parrot_X系列程序的更新检查
可以在此仓库下载专用的全自动更新检查模块{[下载](updatechecker)}  
程序内调用方法(python)：
```python
import UPDATECHECK
UPDATECHECK.check(version,uri)
``` 
`version`为程序目前的版本  
`uri`为最新版本号数据源地址(http/https)  
 例：  
```python
import UPDATECHECK
UPDATECHECK.check("1.0.4","https://squirrel963.github.io/parrot_web_database/WTC_clientversion/index.md")
``` 
以上代码将使更新检查器获取`https://squirrel963.github.io/parrot_web_database/WTC_clientversion/index.md`的内容  
并将它与输入的程序版本`1.0.4`进行比较  
