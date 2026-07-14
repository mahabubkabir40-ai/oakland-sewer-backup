import os
import glob
import re

def audit_and_fix():
    html_files = glob.glob("*.html")
    exclude = ['404.html', 'thank-you.html']
    
    # 5 primary services
    services_map = {
        'basement-sanitization': 'Basement Sanitization',
        'flooded-basement': 'Flooded Basement Cleanup',
        'sewage-extraction': 'Sewage Extraction',
        'sewer-cleanup': 'Sewer Backup Cleanup',
        'sump-pump-repair': 'Sump Pump Repair'
    }
    
    # Suburbs list
    suburbs = ['berkley', 'birmingham', 'clawson', 'royal-oak', 'troy']
    
    for f in html_files:
        if f in exclude:
            continue
            
        print(f"\nProcessing: {f}")
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        modified = False
        
        # 1. Determine Suburb and Service
        basename = os.path.splitext(f)[0]
        suburb_found = None
        service_found = None
        
        for sub in suburbs:
            if basename.startswith(sub):
                suburb_found = sub.replace('-', ' ').title()
                service_key = basename[len(sub)+1:]
                if service_key in services_map:
                    service_found = services_map[service_key]
                break
                
        # 2. Audit/Fix Title Tag
        title_match = re.search(r'<title>(.*?)</title>', content)
        if title_match:
            current_title = title_match.group(1)
            if basename == 'index':
                new_title = "Oakland Sewer Pros | 24/7 Sewer Backup Cleanup & Sewage Extraction"
            elif basename == 'terms':
                new_title = "Terms of Service | Oakland Sewer Pros"
            elif basename == 'contact':
                new_title = "Contact Us | Oakland Sewer Pros"
            elif suburb_found and service_found:
                new_title = f"{service_found} {suburb_found} MI | Oakland Sewer Pros"
            else:
                new_title = current_title
                
            if current_title != new_title:
                print(f"  -> Updating Title: '{current_title}' \n                 to: '{new_title}'")
                content = content.replace(f'<title>{current_title}</title>', f'<title>{new_title}</title>')
                modified = True
                
        # 3. Audit/Fix Canonical Tag
        if '<link rel="canonical"' not in content:
            print("  -> Adding Missing Canonical Tag")
            viewport_pattern = r'(<meta name="viewport" content="width=device-width, initial-scale=1.0">)'
            canonical_href = "https://oaklandsewerpros.com/" if basename == 'index' else f"https://oaklandsewerpros.com/{basename}"
            canonical_tag = f'\n    <link rel="canonical" href="{canonical_href}">'
            
            content = re.sub(viewport_pattern, r'\1' + canonical_tag, content)
            modified = True
            
        # 4. Audit/Fix Meta Description (Include Phone and keep under 160 chars)
        desc_match = re.search(r'<meta name="description" content="(.*?)">', content)
        if desc_match:
            current_desc = desc_match.group(1)
            phone = "(248) 825-8312"
            
            if phone not in current_desc:
                base_desc = current_desc.rstrip('.')
                # Truncate original description slightly if needed to keep under 160 chars total
                if len(base_desc) > 115:
                    base_desc = base_desc[:115] + "..."
                new_desc = f"{base_desc}. Call 24/7: {phone}."
                print(f"  -> Appending Phone to Meta Description: \n     Old: '{current_desc}'\n     New: '{new_desc}'")
                content = content.replace(f'content="{current_desc}"', f'content="{new_desc}"')
                modified = True

        # 5. Audit/Fix Domain Typo (oaklandseweremergency.com)
        if "oaklandseweremergency.com" in content:
            print("  -> Fixing domain typo (oaklandseweremergency.com -> oaklandsewerpros.com)")
            content = content.replace("oaklandseweremergency.com", "oaklandsewerpros.com")
            modified = True

        # Save changes if any modifications were made
        if modified:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"  -> SUCCESS: Saved modifications to {f}")
            
if __name__ == "__main__":
    audit_and_fix()
