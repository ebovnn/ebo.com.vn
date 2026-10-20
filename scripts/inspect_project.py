import ftplib
import io

FTP_HOST = "112.213.89.123"
FTP_USER = "ebocomvn6961"
FTP_PASS = "Ebo@16062015@2015"

def read_remote_file(ftp, filename):
    r = io.BytesIO()
    ftp.retrbinary(f"RETR {filename}", r.write)
    return r.getvalue().decode('utf-8', errors='ignore')

def main():
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.cwd("public_html")
    
    print("=== Read public_html/index.php ===")
    try:
        content = read_remote_file(ftp, "index.php")
        print(content[:1000])
    except Exception as e:
        print("Error reading index.php:", e)

    print("\n=== Read public_html/app_config.php ===")
    try:
        content = read_remote_file(ftp, "app_config.php")
        print(content[:1000])
    except Exception as e:
        print("Error reading app_config.php:", e)

    print("\n=== Listing public_html/wp ===")
    try:
        ftp.cwd("wp")
        items = []
        ftp.retrlines("LIST", items.append)
        for item in items[:30]:
            print(item)
        if len(items) > 30:
            print(f"... and {len(items)-30} more items")
        ftp.cwd("..")
    except Exception as e:
        print("Error cwd wp:", e)
        
    ftp.quit()

if __name__ == "__main__":
    main()
