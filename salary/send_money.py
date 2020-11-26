"""

定义发工资模块
"""
import money


def send_money():
    money.saved_money = 2000
    print("发工资啦")


if __name__ == '__main__':
    send_money()
