
# UI/UX Pattern Analysis - Relay AI Triage

## 1. Doherty Threshold (The 400ms Rule)
- **Concept:** Productivity skyrockets when a system and its users interact at a pace faster than 400ms.
- **Application:** In my triage tool, I ensured that clicking "Analyze Ticket" triggers an immediate visual response (a skeleton loader or button animation). This prevents "Technical Volatility" and keeps the support agent in a flow state.

## 2. Postel’s Law (The Robustness Principle)
- **Concept:** "Be conservative in what you do, be liberal in what you accept from others."
- **Application:** I designed the AI input to be "chill" with messy user data. If a customer sends a misspelled ticket (e.g., "resturnt help"), the interface doesn't crash or error out. It stays flexible, corrects the intent on the back-end, and keeps the process moving.

## 3. Peak-End Rule
- **Concept:** People judge an experience largely based on how they felt at its peak and at its end.
- **Application:** I focused on making the "Success" state of the triage process feel rewarding. By providing a clear, satisfying summary once a ticket is resolved, I ensure the user leaves the application feeling productive and successful.

## Future Improvements
- **Hick's Law:** I plan to simplify the categorization menu to reduce "Choice Overload" for the agents.
- **Fitts's Law:** I want to increase the target size of the "High Priority" buttons to make them easier to hit during high-speed triage.
