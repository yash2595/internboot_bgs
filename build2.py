#!/usr/bin/env python3
"""
Build Script for Bridge Group Solutions
Copies source HTML files, assets, and cpresources to build-output/
without modifying or forcing Tailwind/Alpine boilerplate into standalone pages.
"""
import os
import shutil

SRC_ROOT = os.path.abspath(os.path.dirname(__file__))
DEST_ROOT = os.path.join(SRC_ROOT, 'build-output')

# Re-create build-output directory
if os.path.exists(DEST_ROOT):
    try:
        shutil.rmtree(DEST_ROOT, ignore_errors=True)
    except Exception:
        pass
os.makedirs(DEST_ROOT, exist_ok=True)

# Directories to copy directly
COPY_DIRS = ['assets', 'cpresources', 'services', 'legal', 'docs']

for dir_name in COPY_DIRS:
    src_dir = os.path.join(SRC_ROOT, dir_name)
    dest_dir = os.path.join(DEST_ROOT, dir_name)
    if os.path.exists(src_dir):
        shutil.copytree(src_dir, dest_dir, dirs_exist_ok=True)
        print(f"Copied directory: {dir_name}/")

# Copy root HTML and XML files
for file_name in os.listdir(SRC_ROOT):
    if file_name.lower().endswith(('.html', '.xml', '.json', '.txt', '.png', '.ico', '.svg', '.webmanifest')):
        src_file = os.path.join(SRC_ROOT, file_name)
        if os.path.isfile(src_file):
            shutil.copy2(src_file, os.path.join(DEST_ROOT, file_name))
            print(f"Copied root file: {file_name}")

print("\nBuild completed successfully: build-output/ generated cleanly.")
