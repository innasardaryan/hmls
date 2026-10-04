import time
import requests
import threading
import multiprocessing

# List of URLs for performing parallel network requests
URLS = [
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/1"
]

def fetch_url(url):
    """Function for performing a single HTTP request"""
    try:
        response = requests.get(url, timeout=5)
        return len(response.content)
    except Exception as e:
        return f"Error: {e}"

# 1. Single-process version (sequential execution)
def run_single_process():
    start_time = time.time()
    results = []
    for url in URLS:
        results.append(fetch_url(url))
    end_time = time.time()
    print(f"Single-process time: {end_time - start_time:.2f} sec")

# 2. Multi-thread version (Multi-thread)
def run_multi_thread():
    start_time = time.time()
    threads = []
    
    for url in URLS:
        thread = threading.Thread(target=fetch_url, args=(url,))
        threads.append(thread)
        thread.start()
        
    for thread in threads:
        thread.join()
        
    end_time = time.time()
    print(f"Multi-thread time:   {end_time - start_time:.2f} sec")

# 3. Multi-process version (Multi-process)
def run_multi_process():
    start_time = time.time()
    processes = []
    
    for url in URLS:
        process = multiprocessing.Process(target=fetch_url, args=(url,))
        processes.append(process)
        process.start()
        
    for process in processes:
        process.join()
        
    end_time = time.time()
    print(f"Multi-process time:  {end_time - start_time:.2f} sec")


# Main entry point (protection against multiprocessing errors in Linux/VirtualBox)
if __name__ == '__main__':
    print("=== Execution Results ===")
    run_single_process()
    run_multi_thread()
    run_multi_process()
