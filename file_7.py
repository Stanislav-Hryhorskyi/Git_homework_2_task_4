'''
Program for calculating travel
time from point A to B
'''

lenght = 700   # km
velocity = 90  # km/h
time = lenght/velocity

print(f'Travel time from point A to B '
      f'in hours (precision one decimal place): '
      f'time = {time:.1f} hours')

print(f'Travel time from point A to B '
      f'in minutes (precision one decimal place): '
      f'time = {(time*60):.1f} minutes')

print(f'Travel time from point A to B '
      f'in seconds (precision one decimal place): '
      f'time = {(time*3600):.1f} seconds')

hours = (time*3600) // 3600
minutes = ((time*3600) % 3600) // 60
seconds = ((time*3600) % 3600) % 60
print(f'Travel time from point A to B '
      f'(notation in clock format): '
      f'time = {time:.0f} hours: {minutes:.0f} minutes: {seconds:.0f} seconds')

