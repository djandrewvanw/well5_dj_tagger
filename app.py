import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton
)
from PyQt5.QtCore import Qt


class Well5DJTagger(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("well5_dj_tagger")
        self.setGeometry(100, 100, 1200, 700)

        main = QWidget()
        self.setCentralWidget(main)

        layout = QHBoxLayout()
        main.setLayout(layout)

        # tabela biblioteki
        self.table = QTableWidget()
        self.table.setColumnCount(7)

        self.table.setHorizontalHeaderLabels([
            "★",
            "Title",
            "Artist",
            "Album",
            "Year",
            "Genre",
            "Event Type"
        ])

        self.table.setRowCount(5)

        for row in range(5):
            for col in range(7):
                self.table.setItem(
                    row,
                    col,
                    QTableWidgetItem("")
                )

        layout.addWidget(self.table, 3)

        # prawy panel
        right = QVBoxLayout()

        cover = QLabel("COVER ART")
        cover.setAlignment(Qt.AlignCenter)
        cover.setFixedSize(250,250)
        cover.setStyleSheet(
            "border: 1px solid gray;"
        )

        right.addWidget(cover)

        self.info = QLabel(
            "Title:\n"
            "Artist:\n"
            "Year:\n"
            "Genre:"
        )

        right.addWidget(self.info)

        play = QPushButton("▶ Play")

        right.addWidget(play)

        layout.addLayout(right)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Well5DJTagger()
    window.show()

    sys.exit(app.exec_())
