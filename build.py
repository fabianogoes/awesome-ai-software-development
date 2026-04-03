#!/usr/bin/env python3
"""
Build script: generates index.html from README.md, CONCEPTS.md, and BOOKS.md.

Usage:
    python3 build.py
    open index.html
"""

import re
from pathlib import Path

# ══════════════════════════════════════════════════════════════
# PARSING
# ══════════════════════════════════════════════════════════════

def find_section(text, header_text):
    """Extract content under a markdown header until the next header of same/higher level."""
    lines = text.split('\n')
    level = len(header_text) - len(header_text.lstrip('#'))
    found = False
    content = []

    for line in lines:
        if found:
            stripped = line.lstrip()
            if stripped.startswith('#'):
                h_level = len(stripped) - len(stripped.lstrip('#'))
                if h_level <= level:
                    break
            content.append(line)
        elif line.strip().startswith(header_text.strip()):
            found = True

    return '\n'.join(content).strip()


def parse_table(section_text):
    """Parse a markdown table into a list of dicts keyed by header names."""
    lines = [l.strip() for l in section_text.split('\n') if l.strip() and '|' in l]
    if len(lines) < 3:
        return []

    headers = [h.strip() for h in lines[0].split('|') if h.strip()]
    rows = []
    for line in lines[2:]:  # skip header + separator
        cells = [c.strip() for c in line.split('|')]
        cells = [c for c in cells if c != '']
        # Pad or trim to match headers
        while len(cells) < len(headers):
            cells.append('')
        row = {}
        for i, h in enumerate(headers):
            row[h] = cells[i] if i < len(cells) else ''
        rows.append(row)
    return rows


def extract_url(cell):
    """Extract URL from a markdown cell (handles [text](url), <url>, plain url)."""
    cell = cell.strip()
    m = re.search(r'\[([^\]]*)\]\(([^)]+)\)', cell)
    if m:
        return m.group(2)
    m = re.search(r'<(https?://[^>]+)>', cell)
    if m:
        return m.group(1)
    m = re.search(r'(https?://\S+)', cell)
    if m:
        return m.group(1)
    return cell


def extract_link_text(cell):
    """Extract display text from markdown link, or return cell as-is."""
    m = re.search(r'\[([^\]]*)\]\(', cell)
    if m:
        return m.group(1)
    return cell.strip()


def extract_domain(url):
    """Extract display domain from URL."""
    m = re.search(r'https?://(?:www\.)?([^/]+)', url)
    return m.group(1) if m else url


def parse_rating(rating_str):
    """Convert star/hourglass emoji string to (stars, label, css_class)."""
    stars = rating_str.count(':star:')
    if stars >= 5:
        return 5, 'Essencial', 'badge-essential'
    elif stars >= 3:
        return 3, 'Recomendado', 'badge-recommended'
    elif stars >= 1:
        return 1, 'Novo', 'badge-new'
    else:
        return 0, 'A testar', 'badge-testing'


def parse_concepts(text):
    """Parse CONCEPTS.md into list of (term, description, tag)."""
    concepts = []
    lines = text.split('\n')
    current_term = None
    current_desc = []
    current_tag = None

    for line in lines:
        if line.startswith('### '):
            if current_term:
                concepts.append((current_term, ' '.join(current_desc).strip(), current_tag))
            raw = line[4:].strip()
            # Check for tag in parentheses, e.g. "RAG (Retrieval-Augmented Generation)"
            tag_match = re.match(r'^(.+?)\s*\((.+)\)\s*$', raw)
            if tag_match:
                current_term = tag_match.group(1).strip()
                current_tag = tag_match.group(2).strip()
            elif ' / ' in raw:
                parts = raw.split(' / ')
                current_term = raw
                current_tag = None
            else:
                current_term = raw
                current_tag = None
            current_desc = []
        elif line.startswith('# ') and not line.startswith('### '):
            continue
        elif current_term and line.strip():
            current_desc.append(line.strip())

    if current_term:
        concepts.append((current_term, ' '.join(current_desc).strip(), current_tag))

    return concepts


def parse_courses(section_text):
    """Parse course list items into (name, url, provider)."""
    courses = []
    for line in section_text.split('\n'):
        line = line.strip()
        if not line.startswith('- '):
            continue
        line = line[2:].strip()
        # Handle markdown links
        links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', line)
        if links:
            name = links[0][0]
            url = links[0][1]
            # Try to extract provider from the name or surrounding text
            provider = extract_domain(url)
            # Clean up known providers
            if 'anthropic' in url or 'skilljar' in url:
                provider = 'Anthropic Academy'
            elif 'deeplearning.ai' in url:
                provider = 'DeepLearning.ai'
            elif 'branas.io' in url:
                # Extract author names from the line
                author_match = re.search(r'com\s+(.+?)(?:\]|\))', line)
                if author_match:
                    provider = author_match.group(1).strip()
                else:
                    provider = 'Branas.io'
            courses.append((name, url, provider))
    return courses


# ══════════════════════════════════════════════════════════════
# HTML GENERATION
# ══════════════════════════════════════════════════════════════

def html_escape(text):
    """Basic HTML escaping."""
    return (text
            .replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('"', '&quot;'))


def gen_tool_card(name, description, url, domain, stars, label, css_class):
    """Generate HTML for a tool card."""
    dots = ''
    if stars > 0 or css_class != 'badge-testing':
        dots_html = ''
        for i in range(5):
            filled = ' filled' if i < stars else ''
            dots_html += f'<span class="rating-dot{filled}"></span>\n'
        dots = f'<div class="rating">\n{dots_html}</div>'

    return f'''<div class="card">
  <div class="card-header">
    <span class="card-name"><a href="{html_escape(url)}" target="_blank" rel="noopener">{html_escape(name)}</a></span>
    <span class="badge {css_class}">{html_escape(label)}</span>
  </div>
  <p class="card-description">{html_escape(description)}</p>
  <div class="card-footer">
    <span class="card-link">{html_escape(domain)}</span>
    {dots}
  </div>
</div>'''


def gen_pub_item(title, url, domain, icon_type='article'):
    """Generate HTML for a publication list item."""
    icon_char = '&#9997;' if icon_type == 'article' else '&#9654;'
    icon_class = icon_type
    return f'''<a href="{html_escape(url)}" target="_blank" rel="noopener" class="pub-item">
  <div class="pub-icon {icon_class}">{icon_char}</div>
  <div class="pub-content">
    <span class="pub-title">{html_escape(title)}</span>
    <div class="pub-source">{html_escape(domain)}</div>
  </div>
  <span class="pub-arrow">&#8594;</span>
</a>'''


def gen_glossary_item(term, description, tag=None):
    """Generate HTML for a glossary accordion item."""
    tag_html = ''
    if tag:
        tag_html = f'<span class="glossary-term-tag">{html_escape(tag)}</span>'
    return f'''<div class="glossary-item">
  <button class="glossary-toggle" onclick="toggleGlossary(this)">
    <div class="glossary-term">
      <span class="glossary-term-text">{html_escape(term)}</span>
      {tag_html}
    </div>
    <span class="glossary-chevron">&#9660;</span>
  </button>
  <div class="glossary-body">
    <div class="glossary-body-inner">{html_escape(description)}</div>
  </div>
</div>'''


def gen_book_card(title, author, url, emoji_idx=0):
    """Generate HTML for a book card."""
    emojis = ['&#128218;', '&#128212;', '&#128213;', '&#128214;', '&#128216;']
    emoji = emojis[emoji_idx % len(emojis)]
    return f'''<a href="{html_escape(url)}" target="_blank" rel="noopener" class="book-card">
  <div class="book-emoji">{emoji}</div>
  <div class="book-title">{html_escape(title)}</div>
  <div class="book-author">{html_escape(author)}</div>
</a>'''


def gen_course_card(name, url, provider):
    """Generate HTML for a course card."""
    return f'''<a href="{html_escape(url)}" target="_blank" rel="noopener" class="course-card">
  <div class="course-icon">&#127891;</div>
  <div class="course-info">
    <span class="course-name">{html_escape(name)}</span>
    <span class="course-provider">{html_escape(provider)}</span>
  </div>
</a>'''


def gen_util_item(name, description, url):
    """Generate HTML for a utility item."""
    return f'''<div class="util-item">
  <div class="util-icon">&#128295;</div>
  <div class="util-content">
    <a href="{html_escape(url)}" target="_blank" rel="noopener" class="util-name">{html_escape(name)}</a>
    <p class="util-desc">{html_escape(description)}</p>
  </div>
</div>'''


def gen_section(section_id, icon_char, icon_color, title, content_html, subtitle=None):
    """Wrap content in a section with header."""
    sub = ''
    if subtitle:
        sub = f'<p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 1.25rem;">{html_escape(subtitle)}</p>'
    return f'''<section class="section" id="{section_id}">
  <div class="section-header">
    <div class="section-icon {icon_color}">{icon_char}</div>
    <h2 class="section-title">{html_escape(title)}</h2>
  </div>
  {sub}
  {content_html}
</section>'''


# ══════════════════════════════════════════════════════════════
# PROCESS TOOLS TABLE
# ══════════════════════════════════════════════════════════════

def process_tools(rows, name_col='Ferramenta', desc_col='Descrição', link_col='Link', rating_col='Avaliação'):
    """Process a tools table into card HTML."""
    cards = []
    for row in rows:
        name = row.get(name_col, row.get('Skill', '')).strip()
        desc = row.get(desc_col, '').strip()
        link_raw = row.get(link_col, '').strip()
        rating_raw = row.get(rating_col, row.get('Avaliação', row.get('...', ''))).strip()

        url = extract_url(link_raw)
        # If name column has a link, use that URL
        if '[' in name:
            name = extract_link_text(row.get(name_col, row.get('Skill', '')))

        domain = extract_domain(url)
        stars, label, css_class = parse_rating(rating_raw)
        cards.append(gen_tool_card(name, desc, url, domain, stars, label, css_class))

    return '<div class="card-grid">\n' + '\n'.join(cards) + '\n</div>'


def normalize_tool_rows(rows, source_col, target_col='Ferramenta'):
    """Normalize tool-like tables so different first-column names can be rendered together."""
    normalized = []
    for row in rows:
        copy = dict(row)
        if source_col in copy and target_col not in copy:
            copy[target_col] = copy[source_col]
        normalized.append(copy)
    return normalized


def process_publications(rows, icon_type='article'):
    """Process a publications table into list HTML."""
    items = []
    for row in rows:
        title = row.get('Post', '').strip()
        link_raw = row.get('Link', '').strip()
        url = extract_url(link_raw)
        domain = extract_domain(url)
        items.append(gen_pub_item(title, url, domain, icon_type))
    return '<div class="pub-list">\n' + '\n'.join(items) + '\n</div>'


# ══════════════════════════════════════════════════════════════
# HTML TEMPLATE
# ══════════════════════════════════════════════════════════════

def build_page(sections_html, stats):
    """Build the complete HTML page."""
    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Awesome AI Software Development</title>
  <meta name="description" content="Uma lista curada de ferramentas, frameworks, conceitos e referências para quem usa Inteligência Artificial no desenvolvimento de software.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,700;12..96,800&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg-deep: #0C0A09;
      --bg-surface: #1C1917;
      --bg-elevated: #292524;
      --bg-hover: #322E2B;
      --accent: #E07C4C;
      --accent-soft: rgba(224, 124, 76, 0.15);
      --accent-glow: rgba(224, 124, 76, 0.08);
      --accent-light: #F2A27B;
      --green: #6EE7A0;
      --green-soft: rgba(110, 231, 160, 0.12);
      --blue: #7CB3F2;
      --blue-soft: rgba(124, 179, 242, 0.12);
      --yellow: #F2D07C;
      --yellow-soft: rgba(242, 208, 124, 0.12);
      --purple: #B07CF2;
      --purple-soft: rgba(176, 124, 242, 0.12);
      --text-primary: #FAFAF9;
      --text-secondary: #A8A29E;
      --text-muted: #78716C;
      --border: #2A2725;
      --border-light: #3D3835;
      --font-display: 'Bricolage Grotesque', sans-serif;
      --font-body: 'Plus Jakarta Sans', sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
      --sidebar-width: 280px;
      --content-max: 1000px;
      --radius: 12px;
      --radius-sm: 8px;
      --transition: 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ scroll-behavior: smooth; scroll-padding-top: 2rem; }}
    body {{
      font-family: var(--font-body);
      background: var(--bg-deep);
      color: var(--text-primary);
      line-height: 1.7;
      -webkit-font-smoothing: antialiased;
      overflow-x: hidden;
    }}
    a {{ color: var(--accent-light); text-decoration: none; transition: color var(--transition); }}
    a:hover {{ color: var(--accent); }}
    ::selection {{ background: var(--accent); color: var(--bg-deep); }}
    ::-webkit-scrollbar {{ width: 6px; }}
    ::-webkit-scrollbar-track {{ background: var(--bg-deep); }}
    ::-webkit-scrollbar-thumb {{ background: var(--border-light); border-radius: 3px; }}
    ::-webkit-scrollbar-thumb:hover {{ background: var(--text-muted); }}

    .sidebar {{
      position: fixed; top: 0; left: 0;
      width: var(--sidebar-width); height: 100vh;
      background: var(--bg-surface);
      border-right: 1px solid var(--border);
      padding: 2rem 1.5rem;
      display: flex; flex-direction: column;
      z-index: 100; overflow-y: auto;
      transition: transform 0.3s ease;
    }}
    .sidebar-brand {{
      display: flex; align-items: center; gap: 0.75rem;
      margin-bottom: 2.5rem; padding-bottom: 1.5rem;
      border-bottom: 1px solid var(--border);
    }}
    .sidebar-brand svg {{ width: 36px; height: 32px; flex-shrink: 0; }}
    .sidebar-brand span {{
      font-family: var(--font-display); font-weight: 700;
      font-size: 1.05rem; color: var(--text-primary); line-height: 1.2;
    }}
    .nav-group {{ margin-bottom: 1.75rem; }}
    .nav-group-label {{
      font-family: var(--font-mono); font-size: 0.65rem; font-weight: 500;
      text-transform: uppercase; letter-spacing: 0.12em;
      color: var(--text-muted); margin-bottom: 0.6rem; padding-left: 0.75rem;
    }}
    .nav-link {{
      display: flex; align-items: center; gap: 0.6rem;
      padding: 0.5rem 0.75rem; border-radius: var(--radius-sm);
      font-size: 0.875rem; font-weight: 500;
      color: var(--text-secondary); transition: all var(--transition);
      position: relative;
    }}
    .nav-link:hover {{ color: var(--text-primary); background: var(--accent-glow); }}
    .nav-link.active {{ color: var(--accent); background: var(--accent-soft); }}
    .nav-link.active::before {{
      content: ''; position: absolute; left: 0; top: 50%;
      transform: translateY(-50%); width: 3px; height: 60%;
      background: var(--accent); border-radius: 0 2px 2px 0;
    }}
    .nav-icon {{ width: 18px; height: 18px; display: flex; align-items: center; justify-content: center; font-size: 0.85rem; flex-shrink: 0; }}
    .sidebar-footer {{ margin-top: auto; padding-top: 1.5rem; border-top: 1px solid var(--border); }}
    .sidebar-footer a {{ display: flex; align-items: center; gap: 0.5rem; font-size: 0.8rem; color: var(--text-muted); padding: 0.35rem 0; }}
    .sidebar-footer a:hover {{ color: var(--text-secondary); }}

    .menu-toggle {{
      display: none; position: fixed; top: 1rem; left: 1rem; z-index: 200;
      width: 44px; height: 44px; border-radius: var(--radius-sm);
      background: var(--bg-surface); border: 1px solid var(--border);
      color: var(--text-primary); font-size: 1.25rem; cursor: pointer;
      align-items: center; justify-content: center;
    }}
    .overlay {{ display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.6); z-index: 50; backdrop-filter: blur(4px); }}

    .main {{ margin-left: var(--sidebar-width); min-height: 100vh; }}
    .content {{ max-width: var(--content-max); margin: 0 auto; padding: 3rem 3rem 6rem; }}

    .hero {{ position: relative; padding: 4rem 0 3rem; margin-bottom: 3rem; }}
    .hero::after {{
      content: ''; position: absolute; bottom: 0; left: -3rem; right: -3rem;
      height: 1px;
      background: linear-gradient(90deg, transparent, var(--border-light) 20%, var(--border-light) 80%, transparent);
    }}
    .hero-eyebrow {{
      display: inline-flex; align-items: center; gap: 0.5rem;
      font-family: var(--font-mono); font-size: 0.75rem; font-weight: 500;
      letter-spacing: 0.08em; text-transform: uppercase;
      color: var(--accent); margin-bottom: 1.25rem;
      padding: 0.35rem 0.85rem; background: var(--accent-soft);
      border-radius: 100px; border: 1px solid rgba(224, 124, 76, 0.2);
    }}
    .hero h1 {{
      font-family: var(--font-display); font-size: clamp(2.2rem, 4vw, 3.2rem);
      font-weight: 800; line-height: 1.1; letter-spacing: -0.02em; margin-bottom: 1rem;
    }}
    .hero h1 .gradient-text {{
      background: linear-gradient(135deg, var(--accent) 0%, var(--accent-light) 50%, var(--yellow) 100%);
      -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
    }}
    .hero-description {{ font-size: 1.1rem; color: var(--text-secondary); max-width: 600px; line-height: 1.7; }}
    .hero-stats {{ display: flex; gap: 2rem; margin-top: 2rem; }}
    .hero-stat {{ display: flex; flex-direction: column; }}
    .hero-stat-value {{ font-family: var(--font-display); font-size: 1.8rem; font-weight: 700; color: var(--text-primary); }}
    .hero-stat-label {{ font-size: 0.8rem; color: var(--text-muted); font-weight: 500; }}

    .section {{ margin-bottom: 4rem; animation: fadeUp 0.5s ease both; }}
    .section-header {{
      display: flex; align-items: center; gap: 0.75rem;
      margin-bottom: 1.75rem; padding-bottom: 1rem;
      border-bottom: 1px solid var(--border);
    }}
    .section-icon {{
      width: 40px; height: 40px; border-radius: var(--radius-sm);
      display: flex; align-items: center; justify-content: center;
      font-size: 1.2rem; flex-shrink: 0;
    }}
    .section-icon.orange {{ background: var(--accent-soft); }}
    .section-icon.green {{ background: var(--green-soft); }}
    .section-icon.blue {{ background: var(--blue-soft); }}
    .section-icon.yellow {{ background: var(--yellow-soft); }}
    .section-icon.purple {{ background: var(--purple-soft); }}
    .section-title {{ font-family: var(--font-display); font-size: 1.5rem; font-weight: 700; letter-spacing: -0.01em; }}

    .card-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 1rem; }}
    .card {{
      background: var(--bg-surface); border: 1px solid var(--border);
      border-radius: var(--radius); padding: 1.25rem;
      transition: all var(--transition); position: relative; overflow: hidden;
    }}
    .card::before {{
      content: ''; position: absolute; top: 0; left: 0; right: 0;
      height: 2px; background: transparent; transition: background var(--transition);
    }}
    .card:hover {{
      border-color: var(--border-light); background: var(--bg-elevated);
      transform: translateY(-2px); box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }}
    .card:hover::before {{ background: linear-gradient(90deg, var(--accent), var(--accent-light)); }}
    .card-header {{ display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 0.6rem; }}
    .card-name {{ font-family: var(--font-display); font-weight: 700; font-size: 1rem; color: var(--text-primary); }}
    .card-name a {{ color: inherit; }}
    .card-name a:hover {{ color: var(--accent); }}
    .card-description {{ font-size: 0.85rem; color: var(--text-secondary); line-height: 1.6; }}
    .card-footer {{
      display: flex; align-items: center; justify-content: space-between;
      margin-top: 1rem; padding-top: 0.75rem; border-top: 1px solid var(--border);
    }}
    .card-link {{ font-family: var(--font-mono); font-size: 0.7rem; color: var(--text-muted); display: flex; align-items: center; gap: 0.3rem; }}
    .card-link:hover {{ color: var(--accent-light); }}

    .badge {{
      display: inline-flex; align-items: center; gap: 0.3rem;
      padding: 0.2rem 0.55rem; border-radius: 100px;
      font-size: 0.7rem; font-weight: 600; font-family: var(--font-mono); white-space: nowrap;
    }}
    .badge-essential {{ background: var(--accent-soft); color: var(--accent); border: 1px solid rgba(224, 124, 76, 0.25); }}
    .badge-recommended {{ background: var(--green-soft); color: var(--green); border: 1px solid rgba(110, 231, 160, 0.2); }}
    .badge-new {{ background: var(--blue-soft); color: var(--blue); border: 1px solid rgba(124, 179, 242, 0.2); }}
    .badge-testing {{ background: var(--yellow-soft); color: var(--yellow); border: 1px solid rgba(242, 208, 124, 0.2); }}
    .rating {{ display: flex; gap: 3px; }}
    .rating-dot {{ width: 6px; height: 6px; border-radius: 50%; background: var(--border-light); }}
    .rating-dot.filled {{ background: var(--accent); }}

    .pub-list {{ display: flex; flex-direction: column; gap: 0.5rem; }}
    .pub-item {{
      display: flex; align-items: center; gap: 1rem;
      padding: 1rem 1.25rem; background: var(--bg-surface);
      border: 1px solid var(--border); border-radius: var(--radius);
      transition: all var(--transition);
    }}
    .pub-item:hover {{ border-color: var(--border-light); background: var(--bg-elevated); transform: translateX(4px); }}
    .pub-icon {{
      width: 36px; height: 36px; border-radius: var(--radius-sm);
      display: flex; align-items: center; justify-content: center;
      font-size: 1rem; flex-shrink: 0;
    }}
    .pub-icon.article {{ background: var(--green-soft); }}
    .pub-icon.video {{ background: var(--purple-soft); }}
    .pub-content {{ flex: 1; min-width: 0; }}
    .pub-title {{ font-size: 0.9rem; font-weight: 600; color: var(--text-primary); display: block; }}
    .pub-title:hover {{ color: var(--accent-light); }}
    .pub-source {{ font-family: var(--font-mono); font-size: 0.7rem; color: var(--text-muted); margin-top: 0.15rem; }}
    .pub-arrow {{ color: var(--text-muted); font-size: 0.85rem; transition: all var(--transition); }}
    .pub-item:hover .pub-arrow {{ color: var(--accent); transform: translateX(3px); }}

    .glossary {{ display: flex; flex-direction: column; gap: 0.75rem; }}
    .glossary-item {{
      background: var(--bg-surface); border: 1px solid var(--border);
      border-radius: var(--radius); overflow: hidden;
      transition: border-color var(--transition);
    }}
    .glossary-item:hover {{ border-color: var(--border-light); }}
    .glossary-toggle {{
      width: 100%; display: flex; align-items: center; justify-content: space-between;
      padding: 1rem 1.25rem; background: none; border: none; cursor: pointer;
      color: var(--text-primary); font-family: var(--font-body);
    }}
    .glossary-term {{ display: flex; align-items: center; gap: 0.6rem; }}
    .glossary-term-text {{ font-family: var(--font-display); font-weight: 700; font-size: 1rem; }}
    .glossary-term-tag {{
      font-family: var(--font-mono); font-size: 0.65rem;
      padding: 0.15rem 0.45rem; border-radius: 4px;
      background: var(--accent-soft); color: var(--accent);
    }}
    .glossary-chevron {{ font-size: 0.8rem; color: var(--text-muted); transition: transform var(--transition); }}
    .glossary-item.open .glossary-chevron {{ transform: rotate(180deg); }}
    .glossary-body {{ max-height: 0; overflow: hidden; transition: max-height 0.3s ease; }}
    .glossary-item.open .glossary-body {{ max-height: 300px; }}
    .glossary-body-inner {{
      padding: 0 1.25rem 1.25rem; font-size: 0.875rem;
      color: var(--text-secondary); line-height: 1.7;
      border-top: 1px solid var(--border); padding-top: 1rem;
    }}

    .book-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1rem; }}
    .book-card {{
      background: var(--bg-surface); border: 1px solid var(--border);
      border-radius: var(--radius); padding: 1.5rem;
      transition: all var(--transition); display: flex; flex-direction: column;
    }}
    .book-card:hover {{
      border-color: var(--border-light); background: var(--bg-elevated);
      transform: translateY(-2px); box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }}
    .book-emoji {{ font-size: 2rem; margin-bottom: 0.75rem; }}
    .book-title {{ font-family: var(--font-display); font-weight: 700; font-size: 1rem; color: var(--text-primary); margin-bottom: 0.35rem; }}
    .book-title a {{ color: inherit; }}
    .book-title a:hover {{ color: var(--accent); }}
    .book-author {{ font-size: 0.85rem; color: var(--text-muted); }}

    .course-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 1rem; }}
    .course-card {{
      background: var(--bg-surface); border: 1px solid var(--border);
      border-radius: var(--radius); padding: 1.25rem;
      transition: all var(--transition); display: flex; align-items: flex-start; gap: 1rem;
    }}
    .course-card:hover {{
      border-color: var(--border-light); background: var(--bg-elevated);
      transform: translateY(-2px); box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }}
    .course-icon {{
      width: 40px; height: 40px; border-radius: var(--radius-sm);
      background: var(--purple-soft); display: flex; align-items: center;
      justify-content: center; font-size: 1.1rem; flex-shrink: 0;
    }}
    .course-info {{ flex: 1; }}
    .course-name {{ font-weight: 600; font-size: 0.9rem; color: var(--text-primary); display: block; margin-bottom: 0.25rem; }}
    .course-name:hover {{ color: var(--accent-light); }}
    .course-provider {{ font-family: var(--font-mono); font-size: 0.7rem; color: var(--text-muted); }}

    .util-list {{ display: flex; flex-direction: column; gap: 0.5rem; }}
    .util-item {{
      display: flex; align-items: flex-start; gap: 1rem; padding: 1.25rem;
      background: var(--bg-surface); border: 1px solid var(--border);
      border-radius: var(--radius); transition: all var(--transition);
    }}
    .util-item:hover {{ border-color: var(--border-light); background: var(--bg-elevated); }}
    .util-icon {{
      width: 36px; height: 36px; border-radius: var(--radius-sm);
      background: var(--yellow-soft); display: flex; align-items: center;
      justify-content: center; font-size: 1rem; flex-shrink: 0;
    }}
    .util-content {{ flex: 1; }}
    .util-name {{ font-weight: 600; font-size: 0.9rem; color: var(--text-primary); display: block; margin-bottom: 0.2rem; }}
    .util-name:hover {{ color: var(--accent-light); }}
    .util-desc {{ font-size: 0.825rem; color: var(--text-secondary); line-height: 1.6; }}

    .footer {{
      margin-top: 4rem; padding: 2rem 0; border-top: 1px solid var(--border);
      display: flex; align-items: center; justify-content: space-between;
    }}
    .footer-license {{ display: flex; align-items: center; gap: 0.5rem; font-size: 0.8rem; color: var(--text-muted); }}
    .footer-license-badge {{
      padding: 0.25rem 0.6rem; background: var(--bg-elevated);
      border: 1px solid var(--border); border-radius: 4px;
      font-family: var(--font-mono); font-size: 0.7rem; font-weight: 500; color: var(--text-secondary);
    }}
    .footer-links {{ display: flex; gap: 1.25rem; }}
    .footer-links a {{ font-size: 0.8rem; color: var(--text-muted); }}
    .footer-links a:hover {{ color: var(--text-secondary); }}

    @keyframes fadeUp {{
      from {{ opacity: 0; transform: translateY(20px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}
    .section:nth-child(1) {{ animation-delay: 0s; }}
    .section:nth-child(2) {{ animation-delay: 0.05s; }}
    .section:nth-child(3) {{ animation-delay: 0.1s; }}
    .section:nth-child(4) {{ animation-delay: 0.15s; }}
    .section:nth-child(5) {{ animation-delay: 0.2s; }}
    .section:nth-child(6) {{ animation-delay: 0.25s; }}
    .section:nth-child(7) {{ animation-delay: 0.3s; }}

    @media (max-width: 900px) {{
      .sidebar {{ transform: translateX(-100%); }}
      .sidebar.open {{ transform: translateX(0); }}
      .menu-toggle {{ display: flex; }}
      .overlay.visible {{ display: block; }}
      .main {{ margin-left: 0; }}
      .content {{ padding: 4.5rem 1.5rem 4rem; }}
      .card-grid {{ grid-template-columns: 1fr; }}
      .hero-stats {{ gap: 1.5rem; }}
      .footer {{ flex-direction: column; gap: 1rem; text-align: center; }}
    }}
    @media (max-width: 480px) {{
      .content {{ padding: 4.5rem 1rem 3rem; }}
      .hero h1 {{ font-size: 1.8rem; }}
      .hero-stats {{ flex-wrap: wrap; gap: 1rem; }}
      .book-grid, .course-grid {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>
  <button class="menu-toggle" onclick="toggleSidebar()" aria-label="Abrir menu">
    <span id="menu-icon">&#9776;</span>
  </button>
  <div class="overlay" id="overlay" onclick="toggleSidebar()"></div>

  <nav class="sidebar" id="sidebar">
    <div class="sidebar-brand">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 90">
        <style>
          .sb-body{{animation:sb-jump .5s ease-in-out infinite;transform-origin:center bottom}}
          .sb-shadow{{animation:sb-sh .5s ease-in-out infinite}}
          .sb-la{{animation:sb-wl .5s ease-in-out infinite;transform-origin:right center}}
          .sb-ra{{animation:sb-wr .5s ease-in-out infinite;transform-origin:left center}}
          .sb-le{{animation:sb-eb .5s ease-in-out infinite;transform-origin:center bottom}}
          .sb-re{{animation:sb-eb .5s ease-in-out infinite .1s;transform-origin:center bottom}}
          @keyframes sb-jump{{0%,100%{{transform:translateY(0) scaleY(1) scaleX(1)}}30%{{transform:translateY(-16px) scaleY(1.1) scaleX(.95)}}50%{{transform:translateY(-18px) scaleY(1.05) scaleX(.98)}}80%{{transform:translateY(-5px) scaleY(.95) scaleX(1.05)}}}}
          @keyframes sb-sh{{0%,100%{{transform:scaleX(1);opacity:.25}}50%{{transform:scaleX(.4);opacity:.08}}}}
          @keyframes sb-wl{{0%,100%{{transform:rotate(0)}}50%{{transform:rotate(-25deg)}}}}
          @keyframes sb-wr{{0%,100%{{transform:rotate(0)}}50%{{transform:rotate(25deg)}}}}
          @keyframes sb-eb{{0%,100%{{transform:scaleY(1)}}40%{{transform:scaleY(1.2)}}60%{{transform:scaleY(.85)}}}}
        </style>
        <ellipse class="sb-shadow" cx="50" cy="82" rx="22" ry="5" fill="#000"/>
        <g class="sb-body">
          <rect class="sb-le" x="22" y="10" width="8" height="14" fill="#E07C4C"/>
          <rect class="sb-re" x="70" y="10" width="8" height="14" fill="#E07C4C"/>
          <rect x="18" y="24" width="64" height="4" fill="#E07C4C"/>
          <rect x="14" y="28" width="72" height="32" fill="#E07C4C"/>
          <rect x="30" y="34" width="8" height="10" fill="#000"/>
          <rect x="62" y="34" width="8" height="10" fill="#000"/>
          <rect class="sb-la" x="2" y="36" width="12" height="8" fill="#E07C4C"/>
          <rect class="sb-ra" x="86" y="36" width="12" height="8" fill="#E07C4C"/>
          <rect x="24" y="60" width="12" height="14" fill="#E07C4C"/>
          <rect x="64" y="60" width="12" height="14" fill="#E07C4C"/>
        </g>
      </svg>
      <span>Awesome AI<br>Software Dev</span>
    </div>
    <div class="nav-group">
      <div class="nav-group-label">Ferramentas</div>
      <a href="#cli" class="nav-link"><span class="nav-icon">&#9000;</span> CLI Agents</a>
      <a href="#ide" class="nav-link"><span class="nav-icon">&#9998;</span> IDEs</a>
      <a href="#frameworks" class="nav-link"><span class="nav-icon">&#9881;</span> Frameworks</a>
      <a href="#mcp" class="nav-link"><span class="nav-icon">&#128279;</span> MCP</a>
      <a href="#plugins" class="nav-link"><span class="nav-icon">&#129525;</span> Plugins</a>
      <a href="#skills" class="nav-link"><span class="nav-icon">&#10024;</span> Skills</a>
    </div>
    <div class="nav-group">
      <div class="nav-group-label">Aprender</div>
      <a href="#artigos" class="nav-link"><span class="nav-icon">&#9997;</span> Artigos</a>
      <a href="#videos" class="nav-link"><span class="nav-icon">&#9654;</span> Videos</a>
      <a href="#cursos" class="nav-link"><span class="nav-icon">&#127891;</span> Cursos</a>
      <a href="#livros" class="nav-link"><span class="nav-icon">&#128214;</span> Livros</a>
    </div>
    <div class="nav-group">
      <div class="nav-group-label">Referencia</div>
      <a href="#utilitarios" class="nav-link"><span class="nav-icon">&#128295;</span> Utilidades</a>
      <a href="#conceitos" class="nav-link"><span class="nav-icon">&#128161;</span> Conceitos</a>
    </div>
    <div class="sidebar-footer">
      <a href="https://github.com/fabianogoes/awesome-ai-software-development" target="_blank" rel="noopener">&#10033; GitHub Repo</a>
      <a href="https://code.claude.com/docs/pt/overview" target="_blank" rel="noopener">&#10140; Claude Code Docs</a>
    </div>
  </nav>

  <div class="main">
    <div class="content">
      <header class="hero">
        <div class="hero-eyebrow">&#9733; Lista curada</div>
        <h1>
          <span class="gradient-text">Awesome AI</span><br>
          Software Development
        </h1>
        <p class="hero-description">
          Ferramentas, frameworks, conceitos e refer&ecirc;ncias para quem usa Intelig&ecirc;ncia Artificial no desenvolvimento de software.
        </p>
        <div class="hero-stats">
          <div class="hero-stat">
            <span class="hero-stat-value">{stats[0]}+</span>
            <span class="hero-stat-label">Ferramentas</span>
          </div>
          <div class="hero-stat">
            <span class="hero-stat-value">{stats[1]}</span>
            <span class="hero-stat-label">Conceitos</span>
          </div>
          <div class="hero-stat">
            <span class="hero-stat-value">{stats[2]}</span>
            <span class="hero-stat-label">Cursos</span>
          </div>
        </div>
      </header>

{sections_html}

      <footer class="footer">
        <div class="footer-license">
          <span class="footer-license-badge">MIT</span>
          Licen&ccedil;a open-source
        </div>
        <div class="footer-links">
          <a href="https://github.com/fabianogoes/awesome-ai-software-development" target="_blank" rel="noopener">GitHub</a>
          <a href="https://code.claude.com/docs/pt/overview" target="_blank" rel="noopener">Claude Code</a>
        </div>
      </footer>
    </div>
  </div>

  <script>
    function toggleSidebar() {{
      document.getElementById('sidebar').classList.toggle('open');
      document.getElementById('overlay').classList.toggle('visible');
      const icon = document.getElementById('menu-icon');
      icon.innerHTML = document.getElementById('sidebar').classList.contains('open') ? '&#10005;' : '&#9776;';
    }}
    function toggleGlossary(btn) {{
      btn.closest('.glossary-item').classList.toggle('open');
    }}
    const sections = document.querySelectorAll('.section[id]');
    const navLinks = document.querySelectorAll('.nav-link');
    function updateActiveNav() {{
      const scrollY = window.scrollY + 100;
      sections.forEach(section => {{
        const top = section.offsetTop;
        const height = section.offsetHeight;
        const id = section.getAttribute('id');
        if (scrollY >= top && scrollY < top + height) {{
          navLinks.forEach(link => {{
            link.classList.remove('active');
            if (link.getAttribute('href') === '#' + id) link.classList.add('active');
          }});
        }}
      }});
    }}
    window.addEventListener('scroll', updateActiveNav, {{ passive: true }});
    updateActiveNav();
    navLinks.forEach(link => {{
      link.addEventListener('click', () => {{
        if (window.innerWidth <= 900) toggleSidebar();
      }});
    }});
  </script>
</body>
</html>'''


# ══════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════

def main():
    base = Path(__file__).parent
    readme = (base / 'README.md').read_text(encoding='utf-8')
    concepts_md = (base / 'CONCEPTS.md').read_text(encoding='utf-8')
    books_md = (base / 'BOOKS.md').read_text(encoding='utf-8')

    # ── Parse sections ──
    cli_rows = parse_table(find_section(readme, '### CLI'))
    ide_rows = parse_table(find_section(readme, '### IDE'))
    fw_rows = parse_table(find_section(readme, '### Frameworks'))
    mcp_rows = parse_table(find_section(readme, '### MCP'))
    plugin_rows = parse_table(find_section(readme, '### Plugins'))
    skill_rows = parse_table(find_section(readme, '### Skills'))
    article_rows = parse_table(find_section(readme, '### Write'))
    video_rows = parse_table(find_section(readme, '### Video'))
    util_rows = parse_table(find_section(readme, '## Utilitários'))
    courses = parse_courses(find_section(readme, '## Cursos'))
    concepts = parse_concepts(concepts_md)
    book_rows = parse_table(books_md)

    # ── Generate sections ──
    all_sections = []

    # CLI
    cli_html = process_tools(cli_rows)
    all_sections.append(gen_section('cli', '&#9000;', 'orange', 'CLI Agents', cli_html))

    # IDE
    ide_html = process_tools(ide_rows)
    all_sections.append(gen_section('ide', '&#9998;', 'green', 'IDEs com IA', ide_html))

    # Frameworks
    fw_html = process_tools(fw_rows)
    all_sections.append(gen_section('frameworks', '&#9881;', 'blue', 'Frameworks & Bibliotecas', fw_html))

    # MCP
    mcp_html = process_tools(normalize_tool_rows(mcp_rows, 'MCP'))
    all_sections.append(gen_section('mcp', '&#128279;', 'yellow', 'MCP', mcp_html))

    # Plugins
    plugins_html = process_tools(normalize_tool_rows(plugin_rows, 'Plugin'))
    all_sections.append(gen_section('plugins', '&#129525;', 'orange', 'Plugins', plugins_html))

    # Skills
    skills_html = process_tools(normalize_tool_rows(skill_rows, 'Skill'))
    all_sections.append(gen_section('skills', '&#10024;', 'purple', 'Skills', skills_html))

    # Articles
    articles_html = process_publications(article_rows, 'article')
    all_sections.append(gen_section('artigos', '&#9997;', 'green', 'Artigos', articles_html))

    # Videos
    videos_html = process_publications(video_rows, 'video')
    all_sections.append(gen_section('videos', '&#9654;', 'purple', 'Videos', videos_html))

    # Utilities
    util_items = []
    for row in util_rows:
        name = row.get('Ferramenta', '').strip()
        desc = row.get('Descrição', '').strip()
        link_raw = row.get('Link', '').strip()
        url = extract_url(link_raw)
        util_items.append(gen_util_item(name, desc, url))
    util_html = '<div class="util-list">\n' + '\n'.join(util_items) + '\n</div>'
    all_sections.append(gen_section('utilitarios', '&#128295;', 'yellow', 'Utilidades & Referências', util_html))

    # Courses
    course_cards = [gen_course_card(name, url, prov) for name, url, prov in courses]
    courses_html = '<div class="course-grid">\n' + '\n'.join(course_cards) + '\n</div>'
    all_sections.append(gen_section('cursos', '&#127891;', 'purple', 'Cursos', courses_html))

    # Books
    book_cards = []
    for i, row in enumerate(book_rows):
        title = row.get('Livro', '').strip()
        author = row.get('Autor', '').strip()
        link_raw = row.get('Link', '').strip()
        url = extract_url(link_raw)
        publisher = extract_link_text(link_raw)
        book_cards.append(gen_book_card(title, f'{author} · {publisher}', url, i))
    books_html = '<div class="book-grid">\n' + '\n'.join(book_cards) + '\n</div>'
    all_sections.append(gen_section('livros', '&#128214;', 'orange', 'Livros', books_html))

    # Concepts
    glossary_items = [gen_glossary_item(term, desc, tag) for term, desc, tag in concepts]
    glossary_html = '<div class="glossary">\n' + '\n'.join(glossary_items) + '\n</div>'
    all_sections.append(gen_section(
        'conceitos', '&#128161;', 'yellow', 'Conceitos',
        glossary_html,
        subtitle='Glossário de termos essenciais para desenvolvimento com IA. Clique para expandir.'
    ))

    # ── Stats ──
    total_tools = len(cli_rows) + len(ide_rows) + len(fw_rows) + len(mcp_rows) + len(plugin_rows) + len(skill_rows)
    total_concepts = len(concepts)
    total_courses = len(courses)

    # ── Build page ──
    sections_combined = '\n\n'.join(all_sections)
    html = build_page(sections_combined, (total_tools, total_concepts, total_courses))

    output = base / 'index.html'
    output.write_text(html, encoding='utf-8')
    print(f'index.html gerado com sucesso ({total_tools} ferramentas, {total_concepts} conceitos, {total_courses} cursos)')


if __name__ == '__main__':
    main()
