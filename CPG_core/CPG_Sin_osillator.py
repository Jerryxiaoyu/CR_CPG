from math import pi, cos, sin



class sin_oscillator(object):
    def __init__(self, kf=1):
        # Set up the oscillator constants
        self.tau =kf
 
        self.a1 = 1.0
        self.v1 = 1.0
 
        # Step time
        self.dt = 0.01
    
    def oscillator_fun(self, R1, X1, f12 ,   w_0, u1, u2,  r1, r2  ):
        """
        Calculates the state variables in the next time step
        """

        d_u1_dt = (2 * pi * self.v1 + w_0 * r2 * sin(u2 - u1 - f12)) / self.tau

        r1_dt = self.a1 * (R1 - r1)
        
        u1 += d_u1_dt * self.dt
        r1 += r1_dt * self.dt

        o = r1 * sin(u1) + X1
        
 
        return o, u1, r1
    
 
    
class CPG_Sinneutron(object):
    def __init__(self, id, master_nuron, param ,kf=1, w_ms = 1):
        self.id = id
        self.parm = {'kf': kf, 'u1':param[0],   'r1':param[1],
                      'o':param[2], 'R1':param[3], 'X1':param[4],'f12':param[5],}
         
        self.w_ms =w_ms

        osillator = sin_oscillator(self.parm['kf'])
        self.osillator_fun = osillator.oscillator_fun

        self.master_nuron = master_nuron
        
        
    def next_output(self,  f1, f2  ):
        
        if self.master_nuron is not None:
            u2 =  self.master_nuron.parm['u1']
            r2 =  self.master_nuron.parm['r1']
        else:
            u2 = 0
            r2 = 0
            
        
        self.parm['o'],self.parm['u1'], self.parm['r1']  = \
            self.osillator_fun(self.parm['R1'],self.parm['X1'], self.parm['f12'], self.w_ms, self.parm['u1'], u2, self.parm['r1'], r2 )
        
  