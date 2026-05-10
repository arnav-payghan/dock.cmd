from rich.console import Console
import pygetwindow as gw
import pyautogui

console = Console()

IGNORED_KEYWORDS = [
    "powershell",
    "command prompt",
    "cmd.exe",
    "terminal",
    "windows terminal",
    "dock.cmd",
    "python"
]

def get_valid_windows():
    windows = []

    for window in gw.getAllWindows():
        title = window.title.strip().lower()
        if not title:
            continue
        if window.isMinimized:
            continue
        if any(keyword in title for keyword in IGNORED_KEYWORDS):
            continue

        windows.append(window)

    return windows

def stack_windows():
    windows = get_valid_windows()

    if not windows:
        console.print("[bold red]E500:[/bold red] No valid windows found to stack.")
        return 
    
    screen_width, screen_height = pyautogui.size()

    count = len(windows)

    if count == 1:
        w = windows[0]
        w.moveTo(0, 0)
        w.resizeTo(screen_width, screen_height)
    elif count == 2:
        width = screen_width // 2

        positions = [
            (0, 0),
            (width, 0)
        ]

        for window, (x, y) in zip(windows, positions):
            window.moveTo(x, y)
            window.resizeTo(width, screen_height)
    elif count == 3:
        width = screen_width // 2
        height = screen_height // 2

        positions = [
            (0, 0),
            (width, 0),
            (0, height)
        ]

        for window, (x, y) in zip(windows, positions):
            window.moveTo(x, y)
            window.resizeTo(width, height)
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
        console.print(f"[bold red]E501:[/bold red] Too many windows to stack. Found [bold cyan]{count}[bold cyan] valid windows, but can only stack up to 4.")

    console.print(f"[bold green]S001:[/bold green] Stacked [bold cyan]{min(count, 4)}[/bold cyan] windows.")