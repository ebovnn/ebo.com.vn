# Nhật Ký Hoạt Động (Activity Log) - ebo.com.vn

## [2026-10-20 11:44:00] Điều Tra, Phát Hiện Và Khắc Phục Triệt Để Các Lỗi Trên Website ebo.com.vn

### 1. Nguyên Nhân Gốc Rễ Của Sự Cố (Root Cause Analysis)
Qua rà soát và kiểm tra nhật ký lỗi, hệ thống phát hiện website `ebo.com.vn` gặp nhiều lỗi nghiêm trọng do việc can thiệp nhầm lẫn giữa dự án `petla.vn` và `ebo.com.vn` (cùng lưu trữ trên tài khoản hosting `ebocomvn6961`):

1. **Lỗi tê liệt hoàn toàn Trang Chủ (`/index.php`):**
   - File `/home/ebocomvn6961/public_html/index.php` bị ghi đè bởi một đoạn mã debug 12 dòng kiểm tra file `generated_8_posts.json` và kết thúc bằng `exit;`.
   - Hậu quả: Mọi lượt truy cập `https://ebo.com.vn/` đều bị ngắt và in ra văn bản debug thay vì hiển thị giao diện website.
2. **Lỗi HTTP 500 tại Trang "Về chúng tôi" (`/ve-chung-toi/`):**
   - `ve-chung-toi/index.php` là thư mục vật lý nên Apache truy cập trực tiếp file này thay vì rewrite qua WordPress. Tuy nhiên file này chỉ include `app_config.php` và `libs/head.php` mà không nạp WordPress core (`wp-load.php`).
   - `libs/head.php` gọi các hàm WordPress (`is_front_page()`, `get_bloginfo()`, `wp_head()`) dẫn đến `PHP Fatal error: Uncaught Error: Call to undefined function is_front_page()`.
3. **Lỗi cảnh báo quyền truy cập (Permission Denied) liên tục trên toàn bộ website:**
   - Trong `public_html/wp/wp-content/mu-plugins/`, có 3 file (`popup-notice-simple-x.php`, `reading-time-estimate.php`, `spam-comment-filter-7.php`) bị set quyền `0000` (`----------`).
   - WordPress tự động load tất cả file PHP trong `mu-plugins/`, dẫn đến mỗi lượt truy cập trang web đều sinh ra 3 cảnh báo lỗi `Permission denied in wp-settings.php on line 456`, làm phình to file `error_log` và ảnh hưởng hiệu năng.
4. **Ô nhiễm dữ liệu & SEO của Petla trên ebo.com.vn:**
   - File `public_html/wp/wp-content/mu-plugins/petla-seo-optimization.php` tiêm Schema túi xách nữ Petla, dns-prefetch `petla.vn` vào đầu trang EBO.
   - Các file thừa: `public_html/do_schedule.php`, `public_html/wp/petla_inspect.php`.
   - Trong CSDL WordPress của EBO bị chèn nhầm bài viết ID 668 ("Cách chọn túi xách nữ...") và chuyên mục ID 10 ("Blog - Thời trang").

---

### 2. Các Biện Pháp Xử Lý Đã Thực Hiện

1. **Khôi phục File gốc `public_html/index.php`:**
   - Sao lưu file debug thành `index.php.bak_debug`.
   - Khôi phục file chuẩn WordPress Document Root:
     ```php
     define( 'WP_USE_THEMES', true );
     require __DIR__ . '/wp/wp-blog-header.php';
     ```
2. **Khắc phục lỗi trang `ve-chung-toi/index.php` & `libs/head.php`:**
   - Cập nhật `ve-chung-toi/index.php` tự động nạp `wp-load.php` nếu WordPress chưa khởi chạy.
   - Tối ưu hóa `libs/head.php`: Tự động nạp `wp-load.php` khi cần, kiểm tra an toàn `function_exists()` cho tất cả hàm SEO, loại bỏ cặp thẻ thừa `<body></body></html>` ở cuối file head.
3. **Dọn dẹp triệt để ô nhiễm Petla & lỗi quyền mu-plugins:**
   - Xóa bỏ file tiêm Schema sai: `wp-content/mu-plugins/petla-seo-optimization.php`.
   - Xóa bỏ các kịch bản thừa: `public_html/do_schedule.php`, `public_html/wp/petla_inspect.php`.
   - Xóa bỏ 3 file quyền `0000` trong `mu-plugins/` (`popup-notice-simple-x.php`, `reading-time-estimate.php`, `spam-comment-filter-7.php`) vì các plugin này đã có bản cài đặt chuẩn trong thư mục `wp-content/plugins/`.
   - Dọn sạch CSDL: Xóa bài viết rác ID 668 (túi xách) và chuyên mục ID 10 (thời trang).
4. **Đồng bộ mã nguồn về local:**
   - Đã tạo các bản đồng bộ tại local: `public_html/index.php`, `public_html/libs/head.php`, `public_html/ve-chung-toi/index.php`.

---

### 3. Kết Quả Kiểm Tra Sau Khắc Phục
Tất cả các trang chính trên `https://ebo.com.vn/` đã được kiểm tra và trả về mã phản hồi HTTP 200 OK:
- `https://ebo.com.vn/` => **200 OK** (Nội dung đầy đủ 63.9 KB, hiển thị giao diện EBO chuẩn)
- `https://ebo.com.vn/ve-chung-toi/` => **200 OK** (Đã hết lỗi 500 Fatal error, hiển thị 43 KB)
- `https://ebo.com.vn/blog/` => **200 OK** (36.1 KB)
- `https://ebo.com.vn/dich-vu/` => **200 OK** (46.6 KB)
- `https://ebo.com.vn/dao-tao/` => **200 OK** (26.4 KB)
- `https://ebo.com.vn/tuyen-dung/` => **200 OK** (23.5 KB)
- `https://ebo.com.vn/blog/doanh-nghiep-nho-co-can-marketing-tong-the/` => **200 OK** (55.9 KB)
- `https://ebo.com.vn/wp/wp-login.php` => **200 OK**
- Không còn ghi nhận bất kỳ cảnh báo `PHP Warning` hay `Fatal error` nào trong các tệp `error_log`.
