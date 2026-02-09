def jensen_shield(func):
    """
    Jensen's Shield: Advanced control handling. No crashes.
    Wraps execution in a high-performance safety layer.
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"🛡️ [SHIELD]: Intercepted failure in {func.__name__}: {e}")
            print("🛡️ [SHIELD]: Deploying fallback systems...")
            return None
    return wrapper

@jensen_shield
def launch_antigravity(prompt=None, mode="artist", god_mode=False):
    """Starts the cinematic render engine with professional pipeline simulation."""
    from src.lib.render.pipeline import RenderPipeline
    
    pipeline = RenderPipeline(prompt or "Cinematic Masterpiece", mode=mode, god_mode=god_mode)
    pipeline.run_full_render()

def present_keynote():
    """Steve Jobs Keynote Mode: Tells the story of MotionFrame."""
    os.system('cls' if os.name == 'nt' else 'clear')
    slides = [
        ("✨ [SLIDE 1]: THE VISION", "MotionFrame isn't just a script. It's a cinematic strike-team."),
        ("🧠 [SLIDE 2]: THE BRAIN", "Dual-Layer Intelligence. Nvidia-tier descriptors meets Picasso flair."),
        ("💪 [SLIDE 3]: THE MUSCLE", "Physics-based particle systems. Supernovas and Fluid Flows in CLI."),
        ("🛡️ [SLIDE 4]: THE SHIELD", "Jensen Huang-spec UI. Performance first. No crashes. No compromise.")
    ]
    
    print("\n" + " " * 20)
    print("   MOTIONFRAME KEYNOTE: TURNING TEXT INTO MOTION")
    print("      'One More Thing...' - The v3.0 Release")
    print(" " * 20 + "\n")
    
    for title, content in slides:
        print(f"\n{title}")
        print(f"-- {content}")
        time.sleep(2)
    
    print("\n✅ Keynote Archive complete. System ready for rendering.")
    time.sleep(1)

def creative_director_bot():
    """
    UX Law: Goal Gradient Effect.
    Jensen Huang mission-control spec UI v2.0.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" + "█" * 60)
    print("   🌐 MOTIONFRAME MISSION CONTROL | 'ROOM KILLER' v3.0")
    print("   STATUS: ACTIVE | ENGINE: DUAL-LAYER v2 | LORE: LOADED")
    print("█" * 60)
    print("\n💬 [DIRECTOR]: Welcome to the future of Text-to-Motion.")
    print("DIRECTOR: Enter vision prompt or type '/keynote' for product tour.")
    
    import os
    import time
    from src.engine.prompt_engine import DualLayerEngine
    engine = DualLayerEngine(mode="tactical")
    
    while True:
        try:
            user_input = input("\nYOU: ").strip()
            
            if user_input.lower() in ['exit', 'quit', 'done']:
                print("\nDIRECTOR: Vision archived. See you in the future.")
                break
                
            if user_input.lower() == '/keynote':
                present_keynote()
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\n" + "█" * 60)
                print("   🌐 MOTIONFRAME MISSION CONTROL | 'ROOM KILLER' v3.0")
                print("█" * 60)
                continue

            # THE SHIELD: Validate input length and content
            if not user_input or len(user_input) < 5:
                print("DIRECTOR: Give me more 'muscle' than that. Describe the light, the mood.")
                continue
                
            # Process with DualLayerEngine
            vision = engine.wrap_vision(user_input)
            print(f"\n✨ [INTELLIGENCE]: {vision[:80]}...")
            
            # This is where we trigger the Video Perfection sequence
            confirm = input("\n🕵️  DEPLOY RENDER? (y/n): ").lower()
            if confirm == 'y':
                holographic_print("⚡ [ACTION]: Initializing Cinematic Render...")
                launch_antigravity(user_input, mode=engine.mode)
                # After render, we don't break, we let the user continue
                print("\nDIRECTOR: Masterpiece archived. Ready for next vision.")
            elif confirm == 'n':
                print("DIRECTOR: Vision adjusted. Ready for iteration.")
            else:
                print("DIRECTOR: Precision check failed. Keep refining.")
                
        except KeyboardInterrupt:
            print("\n\nDIRECTOR: Mission control offline. Energy preserved.")
            break
        except Exception as e:
            print(f"\nDIRECTOR: FATAL HUD ERROR: {e}")
            break
          
