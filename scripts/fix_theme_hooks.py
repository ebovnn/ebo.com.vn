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
    
    # 1. Update libs/header.php
    print("Reading public_html/libs/header.php...")
    r = io.BytesIO()
    ftp.retrbinary("RETR public_html/libs/header.php", r.write)
    header_content = r.getvalue().decode('utf-8', errors='ignore')
    
    if "wp_body_open" not in header_content:
        new_header = "<?php if (function_exists('wp_body_open')) { wp_body_open(); } ?>\n" + header_content
        ftp.storbinary("STOR public_html/libs/header.php", io.BytesIO(new_header.encode('utf-8')))
        print("Successfully added wp_body_open() to public_html/libs/header.php")
    else:
        print("wp_body_open already in libs/header.php")
        
    # 2. Update libs/footer.php
    print("Reading public_html/libs/footer.php...")
    r2 = io.BytesIO()
    ftp.retrbinary("RETR public_html/libs/footer.php", r2.write)
    footer_content = r2.getvalue().decode('utf-8', errors='ignore')
    
    if "wp_footer" not in footer_content:
        new_footer = footer_content.rstrip() + "\n\n<?php if (function_exists('wp_footer')) { wp_footer(); } ?>\n"
        ftp.storbinary("STOR public_html/libs/footer.php", io.BytesIO(new_footer.encode('utf-8')))
        print("Successfully added wp_footer() to public_html/libs/footer.php")
    else:
        print("wp_footer already in libs/footer.php")
        
    ftp.quit()
    
    # 3. Test HTTP Response
    ctx = ssl._create_unverified_context()
    req = urllib.request.Request("https://ebo.com.vn/", headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, context=ctx, timeout=15) as res:
        html = res.read().decode('utf-8')
        print(f"\nResponse status: {res.status}")
        print("Found GTM in header:", "googletagmanager.com/gtm.js?id=GTM-KX8XTV38" in html)
        print("Found GTM noscript in body:", "googletagmanager.com/ns.html?id=GTM-KX8XTV38" in html)
        print("Found wp_footer scripts:", "wp-includes" in html or "common.js" in html)

if __name__ == "__main__":
    main()
