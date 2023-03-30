import sys
from PyQt5     import QtCore, QtGui, QtWidgets
from pyqt5span import QSpanTableView

def main() -> int:
    a = QtWidgets.QApplication([])
    w = QtWidgets.QWidget()
    w.setLayout(QtWidgets.QVBoxLayout())
    view = QSpanTableView()
    w.layout().addWidget(view)

    model = QtGui.QStandardItemModel()

    for i in range(10):
        items = []

        for j in range(10):
            items.append(QtGui.QStandardItem(f"item({i},{j})"))

        model.appendRow(items)
    
    view.setModel(model)

    # Horizontal header settings.
    hheader = view.spanHeaderView(QtCore.Qt.Orientation.Horizontal)

    hheader.setSpan(0, 1)
    hheader.setSpan(1, 2)
    hheader.setSpan(3, 3)
    hheader.setSpan(6, 4)

    hheader.setSectionLabel(0, "section1")
    hheader.setSectionLabel(1, "section2")
    hheader.setSectionLabel(3, "section3")
    hheader.setSectionLabel(6, "section4")

    hheader.setSectionBackgroundColor(0, QtGui.QColor(QtCore.Qt.GlobalColor.cyan))
    hheader.setSectionForegroundColor(0, QtGui.QColor(QtCore.Qt.GlobalColor.blue))
    
    # Vertical header settings.
    vheader = view.spanHeaderView(QtCore.Qt.Orientation.Vertical)
    
    vheader.setSpan(0, 4)
    vheader.setSpan(4, 3)
    vheader.setSpan(7, 2)
    vheader.setSpan(9, 1)

    vheader.setSectionLabel(0, "section1")
    vheader.setSectionLabel(4, "section2")
    vheader.setSectionLabel(7, "section3")
    vheader.setSectionLabel(9, "section4")
    
    w.resize(800, 600)
    w.show()

    return a.exec()

if __name__ == '__main__':
    sys.exit(main())