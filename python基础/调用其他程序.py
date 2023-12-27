import os

# 目标目录
targetDir = r'D:\code\demo0701\callOthers'
files =  os.listdir(targetDir)

for  origin_video  in  files :
    # 取出原视频 名称，类型
    origin_name,type  = origin_video.split('.')
    origin_video = 'callOthers\\'+origin_name+'.'+type
    # 名称后 +new，组装
    new_voice_video = 'callOthers\\'+origin_name+'_new.'+type
    cmd = r'ffmpeg.exe -i '+origin_video+' -af asetrate=44100*8.9/10,atempo=10/8.9 -c:v copy '+new_voice_video
    print(cmd)
    os.system(cmd)
    print('转换完成')

