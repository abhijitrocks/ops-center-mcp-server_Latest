from mcp.server.fastmcp import FastMCP
from .models import Tenant
from .storage import _load_sheet
import pandas as pd

def register(mcp: FastMCP):
    @mcp.resource("tenant://{id}")
    def get_tenant(id: int) -> Tenant:
        df = _load_sheet("Tenants")
        row = df[df["id"] == id]
        if row.empty:
            raise KeyError(f"Tenant {id} not found")
        return Tenant(**row.to_dict(orient="records")[0])
