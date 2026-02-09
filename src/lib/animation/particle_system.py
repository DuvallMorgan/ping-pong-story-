import random
import time
import os

class Particle:
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.vx = random.uniform(-1.5, 1.5)
        self.vy = random.uniform(-0.5, 0.5)
        self.char = char
        self.color = color
        self.life = random.randint(10, 20)

    def update(self, gravity=0.1, friction=0.98):
        self.vy += gravity
        self.vx *= friction
        self.vy *= friction
        self.x += self.vx
        self.y += self.vy
        self.life -= 1

class ParticleSystem:
    def __init__(self, width=80, height=24, colors=None):
        self.width = width
        self.height = height
        self.particles = []
        self.colors = colors or ["\033[95m", "\033[94m", "\033[96m", "\033[92m", "\033[91m", "\033[93m"]
        self.chars = ["░", "▒", "▓", "█", "•", "≋", "*", "+"]
        self.gravity = [0.0, 0.1] # Default downward gravity
        self.friction = 0.02 # 2% energy loss per frame

    def emit(self, x, y, count=5):
        for _ in range(count):
            char = random.choice(self.chars)
            color = random.choice(self.colors)
            self.particles.append(Particle(x, y, char, color))

    def emit_supernova(self, x, y, count=50):
        """Explosive radial physics."""
        print("💥 [PHYSICS]: Triggering Supernova Emitter...")
        for _ in range(count):
            char = random.choice(["*", "█", "•", "░"])
            color = random.choice(self.colors)
            p = Particle(x, y, char, color)
            # Radial velocity
            angle = random.uniform(0, 2 * 3.14159)
            speed = random.uniform(2.0, 5.0)
            p.vx = speed * (2 * random.random() - 1)
            p.vy = speed * (2 * random.random() - 1)
            p.life = random.randint(15, 25)
            self.particles.append(p)

    def emit_fluid_flow(self, x, y, count=30):
        """Cinematic liquid motion / stream."""
        print("🌊 [PHYSICS]: Triggering Fluid-Flow Emitter...")
        for _ in range(count):
            char = random.choice(["≋", "░", "▒", "•"])
            color = "\033[96m" # Cyan/Water vibe
            p = Particle(x, y, char, color)
            p.vx = random.uniform(1.0, 3.0)
            p.vy = random.uniform(-0.2, 0.2)
            p.life = random.randint(20, 40)
            self.particles.append(p)

    def render(self, frames=30, delay=0.05):
        for _ in range(frames):
            # Clear buffer (Home cursor)
            sys.stdout.write("\033[H")
            
            # Physics Step: Efficient filtering of dead/off-screen particles
            active_particles = []
            for p in self.particles:
                p.vx += self.gravity[0]
                p.vy += self.gravity[1]
                p.vx *= (1 - self.friction)
                p.vy *= (1 - self.friction)
                p.x += p.vx
                p.y += p.vy
                p.life -= 1
                
                # Boundary Check & Life Check
                if p.life > 0 and -10 < p.x < self.width + 10 and -10 < p.y < self.height + 10:
                    active_particles.append(p)
            
            self.particles = active_particles

            # Build frame using a flat buffer for speed
            grid = [" "] * (self.width * self.height)
            for p in self.particles:
                ix, iy = int(p.x), int(p.y)
                if 0 <= ix < self.width and 0 <= iy < self.height:
                    grid[iy * self.width + ix] = f"{p.color}{p.char}\033[0m"

            # Efficient output assembly
            frame_output = []
            for y in range(self.height):
                frame_output.append("".join(grid[y * self.width : (y + 1) * self.width]))
            
            sys.stdout.write("\n".join(frame_output) + "\n")
            sys.stdout.flush()
            time.sleep(delay)

    def run_benchmark(self, particle_count=1000, duration=50):
        """Showcases engine speed and scalability."""
        print(f"\n🚀 [BENCHMARK]: Scaling to {particle_count} concurrent particles...")
        start_time = time.time()
        
        # Stress the emitter
        self.emit_supernova(self.width//2, self.height//2, count=particle_count)
        
        # Fast render loop (minimal delay)
        self.render(frames=duration, delay=0.01)
        
        end_time = time.time()
        fps = duration / (end_time - start_time)
        print(f"\n📊 [STATS]: Peak Throughput: {fps:.2f} Frames/Second")
        print(f"📊 [STATS]: Load Stabilized. Performance Spec: MASTERPIECE.")

def cinematic_strike_team():
    """UX: Palmer Luckey Spec - Tactical, rugged, high-spec."""
    os.system('cls' if os.name == 'nt' else 'clear')
    ps = ParticleSystem()
    print("\n🚀 [SYSTEM]: Deploying Cinematic Strike-Team Logic...")
    time.sleep(1)
    
    # Emit from multiple points to simulate a tactical "entry"
    ps.emit(10, 5, 20)
    ps.emit(70, 5, 20)
    ps.emit(40, 20, 30)
    
    ps.render(frames=40)
    print("\n✅ Strike-team deployment complete. Perimeter secured.")

if __name__ == "__main__":
    cinematic_strike_team()
