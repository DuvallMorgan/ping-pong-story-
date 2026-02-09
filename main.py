import os
import sys
import time

def jensen_print(text):
    """NVIDIA-green terminal output."""
    print(f"\033[1;32m[ACCELERATED]\033[0m {text}")

def compute_logic(user_input):
    if "->" in user_input:
        pipeline = [p.strip() for p in user_input.split("->")]
        
        if len(pipeline) >= 3:
            asset = pipeline[1]
            env = pipeline[2]
            
            jensen_print(f"Instantiating Digital Twin: '{asset}'")
            time.sleep(0.4)
            jensen_print(f"Applying Omniverse Physics: '{env}'")
            
            if "Deploy Render" in user_input:
                print("🚀 [GPU CLUSTER]: Searing pixels... Render Complete.")
        else:
            jensen_print("⚠️ Pipeline incomplete. Needs: /cook -> Asset -> Physics")
    else:
        jensen_print(f"Echoing Raw Signal: {user_input}")

def main():
    os.system('clear')
    print("\033[1;32m🟢 OSS MOTIONFRAME | AGENT ATELIER\033[0m")
    print("Accelerating Generative Storytelling [SPY KIDS PROTOCOL]")
    print("-" * 40)
    while True:
        try:
            directive = input("\033[1;34m🕵️ AGENT >\033[0m ").strip()
            if directive.lower() in ["exit", "quit"]:
                break
            if not directive:
                continue
            compute_logic(directive)
        except (EOFError, KeyboardInterrupt):
            break

if __name__ == "__main__":
    main()
