# api/index.py
from fasthtml.common import *

app, rt = fast_app()

@rt('/')
def get():
    return Titled("Ledger budget tracker", P("Your FastHTML dashboard is live!"))

# Important: Keep routes here. Do NOT include serve() at the bottom for Vercel.
