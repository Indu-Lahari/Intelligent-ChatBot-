from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton
import sys


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(700, 500)

        # Add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        # To set the chat area only readable
        self.chat_area.setReadOnly(True)

        # Add the input field widget
        self.input_area = QLineEdit(self)
        self.input_area.setGeometry(10, 340, 480, 40)

        # Add the button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 340, 80, 40)

        self.show()


app = QApplication(sys.argv)
chatbot_window = ChatbotWindow()
sys.exit(app.exec())