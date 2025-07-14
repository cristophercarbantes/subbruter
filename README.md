# SubBruter - Advanced Subdomain Brute Forcing tool

```
  ____        _     _                 
 / ___| _   _| |__ | |__   ___  _ __  
 \___ \| | | | '_ \| '_ \ / _ \| '_ \ 
  ___) | |_| | |_) | |_) | (_) | | | |
 |____/ \__,_|_.__/|_.__/ \___/|_| |_|                                  

         SubBruter - Subdomain Bruteforcing Tool
```

# Features
✅ Subdomain brute-forcing with wordlist

✅ Multi-threaded for speed

✅ HTTP/HTTPS status code checker (--http)

✅ DNS record lookup (e.g., MX, TXT, NS) (--dns)

✅ Verbose mode for failed attempts (-v)

✅ Save results to a file with -o

✅ Clean colored terminal output

# Installation

# 1️⃣ Clone the repository:
```
git clone https://github.com/yourusername/SubBruter.git
cd SubBruter
```

# 2️⃣ Install required Python packages:
```
pip install -r requirements.txt
```


# Usage
```
python3 subbruter.py -w wordlist.txt -u FUZZ.example.com -t 30 --http --dns MX -o results.txt -v
```

# Usage:
## Option------------Description
```-w                   / --wordlist	Path to wordlist file (Required)
-u                   / --url	Target with FUZZ placeholder (Required)
-t                  / --threads	Number of threads (Default: 20)
-v                 / --verbose	Verbose mode for failed attempts
-o                / --output	Output file to save results
--http	          Check HTTP response status
--dns	           Lookup DNS record type (e.g., MX, TXT, NS)```



