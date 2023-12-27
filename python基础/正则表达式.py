import re
import os

def subFunc(match):
    origin_str = match[0]
    # 提取要修改的数字
    number = int(match[1]) + 3
    update_str = f'p={number}'
    print(f'{origin_str} 替换为 {update_str}')
    return update_str

keyword='https://www.bilibili.com/video/av74106411/?p='
# 目标目录
targetDir = r'D:\code\demo0701\prac_re'

for (dirpath, dirnames, filenames) in os.walk(targetDir):
    for fn in filenames:
        # 全路径
        fpath = os.path.join(dirpath, fn)
        with open(fpath, 'r', encoding='utf8') as f:
            lines = f.readlines()
        newContent = ''
        for content in lines:
            position = content.find(keyword)
            # 如果没查到
            if position == -1:
                newContent += content
            else:
                newStr = re.sub(r'/?p=(\d+)', subFunc, content)
                print(newStr)
                newContent += newStr
        with open(fpath, "w", encoding='utf8') as f:
            f.write(newContent)
