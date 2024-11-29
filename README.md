
# **Giải Bài Toán Travelling Salesman bằng Thuật Toán Simulated Annealing**

Đây là ứng dụng giải bài toán Travelling Salesman Problem (TSP) sử dụng thuật toán Simulated Annealing, được xây dựng UI từ thư viện PyQt6

---

## **Cài đặt**

### **Bước 1: Cài đặt Visual Studio Code và Python**
- Tải xuống và cài đặt [Visual Studio Code](https://code.visualstudio.com/).
- Tải xuống và cài đặt [Python](https://www.python.org/).

### **Bước 2: Cài đặt extension Python trên Visual Studio Code**
- Trong Visual Studio Code, vào **Extensions** (phím tắt: `Ctrl+Shift+X`), tìm **Python** và nhấn **Install**.

### **Bước 3: Cài đặt các thư viện cần thiết**
Mở **Terminal** (phím tắt: `Ctrl+\``) và nhập các lệnh sau để cài đặt PyQt6 và các công cụ liên quan:
```
pip install pyqt6
```

### **Bước 4: Chạy chương trình**
- Chạy file `main.py`:
  ```
  python main.py
  ```

---

## **Hướng dẫn sử dụng**

### **Chế độ Tạo Điểm**
1. **Thêm Điểm Thủ Công (Manual Points)**:
   - Chọn chế độ **Manual Points** để tạo các điểm bằng cách nhấp chuột vào giao diện.
   - Bạn cũng có thể nhập tọa độ cụ thể thông qua hộp thoại **Add**.

2. **Tạo Điểm Ngẫu Nhiên (Random Points)**:
   - Chọn chế độ **Random Points** để tự động tạo một số lượng điểm ngẫu nhiên trên giao diện.

---

### **Thao Tác với Điểm**
- **Xóa Điểm**: Nhấn nút **Erase** để xóa điểm thông qua hộp thoại nhập hoặc sử dụng chuột.
- **Xóa Toàn Bộ**: Nhấn nút **Clear** để xóa toàn bộ điểm và đường đi.

---

### **Giải Thuật Toán**
- Nhấn **Solve TSP** để bắt đầu thuật toán Simulated Annealing.
  - Quá trình giải sẽ hiển thị từng bước với thời gian trễ 39ms.
  - Tổng khoảng cách và trạng thái sẽ được cập nhật liên tục trong giao diện.

- Trong quá trình giải:
  - Nhấn **Pause** để tạm dừng.
  - Nhấn **Continue** để tiếp tục.

---

### **Kết Thúc**
- Sau khi hoàn thành, kết quả hiển thị:
  - Thứ tự các điểm theo chu trình tối ưu.
  - Tổng khoảng cách của chu trình.

---

## **Công Nghệ Sử Dụng**
- **IDE**: Visual Studio Code
- **Ngôn ngữ**: Python
- **Giao diện**: PyQt6

---

## **Cảm ơn**
Cảm ơn bạn đã sử dụng ứng dụng của chúng tôi. Ứng dụng đã đạt được mục tiêu giải bài toán TSP, nhưng vẫn còn nhiều hạn chế về giao diện người dùng và thuật toán chưa được tối ưu hóa hoàn toàn. Chúng tôi hy vọng sẽ tiếp tục nâng cấp và cải thiện ứng dụng để đáp ứng các nhu cầu thực tế trong tương lai.
