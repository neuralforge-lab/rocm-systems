#!/usr/bin/env python3
"""GPU monitoring dashboard for ROCm systems."""
import subprocess
import time
import json

def get_gpu_info():
    result = subprocess.run(['rocm-smi', '--showproductname', '--showtemp', '--showpower', '--showuse', '--showmeminfo', 'vram', '--json'], 
                          capture_output=True, text=True)
    try:
        return json.loads(result.stdout)
    except:
        return {"raw": result.stdout}

def monitor_loop(interval=5):
    print("Starting GPU monitor... (Ctrl+C to stop)")
    while True:
        info = get_gpu_info()
        print(f"\n[{time.strftime('%H:%M:%S')}]")
        if isinstance(info, dict) and 'raw' in info:
            print(info['raw'][:500])
        else:
            print(json.dumps(info, indent=2)[:500])
        time.sleep(interval)

if __name__ == '__main__':
    monitor_loop()
