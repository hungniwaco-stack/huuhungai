# Hữu Hùng AI - SEO/AEO/GEO Static Build

Bộ file này dùng cho website HTML tĩnh. Mỗi bài viết có một URL riêng trong thư mục `articles/`.

## Cần đổi trước khi xuất bản

Thay toàn bộ `https://example.com` bằng domain thật của anh trong:

- `sitemap.xml`
- `robots.txt`
- `llms.txt`
- schema trong các file HTML nếu muốn chuẩn tuyệt đối theo domain thật

## File chính

- `index.html`: trang danh sách và bộ lọc bài viết
- `articles/*.html`: 82 trang bài viết riêng
- `sitemap.xml`: sitemap liệt kê trang chủ và 82 bài
- `robots.txt`: chỉ dẫn crawler
- `llms.txt`: mô tả website cho AI crawler
