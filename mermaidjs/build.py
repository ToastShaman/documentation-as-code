#!/usr/bin/env python3

import glob
import os
import shutil
import subprocess
from tqdm import tqdm

if __name__ == "__main__":
    output_dir = os.path.join("build")
    shutil.rmtree(output_dir, ignore_errors=True)
    os.mkdir(output_dir)

    files = glob.glob("./src/**/*.md", recursive=True)

    for file in tqdm(files):
        cwd = os.path.join(os.getcwd(), "src")
        file_name = os.path.basename(file)
        file_name_without_extension = os.path.splitext(file_name)[0]
        
        for ext in ["png", "svg"]:
            output = os.path.join(output_dir, f"{file_name_without_extension}.{ext}")
            subprocess.check_output(f"docker run -it -v {cwd}/../:/data minlag/mermaid-cli -i /data/src/{file_name} -o /data/{output}", shell=True)
            subprocess.check_output(f"docker run -it -v {cwd}/../:/data minlag/mermaid-cli -i /data/src/{file_name} -o /data/{output}", shell=True)
