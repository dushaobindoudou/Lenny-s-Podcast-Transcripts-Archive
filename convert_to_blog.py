#!/usr/bin/env python3
"""
Convert Lenny's Podcast transcripts to bilingual blog format (Chinese + English)
"""

import os
import re
from pathlib import Path
from datetime import datetime

def clean_text(text):
    """Clean and normalize text"""
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
                speakers.append({
                    'speaker': current_speaker,
                    'content': clean_text('\n'.join(current_content))
                })
            
            current_speaker = match.group(1).strip()
            current_content = [match.group(2).strip()]
        else:
            if current_speaker:
                current_content.append(line)
    
    # Don't forget the last speaker
    if current_speaker:
        speakers.append({
            'speaker': current_speaker,
            'content': clean_text('\n'.join(current_content))
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

def create_blog_content(filename, speakers):
    """Create bilingual blog content"""
    guest_name = extract_guest_name(filename)
    
    # Extract main content (filter out sponsors and intros)
    main_content = []
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
    ]
    
    for speaker_data in speakers:
        # Skip sponsor content
        is_sponsor = any(re.search(pattern, speaker_data['content'], re.IGNORECASE) 
                        for pattern in sponsor_patterns)
        
        # Skip if content is mostly sponsorship
        if is_sponsor and len(speaker_data['content']) < 200:
            continue
            
        # Skip Lenny's standard intros
        if 'Today my guest is' in speaker_data['content'] and 'Lenny' in speaker_data['speaker']:
            continue
            
        main_content.append(speaker_data)
    
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
    sections.append(f"**{guest_name}** - Featured guest on Lenny's Podcast")
    sections.append("")
    sections.append(f"**{guest_name}** - Lenny's播客特邀嘉宾")
    sections.append("")
    sections.append("---")
    sections.append("")
    
    # Key Insights section
    sections.append("## Key Insights | 核心洞见")
    sections.append("")
    
    # Extract and organize content into insights
    insights = []
    for i, speaker_data in enumerate(main_content):
        if len(speaker_data['content']) > 100:  # Skip very short messages
            # Create a concise summary
            content_preview = speaker_data['content'][:300]
            if len(speaker_data['content']) > 300:
                content_preview += "..."
            
            speaker_label = speaker_data['speaker']
            if 'Lenny' in speaker_label:
                speaker_label = 'Lenny Rachitsky (Host)'
            else:
                speaker_label = guest_name
            
            insights.append(f"### {speaker_label}")
            insights.append("")
            insights.append(content_preview)
            insights.append("")
    
    sections.extend(insights)
    
    # Full Transcript section
    sections.append("---")
    sections.append("")
    sections.append("## Full Transcript | 完整对话记录")
    sections.append("")
    
    for speaker_data in main_content:
        sections.append(f"**{speaker_data['speaker']}:**")
        sections.append("")
        sections.append(speaker_data['content'])
        sections.append("")
    
    return '\n'.join(sections)

def process_all_transcripts():
    """Process all transcript files"""
    txt_folder = Path('txt')
    blog_folder = Path('blog')
    blog_folder.mkdir(exist_ok=True)
    
    txt_files = sorted(txt_folder.glob('*.txt'))
    
    processed = []
    
    for txt_file in txt_files:
        try:
            # Read the transcript
            with open(txt_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse speakers and content
            lines = content.split('\n')
            speakers = extract_speaker_content(lines)
            
            if not speakers:
                print(f"Warning: No content found in {txt_file}")
                continue
            
            # Generate blog content
            blog_content = create_blog_content(txt_file.name, speakers)
            
            # Save blog post
            blog_filename = txt_file.stem + '.md'
            blog_path = blog_folder / blog_filename
            
            with open(blog_path, 'w', encoding='utf-8') as f:
                f.write(blog_content)
            
            guest_name = extract_guest_name(txt_file.name)
            processed.append((guest_name, blog_filename))
            print(f"Processed: {txt_file.name} -> {blog_filename}")
            
        except Exception as e:
            print(f"Error processing {txt_file}: {e}")
    
    return processed

if __name__ == '__main__':
    print("Starting transcript conversion...")
    processed = process_all_transcripts()
    print(f"\nProcessed {len(processed)} transcripts")
