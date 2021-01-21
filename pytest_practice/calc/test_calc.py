"""

    补全计算器（加减乘除）的测试用例
    使用数据的数据驱动，完成加减乘除用例的自动生成
    创建 fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
    控制测试用例顺序按照【加-减-乘-除】这个顺序执行
    结合allure 生成测试结果报告
"""
import allure
import pytest


@allure.feature('测试计算器')
class Test_calc:

    @pytest.mark.run(order=1)  # 按照顺序执行测试用例
    @allure.story("测试加法")
    def test_add(self, get_calc, get_add_datas):
        # 验证加法测试案例
        add_result = None
        try:
            add_result = get_calc.add(get_add_datas[0], get_add_datas[1])
            if isinstance(add_result, float):
                add_result = round(add_result, 2)
        except Exception as e:
            print(e)

        assert add_result == get_add_datas[2]

    @pytest.mark.run(order=2)  # 按照顺序执行测试用例
    @allure.story("测试减法")
    def test_sub(self, get_calc, get_sub_datas):
        # 验证减法
        sub_result = None
        try:
            sub_result = get_calc.sub(get_sub_datas[0], get_sub_datas[1])
            if isinstance(sub_result, float):
                sub_result = round(sub_result, 2)
        except Exception as e:
            print(e)

        assert sub_result == get_sub_datas[2]

    @pytest.mark.run(order=3)  # 按照顺序执行测试用例
    @allure.story("测试乘法")
    def test_mul(self, get_calc, get_mul_datas):
        mul_result = None
        try:
            mul_result = get_calc.mul(get_mul_datas[0], get_mul_datas[1])
            if isinstance(mul_result, float):
                mul_result = round(mul_result, 2)
        except Exception as e:
            print(e)
        assert mul_result == get_mul_datas[2]

    @pytest.mark.run(order=4)  # 按照顺序执行测试用例
    @allure.story("测试除法")
    def test_div(self, get_calc, get_div_datas):
        # 验证除法
        div_result = None
        try:
            div_result = get_calc.div(get_div_datas[0], get_div_datas[1])
            if isinstance(div_result, float):
                div_result = round(div_result, 2)
        except Exception as e:
            print(e)
        assert div_result == get_div_datas[2]
