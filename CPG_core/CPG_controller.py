from CPG_core.CPG_osillator import matsuoka_oscillator

class CPG_controller(object):
    def __init__(self, position_vector):
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
        self.osillator_fun = osillator.oscillator_fun
        
        # Variables
        # Oscillator 1 (pacemaker)
        self.u1_1, self.u2_1, self.v1_1, self.v2_1, self.y1_1, self.y2_1, self.o_1, self.gain_1, self.bias_1 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0
        # Oscillator 2 --cell0
        self.u1_2, self.u2_2, self.v1_2, self.v2_2, self.y1_2, self.y2_2, self.o_2, self.gain_2, self.gias_2 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN0, BIAS0
        # Oscillator 3 --cell1
        self.u1_3, self.u2_3, self.v1_3, self.v2_3, self.y1_3, self.y2_3, self.o_3, self.gain_3, self.gias_3 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN1, BIAS1
        # Oscillator 4 --cell2
        self.u1_4, self.u2_4, self.v1_4, self.v2_4, self.y1_4, self.y2_4, self.o_4, self.gain_4, self.gias_4 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN2, BIAS2
        # Oscillator 5 --cell3
        self.u1_5, self.u2_5, self.v1_5, self.v2_5, self.y1_5, self.y2_5, self.o_5, self.gain_5, self.gias_5 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN3, BIAS3
        # Oscillator 6 --cell4
        self.u1_6, self.u2_6, self.v1_6, self.v2_6, self.y1_6, self.y2_6, self.o_6, self.gain_6, self.gias_6 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN4, BIAS4
        # Oscillator 7 --cell5
        self.u1_7, self.u2_7, self.v1_7, self.v2_7, self.y1_7, self.y2_7, self.o_7, self.gain_7, self.gias_7 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN5, BIAS5
        # Oscillator 8 --cell6
        self.u1_8, self.u2_8, self.v1_8, self.v2_8, self.y1_8, self.y2_8, self.o_8, self.gain_8, self.gias_8 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN6, BIAS6
        # Oscillator 9 --cell7
        self.u1_9, self.u2_9, self.v1_9, self.v2_9, self.y1_9, self.y2_9, self.o_9, self.gain_9, self.gias_9 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN7, BIAS7
        # Oscillator 10 --cell8
        self.u1_10, self.u2_10, self.v1_10, self.v2_10, self.y1_10, self.y2_10, self.o_10, self.gain_10, self.gias_10 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN8, BIAS8
        # Oscillator 11 --cell9
        self.u1_11, self.u2_11, self.v1_11, self.v2_11, self.y1_11, self.y2_11, self.o_11, self.gain_11, self.gias_11 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN9, BIAS9
        # Oscillator 12 --cell10
        self.u1_12, self.u2_12, self.v1_12, self.v2_12, self.y1_12, self.y2_12, self.o_12, self.gain_12, self.gias_12 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN10, BIAS10
        # Oscillator 13 --cell11
        self.u1_13, self.u2_13, self.v1_13, self.v2_13, self.y1_13, self.y2_13, self.o_13, self.gain_13, self.gias_13 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN11, BIAS11
        # Oscillator 14 --cell12
        self.u1_14, self.u2_14, self.v1_14, self.v2_14, self.y1_14, self.y2_14, self.o_14, self.gain_14, self.gias_14 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN12, BIAS12

        
        
        # Oscillator 2 --cell0
        self.u1_2, self.u2
        # Oscillator 3 --cell1
        self.u1_3, self.u2_3, self.v1_3, self.v2_3, self.y1_3, self.y2_3, self.o_3, self.gain_3, self.gias_3 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN1, BIAS1
        # Oscillator 4 --cell2
        self.u1_4, self.u2_4, self.v1_4, self.v2_4, self.y1_4, self.y2_4, self.o_4, self.gain_4, self.gias_4 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN2, BIAS2
        # Oscillator 5 --cell3
        self.u1_5, self.u2_5, self.v1_5, self.v2_5, self.y1_5, self.y2_5, self.o_5, self.gain_5, self.gias_5 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN3, BIAS3
        # Oscillator 6 --cell4
        self.u1_6, self.u2_6, self.v1_6, self.v2_6, self.y1_6, self.y2_6, self.o_6, self.gain_6, self.gias_6 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN4, BIAS4
        # Oscillator 7 --cell5
        self.u1_7, self.u2_7, self.v1_7, self.v2_7, self.y1_7, self.y2_7, self.o_7, self.gain_7, self.gias_7 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN5, BIAS5
        # Oscillator 8 --cell6
        self.u1_8, self.u2_8, self.v1_8, self.v2_8, self.y1_8, self.y2_8, self.o_8, self.gain_8, self.gias_8 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN6, BIAS6
        # Oscillator 9 --cell7
        self.u1_9, self.u2_9, self.v1_9, self.v2_9, self.y1_9, self.y2_9, self.o_9, self.gain_9, self.gias_9 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN7, BIAS7
        # Oscillator 10 --cell8
        self.u1_10, self.u2_10, self.v1_10, self.v2_10, self.y1_10, self.y2_10, self.o_10, self.gain_10, self.gias_10 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN8, BIAS8
        # Oscillator 11 --cell9
        self.u1_11, self.u2_11, self.v1_11, self.v2_11, self.y1_11, self.y2_11, self.o_11, self.gain_11, self.gias_11 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN9, BIAS9
        # Oscillator 12 --cell10
        self.u1_12, self.u2_12, self.v1_12, self.v2_12, self.y1_12, self.y2_12, self.o_12, self.gain_12, self.gias_12 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN10, BIAS10
        # Oscillator 13 --cell11
        self.u1_13, self.u2_13, self.v1_13, self.v2_13, self.y1_13, self.y2_13, self.o_13, self.gain_13, self.gias_13 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN11, BIAS11
        # Oscillator 14 --cell12
        self.u1_14, self.u2_14, self.v1_14, self.v2_14, self.y1_14, self.y2_14, self.o_14, self.gain_14, self.gias_14 = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN12, BIAS12


from CPG_core.CPG_osillator import CPG_neutron
class CPG_network(object):
    def __init__(self, position_vector):
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
        parm_list = {
            0:  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
            1: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN0, BIAS0],
            2: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN1, BIAS1],
            3: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN2, BIAS2],
            4: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN3, BIAS3],
            5: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN4, BIAS4],
            6: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN5, BIAS5],
            7: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN6, BIAS6],
            8: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN7, BIAS7],
            9: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN8, BIAS8],
            10: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN9, BIAS9],
            11: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN10, BIAS10],
            12: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN11, BIAS11],
            13: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN12, BIAS12],
        }
        
        self.kf = position_vector[0]
        self.num_CPG = 14
        self.CPG_list =[]
        #self.w_ms_list = [ None,  1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1 ]
        self.w_ms_list = [None, 1, 1, -1,- 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        #self.w_ms_list =   [None, 1, -1, -1,  1, -1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.master_list = [None, 0, 1, 1,  1,  1,  2,  2,  3,  3,  4,  4,  5,  5]
        
        
        for i in range(self.num_CPG):
            if i == 0:
                self.CPG_list.append(CPG_neutron(0, master_nuron = None, param=parm_list[0] ,kf= self.kf, w_ms = 0))
            else:
                self.CPG_list.append(CPG_neutron(1, master_nuron=self.CPG_list[self.master_list[i]],
                                                 param=parm_list[i], kf=self.kf, w_ms= self.w_ms_list[i]))
                

        # CPG0 = CPG_neutron(0, master_nuron = None, param=parm_list[0] ,kf= self.kf, w_ms = None)
        # CPG1 = CPG_neutron(1, master_nuron=CPG0,  param=parm_list[1] ,kf=self.kf, w_ms = 1)
        # CPG2 = CPG_neutron(2, master_nuron=CPG1, param=parm_list[2] , kf=self.kf, w_ms = 1)
        # CPG3 = CPG_neutron(3, master_nuron=CPG1,  param=parm_list[3] ,kf=self.kf, w_ms = 1)
        # CPG4 = CPG_neutron(4, master_nuron=CPG1,  param=parm_list[4] ,kf=self.kf, w_ms = -1)
        # CPG5 = CPG_neutron(5, master_nuron=CPG1, param=parm_list[5] , kf=self.kf, w_ms = -1)
        # CPG6 = CPG_neutron(6, master_nuron=CPG2, param=parm_list[6] , kf=self.kf, w_ms = -1)
        # CPG7 = CPG_neutron(7, master_nuron=CPG2, param=parm_list[7] , kf=self.kf, w_ms = -1)
        # CPG8 = CPG_neutron(8, master_nuron=CPG3,  param=parm_list[8] ,kf=self.kf, w_ms = -1)
        # CPG9 = CPG_neutron(9, master_nuron=CPG3,  param=parm_list[9] ,kf=self.kf, w_ms = -1)
        # CPG10 = CPG_neutron(10, master_nuron=CPG4, param=parm_list[10] , kf=self.kf, w_ms = -1)
        # CPG11 = CPG_neutron(12, master_nuron=CPG4,  param=parm_list[11] ,kf=self.kf, w_ms = -1)
        # CPG12 = CPG_neutron(13, master_nuron=CPG5,  param=parm_list[12] ,kf=self.kf, w_ms = -1)
        # CPG13 = CPG_neutron(14, master_nuron=CPG5,  param=parm_list[13] ,kf=self.kf, w_ms = -1)
        
        #init

        
    def output(self, state):
        output_list = []
        for cpg_n in self.CPG_list:
            cpg_n.next_output(f1=0, f2=0)
            output_list.append(cpg_n.parm['o'])
        
        return output_list
        
       