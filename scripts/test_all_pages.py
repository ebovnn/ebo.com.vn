import urllib.request
import ssl

ctx = ssl._create_unverified_context()

urls = [
    "https://ebo.com.vn/",
    "https://ebo.com.vn/ve-chung-toi/",
    "https://ebo.com.vn/blog/",
    "https://ebo.com.vn/dich-vu/",
    "https://ebo.com.vn/dao-tao/",
    "https://ebo.com.vn/du-an/",
    "https://ebo.com.vn/tuyen-dung/",
    "https://ebo.com.vn/thiet-ke-website-chuan-seo-can-dap-ung-nhung-tieu-chi-nao/",
    "https://ebo.com.vn/wp/wp-login.php"
]

print("=== Testing all main URLs on ebo.com.vn ===")
for u in urls:
    try:
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=15) as res:
            content = res.read()
            print(f"[OK 200] {u} (Length: {len(content)} bytes)")
    except urllib.error.HTTPError as e:
        print(f"[HTTP {e.code}] {u}: {e.reason}")
    except Exception as e:
        print(f"[ERROR] {u}: {e}")
