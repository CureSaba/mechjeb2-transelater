import re
from googletrans import Translator
translator = Translator()
command1 = re.compile(r'( .*#.* = ).*')
command2 = re.compile(r'#.* = (.*)')
a = 1
to = input("Translate to: ")
with open('en-us.cfg', encoding="utf-8") as f:
  f2 = open(to+".cfg", "w", encoding="utf-8")
  for line in f:
    if a!=3:
      try:
        match1 = command1.search(line).group(1)
      except AttributeError:
        match1 = line
      try:
        match2 = command2.search(line).group(1)
        match2 = translator.translate(match2, dest=to)
        match2 = match2.text
      except AttributeError:
        match2 = None
      try:
        f2.write(match1+match2+"\n")
      except TypeError:
        f2.write(match1+"\n")
    else:
      f2.write(line.replace("en-us", to)+"\n")
    print(a)
    a = a+1
  print("It's done")
  f2.close()    