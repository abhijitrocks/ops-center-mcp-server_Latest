import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

_scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive',
]
_client = None
_sheet_map = {}

def init(sheet_id: str, cred_path: str = 'data/credentials.json'):
    global _client, _sheet_map
    creds = ServiceAccountCredentials.from_json_keyfile_name(cred_path, _scope)
    _client = gspread.authorize(creds)
    ss = _client.open_by_key(sheet_id)
    for ws in ss.worksheets():
        values = ws.get_all_records()
        _sheet_map[ws.title] = pd.DataFrame(values)

def _load_sheet(name: str) -> pd.DataFrame:
    return _sheet_map[name].copy()

def _save_sheet(df: pd.DataFrame, name: str):
    ws = _client.open_by_key(_client.auth.service_account_email).worksheet(name)
    ws.clear()
    ws.update([df.columns.values.tolist()] + df.fillna('').values.tolist())
    _sheet_map[name] = df.copy()
