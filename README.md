# Parrot Web Database
![额，由于某些问题，该图片没能正常显示](PWD_ct.svg "空驱动器？不是我干的。")  
一个基于web网页实现的伪数据库  
为Python程序客户端提供数据  
**~~仅此而已！~~**
>由于一些格式显示问题，如果您使用的是Edge浏览器，请关闭翻译后阅读本文

__锚点引导：__  
[数据库信息调用](#数据库信息调用)  
[数据库信息命名格式](#数据库信息命名格式)  
[数据库更新日志格式](#数据库allinfo格式)   
[PWD数据库配套更新检查模块](#PWD数据库配套更新检查模块)  

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
`allinfo`：适用于目标项目的公告/更新日志  
`clientlast`：目标项目的最新版本的文件存档  
`prolast`：目标项目的测试/特殊版本的文件存档

# PWD数据库配套更新检查模块
可以在此仓库下载专用的全自动更新检查模块(适用于Python)  
{  [下载](updatechecker/UPDATECHECK.py)  }  

## 数据库allinfo（更新日志）格式
```
/版本：
{+}新增内容
{-}修改/删除内容
/版本：
{+}新增内容
{-}修改/删除内容
```  
例：  
```
/1.0.2：
{+}修复一些bug
/1.0.1：
{-}优化稳定性
```  



>注意：在进行以下操作前，您需要先获取"PWD数据库配套更新检查模块"

### 更新检查（check）

程序内调用方法：
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

注意：该方法会产生仅占终端窗口1行的输出  
如果您不需要这些输出，您可以试试下方`getversion()`方法

### 最新版本号获取（getversion）

如果您认为`check()`方法不适用于您的程序  
您可以试试直接获取**最新版本号**，如下：

程序内调用方法：
```python
import UPDATECHECK
UPDATECHECK.getversion(uri)
``` 
`uri`为最新版本号数据源地址(http/https)  
 例：  
```python
import UPDATECHECK
netversion = UPDATECHECK.getversion("https://squirrel963.github.io/parrot_web_database/WTC_clientversion/index.md")
``` 
以上代码将使更新检查器获取`WTC_clientversion`的数据  
并将它返回并赋值到`netversion`中

### 更新日志获取（getlog）

程序内调用方法：
```python
import UPDATECHECK
log = UPDATECHECK.getlog(uri)
``` 
`uri`为更新日志数据源地址(http/https)  
 例：  
```python
import UPDATECHECK
log = UPDATECHECK.getlog("https://squirrel963.github.io/parrot_web_database/WTC_allinfo/index.md")
```
以上代码将使更新检查器获取`WTC_allinfo`的数据  
并将数据打包成一个字典返回并赋值到`log`
