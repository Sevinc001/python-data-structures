# Description: Advanced log processing with exception handling to calculate average spam confidence.

filename = input("Please enter file name: ")

try:
    file_handle = open(filename)
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found. Please check the file path.")
    quit()

count = 0
total_price = 0

for line in file_handle:
    if not line.startswith("Product"):
        continue
        
    start_pos = line.find("ce:")
    end_pos = line.find("AZN")
    
    price_string = line[start_pos + 3 : end_pos]
    price_value = float(price_string.strip())
    print(price_value)
    
    count = count + 1
    total_price = total_price + price_value

print("-" * 30)

if count > 0:
    average_price = total_price / count
    print("Average Price:", round(average_price, 2), "AZN")
else:
    print("The file was opened successfully, but no product entries were found.")
