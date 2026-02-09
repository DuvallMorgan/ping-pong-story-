import subprocess
import time
import sys
import os
import signal

# --- MASTERPIECE ORCHESTRATION SPEC ---
API_CMD = ["python3", "-m", "uvicorn", "src.api.server:app", "--host", "0.0.0.0", "--port", "8000"]
WEB_CMD = ["npm", "run", "dev"]
WEB_DIR = "website"

def kill_port(port):
    """Tactical cleanup of blocked ports."""
    try:
        # Mac-spec port cleanup
        pid = subprocess.check_output(["lsof", "-ti", f":{port}"]).decode().strip()
        if pid:
            os.kill(int(pid), signal.SIGKILL)
            print(f"🛡️ [SENTINEL]: Port {port} secured.")
    except:
        pass

def launch():
    print("\n🚀 [MOTIONFRAME]: Initiating Global Launch Sequence (v3.3 Obsidian Void)...")
    
    # 1. Secured Perimeter
    kill_port(8000)
    kill_port(5173)
    
    # 2. Deploy Brain (API)
    print("🧠 [BRAIN]: Deploying Obsidian Bridge...")
    api_proc = subprocess.Popen(API_CMD, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    time.sleep(2) # Stabilize bridge
    
    # 3. Deploy Showcase (Web)
    print("🎨 [SHOWCASE]: Deploying Diamond Dashboard...")
    web_proc = subprocess.Popen(WEB_CMD, cwd=WEB_DIR, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    print("\n✅ [STATUS]: MISSION SUCCESSFUL.")
    print("🔗 API: http://localhost:8000")
    print("🔗 WEB: http://localhost:5173")
    print("\nPress Ctrl+C to sever the links and shutdown.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛡️ [SENTINEL]: Terminating Masterpiece session...")
        api_proc.terminate()
        web_proc.terminate()
        print("✅ Shutdown complete.")

if __name__ == "__main__":
    launch()
