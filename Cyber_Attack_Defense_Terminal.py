import time
server_health=100
system_status="SECURE"
game_running=True

while game_running:
    print(f"===STATUS: {system_status} | HEALTH : {server_health}% ===")
    print("[1] Scan Network Logs")
    print("[2] Deploy Firewall Override")
    print("[3] Emergency Shutdown")
    user_choice=input("enter your choice : ")



# user option 1
    if user_choice=="1":
        for seconds in range(3,0,-1):
           print(f'SCANNNING NETWORK IN ...{seconds}')
           time.sleep(1)
        target_ip="192.168.8.18"
        log="CRITICAL_INTRUSION_DETECTED//SOURCE_IP:192.168.8.18//PORT:443"
        print(F"🚨AN ACTIVE BREACH WAS INTERCEPTED WITH IP ADRESS OF {log} 🚨")
        print("OVER TO YOU CAP!!!")
        print("NOW YOU CAN ONLY SAVE THE COMPANY.BE A HERO👊")
        ip_adress=input("TYPE THE IP ADRESS OF THE HACKER : ")
        if ip_adress==target_ip:
            system_status="SECURE"
            print("MISSION SUCCESSFUL😎")
            print("YOU JUST SLAYED ENGINEER 🤏")
            print("=====ID BLOCKED====")
        else:
            print("YOU HAVE MISSED YOUR ONLY CHANCE ENGINEER😐.")
            print("tsk-tsk-tsk-tsk")
            server_health=server_health-25
            system_status="UNDER BRUTAL ATTACKKKK "




# user option 2
    elif user_choice=="2":
        base_port=4000
        encryption_key=7
        for i in range(3, 0, -1):
            print(f"System unlocking in... {i}")
            time.sleep(1)
        print(f"To override, multiply the base port {base_port} by {encryption_key} and add 100")
        correct_port=(base_port*encryption_key)+100
        start_time=time.time()
        calculation_result=int(input("enter your input : "))
        end_time=time.time()
        seconds_taken=int(end_time-start_time)
        print(f"Calculation took you {seconds_taken} seconds...")
        if calculation_result==correct_port and  seconds_taken>5:
          
                print("TOO SLOW ADMIN 🐌! THE PATCH WAS DEPLOYED, BUT THE HACKER STILL DRAINED SOME RESOURCES")
                print("YOU HAVE NO TIME MANAGMENT 😣 SKILLS .... THEREFORE YOU HAVE BEEN GIVEN A PENALTY")
                print("ALREADY HEALTH FULL .... WILL SEE U NEXT TIME...BE PUNTUAL ")
                if not server_health==100:
                 server_health+=5
                 print("ONLY 5 SECONDS SERVER HEALTH REWARDED")
        elif calculation_result==correct_port and seconds_taken<=5:
          print("YOU ARE SUCCESSFUL. YOU ARE A GENIUS 👌\n " 
          "FIREWALL OVERRIDE SUCCESSFUL! PROTOCOL RESET ")
          system_status="SECURE"        
          if not server_health==100:
                server_health+=25
        else:
            print("OVERRIDE FAILED! FIREWALL COMPROMISED👎")
            system_status="CRITICAL SYSTEM FAILURE"
            server_health-=25





# user option 3
    elif user_choice=="3":
        print("🚨 EMERGENCY EMERGENCYYYYY")
        print("SHUTTING DOWN ALERT.........")
        print("DEAD💀")
        game_running=False
    if server_health<=0:
        game_running=False
        print("THE SERVER WAS COMPLETELY DESTROYED")
        print("ITS GAME OVER ENGINEER 🤔 BETTER LUCK NEXT TIME")


  