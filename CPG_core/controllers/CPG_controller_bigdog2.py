from CPG_core.CPG_osillator import matsuoka_oscillator


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
        GAIN13 = position_vector[14]
        

        BIAS0 = position_vector[15]
        BIAS1 = position_vector[16]
        BIAS2 = position_vector[17]
        BIAS3 = position_vector[18]
        BIAS4 = position_vector[19]
        BIAS5 = position_vector[20]
        BIAS6 = position_vector[21]
        BIAS7 = position_vector[22]
        BIAS8 = position_vector[23]
        BIAS9 = position_vector[24]
        BIAS10 = position_vector[25]
        BIAS11 = position_vector[26]
        BIAS12 = position_vector[27]
        BIAS13 = position_vector[28]
     
        
        
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
            14: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, GAIN13, BIAS13],
 
        }
        
        self.kf = position_vector[0]
        self.num_CPG = len(parm_list)
        self.CPG_list =[]
        self.w_ms_list = [None, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ]
        self.master_list = [None, 0, 0, 1, 3, 3, 1, 6, 6, 2, 9, 9, 2, 12, 12]
        
        for i in range(self.num_CPG):
            if i == 0:
                self.CPG_list.append(CPG_neutron(0, master_nuron = None, param=parm_list[0] ,kf= self.kf, w_ms = 0))
            else:
                self.CPG_list.append(CPG_neutron(1, master_nuron=self.CPG_list[self.master_list[i]],
                                                 param=parm_list[i], kf=self.kf, w_ms= self.w_ms_list[i]))
                
 

    def output(self, state):
        output_list = []
        for cpg_n in self.CPG_list:
            cpg_n.next_output(f1=0, f2=0)
            output_list.append(cpg_n.parm['o'])
    
        return output_list
        
       