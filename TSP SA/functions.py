import random
import math

from PyQt6.QtWidgets import ( QInputDialog, QGraphicsEllipseItem, QGraphicsTextItem
)
from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtGui import QPen, QColor

from utils import update_order_label, update_text_items


# Tính khoảng cách giữa hai điểm
def distance(point1, point2):
    return math.sqrt((point1.x() - point2.x())**2 + (point1.y() - point2.y())**2)

# Tính tổng khoảng cách của một chu trình
def total_distance(points, order):
    dist = 0
    for i in range(len(order)):
        dist += distance(points[order[i]], points[order[(i + 1) % len(order)]])
    return dist

# Hoán đổi hai điểm ngẫu nhiên
def swap(order):
    idx1, idx2 = random.sample(range(len(order)), 2)
    order[idx1], order[idx2] = order[idx2], order[idx1]
    return order

# Thuật toán Simulated Annealing
def simulated_annealing(points, initial_temp=1000, cooling_rate=0.995, stop_temp=1e-3):
    if len(points) < 2:
        # Không có đủ điểm để chạy thuật toán
        return list(range(len(points))), []

    num_points = len(points)
    order = list(range(num_points))  # Bắt đầu với thứ tự ban đầu
    current_distance = total_distance(points, order)  # Khoảng cách hiện tại
    temp = initial_temp  # Nhiệt độ khởi tạo
    path_updates = []  # Lưu các bước cập nhật đường đi

    while temp > stop_temp:
        idx1, idx2 = random.sample(range(num_points), 2)
        new_order = order[:]
        new_order[idx1], new_order[idx2] = new_order[idx2], new_order[idx1]
        new_distance = total_distance(points, new_order)

        # Điều kiện chấp nhận: tốt hơn hoặc tệ hơn với xác suất
        if new_distance < current_distance or random.random() < math.exp((current_distance - new_distance) / temp):
            order = new_order
            current_distance = new_distance
            path_updates.append((order[:], current_distance))

        # Giảm nhiệt độ và đảm bảo không bị mắc kẹt
        temp *= cooling_rate
        if len(path_updates) > 1000:  # Hạn chế số bước để tránh vòng lặp vô hạn
            break

    return order, path_updates

#Thêm điểm tự do
def add_point(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            pos = self.view.mapToScene(event.pos())
            _create_point(self, pos.x(), pos.y())

def _create_point(self, x, y):
        pos = QPointF(x, y)
        self.points.append(pos)

        ellipse = QGraphicsEllipseItem(pos.x() - 5, pos.y() - 5, 10, 10)
        ellipse.setBrush(QColor("red"))
        self.scene.addItem(ellipse)
        self.ellipses.append(ellipse)

        order_text = QGraphicsTextItem(f"{len(self.ellipses)}")
        order_text.setDefaultTextColor(QColor("blue"))
        order_text.setPos(pos.x() - 10, pos.y() - 20)
        self.scene.addItem(order_text)

        coord_text = QGraphicsTextItem(f"({pos.x():.1f}, {pos.y():.1f})")
        coord_text.setDefaultTextColor(QColor("black"))
        coord_text.setPos(pos.x() - 30, pos.y() + 10)
        self.scene.addItem(coord_text)

        self.text_items.append((order_text, coord_text))

def solve_tsp(self):
    self.order_label.setText("Order: ")
    self.is_pause = False

    if len(self.points) < 2:
        self.status_label.setText("Status: Không đủ điểm để giải TSP")
        return

    # Xóa đường cũ
    for line in self.path:
        self.scene.removeItem(line)
    self.path = []

    try:
        order, path_updates = simulated_annealing(self.points)
        if not path_updates:
            self.status_label.setText("Status: Không tìm thấy giải pháp")
            return

        self.path_updates = path_updates
        self.final_order = order

        self.status_label.setText("Status: Đang tiến hành")
        self.step_index = 0
        self.timer.start(39)

        self.pause_button.setText("Pause")
        self.is_paused = False
    except Exception as e:
        self.status_label.setText(f"Error: {str(e)}")
        print("Error during solving TSP:", str(e))


def draw_next_step(self):
    if not self.path_updates:
        self.timer.stop()
        self.status_label.setText("Status: Không có bước nào để vẽ")
        return

    if self.step_index < len(self.path_updates):
        for line in self.path:
            self.scene.removeItem(line)
        self.path = []

        order, current_distance = self.path_updates[self.step_index]
        pen = QPen(QColor("blue"), 2)
        for i in range(len(order)):
            p1 = self.points[order[i]]
            p2 = self.points[order[(i + 1) % len(order)]]
            line = self.scene.addLine(p1.x(), p1.y(), p2.x(), p2.y(), pen=pen)
            self.path.append(line)

        self.distance_label.setText(f"Distance: {current_distance:.2f}")
        self.step_index += 1
    else:
        self.timer.stop()
        self.status_label.setText("Status: Đã hoàn thành")
        update_order_label(self.order_label, self.final_order)


def random_points(self):
        num_points, ok = QInputDialog.getInt(self, "Random Points", "Enter the number of points:", 5, 1, 100)
        if ok:
            for _ in range(num_points):
                x = random.randint(50, 750)
                y = random.randint(50, 550)
                _create_point(self, x, y)

def clear_screen(self):
        for item in self.ellipses + [text for pair in self.text_items for text in pair] + self.path:
            self.scene.removeItem(item)
        self.points.clear()
        self.ellipses.clear()
        self.text_items.clear()
        self.path.clear()
        self.timer.stop()
        self.distance_label.setText("Distance: 0")
        self.status_label.setText("Status: Chưa bắt đầu")
        self.order_label.setText("Order: ")

def add_custom_point(self):
        x, ok_x = QInputDialog.getDouble(self, "Add Point", "Enter X coordinate:")
        if not ok_x:
            return
        y, ok_y = QInputDialog.getDouble(self, "Add Point", "Enter Y coordinate:")
        if not ok_y:
            return
        _create_point(self, x, y)

def erase_point(self):
        index, ok = QInputDialog.getInt(self, "Erase Point", "Enter point index to erase (1 to N):", 1, 1, len(self.points))
        if not ok:
            return

        idx = index - 1
        self.scene.removeItem(self.ellipses[idx])
        for text_item in self.text_items[idx]:
            self.scene.removeItem(text_item)

        del self.points[idx]
        del self.ellipses[idx]
        del self.text_items[idx]

        update_text_items(self.text_items, self.points)


def toggle_pause(self):
        if self.is_paused:
            self.status_label.setText("Status: Đang tiến hành")
            self.pause_button.setText("Pause")
            self.timer.start(39)
        else:
            self.status_label.setText("Status: Tạm dừng")
            self.pause_button.setText("Continue")
            self.timer.stop()
        self.is_paused = not self.is_paused
