# 请写一个股票信息查询程序，从文件加载数据， 可以让使用者 循环多次 查询股票信息。

# 每次查询时，提示 请输入要查询的股票名称或代码：
# 当用户输入股票代码（6位全是数字）时，打印出对应的 股票名称和代码
# 当用户输入股票名称（不全是数字）时，打印出对应的 股票名称和代码

# 输入 500003
# 返回 基金安信  500003
# 输入 基金安信
# 返回 基金安信  500003


stock_dict = {}

with open('stock.txt', 'r', encoding='utf8') as f:
    content = f.read()
    content_list = content.splitlines()
    for content in content_list:
         stock_name,stock_code = content.split('|')
         stock_dict [stock_name.strip()] = stock_code.strip()

# 反转 key，value
reverse_stock_dict = {v: k for k, v in stock_dict.items()}
def  query_stock_info(user_input,dict1,dict2):
    if user_input in dict1 :
        result = user_input + ' ' + dict1[user_input]
    elif user_input in dict2:
        result = dict2[user_input] + ' ' + user_input
    else:
        result = '未查找到相关股票信息'
    return  result
while True :
    user_input = input('请输入要查询的股票名称或代码：')
    print(query_stock_info(user_input,stock_dict,reverse_stock_dict))









