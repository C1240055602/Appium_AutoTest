import os

# 1、获取项目基本目录
# print(__file__)
# print(os.path.dirname(__file__))
# print(os.path.dirname(os.path.dirname(__file__)))
current = os.path.dirname(os.path.dirname(__file__))
# 2、conf目录 连接符os.sep
conf_path = current + os.sep + "conf"
print(conf_path)
# 3、caps.yml
conf_caps = conf_path + os.sep + "caps.yml"
print(conf_caps)

# log目录
log_path = current + os.sep + "logs"
# keywords文件目录
keywords_path = conf_path + os.sep+"keywords.yml"
