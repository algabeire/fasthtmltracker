# api/index.py
# api/index.py
from fasthtml.common import *

# 1. Initialize FastHTML
fast_app_instance, rt = fast_app()

# 2. Explicitly expose the underlying application app variable Vercel requires
app = fast_app_instance

@rt('/')
def get():
    return Titled("Ledger budget tracker", P("Your FastHTML dashboard is live!"))
