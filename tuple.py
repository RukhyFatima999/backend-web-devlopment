def convert_sec(seconds):
 hours =seconds // 3600
 minutes=(seconds- hours * 3600) // 60
 remainind_sec=seconds - hours * 3600 - minutes * 60
 return hours, minutes, remainind_sec
result = convert_sec(5000)
print (result)

