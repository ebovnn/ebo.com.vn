import ftplib
import io

FTP_HOST = "112.213.89.123"
FTP_USER = "ebocomvn6961"
FTP_PASS = "Ebo@16062015@2015"

def read_file(ftp, path, max_len=2000):
    try:
        r = io.BytesIO()
        ftp.retrbinary(f"RETR {path}", r.write)
        data = r.getvalue().decode('utf-8', errors='ignore')
        return data[:max_len]
    except Exception as e:
        return f"Error: {e}"

def main():
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    
    print("=== public_html/index_html.php (head) ===")
    print(read_file(ftp, "public_html/index_html.php", 1000))
    
    print("\n=== public_html/wp/wp-config.php (head) ===")
    wp_conf = read_file(ftp, "public_html/wp/wp-config.php", 3000)
    for line in wp_conf.splitlines():
        if any(k in line for k in ['DB_NAME', 'DB_USER', 'DB_HOST', '$table_prefix', 'WP_HOME', 'WP_SITEURL']):
            print(line)

    print("\n=== public_html/demo.ebo.com.vn check ===")
    try:
        ftp.cwd("demo.ebo.com.vn")
        items = []
        ftp.retrlines("LIST", items.append)
        for item in items[:15]:
            print(item)
        ftp.cwd("..")
    except Exception as e:
        print("Error demo.ebo.com.vn:", e)

    ftp.quit()

if __name__ == "__main__":
    main()
