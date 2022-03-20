import csv
from . import allvars as av

#print(str(iStep))
#VPC Build Runner 002
def runner02():
    with open(av.iDcp + '_002_VPC_BUILD_runner.csv', 'w+') as file:
        myFile = csv.writer(file)
        myFile.writerow(["ap", "tenant", "epg", "pod", "vlan", "mode", "sw_vpc", "vpc_lipg", "imedcy","bogus"])
        iAp = av.iProj + "_AP"
        sVpc =  str(av.node1_num) + "-" + str(av.node2_num)
        for i in range (av.iTvpc):
            vpcLipg = av.iTenant + "_" + str(av.node1_num) + "_" + str(av.node2_num) + "_" + av.iVrf + "_" + av.iProj + "_VPC" + str(i + 1) + "_LIPG"
            myFile.writerow([av.iProj, av.iTenant, av.iEpg, av.iPod, av.iVlan, av.iModeA, sVpc, vpcLipg, av.iImmdA])