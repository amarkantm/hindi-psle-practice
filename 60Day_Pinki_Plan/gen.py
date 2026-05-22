import os
d = "/Users/amar/Downloads/Hindi-2012-2025/60Day_Pinki_Plan"

CSS = """<style>
:root{--navy:#000080;--saffron:#FF9933;}
*{box-sizing:border-box;margin:0;padding:0;}
body{font-family:'Segoe UI',Arial,sans-serif;background:#f5f5f5;color:#1a1a1a;font-size:13px;line-height:1.6;}
.page-top{background:linear-gradient(135deg,#000080,#003580);color:white;padding:18px 28px;border-bottom:5px solid #FF9933;}
.page-top h1{font-size:20px;}.page-top p{font-size:11px;opacity:.8;margin-top:4px;}
.stripe{display:flex;height:4px;}.stripe div{flex:1;}
.paper{background:white;margin:18px 22px;border-radius:10px;box-shadow:0 2px 8px rgba(0,0,0,.09);overflow:hidden;}
.paper-head{padding:12px 18px;display:flex;align-items:center;justify-content:space-between;border-bottom:2px solid #eee;}
.paper-head.weekend{background:#fff8e1;border-bottom-color:#ffe082;}
.paper-head.weekday{background:#ede7f6;border-bottom-color:#ce93d8;}
.paper-head.hard-wknd{background:#fce4ec;border-bottom-color:#ef9a9a;}
.paper-title{font-size:15px;font-weight:700;color:var(--navy);}
.paper-meta{font-size:11px;color:#555;text-align:right;}
.pinki-band{background:var(--navy);color:white;padding:5px 18px;font-size:11px;display:flex;justify-content:space-between;}
.section{padding:16px 20px;border-bottom:1px solid #f0f0f0;}
.section:last-child{border-bottom:none;}
.sec-head{display:flex;align-items:center;gap:10px;margin-bottom:10px;}
.sec-tag{background:var(--navy);color:white;font-size:10px;font-weight:700;padding:3px 9px;border-radius:4px;}
.sec-title{font-size:14px;font-weight:700;color:var(--navy);}
.sec-marks{font-size:11px;color:#666;margin-left:auto;}
.sec-instr{font-size:12px;color:#444;background:#f9f9f9;border-left:3px solid var(--navy);padding:6px 10px;margin-bottom:12px;border-radius:0 4px 4px 0;}
.q-block{margin-bottom:12px;}
.q-num{font-size:12px;font-weight:700;color:var(--navy);min-width:24px;display:inline-block;}
.q-text{font-size:13px;color:#1a1a1a;line-height:1.7;}
.blank{display:inline-block;min-width:120px;border-bottom:2px solid #333;margin:0 4px;vertical-align:bottom;}
.q-options{display:grid;grid-template-columns:1fr 1fr;gap:4px 16px;margin-top:6px;margin-left:28px;}
.q-opt{font-size:12px;color:#333;}
.q-opt span{display:inline-block;width:18px;height:18px;border:1.5px solid #999;border-radius:50%;margin-right:5px;vertical-align:middle;}
.ans-key{background:#fffde7;border:1px solid #ffe082;border-radius:6px;padding:10px 14px;margin-top:14px;}
.ans-key h4{font-size:11px;font-weight:700;color:#b8860b;margin-bottom:6px;text-transform:uppercase;letter-spacing:.5px;}
.ak-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:4px;}
.ak-item{font-size:11px;color:#333;}.ak-item b{color:var(--navy);}
.passage{background:#f8f9fa;border-left:4px solid var(--navy);padding:12px 16px;border-radius:0 8px 8px 0;margin-bottom:14px;font-size:13px;line-height:1.9;}
.blank-num{background:#000080;color:white;font-size:10px;font-weight:700;padding:1px 6px;border-radius:3px;margin:0 2px;}
.writing-prompt{background:#fff3e0;border:1.5px solid #ffcc80;border-radius:8px;padding:14px;}
.writing-prompt h4{color:#e65100;font-size:13px;font-weight:700;margin-bottom:8px;}
.wp-bullets{margin-left:16px;margin-top:6px;}
.wp-bullets li{font-size:12px;color:#444;margin-bottom:4px;}
.w-line{border-bottom:1px solid #ccc;min-height:28px;margin-bottom:5px;}
.score-box{background:#fff8e1;border:1px solid #ffe082;border-radius:6px;padding:8px 14px;display:flex;gap:20px;align-items:center;margin-top:10px;flex-wrap:wrap;}
.score-box.hard{background:#fce4ec;border-color:#ef9a9a;}
.sc-item{font-size:12px;}.sc-item b{color:var(--navy);}
.page-break{page-break-after:always;height:2px;background:#e0e0e0;margin:16px 22px;}
.notice-box{border:3px double var(--navy);border-radius:8px;padding:16px;margin-bottom:14px;background:#fafff8;}
.notice-box .notice-title{text-align:center;font-size:16px;font-weight:700;color:var(--navy);border-bottom:2px solid var(--navy);padding-bottom:8px;margin-bottom:10px;}
.notice-body{font-size:13px;line-height:1.8;}
.notice-body li{margin-bottom:6px;}
.wb-box{background:#e8eaf6;border-radius:6px;padding:10px 14px;margin-bottom:10px;font-size:12px;}
.oe-line{border-bottom:1.5px solid #aaa;min-height:32px;margin-bottom:8px;}
.tip-box{background:#e8f5e9;border-left:4px solid #2e7d32;padding:8px 12px;border-radius:0 6px 6px 0;font-size:12px;color:#1b5e20;margin-bottom:10px;}
</style>"""

STRIPE = '<div class="stripe"><div style="background:#FF9933"></div><div style="background:white;border-top:1px solid #eee"></div><div style="background:#138808"></div></div>'
FOOTER = '<div style="background:#000080;color:white;text-align:center;padding:12px;font-size:12px;">Pinki Ma\'am\'s PSLE Hindi 60-Day Plan &nbsp;|&nbsp; <b>हिंदी सीखो, आगे बढ़ो! 🌟</b></div>'

def pb(): return '<div class="page-break"></div>'

def band(label, time_marks):
    return f'<div class="pinki-band"><span>{label}</span><span>{time_marks}</span></div>'

def score(marks, time, sections=""):
    s = f'<div class="score-box"><div class="sc-item"><b>कुल अंक:</b> {marks}</div><div class="sc-item"><b>प्राप्त अंक:</b> ___ / {marks}</div><div class="sc-item"><b>समय:</b> {time}</div>'
    if sections: s += f'<div class="sc-item">{sections}</div>'
    s += '</div>'
    return s

def ans_key(title, items):
    grid = "".join(f'<div class="ak-item"><b>{k}.</b> {v}</div>' for k, v in items.items())
    return f'<div class="ans-key"><h4>उत्तर-कुंजी {title}</h4><div class="ak-grid">{grid}</div></div>'

def mcq(num, q, opts, indent=True):
    ops = "".join(f'<div class="q-opt"><span></span>({l}) {t}</div>' for l, t in opts.items())
    qtext = f'<span class="q-num">{num}.</span><span class="q-text"> {q}</span>' if q else f'<span class="q-num">{num}.</span>'
    return f'<div class="q-block">{qtext}<div class="q-options">{ops}</div></div>'

def gap_mcq(num, opts):
    return mcq(num, "", opts)

def fill_blank(num, sentence):
    return f'<div class="q-block"><span class="q-num">{num}.</span><span class="q-text"> {sentence} <span class="blank"></span></span></div>'

def oe_q(num, q):
    return f'<div class="q-block"><span class="q-num">{num}.</span><span class="q-text"> {q}</span><div class="oe-line"></div><div class="oe-line"></div></div>'

def writing_lines(n=15):
    return "".join('<div class="w-line"></div>' for _ in range(n))

