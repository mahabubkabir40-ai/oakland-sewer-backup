import os
import pickle
import datetime
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Define the scopes needed for GSC read access
SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']

def get_service():
    creds = None
    # token.pickle stores the user's access and refresh tokens
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
            
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
            
    return build('webmasters', 'v3', credentials=creds)

def fetch_data():
    service = get_service()
    
    # List verified sites in Google Search Console
    site_list = service.sites().list().execute()
    verified_sites = [site['siteUrl'] for site in site_list.get('siteEntry', [])]
    
    if not verified_sites:
        print("No verified sites found in this Google Search Console account!")
        return
        
    print("Your verified GSC properties:")
    for site in verified_sites:
        print(f"- {site}")
        
    # Automatically select the oaklandsewerpros.com property
    target_site = None
    for site in verified_sites:
        if "oaklandsewerpros.com" in site:
            target_site = site
            break
            
    if not target_site:
        print("\nCould not automatically find oaklandsewerpros.com in the list.")
        target_site = verified_sites[0]
        
    print(f"\nFetching search performance data for: {target_site}")
    
    # Define date range (last 21 days)
    today = datetime.date.today()
    three_weeks_ago = today - datetime.timedelta(days=21)
    
    start_date = three_weeks_ago.strftime('%Y-%m-%d')
    end_date = today.strftime('%Y-%m-%d')
    
    # Query Search Analytics with USA country filter
    request = {
        'startDate': start_date,
        'endDate': end_date,
        'dimensions': ['query'],
        'rowLimit': 50,
        'dimensionFilterGroups': [{
            'filters': [{
                'dimension': 'country',
                'operator': 'equals',
                'expression': 'usa'
            }]
        }]
    }
    
    response = service.searchanalytics().query(siteUrl=target_site, body=request).execute()
    
    rows = response.get('rows', [])
    if not rows:
        print("No query data found for this date range.")
        return
        
    print("\nTop 50 Queries (Last 21 Days):")
    print(f"{'Query':<45} | {'Clicks':<6} | {'Impressions':<11} | {'CTR':<6} | {'Position':<8}")
    print("-" * 85)
    for row in rows:
        query = row['keys'][0]
        clicks = row['clicks']
        impressions = row['impressions']
        ctr = f"{row['ctr']*100:.1f}%"
        position = f"{row['position']:.2f}"
        print(f"{query:<45} | {clicks:<6} | {impressions:<11} | {ctr:<6} | {position:<8}")

if __name__ == "__main__":
    fetch_data()
