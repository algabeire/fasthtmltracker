# main.py
from fasthtml.common import *

# --- 1. GLOBAL STYLING ARCHITECTURE (Defined at top layer) ---
STYLE = r"""
@import url('https://googleapis.com');
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
.profile{display:flex;align-items:center;gap:10px;padding:10px 8px}.avatar{width:34px;height:34px;background:#f3a97d;color:var(--ink);border-radius:50%;display:grid;place-items:center;font:600 12px 'DM Mono'}
.profile-text{font-size:12px}.profile-text small{display:block;color:#77847d;font-size:11px;margin-top:3px}
.main{flex:1;min-width:0;padding:38px 48px 50px}.topbar{display:flex;justify-content:space-between;align-items:center;margin-bottom:35px}
.eyebrow{font:500 11px 'DM Mono';color:var(--muted);letter-spacing:.8px;text-transform:uppercase;margin:0 0 7px}
.topbar h1{font:600 27px 'Space Grotesk';letter-spacing:-1px;margin:0}.top-actions{display:flex;align-items:center;gap:10px}
.month-picker{border:1px solid var(--line);background:#fff;border-radius:7px;padding:10px 13px;display:flex;gap:15px;align-items:center;font-size:13px}
.round-btn{background:#fff;border:1px solid var(--line);width:39px;height:39px;border-radius:50%;display:grid;place-items:center;color:var(--muted)}
.add-btn{display:flex;align-items:center;gap:7px;background:var(--ink);color:#fff;border-radius:7px;padding:11px 15px;font-size:13px;font-weight:600}
.add-btn .icon{color:var(--lime)}.overview{display:grid;grid-template-columns:minmax(270px,1.25fr) repeat(2,minmax(185px,1fr));gap:13px;margin-bottom:28px}
.card{background:#fff;border:1px solid var(--line);border-radius:10px}
.balance-card{background:#fff;border-color:var(--line);padding:21px 23px 19px;position:relative;overflow:hidden;min-height:150px}
.balance-card .eyebrow{color:var(--muted)}
.balance-amount{font:600 35px 'Space Grotesk';letter-spacing:-1.7px;margin:17px 0 11px;position:relative;z-index:2;color:var(--ink)}
.balance-trend{font:12px 'DM Mono';display:flex;gap:7px;align-items:center;position:relative;z-index:2;color:var(--muted)}
.stat-card{padding:21px 21px 16px;min-height:150px;border:1px solid var(--line)}
.stat-card.spending{background:#ffe9e7;border-color:#ffd4cf}
.stat-card.income{background:#e8f9ee;border-color:#d1f3df}
.stat-head{display:flex;align-items:center;justify-content:space-between;color:var(--muted);font-size:12px}
.stat-icon{width:27px;height:27px;border-radius:7px;display:grid;place-items:center}
.stat-icon.purple{background:#eeeaff;color:#6b5bd3}.stat-icon.orange{background:#fff0de;color:#b36b15}
.stat-card.spending .stat-icon{background:#ffd7d2;color:#d64b46}
.stat-card.income .stat-icon{background:#d7f3df;color:#1d8b58}
.stat-value{font:600 26px 'Space Grotesk';margin:19px 0 9px;letter-spacing:-1px;color:var(--ink)}
.stat-foot{font-size:12px;color:var(--muted)}
.stat-card.spending .stat-foot b{font-family:'DM Mono';color:#da4b45;margin-right:4px}
.stat-card.income .stat-foot b{font-family:'DM Mono';color:#1d8b58;margin-right:4px}
.content-grid{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(280px,.8fr);gap:18px}
.section{padding:23px}.section-heading{display:flex;justify-content:space-between;align-items:flex-start;width:100%}
.section-heading h2{font:600 17px 'Space Grotesk';letter-spacing:-.4px;margin:0}.section-heading p{color:var(--muted);font-size:12px;margin:5px 0 0}
.text-btn{display:flex;align-items:center;gap:5px;background:none;color:#506d5a;font-size:12px;font-weight:600;padding:3px}
.chart{height:195px;display:flex;align-items:flex-end;gap:15px;border-bottom:1px solid var(--line);padding:0 4px 0 35px;position:relative;margin-top:20px;background:repeating-linear-gradient(to bottom,transparent 0,transparent 47px,#edf1ed 48px)}
.bar-group{height:100%;flex:1;display:flex;align-items:flex-end;justify-content:center;gap:4px;position:relative;padding-top:12px}
.bar{width:9px;border-radius:4px 4px 0 0;min-height:5px;transition:height .35s ease}
.bar.income{background:#d8e4d7}.bar.expense{background:var(--ink)}.bar-group.current .bar.expense{background:var(--lime)}
.bar-label{position:absolute;bottom:-26px;font:10px 'DM Mono';color:var(--muted)}
.chart-legend{display:flex;gap:19px;margin-top:34px;font-size:11px;color:var(--muted)}
.legend{display:flex;gap:6px;align-items:center}.dot{width:7px;height:7px;border-radius:2px;background:var(--ink)}
.dot.income{background:#d8e4d7}.dot.current{background:var(--lime)}
.budget-section{padding:23px}
.budget-row{display:flex;align-items:center;gap:10px;margin-top:20px}
.budget-emoji{width:32px;height:32px;background:var(--soft);border-radius:8px;display:grid;place-items:center;font-size:15px}
.budget-info{flex:1;min-width:0}.budget-title{font-size:12px;font-weight:600;display:flex;justify-content:space-between;margin-bottom:7px}
.budget-title span{font:10px 'DM Mono';font-weight:400;color:var(--muted)}.progress{height:6px;background:var(--soft);border-radius:3px;overflow:hidden}
.progress-fill{height:100%;border-radius:3px}.progress-fill.fill-housing{background:#a999ff}.progress-fill.fill-transport{background:#ffb35b}.progress-fill.fill-groceries{background:#ff887c}
.spending-list{display:grid;gap:12px;margin-top:18px}
.spending-item{display:flex;align-items:center;justify-content:space-between;padding:12px 14px;border:1px solid var(--line);border-radius:10px;background:#fff}
.spending-item .left{display:flex;align-items:center;gap:12px;min-width:0}
.spending-icon{width:34px;height:34px;border-radius:10px;display:grid;place-items:center;background:var(--soft);font-size:16px}
.spending-name{font-size:13px;font-weight:600;color:var(--ink)}
.spending-meta{font-size:11px;color:var(--muted);margin-top:3px}
.spending-amount{font-size:13px;font-weight:700;color:#d64b46}
.spending-amount.positive{color:#1d8b58}
.pie-card{display:flex;flex-direction:column;gap:18px;padding:23px}
.pie-wrap{display:flex;justify-content:center;align-items:center;position:relative;margin-top:10px}
.pie{width:148px;height:148px;border-radius:50%;background:conic-gradient(#a999ff 0 35%, #ffb35b 35% 62%, #ff887c 62% 82%, #7ad7a6 82% 100%);box-shadow:inset 0 0 0 1px rgba(23,32,28,.05)}
.pie-center{position:absolute;inset:29px;background:#fff;border-radius:50%;display:grid;place-items:center;text-align:center;border:1px solid var(--line)}
.pie-total{font:700 18px 'Space Grotesk';letter-spacing:-.7px}
.pie-label{font:10px 'DM Mono';color:var(--muted);text-transform:uppercase}
.legend-list{display:grid;gap:10px;margin-top:4px}
.legend-row{display:flex;align-items:center;justify-content:space-between;gap:12px;font-size:12px;color:var(--muted)}
.legend-row .left{display:flex;align-items:center;gap:8px}
.legend-dot{width:10px;height:10px;border-radius:3px}
.legend-row strong{color:var(--ink)}
@media (max-width: 760px){
  .app-shell{flex-direction:column}
  .sidebar{width:100%;padding:18px 14px}.nav{grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}
  .nav a{padding:10px 12px}
  .main{padding:20px 16px 32px}
  .topbar{flex-direction:column;align-items:flex-start;gap:12px}
  .top-actions{width:100%;justify-content:space-between;flex-wrap:wrap}
  .month-picker{padding:8px 10px}
  .overview{grid-template-columns:1fr}
  .content-grid{grid-template-columns:1fr}
  .section{padding:18px 14px}
  .pie-card{padding:18px 14px}
  .chart{gap:8px;padding-left:8px}
  .chart-legend{flex-wrap:wrap}
  .spending-item{padding:10px 12px}
}
"""

# --- 2. APP DECLARATION CORE ---
app, rt = fast_app(hdrs=(Meta(name='viewport', content='width=device-width, initial-scale=1'), Style(STYLE)))

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

# --- 3. PAGE VIEW RENDERING ROUTE MAP ---
@rt('/')
def get():
    return Div(
        # Sidebar Panel
        Div(
            Div(Div("L", cls="brand-mark"), "Ledger", cls="brand"),
            Div("Menu", cls="nav-label"),
            Div(
                A(icon("grid"), "Dashboard", href="#", cls="active"),
                A(icon("chart"), "Analytics", href="#"),
                A(icon("wallet"), "Wallets", href="#"),
                A(icon("repeat"), "Transactions", href="#"),
                A(icon("settings"), "Settings", href="#"),
                cls="nav",
            ),
            Div(
                Div(
                    Div("AG", cls="avatar"),
                    Div(B("Ali Gabayare"), Small("Premium Workspace"), cls="profile-text"),
                    cls="profile",
                ),
                cls="sidebar-bottom",
            ),
            cls="sidebar",
        ),

        # Primary Overview Shell
        Div(
            # Dynamic Headings Panel
            Div(
                Div(P("Overview", cls="eyebrow"), H1("Ledger Budget Tracker")),
                Div(
                    Div("September 2026", icon("chevron"), cls="month-picker"),
                    Button(icon("bell"), cls="round-btn"),
                    Button(icon("plus"), "Add Record", cls="add-btn"),
                    cls="top-actions",
                ),
                cls="topbar",
            ),

            # Numeric Financial Display Cards
            Div(
                Div(
                    P("Total Net Balance", cls="eyebrow"),
                    Div("$14,240.50", cls="balance-amount"),
                    Div("Active Growth: ", Strong("+12.4% vs last month"), cls="balance-trend"),
                    cls="card balance-card",
                ),
                Div(
                    Div(P("Spending"), Div(icon("wallet"), cls="stat-icon"), cls="stat-head"),
                    Div("$2,310.40", cls="stat-value"),
                    Div(B("↓ $280"), "from last month", cls="stat-foot"),
                    cls="card stat-card spending",
                ),
                Div(
                    Div(P("Income Inflow"), Div(icon("wallet"), cls="stat-icon"), cls="stat-head"),
                    Div("$4,820.00", cls="stat-value"),
                    Div(B("↑ $610"), "increased revenue streams", cls="stat-foot"),
                    cls="card stat-card income",
                ),
                cls="overview",
            ),

            Div(
                Div(
                    Div(
                        Div(
                            H2("Recent spending"),
                            P("This month", cls="muted"),
                            cls="section-heading",
                        ),
                        Div(
                            Div(
                                Div(Span("🛒", cls="spending-icon"), Div(Strong("Groceries"), Div("Fresh market & pantry", cls="spending-meta"), cls="left-text"), cls="left"),
                                Div("-$420.00", cls="spending-amount"),
                                cls="spending-item",
                            ),
                            Div(
                                Div(Span("🚗", cls="spending-icon"), Div(Strong("Transport"), Div("Fuel + parking", cls="spending-meta"), cls="left-text"), cls="left"),
                                Div("-$190.00", cls="spending-amount"),
                                cls="spending-item",
                            ),
                            Div(
                                Div(Span("🍽️", cls="spending-icon"), Div(Strong("Dining"), Div("Restaurants & coffee", cls="spending-meta"), cls="left-text"), cls="left"),
                                Div("-$260.00", cls="spending-amount"),
                                cls="spending-item",
                            ),
                            Div(
                                Div(Span("🏠", cls="spending-icon"), Div(Strong("Rent"), Div("Apartment payment", cls="spending-meta"), cls="left-text"), cls="left"),
                                Div("-$1,250.00", cls="spending-amount"),
                                cls="spending-item",
                            ),
                            cls="spending-list",
                        ),
                        cls="card section",
                    ),
                    Div(
                        Div(
                            H2("Budget status"),
                            P("Updated today", cls="muted"),
                            cls="section-heading",
                        ),
                        Div(
                            Div(
                                Div(Span("🏠", cls="budget-emoji"), Div(Strong("Housing"), Div("$1,350 / $1,800", cls="spending-meta"), cls="budget-info"), cls="budget-row"),
                                Div(Div(cls='progress-fill fill-housing', style='width:75%'), cls='progress'),
                            ),
                            Div(
                                Div(Span("🚗", cls="budget-emoji"), Div(Strong("Transport"), Div("$420 / $600", cls="spending-meta"), cls="budget-info"), cls="budget-row"),
                                Div(Div(cls='progress-fill fill-transport', style='width:70%'), cls='progress'),
                            ),
                            Div(
                                Div(Span("🛒", cls="budget-emoji"), Div(Strong("Groceries"), Div("$610 / $800", cls="spending-meta"), cls="budget-info"), cls="budget-row"),
                                Div(Div(cls='progress-fill fill-groceries', style='width:76%'), cls='progress'),
                            ),
                            cls="budget-section",
                        ),
                        cls="card section",
                    ),
                    Div(
                        Div(
                            H2("Category spending"),
                            P("Share of this month", cls="muted"),
                            cls="section-heading",
                        ),
                        Div(
                            Div(
                                Div(
                                    Div(cls='pie'),
                                    Div(
                                        Div("$2.3k", cls='pie-total'),
                                        Div("Spent", cls='pie-label'),
                                        cls='pie-center',
                                    ),
                                    cls='pie-wrap',
                                ),
                                Div(
                                    Div(
                                        Div(Span(cls='legend-dot', style='background:#a999ff'), Strong("Housing"), cls='left'),
                                        Span("35%"),
                                        cls='legend-row',
                                    ),
                                    Div(
                                        Div(Span(cls='legend-dot', style='background:#ffb35b'), Strong("Transport"), cls='left'),
                                        Span("27%"),
                                        cls='legend-row',
                                    ),
                                    Div(
                                        Div(Span(cls='legend-dot', style='background:#ff887c'), Strong("Groceries"), cls='left'),
                                        Span("20%"),
                                        cls='legend-row',
                                    ),
                                    Div(
                                        Div(Span(cls='legend-dot', style='background:#7ad7a6'), Strong("Other"), cls='left'),
                                        Span("18%"),
                                        cls='legend-row',
                                    ),
                                    cls='legend-list',
                                ),
                                cls='pie-card',
                            ),
                            cls='card section',
                        ),
                        cls='content-grid',
                    ),
                    cls="content-grid",
                ),
                cls="main",
            ),
            cls="main",
        ),
        cls="app-shell",
    )


if __name__ == "__main__":
    serve()
