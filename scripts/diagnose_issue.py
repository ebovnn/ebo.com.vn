import ftplib
import io
import re

FTP_HOST = "112.213.89.123"
FTP_USER = "ebocomvn6961"
FTP_PASS = "Ebo@16062015@2015"

def read_file(ftp, path, max_len=10000):
    try:
        r = io.BytesIO()
        ftp.retrbinary(f"RETR {path}", r.write)
        return r.getvalue().decode('utf-8', errors='ignore')
    except Exception as e:
        return f"Error reading {path}: {e}"

def read_file_tail(ftp, path, num_bytes=15000):
    try:
        size = ftp.size(path)
        r = io.BytesIO()
        rest_pos = max(0, size - num_bytes) if size else 0
        ftp.retrbinary(f"RETR {path}", r.write, rest=rest_pos)
        return r.getvalue().decode('utf-8', errors='ignore')
    except Exception as e:
        return f"Error reading tail of {path}: {e}"

def main():
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    
    print("=== 1. FULL public_html/index.php ===")
    print(read_file(ftp, "public_html/index.php"))
    
    print("\n=== 2. Tail of public_html/error_log ===")
    tail = read_file_tail(ftp, "public_html/error_log", 10000)
    lines = tail.splitlines()
    for l in lines[-30:]:
        print(l)

    print("\n=== 3. Tail of public_html/wp/error_log ===")
    tail_wp = read_file_tail(ftp, "public_html/wp/error_log", 10000)
    lines_wp = tail_wp.splitlines()
    for l in lines_wp[-30:]:
        print(l)

    print("\n=== 4. Check public_html/do_schedule.php ===")
    print(read_file(ftp, "public_html/do_schedule.php", 3000))

    ftp.quit()

if __name__ == "__main__":
    main()
