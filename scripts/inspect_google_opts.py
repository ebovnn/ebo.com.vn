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
header('Content-Type: text/plain; charset=utf-8');

global $wpdb;

echo "=== Options with google / gtm / analytics ===\\n";
$rows = $wpdb->get_results("SELECT option_name, option_value FROM {$wpdb->options} WHERE option_name LIKE '%google%' OR option_name LIKE '%gtm%' OR option_name LIKE '%tag%' OR option_name LIKE '%analytic%' OR option_name LIKE '%ihaf%' OR option_name LIKE '%snippet%'", ARRAY_A);

foreach ($rows as $r) {
    $val = substr($r['option_value'], 0, 150);
    echo "Option: " . $r['option_name'] . " => " . $val . "\\n";
}

echo "\\n=== Check Rank Math webmaster tools ===\\n";
$rm = get_option('rank_math_options_general');
if ($rm && isset($rm['google_verify'])) {
    echo "Rank Math google_verify: " . $rm['google_verify'] . "\\n";
}
"""
    ftp.storbinary("STOR public_html/wp/check_google_opts.php", io.BytesIO(script_content.encode('utf-8')))
    
    ctx = ssl._create_unverified_context()
    try:
        req = urllib.request.Request("https://ebo.com.vn/wp/check_google_opts.php", headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=15) as res:
            print(res.read().decode('utf-8'))
    except Exception as e:
        print("Error:", e)
        
    ftp.delete("public_html/wp/check_google_opts.php")
    ftp.quit()

if __name__ == "__main__":
    main()
