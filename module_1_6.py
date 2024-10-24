# Работа со словарями
my_dict = {'Petr': 1999, 'Anna': 2010, 'Igor': 1958, 'Elza': 2000}
print(my_dict)
print(my_dict['Anna'])
print(my_dict.get('Max', 'Запрашиваемого абонента нет в базе'))
my_dict.update({'Artur': 1995, 'Fedor': 2014})
print(my_dict)
a = my_dict.pop('Igor')
print(a)
print(my_dict)

#Работа с множествами
my_set = {14, 14, False, 14, 14, 3.25, 'Appel', 'Appel', 'Appel', False, 3.25}
print(my_set)
my_set.update({55, True})
print(my_set.remove(14))
print(my_set)