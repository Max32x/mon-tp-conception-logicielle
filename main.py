from datetime import datetime


current_time = datetime.now()

current_time_formatted = current_time.strftime("%H:%M:%S")

print(current_time_formatted)