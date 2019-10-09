import random


class _Faker:
    clothes = ["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"]
    drinks = ["可乐", "雪碧", "橙汁", "绿茶", "奶茶", "百威", "青岛"]
    phones = ["小米", "三星", "华为", "苹果", "魅族", "VIVO", "OPPO"]
    fruits = ["草莓", "芒果", "葡萄", "雪梨", "西瓜", "柠檬", "车厘子"]
    animal = ["河马", "蟒蛇", "老虎", "大象", "兔子", "熊猫", "狮子"]
    cars = ["宝马", "法拉利", "奔驰", "奥迪", "大众", "丰田", "特斯拉"]
    dogs = ["哈士奇", "萨摩耶", "泰迪", "金毛", "牧羊犬", "吉娃娃", "柯基"]
    week = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    week_en = "Saturday Friday Thursday Wednesday Tuesday Monday Sunday".split()
    colors = [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
    ]

    def choose(self) -> list:
        return random.choice(
            [
                self.clothes,
                self.drinks,
                self.phones,
                self.fruits,
                self.animal,
                self.dogs,
                self.week,
            ]
        )

    @staticmethod
    def values(start: int = 20, end: int = 150) -> list:
        return [random.randint(start, end) for _ in range(7)]


Faker = _Faker()
