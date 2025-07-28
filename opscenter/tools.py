from mcp.server.fastmcp import FastMCP
from .storage import _load_sheet, _save_sheet
from .models import Tenant
import pandas as pd

def register(mcp: FastMCP):
    @mcp.tool()
    def create_tenant(id: int, name: str) -> Tenant:
        df = _load_sheet("Tenants")
        new_row = {"id": id, "name": name, "created_at": "2025-01-01T00:00:00Z", "updated_at": "2025-01-01T00:00:00Z"}
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        _save_sheet(df, "Tenants")
        return Tenant(**new_row)
