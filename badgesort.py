import re
import hashlib

# Yes, sorting by hash makes no sense, but isn't it funny?
with open("README.md", "r+") as f:
    data = f.read()

    for s in re.finditer(r"<p>[\s\S]*?<\/p>", data):
        badges = re.findall(r"<img\b[^>]*\/>", s.group())
        badges.sort(key=lambda e: int(hashlib.sha256(e.encode()).hexdigest(), base=16))
        data = (
            data[: s.start()]
            + "<p>\n  "
            + "\n  ".join(badges)
            + "\n</p>"
            + data[s.end() :]
        )
    
    f.seek(0)
    f.write(data)
    f.truncate()