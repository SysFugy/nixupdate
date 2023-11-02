import os
import sys

def print_banner():
    banner = """
    ███╗░░██╗██╗██╗░░██╗██╗░░░██╗██████╗░██████╗░░█████╗░████████╗███████╗
    █████╗░██║██║╚██╗██╔╝██║░░░██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
    ██╔██╗██║██║░╚███╔╝░██║░░░██║██████╔╝██║░░██║███████║░░░██║░░░█████╗░░
    ██║╚████║██║░██╔██╗░██║░░░██║██╔═══╝░██║░░██║██╔══██║░░░██║░░░██╔══╝░░
    ██║░╚███║██║██╔╝╚██╗╚██████╔╝██║░░░░░██████╔╝██║░░██║░░░██║░░░███████╗
    ╚═╝░░╚══╝╚═╝╚═╝░░╚═╝░╚═════╝░╚═╝░░░░░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝
    """
    print(banner)

def nix_update(category):
    update_actions = {
        "1": lambda: os.system("nix-env -u"),
        "2": lambda: os.system("nix-channel --update")
    }
    update_actions.get(category, lambda: input("Error: Command not found!"))()

def main():
    if sys.platform != "linux":
        input("Error: System not supported!")
    else:
        while True:
            os.system("clear")
            print_banner()
            nix_update(input("\nUpdate 'packages' or 'channels' (1, 2)? ").lower())

if __name__ == "__main__":
    main()
