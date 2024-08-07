import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QSlider, QLabel, QVBoxLayout, QHBoxLayout, 
                             QPushButton, QFileDialog, QFrame, QSplitter)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage, QFont
from PIL import Image, ImageEnhance

class ImageEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.image = None
        self.original_image = None

    def initUI(self):
        self.setWindowTitle('圖像編輯器')
        self.setGeometry(100, 100, 1000, 600)
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
                color: #333;
            }
            QSlider::groove:horizontal {
                border: 1px solid #999999;
                height: 8px;
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);
                margin: 2px 0;
            }
            QSlider::handle:horizontal {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);
                border: 1px solid #5c5c5c;
                width: 18px;
                margin: -2px 0;
                border-radius: 3px;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px 20px;
                text-align: center;
                font-size: 16px;
                margin: 4px 2px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)

        main_layout = QHBoxLayout()
        
        # 左側控制面板
        control_widget = QWidget()
        control_layout = QVBoxLayout(control_widget)
        control_layout.setContentsMargins(20, 20, 20, 20)
        control_layout.setSpacing(15)

        title_label = QLabel('')
        title_label.setFont(QFont('Arial', 60, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        control_layout.addWidget(title_label)

        # 創建滑塊
        self.sliders = {}
        for name in ['曝光度', '對比度', '飽和度', '暗部', '亮部', '銳利化']:
            slider = QSlider(Qt.Horizontal)
            if name == '銳利化':
                slider.setRange(0, 500)  # 將銳利化的範圍擴大到 0-500
                slider.setValue(100)  # 默認值保持在 100
            else:
                slider.setRange(0, 200)
                slider.setValue(100)
            slider.valueChanged.connect(self.updateImage)

            slider_layout = QHBoxLayout()
            label = QLabel(name)
            label.setMinimumWidth(60)
            slider_layout.addWidget(label)
            slider_layout.addWidget(slider)

            control_layout.addLayout(slider_layout)
            self.sliders[name] = slider

        # 添加按鈕
        self.loadButton = QPushButton('載入圖片')
        self.loadButton.clicked.connect(self.loadImage)
        control_layout.addWidget(self.loadButton)

        control_layout.addStretch(1)

        # 右側圖片顯示區域
        self.imageLabel = QLabel()
        self.imageLabel.setAlignment(Qt.AlignCenter)
        self.imageLabel.setStyleSheet("""
            QLabel {
                background-color: white;
                border: 2px solid #cccccc;
            }
        """)

        # 使用QSplitter來允許調整左右兩側的寬度
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(control_widget)
        splitter.addWidget(self.imageLabel)
        splitter.setSizes([300, 700])  # 設置初始寬度比例

        main_layout.addWidget(splitter)
        self.setLayout(main_layout)

    def loadImage(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "選擇圖片", "", "圖片文件 (*.png *.jpg *.bmp)")
        if fileName:
            self.original_image = Image.open(fileName)
            self.image = self.original_image.copy()
            self.updateImageDisplay()

    def updateImage(self):
        if self.original_image:
            self.image = self.original_image.copy()
            
            # 應用編輯
            self.image = ImageEnhance.Brightness(self.image).enhance(self.sliders['曝光度'].value() / 100)
            self.image = ImageEnhance.Contrast(self.image).enhance(self.sliders['對比度'].value() / 100)
            self.image = ImageEnhance.Color(self.image).enhance(self.sliders['飽和度'].value() / 100)
            self.image = ImageEnhance.Brightness(self.image).enhance(self.sliders['暗部'].value() / 100)
            self.image = ImageEnhance.Brightness(self.image).enhance(self.sliders['亮部'].value() / 100)
            
            # 強化銳利化效果
            sharpness_factor = (self.sliders['銳利化'].value() / 100) ** 2
            self.image = ImageEnhance.Sharpness(self.image).enhance(sharpness_factor)

            self.updateImageDisplay()

    
    def updateImageDisplay(self):
        if self.image:
            img = self.image.convert("RGBA")
            data = img.tobytes("raw", "RGBA")
            qimage = QImage(data, img.size[0], img.size[1], QImage.Format_RGBA8888)
            
            pixmap = QPixmap.fromImage(qimage)
            
            # 計算縮放比例
            label_size = self.imageLabel.size()
            pixmap_scaled = pixmap.scaled(label_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            
            # 計算居中位置
            x = (label_size.width() - pixmap_scaled.width()) // 2
            y = (label_size.height() - pixmap_scaled.height()) // 2
            
            # 清除之前的內容
            self.imageLabel.clear()
            
            # 設置新的 pixmap
            self.imageLabel.setPixmap(pixmap_scaled)
            
            # 調整 pixmap 在 label 中的位置
            self.imageLabel.setContentsMargins(x, y, x, y)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageEditor()
    ex.show()
    sys.exit(app.exec_())