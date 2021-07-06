import os

def run_script():
    print("Please Enter Your IP Separately in 4 Octal")
    ip1=input("IP Address octal 1:")
    ip2=input("IP Address octal 2:")
    ip3=input("IP Address octal 3:")
    ip4=int(input("IP Address octal 4:"))
    ranger=int(input("Range add more than one number:"))
    print("[+] Here You get Output file in same Directory.....")
    print("It will take time depends on your range. So,")
    print("Please Wait...")

    while True:
        if ip4<=ranger:
            fo=open("ping.sh","a")
            print("ping -c 1", ip1+"."+ip2+"."+ip3+"."+str(ip4) , file=fo)
            ip4+=1;
            fo.close()
        elif ip4>ranger:
            break;
        else:
            break;

    mycmd="bash ping.sh > output.txt"
    os.system(mycmd)
    mycmd2="rm -rf ping.sh"
    os.system(mycmd2)
    mycmd3="cat output.txt"
    os.system(mycmd3)