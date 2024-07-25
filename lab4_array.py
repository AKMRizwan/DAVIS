import numpy as np
print("\n*********Question :- 1 *************\n")
sales = [200, 300, 400, 500, 600, 700, 800]
sales_array = np.array(sales)
total_sales = np.sum(sales_array)
print("Total Sales:", total_sales)
average_sales = np.mean(sales_array)
print("Average Sales:", average_sales)
sales_variance = np.var(sales_array)
print("Sales Variance:", sales_variance)
print("\n*********Question :- 2 *************\n")
# Temperature data for a week
temps = [
    [15, 22, 18],
    [16, 23, 19],
    [15, 24, 20],
    [17, 22, 18],
    [16, 21, 17],
    [14, 20, 16],
    [13, 19, 15]
]
temps_array = np.array(temps)
print("Temperature Array:\n", temps_array)
monday_temps = temps_array[0]
print("\nMonday's Temperatures:", monday_temps)
afternoon_temps = temps_array[:, 1]
print("\nAfternoon Temperatures for the Week:", afternoon_temps)
wednesday_afternoon_temp = temps_array[2, 1]
print("\nWednesday Afternoon Temperature:", wednesday_afternoon_temp)
reshaped_temps = temps_array.reshape(3, 7)
print("\nReshaped Array (3 rows, 7 columns):\n", reshaped_temps)
flattened_temps = temps_array.flatten()
print("\nFlattened Array:", flattened_temps)
mean_temp = np.mean(temps_array)
print("\nMean Temperature for the Week:", mean_temp)
mean_daily_temps = np.mean(temps_array, axis=1)
print("\nMean Temperature for Each Day:", mean_daily_temps)
temp_variance = np.var(temps_array)
print("\nTemperature Variance for the Week:", temp_variance)
temp_std_dev = np.std(temps_array)
print("\nTemperature Standard Deviation for the Week:", temp_std_dev)
max_temp = np.max(temps_array)
print("\nMaximum Temperature Recorded in the Week:", max_temp)
min_temp = np.min(temps_array)
print("\nMinimum Temperature Recorded in the Week:", min_temp)
