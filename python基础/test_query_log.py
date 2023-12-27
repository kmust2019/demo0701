line_list = ['1571713697.7472|110|响应超时|/api/distributor/orders?action=list&pagenum=3&pagesize=5&keywords=&_=1571625069571',
'1571713697.7530|API list_order >1s|sales_248',
'1571713697.7823|110|响应超时|/api/distributor/orders?action=list&pagenum=2&pagesize=5&keywords=&_=1571625069571',
'1571713697.7911|API list_order >1s|sales_1399','1571713697.9424|API list_order >1s|sales_250'
'1571713698.0097|API list_order >1s|sales_1417','1571713627.4345|API list_order >0.05s|sales_285'
,'1571713627.4540|API list_order >0.03s|sales_583']

resp_time_dict = {}

for line in line_list:
    if line.find('响应超时') >= 0:
        if '响应超时' in resp_time_dict :
            resp_time_dict['响应超时'] += 1
        else:
            resp_time_dict['响应超时'] = 1
    else :
        list  = line.split('|')
        resp_time_key = list [1]
        if resp_time_key in resp_time_dict :
            resp_time_dict [resp_time_key] += 1
        else:
            resp_time_dict[resp_time_key]= 1

for key , value  in resp_time_dict.items() :
    value = str(resp_time_dict[key])+'个'
    resp_time_dict[key] =value

print(resp_time_dict)

print(str(resp_time_dict))
