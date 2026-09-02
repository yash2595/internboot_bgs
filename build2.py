#!/usr/bin/env python3
"""
Build Script for Bridge Group Solutions
Copies source HTML files, assets, and cpresources to build-output/.
Also creates extensionless directory route aliases for root and subfolder HTML pages
and performs automated deterministic integrity verification assertions.
"""
import os
import shutil
import sys

SRC_ROOT = os.path.abspath(os.path.dirname(__file__))
DEST_ROOT = os.path.join(SRC_ROOT, 'build-output')

# Root HTML pages that need extensionless directory aliases
ROOT_PAGES = ['about', 'contact', 'gallery', 'portfolio', 'why-bgs']

# Expected critical files required for deployment integrity verification
CRITICAL_FILES = [
    'index.html',
    'about.html',
    'contact.html',
    'gallery.html',
    'portfolio.html',
    'why-bgs.html',
    os.path.join('services', 'app.html'),
    os.path.join('services', 'web.html'),
    os.path.join('services', 'crm.html'),
    os.path.join('services', 'data.html'),
    os.path.join('services', 'project.html'),
    os.path.join('services', 'erp.html'),
    os.path.join('legal', 'disclaimer.html'),
    os.path.join('legal', 'privacy-policy.html'),
    os.path.join('legal', 'terms-and-conditions.html'),
    os.path.join('legal', 'cookie-policy.html'),
    os.path.join('legal', 'whistleblower-protection-statement.html'),
]

# Re-create build-output directory freshly
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

# Copy root HTML, XML, metadata, and asset files
for file_name in os.listdir(SRC_ROOT):
    if file_name.lower().endswith(('.html', '.xml', '.json', '.txt', '.png', '.ico', '.svg', '.webmanifest')):
        src_file = os.path.join(SRC_ROOT, file_name)
        if os.path.isfile(src_file):
            shutil.copy2(src_file, os.path.join(DEST_ROOT, file_name))
            print(f"Copied root file: {file_name}")

# Create extensionless directory aliases for root HTML pages
for slug in ROOT_PAGES:
    src_file = os.path.join(SRC_ROOT, f"{slug}.html")
    if os.path.isfile(src_file):
        alias_dir = os.path.join(DEST_ROOT, slug)
        os.makedirs(alias_dir, exist_ok=True)
        shutil.copy2(src_file, os.path.join(alias_dir, 'index.html'))
        print(f"Created route alias:  /{slug}/index.html")

# Create extensionless directory aliases for legal pages (e.g. /legal/whistleblower-protection-statement -> /legal/whistleblower-protection-statement/index.html)
legal_src_dir = os.path.join(SRC_ROOT, 'legal')
if os.path.exists(legal_src_dir):
    for l_file in os.listdir(legal_src_dir):
        if l_file.endswith('.html'):
            slug = l_file[:-5]
            alias_dir = os.path.join(DEST_ROOT, 'legal', slug)
            os.makedirs(alias_dir, exist_ok=True)
            shutil.copy2(os.path.join(legal_src_dir, l_file), os.path.join(alias_dir, 'index.html'))
            print(f"Created route alias:  /legal/{slug}/index.html")

# ==============================================================================
# DETERMINISTIC REGRESSION GUARD & INTEGRITY ASSERTIONS
# ==============================================================================
missing_files = []
for req_path in CRITICAL_FILES:
    full_dest = os.path.join(DEST_ROOT, req_path)
    if not os.path.isfile(full_dest) or os.path.getsize(full_dest) == 0:
        missing_files.append(req_path)

if missing_files:
    print(f"\n[CRITICAL ERROR] Build verification failed! Missing files: {missing_files}", file=sys.stderr)
    sys.exit(1)

print(f"\n[PASS] All {len(CRITICAL_FILES)} critical site pages verified in build-output with non-zero byte size.")
print("Build completed successfully: build-output/ generated cleanly.")
