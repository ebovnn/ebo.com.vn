import ftplib
import io
import urllib.request
import ssl

FTP_HOST = "112.213.89.123"
FTP_USER = "ebocomvn6961"
FTP_PASS = "Ebo@16062015@2015"

WP_ROOT_INDEX = """<?php
/**
 * Front to the WordPress application. This file doesn't do anything, but loads
 * wp-blog-header.php which does and tells WordPress to load the theme.
 *
 * @package WordPress
 */

/**
 * Tells WordPress to load the WordPress theme and output it.
 *
 * @var bool
 */
define( 'WP_USE_THEMES', true );

/** Loads the WordPress Environment and Template */
require __DIR__ . '/wp/wp-blog-header.php';
"""

def fix_step_1_restore_index(ftp):
    print("\n--- STEP 1: Restore public_html/index.php ---")
    # Backup current index.php
    try:
        ftp.rename("public_html/index.php", "public_html/index.php.bak_debug")
        print("Backed up public_html/index.php to index.php.bak_debug")
    except Exception as e:
        print("Backup warning:", e)
        
    ftp.storbinary("STOR public_html/index.php", io.BytesIO(WP_ROOT_INDEX.encode('utf-8')))
    print("Uploaded clean WordPress root index.php")

def fix_step_2_remove_misplaced_petla_files(ftp):
    print("\n--- STEP 2: Remove misplaced Petla files ---")
    files_to_remove = [
        "public_html/do_schedule.php",
        "public_html/wp/petla_inspect.php",
        "public_html/wp/wp-content/mu-plugins/petla-seo-optimization.php"
    ]
    for f in files_to_remove:
        try:
            ftp.delete(f)
            print(f"Successfully deleted {f}")
        except Exception as e:
            print(f"Could not delete {f}: {e}")

def fix_step_3_clean_mu_plugins_and_db(ftp):
    print("\n--- STEP 3: Clean 0000 mu-plugins & Petla data from DB via PHP ---")
    cleaner_php = """<?php
require_once __DIR__ . '/wp-load.php';
header('Content-Type: text/plain; charset=utf-8');

$mu_dir = WP_CONTENT_DIR . '/mu-plugins';
$files = array(
    'popup-notice-simple-x.php',
    'reading-time-estimate.php',
    'spam-comment-filter-7.php'
);

foreach ($files as $file) {
    $filepath = $mu_dir . '/' . $file;
    if (file_exists($filepath)) {
        @chmod($filepath, 0666);
        if (@unlink($filepath)) {
            echo "Successfully unlinked $file\\n";
        } else {
            echo "Failed to unlink $file (will try shell/exec if permitted)\\n";
        }
    } else {
        echo "$file not found\\n";
    }
}

// Clean Petla post 668 if it exists and is túi xách
$post_668 = get_post(668);
if ($post_668 && strpos($post_668->post_title, 'túi xách') !== false) {
    wp_delete_post(668, true);
    echo "Deleted Petla post ID 668\\n";
} else {
    echo "Post 668 is not Petla or not found\\n";
}

// Clean Petla category 10
$cat_10 = get_term(10, 'category');
if ($cat_10 && $cat_10->slug === 'blog-thoi-trang') {
    wp_delete_term(10, 'category');
    echo "Deleted Petla category 10 (blog-thoi-trang)\\n";
} else {
    echo "Category 10 not found or not blog-thoi-trang\\n";
}
"""
    ftp.storbinary("STOR public_html/wp/run_cleanup.php", io.BytesIO(cleaner_php.encode('utf-8')))
    print("Uploaded run_cleanup.php")
    
    ctx = ssl._create_unverified_context()
    try:
        req = urllib.request.Request("https://ebo.com.vn/wp/run_cleanup.php", headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=15) as response:
            print("Cleanup script output:\n" + response.read().decode('utf-8'))
    except Exception as e:
        print("Error executing cleanup script:", e)
        
    try:
        ftp.delete("public_html/wp/run_cleanup.php")
        print("Deleted run_cleanup.php")
    except Exception:
        pass

def main():
    ftp = ftplib.FTP(FTP_HOST, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    
    fix_step_1_restore_index(ftp)
    fix_step_2_remove_misplaced_petla_files(ftp)
    fix_step_3_clean_mu_plugins_and_db(ftp)
    
    ftp.quit()
    print("\nAll fix steps executed!")

if __name__ == "__main__":
    main()
