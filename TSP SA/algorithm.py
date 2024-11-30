import math
import random

# Hoán đổi hai điểm ngẫu nhiên
def swap(order):
    idx1, idx2 = random.sample(range(len(order)), 2)
    order[idx1], order[idx2] = order[idx2], order[idx1]
    return order

# Tính khoảng cách giữa hai điểm
def distance(point1, point2):
    return math.sqrt((point1.x() - point2.x())**2 + (point1.y() - point2.y())**2)

# Tính tổng khoảng cách của một chu trình
def total_distance(points, order):
    dist = 0
    for i in range(len(order)):
        dist += distance(points[order[i]], points[order[(i + 1) % len(order)]])
    return dist


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