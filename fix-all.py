#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
سكريبت تصحيح شامل لموقع مخزون السعودية
يصحح الدومين ورقم الواتساب في جميع الملفات
"""

import os
import glob
import re

# الإعدادات
REPO_PATH = r"C:\Users\shero\OneDrive\Desktop\mahkzoon-alsaudia"
OLD_DOMAIN = "mahkzoon-alsaudia.com"
NEW_DOMAIN = "mahkzoon-alsaudia.arabsad.com"
WHATSAPP_NUMBER = "201110760081"

def fix_file(file_path):
    """تصحيح ملف واحد"""
    try:
        # قراءة الملف
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # تصحيح الدومين
        content = content.replace(OLD_DOMAIN, NEW_DOMAIN)
        
        # تصحيح رقم الواتساب
        content = re.sub(r'wa\.me/\d+', f'wa.me/{WHATSAPP_NUMBER}', content)
        
        # حفظ إذا تم التعديل
        if content != original:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"خطأ في معالجة {file_path}: {e}")
        return False

def main():
    print("=" * 60)
    print("  سكريبت التصحيح الشامل لمخزون السعودية")
    print("=" * 60)
    print()
    
    # التحقق من وجود المجلد
    if not os.path.exists(REPO_PATH):
        print(f"خطأ: المجلد غير موجود!")
        print(f"المسار: {REPO_PATH}")
        input("\nاضغط Enter للخروج...")
        return
    
    print(f"تم العثور على المجلد")
    print(f"المسار: {REPO_PATH}")
    print()
    
    # البحث عن ملفات HTML
    products_path = os.path.join(REPO_PATH, "products", "*.html")
    html_files = glob.glob(products_path)
    
    if not html_files:
        print("لم يتم العثور على ملفات HTML في مجلد products")
        input("\nاضغط Enter للخروج...")
        return
    
    print(f"تم العثور على {len(html_files)} ملف HTML")
    print()
    print("بدء التصحيح...")
    print("-" * 60)
    
    # معالجة الملفات
    total = 0
    fixed = 0
    
    for file_path in html_files:
        total += 1
        filename = os.path.basename(file_path)
        
        if fix_file(file_path):
            print(f"[{total}] تم تصحيح: {filename}")
            fixed += 1
        else:
            print(f"[{total}] تخطي: {filename}")
    
    # الملخص
    print()
    print("=" * 60)
    print("ملخص التصحيح:")
    print("-" * 60)
    print(f"   إجمالي الملفات: {total}")
    print(f"   تم التصحيح: {fixed}")
    print(f"   تم التخطي: {total - fixed}")
    print("=" * 60)
    print()
    
    if fixed > 0:
        print("تم التصحيح بنجاح!")
        print()
        print("التفاصيل:")
        print(f"   • الدومين الجديد: {NEW_DOMAIN}")
        print(f"   • رقم الواتساب: {WHATSAPP_NUMBER}")
        print(f"   • عدد الملفات المصححة: {fixed}")
        print()
        print("الخطوة التالية: رفع التغييرات إلى GitHub")
        print("   git add .")
        print('   git commit -m "تصحيح: تحديث الدومين ورقم الواتساب"')
        print("   git push")
    else:
        print("جميع الملفات محدثة بالفعل")
    
    print()
    input("اضغط Enter للخروج...")

if __name__ == "__main__":
    main()
