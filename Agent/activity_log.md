# Nhật Ký Hoạt Động (Activity Log) - ebo.com.vn

## [2026-10-20 11:31:00] Khởi Tạo Dự Án & Kiểm Tra Cấu Trúc Domain

### 1. Kết Nối Git Repository
- Clone repository GitHub: `https://github.com/ebovnn/ebo.com.vn.git` vào thư mục làm việc `/Users/mac/ebo.com.vn`.
- Nhánh hiện tại: `main`.

### 2. Đọc & Xác Minh Cấu Trúc Domain Trên Hosting
- **Server FTP**: `112.213.89.123` (Tài khoản cPanel: `ebocomvn6961`).
- **Xác minh Domain chính xác cho dự án**:
  - Tên miền chính: **`ebo.com.vn`** trỏ trực tiếp vào thư mục **`public_html/`** (đường dẫn máy chủ: `/home/ebocomvn6961/public_html`).
  - Thư mục cấu hình cPanel `etc/ebo.com.vn` xác nhận `ebo.com.vn` là domain chính của tài khoản này.
  - Phân hệ WordPress nằm tại thư mục con: `public_html/wp/` (Cơ sở dữ liệu: `ebocomvn6961_ebocomvn`, tiền tố bảng: `wp_`).
  - Trang chính `public_html/` là kiến trúc PHP tùy chỉnh kết hợp với WordPress (`index_html.php`, `libs/`, `assets/`, `app_config.php`).
  - Các domain khác trên hosting là các addon domains riêng biệt: `demo.ebo.com.vn`, `petla.vn`, `konavis.vn`, `laptopvietnhat.vn`, `luatsuhoangviet.vn`, `ngocanhnailslashes.com`, `noithatnhasaigon.com`, `cokhichuyennghiep.com`, `tubepsaigon.vn`.

### 3. Tệp Scripts Đã Tạo
- `scripts/check_ftp.py`: Kiểm tra kết nối FTP đến hosting.
- `scripts/check_domains.py`: Kiểm tra danh sách thư mục, mapping domain và cấu hình Apache.
- `scripts/inspect_project.py`: Đọc nội dung `index.php`, `app_config.php` và danh mục `wp/`.
- `scripts/inspect_ebo_details.py`: Kiểm tra chi tiết `index_html.php`, cấu hình WordPress `wp-config.php`, và thư mục con `demo.ebo.com.vn`.
