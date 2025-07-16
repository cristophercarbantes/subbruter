# SubBruter

**SubBruter** is a **lightweight asynchronous subdomain brute forcing tool** that supports:

✅ HTTP & HTTPS checks  
✅ Status code filtering  
✅ Saving results to a file  
✅ Verbose mode for full scan details  
✅ Progress bar for scan tracking  
✅ Banner for a nice look

---

## ✨ Features

- **Async scanning** → super fast with `aiohttp`
- **No DNS resolution** → directly checks HTTP/HTTPS endpoints
- **Status code filtering** (`-f 200,301`)
- **Save valid results** to a file (`-o results.txt`)
- **Progress bar** with live request count
- **Verbose mode** → see timeouts, skipped codes, and errors
- **Supports pipx installation**

---

## 📦 Installation

Clone and install via **pipx** (recommended):

```bash
git clone https://github.com/yourusername/subbruter.git
cd SubBruter
pipx install .
```

Alternatively, install with `pip`:

```bash
pip install .
```

---

## 🚀 Usage

```bash
subbruter <domain> -w <wordlist> [options]
```

### **Basic example**

```bash
subbruter example.com -w subdomains.txt
```

This will:
✅ Scan all subdomains from the wordlist
✅ Check both HTTP & HTTPS
✅ Show status codes

---

### **Filter status codes**

```bash
subbruter example.com -w subs.txt -f 200,301
```
Only shows **200 OK** and **301 Redirect** results.

---

### **Save results to a file**

```bash
subbruter example.com -w subs.txt -f 200,301 -o valid.txt
```
Saves valid subdomains to `valid.txt` after the scan.

---

### **Verbose mode**

```bash
subbruter example.com -w subs.txt -f 200,301 -v
```

Shows everything, including:
- `[SKIP 404]` for non-matching codes
- `[TIMEOUT]` for unresponsive hosts
- `[ERROR]` for connection issues

---

### **Combine all features**

```bash
subbruter example.com -w subs.txt -f 200,301 -o results.txt -c 50 -v
```

- **Filters only 200 & 301**
- **Saves valid results to results.txt**
- **Uses concurrency 50 for faster scan**
- **Verbose output with errors/timeouts**

---

## 🖥 Example Output

```
   ____        _     ____              _            
  / ___| _   _| |__ | __ ) _   _ _ __ | |_ ___ _ __ 
  \___ \| | | | '_ \|  _ \| | | | '_ \| __/ _ \ '__|
   ___) | |_| | |_) | |_) | |_| | | | | ||  __/ |   
  |____/ \__,_|_.__/|____/ \__,_|_| |_|\__\___|_|   

  Lightweight Async Subdomain Brute Forcer
  ----------------------------------------

Scanning:  43%|██████████▏             | 86/200 [00:03<00:04, 22.1req/s]
[200] https://api.example.com
[301] http://dev.example.com
[SKIP 404] http://blog.example.com
[TIMEOUT] https://staging.example.com

✅ Results saved to results.txt
```

---

## ⚙ Options

| Option            | Description |
|-------------------|-------------|
| `-w, --wordlist`  | Path to subdomain wordlist (**required**) |
| `-c, --concurrency` | Number of concurrent requests (default: `20`) |
| `-f, --filter`    | Comma-separated list of status codes to show (e.g. `200,301`) |
| `-o, --output`    | Save valid results to a file |
| `-v, --verbose`   | Show verbose output (timeouts, errors, skipped) |

---

## 📋 Example Commands

- **Fast scan with concurrency 50**
  ```bash
  subbruter example.com -w subs.txt -c 50
  ```

- **Save only valid 200/301 results to file**
  ```bash
  subbruter example.com -w subs.txt -f 200,301 -o valid.txt
  ```

- **Full verbose debug scan**
  ```bash
  subbruter example.com -w subs.txt -v
  ```

---

## 🛠 Tech

- **Python 3.8+**
- **aiohttp** for async HTTP requests
- **tqdm** for progress bar

---

## 🔥 Why use SubBruter?

- ✅ **Fast** → async with concurrency
- ✅ **Lightweight** → minimal dependencies
- ✅ **Simple** → no DNS resolution, just HTTP/HTTPS checks
- ✅ **Flexible** → filters, output saving, verbose

---

## 📜 License

MIT License – free to use, modify, and share.
