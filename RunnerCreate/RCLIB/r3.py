import csv
from . import allvars as av

#VPC LIP Runner 003
def runner03():
    with open(av.iDcp + '_003_VPC_LIP_runner.csv', 'w+') as file:
        myFile = csv.writer(file)
        myFile.writerow(["switch_lip", "desc", "vpc_is", "vpc_lipg", "int_desc", "if_f_num", "if_t_num", "bogus"])
        switch_lip = str(av.node1_num) + "_" + str(av.node2_num) + "_" + av.iVrf + "_" + "_" + av.iProj + "_LIP"
        for i in range (av.iTvpc):
            vpc_is = "VPC" + str(i + 1) + "_IS"
            int_desc = "Server " + str(i + 1)
            if_f_num = (av.iSp + av.iStep)
            #print(if_f_num)
            if_t_num = (i + av.iSp)
            #print(if_t_num)
            vpcLipg = av.iTenant + "_" + str(av.node1_num) + "_" + str(av.node2_num) + "_" + av.iVrf + "_" + av.iProj + "_VPC" + str(i + 1) + "_LIPG"
            myFile.writerow([switch_lip, av.iDcp, vpc_is, vpcLipg, int_desc, str(i+if_f_num-av.iStep), str(if_t_num)])