import numpy as np

state_set = ['AMZN', 'GOOG', 'FB']
action_set = ['b', 'h', 's'] # 'b', 'h', and 's' means buy, hold, sell, respectively

num_states = len(state_set)
num_actions = len(action_set)

state_transition_probability = {

    ### Amazon
    'AMZN_b': [0.2, 0.55, 0.25],
    'AMZN_h': [0.66, 0.3, 0.04],
    'AMZN_s': [0.25, 0.21, 0.54],
    
    ### Google
    'GOOG_b': [0.1, 0.6, 0.3],
    'GOOG_h': [0.2, 0.1, 0.7],
    'GOOG_s': [0.6, 0.2, 0.2],
    
    ### Facebook
    'FB_b': [0.2, 0.55, 0.25],
    'FB_h': [0.11, 0.15, 0.74],
    'FB_s': [0.69, 0.2, 0.11]
    
}

def initial_state():
    return np.random.choice(state_set, size=None) # initial state using uniform distribution

def reward_function(state_next, action_curr):
    
    if state_next==state_set[0]: # Amazon
        reward_next = np.random.normal(loc=40, scale=1, size=1)
        
        reward_next = np.random.normal(loc=0.4, scale=0.1, size=1)*reward_next
        if action_curr == 'b': 
            reward_next = - reward_next # leads to loss
        
    elif state_next==state_set[1]: # Google
        reward_next = np.random.normal(loc=60, scale=1, size=1)
        
        reward_next = np.random.normal(loc=-0.3, scale=0.1, size=1)*reward_next
        if action_curr == 'b': 
            reward_next = - reward_next # leads to gain
        
    else: # Facebook
        reward_next = np.random.normal(loc=30, scale=1, size=1)

        reward_next = np.random.normal(loc=0.1, scale=0.1, size=1)*reward_next
        if action_curr == 'b': 
            reward_next = - reward_next # leads to loss
            
    ###################### 
        
    if action_curr == 'h':
        reward_next = 0 # there is no reword if you hold your stock (do not buy of sell)
        
    
    
    return reward_next

def take_action_by_human():
    
    while True:
        a = input()
        is_valid_action = (a in action_set)
        if is_valid_action:
            break
        else:
            print('Action can only be chosen from: ', action_set)
            
    return a

def environment_response(state_curr, action_curr):
    
    stp = state_transition_probability[state_curr+'_'+action_curr]

    state_next = np.random.choice(state_set, size=None, p=stp)

    reward_next = reward_function(state_next=state_next, action_curr=action_curr)
    
    return state_next, reward_next

def print_and_log_string(file_handle, string):
    print(string)
    file_handle.write(string)

