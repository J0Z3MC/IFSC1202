total_seconds = int(input("Enter Length of Time in Seconds: "))

years = total_seconds // 31536000 
remaining_seconds = total_seconds % 31536000

days = remaining_seconds // 86400 
remaining_seconds = remaining_seconds % 86400

hours = remaining_seconds // 3600
remaining_seconds = remaining_seconds % 3600

minutes = remaining_seconds // 60 
remaining_seconds = remaining_seconds % 60

seconds = remaining_seconds

print("Years:", years)
print("Days:", days)
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)