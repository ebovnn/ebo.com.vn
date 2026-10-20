# Nhật Ký Hoạt Động (Activity Log) - ebo.com.vn

## [2026-10-20 13:42:00] Tối Ưu Hóa Vị Trí Thẻ Google Tag Manager (GTM-KX8XTV38) Cho Tag Assistant

### 1. Phân Tích Sự Cố Kết Nối Trong Google Tag Manager Preview (Tag Assistant)
Khi kiểm tra bằng tính năng **Preview (Xem trước)** trong Google Tag Manager (`tagassistant.google.com`), Tag Assistant yêu cầu:
1. Thẻ script GTM phải được nạp **càng sớm càng tốt ngay đầu thẻ `<head>`** để kịp hoàn tất quá trình bắt tay (handshake postMessage) trước khi hết thời gian chờ (timeout). Trước đó thẻ nằm ở cuối `<head>` thông qua `wp_head()`.
2. Thẻ `<noscript>` phải nằm ngay đầu thẻ mở `<body>`.
3. Trình duyệt thực hiện Preview không được chặn script từ `googletagmanager.com` (ví dụ AdBlock, Brave Shields) hoặc chặn pop-up.

### 2. Các Hành Động Đã Khắc Phục
- **Chuyển thẻ GTM lên đầu thẻ `<head>`:** Đã đưa đoạn mã Google Tag Manager (`GTM-KX8XTV38`) trực tiếp lên dòng đầu tiên ngay sau thẻ mở `<head>` trong [public_html/libs/head.php](file:///Users/mac/ebo.com.vn/public_html/libs/head.php).
- **Chuyển thẻ noscript lên đầu thẻ `<body>`:** Đã đưa đoạn mã `<noscript>` trực tiếp lên dòng đầu tiên ngay sau thẻ mở `<body>` trong [public_html/libs/header.php](file:///Users/mac/ebo.com.vn/public_html/libs/header.php).
- **Dọn dẹp WPCode:** Làm sạch ô nhập Header & Body trong WPCode để đảm bảo không bị nạp trùng lặp mã GTM hai lần.
- **Đồng bộ mã nguồn local và máy chủ:** Cập nhật đồng bộ các tệp [libs/head.php](file:///Users/mac/ebo.com.vn/public_html/libs/head.php) và [libs/header.php](file:///Users/mac/ebo.com.vn/public_html/libs/header.php).
