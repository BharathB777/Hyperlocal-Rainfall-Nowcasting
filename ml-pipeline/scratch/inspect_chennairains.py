import urllib.request
import re

req = urllib.request.Request('https://plots.chennairains.com/toggle_rainfall_map.html', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

print("Total HTML length:", len(html))

# Find sidebar structure
sb_idx = html.find('id="sidebar"')
if sb_idx != -1:
    print("=== SIDEBAR SECTION ===")
    print(html[sb_idx-15:sb_idx+4000])

# Look for variable names or model structures
script_matches = re.findall(r'<script\b[^>]*>(.*?)</script>', html, re.DOTALL)
print("\nNumber of scripts:", len(script_matches))
for i, s in enumerate(script_matches):
    print(f"\n--- Script {i} (len: {len(s)}) ---")
    lines = [line.strip() for line in s.split('\n') if line.strip() and not line.strip().startswith('//')][:25]
    print("\n".join(lines[:20]))
