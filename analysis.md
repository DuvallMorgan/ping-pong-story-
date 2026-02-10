## UX/UI Pattern Analysis

### 1. Doherty Threshold (The 400ms Rule)
- **Finding:** System response must be under 400ms to maintain user flow.
- **Application:** My Triage button provides instant visual feedback (animations) to prevent "Technical Volatility" while the AI processes.


### 2. Postel’s Law (The Robustness Principle)
- **Finding:** Be conservative in what you send, liberal in what you accept.
- **Application:** The Relay AI tool handles misspelled or "messy" support tickets (e.g., "resturnt help") by extracting intent rather than throwing an error.


### 3. Peak-End Rule
- **Finding:** Users judge an experience by its most intense point and its end.
- **Application:** I optimized the "Success State" after a ticket is triaged to ensure the agent ends their task with a sense of accomplishment.
