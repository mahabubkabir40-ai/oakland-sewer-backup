import os
import glob
import pickle
import time
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Webmasters readonly scope covers URL inspection
SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']

def get_service():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return build('searchconsole', 'v1', credentials=creds)

def check_indexing():
    service = get_service()
    site_url = 'sc-domain:oaklandsewerpros.com'
    
    # Find all html files in root
    html_files = glob.glob("*.html")
    
    # Exclude legal/admin files that don't need active GSC indexing push
    exclude = ['404.html', 'terms.html', 'thank-you.html']
    html_files = [f for f in html_files if f not in exclude]
    
    urls = []
    for f in html_files:
        name = os.path.splitext(f)[0]
        if name == 'index':
            urls.append('https://oaklandsewerpros.com/')
        else:
            urls.append(f'https://oaklandsewerpros.com/{name}')
            
    print(f"Found {len(urls)} URLs to inspect.\n")
    
    indexed = []
    not_indexed = []
    
    for url in urls:
        print(f"Inspecting: {url}...", end='', flush=True)
        try:
            request = {
                'inspectionUrl': url,
                'siteUrl': site_url
            }
            response = service.urlInspection().index().inspect(body=request).execute()
            result = response.get('inspectionResult', {})
            status_result = result.get('indexStatusResult', {})
            verdict = status_result.get('verdict', 'UNKNOWN')
            coverage = status_result.get('coverageState', 'Unknown status')
            
            if verdict == 'PASS':
                print(" INDEXED")
                indexed.append((url, coverage))
            else:
                print(f" NOT INDEXED ({coverage})")
                not_indexed.append((url, coverage))
                
            time.sleep(0.5) # Pause to respect API rate limits
        except Exception as e:
            print(f" ERROR: {e}")
            not_indexed.append((url, f"API Error: {e}"))
            
    print("\n" + "="*60)
    print(f"INDEXING SUMMARY FOR OAKLANDSEWERPROS.COM:")
    print(f"Indexed URLs: {len(indexed)}")
    print(f"Not Indexed URLs: {len(not_indexed)}")
    print("="*60)
    
    if not_indexed:
        print("\n[X] THE FOLLOWING URLs ARE NOT INDEXED:")
        for url, reason in not_indexed:
            print(f"{url}  ({reason})")
            
    if indexed:
        print("\n[INDEXED] THE FOLLOWING URLs ARE INDEXED:")
        for url, status in indexed:
            print(f"{url}")

if __name__ == "__main__":
    check_indexing()
