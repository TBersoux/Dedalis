import gui
import globals
import sys





#==============Initializations==============#
globals.init()

#==================GUI======================#

app = gui.QApplication(sys.argv)

window = gui.MainWindow()
window.resize(gui.QScreen().availableGeometry().size())

window.ui.graphicsView.setScene(window.scene)
window.ui.graphicsView.centerOn(10,0)

window.showMaximized()

sys.exit(app.exec_())













