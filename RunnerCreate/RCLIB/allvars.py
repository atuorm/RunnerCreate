import datetime

FixIt = "  Nope! Try Again\n"
dashStr = "-"
dashRepeat2 = dashStr * len(FixIt)
print(
'''  
█▀▄ █▀▀ █▄░█   ▄▄   █▀█ █▀█ █▀ ▀█▀ █▀▄▀█ ▄▀█ █▄░█   █▀█ █░█ █▄░█ █▄░█ █▀▀ █▀█   █▀▀ █▀█ █▀▀ ▄▀█ ▀█▀ █▀█ █▀█
█▄▀ █▄▄ █░▀█   ░░   █▀▀ █▄█ ▄█ ░█░ █░▀░█ █▀█ █░▀█   █▀▄ █▄█ █░▀█ █░▀█ ██▄ █▀▄   █▄▄ █▀▄ ██▄ █▀█ ░█░ █▄█ █▀▄
'''
)

#print('  Enter Todays Date:')
e = datetime.datetime.now()
iDate = e.strftime("%m-%d-%Y")
#print(iDate)

print('  Enter DCP Number:')
iDcp = input()

print('  Enter Tenant:')
iTenant = input()

print('  Enter VRF:')
iVrf = input()

print('  Enter Application Name:')
iProj = input()

print('  Enter EPG:')
iEpg = input()

print('  Enter POD:') #This variable has been ID'd as a Digital Millennium Copyright Act Violation!
iPod = input()

print('  Enter Your Initials:')
iIni = input()

print('  Enter Module Number of Switch Interface:')
iMod = input()

print('  Enter the First Node Number:')
node1_num = input()

print('  Enter the Second Node Number:')
node2_num = input()

while True:
    iVlan = int(input("Enter the Encaps VLAN 1-4096: "))
    if iVlan < 0 or iVlan > 4096:
        print("The value is out of range, try again.")
    else:
        break

iImmdQ = "  What Immediacy?  Immediate(immediate) or On Demand(lazy): \n"
iImmdA = input(iImmdQ)

if iImmdA in ['lazy', 'immediate']:
    print("\n")
    
else:   
    #print(dashRepeat2 + "\n" + FixIt + "\n" + dashRepeat2)
    quit()

iModeQ = "  What Mode Configuration For The Ports? Access=(untagged) Trunk=(regular): \n"
iModeA = input(iModeQ) 

if iModeA in ['untagged', 'regular']:
    print("\n")
    
else:   
    print(
'''        
                     _.-*'""'*-._
                  .-"            "-.
                ,"                  ",
              .'      _.-.--.-._      ',
             /     .-'.-"    "-.'-.     \\
            /     /  /"'-.  .-'"\  \     \\
           :     :  :     ;:     ;  ;     ;
           ;     :  ; *   !! *   :  ;     :
           ;      ; :   .'  '.   ; :      :
           :       \ \-'      '-/ /       ;
            \       '.'-_    _-'.'       /
             \        '*-"-+"-*'        /
              '.          /|          .'
                *,       / |        ,*
                / '-_            _-'  \\
               /     "*-.____.-*"      \\
              /            |            \\
             :    :        |        ;    ;
             |.--.;        |        :.--.|
             (   ()        |        ()   )
              '--^_        |        _^--'
                 | "'*--.._I_..--*'" |
                 | __..._  | _..._   |
                .'"      `"'"     ''"'.
                """"""""""""""""""""""" 
                   YOU KILLED KENNY!
            
'''
)
    quit()

print('  Enter Total vPCs:')
iTvpc = int(input())

print('  Enter Starting Enterface: Eth' + iMod +'/')
iSp = int(input())

print('  Contained Ports in vPC: Typically 2 ')
iCvpc = int(input())
iStep = iCvpc//2
iPps = iStep//2
iTp = iTvpc*iStep
