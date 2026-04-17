# Data Structures and Algorithms (DSA) - Midterm Project

##  Tổng quan về dự án
Dự án này là một nghiên cứu chuyên sâu và triển khai thực nghiệm 4 kỹ thuật nền tảng trong cấu trúc dữ liệu và thuật thuật toán: Prefix Sum, Sliding Window, Difference Array và Dynamic Array (Resize). Dự án kết hợp giữa lý thuyết toán học, phân tích độ phức tạp và ứng dụng giải quyết các bài toán thực tế.

**Nội dung chính:**
Nghiên cứu & Cài đặt: Triển khai từ đầu (Custom Class) và dùng Built-in Python cho 4 kỹ thuật: Prefix Sum, Sliding Window, Difference Array, Dynamic Array.

Phân tích & Tối ưu: Đánh giá chi tiết Big-O, nền tảng toán học và tư duy tối ưu hóa "What to use" cho từng dạng bài toán cụ thể.

Thực hành & Tổng hợp: Giải quyết bài tập LeetCode, phân tích ứng dụng thực tế và hệ thống hóa toàn bộ nội dung qua báo cáo LaTeX kèm sơ đồ minh họa.

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
│
├── Leetcode/
│   ├── Array_resize.ipynb
│   ├── Difference_array.ipynb
│   └── prefix_sum.ipynb
│
├── built_in/
│   ├── difference_array.py
│   ├── prefix_sum.py
│   ├── sliding_window.py
│   └── sliding_window copy.py
│
├── src/
│   ├── array.py
│   ├── difference_array.py
│   ├── prefix_sum.py
│   └── sliding_window.py
│
├── test_built_in/
│   ├── __init__.py
│   ├── test_difference_array.py
│   ├── test_prefix_sum.py
│   └── test_sliding_window.py
│
├── tests/
│   ├── __init__.py
│   ├── test_array.py
│   ├── test_difference_array.py
│   ├── test_prefix_sum.py
│   └── test_sliding_window.py
│
├── .gitignore
└── requirements.txt
```
## Các bước cài đặt
### Bước 1: Clone dự án về máy
git clone [https://github.com/khanhlinh170806-cpu/dsa.git](https://github.com/khanhlinh170806-cpu/dsa.git)

### Bước 2: Di chuyển vào thư mục dự án
cd dsa

### Bước 3: Tạo môi trường ảo (Khuyến khích)
python -m venv venv

### Bước 4: Kích hoạt môi trường ảo
### Trên Windows:
venv\Scripts\activate
### Trên macOS/Linux:
source venv/bin/activate

### Bước 5: Cài đặt các thư viện bổ trợ
pip install -r requirements.txt

## Cách chạy thử nghiệm
### Chạy tất cả các bài test trong thư mục tests/
pytest tests/

### Hoặc chạy một file cụ thể trong thư mục src
python src/tên_file.py

## Công nghệ sử dụng
Ngôn ngữ: Python (Cấu trúc dữ liệu linh hoạt, dễ đọc).

Định dạng: .py và .ipynb (Jupyter Notebook cho việc giải thích thuật toán).

Công cụ: Pytest cho Unit Testing.
