print('主线程执行代码')

# 从 threading 库中导入Thread类
from threading import Thread
from time import sleep
import requests


# 定义一个函数，作为新线程执行的入口函数
def threadFunc(arg1,arg2):
    print('子线程 开始')
    taskList = [
        'http://httpbin.org/ip',
        'http://lf26-cdn-tos.bytecdntp.com/cdn/expire-1-M/ace/1.4.14/ext-linking.js',
        'http://lf26-cdn-tos.bytecdntp.com/cdn/expire-1-M/Base64/1.1.0/base64.min.js.map',
    ]
    with open('readme89.TXT', 'w') as f:
        for url in taskList:
            res = requests.get(url)
            print(res.text)
            f.write(res.text)
    print('子线程 结束')


# 创建 Thread 类的实例对象
thread = Thread(
    target=threadFunc,
    args=('参数1', '参数2')
)

thread.start()

thread.join()
print('主线程结束')