# 1. Min, Avg, Max
# Write a function get_min_avg_max (sequence) that returns a tuple with three values, the smallest, the arithmetic mean, and the largest value in the string, respectively.
# Example:
# get_min_avg_max ([0,10,1,9]) -> (0,5,10)
# the incoming sequence can be a tuple or a list with numeric values.
import statistics
def get_min_avg_max(sequence):
    return (min(sequence), statistics.mean(sequence),  max(sequence))

list = [2, 9, 3,2,5,1]
print(get_min_avg_max(list))