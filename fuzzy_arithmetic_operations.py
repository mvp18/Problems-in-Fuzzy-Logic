import numpy as np
import matplotlib.pyplot as plt

print('\nThis program can perform 4 basic arithmetic operations between 2 fuzzy numbers.')

print('\nPlease choose among the following :"add", "subtract", "multiply" and "divide".')

operation = input("\nWhat operation do you want to perform? ")

print('\nNow input the 2 fuzzy numbers.')

i1_left = float(input("Lower Limit of fuzzy number 1 : "))
i1_peak = float(input("Peak of fuzzy number 1 : "))
i1_right = float(input("Upper Limit of fuzzy number 1 : "))
i2_left = float(input("Lower Limit of fuzzy number 2 : "))
i2_peak = float(input("Peak of fuzzy number 2 : "))
i2_right = float(input("Upper Limit of fuzzy number 2 : "))

i1_x = [i1_left, i1_peak, i1_right]
i2_x = [i2_left, i2_peak, i2_right]
i1_y = [0,1,0]

if operation == 'add' or operation == 'subtract':

	if operation == 'add':
	    out_left = i1_left+i2_left
	    out_right = i1_right+i2_right
	    out_peak = i1_peak+i2_peak
	elif operation=='subtract':
	    out_left = i1_left-i2_right
	    out_right = i1_right-i2_left
	    out_peak = i1_peak-i2_peak

	out_x = []
	out_y = [0,1,0]
	out_x.append(out_left)
	out_x.append(out_peak)
	out_x.append(out_right)

def create_arrays(peak, left, right):
    x_arr = np.zeros(21)
    y_arr = np.zeros(21)
    lower_range = peak-left
    inc_lower = lower_range/10
    upper_range = right-peak
    inc_upper = upper_range/10
    for i in range(21):
        if i<=10:
            x_arr[i] = left+i*inc_lower
            y_arr[i] = i/10
        else:
            x_arr[i] = peak+(i-10)*inc_upper
            y_arr[i] = 2-i/10
    return x_arr, y_arr

def find_intervals(x_arr):
    intervals_list = []
    for i in range(11):
        if i!=10:
            intervals_list.append([x_arr[i], x_arr[len(x_arr)-i-1]])
        else:
            intervals_list.append(x_arr[len(x_arr)//2])
    return intervals_list

def compute_output_intervals(operation, x1, x2):
    interval_list1 = find_intervals(x1)
    interval_list2 = find_intervals(x2)
    output_intervals = []
    for i in range(len(interval_list1)):
        interval_x1 = interval_list1[i]
        interval_x2 = interval_list2[i]
        if type(interval_x1)==list:
            if operation=='multiply':
                out_lower = min(interval_x1[0]*interval_x2[0], interval_x1[0]*interval_x2[1], interval_x1[1]*interval_x2[0], interval_x1[1]*interval_x2[1])
                out_upper = max(interval_x1[0]*interval_x2[0], interval_x1[0]*interval_x2[1], interval_x1[1]*interval_x2[0], interval_x1[1]*interval_x2[1])
            elif operation=='divide':
                out_lower = min((interval_x1[0]/interval_x2[0]), (interval_x1[0]/interval_x2[1]), (interval_x1[1]/interval_x2[0]), (interval_x1[1]/interval_x2[1]))
                out_upper = max((interval_x1[0]/interval_x2[0]), (interval_x1[0]/interval_x2[1]), (interval_x1[1]/interval_x2[0]), (interval_x1[1]/interval_x2[1]))
            output_intervals.append([out_lower, out_upper])
        else:
            if operation=='multiply':
                output_intervals.append(interval_x1*interval_x2)
            elif operation=='divide':
                output_intervals.append(interval_x1/interval_x2)
                
    return output_intervals

def create_output_arrays(output_intervals):
    out_x = np.zeros(21)
    for i in range(len(output_intervals)):
        if i!=len(output_intervals)-1:
            out_x[i] = output_intervals[i][0]
            out_x[21-i-1] = output_intervals[i][1]
        else:
            out_x[i] = output_intervals[i]
    return out_x

if operation=='multiply' or operation=='divide':

	x1, y1 = create_arrays(i1_peak, i1_left, i1_right)
	x2, y2 = create_arrays(i2_peak, i2_left, i2_right)
	output_intervals = compute_output_intervals(operation, x1, x2)
	out_x = create_output_arrays(output_intervals)
	out_y = y1

plt.plot(i1_x, i1_y, label = 'A')
plt.plot(i2_x, i1_y, label = 'B')
plt.plot(out_x, out_y, label = 'Output')
plt.xlabel('x')
plt.ylabel('Membership value')
plt.legend(loc='upper right')
plt.show()