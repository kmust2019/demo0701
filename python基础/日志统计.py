# 要求你写一个程序，统计
#  入参
# 1571713706.3272|110|响应超时|/api/distributor/orders?action=list&pagenum=2&pagesize=5&keywords=&_=1571625069571
# 1571713706.3477|API list_order >1s|sales_967
# 1571713706.3721|110|响应超时|/api/distributor/orders?action=list&pagenum=5&pagesize=5&keywords=&_=1571625069571
# 1571713706.3789|API list_order >1s|sales_1223
# 1571713706.4414|API list_order >1s|sales_371

# 返回结果
# API list_order >0.03s : 548个
# API list_order >0.05s : 274个
# API list_order >0.1s : 306个
# API list_order >0.08s : 105个
# API list_order >0.5s : 157个
# API list_order >1s : 2062个
# 响应超时 : 403个
# 并且把结果写入文件

import traceback

resp_time_dict = {}
with open('2019-10-22_11.05.40.log', 'r', encoding='utf8') as f:
    content = f.read()
    line_list = content.splitlines()
    for line in line_list:
            if line.find('响应超时') >= 0:
                resp_time_key = line.split('|')[2]
            else:
                resp_time_key = line.split('|')[1]

            if resp_time_key in resp_time_dict:
                resp_time_dict[resp_time_key] += 1
            else:
                resp_time_dict[resp_time_key] = 1

content_write = '\n'
for key, value in resp_time_dict.items():
    content_write += key + ' : ' + str(value) + '个\n'

with open('2019-10-22_11.05.40.log', 'a', encoding='utf8') as f:
     f.write(content_write)