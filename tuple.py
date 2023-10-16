def convert_sec(seconds):
 hours =seconds // 3600
 minutes=(seconds- hours * 3600) // 60
 remainind_sec=seconds - hours * 3600 - minutes * 60
 return hours, minutes, remainind_sec
hours,minutes,seconds = convert_sec(1000)
print (hours, minutes,seconds)
