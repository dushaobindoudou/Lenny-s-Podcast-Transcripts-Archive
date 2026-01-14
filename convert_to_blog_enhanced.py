#!/usr/bin/env python3
"""
Enhanced blog converter with better content extraction and Chinese translation support
"""

import os
import re
from pathlib import Path
from datetime import datetime

def clean_text(text):
    """Clean and normalize text"""
    # Remove content in brackets like [inaudible 00:09:59]
    text = re.sub(r'\[inaudible \d{2}:\d{2}\]', '', text)
    # Remove timestamps in parentheses like (00:00:00)
    text = re.sub(r'\(\d{2}:\d{2}:\d{2}\)', '', text)
    # Remove extra whitespace
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r' +', ' ', text)
    # Strip leading/trailing whitespace
    text = text.strip()
    return text

def extract_speaker_content(lines):
    """Extract speaker and content from transcript lines"""
    speakers = []
    current_speaker = None
    current_content = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Match speaker pattern: "Name (timestamp):" or just "Name:"
        match = re.match(r'^([^():]+?)\s*(?:\([^)]+\))?:\s*(.+)$', line)
        if match:
            # Save previous speaker content
            if current_speaker:
                content = clean_text('\n'.join(current_content))
                if content:
                    speakers.append({
                        'speaker': current_speaker,
                        'content': content
                    })
            
            current_speaker = match.group(1).strip()
            current_content = [match.group(2).strip()]
        else:
            if current_speaker:
                current_content.append(line)
    
    # Don't forget the last speaker
    if current_speaker:
        content = clean_text('\n'.join(current_content))
        if content:
            speakers.append({
                'speaker': current_speaker,
                'content': content
            })
    
    return speakers

def extract_guest_name(filename):
    """Extract guest name from filename"""
    # Remove .txt extension and clean up
    name = filename.replace('.txt', '')
    # Remove version numbers like "2.0", "3.0"
    name = re.sub(r'\s*\d+\.\d+\s*$', '', name)
    name = re.sub(r'\s*_\s*$', '', name)
    return name.strip()

def create_blog_content(filename, speakers, guest_name):
    """Create bilingual blog content with better formatting"""
    
    # Generate blog sections
    sections = []
    
    # Title section
    title = f"{guest_name} - Lenny's Podcast Insights"
    title_zh = f"{guest_name} - Lenny's播客洞见"
    
    sections.append(f"# {title}")
    sections.append(f"## {title_zh}")
    sections.append("")
    sections.append("---")
    sections.append("")
    
    # About the guest section
    sections.append("## About the Guest | 关于嘉宾")
    sections.append("")
    sections.append(f"**{guest_name}** joined Lenny for an in-depth conversation on product management, leadership, and building successful products.")
    sections.append("")
    sections.append(f"**{guest_name}** 与Lenny进行了深入对话，讨论产品管理、领导力和打造成功产品的经验。")
    sections.append("")
    sections.append("---")
    sections.append("")
    
    # Key Insights section
    sections.append("## Key Takeaways | 核心要点")
    sections.append("")
    
    # Extract meaningful insights
    meaningful_content = []
    sponsor_patterns = [
        r'This episode is brought to you by',
        r'Sidebar',
        r'Jira Product Discovery',
        r'DX',
        r'Basecamp',
        r'Atlassian',
        r'getdx\.com',
        r'basecamp\.com',
        r'atlassian\.com',
        r'sidebar\.com',
        r'Welcome to the podcast',
        r"Thank you so much for being here",
        r"Today my guest is",
        r"If you enjoy this podcast"
    ]
    
    for speaker_data in speakers:
        content = speaker_data['content']
        
        # Skip sponsor content
        is_sponsor = any(re.search(pattern, content, re.IGNORECASE) 
                        for pattern in sponsor_patterns)
        
        # Skip short messages and sponsors
        if len(content) < 50 or is_sponsor:
            continue
            
        meaningful_content.append(speaker_data)
    
    # Create insight points from the content
    for i, speaker_data in enumerate(meaningful_content[:15]):  # Limit to top 15 insights
        speaker = speaker_data['speaker']
        content = speaker_data['content']
        
        # Truncate if too long
        if len(content) > 500:
            content = content[:500] + "..."
        
        sections.append(f"### {speaker}")
        sections.append("")
        sections.append(content)
        sections.append("")
    
    sections.append("---")
    sections.append("")
    
    # Full Transcript section
    sections.append("## Full Conversation | 完整对话")
    sections.append("")
    sections.append("*Below is the complete transcript of the conversation.*")
    sections.append("")
    sections.append("*以下是完整对话记录。*")
    sections.append("")
    
    for speaker_data in speakers:
        sections.append(f"**{speaker_data['speaker']}**:")
        sections.append("")
        sections.append(speaker_data['content'])
        sections.append("")
    
    return '\n'.join(sections)

def create_zh_version(blog_content, guest_name):
    """Create Chinese version of the blog post"""
    # Simple translation mapping for common phrases
    translations = {
        "About the Guest | 关于嘉宾": "## 关于嘉宾 | About the Guest",
        "Key Takeaways | 核心要点": "## 核心要点 | Key Takeaways",
        "Full Conversation | 完整对话": "## 完整对话 | Full Conversation",
        "Below is the complete transcript of the conversation.": "以下是完整对话记录。",
        "*Below is the complete transcript of the conversation.*": "*以下是完整对话记录。*",
        "*以下是完整对话记录。*": "*以下是完整对话记录。*",
        "joined Lenny for an in-depth conversation on product management, leadership, and building successful products.": "与Lenny进行了关于产品管理、领导力和打造成功产品的深入对话。",
        "Featured guest on Lenny's Podcast": "Lenny播客特邀嘉宾"
    }
    
    # Apply translations
    zh_content = blog_content
    for en, zh in translations.items():
        zh_content = zh_content.replace(en, zh)
    
    return zh_content

def process_all_transcripts():
    """Process all transcript files and create bilingual blog posts"""
    txt_folder = Path('txt')
    blog_folder = Path('blog')
    blog_folder.mkdir(exist_ok=True)
    
    txt_files = sorted(txt_folder.glob('*.txt'))
    
    processed = []
    failed = []
    
    for txt_file in txt_files:
        try:
            # Read the transcript
            with open(txt_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse speakers and content
            lines = content.split('\n')
            speakers = extract_speaker_content(lines)
            
            if not speakers:
                failed.append(txt_file.name)
                continue
            
            # Get guest name
            guest_name = extract_guest_name(txt_file.name)
            
            # Generate blog content
            blog_content = create_blog_content(txt_file.name, speakers, guest_name)
            
            # Save English version
            blog_filename = txt_file.stem + '.md'
            blog_path = blog_folder / blog_filename
            
            with open(blog_path, 'w', encoding='utf-8') as f:
                f.write(blog_content)
            
            # Create Chinese version
            zh_content = create_zh_version(blog_content, guest_name)
            zh_filename = txt_file.stem + '.zh.md'
            zh_path = blog_folder / zh_filename
            
            with open(zh_path, 'w', encoding='utf-8') as f:
                f.write(zh_content)
            
            processed.append((guest_name, blog_filename, zh_filename))
            print(f"✓ {txt_file.name}")
            
        except Exception as e:
            failed.append((txt_file.name, str(e)))
            print(f"✗ {txt_file.name}: {e}")
    
    return processed, failed

if __name__ == '__main__':
    print("Creating bilingual blog posts...")
    print("=" * 50)
    processed, failed = process_all_transcripts()
    print("=" * 50)
    print(f"\n✓ Successfully processed: {len(processed)} files")
    print(f"✗ Failed: {len(failed)} files")
