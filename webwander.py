import sys
import random
from cefpython3 import cefpython as cef
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QMainWindow, QTabWidget, QWidget
from PyQt5.QtCore import Qt, QTimer


class WebWanderBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window_title = "WebWander"
        self.tabs = []
        self.logged_in = False
        self.sync_complete = False
        self.theme_css = ""
        self.themes = {
            "Actual Gamer Stuff": self.actual_gamer_stuff_theme(),
            "Cyberpunk": self.cyberpunk_theme(),
            "Dark Mode": self.dark_mode_theme(),
            "Retro": self.retro_theme(),
            "Minimalistic": self.minimalistic_theme(),
            "Gamer": self.gamer_theme(),
            "Neon": self.neon_theme()
        }
        self.current_theme = self.themes["Actual Gamer Stuff"]  # Default theme

        self.setWindowTitle(self.window_title)
        self.setGeometry(100, 100, 1200, 800)

        self.browser_widget = QWidget(self)
        self.setCentralWidget(self.browser_widget)

        self.init_ui()

    def init_ui(self):
        # Main layout for the browser window
        layout = QVBoxLayout(self.browser_widget)

        self.tabs_widget = QTabWidget(self)
        layout.addWidget(self.tabs_widget)

        self.add_tab_button = QPushButton("Add Tab", self)
        self.add_tab_button.clicked.connect(self.add_new_tab)
        layout.addWidget(self.add_tab_button)

        self.theme_button = QPushButton("Choose Theme", self)
        self.theme_button.clicked.connect(self.choose_theme)
        layout.addWidget(self.theme_button)

        self.login_button = QPushButton("Login", self)
        self.login_button.clicked.connect(self.login_dialog)
        layout.addWidget(self.login_button)

        self.default_browser_button = QPushButton("Set as Default Browser", self)
        self.default_browser_button.clicked.connect(self.set_as_default_browser)
        layout.addWidget(self.default_browser_button)

        self.quit_button = QPushButton("Quit", self)
        self.quit_button.clicked.connect(self.quit_app)
        layout.addWidget(self.quit_button)

        # Show the main window
        self.show()

    def add_new_tab(self):
        """Add a new tab to the browser."""
        url = "https://www.example.com"  # Default URL to load
        self.create_browser(url)

    def create_browser(self, url):
        """Create a new browser with a given URL."""
        browser = cef.CreateBrowserSync(url=url, window_title=self.window_title)
        self.tabs.append(browser)

        tab_widget = QWidget(self)
        tab_layout = QVBoxLayout(tab_widget)
        tab_label = QLabel(f"Tab {len(self.tabs)} - {url}", self)
        tab_layout.addWidget(tab_label)
        self.tabs_widget.addTab(tab_widget, f"Tab {len(self.tabs)}")

    def set_as_default_browser(self):
        """Set the application as the default browser in Windows."""
        if sys.platform == "win32":
            app_path = sys.executable
            app_name = "WebWanderBrowser"

            try:
                reg_path = r"Software\Classes\http\shell\open\command"
                reg_key = app_name
                reg_value = f'"{app_path}" -- "%1"'
                
                import winreg as reg
                registry = reg.ConnectRegistry(None, reg.HKEY_CURRENT_USER)
                key = reg.CreateKey(registry, reg_path)
                reg.SetValueEx(key, reg_key, 0, reg.REG_SZ, reg_value)
                reg.CloseKey(key)

                print(f"Successfully set WebWander as the default browser.")
            except Exception as e:
                print(f"Error setting default browser: {e}")

    def login_dialog(self):
        """Display a login dialog for the user to log in to Google."""
        dialog = QDialog(self)
        dialog.setWindowTitle("Login to WebWander")
        dialog.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        label = QLabel("Login to WebWander (Optional Google Login)", self)
        layout.addWidget(label)

        username_input = QLineEdit(self)
        username_input.setPlaceholderText("Enter your email (Optional)")
        layout.addWidget(username_input)

        password_input = QLineEdit(self)
        password_input.setPlaceholderText("Enter your password (Optional)")
        password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(password_input)

        login_button = QPushButton("Login", self)
        skip_button = QPushButton("Skip Login", self)
        layout.addWidget(login_button)
        layout.addWidget(skip_button)

        login_button.clicked.connect(lambda: self.handle_login(username_input.text(), password_input.text(), dialog))
        skip_button.clicked.connect(lambda: self.skip_login(dialog))

        dialog.setLayout(layout)
        dialog.exec_()

    def handle_login(self, email, password, dialog):
        """Simulate handling login and syncing."""
        if email and password:
            self.logged_in = True
            self.sync_complete = True  # Simulate syncing extensions and bookmarks
            dialog.accept()
            print(f"Logged in as {email}. Syncing your settings...")

    def skip_login(self, dialog):
        """Skip the login process."""
        self.logged_in = False
        self.sync_complete = False
        dialog.accept()
        print("Skipping login, starting the browser with default settings.")

    def choose_theme(self):
        """Allow the user to select a custom theme file (CSS)."""
        options = QFileDialog.Options()
        theme_file, _ = QFileDialog.getOpenFileName(self, "Choose a Theme", "", "CSS Files (*.css);;All Files (*)", options=options)
        if theme_file:
            with open(theme_file, 'r') as file:
                self.theme_css = file.read()
            print(f"Theme applied from {theme_file}")

    def actual_gamer_stuff_theme(self):
        return """
        body {
            background: linear-gradient(135deg, #111111, #181818);
            color: #f8f8f8;
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            overflow: hidden;
        }

        h1 {
            font-size: 50px;
            color: #ff4e00;
            text-shadow: 0 0 20px rgba(255, 78, 0, 0.8), 0 0 40px rgba(255, 78, 0, 0.6);
        }

        .btn {
            background: #222;
            color: #fff;
            font-size: 18px;
            padding: 15px;
            border-radius: 8px;
            cursor: pointer;
            margin: 10px;
            border: 2px solid transparent;
            box-shadow: 0 0 10px #ff4e00, 0 0 20px #ff4e00;
            transition: all 0.3s ease;
        }

        .btn:hover {
            background-color: #333;
            border-color: #ff4e00;
            box-shadow: 0 0 20px #ff4e00, 0 0 40px #ff4e00;
        }

        .btn:active {
            background-color: #444;
            box-shadow: 0 0 15px #ff4e00;
        }

        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
            padding: 10px;
            color: #f8f8f8;
            font-size: 14px;
            background: #111;
            box-shadow: 0 -2px 8px rgba(0, 0, 0, 0.5);
        }

        .tabs {
            background: #222;
            color: #f0f0f0;
            padding: 10px;
            border-radius: 5px;
            box-shadow: 0 0 15px rgba(255, 78, 0, 0.5);
        }

        .tabs:hover {
            background: #333;
            box-shadow: 0 0 20px rgba(255, 78, 0, 0.5);
        }
        """

    def cyberpunk_theme(self):
        return """
        body {
            background: linear-gradient(135deg, #0f0f0f, #2b2b2b);
            color: #00ff00;
            font-family: 'Press Start 2P', cursive;
            text-align: center;
            margin: 0;
            padding: 0;
        }
        h1 {
            font-size: 50px;
            color: #ff00ff;
            text-shadow: 0 0 10px #ff00ff, 0 0 20px #ff00ff;
        }
        .btn {
            background-color: #333;
            border: 2px solid #00ff00;
            color: #00ff00;
            font-size: 18px;
            padding: 15px;
            border-radius: 8px;
            cursor: pointer;
            margin: 10px;
            box-shadow: 0 0 5px #00ff00;
            transition: 0.3s;
        }
        .btn:hover {
            background-color: #444;
            box-shadow: 0 0 10px #ff00ff;
        }
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
            padding: 10px;
            color: #f0f0f0;
            font-size: 14px;
            background: #111;
            box-shadow: 0 -2px 8px rgba(0, 0, 0, 0.5);
        }
        """
# To use the theme, just run the browser and it will apply the "Actual Gamer Stuff" theme by default.
