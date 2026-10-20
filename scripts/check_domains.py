import ftplib
import io

FTP_HOST = "112.213.89.123"
FTP_USER = "ebocomvn6961"
FTP_PASS = "Ebo@16062015@2015"

def read_file(ftp, path):
    try:
        r = io.BytesIO()
        ftp.retrbinary(f"RETR {path}", r.write)
        return r.getvalue().decode('utf-8', errors='ignore')
    except Exception as e:
        return f"Error: {e}"

def main():
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    
    print("=== Root directories ===")
    root_items = []
    ftp.retrlines("LIST", root_items.append)
    for item in root_items:
        print(item)
        
    print("\n=== Check etc directory ===")
    try:
        ftp.cwd("etc")
        etc_items = []
        ftp.retrlines("LIST", etc_items.append)
        for item in etc_items:
            print(item)
        ftp.cwd("..")
    except Exception as e:
        print("Cannot cwd to etc:", e)

    print("\n=== Check access-logs ===")
    try:
        ftp.cwd("access-logs")
        logs = []
        ftp.retrlines("LIST", logs.append)
        for l in logs:
            print(l)
        ftp.cwd("..")
    except Exception as e:
        print("Cannot cwd to access-logs:", e)
        
    print("\n=== Check public_html .htaccess ===")
    ht = read_file(ftp, "public_html/.htaccess")
    for line in ht.splitlines()[:30]:
        print(line)
        
    ftp.quit()

if __name__ == "__main__":
    main()
