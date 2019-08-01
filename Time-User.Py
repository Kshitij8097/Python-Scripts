#Get Seconds from User and convert into Days, hour, Minute and seconds
str_seconds = input("Please enter the number of seconds you wish to convert")
total_secs = int(str_seconds)

days=total_secs // (3600 * 24)
secs_remaining = total_secs % (3600 * 24)
hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
minutes =  secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining  % 60

print("days=" if days > 0 else "day=",days, "Hrs=", hours, "mins=", minutes, "secs=", secs_finally_remaining)
#print(f"days={days} if {days > 0} else day={day}, Hrs={hours}, Minutes={minutes},seconds={secs_finally_remaining}")
