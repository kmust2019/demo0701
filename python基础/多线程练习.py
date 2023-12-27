from threading import Thread, Lock
import requests


taskList = [
        'http://httpbin.org/ip',
        'http://lf26-cdn-tos.bytecdntp.com/cdn/expire-1-M/ace/1.4.14/ext-linking.js',
        'http://lf26-cdn-tos.bytecdntp.com/cdn/expire-1-M/Base64/1.1.0/base64.min.js.map',
]
content_dict = {}

writeLock = Lock()
print('主线程开始')
# 定义一个函数，作为新线程执行的入口函数
def deposit(theadidx, url):
    #  调用requests 库获取 返回报文，存储到 指定文件中
    print(f'子线程 {theadidx} 开始')
    res = requests.get(url)
    # 注意上面的代码不应该放在获取锁的代码中
    writeLock.acquire()
    # 注意 r.text的类型是unicode，可以在文档中查到
    content_dict[theadidx] = res.text
    writeLock.release()
    print(f'子线程 {theadidx} 结束')


theadlist = []
for idx in range(3):
    thread = Thread(target=deposit,
                    args=(idx, taskList[idx])
                    )
    thread.start()
    # 把线程对象都存储到 threadlist中
    theadlist.append(thread)

for thread in theadlist:
    thread.join()

print('主线程结束')
print(content_dict)