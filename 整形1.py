import re


#input_string = '#MechJeb_Aircraftauto_title = Aircraft Autopilot\n#MechJeb_Aircraftauto_button1 = Disengage autopilot\n'
input_string = 'jijikon'
pattern = re.compile(r'#.* = (.*)')
try:
   match = pattern.search(input_string).group(1)
except AttributeError:
   match = input_string
print(match)
