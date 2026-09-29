import { writeFileSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const root = dirname(dirname(fileURLToPath(import.meta.url)));

const categories = {
  community: "Cộng đồng AI",
  productivity: "Năng suất",
  design: "Công cụ AI",
  models: "Mô hình AI",
  agents: "AI Agent",
  tools: "Công cụ AI",
  education: "Cộng đồng AI",
  seo: "AI SEO",
  business: "Tự động hóa doanh nghiệp",
  automation: "Tự động hóa doanh nghiệp",
  news: "Mô hình AI"
};

const records = [
  ["AI Money Lab Vs AI Profit Boardroom", "So sánh cộng đồng AI miễn phí và trả phí: nên bắt đầu từ đâu?", "community", "2026-05-08", "7 phút đọc", ["cộng đồng AI", "học AI", "automation"]],
  ["OMI Obsidian For Entrepreneurs", "OMI và Obsidian cho doanh nhân: xây hệ thống ghi nhớ công việc bằng AI", "productivity", "2026-05-08", "6 phút đọc", ["Obsidian", "năng suất", "ghi chú AI"]],
  ["Open Design Vs Claude Design For Agencies", "Open Design và Claude Design cho agency: chọn công cụ thiết kế AI thế nào?", "design", "2026-05-08", "6 phút đọc", ["thiết kế AI", "agency", "workflow"]],
  ["OpenClaw Roadmap Course", "Lộ trình học OpenClaw: cách theo kịp công cụ AI Agent mới", "community", "2026-05-08", "7 phút đọc", ["OpenClaw", "AI Agent", "lộ trình học"]],
  ["Sonnet For Business", "Sonnet cho doanh nghiệp: dùng mô hình AI vào quy trình nào trước?", "models", "2026-05-08", "6 phút đọc", ["mô hình AI", "doanh nghiệp", "workflow"]],
  ["Switched From OpenClaw To Accomplish", "Khi nào nên đổi nền tảng AI Agent trong workflow của bạn?", "agents", "2026-05-06", "6 phút đọc", ["AI Agent", "workflow", "nền tảng"]],
  ["Why Agent Zero Beats OpenClaw In Real Tests", "Đánh giá AI Agent qua bài test thực tế: nhìn vào tiêu chí nào?", "agents", "2026-05-06", "6 phút đọc", ["Agent Zero", "OpenClaw", "đánh giá agent"]],
  ["AI Profit Boardroom Vault Tools", "Một kho công cụ AI nên được tổ chức như thế nào để dễ dùng?", "community", "2026-05-06", "5 phút đọc", ["kho công cụ", "automation", "template"]],
  ["Claude Operon Vs Chat Code Co-work", "Các chế độ làm việc của Claude: chat, code và cộng tác khác nhau ra sao?", "tools", "2026-05-06", "6 phút đọc", ["Claude", "AI tools", "workflow"]],
  ["Build Anything With Hermes", "Hermes AI Agent: dùng framework agent để tự động hóa công việc", "agents", "2026-05-06", "6 phút đọc", ["Hermes", "AI Agent", "framework"]],
  ["Hermes Kanban Setup Build Websites With AI", "Thiết lập Kanban cho Hermes: quản lý quy trình xây website bằng AI", "agents", "2026-05-06", "6 phút đọc", ["Hermes", "Kanban", "xây website"]],
  ["Build A Hermes Second Brain", "Xây second brain với Hermes, ghi chú và AI Automation", "agents", "2026-05-06", "7 phút đọc", ["second brain", "Hermes", "Obsidian"]],
  ["AI Profit Boardroom Review", "Đánh giá một cộng đồng AI Automation: nên nhìn vào giá trị nào?", "community", "2026-05-06", "7 phút đọc", ["review", "cộng đồng AI", "automation"]],
  ["Julian Goldie Courses Overview", "Một khóa học AI Automation nên có những phần nào?", "education", "2026-05-06", "6 phút đọc", ["khóa học AI", "workflow", "thực hành"]],
  ["Setting Up Remotion Inside Google Antigravity", "Thiết lập Remotion trong môi trường coding AI: quy trình cho video tự động", "tools", "2026-05-06", "6 phút đọc", ["Remotion", "video AI", "coding agent"]],
  ["How To Setup Claude Code Remotion", "Claude Code và Remotion: tạo video bằng workflow lập trình AI", "tools", "2026-05-05", "6 phút đọc", ["Claude Code", "Remotion", "video tự động"]],
  ["Hermes Swarm Roles Explained", "Các vai trò trong Hermes Swarm: builder, reviewer và cách phối hợp", "agents", "2026-05-05", "6 phút đọc", ["agent swarm", "Hermes", "đội AI"]],
  ["Hermes Workspace V2 Setup Guide", "Thiết lập Hermes Workspace: nền làm việc cho AI Agent", "agents", "2026-05-05", "6 phút đọc", ["Hermes Workspace", "AI Agent", "setup"]],
  ["Persistent Memory In OpenClaw", "Thiết lập bộ nhớ dài hạn cho OpenClaw: khi nào cần và làm sao kiểm soát?", "agents", "2026-05-05", "6 phút đọc", ["OpenClaw", "memory", "MCP"]],
  ["OpenClaw Mission Control Setup", "OpenClaw Mission Control: quản lý agent bằng dashboard trực quan", "agents", "2026-05-05", "5 phút đọc", ["OpenClaw", "dashboard", "agent ops"]],
  ["Auto Research Claw In OpenClaw", "Auto Research Claw: tự động hóa quy trình nghiên cứu bằng AI Agent", "agents", "2026-05-02", "6 phút đọc", ["research agent", "OpenClaw", "tự động hóa nghiên cứu"]],
  ["Gemma Chat Build Apps Offline", "Gemma Chat: xây ứng dụng offline bằng mô hình cục bộ", "models", "2026-05-02", "6 phút đọc", ["Gemma", "offline AI", "local model"]],
  ["Google Jitro Vs Jules", "Google Jitro và Jules: khác nhau ở đâu trong workflow lập trình AI?", "agents", "2026-05-02", "6 phút đọc", ["Google", "coding agent", "developer workflow"]],
  ["Google Simula Mechanism Design", "Google Simula và mechanism design: hiểu dữ liệu tổng hợp cho AI", "models", "2026-05-02", "7 phút đọc", ["synthetic data", "mechanism design", "mô hình AI"]],
  ["Hermes Workspace Swarms Setup", "Thiết lập agent swarm trong Hermes Workspace từng bước", "agents", "2026-05-02", "6 phút đọc", ["Hermes", "swarm", "multi-agent"]],
  ["Hermes Agent One-Click Install Guide", "Cài Hermes Agent đơn giản: hướng dẫn cho người không chuyên kỹ thuật", "agents", "2026-05-02", "6 phút đọc", ["Hermes", "cài đặt", "AI Agent"]],
  ["Kimi Benchmark Vs Claude GPT And Gemini", "Kimi so với Claude, GPT và Gemini: đọc benchmark thế nào cho đúng?", "models", "2026-05-02", "6 phút đọc", ["Kimi", "benchmark", "mô hình AI"]],
  ["Manus Cloud Computer Vs AWS", "Manus Cloud Computer và AWS: stack mới cho người làm solo", "agents", "2026-05-02", "7 phút đọc", ["Manus", "cloud computer", "solo business"]],
  ["Aion UI With OpenClaw", "Thiết lập Aion UI với OpenClaw: giao diện điều khiển agent", "agents", "2026-05-02", "6 phút đọc", ["Aion UI", "OpenClaw", "agent UI"]],
  ["Claude Code SEO Agent Workflow", "Claude Code SEO Agent: quy trình xây nội dung SEO bằng AI", "seo", "2026-04-30", "7 phút đọc", ["Claude Code", "AI SEO", "content workflow"]],
  ["ClawX OpenClaw First Day", "Ngày đầu với ClawX OpenClaw: nên kiểm tra gì trước khi dùng thật?", "agents", "2026-04-30", "7 phút đọc", ["ClawX", "OpenClaw", "review"]],
  ["Free Local AI Agent Hermes Ollama", "AI Agent local miễn phí với Hermes và Ollama: khi nào nên dùng?", "agents", "2026-04-30", "7 phút đọc", ["Ollama", "Hermes", "local AI"]],
  ["OpenClaw Computer Use Codex", "OpenClaw Computer Use: cho agent thao tác máy tính sao cho an toàn?", "agents", "2026-04-30", "6 phút đọc", ["computer use", "OpenClaw", "Codex"]],
  ["OpenClaw Desktop App Setup", "Cài OpenClaw Desktop App: cách bắt đầu với AI Agent giao diện sạch", "agents", "2026-04-30", "6 phút đọc", ["OpenClaw", "desktop app", "setup"]],
  ["Rank Reddit On Google With AI Content", "SEO Reddit bằng nội dung AI: cơ hội và giới hạn khi làm ở Việt Nam", "seo", "2026-04-30", "6 phút đọc", ["Reddit SEO", "AI content", "Google"]],
  ["Build A Telegram AI Agent", "Xây Telegram AI Agent: biến chat thành kênh automation", "agents", "2026-04-30", "7 phút đọc", ["Telegram", "AI Agent", "automation"]],
  ["Telegram Lobster AI Agent Setup", "Thiết lập Telegram AI Agent: token, cấu hình và tác vụ đầu tiên", "agents", "2026-04-30", "6 phút đọc", ["Telegram bot", "AI Agent", "setup"]],
  ["Claude Code Setup Step By Step", "Thiết lập Claude Code từng bước: nền tảng cho coding bằng AI", "tools", "2026-04-29", "5 phút đọc", ["Claude Code", "setup", "developer"]],
  ["ChatGPT Chronicle Setup", "ChatGPT Chronicle: bật, cấu hình và dùng an toàn cho năng suất", "tools", "2026-04-28", "5 phút đọc", ["ChatGPT", "năng suất", "privacy"]],
  ["Hermes Desktop App Setup", "Hermes Desktop App: thiết lập nhanh để bắt đầu làm việc với agent", "agents", "2026-04-28", "6 phút đọc", ["Hermes", "desktop", "AI Agent"]],
  ["Hermes WebUI Setup", "Hermes WebUI: dựng giao diện chat cho agent trong vài bước", "agents", "2026-04-28", "6 phút đọc", ["Hermes WebUI", "chat UI", "setup"]],
  ["Rank In Google AI Mode", "Xếp hạng trong Google AI Mode: quy trình SEO cần thay đổi gì?", "seo", "2026-04-28", "6 phút đọc", ["Google AI Mode", "AI SEO", "search"]],
  ["AI Lead Generation Agents", "AI Lead Generation Agent: tự động hóa pipeline bán hàng", "business", "2026-04-27", "3 phút đọc", ["lead generation", "sales automation", "AI Agent"]],
  ["Skool SEO Content Strategy", "SEO cho cộng đồng online: biến trang cộng đồng thành tài sản nội dung", "seo", "2026-04-27", "2 phút đọc", ["community SEO", "content strategy", "Skool"]],
  ["Build Your Own OpenClaw Skills Tools", "Tự xây OpenClaw: lớp skills và tools quyết định năng lực agent", "agents", "2026-04-26", "8 phút đọc", ["OpenClaw", "skills", "tools"]],
  ["DeepSeek OpenClaw Setup", "DeepSeek và OpenClaw: thiết lập local gateway cho agent", "agents", "2026-04-26", "6 phút đọc", ["DeepSeek", "OpenClaw", "gateway"]],
  ["DeepSeek SEO Tool Landing Pages", "DeepSeek SEO Tool: tạo landing page có cấu trúc bằng một prompt", "seo", "2026-04-26", "7 phút đọc", ["DeepSeek", "landing page", "AI SEO"]],
  ["DeepSeek SEO Trending Keyword Method", "DeepSeek SEO: phương pháp chọn từ khóa xu hướng để lên bài nhanh", "seo", "2026-04-26", "7 phút đọc", ["DeepSeek", "keyword research", "SEO"]],
  ["DeepSeek Ollama Install", "Cài DeepSeek với Ollama: chạy mô hình AI theo hướng tiết kiệm", "tools", "2026-04-26", "8 phút đọc", ["DeepSeek", "Ollama", "local model"]],
  ["DeepSeek OpenClaw Ollama Cloud", "DeepSeek, OpenClaw và Ollama Cloud: kết nối mô hình với agent", "agents", "2026-04-26", "6 phút đọc", ["DeepSeek", "Ollama Cloud", "OpenClaw"]],
  ["Generic Agent Skill Tree", "Skill tree cho AI Agent: vì sao agent cần học theo năng lực?", "agents", "2026-04-26", "6 phút đọc", ["skill tree", "AutoGPT", "AI Agent"]],
  ["Hermes AI Course Multi-Agent Profiles", "Hermes AI Course: hiểu multi-agent profile và fallback chain", "education", "2026-04-26", "9 phút đọc", ["Hermes", "multi-agent", "fallback"]],
  ["Hermes DeepSeek Setup", "Hermes và DeepSeek: thiết lập mô hình cho agent trong workflow thật", "agents", "2026-04-26", "7 phút đọc", ["Hermes", "DeepSeek", "setup"]],
  ["Hermes Open WebUI Docker Ollama", "Hermes Open WebUI với Docker và Ollama: dựng giao diện AI nội bộ", "agents", "2026-04-26", "7 phút đọc", ["Docker", "Ollama", "Hermes"]],
  ["ChatGPT AI SEO Workspace Agents", "ChatGPT AI SEO với Workspace Agents: vận hành nội dung mỗi ngày", "seo", "2026-04-24", "7 phút đọc", ["ChatGPT", "workspace agents", "AI SEO"]],
  ["ChatGPT Image Tutorial", "ChatGPT Image cho nội dung marketing: tạo poster, mockup và bản đồ ý tưởng", "tools", "2026-04-24", "7 phút đọc", ["ChatGPT Image", "thiết kế", "marketing"]],
  ["DeepSeek Tutorial Context MoE", "DeepSeek tutorial: hiểu context dài và MoE khi chọn mô hình", "models", "2026-04-24", "7 phút đọc", ["DeepSeek", "MoE", "context"]],
  ["Paperclip Hermes Agent Review", "Paperclip Hermes Agent: mô hình tổ chức công việc bằng AI", "agents", "2026-04-24", "7 phút đọc", ["Paperclip", "Hermes", "AI org chart"]],
  ["ChatGPT Workspace Agents Handoff", "Workspace Agents trong ChatGPT: handoff tác vụ giữa nhiều agent", "automation", "2026-04-23", "7 phút đọc", ["ChatGPT", "handoff", "multi-agent"]],
  ["Claude Obsidian Plugin Vs Claude Code", "Claude và Obsidian: chọn plugin hay Claude Code cho hệ ghi chú?", "tools", "2026-04-23", "5 phút đọc", ["Claude", "Obsidian", "notes"]],
  ["OpenClaw Mission Control Dashboard", "OpenClaw Mission Control: squad agent, task board và memory browser", "automation", "2026-04-23", "5 phút đọc", ["OpenClaw", "mission control", "agent squad"]],
  ["OpenMythos Open Source AI", "Open source AI đang thắng ở đâu: bài học cho doanh nghiệp nhỏ", "business", "2026-04-23", "6 phút đọc", ["open source AI", "doanh nghiệp", "chiến lược"]],
  ["Space Agent vs OpenClaw", "Space Agent và OpenClaw: so sánh sức mạnh, tốc độ và chi phí", "agents", "2026-04-23", "6 phút đọc", ["Space Agent", "OpenClaw", "so sánh agent"]],
  ["Free AI SEO Agent Hermes Firecrawl Qwen", "AI SEO Agent miễn phí: kết hợp Hermes, Firecrawl và Qwen", "seo", "2026-04-22", "10 phút đọc", ["Firecrawl", "Qwen", "AI SEO"]],
  ["Hermes Gemma Setup Local Agent Stack", "Hermes và Gemma: stack AI Agent local cho dữ liệu riêng tư", "agents", "2026-04-22", "9 phút đọc", ["Hermes", "Gemma", "local AI"]],
  ["Kimi Agent Swarms Review", "Kimi Agent Swarm: khi nào nên dùng nhiều agent cùng lúc?", "tools", "2026-04-22", "8 phút đọc", ["Kimi", "agent swarm", "review"]],
  ["OpenClaw Update iMessage Agents", "OpenClaw update: bài học về tích hợp message, cron và bảo mật", "agents", "2026-04-22", "11 phút đọc", ["OpenClaw", "update", "security"]],
  ["OpenClaw Kimi Tutorial", "OpenClaw và Kimi: dựng agent stack với mô hình mở", "agents", "2026-04-22", "7 phút đọc", ["OpenClaw", "Kimi", "Ollama"]],
  ["Claude Code Free Ollama Setup", "Claude Code miễn phí qua Ollama: hiểu đúng giới hạn và lựa chọn mô hình", "tools", "2026-04-20", "6 phút đọc", ["Claude Code", "Ollama", "local model"]],
  ["Claude Code Local Offline Setup", "Claude Code local: thiết lập môi trường offline cho lập trình bằng AI", "tools", "2026-04-20", "6 phút đọc", ["Claude Code", "offline", "developer"]],
  ["GPT Pro Spud Model Revealed", "Tin đồn mô hình GPT mới: nên đọc thông tin rò rỉ như thế nào?", "news", "2026-04-20", "6 phút đọc", ["GPT", "AI news", "model rumors"]],
  ["Hermes Agent Mission Control V2", "Hermes Agent Mission Control: giao diện quản trị agent thế hệ mới", "agents", "2026-04-20", "5 phút đọc", ["Hermes", "mission control", "workspace"]],
  ["Hermes Agent Workspace Developer Review", "Hermes Agent Workspace: góc nhìn developer về kiến trúc và hiệu năng", "agents", "2026-04-20", "5 phút đọc", ["Hermes", "developer", "workspace"]],
  ["Hermes AI Video Generator Manim", "Hermes AI Video Generator: tạo video giải thích bằng Manim", "tools", "2026-04-20", "9 phút đọc", ["Manim", "video AI", "Hermes"]],
  ["Best AI Agent Community Review", "Chọn cộng đồng AI Agent: tiêu chí đánh giá trước khi tham gia", "community", "2026-04-19", "9 phút đọc", ["cộng đồng AI", "AI Agent", "review"]],
  ["Hermes VS OpenClaw", "Hermes hay OpenClaw: vì sao câu trả lời phụ thuộc workflow?", "agents", "2026-04-19", "9 phút đọc", ["Hermes", "OpenClaw", "so sánh"]],
  ["OpenClaw Byterover Memory Upgrade", "OpenClaw và Byterover: nâng cấp bộ nhớ dài hạn cho agent", "agents", "2026-04-19", "10 phút đọc", ["Byterover", "memory", "OpenClaw"]],
  ["Claude Code AI SEO Netlify MCP", "Claude Code AI SEO với Netlify và MCP: workflow xuất bản nội dung", "seo", "2026-04-18", "10 phút đọc", ["Claude Code", "Netlify", "MCP"]],
  ["Ollama Hermes Combo", "Ollama và Hermes: khi nào local AI Agent tốt hơn cloud?", "agents", "2026-04-18", "9 phút đọc", ["Ollama", "Hermes", "local agent"]],
  ["Claude Opus AI SEO System", "Hệ thống AI SEO với Claude: tự động hóa nội dung nhưng vẫn cần biên tập", "seo", "2026-04-17", "11 phút đọc", ["Claude", "AI SEO", "content system"]],
  ["OpenClaw Opus Update", "OpenClaw và model mới: cách đọc một bản cập nhật có giá trị", "tools", "2026-04-17", "11 phút đọc", ["OpenClaw", "model update", "AI tools"]],
  ["OpenClaw AI SEO System", "OpenClaw AI SEO: thiết kế hệ thống nội dung tự động có kiểm soát", "seo", "2026-04-16", "10 phút đọc", ["OpenClaw", "AI SEO", "automation"]]
];

function slugify(value) {
  return value
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .replace(/đ/g, "d")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-|-$/g, "");
}

function inferTopic(title) {
  return title.replace(/:.*$/, "").replace(/\?.*$/, "").trim();
}

function inferAngle(category) {
  const mapping = {
    "AI Agent": "việc đưa AI Agent vào quy trình làm việc có kiểm soát",
    "AI SEO": "việc dùng AI để nghiên cứu, sản xuất và tối ưu nội dung tìm kiếm",
    "Công cụ AI": "việc chọn công cụ đúng với nhu cầu thay vì chạy theo xu hướng",
    "Mô hình AI": "việc đánh giá mô hình theo nhiệm vụ kinh doanh cụ thể",
    "Tự động hóa doanh nghiệp": "việc biến tác vụ lặp lại thành hệ thống vận hành rõ ràng",
    "Năng suất": "việc giảm tải thao tác cá nhân và lưu lại tri thức làm việc",
    "Cộng đồng AI": "việc học AI trong môi trường có định hướng và phản hồi"
  };
  return mapping[category] || "việc áp dụng AI vào quy trình thực tế";
}

function inferUseCase(category) {
  const mapping = {
    "AI Agent": "Trong thực tế, một đội nhỏ có thể giao cho agent nhiệm vụ nghiên cứu thị trường, đọc tài liệu, tạo bản nháp báo cáo và nhắc người phụ trách kiểm tra trước khi gửi ra ngoài.",
    "AI SEO": "Với đội nội dung, workflow có thể bắt đầu từ nghiên cứu từ khóa, gom insight, tạo dàn ý, viết bản nháp, tối ưu tiêu đề và chuẩn bị checklist xuất bản.",
    "Công cụ AI": "Với người làm marketing hoặc vận hành, công cụ nên được thử trên một tác vụ nhỏ trước, sau đó mới đưa vào quy trình chính thức.",
    "Mô hình AI": "Khi chọn mô hình, doanh nghiệp nên test bằng tài liệu thật, ngôn ngữ thật và yêu cầu thật, thay vì chỉ nhìn bảng xếp hạng chung.",
    "Tự động hóa doanh nghiệp": "Một doanh nghiệp dịch vụ có thể tự động hóa thu lead, phân loại yêu cầu, gửi phản hồi ban đầu và tạo nhắc việc cho đội sales.",
    "Năng suất": "Một cá nhân bận rộn có thể dùng AI để tóm tắt họp, ghi lại quyết định, trích việc cần làm và tổ chức kiến thức theo dự án.",
    "Cộng đồng AI": "Người mới nên dùng cộng đồng để hỏi đúng câu hỏi, xem ví dụ triển khai thật và tránh mất thời gian vào những công cụ chưa phù hợp."
  };
  return mapping[category] || "Ứng dụng nên bắt đầu từ một tác vụ rõ đầu vào, rõ đầu ra và có tiêu chuẩn kiểm tra.";
}

function bodyFor(record) {
  const [sourceTitle, title, categoryKey] = record;
  const category = categories[categoryKey];
  const topic = inferTopic(title);
  const angle = inferAngle(category);
  const useCase = inferUseCase(category);
  return [
    `## Vì sao chủ đề này đáng quan tâm\n\n${topic} là một chủ đề đáng theo dõi vì AI Automation không còn dừng ở việc hỏi đáp với chatbot. Doanh nghiệp, freelancer và đội marketing đang bắt đầu dùng AI như một lớp vận hành mới: đọc tài liệu, gom dữ liệu, tạo bản nháp, kiểm tra chất lượng và phối hợp giữa nhiều công cụ. Điểm quan trọng không phải là công cụ nào đang được nhắc nhiều nhất, mà là công cụ đó giúp giảm ma sát ở khâu nào trong công việc hằng ngày. Khi nhìn theo hướng này, mỗi bài viết không còn là tin tức công nghệ đơn lẻ, mà trở thành một gợi ý để thiết kế quy trình làm việc tốt hơn.`,
    `## Cách nhìn đúng cho người Việt\n\nVới thị trường Việt Nam, ${angle} cần được đặt trong bối cảnh rất thực tế: ngân sách hạn chế, đội ngũ nhỏ, dữ liệu phân tán và nhiều người chưa quen làm việc với quy trình chuẩn. Vì vậy, một workflow AI tốt phải dễ giải thích cho người không chuyên, có bước kiểm tra đầu ra và không phụ thuộc hoàn toàn vào một nền tảng duy nhất. Nếu một công cụ đòi hỏi quá nhiều cấu hình, quá nhiều quyền truy cập hoặc quá khó bảo trì, nó có thể tạo thêm rủi ro thay vì tiết kiệm thời gian. Cách tiếp cận an toàn là bắt đầu từ một tác vụ nhỏ, đo kết quả, rồi mới mở rộng.`,
    `## Quy trình triển khai gợi ý\n\nBước đầu tiên là xác định rõ đầu vào, đầu ra và tiêu chuẩn chất lượng. Ví dụ: đầu vào là danh sách từ khóa, tài liệu khách hàng hoặc lịch sử hội thoại; đầu ra là bản tóm tắt, dàn ý, email cá nhân hóa hoặc báo cáo nghiên cứu. Bước thứ hai là chia workflow thành các khâu nhỏ: thu thập dữ liệu, xử lý bằng AI, kiểm tra kết quả, lưu lại tri thức và chuyển giao cho người phụ trách. Bước thứ ba là đặt điểm kiểm soát. Với AI Agent, không nên cấp quyền quá rộng ngay từ đầu. Hãy ghi log thao tác, giới hạn phạm vi dữ liệu và yêu cầu con người phê duyệt trước khi kết quả ảnh hưởng đến khách hàng, tài chính hoặc thương hiệu.`,
    `## Ứng dụng thực tế\n\n${useCase} Với chủ đề "${sourceTitle}", cách áp dụng tốt nhất là biến ý tưởng thành checklist triển khai. Người phụ trách nên hỏi: tác vụ này đang tốn bao nhiêu thời gian, lỗi thường xảy ra ở đâu, dữ liệu nằm ở hệ thống nào, ai là người duyệt cuối cùng và kết quả cần được lưu lại ra sao. Khi trả lời được các câu hỏi đó, AI mới có đất để tạo giá trị. Một automation tốt thường không thay thế toàn bộ con người; nó giảm thao tác lặp lại để con người tập trung vào quyết định, sáng tạo và quan hệ khách hàng.`,
    `## Lưu ý khi áp dụng\n\nKhông nên xem AI Automation là phép màu. Mô hình có thể trả lời sai, công cụ có thể đổi giá, API có thể giới hạn tốc độ và dữ liệu nội bộ có thể chứa thông tin nhạy cảm. Với các tác vụ liên quan đến nội dung công khai, nên có bước biên tập để kiểm tra giọng văn, nguồn thông tin và tính phù hợp với khách hàng Việt Nam. Với các tác vụ liên quan đến vận hành, nên có phương án dự phòng nếu công cụ dừng hoạt động. Đặc biệt, các con số về doanh thu, traffic, thành viên hoặc hiệu suất chỉ nên dùng khi bạn có dữ liệu của chính mình và có thể giải thích cách đo.`,
    `## Kết luận\n\n${topic} hữu ích nhất khi được đặt vào một hệ thống rõ ràng: mục tiêu cụ thể, dữ liệu sạch, quy trình nhỏ, kiểm tra đều và cải tiến liên tục. Nếu bạn mới bắt đầu, hãy chọn một workflow có rủi ro thấp như tóm tắt tài liệu, tạo dàn ý nội dung hoặc phân loại lead. Sau khi đã thấy tiết kiệm thời gian thật, hãy mở rộng sang những tác vụ có nhiều bước hơn như SEO AI, chăm sóc khách hàng, nghiên cứu thị trường hoặc điều phối agent. Làm chậm một chút ở giai đoạn thiết kế sẽ giúp hệ thống AI bền hơn khi đi vào vận hành.`
  ].join("\n\n");
}

const articles = records.map(([sourceTitle, title, categoryKey, date, readTime, tags]) => {
  const category = categories[categoryKey];
  return {
    slug: slugify(title),
    title,
    sourceTitle,
    category,
    date,
    readTime,
    excerpt: `Bài viết phân tích ${inferTopic(title).toLowerCase()} theo hướng thực chiến, giúp người Việt hiểu cách áp dụng AI Automation vào công việc mà không bị cuốn theo quảng cáo công cụ.`,
    tags,
    body: bodyFor([sourceTitle, title, categoryKey])
  };
});

const source = `// Generated from work/generate-articles.mjs. Public source topics only; Vietnamese content is original.\n(function () {\n  window.HHA_ARTICLES = ${JSON.stringify(articles, null, 2)};\n  window.HHA_CATEGORIES = ${JSON.stringify([...new Set(articles.map((article) => article.category))], null, 2)};\n})();\n`;

writeFileSync(join(root, "articles.js"), source, "utf8");
console.log(`Generated ${articles.length} articles`);
