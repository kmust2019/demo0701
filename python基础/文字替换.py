import os
from os.path import isfile, join,isdir

# 目标目录
targetDir = r'D:\code\demo0701\prac_re'

files = []
dirs  = []

# 下面的三个变量 dirpath, dirnames, filenames
# dirpath 代表当前遍历到的目录名
# dirnames 是列表对象，存放当前dirpath中的所有子目录名
# filenames 是列表对象，存放当前dirpath中的所有文件名

for (dirpath, dirnames, filenames) in os.walk(targetDir):
    files += filenames
    dirs += dirnames

print(files)
print(dirs)

keyword='https://www.bilibili.com/video/av74106411/?p='



with open('prac_filerw.txt', 'r',encoding='utf8') as f:
    lines = f.readlines()

# 新文件的内容
newContent = ''
# 一行行分析
for content in lines:
    position = content.find(keyword)
    # 如果没查到
    if position == -1:
        newContent += content
    else:
        before_num = content[0:position] + keyword
        str1, str2 = content.split('?p=')
        # temp 用来记录 ？p= 后面有几位数字
        temp = 0
        for i in str2:
            if i.isdigit():
                temp += 1
            else:
                break

        num = content[position + len(keyword): position + len(keyword) + temp]
        update_num = int(num) + 3
        print(update_num)
        after_num = content[position + len(keyword) + temp:len(content)]
        newContent += before_num+str(update_num)+after_num


with open('prac_filerw2.txt', "w", encoding='utf8') as f:
    f.write(newContent)