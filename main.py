def dict_preparation(book_name):
  with open(book_name, encoding='UTF-8') as file:
    cook_of_dishes = {}
    for line in file:
      dish_name = line[:-1]
      counter = file.readline().strip()
      dishes = []
      for value in range(int(counter)):
        structure_of_dishes = dict.fromkeys(['ingredient_name', 'quantity', 'measure'])
        ingridients = file.readline().strip().split('|')
        for structure in ingridients:
          structure_of_dishes['ingredient_name'] = ingridients[0]
          structure_of_dishes['quantity'] = ingridients[1]
          structure_of_dishes['measure'] = ingridients[2]
        dishes.append(structure_of_dishes)
        cook_book = {dish_name: dishes}
        cook_of_dishes.update(cook_book)
      file.readline()

  return (cook_of_dishes)

print(dict_preparation('cook_book.txt'))


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = dict_preparation('cook_book.txt')
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingridients in cook_book[dish]:
                if ingridients['ingredient_name'] not in shop_list:
                    shop_list[ingridients['ingredient_name']] = {'measure': ingridients['measure'], 'quantity': (int(ingridients['quantity'])*person_count)}
                else:
                    shop_list[ingridients['ingredient_name']]['quantity'] += (int(ingridients['quantity'])*person_count)
    return (shop_list)

print(get_shop_list_by_dishes(['Запеченный картофель','Омлет'], 2))

