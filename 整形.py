import re


input_string = '#MechJeb_Aircraftauto_title = Aircraft Autopilot'

usiro_pattern = re.compile(r'#.* = (.*)')
usiro_match = usiro_pattern.search(input_string)
mae_pattern = re.compile(r'(#.* = ).*')
mae_match = mae_pattern.search(usiro_match.group(0))
print(usiro_match.group(1))
print(usiro_match.group(0))
print(mae_match.group(1))

