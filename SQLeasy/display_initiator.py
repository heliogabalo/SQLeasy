import SQLeasy
# import pdb


def counter_iterator(x):
  while True:
    yield x
    x = x + 1


def list_fn(n):
  with open('modAttr.py', mode="w", encoding="utf-8") as file:
    functions = dir(SQLeasy)
    counter = counter_iterator(n)
    for fn in functions:
      file.write('{} {}()\n'.format(next(counter), fn))

list_fn(1)



def display_options():
  functions = dir()
  counter = counter_iterator(1)
  next(counter)

  a_list = []
  with open('modAttr.py', mode="r", encoding="utf-8") as pattern_file:
    for line in pattern_file:
      string = line.split(None, 2)
      a_list.append(string)
  # a_list
  result = dict(a_list)
  return result
  # print(result)

display_options()

# Calling options from  is local from the function perspective(init_app) and
# global from the module.
# options = display_options()
# test_con = options['31']
# exec(test_con)

# small and medium enterprises,




# known_call: connection = connect_to_database()
# pattern: name args
#   if job[num]
#     - check for imports
#     - identify query and pass it as required args
#     - build the calls
#     - name(connection, builder(num))



# with open('modAttr.py', mode="r", encoding="utf-8") as pattern_file:
#   for line in pattern_file:
#     num, fn = line.split(None, 2)
#     a_list.append(num, fn)

# def example_d():
#   with open('modAttr.py', mode="r", encoding="utf-8") as file:
#     a_dict = {}
#     # empaquetado = [des, emp, aquet, ado]
#     for num, fn in file:
#       a_dict[num] = fn
#
#   print(a_dict)

# if job in list:
#   call(list[job])
#
# my_dict = {n: fn}
# a_dict = dict(a_list_of_lists)
#

# def dontUseThis():
#   job = input('>>> ')
#   if not isinstance(job, str):
#      print('Invalid entry...')
#   if (job == '1'):
#     test_connection()
# def dontUseNeither():
#   jobs = input('>>> ')
#   for n in jobs:
#     job = n
#     trigrer_fn()
# def my_fn(n):
#   with open('modAttr.py', mode="w", encoding="utf-8") as file:
#     functions = dir()
#     for fn in functions:
#       file.write('\t' + fn + '()\n')



# pdb.run('example_d()')
