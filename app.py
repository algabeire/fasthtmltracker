from fasthtml.common import *

app, rt = fast_app()

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


STYLE = r"""
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');
:root{--ink:#17201c;--muted:#738078;--line:#e3e9e2;--soft:#f4f7f2;--lime:#c7f36b;--purple:#a999ff;--orange:#ffb35b;--blue:#75c9dc;--red:#ff887c;font-family:'DM Sans',sans-serif;color:var(--ink);background:#fafcf9}
*{box-sizing:border-box}body{margin:0;background:#fafcf9}button,input,select{font:inherit}button{cursor:pointer;border:0}.icon{display:block}.app-shell{display:flex;min-height:100vh}.sidebar{width:242px;background:var(--ink);color:#f9fff5;padding:27px 17px;display:flex;flex-direction:column;flex-shrink:0}.brand{display:flex;align-items:center;gap:10px;font-family:'Space Grotesk';font-size:19px;letter-spacing:-.5px;padding:0 12px;margin-bottom:54px}.brand-mark{width:30px;height:30px;background:var(--lime);color:var(--ink);display:grid;place-items:center;border-radius:9px;font-weight:700;font-size:13px}.nav-label{font:500 10px 'DM Mono';color:#77847d;text-transform:uppercase;letter-spacing:1.4px;padding:0 14px;margin:0 0 12px}.nav{display:grid;gap:5px}.nav a{display:flex;align-items:center;gap:13px;color:#99a69e;text-decoration:none;padding:12px 14px;border-radius:8px;font-size:14px}.nav a.active{background:#29362e;color:#f9fff5}.nav a.active .icon{color:var(--lime)}.nav a:hover{color:#f9fff5;background:#233029}.sidebar-bottom{margin-top:auto;border-top:1px solid #344139;padding-top:19px}.profile{display:flex;align-items:center;gap:10px;padding:10px 8px}.avatar{width:34px;height:34px;background:#f3a97d;color:var(--ink);border-radius:50%;display:grid;place-items:center;font:600 12px 'DM Mono'}.profile-text{font-size:12px}.profile-text small{display:block;color:#77847d;font-size:11px;margin-top:3px}.main{flex:1;min-width:0;padding:38px 48px 50px}.topbar{display:flex;justify-content:space-between;align-items:center;margin-bottom:35px}.eyebrow{font:500 11px 'DM Mono';color:var(--muted);letter-spacing:.8px;text-transform:uppercase;margin:0 0 7px}.topbar h1{font:600 27px 'Space Grotesk';letter-spacing:-1px;margin:0}.top-actions{display:flex;align-items:center;gap:10px}.month-picker{border:1px solid var(--line);background:#fff;border-radius:7px;padding:10px 13px;display:flex;gap:15px;align-items:center;font-size:13px}.month-picker .icon{width:14px;color:var(--muted)}.round-btn{background:#fff;border:1px solid var(--line);width:39px;height:39px;border-radius:50%;display:grid;place-items:center;color:var(--muted)}.add-btn{display:flex;align-items:center;gap:7px;background:var(--ink);color:#fff;border-radius:7px;padding:11px 15px;font-size:13px;font-weight:600}.add-btn .icon{color:var(--lime)}.overview{display:grid;grid-template-columns:minmax(270px,1.25fr) repeat(2,minmax(185px,1fr));gap:13px;margin-bottom:28px}.card{background:#fff;border:1px solid var(--line);border-radius:10px}.balance-card{background:var(--lime);border-color:var(--lime);padding:21px 23px 19px;position:relative;overflow:hidden;min-height:150px}.balance-card:after{content:'';position:absolute;width:190px;height:190px;border:1px solid rgba(23,32,28,.16);border-radius:50%;right:-60px;top:-79px}.balance-card:before{content:'';position:absolute;width:230px;height:230px;border:1px solid rgba(23,32,28,.13);border-radius:50%;right:-70px;top:-97px}.balance-card .eyebrow{color:#566b51}.balance-amount{font:600 35px 'Space Grotesk';letter-spacing:-1.7px;margin:17px 0 11px}.balance-trend{font:12px 'DM Mono';display:flex;gap:7px;align-items:center}.balance-trend strong{font-weight:500;background:rgba(23,32,28,.11);padding:4px 6px;border-radius:4px}.stat-card{padding:21px 21px 16px;min-height:150px}.stat-head{display:flex;align-items:center;justify-content:space-between;color:var(--muted);font-size:12px}.stat-icon{width:27px;height:27px;border-radius:7px;display:grid;place-items:center}.stat-icon.purple{background:#eeeaff;color:#6b5bd3}.stat-icon.orange{background:#fff0de;color:#b36b15}.stat-value{font:600 26px 'Space Grotesk';margin:19px 0 9px;letter-spacing:-1px}.stat-foot{font:12px;color:var(--muted)}.stat-foot b{font:500 'DM Mono';color:#42a06c;margin-right:4px}.content-grid{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(280px,.8fr);gap:18px}.section{padding:23px}.section-heading{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:22px}.section-heading h2{font:600 17px 'Space Grotesk';letter-spacing:-.4px;margin:0}.section-heading p{color:var(--muted);font-size:12px;margin:5px 0 0}.text-btn{display:flex;align-items:center;gap:5px;background:none;color:#506d5a;font-size:12px;font-weight:600;padding:3px}.text-btn .icon{width:14px}.chart{height:195px;display:flex;align-items:flex-end;gap:15px;border-bottom:1px solid var(--line);padding:0 4px 0 0;position:relative;background:repeating-linear-gradient(to bottom,transparent 0,transparent 47px,#edf1ed 48px)}.chart:before{content:'$4k\A$3k\A$2k\A$1k\A$0';white-space:pre;position:absolute;left:-1px;top:-5px;transform:translateX(-100%);font:10px/48px 'DM Mono';color:#a4aea7;text-align:right;width:29px}.bar-group{height:100%;flex:1;display:flex;align-items:flex-end;justify-content:center;gap:4px;position:relative;padding-top:12px}.bar{width:9px;border-radius:4px 4px 0 0;min-height:5px;transition:height .35s ease}.bar.income{background:#d8e4d7}.bar.expense{background:var(--ink)}.bar-group.current .bar.expense{background:var(--lime)}.bar-label{position:absolute;bottom:-26px;font:10px 'DM Mono';color:var(--muted)}.chart-legend{display:flex;gap:19px;margin-top:24px;font-size:11px;color:var(--muted)}.legend{display:flex;gap:6px;align-items:center}.dot{width:7px;height:7px;border-radius:2px;background:var(--ink)}.dot.income{background:#d8e4d7}.dot.current{background:var(--lime)}.budget-section{padding:23px}.budget-row{display:flex;align-items:center;gap:10px;margin-top:20px}.budget-emoji{width:32px;height:32px;background:var(--soft);border-radius:8px;display:grid;place-items:center;font-size:15px}.budget-info{flex:1;min-width:0}.budget-title{font-size:12px;font-weight:600;display:flex;justify-content:space-between;margin-bottom:7px}.budget-title span{font:10px 'DM Mono';font-weight:400;color:var(--muted)}.progress{height:5px;background:#eef2ed;border-radius:3px;overflow:hidden}.progress i{height:100%;display:block;border-radius:3px;background:var(--ink)}.progress i.warn{background:var(--orange)}.progress i.good{background:var(--lime)}.activity{margin-top:18px}.activity-row{display:flex;align-items:center;padding:14px 0;border-top:1px solid var(--line);gap:11px}.activity-icon{width:34px;height:34px;display:grid;place-items:center;background:var(--soft);border-radius:9px;font-size:15px}.activity-copy{flex:1}.activity-copy strong{display:block;font-size:12px;font-weight:600}.activity-copy small{display:block;font-size:11px;color:var(--muted);margin-top:4px}.activity-amount{text-align:right;font:500 12px 'DM Mono'}.activity-amount small{display:block;color:#d06c62;font:10px 'DM Mono';margin-top:4px}.positive{color:#4a9b6c}.bottom-grid{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(280px,.8fr);gap:18px;margin-top:18px}.insight{background:var(--ink);color:#f7fbf5;border-radius:10px;padding:23px;display:flex;justify-content:space-between;align-items:center;overflow:hidden;position:relative}.insight:after{content:'';position:absolute;width:230px;height:230px;border:1px solid #455248;border-radius:50%;right:-80px;top:-110px}.insight-copy{max-width:390px;position:relative;z-index:1}.insight .eyebrow{color:#99a69e}.insight h2{font:600 20px 'Space Grotesk';letter-spacing:-.5px;margin:10px 0 8px}.insight p{color:#a9b4ac;font-size:12px;line-height:1.6;margin:0}.insight-mark{font:600 46px 'Space Grotesk';color:var(--lime);padding-right:16px;position:relative;z-index:1}.modal-backdrop{display:none;position:fixed;inset:0;background:rgba(23,32,28,.38);z-index:5;align-items:center;justify-content:center;padding:20px}.modal-backdrop.open{display:flex}.modal{background:#fff;width:100%;max-width:420px;border-radius:12px;padding:25px;box-shadow:0 20px 70px rgba(23,32,28,.2)}.modal-header{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:22px}.modal h2{font:600 20px 'Space Grotesk';margin:0}.modal-sub{font-size:12px;color:var(--muted);margin:5px 0 0}.close-btn{background:var(--soft);color:var(--muted);border-radius:50%;width:30px;height:30px;display:grid;place-items:center}.field{margin-bottom:15px}.field label{display:block;font:500 10px 'DM Mono';text-transform:uppercase;letter-spacing:.8px;color:var(--muted);margin-bottom:7px}.field input,.field select{width:100%;border:1px solid var(--line);background:#fbfcfa;border-radius:6px;padding:11px 12px;font-size:13px;color:var(--ink);outline:none}.field input:focus,.field select:focus{border-color:#91b66a;box-shadow:0 0 0 3px #eaf6d9}.modal-submit{width:100%;justify-content:center;margin-top:6px}.toast{position:fixed;bottom:24px;right:24px;background:var(--ink);color:#fff;padding:12px 16px;border-radius:7px;font-size:12px;opacity:0;transform:translateY(10px);transition:.25s;z-index:8}.toast.show{opacity:1;transform:translateY(0)}
@media(max-width:1000px){.sidebar{width:76px;padding-left:10px;padding-right:10px}.brand{padding:0;justify-content:center;margin-bottom:48px}.brand span,.nav-label,.nav a span,.profile-text{display:none}.nav a{justify-content:center;padding:12px}.profile{justify-content:center}.main{padding:30px 28px}.overview{grid-template-columns:1.2fr 1fr 1fr}.content-grid,.bottom-grid{grid-template-columns:1fr}.budget-section{min-height:0}}
@media(max-width:650px){.sidebar{display:none}.main{padding:24px 16px 35px}.topbar{align-items:flex-start;margin-bottom:26px}.topbar h1{font-size:23px}.top-actions{gap:6px}.month-picker{display:none}.add-btn{padding:10px}.add-btn span{display:none}.overview{grid-template-columns:1fr 1fr}.balance-card{grid-column:1/-1}.stat-card{min-height:132px;padding:17px}.stat-value{font-size:22px;margin-top:15px}.section,.budget-section,.insight{padding:18px}.chart{gap:6px;height:170px}.bar{width:7px}.chart:before{display:none}.section-heading{margin-bottom:16px}.insight-mark{font-size:32px}.bottom-grid{margin-top:15px}.topbar .eyebrow{font-size:10px}}

/* Wide finance overview refinements */
.main{max-width:1680px;padding:44px clamp(32px,5vw,86px) 64px}
.overview{grid-template-columns:minmax(340px,1.35fr) repeat(2,minmax(260px,1fr));gap:18px;margin-bottom:32px}
.balance-card{background:#fff;border-color:#d8e2d8;min-height:178px;padding:27px 29px 24px;box-shadow:0 10px 30px rgba(23,32,28,.05)}
.balance-amount{font-size:40px;margin:22px 0 13px}
.balance-trend strong{background:#e5f6d2;color:#39704a}
.stat-card{min-height:178px;padding:25px 25px 20px}
.income-card{background:#e5f6d8;border-color:#c9e7c0}
.spend-card{background:#ffe3de;border-color:#f2c4bc}
.income-card .stat-head{color:#39704a}
.spend-card .stat-head,.spend-card .stat-foot b{color:#a75048}
.stat-icon.purple{background:#c5edb6;color:#39704a}
.stat-icon.orange{background:#ffc7be;color:#a75048}
.stat-value{font-size:31px;margin:25px 0 10px}
.income-card .stat-value{color:#2f8a53}
.spend-card .stat-value{color:#c85249}
@media(max-width:650px){.main{padding:24px 16px 35px}.overview{grid-template-columns:1fr 1fr}.balance-card{grid-column:1/-1}.stat-card{min-height:132px;padding:17px}.stat-value{font-size:22px;margin-top:15px}}

/* Keep primary navigation in the header on wide screens. */
.sidebar{display:none}
.topbar{display:grid;grid-template-columns:minmax(220px,1fr) auto auto;gap:28px;align-items:center}
.header-nav{display:flex;align-items:center;gap:4px;white-space:nowrap}
.header-nav a{display:flex;align-items:center;gap:7px;color:var(--muted);text-decoration:none;padding:9px 10px;border-radius:7px;font-size:12px}
.header-nav a .icon{width:14px}
.header-nav a.active{background:var(--ink);color:#fff}
.header-nav a.active .icon{color:var(--lime)}
.header-nav a:hover{background:#e4ebe4;color:var(--ink)}
@media(max-width:1100px){.topbar{grid-template-columns:1fr auto;gap:16px}.header-nav{grid-column:1/-1;grid-row:2;order:3;overflow-x:auto;padding-bottom:2px}.top-actions{grid-column:2;grid-row:1}}
@media(max-width:650px){.topbar{display:flex;flex-wrap:wrap;gap:14px}.topbar>div:first-child{flex:1;min-width:170px}.header-nav{order:3;flex-basis:100%;overflow-x:auto}.header-nav a{padding:8px 9px}.main{width:100%}}
"""


def nav_link(label, icon_name, active=False):
    return A(icon(icon_name), Span(label), href="#", cls="active" if active else "")


def transaction_row(emoji, title, category, amount, date, negative=True):
    return Div(Div(emoji, cls="activity-icon"), Div(Strong(title), Small(category + " · " + date), cls="activity-copy"), Div(("−" if negative else "+") + amount, Small("expense" if negative else "income"), cls="activity-amount " + ("" if negative else "positive")), cls="activity-row")


@rt("/")
def get():
    chart_data = [(58, 36), (66, 46), (53, 40), (77, 57), (62, 43), (79, 50), (69, 46), (73, 52), (61, 43), (82, 51), (75, 47), (88, 58)]
    bars = [Div(Div(style=f"height:{income}%", cls="bar income"), Div(style=f"height:{expense}%", cls="bar expense"), Span(label, cls="bar-label"), cls="bar-group" + (" current" if label == "Sep" else "")) for (income, expense), label in zip(chart_data, ["Oct", "Nov", "Dec", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep"])]
    return Html(
        Head(Title("Ledger — Personal finance, made clear"), Meta(name="viewport", content="width=device-width, initial-scale=1"), Style(STYLE)),
        Body(
            Div(
                Aside(
                    Div(Div("L", cls="brand-mark"), Span("ledger"), cls="brand"),
                    P("Workspace", cls="nav-label"),
                    Nav(nav_link("Overview", "grid", True), nav_link("Analytics", "chart"), nav_link("Transactions", "wallet"), nav_link("Recurring", "repeat"), cls="nav"),
                    Div(P("Account", cls="nav-label"), Div(Div("AM", cls="avatar"), Div("Alex Morgan", Small("Personal account"), cls="profile-text"), cls="profile"), cls="sidebar-bottom"),
                    cls="sidebar",
                ),
                Div(
                    Div(Div(P("Tuesday, September 23, 2026", cls="eyebrow"), H1("Good morning, Alex.")), Nav(nav_link("Overview", "grid", True), nav_link("Analytics", "chart"), nav_link("Transactions", "wallet"), nav_link("Recurring", "repeat"), cls="header-nav"), Div(Button(icon("bell", 17), cls="round-btn", title="Notifications"), Button("Sep 2026", icon("chevron", 14), cls="month-picker"), Button(icon("plus", 17), Span("Add transaction"), cls="add-btn", onclick="openModal()"), cls="top-actions"), cls="topbar"),
                    Div(
                        Div(P("Total balance", cls="eyebrow"), Div("$12,840.40", cls="balance-amount"), Div(Strong("+12.4%"), Span("vs. last month"), cls="balance-trend"), cls="card balance-card"),
                        Div(Div(Div("Monthly income", cls="stat-head"), Div(icon("arrow", 14), cls="stat-icon purple"), cls="stat-head"), Div("+$6,200", cls="stat-value"), Div(Strong("+8.2%"), "from Aug", cls="stat-foot"), cls="card stat-card income-card"),
                        Div(Div(Div("Monthly spending", cls="stat-head"), Div(icon("chart", 14), cls="stat-icon orange"), cls="stat-head"), Div("−$3,359", cls="stat-value"), Div(Strong("−4.6%"), "under budget", cls="stat-foot"), cls="card stat-card spend-card"),
                        cls="overview",
                    ),
                    Div(
                        Div(
                            Div(Div(H2("Cash flow"), P("Income vs. expenses over the last 12 months")), Button("View report", icon("arrow", 13), cls="text-btn"), cls="section-heading"),
                            Div(*bars, cls="chart"), Div(Div(Span(cls="dot income"), "Income", cls="legend"), Div(Span(cls="dot"), "Expenses", cls="legend"), Div(Span(cls="dot current"), "Current month", cls="legend"), cls="chart-legend"), cls="card section",
                        ),
                        Div(
                            Div(Div(H2("Budget status"), P("September allocation")), Button("Manage", icon("arrow", 13), cls="text-btn"), cls="section-heading"),
                            Div(Div("🏠", cls="budget-emoji"), Div(Div("Housing", Span("$1,420 / $1,600", cls="budget-title")), Div(I(style="width:89%", cls="good"), cls="progress"), cls="budget-info"), cls="budget-row"),
                            Div(Div("🍜", cls="budget-emoji"), Div(Div("Food & dining", Span("$486 / $520", cls="budget-title")), Div(I(style="width:94%", cls="warn"), cls="progress"), cls="budget-info"), cls="budget-row"),
                            Div(Div("✈️", cls="budget-emoji"), Div(Div("Travel", Span("$248 / $600", cls="budget-title")), Div(I(style="width:41%", cls="good"), cls="progress"), cls="budget-info"), cls="budget-row"),
                            Div(Div("◌", cls="budget-emoji"), Div(Div("Subscriptions", Span("$79 / $120", cls="budget-title")), Div(I(style="width:66%", cls="progress"), cls="progress"), cls="budget-info"), cls="budget-row"),
                            cls="card budget-section",
                        ),
                        cls="content-grid",
                    ),
                    Div(
                        Div(
                            Div(Div(H2("Recent activity"), P("Your latest money moves")), Button("See all", icon("arrow", 13), cls="text-btn"), cls="section-heading"),
                            Div(transaction_row("☕", "Blue Bottle Coffee", "Food & dining", "$6.80", "Today"), transaction_row("◈", "Notion", "Subscriptions", "$10.00", "Yesterday"), transaction_row("↗", "Acme Studio", "Freelance income", "$850.00", "Sep 20", False), transaction_row("🚇", "City Transit", "Transport", "$42.50", "Sep 19"), cls="activity"),
                            cls="card section",
                        ),
                        Div(Div(P("A little nudge", cls="eyebrow"), H2("You’re on track to save $1,240 this month."), P("That’s 20% of your income, and $180 more than your August average.", cls="insight-copy"), Div("20%", cls="insight-mark"), cls="insight"),
                        cls="bottom-grid",
                    ),
                cls="main"),
                Div(
                    Div(
                        Div(Div(H2("Add transaction"), P("Keep your ledger up to date", cls="modal-sub")), Button(icon("close", 16), cls="close-btn", onclick="closeModal()"), cls="modal-header"),
                        Form(
                            Div(Label("Description", fr="description"), Input(id="description", name="description", placeholder="e.g. Weekly groceries", required=True), cls="field"),
                            Div(Label("Amount", fr="amount"), Input(id="amount", name="amount", type="number", step="0.01", placeholder="0.00", required=True), cls="field"),
                            Div(Label("Category", fr="category"), Select(Option("Food & dining", value="food"), Option("Housing", value="housing"), Option("Transport", value="transport"), Option("Subscriptions", value="subscriptions"), Option("Other", value="other"), id="category", name="category"), cls="field"),
                            Button(icon("plus", 16), "Save transaction", type="button", cls="add-btn modal-submit", onclick="saveTransaction()"),
                        ),
                        cls="modal",
                    ),
                    cls="modal-backdrop",
                    id="modal",
                ),
                Div("Transaction saved", cls="toast", id="toast"),
                Script("""
                const modal = document.getElementById('modal');
                const toast = document.getElementById('toast');
                function openModal(){ modal.classList.add('open'); document.getElementById('description').focus(); }
                function closeModal(){ modal.classList.remove('open'); }
                modal.addEventListener('click', (e) => { if(e.target === modal) closeModal(); });
                document.addEventListener('keydown', (e) => { if(e.key === 'Escape') closeModal(); });
                function saveTransaction(){
                  const description = document.getElementById('description').value.trim();
                  const amount = document.getElementById('amount').value;
                  if(!description || !amount) return;
                  closeModal();
                  document.querySelector('.modal form').reset();
                  toast.classList.add('show');
                  setTimeout(() => toast.classList.remove('show'), 2600);
                }
                """),
            )
        )
    )
    )


if __name__ == "__main__":
    serve(live=True)
