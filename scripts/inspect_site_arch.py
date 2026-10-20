import ftplib
import io
import zipfile

FTP_HOST = "112.213.89.123"
FTP_USER = "ebocomvn6961"
FTP_PASS = "Ebo@16062015@2015"

def read_file(ftp, path, max_len=10000):
    try:
        r = io.BytesIO()
        ftp.retrbinary(f"RETR {path}", r.write)
        return r.getvalue().decode('utf-8', errors='ignore')[:max_len]
    except Exception as e:
        return f"Error reading {path}: {e}"

def main():
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    
    print("=== Listing public_html/libs ===")
    try:
        ftp.cwd("public_html/libs")
        items = []
        ftp.retrlines("LIST", items.append)
        for i in items:
            print(i)
        ftp.cwd("../..")
    except Exception as e:
        print("Error in libs:", e)

    print("\n=== Listing public_html/ve-chung-toi ===")
    try:
        ftp.cwd("public_html/ve-chung-toi")
        items = []
        ftp.retrlines("LIST", items.append)
        for i in items:
            print(i)
        ftp.cwd("../..")
    except Exception as e:
        print("Error in ve-chung-toi:", e)

    print("\n=== Check public_html/libs/head.php ===")
    print(read_file(ftp, "public_html/libs/head.php", 1000))

    print("\n=== Check public_html/wp/index.php ===")
    print(read_file(ftp, "public_html/wp/index.php", 1000))

    print("\n=== Check public_html/wp/wp-blog-header.php ===")
    print(read_file(ftp, "public_html/wp/wp-blog-header.php", 1000))

    ftp.quit()

if __name__ == "__main__":
    main()
