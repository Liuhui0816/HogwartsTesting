"""
python实战.第二次作业,
动物
"""

# 定义了Animal类
import yaml


class Animal:
    # 定义了属性名称，颜色，年龄，性别
    name: str = ''
    color: str = ''
    age: int = 1
    sex: str = 'male'

    def __init__(self, name, color, age, sex):
        #  内置函数
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    def cry(self):
        # 定义了方法cry
        print(f'{self.name} can crying')

    def run(self):
        # 定义了方法run
        print(f'{self.name} can running')


class Cat(Animal):
    def __init__(self, hair, name, color, age, sex):
        self.hair = hair
        super().__init__(name, color, age, sex)

    def cat_skill(self):
        print(f'{self.name} can catch  mouse')

    def cat_cry(self):
        # super().cry()
        print(f"{self.name} can miamiaojiao")


# 创建子类【狗】，继承【动物类】，
class Dog(Animal):
    # 复写父类的__init__方法，继承父类的属性，
    def __init__(self, hair, name, color, age, sex):
        super().__init__(name, color, age, sex)
        self.hair = hair

    def dog_skill(self):
        # 添加一个新的方法， 会看家，
        print(f"{self.name} can look after the house")

    def dog_cry(self):
        # 复写父类的【会叫】的方法，改成【汪汪叫】
        # super().cry()
        print(f"{self.name} can wangwangjiao")


if __name__ == '__main__':
    cat = Cat('short', 'BlueCat', 'white', 1, 'female')
    print("猫猫的特征如下：")
    cat.cat_skill()
    cat.cat_cry()
    print(cat.name)
    print(cat.color)
    print(cat.age)
    print(cat.sex)
    # dog = Dog('long', 'Golden Retriever', 'golden', '5', 'fale')
    # dog.dog_skill()
    # print(dog.name)
    # print(dog.color)
    # print(dog.age)
    # print(dog.sex)
    # print(dog.hair)

    with open('animal.yml', encoding='utf-8') as f:
        animal_data = yaml.safe_load(f)  # yaml.safe_load()将yaml数据流转程json对象
        print(animal_data)
        dog = Dog(animal_data['dog']['hair'], animal_data['dog']['name'], animal_data['dog']['color'],
                  animal_data['dog']['age'], animal_data['dog']['sex'])
        print("狗狗的特征如下：")
        dog.dog_skill()
        print(dog.name)
        print(dog.color)
        print(dog.age)
        print(dog.sex)
        print(dog.hair)
