import re

names = '''

下面是这学期要学习的课程：

<a href='https://www.bilibili.com/video/av66771949/?p=1' target='_blank'>点击这里，边看视频讲解，边学习以下内容</a>
这节讲的是牛顿第2运动定律

<a href='https://www.bilibili.com/video/av46349552/?p=125' target='_blank'>点击这里，边看视频讲解，边学习以下内容</a>
这节讲的是毕达哥拉斯公式

<a href='https://www.bilibili.com/video/av90571967/?p=33' target='_blank'>点击这里，边看视频讲解，边学习以下内容</a>
这节讲的是切割磁力线
'''


# 替换函数，参数是 Match对象
def subFunc(match):

    origin_str = match[0]
    number = int(match[1]) + 3
    update_str = f'p={number}'
    print(f'{origin_str} 替换为 {update_str}')
    return update_str


newStr = re.sub(r'/?p=(\d+)', subFunc, names)
print(newStr)