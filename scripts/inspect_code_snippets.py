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

echo "=== 1. Active Plugins ===\\n";
$active_plugins = get_option('active_plugins', array());
foreach ($active_plugins as $p) {
    echo "- $p\\n";
}

echo "\\n=== 2. Check Snippets Tables & Options ===\\n";
$tables = $wpdb->get_results("SHOW TABLES LIKE '%snippet%'", ARRAY_N);
foreach ($tables as $t) {
    echo "Found table: " . $t[0] . "\\n";
    $rows = $wpdb->get_results("SELECT id, name, active, scope FROM " . $t[0] . " LIMIT 10", ARRAY_A);
    foreach ($rows as $r) {
        echo "  Snippet: [ID {$r['id']}] {$r['name']} | Active: {$r['active']} | Scope: {$r['scope']}\\n";
    }
}

$wpcode_tables = $wpdb->get_results("SHOW TABLES LIKE '%wpcode%'", ARRAY_N);
foreach ($wpcode_tables as $t) {
    echo "Found table: " . $t[0] . "\\n";
}

echo "\\n=== 3. Check wp_snippets content if any ===\\n";
if ($wpdb->get_var("SHOW TABLES LIKE '{$wpdb->prefix}snippets'")) {
    $snippets = $wpdb->get_results("SELECT id, name, code, active, scope FROM {$wpdb->prefix}snippets");
    foreach ($snippets as $s) {
        echo "Snippet ID: " . $s->id . " | Name: " . $s->name . " | Active: " . $s->active . "\\n";
        echo "Code preview:\\n" . substr($s->code, 0, 300) . "\\n---\\n";
    }
}

// Also check insert-headers-and-footers settings
$ihaf_head = get_option('ihaf_insert_header');
$ihaf_body = get_option('ihaf_insert_body');
$ihaf_footer = get_option('ihaf_insert_footer');
if ($ihaf_head || $ihaf_body || $ihaf_footer) {
    echo "\\n=== Insert Headers and Footers Settings ===\\n";
    echo "Header:\\n" . substr($ihaf_head, 0, 300) . "\\n";
    echo "Body:\\n" . substr($ihaf_body, 0, 300) . "\\n";
    echo "Footer:\\n" . substr($ihaf_footer, 0, 300) . "\\n";
}

echo "\\n=== 4. Check if wp_footer() hook has callbacks ===\\n";
global $wp_filter;
if (isset($wp_filter['wp_footer'])) {
    echo "wp_footer has " . count($wp_filter['wp_footer']->callbacks) . " priority levels.\\n";
} else {
    echo "wp_footer has NO callbacks registered.\\n";
}
"""
    ftp.storbinary("STOR public_html/wp/check_snippets.php", io.BytesIO(script_content.encode('utf-8')))
    
    ctx = ssl._create_unverified_context()
    try:
        req = urllib.request.Request("https://ebo.com.vn/wp/check_snippets.php", headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=15) as res:
            print(res.read().decode('utf-8'))
    except Exception as e:
        print("Error fetching:", e)
        
    try:
        ftp.delete("public_html/wp/check_snippets.php")
    except Exception:
        pass
        
    ftp.quit()

if __name__ == "__main__":
    main()
