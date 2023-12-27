import requests


taskList = [
    'http://httpbin.org/ip',
    'http://lf26-cdn-tos.bytecdntp.com/cdn/expire-1-M/ace/1.4.14/ext-linking.js',
    'http://lf26-cdn-tos.bytecdntp.com/cdn/expire-1-M/Base64/1.1.0/base64.min.js.map',
]

with open('readme89.TXT', 'w') as f :

    for url in taskList :
        res = requests.get(url)
        print(res.text)
        f.write(res.text)



# 编写一个python程序，创建用多线程方法，分别到里面的网址获取文本内容
#
# 主线程等待这些子线程获取到信息后，将其内容依次合并后存入名为 readme89.TXT 的文件中
#
# 这题要注意防止 存入结果乱序。
#
# 因为，如果第2个线程访问的网站更快，程序处理不好，就会把第2 个结果先存入文件。
#
# 这样次序就乱了，想想怎么解决这个问题。