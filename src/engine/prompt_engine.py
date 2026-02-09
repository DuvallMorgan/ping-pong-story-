# The Intelligence: Dual-Layer Prompt Engine

# Layer 1: The "Anduril" Tactical Preset - Palmer Luckey Spec
PALMER_MUSCLE = (
    "rugged industrialism, matte black carbon fiber, infrared sensor glow, "
    "mechanical precision, high-torque actuators, tactical telemetry overlays, "
    "aerospace-grade aluminum, harsh desert lighting, shot on RED V-Raptor"
)

# Layer 2: Picasso Bleed - Artistic Flair
PICASSO_FLAIR = (
    "surrealist fluid dynamics, wet oil paint bleed, high-contrast chiaroscuro, "
    "dynamic brushstrokes, vibrant pigment diffusion, abstract geometric forms"
)

class DualLayerEngine:
    """
    Combines Technical Precision with Artistic Flair.
    Inspired by Jensen Huang's Nvidia and Steve Jobs' Apple design logic.
    Injects MotionFrame lore for a 'one-of-a-kind' source.
    """
    def __init__(self, mode="tactical", archetype="none"):
        self.mode = mode
        self.archetype = archetype.lower()
        self.lore = self._load_lore()

    def _get_archetype_prompt(self):
        archetypes = {
            "neon": "STYLING: Cyberpunk, high-contrast, bioluminescent gradients.",
            "tactical": "STYLING: Rugged industrial, infrared overlays, HUD elements.",
            "ethereal": "STYLING: Soft pigment diffusion, dreamlike, surrealist light play.",
            "industrial": "STYLING: Raw steel, monochrome with alert orange accents, heavy machinery.",
            "none": ""
        }
        return archetypes.get(self.archetype, "")

    def _load_lore(self):
        try:
            with open("product-analysis.txt", "r") as f:
                analysis = f.read().strip()
            with open("story.txt", "r") as f:
                story = f.read().strip()
            return f"{analysis}\n{story}"
        except Exception:
            return "MotionFrame: The future of Text-to-Motion."

    def wrap_vision(self, prompt):
        # Re-load lore in case it was dynamically updated
        self.lore = self._load_lore()
        
        archetype_spec = self._get_archetype_prompt()
        context = "Focus on cinematic strike-team efficiency" if self.mode == "tactical" else "Embrace surrealist pigment diffusion"
        
        if self.mode == "tactical":
            wrapped = f"MISSION CRITICAL VISION: {prompt}. {archetype_spec} CONTEXT: {context}."
        else:
            wrapped = f"ARTISTIC MASTERPIECE: {prompt}. {archetype_spec} CONTEXT: {context}."
        
        print(f"🧠 [INTELLIGENCE]: Injecting dual-layer logic and lore... ({self.mode} mode)")
        return wrapped

def apply_muscle(user_input):
    """Legacy wrapper for backward compatibility."""
    engine = DualLayerEngine(mode="tactical")
    return engine.wrap_vision(user_input)
