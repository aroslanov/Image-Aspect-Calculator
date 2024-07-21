import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox, QCheckBox, QSpinBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QDropEvent, QDragEnterEvent, QPixmap
from PIL import Image
import re
import io

class AspectRatioCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Aspect Ratio Calculator')
        self.setGeometry(100, 100, 400, 400)
        self.setAcceptDrops(True)

        main_layout = QVBoxLayout()

        # First row: W1 and W2
        w1_layout = QHBoxLayout()
        self.w1_input = QSpinBox()
        self.w2_input = QSpinBox()
        self.w1_input.setRange(1, 10000)
        self.w2_input.setRange(1, 10000)
        w1_layout.addWidget(QLabel('W1'))
        w1_layout.addWidget(self.w1_input)
        w1_layout.addWidget(QLabel('W2'))
        w1_layout.addWidget(self.w2_input)
        main_layout.addLayout(w1_layout)

        # Second row: H1 and H2
        h1_layout = QHBoxLayout()
        self.h1_input = QSpinBox()
        self.h2_input = QSpinBox()
        self.h1_input.setRange(1, 10000)
        self.h2_input.setRange(1, 10000)
        h1_layout.addWidget(QLabel('H1'))
        h1_layout.addWidget(self.h1_input)
        h1_layout.addWidget(QLabel('H2'))
        h1_layout.addWidget(self.h2_input)
        main_layout.addLayout(h1_layout)

        # Connect valueChanged signals to calculate_ratio
        self.w2_input.valueChanged.connect(self.calculate_ratio)
        self.h2_input.valueChanged.connect(self.calculate_ratio)

        # Common ratios dropdown
        ratio_layout = QHBoxLayout()
        ratio_layout.addWidget(QLabel('Common ratios:'))
        self.ratio_combo = QComboBox()
        self.ratio_combo.addItems([
            '1920 x 1080 (HD TV, iPhone 6 plus)',
            '1334 x 750 (iPhone 6)',
            '1024 x 768 (iPad)',
            '800 x 600',
            '640 x 480 (VGA)'
        ])
        self.ratio_combo.currentIndexChanged.connect(self.set_common_ratio)
        ratio_layout.addWidget(self.ratio_combo)
        main_layout.addLayout(ratio_layout)

        # Checkbox for rounding
        self.round_checkbox = QCheckBox('Round results to the nearest whole number')
        main_layout.addWidget(self.round_checkbox)

        # Aspect ratio result
        self.result_label = QLabel('Your aspect ratio is:')
        main_layout.addWidget(self.result_label)

        # Calculate button
        self.calc_button = QPushButton('Calculate')
        self.calc_button.clicked.connect(self.calculate_ratio)
        main_layout.addWidget(self.calc_button)

        # Drop area label and thumbnail
        drop_thumbnail_layout = QHBoxLayout()
        self.drop_label = QLabel('Drop an image here to auto-fill dimensions')
        self.drop_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.drop_label.setStyleSheet('border: 2px dashed #aaa; padding: 10px;')
        drop_thumbnail_layout.addWidget(self.drop_label)
        
        self.thumbnail_label = QLabel()
        self.thumbnail_label.setFixedSize(100, 100)
        self.thumbnail_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.thumbnail_label.setStyleSheet('border: 1px solid #aaa;')
        drop_thumbnail_layout.addWidget(self.thumbnail_label)
        
        main_layout.addLayout(drop_thumbnail_layout)

        self.setLayout(main_layout)

    def calculate_ratio(self):
        try:
            w1 = self.w1_input.value()
            h1 = self.h1_input.value()
            w2 = self.w2_input.value()
            h2 = self.h2_input.value()

            # Calculate aspect ratio from W1 and H1
            if w1 and h1:
                gcd = self.gcd(w1, h1)
                ratio = f"{int(w1/gcd)}:{int(h1/gcd)}"
                self.result_label.setText(f"Your aspect ratio is: {ratio}")

            # Calculate missing dimension if one is provided
            if w2 and not h2 and w1 and h1:
                h2 = int((h1 / w1) * w2)
                self.h2_input.setValue(h2)
            elif h2 and not w2 and w1 and h1:
                w2 = int((w1 / h1) * h2)
                self.w2_input.setValue(w2)

        except ValueError as e:
            self.result_label.setText(f"Error: Please enter valid numbers")

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def set_common_ratio(self, index):
        ratio_text = self.ratio_combo.currentText()
        match = re.search(r'(\d+)\s*x\s*(\d+)', ratio_text)
        if match:
            width, height = map(int, match.groups())
            self.w1_input.setValue(width)
            self.h1_input.setValue(height)
            self.calculate_ratio()
        else:
            self.result_label.setText("Error: Could not parse the selected ratio")

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        for file_path in files:
            try:
                with Image.open(file_path) as img:
                    width, height = img.size
                    self.w1_input.setValue(width)
                    self.h1_input.setValue(height)
                    self.calculate_ratio()
                    
                    # Create thumbnail
                    img.thumbnail((100, 100))
                    img_byte_arr = io.BytesIO()
                    img.save(img_byte_arr, format='PNG')
                    img_byte_arr = img_byte_arr.getvalue()
                    
                    pixmap = QPixmap()
                    pixmap.loadFromData(img_byte_arr)
                    self.thumbnail_label.setPixmap(pixmap)
                    
                    self.drop_label.setText("Image loaded")
                    break  # Process only the first image
            except Exception as e:
                self.drop_label.setText(f"Error loading image")
                self.thumbnail_label.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = AspectRatioCalculator()
    calc.show()
    sys.exit(app.exec())