import numpy as np



def PID_controller(cur_angles, target_angles, target_velocities=0.1):
        target_angles = target_angles.reshape((-1, 1))
    
        q = cur_angles.reshape((-1, 1))
    
        kp = 5
    
        Kp = np.diag(np.ones(q.shape[0]) * kp)
    
        action = Kp.dot(target_angles - q)
    
        action = np.clip(action, -1, 1)
        action = np.array(action)
    
        return action.reshape((1, -1))[0]
        