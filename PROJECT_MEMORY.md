# Hữu Hùng AI - Project Memory

Ngày ghi nhớ/cập nhật: 2026-07-05

## Thương hiệu đã chốt

- Tên dùng chính: **Hữu Hùng AI**.
- Tên ban đầu/cũ: Hữu Hùng AI Automation.
- Định vị: **AI Automation thực chiến cho người Việt**.
- Website là trung tâm tri thức/blog cá nhân trước, chưa bán mạnh.
- Giọng thương hiệu: chuyên gia, thực tế, dễ hiểu, đúng chuyên ngành, dành cho người Việt đọc.
- CTA nên nhẹ, authority-first: đọc bài, khám phá chủ đề, theo dõi cập nhật, nhận tài liệu hoặc liên hệ sau này.

## Nguồn tham khảo và nguyên tắc nội dung

- Nguồn tham khảo ban đầu: https://aiprofitboardroom.com/blog/
- Chỉ lấy dữ liệu công khai: mô hình topic, tiêu đề/chủ đề bài viết, cấu trúc blog.
- Không lấy số liệu nội bộ, traffic, doanh thu, conversion, member count riêng tư.
- Không copy/dịch nguyên văn bài gốc; nội dung phải viết lại bằng tiếng Việt gốc.
- Người dùng muốn mô hình topic giống website nguồn, nhưng ngôn ngữ website chính là tiếng Việt.

## Taxonomy/topic model đã áp dụng

Mô hình Browse by Topic lấy theo ảnh website nguồn, gồm 33 chip chủ đề. Chip hiển thị nhãn tiếng Việt nhưng vẫn giữ số liệu nguồn trong ngoặc.

Ví dụ:

- Tất cả bài viết (298)
- AI Agent (106)
- Khóa học AI (19)
- Tự động hóa AI (16)
- Cộng đồng AI (51)
- Công cụ AI (18)
- SEO bằng AI (17)
- Lập trình với AI (6)
- Năng suất với AI (2)
- Mô hình AI (5)
- Kinh doanh với AI (3)
- Tin tức AI (2)

Số nhỏ bên phải chip là số bài hiện có trong thư viện Hữu Hùng AI.

## Cấu trúc website hiện tại

Thư mục chính người dùng yêu cầu lưu:

- `D:\Skill\Huu Hung AI Automation`

File chính:

- `D:\Skill\Huu Hung AI Automation\index.html`

Thư mục bài viết riêng:

- `D:\Skill\Huu Hung AI Automation\articles\`

Hiện trạng:

- Có 82 bài viết.
- Mỗi bài đã được tách thành 1 file HTML riêng trong `articles/`.
- `index.html` chỉ là trang danh sách, có topic chips, tìm kiếm, lọc bài.
- Bấm/chọn bài nào sẽ mở trực tiếp trang riêng của bài đó, không còn mở bằng anchor `#ten-bai` trong cùng một file.
- Mỗi trang bài có:
  - Tiêu đề riêng.
  - Meta description.
  - Article schema.
  - Khối “Trả lời nhanh”.
  - Nút “Về danh sách bài”.

## File crawler/SEO đã tạo

Đã tạo/cập nhật trong `D:\Skill\Huu Hung AI Automation\`:

- `sitemap.xml`
- `robots.txt`
- `llms.txt`
- `README.md`

Kết quả kiểm tra gần nhất:

- `sitemap.xml` có 84 URL: trang chủ `/`, `index.html`, và 82 bài riêng trong `/articles/`.
- `robots.txt` trỏ đến sitemap.
- `llms.txt` mô tả thương hiệu, chủ đề chính, số bài và nhóm nội dung cho AI crawler.
- Không lỗi mã hóa tiếng Việt.

Lưu ý quan trọng:

- Domain đang để placeholder: `https://huuhungai.com`.
- Khi người dùng có domain thật, cần thay `https://huuhungai.com` trong:
  - `sitemap.xml`
  - `robots.txt`
  - `llms.txt`
  - schema trong các file HTML nếu muốn chuẩn tuyệt đối.

## Workspace và output liên quan

Workspace gốc:

- `C:\Users\HUNG\Documents\Codex\2026-07-05\https-aiprofitboardroom-com-blog`

Output static chính trong workspace:

- `outputs\huu-hung-ai-seo-aeo-geo\index.html`
- `outputs\huu-hung-ai-seo-aeo-geo\articles\*.html`
- `outputs\huu-hung-ai-seo-aeo-geo\sitemap.xml`
- `outputs\huu-hung-ai-seo-aeo-geo\robots.txt`
- `outputs\huu-hung-ai-seo-aeo-geo\llms.txt`

Scripts quan trọng:

- `work\generate-separated-articles.mjs`: tạo `index.html` và 82 bài riêng.
- `work\generate-crawler-files.mjs`: tạo `sitemap.xml`, `robots.txt`, `llms.txt`, `README.md`.
- `work\verify-topic-model.mjs`: kiểm tra nhanh topic/search/script của bản trước.

## Tài liệu SEO/AEO/GEO đã đọc và áp dụng

Người dùng cung cấp file:

- `D:\Dropbox\01. DỰ ÁN 2026\SEO\SEO-AEO-GEO.docx`

Các điểm đã vận dụng:

- SEO: topic cluster, intent, HTML crawlable, sitemap.
- AEO: trả lời nhanh đầu bài, heading rõ, FAQ/schema.
- GEO: nội dung tĩnh dễ đọc cho AI crawler, `llms.txt`, schema, cấu trúc URL riêng cho từng bài.
- Quyết định kỹ thuật: ưu tiên static HTML vì nhiều AI crawler không chạy JavaScript.

## UI/UX đã áp dụng

Dựa trên 2 bộ skill đã nạp:

1. UI/UX Pro Max
2. frontend-design

Định hướng:

- Content-first / Newsletter-like blog.
- Swiss Modernism 2.0.
- Giao diện chuyên gia, tối giản, dễ đọc.
- Tránh landing page bán hàng quá mạnh.
- Tránh gradient AI tím-xanh sáo mòn.
- Có hệ thống chip chủ đề rõ ràng.
- Có tìm kiếm/lọc để người đọc nhanh chóng chọn bài.

## Lỗi đã gặp và cách xử lý

1. Người dùng báo: “Chưa xem được các bài viết”.
   - Nguyên nhân: bản tương tác/JS/hash route không phù hợp khi mở trực tiếp hoặc crawler đọc.
   - Cách xử lý: tạo bản HTML tĩnh/reader và sau đó tách từng bài thành file riêng.

2. Người dùng báo: “file index.html chưa hoạt động”.
   - Nguyên nhân: file root `index.html` chưa phải bản static SEO/AEO/GEO chính.
   - Cách xử lý: thay root `index.html` bằng bản static hoạt động.

3. Người dùng muốn “sắp xếp theo mô hình của Website mình đã lấy số liệu”.
   - Cách xử lý: thêm Browse/Duyệt theo chủ đề giống mô hình nguồn, giữ số liệu nguồn trong ngoặc.

4. Người dùng muốn “tách riêng từng bài”.
   - Cách xử lý: tạo 82 file riêng trong `articles/`, sửa toàn bộ link card sang `articles/*.html`.

## Kiểm tra đã thực hiện

- Đếm đủ 82 file bài viết riêng.
- Kiểm tra `index.html` có 82 thẻ bài trỏ sang `articles/*.html`.
- Kiểm tra không còn thẻ bài nào mở bằng anchor `#ten-bai`.
- Mở thử một bài bằng Chrome headless: có tiêu đề, nội dung, Article schema, nút quay lại, không lỗi mã hóa.
- Kiểm tra `sitemap.xml`: 84 URL, gồm 82 article URL.
- Kiểm tra `robots.txt` có sitemap.
- Kiểm tra `llms.txt` có thương hiệu và đường dẫn bài viết.

## Đánh giá chất lượng hiện tại

- Cấu trúc kỹ thuật đã tốt hơn bản đầu: có trang danh sách, 82 trang bài riêng, sitemap/robots/llms.
- Phù hợp để đưa lên hosting tĩnh như Netlify, Cloudflare Pages hoặc hosting thường.
- Nội dung hiện vẫn còn tính template; nếu public nghiêm túc cần chọn nhóm bài trọng điểm để viết sâu hơn.
- Điểm mạnh: cấu trúc SEO/GEO tốt, topic model rõ, dễ mở rộng.
- Điểm cần làm tiếp: domain thật, polish UI, viết lại sâu các bài quan trọng, thêm trang giới thiệu/tác giả, CTA nhẹ.

## Skills đã nạp trong phiên

Đã nạp UI/UX Pro Max vào:

- `C:\Users\HUNG\.codex\skills\ui-ux-pro-max`
- `C:\Users\HUNG\.codex\skills\ui-styling`
- `C:\Users\HUNG\.codex\skills\design-system`
- `C:\Users\HUNG\.codex\skills\design`
- `C:\Users\HUNG\.codex\skills\brand`
- `C:\Users\HUNG\.codex\skills\banner-design`
- `C:\Users\HUNG\.codex\skills\slides`

Đã nạp frontend-design từ GitHub vào:

- `C:\Users\HUNG\.codex\skills\frontend-design`

## Cách tiếp tục lần sau

Khi tiếp tục, đọc file này trước:

- `D:\Skill\Huu Hung AI Automation\PROJECT_MEMORY.md`

Không hỏi lại các quyết định đã chốt, trừ khi người dùng muốn đổi.

Ưu tiên tiếp theo:

1. Nếu có domain thật: thay `https://huuhungai.com` toàn site và tạo lại sitemap/robots/llms/schema.
2. Nếu chưa có domain: polish UI trang danh sách và trang bài.
3. Chọn 10-15 bài quan trọng nhất để viết lại sâu, tăng chuyên môn và khác biệt.
4. Thêm trang `about.html` giới thiệu Hữu Hùng AI.
5. Thêm CTA nhẹ: nhận tài liệu, theo dõi cập nhật hoặc liên hệ tư vấn.
6. Khi publish, upload toàn bộ thư mục `D:\Skill\Huu Hung AI Automation` hoặc bản trong `outputs\huu-hung-ai-seo-aeo-geo` lên hosting tĩnh.
