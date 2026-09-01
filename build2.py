#!/usr/bin/env python3
"""
Build Script for Bridge Group Solutions
Copies source HTML files, assets, and cpresources to build-output/.
Also creates extensionless directory route aliases for root HTML pages
so that Render's static CDN resolves e.g. /about → /about/index.html
without needing server-side rewrite rules.
"""
import os
import shutil

SRC_ROOT = os.path.abspath(os.path.dirname(__file__))
DEST_ROOT = os.path.join(SRC_ROOT, 'build-output')

# Root HTML pages that need extensionless directory aliases
# (index.html is excluded — it's the root, already handled)
ROOT_PAGES = ['about', 'contact', 'gallery', 'portfolio', 'why-bgs']

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

# Create extensionless directory aliases for root HTML pages.
# Render static CDN resolves /about → /about/index.html, but not /about.html.
# This ensures both /about.html (linked internally) and /about (typed in browser)
# resolve correctly without server-side rewrites failing.
for slug in ROOT_PAGES:
    src_file = os.path.join(SRC_ROOT, f"{slug}.html")
    if os.path.isfile(src_file):
        alias_dir = os.path.join(DEST_ROOT, slug)
        os.makedirs(alias_dir, exist_ok=True)
        shutil.copy2(src_file, os.path.join(alias_dir, 'index.html'))
        print(f"Created route alias:  /{slug}/index.html")

print("\nBuild completed successfully: build-output/ generated cleanly.")
