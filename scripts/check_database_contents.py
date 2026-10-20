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

// Check category
$cat = get_term_by('slug', 'blog-thoi-trang', 'category');
if ($cat) {
    echo "Found category: " . $cat->name . " (ID: " . $cat->term_id . ")\\n";
} else {
    echo "Category 'blog-thoi-trang' NOT found.\\n";
}

// Check recent posts
$args = array(
    'post_type' => array('post', 'blog', 'service', 'project'),
    'posts_per_page' => 15,
    'post_status' => 'any',
    'orderby' => 'ID',
    'order' => 'DESC'
);
$query = new WP_Query($args);
echo "\\nLast 15 posts in DB:\\n";
while ($query->have_posts()) {
    $query->the_post();
    echo get_the_ID() . " | " . get_post_type() . " | " . get_post_status() . " | " . get_the_date('Y-m-d H:i') . " | " . get_the_title() . "\\n";
}
wp_reset_postdata();
"""
    ftp.storbinary("STOR public_html/wp/check_db.php", io.BytesIO(script_content.encode('utf-8')))
    
    ctx = ssl._create_unverified_context()
    try:
        req = urllib.request.Request("https://ebo.com.vn/wp/check_db.php", headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=10) as response:
            print(response.read().decode('utf-8'))
    except Exception as e:
        print("Error fetching URL:", e)
        
    try:
        ftp.delete("public_html/wp/check_db.php")
    except Exception:
        pass
        
    ftp.quit()

if __name__ == "__main__":
    main()
