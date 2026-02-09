import './style.css'

// --- PING-PONG-STORY: THE OBSIDIAN MASTERPIECE ---

// 1. Picasso-Bleed Background Animation
const canvas = document.getElementById('picasso-canvas');
const ctx = canvas.getContext('2d');
let particles = [];

function resize() {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
}

window.addEventListener('resize', resize);
resize();

class Particle {
  constructor() {
    this.reset();
  }

  reset() {
    this.x = Math.random() * canvas.width;
    this.y = Math.random() * canvas.height;
    this.size = Math.random() * 100 + 50;
    this.color = ['#ff3c3c', '#ff00ff', '#00d2ff', '#00ff8c'][Math.floor(Math.random() * 4)];
    this.vx = (Math.random() - 0.5) * 1.5;
    this.vy = (Math.random() - 0.5) * 1.5;
    this.alpha = Math.random() * 0.4 + 0.1;
  }

  update() {
    this.x += this.vx;
    this.y += this.vy;

    if (this.x < -this.size || this.x > canvas.width + this.size ||
      this.y < -this.size || this.y > canvas.height + this.size) {
      this.reset();
    }
  }

  draw() {
    ctx.globalAlpha = this.alpha;
    ctx.fillStyle = this.color;
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
    ctx.fill();
  }
}

function initParticles() {
  particles = [];
  for (let i = 0; i < 30; i++) {
    particles.push(new Particle());
  }
}

function animate() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  particles.forEach(p => {
    p.update();
    p.draw();
  });
  requestAnimationFrame(animate);
}

initParticles();
animate();

// 2. Reveal Animations (Intersection Observer)
const observerOptions = {
  threshold: 0.1
};

const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, observerOptions);

document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

// 3. The Muscle Lab: Ping-Pong Physics
const pCanvas = document.getElementById('physics-canvas');
const pCtx = pCanvas.getContext('2d');
const pWrapper = document.querySelector('.physics-canvas-wrapper');
const pScore = document.getElementById('physics-score');
const pVelocity = document.getElementById('physics-velocity');

let isPhysicsRunning = false;
let score = 0;
let ball = { x: 0, y: 0, vx: 5, vy: 5, radius: 10 };
let paddle = { x: 0, width: 80, height: 10 };

function initPhysics() {
  pCanvas.width = pWrapper.clientWidth;
  pCanvas.height = 500;
  ball.x = pCanvas.width / 2;
  ball.y = pCanvas.height / 2;
  paddle.x = pCanvas.width / 2 - paddle.width / 2;
}

pWrapper.addEventListener('click', () => {
  if (!isPhysicsRunning) {
    pWrapper.classList.add('active');
    isPhysicsRunning = true;
    initPhysics();
    runPhysics();
  }
});

pCanvas.addEventListener('mousemove', (e) => {
  const rect = pCanvas.getBoundingClientRect();
  paddle.x = e.clientX - rect.left - paddle.width / 2;
});

function runPhysics() {
  if (!isPhysicsRunning) return;

  pCtx.clearRect(0, 0, pCanvas.width, pCanvas.height);

  // Draw Paddle
  pCtx.fillStyle = '#00d2ff';
  pCtx.fillRect(paddle.x, pCanvas.height - paddle.height - 10, paddle.width, paddle.height);

  // Draw Ball
  pCtx.fillStyle = '#ff00ff';
  pCtx.beginPath();
  pCtx.arc(ball.x, ball.y, ball.radius, 0, Math.PI * 2);
  pCtx.fill();

  // Physics Logic
  ball.x += ball.vx;
  ball.y += ball.vy;

  // Wall Collision
  if (ball.x < ball.radius || ball.x > pCanvas.width - ball.radius) ball.vx *= -1;
  if (ball.y < ball.radius) ball.vy *= -1;

  // Paddle Collision
  const paddleY = pCanvas.height - paddle.height - 10;
  if (ball.y + ball.radius > paddleY && ball.x > paddle.x && ball.x < paddle.x + paddle.width) {
    ball.vy *= -1.1; // Speed up
    ball.vx *= 1.1;
    score++;
    pScore.textContent = score;
    pVelocity.textContent = Math.abs(Math.round(ball.vy));
  }

  // Game Over
  if (ball.y > pCanvas.height) {
    score = 0;
    pScore.textContent = score;
    ball.x = pCanvas.width / 2;
    ball.y = pCanvas.height / 3;
    ball.vx = 5;
    ball.vy = 5;
    updateSentinelLog("PHYSICS_REBOOT: Collision engine reset.");
  }

  requestAnimationFrame(runPhysics);
}

// 4. Gen AI Chat Bot (Agent Console)
const consoleOutput = document.getElementById('console-output');
const consoleInput = document.getElementById('web-agent-input');
const sentinelLog = document.getElementById('sentinel-log');
const sentinelStatus = document.getElementById('sentinel-status');
const clearanceEl = document.getElementById('user-clearance');

function updateSentinelLog(msg) {
  const time = new Date().toLocaleTimeString([], { hour12: false, hour: '2-digit', minute: '2-digit', second: '2-digit' });
  sentinelLog.textContent += `\n[${time}] > ${msg}`;
  sentinelLog.scrollTop = sentinelLog.scrollHeight;
}

function appendToConsole(text, type = 'holographic') {
  const p = document.createElement('p');
  p.className = type;
  p.textContent = text;
  consoleOutput.appendChild(p);
  consoleOutput.scrollTop = consoleOutput.scrollHeight;
}

const API_BASE = "http://localhost:8000";

// Handle Auth Success from URL
const urlParams = new URLSearchParams(window.location.search);
if (urlParams.get('auth') === 'success') {
  clearanceEl.textContent = 'OSS_AGENT_V1';
  document.body.classList.add('auth-active');
  appendToConsole("🔓 [SECURITY]: GOOGLE AUTH VERIFIED. CLEARANCE ESCALATED.", 'verified-text');
  updateSentinelLog("AUTH_BRIDGE: Agent identity confirmed.");
}

consoleInput.addEventListener('keypress', async (e) => {
  if (e.key === 'Enter') {
    const input = consoleInput.value.trim().toLowerCase();
    if (!input) return;

    appendToConsole(`🕵️ AGENT > ${input}`, 'user-input');
    consoleInput.value = '';

    // Spy Kids / OSS Agent Logic
    if (input.includes('hello') || input.includes('hi')) {
      appendToConsole("🤖 [OSS DIRECTOR]: Welcome, recruit. Our gadgets are prepped and the Danger Room is hot. Ready for a mission?");
    } else if (input.includes('spy kids') || input.includes('oss')) {
      appendToConsole("🤖 [OSS DIRECTOR]: Correct. We are a cinematic strike team. No parents, no rules, just gadgets.");
    } else if (input.includes('gadgets')) {
      appendToConsole("🤖 [OSS DIRECTOR]: Check the Gadget Bay above. We've got Flight Kicks and Sentinel Visors ready for deployment.");
    } else if (input.includes('status') || input.includes('health')) {
      appendToConsole("🤖 [OSS DIRECTOR]: All systems nominal. The Obsidian Bridge is stable. We're waiting for your lead.");
    } else if (input.includes('floop')) {
      appendToConsole("🤖 [OSS DIRECTOR]: Floop is a madman. Help us save us.");
    } else if (input.includes('render') || input.includes('create') || input.includes('strike')) {
      appendToConsole("🤖 [OSS DIRECTOR]: Deploying mission assets. Engaging Antigravity drive...");
      triggerRender(input);
    } else {
      appendToConsole("🤖 [OSS DIRECTOR]: Signal received. Analyzing via Sentinel Logic v2.0...");
      triggerRender(input);
    }
  }
});

// Google Auth Trigger
const authBtn = document.getElementById('auth-google');
if (authBtn) {
  authBtn.addEventListener('click', async () => {
    try {
      const response = await fetch(`${API_BASE}/auth/google`);
      const data = await response.json();
      appendToConsole("🚀 [LINK]: Establishing secure Google tunnel...");
      setTimeout(() => {
        window.location.href = data.auth_url;
      }, 1000);
    } catch (err) {
      updateSentinelLog("AUTH_ERROR: Google Bridge offline.");
      appendToConsole("⚠️ [OSS]: Failed to initiate Google Auth sequence.");
    }
  });
}

async function triggerRender(input) {
  sentinelStatus.textContent = 'ANALYZING...';
  sentinelStatus.style.color = '#00d2ff';
  updateSentinelLog(`Engine Call: vision_prompt="${input}"`);

  try {
    const response = await fetch(`${API_BASE}/render?prompt=${encodeURIComponent(input)}`, {
      method: 'POST'
    });
    const result = await response.json();

    // Logic Gates Interaction (Visual Feedback)
    setTimeout(() => {
      document.getElementById('gate-semantic').classList.add('verified');
      updateSentinelLog(`Semantic matches found: [${result.analysis.archetype.toUpperCase()}]`);

      setTimeout(() => {
        document.getElementById('gate-hallucination').classList.add('verified');
        updateSentinelLog(`Sentinel Intercept: CLEAN`);

        setTimeout(() => {
          document.getElementById('gate-fallback').classList.add('verified');
          updateSentinelLog(`Render Priority: ${result.validation.status}`);

          sentinelStatus.textContent = 'VALIDATED';
          sentinelStatus.style.color = '#00ff8c';
          appendToConsole(`⚡ [ACTION]: Orchestrating "${result.analysis.archetype}" render pipeline.`);
        }, 800);
      }, 800);
    }, 800);

  } catch (err) {
    updateSentinelLog(`CRITICAL: Bridge connection severed.`);
    sentinelStatus.textContent = 'OFFLINE';
    sentinelStatus.style.color = '#ff3c3c';
    appendToConsole("⚠️ [SYSTEM]: Could not establish link to Obsidian Bridge. Ensure launch.py is running.", 'alert-text');
  }
}

// 5. Manifesto Decryption
const loreContent = document.getElementById('lore-content');
const decryptBtn = document.getElementById('decrypt-lore');

const MANIFESTO = `[ THE MOTIONFRAME MANIFESTO ]
The "Cinematic Strike" was a whisper. Born from a simple obsession: what if code didn't just execute, but performed? 

MotionFrame v3.3 is the Masterpiece. 
1. THE BRAIN: Dual-Layer Intelligence.
2. THE MUSCLE: Antigravity Rendering.
3. THE SHIELD: Sentinel Logic v2.0.

We aren't just building a project. We are building a legacy. A cinematic strike team in a repository, ready to put a dent in the universe.`;

decryptBtn.addEventListener('click', () => {
  decryptBtn.disabled = true;
  decryptBtn.textContent = 'AUTHORIZING...';
  let i = 0;
  loreContent.textContent = '';
  const interval = setInterval(() => {
    loreContent.textContent += MANIFESTO[i];
    i++;
    if (i >= MANIFESTO.length) {
      clearInterval(interval);
      decryptBtn.textContent = 'DECRYPTED';
    }
  }, 20);
});

// 6. Cinematic Mode Toggle
const cinematicBtn = document.getElementById('toggle-cinematic');
let isCinematic = false;

cinematicBtn.addEventListener('click', () => {
  isCinematic = !isCinematic;
  document.body.classList.toggle('cinematic-active', isCinematic);

  if (isCinematic) {
    cinematicBtn.textContent = '❌';
    updateSentinelLog("IMMERSE_MODE: UI layers hidden.");
  } else {
    cinematicBtn.textContent = '👁️';
    updateSentinelLog("GUI_RESTORED: All layers online.");
  }
});

