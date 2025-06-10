import subprocess
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()

file_path = os.path.abspath(args.filename)
jupyter_root_dir = os.getcwd()

relative_path = os.path.relpath(file_path, jupyter_root_dir)


result = subprocess.run(["jupyter", "lab", "list"], capture_output=True, text=True)

output = result.stdout.split()

#for now we are only dealing with single server so the token will be at output[3] always

base_url = output[3]
host_and_port, token = base_url.split('?')
final_url = f"{host_and_port}lab/tree/{relative_path}?{token}"
subprocess.run(["google-chrome", final_url])
