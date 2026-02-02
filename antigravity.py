import random

def picasso_paint_bleed():
    """
    UX LAW: Aesthetic-Usability Effect.
    Creates a visual 'bleed' that makes the render feel like a living painting.
    """
    palette = ["\033[95m", "\033[94m", "\033[96m", "\033[92m", "\033[0m"]
    canvas_width = 40
    
    print("\n🎨 [ARTIST MODE]: Beginning Pigment Diffusion...")
    
    for _ in range(15):
        # Create a 'swirl' of random colors and symbols
        line = "".join(random.choice(["░", "▒", "▓", "█", "•", "≋"]) for _ in range(canvas_width))
        color = random.choice(palette)
        
        # Shift the line to simulate 'bleeding' motion
        padding = " " * random.randint(0, 5)
        print(f"{padding}{color}{line}\033[0m")
        time.sleep(0.15)
        
    print("\n✅ Canvas saturated. Picasso-bleed stabilized.")
  
