import csv
import datetime
from RCLIB import allvars

#print(str(iStep))
#VPC Build Runner 002
with open(allvars.iDcp + '_002_VPC_BUILD_runner.csv', 'w+') as file:
    myFile = csv.writer(file)
    myFile.writerow(["ap", "tenant", "epg", "pod", "vlan", "mode", "sw_vpc", "vpc_lipg", "imedcy","bogus"])
    iAp = iProj + "_AP"
    sVpc =  str(node1_num) + "-" + str(node2_num)
    for i in range (iTvpc):
        vpcLipg = iTenant + "_" + str(node1_num) + "_" + str(node2_num) + "_" + iVrf + "_" + iProj + "_VPC" + str(i + 1) + "_LIPG"
        myFile.writerow([iProj, iTenant, iEpg, iPod, iVlan, iModeA, sVpc, vpcLipg, iImmdA])

#VPC LIP Runner 003
with open(iDcp + '_003_VPC_LIP_runner.csv', 'w+') as file:
    myFile = csv.writer(file)
    myFile.writerow(["switch_lip", "desc", "vpc_is", "vpc_lipg", "int_desc", "if_f_num", "if_t_num", "bogus"])
    switch_lip = str(node1_num) + "_" + str(node2_num) + "_" + iVrf + "_" + "_" + iProj + "_LIP"
    for i in range (iTvpc):
        vpc_is = "VPC" + str(i + 1) + "_IS"
        int_desc = "Server " + str(i + 1)
        if_f_num = (iSp + iStep)
        #print(if_f_num)
        if_t_num = (i + iSp)
        #print(if_t_num)
        vpcLipg = iTenant + "_" + str(node1_num) + "_" + str(node2_num) + "_" + iVrf + "_" + iProj + "_VPC" + str(i + 1) + "_LIPG"
        myFile.writerow([switch_lip, iDcp, vpc_is, vpcLipg, int_desc, str(i+if_f_num-iStep), str(if_t_num)])
#Interface Description Runner 005
with open(iDcp + '_005_IFDESC_runner.csv', 'w+') as file:
    myFile = csv.writer(file)
    myFile.writerow(["pod_num", "node_num", "mod_num", "if_num", "desc", "bogus"])
    #tpN1 = int(input("Enter Total Number of Ports on First Node: "))
    #tpN2 = int(input("Enter Total Number of Ports on Second Node: "))
    tpN1 = iTp
    tpN2 = iTp
    desc = (iDcp + '_' + iDate + '_' + iProj + '_' + iIni)
    print("Please Enter The Inferfaces For " + node1_num + " : ")
    for i in range (tpN1):
        if1_num = int(input("Enter interface " + str(i +1) + " of " + str(tpN1) + ": Eth" + str(iMod) + "/"))
        myFile.writerow([iPod, node1_num, iMod, if1_num, desc])
    desc = (iDcp + '_' + iDate + '_' + iProj + '_' + iIni)
    print("Please Enter The Inferfaces For " + node2_num + " : ")
    for i in range (tpN2):
        if2_num = int(input("Enter interface " + str(i +1) + " of " + str(tpN2) + ": Eth" + str(iMod) + "/"))
        myFile.writerow([iPod, node2_num, iMod, if2_num, desc])
