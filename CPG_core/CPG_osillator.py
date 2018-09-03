from math import pi, cos, sin

class matsuoka_oscillator(object):
    def __init__(self, kf=1):
        
        # Set up the oscillator constants
        self.tau = 0.2800
        self.tau_prime = 0.4977
        self.beta = 2.5000
        self.w_0 = 2.2829
        self.u_e = 0.4111
        self.m1 = 1.0
        self.m2 = 1.0
        self.a = 1.0
    
        # Modify the time constants based on kf
        self.tau *= kf
        self.tau_prime *= kf
    
        # Step time
        self.dt = 0.01

    def oscillator_fun(self, u1, u2, v1, v2, y1, y2, f1, f2, s1, s2, bias, gain ):
        """
        Calculates the state variables in the next time step
        """
        d_u1_dt = (-u1 - self.w_0 *y2 -self.beta * v1 + self.u_e + f1 + self.a * s1) / self.tau
        d_v1_dt = (-v1 + y1) / self.tau_prime
        y1 = max([0.0, u1])
        
        d_u2_dt = (-u2 - self.w_0 * y1 - self.beta * v2 + self.u_e + f2 + self.a * s2) / self.tau
        d_v2_dt = (-v2 + y2) / self.tau_prime
        y2 = max([0.0, u2])
        
        u1 += d_u1_dt * self.dt
        u2 += d_u2_dt * self.dt
        v1 += d_v1_dt * self.dt
        v2 += d_v2_dt * self.dt
        
        o = bias + gain * (-self.m1 * y1 + self.m2 * y2)
        
        return u1, u2, v1, v2, y1, y2, o

 
    
    
    
class CPG_neutron(object):
    def __init__(self, id, master_nuron, param ,kf=1, w_ms = 1):
        self.id = id
        self.parm = {'kf': kf, 'u1':param[0], 'u2':param[1], 'v1':param[2], 'v2':param[3],
                     'y1':param[4], 'y2':param[5], 'o':param[6], 'gain':param[7], 'bias':param[8]}
        self.w_ms = w_ms
        

        osillator = matsuoka_oscillator(self.parm['kf'])
        self.osillator_fun = osillator.oscillator_fun

        self.master_nuron = master_nuron
        
        
    def next_output(self,  f1, f2  ):
        
        if self.master_nuron is not None:
            s1 = self.w_ms * self.master_nuron.parm['u1']
            s2 = self.w_ms * self.master_nuron.parm['u2']
        else:
            s1 = 0
            s2 = 0
        
        self.parm['u1'],self.parm['u2'], self.parm['v1'], self.parm['v2'], self.parm['y1'], self.parm['y2'], self.parm['o'] = \
            self.osillator_fun(self.parm['u1'],self.parm['u2'], self.parm['v1'], self.parm['v2'], self.parm['y1'], self.parm['y2'],
                               f1, f2, s1, s2, self.parm['bias'], self.parm['gain'] )
        
    

def build_CPG(position_vector ):
    kf = position_vector[0]
    GAIN0 = position_vector[1]
    GAIN1 = position_vector[2]
    GAIN2 = position_vector[3]
    GAIN3 = position_vector[4]
    GAIN4 = position_vector[5]
    GAIN5 = position_vector[6]
    GAIN6 = position_vector[7]
    GAIN7 = position_vector[8]
    GAIN8 = position_vector[9]
    GAIN9 = position_vector[10]
    GAIN10 = position_vector[11]
    GAIN11 = position_vector[12]
    GAIN12 = position_vector[13]
    
    BIAS0 = position_vector[14]
    BIAS1 = position_vector[15]
    BIAS2 = position_vector[16]
    BIAS3 = position_vector[17]
    BIAS4 = position_vector[18]
    BIAS5 = position_vector[19]
    BIAS6 = position_vector[20]
    BIAS7 = position_vector[21]
    BIAS8 = position_vector[22]
    BIAS9 = position_vector[23]
    BIAS10 = position_vector[24]
    BIAS11 = position_vector[25]
    BIAS12 = position_vector[26]
    
    osillator = matsuoka_oscillator(kf)
    osillator_fun = osillator.oscillator_fun
    
    # Variables
    # Oscillator 1 (pacemaker)
    u1_1, u2_1, v1_1, v2_1, y1_1, y2_1, o_1, gain_1, bias_1 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0
    # Oscillator 2 --cell0
    u1_2, u2_2, v1_2, v2_2, y1_2, y2_2, o_2, gain_2, bias_2 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN0, BIAS0
    # Oscillator 3 --cell1
    u1_3, u2_3, v1_3, v2_3, y1_3, y2_3, o_3, gain_3, bias_3 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN1, BIAS1
    # Oscillator 4 --cell2
    u1_4, u2_4, v1_4, v2_4, y1_4, y2_4, o_4, gain_4, bias_4 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN2, BIAS2
    # Oscillator 5 --cell3
    u1_5, u2_5, v1_5, v2_5, y1_5, y2_5, o_5, gain_5, bias_5 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN3, BIAS3
    # Oscillator 6 --cell4
    u1_6, u2_6, v1_6, v2_6, y1_6, y2_6, o_6, gain_6, bias_6 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN4, BIAS4
    # Oscillator 7 --cell5
    u1_7, u2_7, v1_7, v2_7, y1_7, y2_7, o_7, gain_7, bias_7 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN5, BIAS5
    # Oscillator 8 --cell6
    u1_8, u2_8, v1_8, v2_8, y1_8, y2_8, o_8, gain_8, bias_8 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN6, BIAS6
    # Oscillator 9 --cell7
    u1_9, u2_9, v1_9, v2_9, y1_9, y2_9, o_9, gain_9, bias_9 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN7, BIAS7
    # Oscillator 10 --cell8
    u1_10, u2_10, v1_10, v2_10, y1_10, y2_10, o_10, gain_10, bias_10 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN8, BIAS8
    # Oscillator 11 --cell9
    u1_11, u2_11, v1_11, v2_11, y1_11, y2_11, o_11, gain_11, bias_11 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN9, BIAS9
    # Oscillator 12 --cell10
    u1_12, u2_12, v1_12, v2_12, y1_12, y2_12, o_12, gain_12, bias_12 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN10, BIAS10
    # Oscillator 13 --cell11
    u1_13, u2_13, v1_13, v2_13, y1_13, y2_13, o_13, gain_13, bias_13 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN11, BIAS11
    # Oscillator 14 --cell12
    u1_14, u2_14, v1_14, v2_14, y1_14, y2_14, o_14, gain_14, bias_14 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN12, BIAS12
    
   
    
    
    # Calculate next state of oscillator 1 (pacemaker)
    f1_1, f2_1 = 0.0, 0.0
    s1_1, s2_1 = 0.0, 0.0
    u1_1, u2_1, v1_1, v2_1, y1_1, y2_1, o_1 = osillator_fun(u1=u1_1, u2=u2_1, v1=v1_1, v2=v2_1, y1=y1_1, y2=y2_1,
                                                              f1=f1_1, f2=f2_1, s1=s1_1, s2=s2_1,
                                                              bias=bias_1, gain=gain_1, )

    # center
    # Calculate next state of oscillator 2  --cell0
    # w_ij -> j=1 (oscillator 1) is master, i=2 (oscillator 2) is slave
    w_21 = 1.0
    f1_2, f2_2 = 0.0, 0.0
    s1_2, s2_2 = w_21 * u1_1, w_21 * u2_1
    u1_2, u2_2, v1_2, v2_2, y1_2, y2_2, o_2 = osillator_fun(u1=u1_2, u2=u2_2, v1=v1_2, v2=v2_2, y1=y1_2, y2=y2_2,
                                                              f1=f1_2, f2=f2_2, s1=s1_2, s2=s2_2,
                                                              bias=bias_2, gain=gain_2 )
    
    # Left forward 1
    # Calculate next state of oscillator 3 --cell1
    # w_ij -> j=1 (oscillator 2) is master, i=3 (oscillator 3) is slave
    w_32 = 1.0
    f1_3, f2_3 = 0.0, 0.0
    s1_3, s2_3 = w_32 * u1_1, w_32 * u2_1
    u1_3, u2_3, v1_3, v2_3, y1_3, y2_3, o_3 = osillator_fun(u1=u1_3, u2=u2_3, v1=v1_3, v2=v2_3, y1=y1_3, y2=y2_3,
                                                              f1=f1_3, f2=f2_3, s1=s1_3, s2=s2_3,
                                                              bias=bias_3, gain=gain_3 )
    
    # Left back 1
    # Calculate next state of oscillator 4 --cell2
    # w_ij -> j=2 (oscillator 2) is master, i=4 (oscillator 4) is slave
    w_42 = 1.0
    f1_4, f2_4 = 0.0, 0.0
    s1_4, s2_4 = w_42 * u1_2, w_42 * u2_2  # s1_i = w_ij*u1_j, s2_i = w_ij*u2_j
    u1_4, u2_4, v1_4, v2_4, y1_4, y2_4, o_4 = osillator_fun(u1=u1_4, u2=u2_4, v1=v1_4, v2=v2_4, y1=y1_4, y2=y2_4,
                                                              f1=f1_4, f2=f2_4, s1=s1_4, s2=s2_4,
                                                              bias=bias_4, gain=gain_4 )
    
    # Right forward 1
    # Calculate next state of oscillator 5 --cell3
    # w_ij -> j=3 (oscillator 3) is master, i=5 (oscillator 5) is slave
    w_52 = -1.0
    f1_5, f2_5 = 0.0, 0.0
    s1_5, s2_5 = w_52 * u1_3, w_52 * u2_3  # s1_i = w_ij*u1_j, s2_i = w_ij*u2_j
    u1_5, u2_5, v1_5, v2_5, y1_5, y2_5, o_5 = osillator_fun(u1=u1_5, u2=u2_5, v1=v1_5, v2=v2_5, y1=y1_5, y2=y2_5,
                                                              f1=f1_5, f2=f2_5, s1=s1_5, s2=s2_5,
                                                              bias=bias_5, gain=gain_5 )
    
    # Right back1
    # Calculate next state of oscillator 6 --cell4
    # w_ij -> j=2 (oscillator 2) is master, i=6 (oscillator 6) is slave
    w_62 = -1.0
    f1_6, f2_6 = 0.0, 0.0
    s1_6, s2_6 = w_62 * u1_2, w_62 * u2_2  # s1_i = w_ij*u1_j, s2_i = w_ij*u2_j
    u1_6, u2_6, v1_6, v2_6, y1_6, y2_6, o_6 = osillator_fun(u1=u1_6, u2=u2_6, v1=v1_6, v2=v2_6, y1=y1_6, y2=y2_6,
                                                              f1=f1_6, f2=f2_6, s1=s1_6, s2=s2_6,
                                                              bias=bias_6, gain=gain_6 )
    
    # Left forward 2
    # Calculate next state of oscillator 7 --cell5
    # w_ij -> j=3 (oscillator 3) is master, i=7 (oscillator 7) is slave
    w_73 = -1.0
    f1_7, f2_7 = 0.0, 0.0
    s1_7, s2_7 = w_73 * u1_3, w_73 * u2_3  # s1_i = w_ij*u1_j, s2_i = w_ij*u2_j
    u1_7, u2_7, v1_7, v2_7, y1_7, y2_7, o_7 = osillator_fun(u1=u1_7, u2=u2_7, v1=v1_7, v2=v2_7, y1=y1_7, y2=y2_7,
                                                              f1=f1_7, f2=f2_7, s1=s1_7, s2=s2_7,
                                                              bias=bias_7, gain=gain_7 )
    
    # Left foward 3
    # Calculate next state of oscillator 8 --cell6
    # w_ij -> j=1 (oscillator 3) is master, i=8 (oscillator 8) is slave
    w_83 = -1.0
    f1_8, f2_8 = 0.0, 0.0
    s1_8, s2_8 = w_83 * u1_1, w_83 * u2_1  # s1_i = w_ij*u1_j, s2_i = w_ij*u2_j
    u1_8, u2_8, v1_8, v2_8, y1_8, y2_8, o_8 = osillator_fun(u1=u1_8, u2=u2_8, v1=v1_8, v2=v2_8, y1=y1_8, y2=y2_8,
                                                              f1=f1_8, f2=f2_8, s1=s1_8, s2=s2_8,
                                                              bias=bias_8, gain=gain_8 )
    
    # Left back 2
    # Calculate next state of oscillator 9 --cell7
    # w_ij -> j=8 (oscillator 4) is master, i=9 (oscillator 9) is slave
    w_94 = -1.0
    f1_9, f2_9 = 0.0, 0.0
    s1_9, s2_9 = w_94 * u1_8, w_94 * u2_8  # s1_i = w_ij*u1_j, s2_i = w_ij*u2_j
    u1_9, u2_9, v1_9, v2_9, y1_9, y2_9, o_9 = osillator_fun(u1=u1_9, u2=u2_9, v1=v1_9, v2=v2_9, y1=y1_9, y2=y2_9,
                                                              f1=f1_9, f2=f2_9, s1=s1_9, s2=s2_9,
                                                              bias=bias_9, gain=gain_9 )
    
    # Left back 3
    # Calculate next state of oscillator 10 --cell8
    # w_ij -> j=1 (oscillator 4) is master, i=10 (oscillator 10) is slave
    w_104 = -1.0
    f1_10, f2_10 = 0.0, 0.0
    s1_10, s2_10 = w_104 * u1_1, w_104 * u2_1  # s1_i = w_ij*u1_j, s2_i = w_ij*u2_j
    u1_10, u2_10, v1_10, v2_10, y1_10, y2_10, o_10 = osillator_fun(u1=u1_10, u2=u2_10, v1=v1_10, v2=v2_10, y1=y1_10,
                                                                     y2=y2_10,
                                                                     f1=f1_10, f2=f2_10, s1=s1_10, s2=s2_10,
                                                                     bias=bias_10, gain=gain_10 )
    
    # Right forward 2
    # Calculate next state of oscillator 11 --cell9
    # w_ij -> j=10 (oscillator 5) is master, i=11 (oscillator 11) is slave
    w_115 = -1.0
    f1_11, f2_11 = 0.0, 0.0
    s1_11, s2_11 = w_115 * u1_10, w_115 * u2_10  # s1_i = w_ij*u1_j, s2_i = w_ij*u2_j
    u1_11, u2_11, v1_11, v2_11, y1_11, y2_11, o_11 = osillator_fun(u1=u1_11, u2=u2_11, v1=v1_11, v2=v2_11, y1=y1_11,
                                                                     y2=y2_11,
                                                                     f1=f1_11, f2=f2_11, s1=s1_11, s2=s2_11,
                                                                     bias=bias_11, gain=gain_11 )
    
    # Right forward 3
    # Calculate next state of oscillator 12 --cell10
    # w_ij -> j=1 (oscillator 5) is master, i=12 (oscillator 12) is slave
    w_125 = -1.0
    f1_12, f2_12 = 0.0, 0.0
    s1_12, s2_12 = w_125 * u1_1, w_125 * u2_1  # s1_i = w_ij*u1_j, s2_i = w_ij*u2_j
    u1_12, u2_12, v1_12, v2_12, y1_12, y2_12, o_12 = osillator_fun(u1=u1_12, u2=u2_12, v1=v1_12, v2=v2_12, y1=y1_12,
                                                                     y2=y2_12,
                                                                     f1=f1_12, f2=f2_12, s1=s1_12, s2=s2_12,
                                                                     bias=bias_12, gain=gain_12)
    
    # Right back 2
    # Calculate next state of oscillator 13 --cell11
    # w_ij -> j=1 (oscillator 6) is master, i=13 (oscillator 13) is slave
    w_136 = 1.0
    f1_13, f2_13 = 0.0, 0.0
    s1_13, s2_13 = w_136 * u1_1, w_136 * u2_1  # s1_i = w_ij*u1_j, s2_i = w_ij*u2_j
    u1_13, u2_13, v1_13, v2_13, y1_13, y2_13, o_13 = osillator_fun(u1=u1_13, u2=u2_13, v1=v1_13, v2=v2_13, y1=y1_13,
                                                                     y2=y2_13,
                                                                     f1=f1_13, f2=f2_13, s1=s1_13, s2=s2_13,
                                                                     bias=bias_13, gain=gain_13)

    # Right back 3
    # Calculate next state of oscillator 14 --cell11
    # w_ij -> j=1 (oscillator 6) is master, i=14 (oscillator 14) is slave
    w_146 = 1.0
    f1_14, f2_14 = 0.0, 0.0
    s1_14, s2_14 = w_146 * u1_1, w_146 * u2_1  # s1_i = w_ij*u1_j, s2_i = w_ij*u2_j
    u1_14, u2_14, v1_14, v2_14, y1_14, y2_14, o_14 = osillator_fun(u1=u1_14, u2=u2_14, v1=v1_14, v2=v2_14, y1=y1_14,
                                                                   y2=y2_14,
                                                                   f1=f1_14, f2=f2_14, s1=s1_14, s2=s2_14,
                                                                   bias=bias_14, gain=gain_14)