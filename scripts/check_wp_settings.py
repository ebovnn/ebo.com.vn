import ftplib
import io
import urllib.request
import ssl

FTP_HOST = "112.213.89.123"
FTP_USER = "ebocomvn6961"
FTP_PASS = "Ebo@16062015@2015"

def main():
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    
    script_content = """<?php
require_once __DIR__ . '/wp-load.php';
header('Content-Type: text/plain');
echo "siteurl: " . get_option('siteurl') . "\\n";
echo "home: " . get_option('home') . "\\n";
echo "template: " . get_option('template') . "\\n";
echo "stylesheet: " . get_option('stylesheet') . "\\n";
"""
    ftp.storbinary("STOR public_html/wp/check_settings.php", io.BytesIO(script_content.encode('utf-8')))
    print("Uploaded check_settings.php")
    
    ctx = ssl._create_unverified_context()
    try:
        req = urllib.request.Request("https://ebo.com.vn/wp/check_settings.php", headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=10) as response:
            print("Response from check_settings.php:")
            print(response.read().decode('utf-8'))
    except Exception as e:
        print("Error fetching URL:", e)
        
    try:
        ftp.delete("public_html/wp/check_settings.php")
        print("Deleted check_settings.php safely.")
    except Exception as e:
        print("Error deleting:", e)
        
    ftp.quit()

if __name__ == "__main__":
    main()
