import numpy as np

def generate_vertices(attributes):
    vertices = np.zeros((2**len(attributes), len(attributes)))
    x1_pointer_state = 0
    x2_pointer_state = 0
    x3_pointer_state = 0
    x4_pointer_state = 0
    for i in range(vertices.shape[0]):
        vertices[i][0] = attributes[0][x1_pointer_state]
        vertices[i][1] = attributes[1][x2_pointer_state]
        vertices[i][2] = attributes[2][x3_pointer_state]
        vertices[i][3] = attributes[3][x4_pointer_state]
        x1_pointer_state = 1 - x1_pointer_state
        if (i+1)%2==0:
            x2_pointer_state = 1 - x2_pointer_state
        if (i+1)%4==0:
            x3_pointer_state = 1 - x3_pointer_state
        if (i+1)%8==0:
            x4_pointer_state = 1 - x4_pointer_state
    return vertices

def calculate_intervals(interval_func_y):
    interval_values = np.zeros(interval_func_y.shape[0])
    y_interval = []
    for i in range(interval_func_y.shape[0]):
        attr = interval_func_y[i][:4]
        wts = interval_func_y[i][4:]
        interval_values[i] = sum(attr*wts)/sum(wts)

    y_interval.append(np.min(interval_values))
    y_interval.append(np.max(interval_values))
    
    return y_interval  

x1 = [0.4, 0.6]
x2 = [0.7, 0.96]
x3 = [0.1, 0.3]
x4 = [0.0, 0.2]
w1 = [0.8, 1.0]
w2 = [0.5, 0.9]
w3 = [0.8, 1.0]
w4 = [0.5, 0.9]

x = [x1, x2, x3, x4]
w = [w1, w2, w3, w4]   

attribute_vertices = generate_vertices(x)
weight_vertices = generate_vertices(w)
interval_func_y = np.zeros(((2**len(x))**2, 2*len(x)))
wt_pointer_state = 0
att_pointer_state = 0
for i in range(interval_func_y.shape[0]):
    interval_func_y[i] = np.concatenate((attribute_vertices[att_pointer_state], weight_vertices[wt_pointer_state]))
    if att_pointer_state<attribute_vertices.shape[0]-1:
        att_pointer_state+=1
    else:
        att_pointer_state=0
    if (i+1)%attribute_vertices.shape[0]==0:
        wt_pointer_state+=1

print('Interval of y values : ', calculate_intervals(interval_func_y))