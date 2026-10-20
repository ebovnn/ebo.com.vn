import ftplib

FTP_HOST = "112.213.89.123"
FTP_USER = "ebocomvn6961"
FTP_PASS = "Ebo@16062015@2015"

def main():
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    
    print("=== Listing public_html/wp/wp-content/mu-plugins ===")
    try:
        ftp.cwd("public_html/wp/wp-content/mu-plugins")
        items = []
        ftp.retrlines("LIST", items.append)
        for i in items:
            print(i)
    except Exception as e:
        print("Error:", e)
        
    print("\n=== Listing public_html/wp/wp-content/plugins ===")
    try:
        ftp.cwd("../plugins")
        items = []
        ftp.retrlines("LIST", items.append)
        for i in items:
            print(i)
    except Exception as e:
        print("Error:", e)

    ftp.quit()

if __name__ == "__main__":
    main()
