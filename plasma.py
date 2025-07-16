import random
from datetime import datetime

code_snippets = [
    "echo 'Charging plasma...'",
    "echo 'Plasma core online 🧪'",
    "echo $((RANDOM % 100)) > /dev/null",
    "for i in {1..5}; do echo '💥'; done",
    "echo 'System check: PASS ✅'",
    f"echo 'Timestamp: {datetime.now()}'"
]

# 🎲 Choose how many random code drops today (1–5)
num_drops_today = random.randint(1, 5)

with open("plasma_codes.sh", "a") as f:
    for i in range(num_drops_today):
        f.write("\n# --- Plasma Code Drop ---\n")
        # 🌀 Pick 1–5 random lines per drop
        num_lines = random.randint(1, 5)
        selected = random.sample(code_snippets, num_lines)
        for line in selected:
            f.write(f"{line}\n")

print(f"🔥 Dropped {num_drops_today} code blocks into plasma_codes.sh")
