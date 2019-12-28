import gui
import settings
import sys





#==============Initializations==============#
settings.init()

#==================GUI======================#

app = gui.QApplication(sys.argv)

window = gui.MainWindow(gui.sceneMaze())
window.resize(gui.QScreen().availableGeometry().size())

window.ui.graphicsView.setScene(window.scene)
window.ui.graphicsView.centerOn(10,0)

window.showMaximized()

sys.exit(app.exec_())













