cook_book = {}
with open (r"C:\Users\alfa18\Desktop\hw\recipes\recipes.txt", "r", encoding="utf-8") as f:
    while True:
        key_1 = f.readline().strip()
        v_ingr = f.readline().strip()
        if v_ingr == "":
          break
        counter = int(v_ingr)
        for i in range (0, counter):
            f_str = f.readline().strip().split(" | ")
            #print (f_str)
            value = {}
            value['ingredient_name'] = f_str[0]
            value['quantity'] = f_str[1]
            value['measure'] = f_str[2]
            if key_1 in cook_book:
                cook_book[key_1].append(value)
            else:
                cook_book[key_1] = [value]
        f.readline()
        
print(cook_book)


def get_shop_list_by_dishes(dishes, person_quant):
    grocery_dict = {}  
    for _dish in dishes:
        for ingredient in cook_book[_dish]:
            ingredient_list = dict([(ingredient['ingredient_name'],
                                     {'quantity': int(ingredient['quantity']) * person_quant,
                                      'measure': ingredient['measure']})])
            if grocery_dict.get(ingredient['ingredient_name']) == 'None':
                _plus = (int(grocery_dict[ingredient['ingredient_name']]['quantity']) +
                           int(ingredient_list[ingredient['ingredient_name']]['quantity']))
                grocery_dict[ingredient['ingredient_name']]['quantity'] = _plus
            else:
                grocery_dict.update(ingredient_list)
    for key, value in grocery_dict.items():
        print(key, ' : ', value)
    return grocery_dict


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос', 'Омлет', 'Запеченный картофель'], 5)