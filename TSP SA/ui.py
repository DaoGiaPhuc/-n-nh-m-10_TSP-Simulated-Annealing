from PyQt6.QtWidgets import (
    QMainWindow, QGraphicsScene, QGraphicsView, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QWidget
)
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QPainter
from functions import (add_point, _create_point, solve_tsp, erase_point, clear_screen,
    toggle_pause, draw_next_step, random_points, add_custom_point
)

class TSPWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simulated Annealing - TSP")
        self.setGeometry(100, 100, 800, 600)

        # Main widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Graphics View
        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene, self)
        self.view.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.view.mousePressEvent = self.add_point
        self.layout.addWidget(self.view)

        # Labels container
        self.labels_layout = QHBoxLayout()
        self.distance_label = QLabel("Distance: 0", self)
        self.status_label = QLabel("Status: Chưa bắt đầu", self)
        self.labels_layout.addWidget(self.distance_label)
        self.labels_layout.addWidget(self.status_label)
        self.layout.addLayout(self.labels_layout)

        # Order Label
        self.order_label = QLabel("Order: ", self)
        self.order_label.setWordWrap(True)
        self.layout.addWidget(self.order_label)

        # Buttons container
        self.buttons_layout = QHBoxLayout()
        self.solve_button = QPushButton("Solve TSP", self)
        self.solve_button.clicked.connect(self.solve_tsp)
        self.random_button = QPushButton("Random Points", self)
        self.random_button.clicked.connect(self.random_points)
        self.clear_button = QPushButton("Clear", self)
        self.clear_button.clicked.connect(self.clear_screen)
        self.add_button = QPushButton("Add", self)
        self.add_button.clicked.connect(self.add_custom_point)
        self.erase_button = QPushButton("Erase", self)
        self.erase_button.clicked.connect(self.erase_point)
        self.exit_button = QPushButton("Exit", self)
        self.exit_button.clicked.connect(self.close)
        self.pause_button = QPushButton("Pause", self)
        self.pause_button.clicked.connect(self.toggle_pause)
        self.buttons_layout.addWidget(self.solve_button)
        self.buttons_layout.addWidget(self.random_button)
        self.buttons_layout.addWidget(self.clear_button)
        self.buttons_layout.addWidget(self.add_button)
        self.buttons_layout.addWidget(self.erase_button)
        self.buttons_layout.addWidget(self.pause_button)
        self.buttons_layout.addWidget(self.exit_button)
        self.layout.addLayout(self.buttons_layout)

        # Variables
        self.points = []
        self.ellipses = []
        self.text_items = []
        self.path = []
        self.path_updates = []
        self.final_order = []
        self.step_index = 0
        self.is_paused = False

        # Timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.draw_next_step)

        # Apply Light Theme Styling
        self.setStyleSheet("""
            QMainWindow {
                background-color: #fdfdfd;
            }
            QPushButton {
                background-color: #e6e6e6;
                border: 1px solid #bfbfbf;
                color: #333333;
                padding: 5px;
                font-size: 14px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #d9d9d9;
            }
            QPushButton:pressed {
                background-color: #cccccc;
            }
            QLabel {
                color: #333333;
                font-size: 14px;
            }
            QGraphicsView {
                background-color: #ffffff;
                border: 1px solid #bfbfbf;
            }
        """)

    def _create_point(self, x, y):
        _create_point(self, x, y)

    def add_point(self, event):
        add_point(self, event)

    def solve_tsp(self):
        solve_tsp(self)

    def draw_next_step(self):
        draw_next_step(self)

    def random_points(self):
        random_points(self)

    def clear_screen(self):
        clear_screen(self)

    def add_custom_point(self):
        add_custom_point(self)

    def erase_point(self):
        erase_point(self)

    def toggle_pause(self):
        toggle_pause(self)
