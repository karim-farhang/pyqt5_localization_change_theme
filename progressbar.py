from PyQt5 import QtCore, QtWidgets, uic
import sys
import time


class MainWindows(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        self.ui = uic.loadUi('progress.ui', self)
        self.resize(888, 200)

        # Button and Progress Bar for Task 1
        self.btn_start_1 = self.findChild(QtWidgets.QPushButton, 'btn_start_1')
        self.btn_stop_1 = self.findChild(QtWidgets.QPushButton, 'btn_stop_1')
        self.prog_1 = self.findChild(QtWidgets.QProgressBar, 'prog_1')
        self.lbl_1 = self.findChild(QtWidgets.QLabel, 'lbl_1')

        # Connect buttons to actions
        self.btn_start_1.clicked.connect(self.start_task)
        self.btn_stop_1.clicked.connect(self.stop_task)

        self.worker = None

    def start_task(self):
        if self.worker and self.worker.isRunning():
            return  # Don't start if already running

        self.worker = Worker()
        self.worker.progress_updated.connect(self.update_ui)
        self.worker.task_done.connect(self.on_done)
        self.worker.start()

    def stop_task(self):
        if self.worker and self.worker.isRunning():
            self.worker.terminate()
            self.worker.wait()
            self.lbl_1.setText("Stopped")
            self.prog_1.setValue(0)

    def update_ui(self, value, remaining_time):
        self.prog_1.setValue(value)
        self.lbl_1.setText(f"{value}% - {remaining_time} sec left")

    def on_done(self):
        self.lbl_1.setText("Done!")


class Worker(QtCore.QThread):
    progress_updated = QtCore.pyqtSignal(int, int)  # value, remaining_time
    task_done = QtCore.pyqtSignal()

    def run(self):
        total = 100
        start = time.time()
        for i in range(total + 1):
            elapsed = time.time() - start
            remaining = int((elapsed / i) * (total - i)) if i > 0 else 0
            time.sleep(0.05)
            self.progress_updated.emit(i, remaining)
        self.task_done.emit()


def main():
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindows()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
