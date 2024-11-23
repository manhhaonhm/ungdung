import sys
import json
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QListWidget, QTableWidget, QTableWidgetItem,
    QInputDialog, QFileDialog, QMessageBox, QScrollArea, QCheckBox, QHeaderView
)
from PyQt6.QtGui import QPixmap, QIcon, QIntValidator
from PyQt6.QtCore import Qt
import os
def load_products():
    try:
        with open("data/products.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
        
def save_products(products):
    with open("products.json", "w") as file:
        json.dump(products, file, indent=4)


# Path to the JSON file
USER_DATA_FILE = "data/users.json"

# Function to load users from the JSON file
def load_users():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as file:
            return json.load(file).get("users", [])
    else:
        return []

# Function to save users to the JSON file
def save_users(users):
    with open(USER_DATA_FILE, "w") as file:
        json.dump({"users": users}, file, indent=4)

# Styling
APP_STYLE = """
QMainWindow {
    background-color: #f0f2f5;
}

QLabel {
    font-size: 16px;
    color: #333;
    margin: 5px 0;
}

QPushButton {
    background-color: #0056b3;
    color: white;
    border-radius: 8px;
    padding: 16px;
    font-size: 16px;
    font-weight: bold;
    transition: all 0.3s ease;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

QPushButton:hover {
    background-color: #0073e6;
    box-shadow: 0 6px 8px rgba(0, 0, 0, 0.2);
    transform: scale(1.02);
}

QPushButton:pressed {
    background-color: #003d80;
    box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.2);
}

QLineEdit {
    padding: 10px;
    border: 2px solid #ccc;
    border-radius: 8px;
    font-size: 14px;
    background-color: #fff;
    transition: border-color 0.3s ease;
    box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1);
}

QLineEdit:focus {
    border-color: #0056b3;
    box-shadow: 0 0 5px rgba(0, 86, 179, 0.3);
}

QVBoxLayout {
    margin: 20px;
}

QMessageBox {
    background-color: #fefefe;
    font-size: 14px;
}

QWidget {
    border: none;
    margin: 0;
    padding: 0;
}

QLabel#title {
    font-size: 22px;
    font-weight: bold;
    color: #0056b3;
    margin-bottom: 15px;
    text-align: center;
}
"""


# Login Window
class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 400, 400)
        self.setStyleSheet(APP_STYLE)

        layout = QVBoxLayout()
        layout.setSpacing(20)

        self.title = QLabel("Welcome to Stock Manager")
        self.title.setObjectName("title")

        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your username")

        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.handle_login)

        self.register_button = QPushButton("Register")
        self.register_button.clicked.connect(self.go_to_register)

        layout.addWidget(self.title, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def handle_login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        users = load_users()
        user_found = any(user for user in users if user["username"] == username and user["password"] == password)

        if user_found:
            self.go_to_home()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")

    def go_to_register(self):
        self.register_window = RegisterWindow()
        self.register_window.show()
        self.close()

    def go_to_home(self):
        self.home_window = HomeWindow()
        self.home_window.show()
        self.close()


class RegisterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Register")
        self.setGeometry(100, 100, 400, 400)
        self.setStyleSheet(APP_STYLE)

        layout = QVBoxLayout()

        self.title = QLabel("Register a New Account")
        self.title.setObjectName("title")

        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Choose a username")

        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Choose a password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.register_button = QPushButton("Register")
        self.register_button.clicked.connect(self.handle_register)

        self.login_button = QPushButton("Back to Login")
        self.login_button.clicked.connect(self.go_to_login)

        layout.addWidget(self.title, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.register_button)
        layout.addWidget(self.login_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def handle_register(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        if not username or not password:
            QMessageBox.warning(self, "Registration Failed", "Username and password cannot be empty.")
            return

        users = load_users()

        # Check if the username already exists
        if any(user for user in users if user["username"] == username):
            QMessageBox.warning(self, "Registration Failed", "Username already exists.")
            return

        # Add the new user and save to the JSON file
        users.append({"username": username, "password": password})
        save_users(users)

        QMessageBox.information(self, "Success", "User registered successfully.")
        self.go_to_login()

    def go_to_login(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()


class ProductCard(QWidget):
    def __init__(self, product):
        super().__init__()
        self.product = product
        self.setStyleSheet("""
            QWidget {
                border-radius: 10px;
                border: 1px solid #ddd;
                padding: 15px;
                background-color: #ffffff;
                margin: 10px;
                max-width: 250px;
                box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.15);
            }

            QLabel {
                font-size: 16px;
                font-weight: bold;
                color: #333;
                margin-bottom: 8px;
                text-align: center;
            }

            QLabel.price {
                font-size: 18px;
                color: #e74c3c;
                font-weight: bold;
                margin-bottom: 15px;
            }

            QPushButton {
                background-color: #0056b3;
                color: white;
                border-radius: 8px;
                padding: 16px;
                font-size: 16px;
                font-weight: bold;
                transition: all 0.3s ease;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }


            QPushButton:hover {
                background-color: #0056b3;
            }

            QPushButton:pressed {
                background-color: #004085;
            }

            QLabel.image {
                border-radius: 5px;
                overflow: hidden;
                margin-bottom: 10px;
            }
        """)

        layout = QVBoxLayout()

        # Product image
        self.image_label = QLabel()
        pixmap = QPixmap(self.product["image"]).scaled(200, 150, Qt.AspectRatioMode.KeepAspectRatio)
        self.image_label.setPixmap(pixmap)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setObjectName("image")

        # Product name
        self.name_label = QLabel(self.product["name"])
        
        # Product price
        self.price_label = QLabel(f"${self.product['price']}")
        self.price_label.setObjectName("price")
        
        # Buy now button
        self.buy_button = QPushButton("Buy Now")
        self.buy_button.clicked.connect(self.on_buy)

        # Add widgets to layout
        layout.addWidget(self.image_label)
        layout.addWidget(self.name_label)
        layout.addWidget(self.price_label)
        layout.addWidget(self.buy_button)

        self.setLayout(layout)

    def on_buy(self):
        if self.product["stock"] > 0:
            self.product["stock"] -= 1
            save_products(self.products)  # Save updated stock to JSON
            QMessageBox.information(self, "Purchase Successful", f"You bought 1 {self.product['name']}!")
        else:
            QMessageBox.warning(self, "Out of Stock", f"{self.product['name']} is out of stock!")




class HomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Home")
        self.setGeometry(100, 100, 1000, 600)  # Optimized for modern screens
        self.setStyleSheet(APP_STYLE)

        main_layout = QVBoxLayout()

        # Header label
        header_label = QLabel("Products in Stock")
        header_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #333;")
        header_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Scrollable area for product cards
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        self.product_list_widget = QWidget()  # Container for product cards
        self.product_list_layout = QHBoxLayout()  # Horizontal scroll layout
        self.product_list_widget.setLayout(self.product_list_layout)
        scroll_area.setWidget(self.product_list_widget)

        # Navigation button
        self.product_management_button = QPushButton("Go to Product Management")
        self.product_management_button.setStyleSheet("""
            QPushButton {
                background-color: #0056b3;
                color: white;
                border-radius: 8px;
                padding: 16px;
                font-size: 16px;
                font-weight: bold;
                transition: all 0.3s ease;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }

            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        self.product_management_button.clicked.connect(self.go_to_product_management)

        # Assemble main layout
        main_layout.addWidget(header_label)
        main_layout.addWidget(scroll_area)
        main_layout.addWidget(self.product_management_button, alignment=Qt.AlignmentFlag.AlignCenter)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        self.load_products()

    def load_products(self):
        self.product_list_layout.setContentsMargins(10, 10, 10, 10)
        self.product_list_layout.setSpacing(20)

        products = load_products()

        # Populate the layout with product cards
        for product in products:
            card = ProductCard(product)
            self.product_list_layout.addWidget(card)

    def go_to_product_management(self):
        self.product_management_window = ProductManagementWindow(self)
        self.product_management_window.show()
        self.close()

# Product Management Window
class ProductManagementWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.setWindowTitle("Product Management")
        self.setGeometry(100, 100, 1000, 900)
        self.setStyleSheet(APP_STYLE)

        layout = QVBoxLayout()
        
        # Search functionality
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search by name...")

        # Filters for price and stock
        self.min_price_input = QLineEdit()
        self.min_price_input.setPlaceholderText("Min Price")
        self.min_price_input.setValidator(QIntValidator(0, 100000, self))

        self.max_price_input = QLineEdit()
        self.max_price_input.setPlaceholderText("Max Price")
        self.max_price_input.setValidator(QIntValidator(0, 100000, self))

        self.stock_filter_checkbox = QCheckBox("Show only low-stock items")

        # Table to display products
        self.product_table = QTableWidget(0, 5)
        self.product_table.setHorizontalHeaderLabels(["ID", "Name", "Price", "Stock", "Image"])
        self.product_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)


        # Buttons for actions
        self.add_button = QPushButton("Add Product")
        self.delete_button = QPushButton("Delete Product")
        self.edit_button = QPushButton("Edit Product")
        self.update_stock_button = QPushButton("Update Stock")
        self.back_button = QPushButton("Back to Homepage")

        # Load initial products
        self.products = load_products()
        self.load_products()

        # Connect signals
        self.search_input.textChanged.connect(self.filter_products)
        self.min_price_input.textChanged.connect(self.filter_products)
        self.max_price_input.textChanged.connect(self.filter_products)
        self.stock_filter_checkbox.toggled.connect(self.filter_products)
        self.add_button.clicked.connect(self.add_product)
        self.delete_button.clicked.connect(self.delete_product)
        self.edit_button.clicked.connect(self.edit_product)
        self.update_stock_button.clicked.connect(self.update_stock)
        self.back_button.clicked.connect(self.go_back_to_home)

        # Arrange widgets in the layout
        filters_layout = QHBoxLayout()
        filters_layout.addWidget(QLabel("Search:"))
        filters_layout.addWidget(self.search_input)
        filters_layout.addWidget(QLabel("Min Price:"))
        filters_layout.addWidget(self.min_price_input)
        filters_layout.addWidget(QLabel("Max Price:"))
        filters_layout.addWidget(self.max_price_input)
        filters_layout.addWidget(self.stock_filter_checkbox)

        layout.addLayout(filters_layout)
        layout.addWidget(self.product_table)
        layout.addWidget(self.add_button)
        layout.addWidget(self.delete_button)
        layout.addWidget(self.edit_button)
        layout.addWidget(self.update_stock_button)
        layout.addWidget(self.back_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def load_products(self):
        self.product_table.setRowCount(0)
        self.product_table.verticalHeader().setDefaultSectionSize(150)  # Set default row height
        for product in self.products:
            self.add_product_to_table(product)

    def add_product_to_table(self, product):
        row_position = self.product_table.rowCount()
        self.product_table.insertRow(row_position)

        self.product_table.setItem(row_position, 0, QTableWidgetItem(product["id"]))
        self.product_table.setItem(row_position, 1, QTableWidgetItem(product["name"]))
        self.product_table.setItem(row_position, 2, QTableWidgetItem(f"${product['price']}"))
        self.product_table.setItem(row_position, 3, QTableWidgetItem(str(product.get("stock", 0))))

        # Set image
        img_item = QTableWidgetItem()
        img_item.setData(
            Qt.ItemDataRole.DecorationRole,
            QPixmap(product["image"]).scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio)
        )
        self.product_table.setItem(row_position, 4, img_item)

        # Set row height
        self.product_table.setRowHeight(row_position, 150)



    def filter_products(self):
        search_text = self.search_input.text().lower()
        min_price = int(self.min_price_input.text()) if self.min_price_input.text() else 0
        max_price = int(self.max_price_input.text()) if self.max_price_input.text() else float("inf")
        show_low_stock = self.stock_filter_checkbox.isChecked()

        self.product_table.setRowCount(0)
        for product in self.products:
            price = int(product["price"])
            stock = product.get("stock", 0)

            if (
                search_text in product["name"].lower()
                and min_price <= price <= max_price
                and (not show_low_stock or stock < 5)  # Example: Low stock is defined as less than 5
            ):
                self.add_product_to_table(product)

    def add_product(self):
        name, ok = QInputDialog.getText(self, "Add Product", "Enter product name:")
        if ok and name:
            price, ok = QInputDialog.getText(self, "Add Product", "Enter product price:")
            if ok and price.isdigit():
                stock, ok = QInputDialog.getInt(self, "Add Product", "Enter stock quantity:", min=0, max=100000)
                if ok:
                    image_path, _ = QFileDialog.getOpenFileName(self, "Select Product Image", "", "Images (*.png *.jpg *.jpeg)")
                    if image_path:
                        new_product = {
                            "id": str(len(self.products) + 1),
                            "name": name,
                            "price": price,
                            "stock": stock,
                            "image": image_path,
                        }
                        self.products.append(new_product)
                        save_products(self.products)
                        self.load_products()

    def delete_product(self):
        selected_row = self.product_table.currentRow()
        if selected_row >= 0:
            product_id = self.product_table.item(selected_row, 0).text()
            self.products = [p for p in self.products if p["id"] != product_id]
            save_products(self.products)
            self.load_products()

    def edit_product(self):
        selected_row = self.product_table.currentRow()
        if selected_row >= 0:
            product = self.products[selected_row]
            name, ok = QInputDialog.getText(self, "Edit Product", "Enter new product name:", text=product["name"])
            if ok and name:
                price, ok = QInputDialog.getText(self, "Edit Product", "Enter new product price:", text=str(product["price"]))
                if ok and price.isdigit():
                    stock, ok = QInputDialog.getInt(self, "Edit Product", "Enter stock quantity:", value=product.get("stock", 0))
                    if ok:
                        image_path, _ = QFileDialog.getOpenFileName(self, "Select New Product Image", "", "Images (*.png *.jpg *.jpeg)")
                        if image_path:
                            product["image"] = image_path
                        product["name"] = name
                        product["price"] = price
                        product["stock"] = stock
                        save_products(self.products)
                        self.load_products()

    def update_stock(self):
        selected_row = self.product_table.currentRow()
        if selected_row >= 0:
            product_id = self.product_table.item(selected_row, 0).text()
            stock, ok = QInputDialog.getInt(self, "Update Stock", "Enter new stock quantity:", min=0, max=100000)
            if ok:
                for product in self.products:
                    if product["id"] == product_id:
                        product["stock"] = stock
                        break
                save_products(self.products)
                self.load_products()

    def go_back_to_home(self):
        self.parent.load_products()
        self.parent.show()
        self.close()

# Main function
def main():
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()