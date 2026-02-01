# SENTINEL-01: THE ARCHITECT'S GUARDRAIL
# This script validates AI recommendations to prevent hallucinations

def validate_motion_recommendation(ai_output, vision_labels):
    """
    Checks if the AI's motion suggestion matches the reality of the image.
    """
    # 1. THE FALLBACK DEFAULT (The "Ken Burns" Safety Net)
    fallback_config = {
        "effect": "ken-burns",
        "intensity": 0.5,
        "status": "FALLBACK_TRIGGERED",
        "reason": "AI confidence low or logic mismatch."
    }

    try:
        # 2. VALIDATION LOGIC (The Logic Gate)
        # If AI suggests 'parallax' but there is no depth (labels), it's a hallucination
        if ai_output['type'] == 'parallax' and 'landscape' not in vision_labels:
            print("⚠️ Hallucination Detected: Parallax suggested for non-landscape image.")
            return fallback_config

        # 3. SUCCESS (The Validated Signal)
        return {
            "effect": ai_output['type'],
            "intensity": ai_output.get('intensity', 0.7),
            "status": "VALIDATED",
            "reason": "Recommendation matches visual semantics."
        }

    except Exception as e:
        # If the AI's JSON is broken (Hallucination Type B)
        return fallback_config

# --- TEST THE SYSTEM ---
# Example: AI hallucinates parallax for a close-up face
ai_hallucination = {"type": "parallax", "intensity": 0.9}
current_image_labels = ["face", "portrait", "close-up"]

final_decision = validate_motion_recommendation(ai_hallucination, current_image_labels)
print(f"Final System Decision: {final_decision}")
