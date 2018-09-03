import numpy as np


def rollout(env, policy, max_steps=100, render=False):
    """Generate one trajectory , return transitions

    data : D+E+1
    {state * D, action * E, cost *1 }

    """
    s = env.reset()

    data = []
    for _ in range(max_steps):
        if render:
            env.render()

        # Select an action by policy
        a = policy(s)
        
        # excuate action
        s_next, reward, done, _ = env.step(a)
      
        # Record data
        data.append(np.concatenate([s , a , s_next, np.array([reward])]))
        
        # break if done
        if done:
            break
        # Update s as s_next for recording next transition
        s = s_next
    
    return np.array(data)