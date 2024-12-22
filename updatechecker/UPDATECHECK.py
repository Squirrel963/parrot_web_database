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
