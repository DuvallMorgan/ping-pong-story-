import random
import time
import sys
import os
from src.lib.animation.particle_system import ParticleSystem

# --- CONFIGURATION ( Jensen's Shield: Configuration Layer ) ---
CANVAS_WIDTH = 80
CANVAS_HEIGHT = 15
ANIMATION_SPEED = 0.05
ANIMATION_CYCLES = 30
# --- PALETTES ( Logic Layers ) ---
ARTIST_PALETTE = [
    "\033[38;5;196m", # Electric Red
    "\033[38;5;201m", # Neon Pink
    "\033[38;5;45m",  # Deep Sky Blue
    "\033[38;5;46m",  # Spring Green
    "\033[38;5;226m", # Pure Yellow
    "\033[0m"         # Reset
]

TACTICAL_PALETTE = [
    "\033[38;5;196m", # Infrared Red
    "\033[38;5;235m", # Tactical Grey
    "\033[38;5;238m", # Steel grey
    "\033[38;5;202m", # Alert Orange
    "\033[0m"         # Reset
]

# --- PERFORMANCE SPEC ( Platinum Layer ) ---
GOD_MODE_INTENSITY = 2.0
GOD_MODE_PALETTE = [
    "\033[38;5;196m", "\033[38;5;201m", "\033[38;5;45m",
    "\033[38;5;46m", "\033[38;5;226m", "\033[38;5;231m", # High-intensity white
    "\033[0m"
]

DIAMOND_PALETTE = [
    "\033[38;5;45m",  # Diamond Blue
    "\033[38;5;231m", # Pure White
    "\033[38;5;201m", # Neon Pink
    "\033[38;5;46m",  # Spring Green
    "\033[38;5;196m", # Alert Red
    "\033[0m"
]

OBSIDIAN_PALETTE = [
    "\033[38;5;93m",  # Deep Purple
    "\033[38;5;129m", # Electric Indigo
    "\033[38;5;231m", # Stellar White
    "\033[38;5;232m", # Void Black
    "\033[38;5;45m",  # Nebula Blue
    "\033[0m"
]

def parallax_render(text, depth=1):
    """
    Creates a 3D parallax effect in the terminal.
    Higher depth moves slower.
    """
    padding = " " * (int(time.time() * 5 / depth) % 20)
    print(f"\033[90m{padding}{text}\033[0m")

def picasso_paint_bleed(mode="artist", god_mode=False):
    """
    Now mode-driven to support the Palmer Luckey vs Picasso vision.
    God Mode: Doubled intensity, Supernova finales.
    Diamond Mode: The ultimate "Room Killer" merge.
    Obsidian Mode: Void-Spec deep-space physics.
    """
    if mode == "diamond":
        palette = DIAMOND_PALETTE
        label = "💎 DIAMOND SHOWCASE"
    elif mode == "obsidian":
        palette = OBSIDIAN_PALETTE
        label = "🖤 OBSIDIAN VOID"
    else:
        palette = GOD_MODE_PALETTE if god_mode else (TACTICAL_PALETTE if mode == "tactical" else ARTIST_PALETTE)
        label = "GOD MODE: ACTIVE" if god_mode else ("TACTICAL INFRARED" if mode == "tactical" else "ARTIST MODE")
    
    ps = ParticleSystem(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, colors=palette)
    cycles = ANIMATION_CYCLES * 4 if mode == "obsidian" else (ANIMATION_CYCLES * 3 if mode == "diamond" else (ANIMATION_CYCLES * 2 if god_mode else ANIMATION_CYCLES))
    
    print(f"\n🎨 [{label}]: Beginning Pigment Diffusion...")
    if mode == "diamond" or mode == "obsidian":
        print(f"🛡️ [SENTINEL]: Sentinel Logic v2.1 engaged for {mode.capitalize()} Verification.")
    
    if mode == "obsidian":
        ps.gravity = [0.0, 0.0] # Zero-G in the Void
        ps.friction = 0.01
    
    time.sleep(1)

    for i in range(cycles):
        if i % 5 == 0:
            parallax_render(f"::: {label} :::", depth=3)
        
        # Emission Logic
        if mode == "obsidian":
            # Void Implosion
            if i < cycles // 2:
                ps.emit(random.choice([0, CANVAS_WIDTH-1]), random.randint(0, CANVAS_HEIGHT-1), count=4)
            else:
                # Event Horizon Implosion
                ps.emit_supernova(CANVAS_WIDTH//2, CANVAS_HEIGHT//2, count=2)
                ps.gravity = [0.0, 0.05] # Returning gravity
        elif mode == "diamond":
            ps.emit_supernova(CANVAS_WIDTH//2, CANVAS_HEIGHT//2, count=5)
            ps.emit(random.randint(0, CANVAS_WIDTH-1), 0, count=2)
            ps.emit(random.randint(0, CANVAS_WIDTH-1), CANVAS_HEIGHT-1, count=2)
        elif god_mode:
            ps.emit_supernova(random.randint(0, CANVAS_WIDTH-1), random.randint(0, CANVAS_HEIGHT-1), count=10)
        elif mode == "tactical" and i % 10 == 0:
            ps.emit_supernova(CANVAS_WIDTH//2, 0, count=10)
        else:
            ps.emit(random.randint(0, CANVAS_WIDTH-1), 0, count=3)
        
        speed_boost = 4 if mode == "obsidian" else (3 if mode == "diamond" else (2 if god_mode else 1))
        ps.render(frames=1, delay=ANIMATION_SPEED / speed_boost)
        
    if god_mode:
        print("\n💥 [GOD MODE]: Initiating Supernova Finale...")
        ps.emit_supernova(CANVAS_WIDTH//2, CANVAS_HEIGHT//2, count=100)
        ps.render(frames=20, delay=0.01)

    print(f"\n✅ {label} stabilized.")

if __name__ == "__main__":
    picasso_paint_bleed()
  
