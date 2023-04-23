import re
command = re.compile(r'#.* = (.*)')
with open('text.txt') as f:
    for line in f:
      try:
        match = command.search(line).group(1)
      except AttributeError:
        match = line
      print(match)