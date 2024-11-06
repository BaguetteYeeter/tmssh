import os
import os.path
from pathlib import Path
import readline

def main():
    home = Path.home()
    filename = f"{home}/.ssh/tmssh_hosts"

    print("\033[0;34m--TMSSH--\033[0m")

    if os.path.isfile(filename):
        f = open(filename, "r")
        hosts = f.read().splitlines()
        f.close()
    else:
        os.system(f"touch {filename}")
        hosts = []

    while True:
        for i, k in enumerate(hosts):
            print(f"{i+1}: {k}")

        try:
            cmd = input("\033[0;32mType a command>\033[0m ")
        except EOFError:
            print()
            exit()
        except KeyboardInterrupt:
            print()
            exit()

        if cmd.isdigit():
            try:
                host = hosts[int(cmd)-1]
            except Exception:
                print("ERROR: number not found in hosts")
                continue
            else:
                os.system(f"ssh {host}")
                print("\033[0;34m--TMSSH--\033[0m")

        if cmd == "q":
            break
        if cmd == "a":
            try:
                host = input("username@server> ")
            except Exception:
                print()
                continue
            except KeyboardInterrupt:
                print()
                continue
            hosts.append(host)
            f = open(filename, "w")
            f.write("\n".join(hosts))
            f.close()
            print("\033[0;34m--TMSSH--\033[0m")
        if cmd == "r":
            num = input("Host to remove? ")
            if num.isdigit():
                del hosts[int(num)-1]
            else:
                try:
                    hosts.remove(num)
                except ValueError:
                    print("Host not found")
                    continue
            f = open(filename, "w")
            f.write("\n".join(hosts))
            f.close()
            print("\033[0;34m--TMSSH--\033[0m")

if __name__ == "__main__":
    main()