# SubBruter  
# 🚀 Advanced Subdomain Bruteforcing Tool

```
  ____        _     _                 
 / ___| _   _| |__ | |__   ___  _ __  
 \___ \| | | | '_ \| '_ \ / _ \| '_ \ 
  ___) | |_| | |_) | |_) | (_) | | | |
 |____/ \__,_|_.__/|_.__/ \___/|_| |_|                                  

         SubBruter - Subdomain Bruteforcing Tool
```

# 🛠️ Installation
## ✅ Install with pipx directly from GitHub:
```
pipx install git+https://github.com/cristophercervantes/SubBruter.git
```

## 🔄 Updating the Tool
```
pipx upgrade subbruter
```

## ❌ Uninstalling
```
pipx uninstall subbruter
```

## 📝 Usage Examples
### Basic bruteforce:
```
subbruter -w wordlist.txt -u FUZZ.example.com
```

### Check HTTP Response:
```
subbruter -w wordlist.txt -u FUZZ.example.com --http
```

### Lookup DNS Records (e.g., MX):
```
subbruter -w wordlist.txt -u FUZZ.example.com --dns MX
```

### Save found subdomains to a file:
```
subbruter -w wordlist.txt -u FUZZ.example.com -o results.txt
```
### Show progress and failed attempts (verbose):
```
subbruter -w wordlist.txt -u FUZZ.example.com -v
```

### Change number of threads:
```
subbruter -w wordlist.txt -u FUZZ.example.com -t 50
```

# 🔹 All Command Options



