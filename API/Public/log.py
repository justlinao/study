import logging
import time
import os


def get_log():
    log = logging.getLogger('API_test')  # 创建一个log对象 不传递参数默认命名为root
    log.handlers.clear()  # 及时清理 handlers 不然会出现日志递增重复的情况
    log.setLevel(logging.INFO)  # 设置日志等级

    log_time = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))  # 当前时间 精确到分
    log_path = os.path.dirname(os.getcwd())+'/Log/'  # log存放路径
    log_name = log_path + log_time + '.log'  #

    fh = logging.FileHandler(log_name)  # 日志到文件
    fh.setLevel(logging.INFO)

    ch = logging.StreamHandler()  # 日志到控制台
    ch.setLevel(logging.INFO)

    log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # 日志格式
    fh.setFormatter(log_formatter)  # 将定义好的输出形式添加到handler
    ch.setFormatter(log_formatter)

    log.addHandler(fh)
    log.addHandler(ch)
    return log







