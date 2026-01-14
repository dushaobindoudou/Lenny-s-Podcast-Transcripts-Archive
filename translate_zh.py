import os
import re
from pathlib import Path

TRANSLATIONS = {
    "Lenny's Podcast": "Lenny的播客",
    "About the Guest": "关于嘉宾",
    "Key Takeaways": "核心要点",
    "Full Conversation": "完整对话",
    "Welcome to Lenny's Podcast": "欢迎来到Lenny的播客",
    "Thanks for listening": "感谢收听",
    "Subscribe to the show": "订阅节目",
    "Apple Podcasts": "Apple Podcasts",
    "Spotify": "Spotify",
    "Lenny Rachitsky": "Lenny Rachitsky",
    "Ada Chen Rekhi": "Ada Chen Rekhi",
}

def translate_text(text):
    for eng, chn in TRANSLATIONS.items():
        text = text.replace(eng, chn)
    return text

def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        translated_content = translate_text(content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(translated_content)
        
        return True
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    blog_dir = Path("blog")
    zh_files = list(blog_dir.glob("*.zh.md"))
    
    print(f"找到 {len(zh_files)} 个需要翻译的文件")
    
    success_count = 0
    for i, file_path in enumerate(zh_files, 1):
        if process_file(file_path):
            success_count += 1
        if i % 10 == 0:
            print(f"已处理 {i}/{len(zh_files)} 个文件")
    
    print(f"成功处理 {success_count}/{len(zh_files)} 个文件")

if __name__ == "__main__":
    main()
