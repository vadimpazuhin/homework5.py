immutable_var = 1,2,3,'string',True
print('Immutable tuple:',immutable_var)
#immutable_var[0] = 100
#print(immutable_var)
mutable_list = [1,2,3,'string',True]
mutable_list[0] = 'modified'
print('Mutable list:',mutable_list)