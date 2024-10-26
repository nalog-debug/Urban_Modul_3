def print_params(a=1, b='строка', c=True, ):
    print(a, b, c)


print_params()
print_params(1, 2)
print_params(5, 6, 8)
print_params(8, 'play', False)
print_params(b=25, c=[1, 2, 3])

values_list = [1, 'two', True]
values_dict = {'a': 2, 'b': 'stop', 'c': False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [True, 88]
print_params(*values_list_2, 42)
