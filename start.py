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
    # Detect cloud vs local environment and resolve PORT
    is_cloud = "PORT" in os.environ
    port_str = os.environ.get("PORT", "8000")
    try:
        port_int = int(port_str)
    except ValueError:
        port_int = 8000
        port_str = "8000"

    print("\n==========================================")
    print("  Build Success! Starting Server...        ")
    if is_cloud:
        print(f"  Cloud Mode Detected (PORT={port_str})  ")
        print(f"  Server listening on port {port_str}   ")
    else:
        print(f"  Local Mode (http://localhost:{port_str}) ")
    print("==========================================")
    
    # 2. Auto-open browser only in local mode with try/except safety net
    if not is_cloud:
        try:
            webbrowser.open(f"http://localhost:{port_str}")
        except Exception:
            pass
    
    # 3. Start Python HTTP server on bound port
    os.system(f"{sys.executable} -m http.server {port_str} --directory build-output")
else:
    print("\n[ERROR] Build failed. Please check build errors.")
