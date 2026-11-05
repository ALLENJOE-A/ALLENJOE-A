#!/usr/bin/env python3
"""
Custom GitHub Contribution Heatmap Generator
Theme: Electric Cyan (#00D9FF) & Semiconductor Blue (#268BFF)
Author: Allen Joe A (github.com/ALLENJOE-A)

Fetches genuine contribution data from the GitHub GraphQL API and renders
a responsive, dark-mode SVG contribution heatmap with cyan/blue intensity levels.
"""

import argparse
import datetime
import json
import os
import subprocess
import sys
import urllib.request


def fetch_contributions(username: str, token: str | None = None) -> dict:
    query = """
    query($userName: String!) {
      user(login: $userName) {
        contributionsCollection {
          contributionCalendar {
            totalContributions
            weeks {
              contributionDays {
                contributionCount
                date
                weekday
              }
            }
          }
        }
      }
    }
    """
    token = token or os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")

    if token:
        payload = json.dumps({"query": query, "variables": {"userName": username}}).encode("utf-8")
        req = urllib.request.Request(
            "https://api.github.com/graphql",
            data=payload,
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
                "User-Agent": "Antigravity-Heatmap-Generator/1.0",
            },
        )
        try:
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode("utf-8"))
        except Exception as exc:
            print(f"[Error] GraphQL request via token failed: {exc}", file=sys.stderr)
            raise
    else:
        # Fall back to GitHub CLI
        try:
            res = subprocess.check_output(
                ["gh", "api", "graphql", "-F", f"userName={username}", "-f", f"query={query}"],
                text=True,
            )
            data = json.loads(res)
        except Exception as exc:
            print(f"[Error] GraphQL request via gh CLI failed: {exc}", file=sys.stderr)
            raise

    if "errors" in data:
        raise RuntimeError(f"GraphQL returned errors: {data['errors']}")

    calendar = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    return calendar


def get_palette_color(count: int) -> tuple[str, str]:
    """Returns (fill_color, stroke_color) for a given daily contribution count."""
    if count == 0:
        return "#161B22", "#1A3A4A"  # Dark background tile
    elif count <= 2:
        return "#0A3A60", "#0E4D7A"  # Level 1: Deep Navy Blue
    elif count <= 5:
        return "#0E6BA8", "#1E82C4"  # Level 2: Semiconductor Blue
    elif count <= 9:
        return "#00A3E0", "#00B8FC"  # Level 3: Vibrant Cyan
    else:
        return "#00D9FF", "#33E2FF"  # Level 4: Electric Cyan


def generate_svg(calendar: dict, username: str = "ALLENJOE-A") -> str:
    total = calendar["totalContributions"]
    weeks = calendar["weeks"]

    width = 880
    height = 205
    grid_x0 = 55
    grid_y0 = 66
    cell_size = 11.0
    gap = 4.0
    step = cell_size + gap

    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    # Month label positions
    month_labels = []
    last_month = None
    for w_idx, week in enumerate(weeks):
        days = week.get("contributionDays", [])
        if not days:
            continue
        first_day_date = days[0]["date"]
        dt = datetime.date.fromisoformat(first_day_date)
        if dt.month != last_month:
            last_month = dt.month
            month_labels.append((w_idx, months[dt.month - 1]))

    # Cells
    cells_svg = []
    for w_idx, week in enumerate(weeks):
        x = grid_x0 + w_idx * step
        for day in week.get("contributionDays", []):
            weekday = day["weekday"]
            y = grid_y0 + weekday * step
            count = day["contributionCount"]
            date_str = day["date"]
            fill, stroke = get_palette_color(count)
            plural = "s" if count != 1 else ""
            tip = f"{count} contribution{plural} on {date_str}"
            cells_svg.append(
                f'    <rect class="day-cell" x="{x:.1f}" y="{y:.1f}" width="{cell_size:.1f}" height="{cell_size:.1f}" '
                f'rx="2" fill="{fill}" stroke="{stroke}" stroke-width="0.5">\n'
                f'      <title>{tip}</title>\n'
                f'    </rect>'
            )

    # Month labels SVG
    month_svg = []
    for w_idx, name in month_labels:
        x = grid_x0 + w_idx * step
        if x > width - 40:
            continue
        month_svg.append(f'    <text class="axis-label" x="{x:.1f}" y="{grid_y0 - 9}">{name}</text>')

    cells_str = "\n".join(cells_svg)
    month_str = "\n".join(month_svg)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&amp;display=swap');
      text {{ font-family: 'JetBrains Mono', -apple-system, BlinkMacSystemFont, 'Segoe UI', monospace; }}
      .bg {{ fill: #0D1117; }}
      .card-border {{ fill: none; stroke: #1A3A4A; stroke-width: 1.2; rx: 6px; }}
      .title-main {{ font-size: 13px; font-weight: 700; fill: #00D9FF; letter-spacing: 1.5px; }}
      .title-stats {{ font-size: 12px; font-weight: 600; fill: #FFFFFF; text-anchor: end; }}
      .subtitle {{ font-size: 10px; fill: #AAB8C5; }}
      .axis-label {{ font-size: 9px; fill: #AAB8C5; }}
      .weekday-label {{ font-size: 9px; fill: #AAB8C5; text-anchor: end; }}
      .legend-text {{ font-size: 9px; fill: #AAB8C5; }}
      .disclaimer {{ font-size: 8.5px; fill: #5A7A8A; }}
      .day-cell {{ transition: all 0.15s ease; }}
      .day-cell:hover {{ stroke: #FFFFFF; stroke-width: 1.2; }}
    </style>
  </defs>

  <!-- Background and card border -->
  <rect class="bg" width="{width}" height="{height}" rx="6"/>
  <rect class="card-border" x="1" y="1" width="{width - 2}" height="{height - 2}" rx="6"/>

  <!-- Header Section -->
  <text class="title-main" x="20" y="28">ALLEN JOE A &#x2014; CONTRIBUTION HEATMAP</text>
  <text class="title-stats" x="{width - 20}" y="28">{total} Contributions in the Last Year</text>
  <text class="subtitle" x="20" y="44">Electric Cyan &amp; Semiconductor Blue Theme  &#x2022;  Live GitHub GraphQL Activity</text>

  <!-- Month Labels -->
{month_str}

  <!-- Weekday Labels -->
  <text class="weekday-label" x="{grid_x0 - 9}" y="{grid_y0 + 1 * step + 8.5}">Mon</text>
  <text class="weekday-label" x="{grid_x0 - 9}" y="{grid_y0 + 3 * step + 8.5}">Wed</text>
  <text class="weekday-label" x="{grid_x0 - 9}" y="{grid_y0 + 5 * step + 8.5}">Fri</text>

  <!-- Calendar Day Grid (53 Weeks x 7 Days) -->
  <g class="calendar-grid">
{cells_str}
  </g>

  <!-- Footer: Technical Disclaimer & Color Scale Legend -->
  <text class="disclaimer" x="20" y="{height - 13}">Custom SVG Heatmap powered by GitHub GraphQL API &#x2022; Auto-refreshed via GitHub Actions</text>

  <g class="legend" transform="translate({width - 150}, {height - 21})">
    <text class="legend-text" x="0" y="8" text-anchor="end">Less</text>
    <rect x="8" y="0" width="9" height="9" rx="1.5" fill="#161B22" stroke="#1A3A4A" stroke-width="0.5"><title>0 contributions</title></rect>
    <rect x="21" y="0" width="9" height="9" rx="1.5" fill="#0A3A60" stroke="#0E4D7A" stroke-width="0.5"><title>1-2 contributions</title></rect>
    <rect x="34" y="0" width="9" height="9" rx="1.5" fill="#0E6BA8" stroke="#1E82C4" stroke-width="0.5"><title>3-5 contributions</title></rect>
    <rect x="47" y="0" width="9" height="9" rx="1.5" fill="#00A3E0" stroke="#00B8FC" stroke-width="0.5"><title>6-9 contributions</title></rect>
    <rect x="60" y="0" width="9" height="9" rx="1.5" fill="#00D9FF" stroke="#33E2FF" stroke-width="0.5"><title>10+ contributions</title></rect>
    <text class="legend-text" x="76" y="8">More</text>
  </g>
</svg>
"""
    return svg


def main():
    parser = argparse.ArgumentParser(description="Generate Cyan/Blue Contribution Heatmap SVG")
    parser.add_argument("--username", default="ALLENJOE-A", help="GitHub username")
    parser.add_argument(
        "--output",
        default="assets/contribution-heatmap.svg",
        help="Output SVG file path",
    )
    args = parser.parse_args()

    print(f"Fetching contribution data for @{args.username}...")
    calendar = fetch_contributions(args.username)
    print(f"Retrieved {calendar['totalContributions']} total contributions across {len(calendar['weeks'])} weeks.")

    svg_content = generate_svg(calendar, args.username)

    # Ensure output directory exists
    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"Successfully generated heatmap at: {args.output}")


if __name__ == "__main__":
    main()
