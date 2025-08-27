# Finds the highest frequency element in a list.

x = [1, 2, 3, 4, 3, 5, 6, 3, 7, 8, 3, 3, 9, 10]
highest_freq = max(x, key=x.count)
print("Highest frequency element is:", highest_freq)
frequency = x.count(highest_freq)
print("Frequency is:", frequency)
