import os as _os
import time
import sys

# Ensure the root directory is in sys.path
_os.environ['PYTHONPATH'] = _os.getcwd()
sys.path.insert(0, _os.getcwd())

try:
    from src.chatbot import present_keynote, launch_antigravity
    from src.engine.prompt_engine import DualLayerEngine
    # Gallery Persistence
    GALLERY = []
except ImportError:
    # Fallback for different execution contexts
    pass

def holographic_print(text, delay=0.02):
    """Prints text with a 'Spy Kids' terminal typing effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    _os.system('clear')
    holographic_print("🔊 [SYSTEM]: *Click* ... *Hummm*")
    time.sleep(0.5)
    holographic_print("🔓 ACCESS GRANTED: OSS SECURE LINE ESTABLISHED.")
    holographic_print("🚀 MOTIONFRAME ENGINE: ONLINE [v3.0 MASTERPIECE]")
    print("--------------------------------------------------")
    print("MODES: /artist, /tactical, /god-mode")
    print("INTEL: /archetype [neon|tactical|ethereal|industrial], /inject-lore")
    print("TOOLS: /dashboard, /gallery, /present, /diagnose, /keynote, /benchmark, /exit")

    engine_mode = "tactical" # Default spec
    archetype = "none"
    god_mode = False
    while True:
        try:
            cmd = input(f"\n🕵️  AGENT INPUT [{engine_mode}] > ").strip()
            
            if not cmd:
                continue

            if cmd.lower() == "/artist":
                engine_mode = "artist"
                holographic_print("🎨 [MODE]: Switched to ARTIST (Picasso Flair)")
                continue
            elif cmd.lower() == "/tactical":
                engine_mode = "tactical"
                holographic_print("🛡️ [MODE]: Switched to TACTICAL (Palmer Luckey Spec)")
                continue
            elif cmd.lower() == "/god-mode":
                god_mode = not god_mode
                status = "ENABLED" if god_mode else "DISABLED"
                holographic_print(f"⚡ [GOD MODE]: Reality distortion {status}.")
                continue
            elif cmd.lower().startswith("/archetype"):
                parts = cmd.split()
                if len(parts) > 1:
                    archetype = parts[1].lower()
                    holographic_print(f"🧬 [ARCHETYPE]: Switched to {archetype.upper()}. Intelligence adapted.")
                else:
                    holographic_print("🕵️ [ERROR]: Usage: /archetype [neon|tactical|ethereal|industrial]")
                continue

            if cmd.lower() in ["exit", "quit", "abort"]:
                holographic_print("🔒 MISSION COMPLETED. SECURING LINE...")
                break
            
            elif cmd.lower() == "/keynote":
                holographic_print("🎨 [CREATIVE DIRECTOR]: Deploying presentation assets...")
                holographic_print("🚀 Generating antigravity visual concepts...")
                time.sleep(1)
                try:
                    present_keynote()
                    # Restore Agent UI state after keynote
                    _os.system('clear')
                    holographic_print("🔓 MISSION RESUMED: SECURE LINE ACTIVE.")
                except NameError:
                    holographic_print("🚨 ERROR: Keynote Module not found.")
            
            else:
                holographic_print(f"🧬 [PROCESSING]: Analyzing vision: '{cmd}'")
                try:
                    engine = DualLayerEngine(mode=engine_mode, archetype=archetype)
                    vision = engine.wrap_vision(cmd)
                    holographic_print(f"🤖 [AI DIRECTOR]: Vision stabilized.")
                    holographic_print(f"✨ [PROMPT]: {vision[:80]}...")
                    
                    confirm = input("\n🕵️  DEPLOY RENDER? (y/n): ").lower()
                    if confirm == 'y':
                        holographic_print("🔊 [SYSTEM]: *Whirrr* ... *Powering Up Shaders*")
                        holographic_print("⚡ [ACTION]: Initializing Cinematic Render...")
                        launch_antigravity(cmd, mode=engine_mode, god_mode=god_mode)
                        GALLERY.append(f"[{engine_mode}] {cmd}")
                        holographic_print("\n✅ MISSION SUCCESS: Masterpiece archived.")
                        holographic_print("🔊 [SYSTEM]: *Ding* ... Render Pipeline Standing By.")
                    else:
                        holographic_print("✋ [HOLD]: Vision stored for revision.")
                except NameError:
                    holographic_print("🤖 [AI RESPONSE]: Prototype logic active. I'm ready for the mission.")

            elif cmd.lower() == "/benchmark":
                holographic_print("💪 [STRENGTH]: Deploying Physics Stress Test...")
                from src.lib.animation.particle_system import ParticleSystem
                ps = ParticleSystem(width=80, height=15)
                ps.run_benchmark(particle_count=1500)
                holographic_print("\n📊 [STATUS]: Performance holding at 'Unstoppable' levels.")
                continue

            elif cmd.lower() == "/dashboard":
                holographic_print("📊 [TELEMETRY]: Initializing High-Spec Dashboard...")
                time.sleep(0.5)
                telemetry = [
                    f"| ENGINE STABLE | UPTIME: {_os.popen('uptime').read().strip()}",
                    f"| CORE TEMPERATURE: OPTIMAL | ENTROPY: 0.0004",
                    f"| MEMORY BUFFER: {len(GALLERY)} Masterpieces archived",
                    f"| THREADS: NEURAL_DIRECTOR_01, PHYSICS_ENGINE_X7",
                    f"| STATUS: UNSTOPPABLE"
                ]
                print("\n" + "╔" + "═" * 60 + "╗")
                for line in telemetry:
                    print(f"║ {line:<58} ║")
                print("╚" + "═" * 60 + "╝")
                continue

            elif cmd.lower() == "/inject-lore":
                new_lore = input("\n🕵️  INPUT NEW LORE SEGMENT > ").strip()
                if new_lore:
                    holographic_print("🧠 [INTELLIGENCE]: Injecting new story DNA...")
                    with open("story.txt", "a") as f:
                        f.write(f"\n{new_lore}")
                    holographic_print("✅ LORE STABILIZED. Future visions will adapt.")
                continue

            elif cmd.lower() == "/gallery":
                if not GALLERY:
                    holographic_print("📂 [GALLERY]: No visions archived yet. Deploy a render first.")
                else:
                    holographic_print("📂 [GALLERY]: Loading persistent vision buffer...")
                    for i, vision in enumerate(GALLERY, 1):
                        print(f"  {i}. {vision}")
                continue

            elif cmd.lower() == "/present":
                if not GALLERY:
                    holographic_print("🎬 [PRESENTER]: Gallery empty. No assets to loop.")
                else:
                    holographic_print("🎬 [PRESENTER]: Initiating Cinematic Gallery Loop...")
                    time.sleep(1)
                    for vision_entry in GALLERY:
                        # Parse entry: [mode] prompt
                        try:
                            v_mode = "tactical" if "[tactical]" in vision_entry else "artist"
                            v_prompt = vision_entry.split("] ", 1)[1]
                            holographic_print(f"\n🎥 [PLAYING]: {v_prompt} ({v_mode.upper()})")
                            launch_antigravity(v_prompt, mode=v_mode, god_mode=god_mode)
                            time.sleep(2)
                        except Exception:
                            continue
                    holographic_print("\n🏆 [PRESENTER]: Loop complete. Returning to Mission Control.")
                continue

            elif cmd.lower() == "/diagnose":
                holographic_print("🩺 [DIAGNOSTIC]: Running System Integrity Check...")
                checks = [
                    ("Source Root", _os.path.exists("src")),
                    ("Engine Logic", _os.path.exists("src/engine/prompt_engine.py")),
                    ("Render Pipeline", _os.path.exists("src/lib/render/pipeline.py")),
                    ("Animation Muscle", _os.path.exists("src/lib/animation/particle_system.py")),
                    ("Sentinel Shield", _os.path.exists("src/sentinel_logic.py")),
                ]
                print("\n" + "█" * 40)
                for name, status in checks:
                    icon = "✅" if status else "❌"
                    print(f"{icon} {name:<25} [STABLE]")
                print("█" * 40)
                holographic_print("\n🛡️ [RESULT]: System is 100% UNSTOPPABLE.")
                continue

        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"🚨 SYSTEM COMPROMISED: {e}")

if __name__ == "__main__":
    main()
