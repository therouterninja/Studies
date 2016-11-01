def add(list, mydict):
  for word in list:
    current_dict = mydict
    for letter in word:
      current_dict = current_dict.setdefault(letter, {})
    current_dict["end"] = True
  return mydict


def get(mystring, mydict):
  """Transverse through nested dict() until it hits rock bottom."""
  current_dict = mydict
  prefix = ""

  for letter in mystring:
    if current_dict.get(letter):
      prefix += letter
      current_dict = current_dict.get(letter)
    else:
      # If at any point this doesn"t match, terminate and return an empty dict()
      return (prefix, {})
  return (prefix, current_dict)


def print_strings(prefix, mydict, current_string=""):
  """Prints flattened strings from a nested dict()."""
  for k, v in mydict.items():
    if k == "end":
      print("".join([prefix, current_string]))
    elif isinstance(v, dict):
      print_strings(prefix, v, current_string=current_string+k)
    else:
      return None


mylist = ["a", "arch", "angst", "ant", "b", "bad"]
mydict = add(mylist, {})
prefix, mydict = get("a", mydict)
print_strings(prefix, mydict)
