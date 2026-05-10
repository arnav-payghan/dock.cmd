from rich.console import Console
import pygetwindow as gw
import pyautogui
import win32gui

console = Console()

IGNORED_KEYWORDS = [
    "powershell",
    "command prompt",
    "cmd.exe",
    "terminal",
    "windows terminal",
    "python",

    "program manager",
    "windows input experience",
    "task switching",
    "search",
    "widgets",
    "notification center",
    "settings"
]

def get_valid_windows():
    windows = []

    def enum_handler(hwnd, _):
        try:
            # only actual visible windows
            if not win32gui.IsWindowVisible(hwnd):
                return

            title = win32gui.GetWindowText(hwnd)

            if not title:
                return

            lower_title = title.lower()

            # ignore terminal/system windows
            if any(
                keyword in lower_title
                for keyword in IGNORED_KEYWORDS
            ):
                return

            print(f"Detected: {title}")

            # convert hwnd -> PyGetWindow object
            window_obj = gw.Win32Window(hwnd)

            windows.append(window_obj)

        except Exception:
            pass

    win32gui.EnumWindows(enum_handler, None)

    return windows

def stack_windows():
    windows = get_valid_windows()

    if not windows:
        console.print("[bold red]E500:[/bold red] No valid windows found to stack.\n")
        return 
    
    screen_width, screen_height = pyautogui.size()

    count = len(windows)

    # 1 window
    if count == 1:
        w = windows[0]
        w.moveTo(0, 0)
        w.resizeTo(screen_width, screen_height)
        w.activate()

    # 2 windows
    elif count == 2:
        width = screen_width // 2

        positions = [
            (0, 0),
            (width, 0)
        ]

        for window, (x, y) in zip(windows, positions):
            window.restore()
            window.moveTo(x, y)
            window.resizeTo(width, screen_height)
            window.activate()

    # 3 windows        
    elif count == 3:
        left_width = screen_width // 2
        right_width = screen_width // 2
        right_height = screen_height // 2

        windows[0].restore()
        windows[0].moveTo(0, 0)
        windows[0].resizeTo(left_width, screen_height)
        windows[0].activate()

        windows[1].restore()
        windows[1].moveTo(left_width, 0)
        windows[1].resizeTo(right_width, right_height)
        windows[1].activate()

        windows[2].restore()
        windows[2].moveTo(left_width, right_height)
        windows[2].resizeTo(right_width, right_height)
        windows[2].activate()

    # 4 windows
    elif count == 4:
        width = screen_width // 2
        height = screen_height // 2

        positions = [
            (0, 0),
            (width, 0),
            (0, height),
            (width, height)
        ]

        for window, (x, y) in zip(windows, positions):
            window.moveTo(x, y)
            window.resizeTo(width, height)
    else:
        console.print(
            f"[bold red]E501:[/bold red] Too many windows to stack.\n"
            f"Found {count} valid windows.\n"
        )
        return

    console.print(f"[bold green]S001:[/bold green] Stacked [bold cyan]{min(count, 4)}[/bold cyan] windows.\n")