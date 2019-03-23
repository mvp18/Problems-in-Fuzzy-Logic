import numpy as np
import matplotlib.pyplot as plt

weights = {'pressure':0.5, 'temperature':0.25, 'flow':0.25}

pr_max = 8
temp_max = 800
flow_max = 80

pressure = float(input('Enter pressure value (max value : 8): '))
temperature = float(input('Enter temperature value (max value : 800): '))
flow_rate = float(input('Enter flow value (max value : 80): '))

pr = pressure/pr_max
temp = temperature/temp_max
flow = flow_rate/flow_max

pressure_membership_func = {'z':[0, 0, 0.5], 'l':[0, 0.5, 1], 'h':[0.5, 1, 1]}
temperature_membership_func = {'z':[0, 0, 0.25], 'l':[0, 0.25, 0.5], 'h':[0.25, 1, 1]}
flow_membership_func = {'z':[0, 0, 0.125], 'l':[0, 0.125, 0.25], 'h':[0.125, 1, 1]}

autoclaving = {'pressure':'h', 'temperature':'h', 'flow':'z'}
annealing = {'pressure':'h', 'temperature':'l', 'flow':'z'}
sintering = {'pressure':'l', 'temperature':'z', 'flow':'l'}
transport = {'pressure':'z', 'temperature':'z', 'flow':'h'}

def find_membership_value(val, param, mode, param_memb):
    memb_func = mode[param]
    memb_func_x_values = param_memb[memb_func]
    if (val==memb_func_x_values[0] and val==memb_func_x_values[1]) or (val==memb_func_x_values[1] and val==memb_func_x_values[2]) or val==memb_func_x_values[1]:
        memb_value = 1
    if (val==memb_func_x_values[0] and val!=memb_func_x_values[1]) or (val!=memb_func_x_values[1] and val==memb_func_x_values[2]):
        memb_value = 0
    if val<memb_func_x_values[0] or val>memb_func_x_values[2]:
        memb_value = 0
    elif memb_func_x_values[0]<val<memb_func_x_values[1]:
        memb_value = (val-memb_func_x_values[0])/(memb_func_x_values[1]-memb_func_x_values[0])
    elif memb_func_x_values[1]<val<memb_func_x_values[2]:
        memb_value = 1-(val-memb_func_x_values[1])/(memb_func_x_values[2]-memb_func_x_values[1])
    return memb_value

def find_mode_membership(mode, pr, temp, flow):
    pr_memb_value = find_membership_value(pr, 'pressure', mode, pressure_membership_func)
    temp_memb_value = find_membership_value(temp, 'temperature', mode, temperature_membership_func)
    flow_memb_value = find_membership_value(flow, 'flow', mode, flow_membership_func)
    mode_membership = pr_memb_value*weights['pressure']+temp_memb_value*weights['temperature']+flow_memb_value*weights['flow']
    return mode_membership

modes = ['autoclaving', 'annealing', 'sintering', 'transport']
mode_memberships = []
mode_memberships.append(find_mode_membership(autoclaving, pr, temp, flow))
mode_memberships.append(find_mode_membership(annealing, pr, temp, flow))
mode_memberships.append(find_mode_membership(sintering, pr, temp, flow))
mode_memberships.append(find_mode_membership(transport, pr, temp, flow))

max_index = np.argmax(mode_memberships)

print('The process is {}'.format(modes[max_index]))