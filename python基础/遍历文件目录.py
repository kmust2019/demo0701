import os



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
                print('修改前 '+keyword+str(num))
                print('修改后 '+keyword+str(update_num))
                after_num = content[position + len(keyword) + temp:len(content)]
                newContent += before_num + str(update_num) + after_num
        with open(fpath, "w", encoding='utf8') as f:
            f.write(newContent)










