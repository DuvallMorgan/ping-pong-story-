def creative_director_bot():
    """
    UX Law: Goal Gradient Effect.
    The bot makes the user feel closer to a 'Perfect Video' with every word.
    """
    print("\n💬 [DIRECTOR]: Welcome to the Antigravity Suite.")
    print("DIRECTOR: Tell me your vision. I'll make it cinematic.")
    
    while True:
        user_input = input("\nYOU: ")
        
        if user_input.lower() in ['exit', 'quit', 'done']:
            break
            
        # THE SHIELD: If the input is too short or messy, the bot fixes it.
        if len(user_input) < 5:
            print("DIRECTOR: Give me more 'muscle' than that. Describe the light, the mood.")
            continue
            
        print(f"DIRECTOR: I see it. Adding ray-tracing and Picasso-bleed to '{user_input}'...")
        
        # This is where we trigger the Video Perfection sequence
        confirm = input("DIRECTOR: Shall we render the masterpiece? (y/n): ")
        if confirm.lower() == 'y':
            jensen_shield(launch_antigravity)
            break
          
