import requests
requests.packages.urllib3.disable_warnings()
def check(version, uri):
    print("[ 更新 ]：检查新版本中...",end='\r')
    updated = False
    try:
        cloud = requests.get(uri, verify=False)
        cloud_version = cloud.content
        cloud_version = cloud_version.decode('utf-8')
        cloud_version = cloud_version.strip()
        versioncode = cloud.status_code
        if versioncode == 200:
            if cloud_version == version:
                print('[ 更新 ]：您当前的软件为最新版本')
            else:
                print(f'[ 更新 ]：有新版本的软件: v{cloud_version}可用')
            updated = True
        else:
            print(f'[ 更新 ]：检查失败，返回码为{versioncode}')
    except:
        print('[ 更新 ]：检查失败          ')
    return updated

def getlog(uri):
    uplog = requests.get(uri, verify=False).content.decode("utf-8").replace("\n"," ").split("/")
    uplog.pop(0)
    up_dict = {}
    logvlist = []
    logslist = []
    for i in uplog:
        logvlist.append(i.split("：")[0])
        logslist.append(i.split("：")[1])
    seg = zip(logvlist,logslist)
    return dict(seg)

def getversion(uri):
    try:
        cloud = requests.get(uri, verify=False)
        cloud_version = cloud.content
        cloud_version = cloud_version.decode('utf-8')
        cloud_version = cloud_version.strip()
        versioncode = cloud.status_code
        if versioncode == 200:
            version = cloud_version
        else:
            version = f"fall_{versioncode}"
    except:
        version = "fall"
    return version

if __name__ == '__main__':
    print("UPDATECHECK模块版本自检：")
    check("1.4" ,"https://squirrel963.github.io/parrot_web_database/UC_clientversion/index.md")
    wait = input("*按下enter退出*")
