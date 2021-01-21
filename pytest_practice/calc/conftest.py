'''
定义计算器类
定义加法 减法 乘法 除法
'''
import os
import pytest
import yaml

from pytest_practice.calc.calculator import Calculator

yaml_file_path = os.path.dirname(__file__) + "/calc_data.yml"  # 获取文件的绝对路径

with open(yaml_file_path, encoding='utf-8') as f:
    caladatas = yaml.safe_load(f)
    add_data = caladatas['add']['add_data']
    add_myid = caladatas['add']['add_myId']
    sub_data = caladatas['sub']['sub_data']
    sub_myid = caladatas['sub']['sub_myId']
    mul_data = caladatas['mul']['mul_data']
    mul_myid = caladatas['mul']['mul_myId']
    div_data = caladatas['div']['div_data']
    div_myid = caladatas['div']['div_myId']
    # print(caladatas)
    # print(div_data)


@pytest.fixture(scope='class')
def get_calc():
    print("-----------开始计算-----------")
    print('获取计算方法')
    calc = Calculator()
    yield calc
    print("-----------计算结束-----------")


@pytest.fixture(params=add_data, ids=add_myid)
# 获取加法 add_data 和 add_myid
def get_add_datas(request):
    # print('开始计算')
    add_data = request.param
    # print(data)
    yield add_data
    # print("结束计算")


@pytest.fixture(params=sub_data, ids=sub_myid)
# 获取减法 sub_data 和 sub_myid
def get_sub_datas(request):
    sub_data = request.param
    yield sub_data


@pytest.fixture(params=mul_data, ids=mul_myid)
# 获取乘法mul_datah和mul_myid
def get_mul_datas(request):
    mul_data = request.param
    print(mul_data)
    yield mul_data


@pytest.fixture(params=div_data, ids=div_myid)
# 获取除法 div_data 和 div_myid
def get_div_datas(request):
    div_data = request.param
    print(div_data)
    yield div_data

# def test_case11(get_mul_datas):
#     print("test testcase11")
