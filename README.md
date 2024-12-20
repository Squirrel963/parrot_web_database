# parrot_database
一个基于web网页实现的伪数据库
为parrot系列程序客户端提供数据
仅此而已！
## 对于Parrot_X系列程序的更新检查
可以在此仓库下载专用的全自动更新检查模块{[下载](updatechecker)}  
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
以上代码将使更新检查器获取`https://squirrel963.github.io/parrot_web_database/WTC_clientversion/index.md`的内容  
并将它与输入的程序版本`1.0.4`进行比较  
