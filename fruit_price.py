
def fruit_price():
    
    fruits = {
        "柿子": 4,
        "苹果": 5,
        "进口苹果": 10,
        "阳光玫瑰葡萄": 6,
        "车厘子樱桃": 40,
        "菠萝": 3,
        "麒麟西瓜": 3,
        "圣女果": 6,
        "库尔勒香梨": 4,
        "热带香蕉": 3,
        "湖南麻阳橙子": 5,
        "哈密瓜": 8,
        "金枕榴莲": 50
    }
    
    print("=== 水果价格查询 ===")

    print("\n可选水果:\n")

    for fruit in fruits:
        print(str(fruit))

    print("\n\n暂时未上架的水果有：芒果")
    
    fruit_name = input("\n\n请输入水果名称: ")
    
    if fruit_name in fruits:
        price = fruits[fruit_name]
        print(str(fruit_name)+"的单价是: "+str(price)+"元/斤")
    elif fruit_name=="芒果":
        print("抱歉！该水果暂时未上架，请查询别的水果。")
    else:
        print("抱歉，没有找到"+fruit_name+"的价格信息, 请重新输入。")
     
    print("\n可选水果:\n")
    for fruit in fruits:
        print(str(fruit))

fruit_price()
