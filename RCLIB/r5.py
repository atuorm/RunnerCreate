import csv
from . import allvars as av

#Interface Description Runner 005
def runner05():
    with open(av.iDcp + '_005_IFDESC_runner.csv', 'w+') as file:
        myFile = csv.writer(file)
        myFile.writerow(["pod_num", "node_num", "mod_num", "if_num", "desc", "bogus"])
        desc = (av.iDcp + '_' + av.iDate + '_' + av.iProj + '_' + av.iIni)
        print("Please Enter The Inferfaces For " + av.node1_num + " : (First Port should be Eth" +str(av.iMod) + "/" + str(av.iSp) +"): ")
        for i in range (av.iTp):
            if1_num = int(input("Enter interface " + str(i +1) + " of " + str(av.iTp) + ": Eth" + str(av.iMod) + "/"))
            myFile.writerow([av.iPod, av.node1_num, av.iMod, if1_num, desc])
            desc = (av.iDcp + '_' + av.iDate + '_' + av.iProj + '_' + av.iIni)
        print("Please Enter The Inferfaces For " + av.node2_num + " : (First Port should be Eth" +str(av.iMod) + "/" + str(av.iSp) +"): ")
        for i in range (av.iTp):
            if2_num = int(input("Enter interface " + str(i +1) + " of " + str(av.iTp) + ": Eth" + str(av.iMod) + "/"))
            myFile.writerow([av.iPod, av.node2_num, av.iMod, if2_num, desc])
