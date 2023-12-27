# ...
# @list_data(*cases)
#     def test_login(self, case):
#         """
#         登陆测试
#         """
#         logger.info('测试用例【{}】开始测试'.format(case['title']))
#         # 1. 测试数据
#         # 传入进来的case参数
#         logger.info('测试用例【{}】的测试数据是:{}'.format(case['title'], case))
#         # 2. 测试步骤
#         res = login_check(case['username'], case['password'])
#         logger.info('测试用例【{}】的测试结果是:{}'.format(case['title'], res))
#         # 3. 断言
#         try:
#             self.assertEqual(res, case['expect'])
#         except AssertionError as e:
#             logger.error('测试用例【{}】断言失败'.format(case['title']))
#             raise e
#         else:
#             logger.info('测试用例【{}】断言成功'.format(case['title']))
#         finally:
#             logger.info('测试用例【{}】测试结束')
