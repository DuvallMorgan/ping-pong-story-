import time
import os
from src.lib.render.pipeline import RenderPipeline
from src.engine.prompt_engine import DualLayerEngine

def run_demo():
    """MotionFrame v3.0 Masterpiece Demo Loop."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("🎬 [SHOWCASE]: Initializing MotionFrame v3.0 Masterpiece Demo...")
    time.sleep(1.5)

    masterpieces = [
        "A neon-drenched cyberpunk city in the rain, 8k ray-tracing",
        "Abstract oil painting of a nebula, vibrant pigment diffusion",
        "A lone samurai standing on a cliff at golden hour, cinematic parallax",
        "Futuristic garden with bioluminescent plants, supernova particle glow"
    ]

    engine = DualLayerEngine(mode="tactical")

    for i, prompt in enumerate(masterpieces, 1):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\n🎥 [DEMO {i}/4]: PROCESSING MASTERPIECE")
        print(f"   PROMPT: {prompt}")
        print("=" * 60)
        
        # Inject Lore and Muscle
        vision = engine.wrap_vision(prompt)
        time.sleep(1)
        
        # Run Pipeline
        pipeline = RenderPipeline(vision)
        pipeline.run_full_render()
        
        print("\n[PAUSE]: Masterpiece archived. Preparing next frame...")
        time.sleep(3)

    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" + "█" * 60)
    print("   🏆 DEMO COMPLETE: THE WORLD HAS SEEN THE UNSTOPPABLE")
    print("   MOTIONFRAME v3.0 | BY DUVALL & ANTIGRAVITY")
    print("█" * 60)

if __name__ == "__main__":
    try:
        run_demo()
    except KeyboardInterrupt:
        print("\n\n👋 Demo interrupted. Vision saved.")
