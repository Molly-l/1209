import re

def get_address(file):
    """
    :param file: 查找目标
    :return: 查找到的地址
    """
    port = input("端口:")

    while True:
        data = ''
        for line in file:
            if line == '\n':
                break
            data += line
        obj = re.match(r'\S+',data) # 匹配首单词
        if not obj:
            # 文件结束
            return "PORT ERROR"
        if obj.group() == port:
            # 匹配到了
            # pattern = r"(\d{1,3}\.){3}\d{1,3}/\d+"
            pattern=r"[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}"
            m = re.search(pattern,data)
            if m:
                return m.group()
            return

if __name__ == '__main__':
    f = open('exc.txt')
    print(get_address(f))