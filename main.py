# main.py
from fasthtml.common import *

# 1. Initialize FastHTML with explicit dashboard style headers
app, rt = fast_app(hdrs=(Style(STYLE),))

COLORS = {
    "lime": "#c7f36b",
    "ink": "#17201c",
    "muted": "#738078",
    "line": "#e3e9e2",
    "soft": "#f4f7f2",
}

def icon(name, size=18):
    paths = {
        "grid": '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/>',
        "chart": '<path d="M4 19V5M4 19h17"/><path d="m7 15 3-4 3 2 5-7"/>',
        "wallet": '<path d="M4 7.5V5a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v3"/><path d="M4 7h16a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a3 3 0 0 1-3-3V7.5A.5.5 0 0 1 2.5 7H4Z"/><path d="M17 14h.01"/>',
        "repeat": '<path d="m17 2 4 4-4 4"/><path d="M3 11V9a3 3 0 0 1 3-3h15"/><path d="m7 22-4-4 4-4"/><path d="M21 13v2a3 3 0 0 1-3 3H3"/>',
        "settings": '<path d="M12 15.5a3.5 3.5 0 1 0 0-7 3.5 3.5 0 0 0 0 7Z"/><path d="M19.4 15a1.7 1.7 0 0 0 .34 1.88l.06.06-1.41 1.41-.06-.06a1.7 1.7 0 0 0-1.88-.34 1.7 1.7 0 0 0-1.03 1.56V20h-2v-.09a1.7 1.7 0 0 0-1.03-1.56 1.7 1.7 0 0 0-1.88.34l-.06.06-1.41-1.41.06-.06A1.7 1.7 0 0 0 9.4 15a1.7 1.7 0 0 0-1.56-1.03H7v-2h.84A1.7 1.7 0 0 0 9.4 11a1.7 1.7 0 0 0-.34-1.88L9 9.06l1.41-1.41.06.06a1.7 1.7 0 0 0 1.88.34A1.7 1.7 0 0 0 13.38 6.5V6h2v.5a1.7 1.7 0 0 0 1.03 1.55 1.7 1.7 0 0 0 1.88-.34l.06-.06 1.41 1.41-.06.06A1.7 1.7 0 0 0 19.4 11c.23.61.82 1.03 1.48 1.03H21v2h-.12A1.7 1.7 0 0 0 19.4 15Z"/>',
        "plus": '<path d="M12 5v14M5 12h14"/>',
        "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
        "chevron": '<path d="m7 10 5 5 5-5"/>',
        "bell": '<path d="M18 8a6 6 0 0 0-12 0c0 7-3 7-3 9h18c0-2-3-2-3-9ZM10 21h4"/>',
        "close": '<path d="m6 6 12 12M18 6 6 18"/>',
    }
    return NotStr(f'<svg class="icon" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{paths[name]}</svg>')

# 2. Main Web Application Endpoint Layout Route Mapping
@rt('/')
def get():
    return Div(
        # Complete Sidebar Navigation
        Div(
            Div(Div("L", cls="brand-mark"), "Ledger", cls="brand"),
            Div("Menu", cls="nav-label"),
            Div(
                A(icon("grid"), "Dashboard", href="#", cls="active"),
                A(icon("chart"), "Analytics", href="#"),
                A(icon("wallet"), "Wallets", href="#"),
                A(icon("repeat"), "Transactions", href="#"),
                A(icon("settings"), "Settings", href="#"),
                cls="nav"
            ),
            Div(
                Div(
                    Div("AG", cls="avatar"),
                    Div(b("Ali Gabayare"), Small("Premium Workspace"), cls="profile-text"),
                    cls="profile"
                ),
                cls="sidebar-bottom"
            ),
            cls="sidebar"
        ),
        
        # Dashboard Analytics Content Container
        Div(
            # Top Action Bar Layout
            Div(
                Div(P("Overview", cls="eyebrow"), H1("Ledger Budget Tracker")),
                Div(
                    Div("September 2026", icon("chevron"), cls="month-picker"),
                    Button(icon("bell"), cls="round-btn"),
                    Button(icon("plus"), "Add Record", cls="add-btn"),
                    cls="top-actions"
                ),
                cls="topbar"
            ),
            
            # Financial Data Aggregation Cards Layout
            Div(
                # Balance Highlight Card
                Div(
                    P("Total Net Balance", cls="eyebrow"), 
                    Div("$14,240.50", cls="balance-amount"),
                    Div("Active Growth: ", Strong("+12.4% vs last month"), cls="balance-trend"),
                    cls="card balance-card"
                ),
                # Monthly Cash Inflow Metrics Card
                Div(
                    Div(P("Monthly Inflow"), Div(icon("wallet"), cls="stat-icon purple"), cls="stat-head"),
                    Div("$4,820.00", cls="stat-value"),
                    Div(B("↑ $610"), "increased revenue streams", cls="stat-foot"),
                    cls="card stat-card"
                ),
                # Monthly Outflow Metrics Card
                Div(
                    Div(P("Monthly Outflow"), Div(icon("repeat"), cls="stat-icon orange"), cls="stat-head"),
                    Div("$1,579.50", cls="stat-value"),
                    Div(B("↓ 4.2%"), "lower recurring expenses", cls="stat-foot"),
                    cls="card stat-card"
                ),
                cls="overview"
            ),
            
            # Sub-Section Grid: Interactive Charts & Expense Ledger Tracker
            Div(
                # Graphical Bar Chart Layout Component
                Div(
                    Div(
                        Div(H2("Cash Flow Operations"), P("Visual tracking of income against outlays"), cls="section-heading"),
                        Button("Detailed Analytics", icon("arrow"), cls="text-btn"),
                        cls="section-heading"
                    ),
                    Div(
                        Div(Div(cls="bar income", style="height:70%"), Div(cls="bar expense", style="height:35%"), P("Jun", cls="bar-label"), cls="bar-group"),
                        Div(Div(cls="bar income", style="height:85%"), Div(cls="bar expense", style="height:45%"), P("Jul", cls="bar-label"), cls="bar-group"),
                        Div(Div(cls="bar income", style="height:60%"), Div(cls="bar expense", style="height:50%"), P("Aug", cls="bar-label"), cls="bar-group"),
                        Div(Div(cls="bar income", style="height:95%"), Div(cls="bar expense", style="height:30%"), P("Sep", cls="bar-label"), cls="bar-group current"),
                        cls="chart"
                    ),
                    Div(
                        Div(Div(cls="dot income"), "Total Income", cls="legend"),
                        Div(Div(cls="dot"), "Fixed Expenses", cls="legend"),
                        Div(Div(cls="dot current"), "Active Month Target", cls="legend"),
                        cls="chart-legend"
                    ),
                    cls="card section"
                ),
                
                # Active Budget Category Tracking Components
                Div(
                    Div(H2("Active Budgets"), P("Current limits allocation status"), cls="section-heading"),
                    
                    # Category Row: Housing/Rent
                    Div(
                        Div("🏠", cls="budget-emoji"),
                        Div(
                            Div("Housing & Infrastructure", Span("$850 / $1,200"), cls="budget-title"),
                            Div(Div(cls="progress-fill fill-housing", style="width:70.8%"), cls="progress"),
                            cls="budget-info"
                        ),
                        cls="budget-row"
                    ),
                    # Category Row: Logistics
                    Div(
                        Div("🚗", cls="budget-emoji"),
                        Div(
                            Div("Transport & Commute", Span("$240 / $400"), cls="budget-title"),
                            Div(Div(cls="progress-fill fill-transport", style="width:60%"), cls="progress"),
                            cls="budget-info"
                        ),
                        cls="budget-row"
                    ),
                    # Category Row: Groceries/Living
                    Div(
                        Div("🛒", cls="budget-emoji"),
                        Div(
                            Div("Groceries & Food Provision", Span("$489 / $500"), cls="budget-title"),
                            Div(Div(cls="progress-fill fill-groceries", style="width:97.8%"), cls="progress"),
                            cls="budget-info"
                        ),
                        cls="budget-row"
                    ),
                    cls="card budget-section"
                ),
                cls="content-grid"
            ),
            cls="main"
        ),
        cls="app-shell"
    )

if __name__ == '__main__':
    serve()

# 3. Global CSS Layout Stylesheets
STYLE = r"""
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');
:root{--ink:#17201c;--muted:#738078;--line:#e3e9e2;--soft:#f4f7f2;--lime:#c7f36b;font-family:'DM Sans',sans-serif;color:var(--ink);background:#fafcf9}
*{box-sizing:border-box}body{margin:0;background:#fafcf9;overflow-x:hidden}button,input,select{font:inherit}button{cursor:pointer;border:0}
.icon{display:inline-block;vertical-align:middle}.app-shell{display:flex;min-height:100vh;width:100%}
.sidebar{width:242px;background:var(--ink);color:#f9fff5;padding:27px 17px;display:flex;flex-direction:column;flex-shrink:0}
.brand{display:flex;align-items:center;gap:10px;font-family:'Space Grotesk';font-size:19px;letter-spacing:-.5px;padding:0 12px;margin-bottom:54px}
.brand-mark{width:30px;height:30px;background:var(--lime);color:var(--ink);display:grid;place-items:center;border-radius:9px;font-weight:700;font-size:13px}
.nav-label{font:500 10px 'DM Mono';color:#77847d;text-transform:uppercase;letter-spacing:1.4px;padding:0 14px;margin:0 0 12px}
.nav{display:grid;gap:5px}.nav a{display:flex;align-items:center;gap:13px;color:#99a69e;text-decoration:none;padding:12px 14px;border-radius:8px;font-size:14px}
.nav a.active{background:#29362e;color:#f9fff5}.nav a.active .icon{color:var(--lime)}.nav a:hover{color:#f9fff5;background:#233029}
.sidebar-bottom{margin-top:auto;border-top:1px solid #344139;padding-top:19px}
