import os
import yaml


# 1、创建类
class YamlReader:
    # 2、初始化方法，判断文件是否存在
    def __init__(self, yamlf):
        """
        判断文件是否存在，不存在抛出异常
        :param yamlf:
        """
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError("文件不存在")
        self._data = None
        self._data_all = None

    # 3、定义方法，yaml读取 单个文档，多个文档
    def data(self):
        """
        单个文档
        :return:
        """
        if not  self._data:
            with open(self.yamlf, "r", encoding='utf-8') as f:
                 self._data = yaml.safe_load(f)
        return  self._data

    def data_all(self):
        """
        多个文档，以列表方式返回
        :return:
        """
        if not self._data_all:
            with open(self.yamlf, "r", encoding="utf-8") as f:
                 self._data_all = list(yaml.safe_load_all(f))
        return self._data_all
