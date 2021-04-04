import sys
import requests
import os


def find_subdomain_and_scan(domain, txt_file):
    print(f"\nTarget domain: {domain}")
    discovered_subdomains = []
    with open(txt_file, "r") as f1:
        for i in f1:
            subdomain = i.strip()
            new_url = subdomain + "." + domain
            subdomains_file = domain + "_subdomains.txt"
            try:
                get_response = requests.get("https://" + new_url)
                print(f"\n[*] Found: {new_url} {get_response}")
                discovered_subdomains.append(new_url)
            except requests.ConnectionError:
                print(f"\n[*] Did not found: {new_url}")
                pass
    print("\n[-] Discovered subdomains:")
    print(*discovered_subdomains, sep="\n")
    with open(subdomains_file, "w") as f:
        for subdomain in discovered_subdomains:
            print(subdomain, file=f)
    print(f"\nDiscovered subdomains saved in {subdomains_file}")
    with open(subdomains_file, "r") as f2:
        for i in f2:
            final_subdomain = i.strip()
            complete_subdomain = "https://" + final_subdomain
            try:
                print(f"\nScanning {complete_subdomain} for web technologies...\n")
                os.system(f"sudo wappy {complete_subdomain} -kbc -d '-'")
            except (FileExistsError, FileNotFoundError, ConnectionError):
                pass


if len(sys.argv) < 3:
    print("*" * 50)
    print("You did not provide any argument!")
    print("*" * 50)
    print("Syntax example:")
    print("python3 script.py google.com subdomains_dictionary.txt")
else:
    domain = sys.argv[1]
    txt_file = sys.argv[2]
    find_subdomain_and_scan(domain, txt_file)
    print("\nExit.")
    print("Hire me.")
