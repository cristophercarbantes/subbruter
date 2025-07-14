import socket
import threading
import argparse
from queue import Queue
import requests
import dns.resolver
from colorama import Fore, Style, init
import sys

init(autoreset=True)

q = Queue()
found = []
lock = threading.Lock()
progress_lock = threading.Lock()

progress_total = 0
progress_done = 0

def banner():
    print(r"""
  ____        _     _                 
 / ___| _   _| |__ | |__   ___  _ __  
 \___ \| | | | '_ \| '_ \ / _ \| '_ \ 
  ___) | |_| | |_) | |_) | (_) | | | |
 |____/ \__,_|_.__/|_.__/ \___/|_| |_|                                  

         SubBruter - Subdomain Bruteforcing Tool
    """)

def check_subdomain(subdomain, verbose, http_check, dns_record):
    try:
        ip = socket.gethostbyname(subdomain)
        status = ""
        if http_check:
            try:
                response = requests.get(f"http://{subdomain}", timeout=3)
                status = f" | HTTP {response.status_code}"
            except:
                status = " | HTTP Request Failed"

        if dns_record:
            try:
                answers = dns.resolver.resolve(subdomain, dns_record)
                records = ", ".join([str(r) for r in answers])
                status += f" | {dns_record} Record(s): {records}"
            except:
                status += f" | No {dns_record} Record"

        with lock:
            print(f"{Fore.GREEN}[FOUND] {subdomain} - {ip}{status}")
            found.append(f"{subdomain} - {ip}{status}")
    except socket.gaierror:
        if verbose:
            with lock:
                print(f"{Fore.RED}[FAILED] {subdomain}")

def worker(fuzz_target, verbose, http_check, dns_record):
    global progress_done
    while not q.empty():
        sub = q.get()
        subdomain = fuzz_target.replace("FUZZ", sub)
        check_subdomain(subdomain, verbose, http_check, dns_record)
        with progress_lock:
            progress_done += 1
            print(f"{Fore.CYAN}[PROGRESS] {progress_done}/{progress_total} words tested", end='\r', flush=True)
        q.task_done()

def main():
    global progress_total
    banner()

    parser = argparse.ArgumentParser(description="Advanced SubBruter with HTTP Check & DNS Records")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to wordlist file")
    parser.add_argument("-u", "--url", required=True, help="Target URL with FUZZ placeholder (e.g., FUZZ.example.com)")
    parser.add_argument("-t", "--threads", type=int, default=20, help="Number of threads (default: 20)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose mode for failed attempts")
    parser.add_argument("-o", "--output", help="Output file to save found subdomains")
    parser.add_argument("--http", action="store_true", help="Check HTTP response status of found subdomains")
    parser.add_argument("--dns", help="Check for specific DNS record (e.g., MX, TXT, NS)")
    args = parser.parse_args()

    try:
        with open(args.wordlist, "r") as f:
            wordlist_lines = [line.strip() for line in f if line.strip()]
            progress_total = len(wordlist_lines)
            for word in wordlist_lines:
                q.put(word)
    except FileNotFoundError:
        print(f"{Fore.RED}[ERROR] Wordlist file '{args.wordlist}' not found.")
        return

    print(f"[*] Starting brute-force on {args.url} with {args.threads} threads...")
    print(f"[*] Total words loaded: {progress_total}\n")

    threads = []
    for _ in range(args.threads):
        t = threading.Thread(target=worker, args=(args.url, args.verbose, args.http, args.dns))
        t.start()
        threads.append(t)

    q.join()

    if found:
        output_file = args.output if args.output else f"found_{args.url.replace('FUZZ.', '').replace('.', '_')}.txt"
        with open(output_file, "w") as f:
            for entry in found:
                f.write(entry + "\n")
        print(f"\n{Fore.GREEN}[+] Found {len(found)} subdomains. Saved to '{output_file}'")
    else:
        print(f"\n{Fore.YELLOW}[-] No subdomains found.")

def cli():
    main()
