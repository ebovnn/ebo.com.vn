# Nhật Ký Hoạt Động (Activity Log) - ebo.com.vn

## [2026-10-20 11:58:00] Điều Tra Sự Cố Thẻ Google (GTM / Code Snippets) & Bổ Sung Hook wp_body_open, wp_footer

### 1. Phân Tích Nguyên Nhân Thẻ Google Chưa Được Nhận
1. **Sự cố sập trang chủ trước đó:**
   - File `public_html/index.php` trước khi fix bị thoát bằng lệnh `exit;`, dẫn đến bot của Google (Google Tag Assistant / Search Console / Analytics) quét trang chủ không thấy bất kỳ thẻ HTML nào.
2. **Theme thiếu hook `wp_body_open()` và `wp_footer()`:**
   - Plugin chèn mã trên web hiện tại là **WPCode (Insert Headers and Footers)** chứa thẻ Google Tag Manager:
     - Header: Script Google Tag Manager container `GTM-KX8XTV38`.
     - Body: `<noscript>` iframe Google Tag Manager.
   - Tuy nhiên, theme `wp-templ` trước đây thiếu hoàn toàn hook `wp_body_open()` sau thẻ `<body>` và thiếu `wp_footer()` trước `</body>`. Do đó, phần mã `noscript` trong Body hoàn toàn không được in ra trang web, dẫn đến việc Google báo thẻ chưa được gắn chuẩn hoặc thiếu phần body.
3. **Phân biệt plugin Code Snippets và WPCode:**
   - Plugin "Code Snippets" cũ hiện không hoạt động (các snippet cũ đều tắt). Plugin đang quản trị mã Google thực tế là **WPCode (Insert Headers and Footers)**.
4. **Cấu hình Google Analytics trong Google Tag Manager:**
   - Website đang cài đặt container `GTM-KX8XTV38`. Nếu mục tiêu là kết nối Google Analytics 4 (GA4) hoặc Google Ads, người dùng cần vào giao diện `tagmanager.google.com` của container này tạo thẻ GA4/Google Tag và bấm **Publish (Xuất bản)** để container kích hoạt truyền dữ liệu.

### 2. Các Hành Động Đã Khắc Phục
- **Bổ sung `wp_body_open()` vào [public_html/libs/header.php](file:///Users/mac/ebo.com.vn/public_html/libs/header.php):** Tự động gọi hàm hook ngay đầu file header (ngay sau khi thẻ `<body>` mở trên mọi trang).
- **Bổ sung `wp_footer()` vào [public_html/libs/footer.php](file:///Users/mac/ebo.com.vn/public_html/libs/footer.php):** Cho phép các script của plugin và mã nhúng footer thực thi trước khi đóng thẻ `</body>`.
- **Cập nhật đồng bộ lên FTP hosting và mã nguồn local.**
- **Kiểm tra trực tiếp kết quả tải trang:** Cả thẻ script trong Header và thẻ iframe noscript trong Body của `GTM-KX8XTV38` hiện đã hiển thị đầy đủ, chính xác trong mã nguồn HTML trang web `https://ebo.com.vn/`.
