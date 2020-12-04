"""
    补全计算器中加法和除法的测试用例
    使用参数化完成测试用例的自动生成
    在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】

"""
import pytest
import yaml

from pytest_practice.calc.calculator import Calculator

with open('calc_data.yml', encoding='utf-8') as f:
    caladatas = yaml.safe_load(f)
    add_data = caladatas['add']['add_data']
    add_myid = caladatas['add']['add_myId']
    div_data = caladatas['div']['div_data']
    div_myid = caladatas['div']['div_myId']


class Test_calc:
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    # 装饰器
    # @pytest.mark.parametrize(
    #     'num1,num2,expect', [
    #         [1, 1, 2],
    #         [0.1, 0.2, 0.3],
    #         [-1, -2, -3]
    #     ], ids=["int", "float", "negative"]
    # )
    @pytest.mark.parametrize(
        'num1, num2, expect', add_data, ids=add_myid
    )
    def test_add(self, num1, num2, expect):
        # 测试加法
        add_result = self.calc.add(num1, num2)
        if isinstance(add_result, float):
            add_result = round(add_result, 2)
        assert add_result == expect

    # def test_add2(self):
    #     result = self.calc.add(0.1, 0.2)
    #     if isinstance(result, float):
    #         result = round(result, 2)
    #     assert result == 0.3
    #
    # def test_add3(self):
    #     result = self.calc.add(-1, -2)
    #     assert result == -3

    @pytest.mark.parametrize(
        "a,b,c", div_data, ids=div_myid
    )
    def test_div(self, a, b, c):
        # 定了除法测试方法
        div_result = self.calc.div(a, b)
        if isinstance(div_result, float):
            div_result = round(div_result, 2)
        assert div_result == c
