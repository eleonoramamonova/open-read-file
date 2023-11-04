# import os
# from pprint import pprint
#
# path = os.path.join(os.getcwd(), 'recipes.txt')
# with open(path, encoding='utf-8') as recipes:
#     cook_book = {}
#     for recipe in recipes:
#         dish = recipe.strip()
#         ing_count = int(recipes.readline().strip())
#         book_dict = []
#         for item in range(ing_count):
#             ingredient_name, quantity, measure = recipes.readline().strip().split('|')
#             book_dict.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
#         cook_book[dish] = book_dict
#         recipes.readline()
#
# def get_shop_list_by_dishes(dishes, person_count):
#     grocery_dict = {}
#     for dish1 in dishes:
#         for ingredient in cook_book[dish1]:
#             food_dict = {}
#             if ingredient['ingredient_name'] not in grocery_dict:
#                 food_dict['measure'] = ingredient['measure']
#                 food_dict['quantity'] = int(ingredient['quantity']) * person_count
#                 grocery_dict[ingredient['ingredient_name']] = food_dict
#             else:
#                 grocery_dict[ingredient['ingredient_name']]['quantity'] = int(grocery_dict[ingredient['ingredient_name']]['quantity']) + \
#                                                                            int(ingredient['quantity']) * person_count
#     return grocery_dict
#
# pprint(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2))




file_name = ['1.txt', '2.txt', '3.txt']
file_path = [r"t\1.txt", r"t\2.txt", r"t\3.txt"]
contents = []
for file, path in zip(file_name, file_path):
    with open(path, 'r', encoding="utf-8") as f:
        lines = f.readlines()
        contents.append((file, len(lines), lines))
contents.sort(key=lambda x: x[1])
with open('all.txt', 'w', encoding="utf-8") as f:
    for item in contents:
        f.write(f'{item[0]}\n{item[1]}\n')
        f.writelines(item[2])
        f.write('\n')





