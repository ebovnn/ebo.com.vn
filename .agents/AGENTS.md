# Agent Rules & Guidelines for ebo.com.vn

1. **Lưu Tệp Mã Nguồn / Kịch Bản Xử Lý (Scripts)**:
   - Khi viết script/code để xử lý công việc (ví dụ các tệp Python `.py`, Node.js `.js`, PHP `.php` kết nối FTP, gọi API, sửa bài viết, upload mu-plugin, cập nhật CSDL), Agent **bắt buộc phải lưu tệp mã nguồn đó lại trong dự án** (ví dụ thư mục `scratch/` hoặc thư mục làm việc tương ứng).

2. **Kết Nối FTP & Cập Nhật Trực Tiếp Trên Máy Chủ**:
   - Khi chỉnh sửa, tạo mới hoặc fix code cho dự án, Agent trực tiếp kết nối qua FTP để cập nhật/đồng bộ tệp trên máy chủ hosting (`public_html/`) và cập nhật đồng bộ ở mã nguồn local.

3. **Ghi Nhật Ký Làm Việc Chi Tiết (Agent Log)**:
   - Mọi thao tác sửa đổi, tệp script nào được tạo/chạy, đoạn mã nào được chỉnh sửa/thêm vào, tệp nào được upload phải được lưu vết đầy đủ và rõ ràng trong tệp `Agent/activity_log.md`.

4. **Tự Động Đồng Bộ Git (Auto Push)**:
   - Ngay sau khi hoàn thành thao tác và ghi nhận log, Agent tự động chạy lệnh `git add`, `git commit` và `git push origin main` để lưu trữ tất cả tệp script, mã nguồn cùng tệp nhật ký lên GitHub.
