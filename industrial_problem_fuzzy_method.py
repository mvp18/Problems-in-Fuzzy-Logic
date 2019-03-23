import numpy as np
import matplotlib.pyplot as plt

weights = {'pressure':0.5, 'temperature':0.25, 'flow':0.25}

pr_max = 8
temp_max = 800
flow_max = 80

print('Enter limits of pressure parameter (max value : 8) : ')
p_left = float(input('Enter lower limit : '))
p_peak = float(input('Enter peak : '))
p_right = float(input('Enter upper limit : '))

print('Enter limits of temperature parameter (max value : 800) : ')
t_left = float(input('Enter lower limit : '))
t_peak = float(input('Enter peak : '))
t_right = float(input('Enter upper limit : '))

print('Enter limits of flow rate parameter (max value : 80) : ')
f_left = float(input('Enter lower limit : '))
f_peak = float(input('Enter peak : '))
f_right = float(input('Enter upper limit : '))

pressure = np.array([p_left, p_peak, p_right])
temperature = np.array([t_left, t_peak, t_right])
flow_rate = np.array([f_left, f_peak, f_right])

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

def find_mode_membership(mode):
    pr_memb = pressure_membership_func[mode['pressure']]
    temp_memb = temperature_membership_func[mode['temperature']]
    flow_memb = flow_membership_func[mode['flow']]
    mode_lower = pr_memb[0]*weights['pressure']+temp_memb[0]*weights['temperature']+flow_memb[0]*weights['flow']
    mode_peak = pr_memb[1]*weights['pressure']+temp_memb[1]*weights['temperature']+flow_memb[1]*weights['flow']
    mode_upper = pr_memb[2]*weights['pressure']+temp_memb[2]*weights['temperature']+flow_memb[2]*weights['flow']
    mode_memb = [mode_lower, mode_peak, mode_upper]
    return mode_memb

def actual_mode_membership(pr, temp, flow):
    mode_lower = pr[0]*weights['pressure']+temp[0]*weights['temperature']+flow[0]*weights['flow']
    mode_peak = pr[1]*weights['pressure']+temp[1]*weights['temperature']+flow[1]*weights['flow']
    mode_upper = pr[2]*weights['pressure']+temp[2]*weights['temperature']+flow[2]*weights['flow']
    mode_memb = [mode_lower, mode_peak, mode_upper]
    return mode_memb

def evaluate(memb_func):
    pseudo_exp = (memb_func[2]-memb_func[0])*(memb_func[0]+memb_func[1]+memb_func[2])/6
    return pseudo_exp

pseudo_exp_actual_mode = evaluate(actual_mode_membership(pr, temp, flow))
pseduo_exp_autoclaving = evaluate(find_mode_membership(autoclaving))
pseduo_exp_annealing = evaluate(find_mode_membership(annealing))
pseduo_exp_sintering = evaluate(find_mode_membership(sintering))
pseduo_exp_transport = evaluate(find_mode_membership(transport))
pseudo_exp_list = [pseduo_exp_autoclaving, pseduo_exp_annealing, pseduo_exp_sintering, pseduo_exp_transport]

min_index = (np.abs(pseudo_exp_list-pseudo_exp_actual_mode)).argmin()

modes = ['autoclaving', 'annealing', 'sintering', 'transport']

print('The process is {}'.format(modes[min_index]))