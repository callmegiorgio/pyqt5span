import sys
from PyQt5     import QtCore, QtGui, QtWidgets
from pyqt5span import QSpanTableView

def main() -> int:
    a = QtWidgets.QApplication([])
    w = QtWidgets.QWidget()
    vbox = QtWidgets.QVBoxLayout()
    
    model = QtGui.QStandardItemModel()

    @QtCore.pyqtSlot()
    def onAddRowButtonClicked():
        model.appendRow([])

        if model.rowCount() == 4:
            view.spanHeaderView(QtCore.Qt.Orientation.Vertical).setSpan(1, 2)
    
    @QtCore.pyqtSlot()
    def onAddColumnButtonClicked():
        model.appendColumn([])
        
        if model.columnCount() == 3:
            view.spanHeaderView(QtCore.Qt.Orientation.Horizontal).setSpan(0, 3)

    add_row_btn = QtWidgets.QPushButton('Add Row')
    add_row_btn.clicked.connect(onAddRowButtonClicked)

    add_column_btn = QtWidgets.QPushButton('Add Column')
    add_column_btn.clicked.connect(onAddColumnButtonClicked)

    # Top layout
    hbox = QtWidgets.QHBoxLayout()
    hbox.addWidget(add_row_btn)
    hbox.addWidget(add_column_btn)

    view = QSpanTableView()

    vbox.addLayout(hbox)
    vbox.addWidget(view)
    w.setLayout(vbox)

    view.setModel(model)

    w.resize(800, 600)
    w.show()

    return a.exec()

if __name__ == '__main__':
    sys.exit(main())