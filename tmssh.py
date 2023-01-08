import pickle
import os
from getpass import getpass

class Host:
    def __init__(self, server="voidtm.tk", user="egg", password="a", key=False):
        self.server = server
        self.user = user
        self.password = password
        self.key = key

def newFile():
    pickle.dump([], open("tmssh_hosts", "wb"))

#os.system("touch hosts")
#open("hosts", "w").close()
try:
    if open("tmssh_hosts","r").read() in ["", "\n", " ", " \n", "\n "]:
        newFile()
except Exception:
    pass

error = os.system("cat tmssh_hosts > /dev/null 2>&1")
if error != 0:
    print("ERROR: hosts file not found, can be solved by running `touch ~/.ssh/tmssh_hosts`")
    exit()

hosts = pickle.load(open("tmssh_hosts", "rb"))

print("\033[0;34m--TMSSH--\033[0m")

while True:
    count = 1
    for i in hosts:
        print("%d: %s@%s" % (count, i.user, i.server))
        count += 1
    try:
        cmd = input("\033[0;32mType a command>\033[0m ")
    except EOFError:
        print("^D")
        exit()
    except KeyboardInterrupt:
        print("^C")
        exit()
    if cmd.isdigit():
        try:
            host = hosts[int(cmd)-1]
        except Exception:
            print("ERROR: number not found in hosts")
            continue
        if not host.key:
            #error = os.system("sshpass")
            #if int(error) != 0:
            #    print("ERROR: sshpass is not installed.")
            #    break
            #os.system("sshpass -p \"%s\" ssh %s@%s" % (host.password, host.user, host.server))
            #continue
            print("Passwords currently not supported")
        else:
            os.system("ssh %s@%s" % (host.user, host.server))
            print("\033[0;34m--TMSSH--\033[0m")
    if cmd == "q":
        break
    if cmd == "a":
        user = input("Username> ")
        server = input("Server> ")
        passwd = "a"#passwd = getpass(prompt="Password> ")
        host = Host(server=server, user=user, password=passwd, key=True)
        hosts.append(host)
        pickle.dump(hosts, open("tmssh_hosts", "wb"))
        print("\033[0;34m--TMSSH--\033[0m")
