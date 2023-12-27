import os

# 获取 callothers目录下 三个文件名
targetDir = r'D:\code\demo0701\callOthers'
files =  os.listdir(targetDir)

videoFiles = ['bandicam_test.mp4']

for  origin_video  in  videoFiles :

    name,type  = origin_video.split('.')
    # name = name.replace(' ','-')

    origin_video = 'callOthers\\'+name+'.'+type
    new_voice_video = 'callOthers\\'+name+'_new.'+type

    cmd = r'ffmpeg.exe -i '+origin_video+' -af asetrate=44100*8.9/10,atempo=10/8.9 -c:v copy '+new_voice_video
    print(cmd)
    os.system(cmd)
    print('转换完成')

#  update_name

# 目标目录

# cmd = r'D:\tools\ffmpeg\ffmpeg.exe -i in.mp4 -af asetrate=44100*8.9/10,atempo=10/8.9 -c:v copy out.mp4'
# os.system(cmd)
#
# print('下载完毕')

# ffmpeg是一个处理视频的工具软件，从下面网盘地址下载。
#
# 只要执行如下命令 ，即可将视频中的声音进行变声
#
# ffmpeg.exe -i in.mp4 -af asetrate=44100*8.9/10,atempo=10/8.9 -c:v copy out.mp4
# 这行命令中， 你要把 ：
#
# in.mp4 替换为 要处理的原来的视频文件名
#
# 比如 bandicam 2020-01-10 10-45-13-679.mp4
#
# out.mp4 替换为输出结果视频文件名
#
# 可以是原来的视频文件加个后缀， 比如 bandicam 2020-01-10 10-45-13-679.new.mp4
#
# 请写一个程序，在程序开头可以定义一个变量，包含一批视频文件名，如下，该程序可以批量将这批文件中所有的视频进行变声
#
# videoFiles = '''
# bandicam 2020-01-10 10-45-13-679.mp4
# bandicam 2020-01-06 11-01-35-020.mp4
# bandicam 2020-01-06 11-05-11-334.mp4
# '''
