import asyncio
import aiohttp
import argparse
from tqdm.asyncio import tqdm_asyncio

BANNER = r"""
   ____        _     ____              _            
  / ___| _   _| |__ | __ ) _   _ _ __ | |_ ___ _ __ 
  \___ \| | | | '_ \|  _ \| | | | '_ \| __/ _ \ '__|
   ___) | |_| | |_) | |_) | |_| | | | | ||  __/ |   
  |____/ \__,_|_.__/|____/ \__,_|_| |_|\__\___|_|   

  Lightweight Async Subdomain Brute Forcer
  ----------------------------------------
"""

class ResultLogger:
    def __init__(self, output_file=None):
        self.output_file = output_file
        self.buffer = []
    
    def log(self, text):
        if self.output_file:
            self.buffer.append(text)
    
    def save(self):
        if self.output_file and self.buffer:
            with open(self.output_file, "w") as f:
                f.write("\n".join(self.buffer))
            print(f"\n✅ Results saved to {self.output_file}")

async def fetch(session, url, status_filter, logger, verbose):
    try:
        async with session.get(url, timeout=5) as response:
            status = response.status
            if (not status_filter) or (status in status_filter):
                line = f"[{status}] {url}"
                print(line)
                logger.log(line)
            elif verbose:
                print(f"[SKIP {status}] {url}")
    except asyncio.TimeoutError:
        if verbose:
            print(f"[TIMEOUT] {url}")
    except aiohttp.ClientError as e:
        if verbose:
            print(f"[ERROR] {url} -> {e}")

async def limited_fetch(session, url, sem, progress_bar, status_filter, logger, verbose):
    async with sem:
        await fetch(session, url, status_filter, logger, verbose)
        progress_bar.update(1)

async def brute_force(domain, wordlist, concurrency, status_filter, logger, verbose):
    total_requests = len(wordlist) * 2  # http + https for each subdomain

    connector = aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(connector=connector) as session:
        sem = asyncio.Semaphore(concurrency)
        tasks = []
        with tqdm_asyncio(total=total_requests, desc="Scanning", unit="req") as pbar:
            for sub in wordlist:
                sub = sub.strip()
                if not sub:
                    continue
                for proto in ["http", "https"]:
                    url = f"{proto}://{sub}.{domain}"
                    tasks.append(asyncio.create_task(
                        limited_fetch(session, url, sem, pbar, status_filter, logger, verbose)
                    ))
            await asyncio.gather(*tasks)
    logger.save()

def cli():
    print(BANNER)
    
    parser = argparse.ArgumentParser(description="Subdomain brute forcing tool (HTTP/HTTPS)")
    parser.add_argument("domain", help="Target domain (e.g., example.com)")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to subdomain wordlist")
    parser.add_argument("-c", "--concurrency", type=int, default=20, help="Concurrent requests (default: 20)")
    parser.add_argument("-o", "--output", help="Save valid results to file")
    parser.add_argument("-f", "--filter", help="Comma-separated status codes to filter (e.g. 200,301)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Show verbose output (timeouts, errors, skipped)")
    args = parser.parse_args()

    # Parse wordlist
    with open(args.wordlist, "r") as f:
        words = f.read().splitlines()

    # Parse status filter
    status_filter = None
    if args.filter:
        status_filter = {int(code.strip()) for code in args.filter.split(",")}

    logger = ResultLogger(args.output)

    asyncio.run(brute_force(args.domain, words, args.concurrency, status_filter, logger, args.verbose))

if __name__ == "__main__":
    cli()
