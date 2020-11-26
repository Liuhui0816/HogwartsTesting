'''
定义工资查询模块
'''
import money


def select_money():
    current_money = money.saved_money
    if current_money == 2000:
        print("现有存款：" + str(current_money))
    else:
        print("还未收到工资")


if __name__ == '__main__':
    select_money()
