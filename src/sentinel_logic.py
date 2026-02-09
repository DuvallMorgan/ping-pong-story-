"""
SENTINEL 2.0: THE ARCHITECT'S GUARDRAIL
Unbreakable semantic validation for the MotionFrame Render Pipeline.
Inspired by Jensen Huang's 'No-Failure' engineering philosophy.
"""

def validate_motion_recommendation(ai_output, vision_labels):
    """
    SENTINEL v2.1 (Obsidian Spec): 
    Validates AI motion suggestions and returns a rich diagnostic signature.
    """
    # 💎 THE MASTERPIECE FALLBACK (Ken Burns Spec)
    fallback_config = {
        "effect": "ken-burns",
        "intensity": 0.5,
        "status": "FALLBACK_TRIGGERED",
        "reason": "AI logic mismatch. Deploying safe cinematic default.",
        "gates": {
            "semantic": "FAIL",
            "hallucination": "ALERT",
            "fallback": "ACTIVE"
        }
    }

    try:
        # 1. INDUSTRIAL-SPEC VALIDATION
        if not isinstance(ai_output, dict) or not isinstance(vision_labels, (list, tuple, set)):
            return fallback_config

        # 2. LOGIC GATE: MOVEMENT VS SEMANTICS
        rec_type = ai_output.get('type')
        if not rec_type:
            return fallback_config
            
        intensity = ai_output.get('intensity', 0.5)
        
        # Diagnostic results for the Web Hub
        gates = {
            "semantic": "VERIFIED",
            "hallucination": "CLEAN",
            "fallback": "STANDBY"
        }

        # Hallucination Check: Parallax requires Z-depth
        depth_cues = ["landscape", "city", "street", "mountain", "nebula"]
        if rec_type == 'parallax' and not any(cue in vision_labels for cue in depth_cues):
            print("🛡️ [SENTINEL]: Hallucination Intercepted. Parallax requires depth cues.")
            gates["hallucination"] = "INTERCEPTED"
            gates["fallback"] = "ACTIVE"
            return {**fallback_config, "gates": gates, "reason": "Parallax mismatch: No depth cues."}

        # Hallucination Check: Fluid Flow requires liquid/flow semantics
        flow_cues = ["water", "fire", "smoke", "nebula", "rain", "abstract"]
        if rec_type == 'fluid_flow' and not any(cue in vision_labels for cue in flow_cues):
            print("🛡️ [SENTINEL]: Logic Mismatch. Fluid-flow requires fluid semantics.")
            gates["hallucination"] = "INTERCEPTED"
            gates["fallback"] = "ACTIVE"
            return {**fallback_config, "gates": gates, "reason": "Fluid-flow mismatch: No fluid semantics."}

        # Hallucination Check: Obsidian/Void requires depth or stellar cues
        void_cues = ["nebula", "stellar", "galaxy", "black hole", "void", "space", "landscape"]
        if rec_type == 'obsidian' and not any(cue in vision_labels for cue in void_cues):
            print("🛡️ [SENTINEL]: Logic Mismatch. Obsidian/Void requires stellar or depth cues.")
            gates["hallucination"] = "INTERCEPTED"
            gates["fallback"] = "ACTIVE"
            return {**fallback_config, "gates": gates, "reason": "Obsidian/Void mismatch: No stellar/depth cues."}

        # 3. VERIFIED SIGNAL
        return {
            "effect": rec_type,
            "intensity": intensity,
            "status": "VALIDATED",
            "reason": "Kinetic profile matches semantic signature.",
            "gates": gates
        }

    except Exception as e:
        print(f"🛡️ [SENTINEL]: Critical failure in validation logic: {e}")
        return fallback_config
