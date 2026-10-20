import ftplib
import io

FTP_HOST = "112.213.89.123"
FTP_USER = "ebocomvn6961"
FTP_PASS = "Ebo@16062015@2015"

def main():
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    
    files = [
        "public_html/wp/wp-content/mu-plugins/popup-notice-simple-x.php",
        "public_html/wp/wp-content/mu-plugins/reading-time-estimate.php",
        "public_html/wp/wp-content/mu-plugins/spam-comment-filter-7.php"
    ]
    
    for f in files:
        print(f"Checking {f}...")
        try:
            ftp.sendcmd(f"SITE CHMOD 644 {f}")
            print(f"CHMOD 644 successful on {f}")
        except Exception as e:
            print(f"CHMOD failed: {e}")
            
    print("\nListing mu-plugins again:")
    ftp.cwd("public_html/wp/wp-content/mu-plugins")
    ftp.dir()
    
    # Read first 500 bytes of each to see what they are
    for fname in ["popup-notice-simple-x.php", "reading-time-estimate.php", "spam-comment-filter-7.php"]:
        try:
            r = io.BytesIO()
            ftp.retrbinary(f"RETR {fname}", r.write)
            print(f"\n--- {fname} Header ---")
            print(r.getvalue()[:300].decode('utf-8', errors='ignore'))
        except Exception as e:
            print(f"Error reading {fname}: {e}")
            
    ftp.quit()

if __name__ == "__main__":
    main()
