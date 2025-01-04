# Parrot Web Database
![额，由于一些问题，该图片没能正常显示](PWD_ct.svg "空驱动器？不是我干的。")  
一个基于web网页实现的伪数据库  
为Parrot_X系列程序客户端提供数据  
**~~仅此而已！~~**
>由于一些格式显示问题，如果您使用的是Edge浏览器，请关闭翻译后阅读本文

__锚点引导：__  
[数据库信息调用](#数据库信息调用)  
[数据库信息命名格式](#数据库信息命名格式)  
[PWD数据库配套更新检查模块](#PWD数据库配套更新检查模块)  
[利用PWD数据库进行更新检查](#对于Python程序的更新检查)  
[利用PWD数据库获取更新日志](#对于Python程序的更新日志获取)  

## 数据库信息调用
要获取PWD数据库中的信息  
需通过github.io页面访问：  

squirrel963.github.io/parrot_web_database/`你需要的数据名称`/index.md  
我们建议在地址末尾加入**index.md**，因为这样能去除大量***对程序来说没有用的html元素***，以便处理

## 数据库信息命名格式
PWD通用数据名称命名格式：`项目名称`_`数据类型`  
数据类型标签：  
`clientversion`：目标项目的最新版本号  
`proversion`：目标项目的测试/特殊版本的最新版本号  
`allinfo`：适用于目标项目的公告  
`clientlast`：目标项目的最新版本的文件存档  
`prolast`：目标项目的测试/特殊版本的文件存档

# PWD数据库配套更新检查模块
可以在此仓库下载专用的全自动更新检查模块(适用于Python){[下载](updatechecker)}  

## 对于Python程序的更新检查
>在进行以下操作前，您需要获取[PWD数据库配套更新检查模块](#PWD数据库配套更新检查模块)  

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
以上代码将使更新检查器获取`WTC_clientversion`的数据  
并将它与输入的程序版本`1.0.4`进行比较  

## 对于Python程序的更新日志获取
>在进行以下操作前，您需要获取[PWD数据库配套更新检查模块](#PWD数据库配套更新检查模块)  

程序内调用方法(python)：
```python
import UPDATECHECK
log = UPDATECHECK.uplog(uri)
``` 
`uri`为最新版本号数据源地址(http/https)  
 例：  
```python
import UPDATECHECK
log = UPDATECHECK.check("https://squirrel963.github.io/parrot_web_database/WTC_allinfo/index.md")
```
以上代码将使更新检查器获取`WTC_allinfo`的数据  
并将数据打包成一个字典赋值到`log`
