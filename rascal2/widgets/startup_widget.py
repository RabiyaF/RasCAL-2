from PyQt6 import QtCore, QtGui, QtWidgets

from rascal2.config import path_for


class StartUpWidget(QtWidgets.QWidget):
    """
    The Start Up widget
    """

    _button_style = """background-color: #0D69BB;
                       icon-size: 4em;
                       border-radius : 0.5em;
                       padding: 0.5em;
                       margin-left: 5em;
                       margin-right: 5em;"""

    _label_style = "font-weight: bold; font-size: 1em;"

    def __init__(self, parent):
        """
        Initializes the widget

        Parameters
        ----------
        parent: MainWindowView
                An instance of the MainWindowView
        """
        super().__init__(parent)

        self.create_banner_and_footer()
        self.create_buttons_for_startup_page()
        self.create_labels_for_startup_page()

        self.add_widgets_to_startup_page_layout()

    def add_widgets_to_startup_page_layout(self) -> None:
        """
        Adds the widgets to the startup layout.
        """
        startup_layout = QtWidgets.QVBoxLayout()

        startup_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        startup_layout.setSpacing(50)

        # Add banner
        startup_layout.addStretch(1)
        startup_layout.addWidget(self.banner_label)

        # Add buttons and labels
        for widget in ["button", "label"]:
            layout = QtWidgets.QHBoxLayout()
            for name in ["new_project_", "import_project_", "import_r1_"]:
                layout.addWidget(getattr(self, name + widget))
            startup_layout.addLayout(layout)

        # Add footer
        startup_layout.addWidget(self.footer_label)
        startup_layout.addStretch(1)

        self.setLayout(startup_layout)

    def create_banner_and_footer(self) -> None:
        """
        Creates the banner and footer for the startup page.
        """
        # Create the banner
        self.banner_label = QtWidgets.QLabel(self)
        self.banner_label.setPixmap(QtGui.QPixmap(path_for("banner.png")))
        self.banner_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # Create the footer
        self.footer_label = QtWidgets.QLabel(self)
        self.footer_label.setPixmap(QtGui.QPixmap(path_for("footer.png")))
        self.footer_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

    def toggle_view(self) -> None:
        """
        Shows the project dialog
        """
        self.parent().toggleView()

    def create_buttons_for_startup_page(self) -> None:
        """
        Creates the buttons for the startup page.
        """
        self.new_project_button = QtWidgets.QPushButton(self)
        self.new_project_button.setIcon(QtGui.QIcon(path_for("plus.png")))
        self.new_project_button.clicked.connect(self.toggle_view)
        self.new_project_button.setStyleSheet(self._button_style)

        self.import_project_button = QtWidgets.QPushButton(self)
        self.import_project_button.setIcon(QtGui.QIcon(path_for("open-project-light.png")))
        self.import_project_button.setStyleSheet(self._button_style)

        self.import_r1_button = QtWidgets.QPushButton(self)
        self.import_r1_button.setIcon(QtGui.QIcon(path_for("import-r1.png")))
        self.import_r1_button.setStyleSheet(self._button_style)

    def create_labels_for_startup_page(self) -> None:
        """
        Creates the labels for the startup page.
        """
        self.new_project_label = QtWidgets.QLabel("New\nProject", self)
        self.new_project_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.new_project_label.setStyleSheet(self._label_style)

        self.import_project_label = QtWidgets.QLabel("Import Existing\nProject", self)
        self.import_project_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.import_project_label.setStyleSheet(self._label_style)

        self.import_r1_label = QtWidgets.QLabel("Import R1\nProject", self)
        self.import_r1_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.import_r1_label.setStyleSheet(self._label_style)
