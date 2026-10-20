import ftplib

FTP_HOST = "112.213.89.123"
FTP_USER = "ebocomvn6961"
FTP_PASS = "Ebo@16062015@2015"

def scan_dir(ftp, rel_path, depth=0, max_depth=3):
    if depth > max_depth:
        return
    try:
        ftp.cwd(rel_path)
    except Exception as e:
        return
        
    lines = []
    ftp.retrlines("LIST", lines.append)
    
    dirs = []
    for l in lines:
        parts = l.split(None, 8)
        if len(parts) < 9:
            continue
        perms, _, owner, group, size, m1, m2, m3, name = parts
        if name in [".", ".."]:
            continue
        if "petla" in name.lower() or "schedule" in name.lower():
            print(f"[MATCH] {rel_path}/{name} ({perms}, {size} bytes)")
        if perms.startswith("d") and name not in ["wp-admin", "wp-includes", "languages"]:
            dirs.append(name)
            
    for d in dirs:
        scan_dir(ftp, d, depth+1, max_depth)
        ftp.cwd("..")

def main():
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    print("=== Scanning public_html ===")
    scan_dir(ftp, "public_html", depth=0, max_depth=3)
    ftp.quit()

if __name__ == "__main__":
    main()
