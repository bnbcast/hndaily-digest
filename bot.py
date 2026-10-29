import json, urllib.request, datetime, pathlib

today = datetime.date.today()

def get(url):
    with urllib.request.urlopen(url, timeout=20) as r:
        return json.load(r)

base = "https://hacker-news.firebaseio.com/v0"
ids = get(f"{base}/topstories.json")[:5]
items = [get(f"{base}/item/{i}.json") for i in ids]

path = pathlib.Path(f"digest/{today:%Y/%m}/{today}.md")
path.parent.mkdir(parents=True, exist_ok=True)

lines = [f"# {today}", ""]
for it in items:
    link = it.get("url") or f"https://news.ycombinator.com/item?id={it['id']}"
    lines.append(f"- [{it['title']}]({link}) ({it.get('score', 0)} points)")
path.write_text("\n".join(lines) + "\n")

pathlib.Path("msg.txt").write_text(f"digest: {today} - {items[0]['title'][:60]}")
