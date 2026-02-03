cat <<EOF > main.py
import os
import sys

def handle_spy_kids_logic(user_input):
    if "->" in user_input:
        parts = [p.strip() for p in user_input.split("->")]
        if len(parts) < 3:
            print("🚨 ERROR: Command must follow the pattern: /command -> 'Prompt' -> Action")
            return
            
        command, prompt, action = parts[0], parts[1], parts[2]

        if command == "/tactical":
            print(f"\n🎯 [STRIKE TEAM ACTIVATED]: Rendering {prompt}...")
        elif command == "/artist":
            print(f"\n🎨 [AESTHETIC MODE]: Visualizing {prompt}...")

        if "Deploy Render" in action:
            print("🚀 SENDING TO IMAGE ENGINE... DONE.\n")
    else:
        print(f"🕵️ Standby... Echoing raw signal: {user_input}")

def main():
    print("🚀 PING-PONG-STORY ENGINE ONLINE")
    while True:
        try:
            cmd = input("🕵️  AGENT INPUT > ").strip()
            if cmd.lower() in ["exit", "quit"]:
                break
            handle_spy_kids_logic(cmd)
        except EOFError:
            break

if __name__ == "__main__":
    main()
EOF
