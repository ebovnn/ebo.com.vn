import ftplib
import io
import urllib.request
import ssl

FTP_HOST = "112.213.89.123"
FTP_USER = "ebocomvn6961"
FTP_PASS = "Ebo@16062015@2015"

CLEAN_HTACCESS = """# BEGIN WordPress
# Các nội dung nằm giữa "BEGIN WordPress" và "END WordPress" được tạo ra tự động, và chỉ nên được thay đổi thông qua các filter của WordPress. Mọi thay đổi tới thành phần này có thể sẽ bị mất và ghi đè.
<IfModule mod_rewrite.c>
RewriteEngine On
RewriteRule .* - [E=HTTP_AUTHORIZATION:%{HTTP:Authorization}]
RewriteBase /
RewriteRule ^index\.php$ - [L]
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule . /index.php [L]
</IfModule>
# END WordPress
"""

def main():
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    
    # 1. Backup existing .htaccess
    try:
        ftp.rename("public_html/.htaccess", "public_html/.htaccess.bak_geo")
        print("Backed up .htaccess to .htaccess.bak_geo")
    except Exception as e:
        print("Backup warning:", e)
        
    # 2. Upload clean WordPress .htaccess
    ftp.storbinary("STOR public_html/.htaccess", io.BytesIO(CLEAN_HTACCESS.encode('utf-8')))
    print("Uploaded clean WordPress .htaccess (no foreign IP deny)")
    ftp.quit()

if __name__ == "__main__":
    main()
