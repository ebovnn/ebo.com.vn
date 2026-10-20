import ftplib
import sys

FTP_HOST = "112.213.89.123"
FTP_USER = "ebocomvn6961"
FTP_PASS = "Ebo@16062015@2015"

def check_ftp():
    try:
        print(f"Connecting to FTP {FTP_HOST}...")
        ftp = ftplib.FTP(FTP_HOST, timeout=15)
        print("Connected. Logging in...")
        ftp.login(FTP_USER, FTP_PASS)
        print("Login successful!")
        
        print("\n--- Current Directory Listing ---")
        ftp.dir()
        
        print("\nChecking public_html...")
        try:
            ftp.cwd("public_html")
            print("Entered public_html:")
            items = []
            ftp.retrlines("LIST", items.append)
            for item in items[:30]:
                print(item)
            if len(items) > 30:
                print(f"... and {len(items) - 30} more items.")
        except Exception as e:
            print(f"Failed to cwd to public_html: {e}")
            
        ftp.quit()
        print("\nFTP connection closed safely.")
    except Exception as e:
        print(f"FTP Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    check_ftp()
