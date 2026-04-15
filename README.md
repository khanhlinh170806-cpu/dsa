# Data Structures and Algorithms (DSA) - Midterm Project

##  Tổng quan về dự án
Dự án này tập trung vào việc nghiên cứu, triển khai và đánh giá các cấu trúc dữ liệu và giải thuật cơ bản. Mục tiêu chính là hiểu rõ cách thức hoạt động của các cấu trúc dữ liệu từ mức độ mã nguồn thấp nhất và ứng dụng chúng để tối ưu hóa hiệu suất bài toán.

**Nội dung chính:**
- Triển khai thủ công (Manual Implementation) các cấu trúc dữ liệu: Linked List, Stack, Queue, Trees, Graphs.
- So sánh hiệu năng giữa mã nguồn tự viết và các thư viện sẵn có (`built-in`) của Python.
- Giải quyết các bài toán thuật toán trên nền tảng **LeetCode** để luyện tập tư duy logic.

---

##  Thông tin thành viên
Dự án được thực hiện bởi:

| Họ và Tên | Mã Sinh Viên | Contribution |
|-----------|--------------|---------|
| Lê Phạm Khánh Linh | [Mã số sinh viên] | -- |
| Trần Viết Long | [Mã số sinh viên] | -- |
| Vũ Trần Cát Linh | [Mã số sinh viên] | -- |
| Phùng Nhật Minh | [Mã số sinh viên] | -- |

---

##  Cấu trúc thư mục
Repository được tổ chức khoa học như sau:

```text
dsa/
├── src/                # Mã nguồn tự triển khai các cấu trúc dữ liệu
├── built_in/           # Ví dụ về các cấu trúc dữ liệu có sẵn trong Python
├── Leetcode/           # Lời giải các bài tập thuật toán (Python/Notebook)
├── tests/              # Bộ mã kiểm thử cho các cấu trúc dữ liệu tự viết
├── test_built_in/      # Bộ mã kiểm thử cho các thư viện built-in
├── .gitignore          # Cấu hình các tệp tin không đẩy lên GitHub
├── requirements.txt    # Danh sách các thư viện cần thiết
└── README.md           # Tài liệu hướng dẫn này
```
## Các bước cài đặt
# Bước 1: Clone dự án về máy
git clone [https://github.com/khanhlinh170806-cpu/dsa.git](https://github.com/khanhlinh170806-cpu/dsa.git)

# Bước 2: Di chuyển vào thư mục dự án
cd dsa

# Bước 3: Tạo môi trường ảo (Khuyến khích)
python -m venv venv

# Bước 4: Kích hoạt môi trường ảo
# Trên Windows:
venv\Scripts\activate
# Trên macOS/Linux:
source venv/bin/activate

# Bước 5: Cài đặt các thư viện bổ trợ
pip install -r requirements.txt

## Cách chạy thử nghiệm
# Chạy tất cả các bài test trong thư mục tests/
pytest tests/

# Hoặc chạy một file cụ thể trong thư mục src
python src/tên_file.py

## Công nghệ sử dụng
Ngôn ngữ: Python (Cấu trúc dữ liệu linh hoạt, dễ đọc).

Định dạng: .py và .ipynb (Jupyter Notebook cho việc giải thích thuật toán).

Công cụ: Pytest cho Unit Testing.
