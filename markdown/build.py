#!/usr/bin/env python3

import fileinput
import glob
import os
from re import T
import shutil
import subprocess
from tqdm import tqdm

def replace(file_name, text_to_search, replacement_text):
    with fileinput.FileInput(file_name, inplace=True) as f:
        for line in f:
            print(line.replace(text_to_search, replacement_text), end='')


def split(path_to_file):
    file_name = os.path.basename(path_to_file)
    file_name_without_extension = os.path.splitext(file_name)[0]
    return file_name, file_name_without_extension


if __name__ == "__main__":
    output_dir = os.path.join("build")
    shutil.rmtree(output_dir, ignore_errors=True)
    os.mkdir(output_dir)

    files = glob.glob("./src/**/*.md", recursive=True)

    for file in tqdm(files):
        cwd = os.path.join(os.getcwd(), "src")
        file_name, file_name_without_extension = split(file)
        
        if file.endswith(".md"):
            # Create PNG files because pandoc doesn't support SVG
            output_png = os.path.join(output_dir, f"{file_name_without_extension}.png")
            subprocess.check_output(f"docker run -it --rm -v {cwd}/../:/data minlag/mermaid-cli -i /data/src/{file_name} -o /data/{output_png} -t dark -b transparent", shell=True)

            # Re-write the markdown file to replace mermaid code blocks with SVG image
            # See https://github.com/mermaid-js/mermaid-cli/issues/248
            output_md = os.path.join(output_dir, f"{file_name_without_extension}.md")
            subprocess.check_output(f"docker run -it --rm -v {cwd}/../:/data minlag/mermaid-cli -i /data/src/{file_name} -o /data/{output_md} -t dark -b transparent", shell=True)

            # Re-write markdown file to replace *.svg with *.png
            for svg in glob.glob(f"{output_dir}/**/*.svg", recursive=True):
                svg_file_name, svg_file_name_without_extension = split(svg)
                replace(output_md, svg_file_name, f"{svg_file_name_without_extension}.png")
            
            # Convert markdown to PDF using Eisvogel template
            subprocess.check_output(f"docker run --rm -v {cwd}/../build:/data rstropek/pandoc-latex -f markdown --template https://raw.githubusercontent.com/Wandmalfarbe/pandoc-latex-template/v2.0.0/eisvogel.tex -t latex -o /data/{file_name_without_extension}.pdf /data/{file_name_without_extension}.md", shell=True)

            # Cleanup temporary files
            for ext in ["*.md", "*.png", "*.svg"]:
                for f in glob.glob(f"{output_dir}/**/{ext}", recursive=True):
                    os.remove(f)