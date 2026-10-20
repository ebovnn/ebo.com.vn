import ftplib
import io

FTP_HOST = "112.213.89.123"
FTP_USER = "ebocomvn6961"
FTP_PASS = "Ebo@16062015@2015"

def read_remote_file(ftp, path):
    r = io.BytesIO()
    ftp.retrbinary(f"RETR {path}", r.write)
    return r.getvalue().decode('utf-8', errors='ignore')

def main():
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    
    print("=== Read public_html/wp/wp-config.php ===")
    try:
        content = read_remote_file(ftp, "public_html/wp/wp-config.php")
        # filter out passwords if printing, but keep db name/user/prefix
        for line in content.splitlines():
            if any(k in line for k in ['DB_NAME', 'DB_USER', 'DB_HOST', '$table_prefix', 'WP_HOME', 'WP_SITEURL']):
                print(line)
    except Exception as e:
        print("Error:", e)

    print("\n=== Read public_html/do_schedule.php ===")
    try:
        content = read_remote_file(ftp, "public_html/do_schedule.php")
        print(content[:1500])
    except Exception as e:
        print("Error:", e)

    print("\n=== Check public_html/wp/wp-content/themes/ ===")
    try:
        ftp.cwd("public_html/wp/wp-content/themes")
        items = []
        ftp.retrlines("LIST", items.append)
        for item in items:
            print(item)
    except Exception as e:
        print("Error:", e)

    print("\n=== Check public_html/wp/wp-content/plugins/ ===")
    try:
        ftp.cwd("../plugins")
        items = []
        ftp.retrlines("LIST", items.append)
        for item in items[:25]:
            print(item)
        if len(items) > 25:
            print(f"... and {len(items)-25} more plugins")
    except Exception as e:
        print("Error:", e)

    ftp.quit()

if __name__ == "__main__":
    main()
