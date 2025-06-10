import argparse
import subprocess
import os

parser = argparse.ArgumentParser()

parser.add_argument("filename")
args = parser.parse_args()

file_name_string ,file_extension = os.path.splitext(args.filename)
file_exists = os.path.exists(args.filename)

if file_extension == ".ipynb" and file_exists:
    subprocess.run([ "jupytext", "--set-formats", "ipynb,py:percent", f"{args.filename}" ])
elif file_extension == ".py" and file_exists:
    subprocess.run(["jupytext", "--to", "ipynb", f"{args.filename}"])
    subprocess.run([ "jupytext", "--set-formats", "ipynb,py:percent", f"{args.filename}" ])
else:
    subprocess.run(["touch", f"{file_name_string}.py"])
    subprocess.run([ "jupytext", "--set-formats", "ipynb,py:percent", "--to", "ipynb", f"{file_name_string}.py"])
