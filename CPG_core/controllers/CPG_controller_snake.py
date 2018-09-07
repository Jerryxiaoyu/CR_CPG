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

        BIAS0 = position_vector[10]
        BIAS1 = position_vector[11]
        BIAS2 = position_vector[12]
        BIAS3 = position_vector[13]
        BIAS4 = position_vector[14]
        BIAS5 = position_vector[15]
        BIAS6 = position_vector[16]
        BIAS7 = position_vector[17]
        BIAS8 = position_vector[18]
        
        
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
          
        }
        
        self.kf = position_vector[0]
        self.num_CPG = len(parm_list)
        self.CPG_list =[]
        self.w_ms_list  =   [None, 1, 1, 1, 1, -1, 1, 1, 1, 1]
        #self.master_list =  [None, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.master_list = [None, 0, 1, 1, 1, 1, 1, 1, 1, 1]
        
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
        
       