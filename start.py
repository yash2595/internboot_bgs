import os
import subprocess
import webbrowser
import sys

print("==========================================")
print("  Building Bridge Group Solutions...      ")
print("==========================================")

# 1. Run build script
res = subprocess.run([sys.executable, "build2.py"])

if res.returncode == 0:
    print("\n==========================================")
    print("  Build Success! Starting Local Server... ")
    print("  URL: http://localhost:8000              ")
    print("==========================================")
    
    # 2. Open browser automatically
    webbrowser.open("http://localhost:8000")
    
    # 3. Start python HTTP server
    os.system(f"{sys.executable} -m http.server 8000 --directory build-output")
else:
    print("\n[ERROR] Build failed. Please check build errors.")
