from PyQt6.QtWidgets import QGraphicsTextItem

def update_order_label(order_label, order):
    order_text = "Order: " + " -> ".join(str(i + 1) for i in order)
    order_label.setText(order_text)

def update_text_items(text_items, points):
    for i, (order_text, coord_text) in enumerate(text_items):
        order_text.setPlainText(f"{i + 1}")
        coord_text.setPlainText(f"({points[i].x():.1f}, {points[i].y():.1f})")
