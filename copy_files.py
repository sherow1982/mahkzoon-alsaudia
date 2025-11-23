#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import shutil
from pathlib import Path

# نسخ index.html من store إلى الجذر
shutil.copy('store/index.html', 'index.html')
shutil.copytree('store/products', 'products', dirs_exist_ok=True)
shutil.copytree('store/data', 'data', dirs_exist_ok=True)
shutil.copytree('store/css', 'css', dirs_exist_ok=True)
shutil.copytree('store/js', 'js', dirs_exist_ok=True)

print("✅ تم نسخ جميع الملفات إلى الجذر!")
