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

# list_fn(1)



def display_options():
  """
  This is the documentation for the display_options function.
  """
  # functions = dir()
  counter = counter_iterator(1)
  next(counter)
  a_list = []
  with open('modAttr.py', mode="r", encoding="utf-8") as pattern_file:
    for line in pattern_file:
      string = line.split(None, 2)
      a_list.append(string)

  result = dict(a_list)
  return result
