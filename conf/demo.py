from conf import Conf
from utils.YamlUtil import YamlReader


def get_keyword():
    # 1、读取配置文件，文件路径：绝对路径
    keyword_file = Conf.keywords_path
    # 2、YamlReader, data()
    reader = YamlReader(keyword_file).data()
    # 3、key获取值 name
    value = reader[name]
    return value


if __name__ == '__main__':
    print(get_keyword("click"))
