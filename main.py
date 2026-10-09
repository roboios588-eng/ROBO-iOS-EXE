import tkinter as tk
from tkinter import messagebox
import random
import math

APP_NAME = "ROBO iOS"
BG = "#07111f"
PANEL = "#0b1b30"
PANEL2 = "#102641"
BLUE = "#168cff"
CYAN = "#55d7ff"
TEXT = "#e8f5ff"
MUTED = "#8da9c7"

class RoboApp:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_NAME)
        self.root.geometry("920x590")
        self.root.minsize(820, 520)
        self.root.configure(bg=BG)
        self.logged_in = False
        self.page = "Aimbot"
        self.particles = []
        self._build_background()
        self._show_login()

    def _build_background(self):
        self.canvas = tk.Canvas(self.root, bg=BG, highlightthickness=0)
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)
        for _ in range(75):
            x = random.randint(0, 920)
            y = random.randint(0, 590)
            r = random.choice([1, 1, 2])
            item = self.canvas.create_oval(x-r, y-r, x+r, y+r, fill=random.choice(["#174a77", "#176aa2", "#49bfff"]), outline="")
            self.particles.append({
                "id": item, "x": x, "y": y, "r": r,
                "speed": random.uniform(0.5, 2.1),
                "drift": random.uniform(-0.55, 0.55)
            })
        self._animate_particles()
        self.root.bind("<Configure>", self._resize_canvas)

    def _resize_canvas(self, event):
        if event.widget is self.root:
            self.canvas.configure(width=event.width, height=event.height)

    def _animate_particles(self):
        try:
            w = max(self.canvas.winfo_width(), 1)
            h = max(self.canvas.winfo_height(), 1)
            for p in self.particles:
                p["x"] += p["drift"]
                p["y"] += p["speed"]
                if p["y"] > h + 5:
                    p["y"] = -5
                    p["x"] = random.randint(0, w)
                if p["x"] < -5:
                    p["x"] = w + 5
                elif p["x"] > w + 5:
                    p["x"] = -5
                r = p["r"]
                self.canvas.coords(p["id"], p["x"]-r, p["y"]-r, p["x"]+r, p["y"]+r)
            self.root.after(35, self._animate_particles)
        except tk.TclError:
            pass

    def _clear_ui(self):
        for widget in getattr(self, "ui_widgets", []):
            try: widget.destroy()
            except tk.TclError: pass
        self.ui_widgets = []

    def _track(self, widget):
        self.ui_widgets.append(widget)
        return widget

    def _show_login(self):
        self._clear_ui()
        frame = self._track(tk.Frame(self.root, bg=PANEL, highlightbackground="#174a77", highlightthickness=1))
        frame.place(relx=.5, rely=.5, anchor="center", width=360, height=360)
        tk.Label(frame, text="ROBO iOS", bg=PANEL, fg=CYAN, font=("Segoe UI", 25, "bold")).pack(pady=(32, 4))
        tk.Label(frame, text="SECURE DESKTOP PANEL", bg=PANEL, fg=MUTED, font=("Segoe UI", 9, "bold")).pack(pady=(0, 24))
        tk.Label(frame, text="Username", bg=PANEL, fg=TEXT, font=("Segoe UI", 10)).pack(anchor="w", padx=35)
        user = tk.Entry(frame, bg="#06101d", fg=TEXT, insertbackground=TEXT, relief="flat", font=("Segoe UI", 11))
        user.pack(fill="x", padx=35, ipady=9, pady=(5, 15))
        user.insert(0, "shafayy")
        tk.Label(frame, text="Password", bg=PANEL, fg=TEXT, font=("Segoe UI", 10)).pack(anchor="w", padx=35)
        pw = tk.Entry(frame, show="•", bg="#06101d", fg=TEXT, insertbackground=TEXT, relief="flat", font=("Segoe UI", 11))
        pw.pack(fill="x", padx=35, ipady=9, pady=(5, 20))
        pw.insert(0, "1")
        def login():
            if user.get().strip() == "shafayy" and pw.get() == "1":
                self.logged_in = True
                self._show_dashboard(user.get().strip())
            else:
                messagebox.showerror("Login Failed", "Incorrect username or password.")
        tk.Button(frame, text="LOGIN  →", command=login, bg=BLUE, fg="white", activebackground=CYAN, activeforeground=BG, relief="flat", cursor="hand2", font=("Segoe UI", 10, "bold")).pack(fill="x", padx=35, ipady=10)
        tk.Label(frame, text="Demo credentials: shafayy / 1", bg=PANEL, fg=MUTED, font=("Segoe UI", 8)).pack(pady=14)

    def _show_dashboard(self, username):
        self._clear_ui()
        shell = self._track(tk.Frame(self.root, bg=BG))
        shell.place(x=16, y=16, relwidth=1, relheight=1, width=-32, height=-32)
        shell.pack_propagate(False)
        # Use place for a stable compact layout over animated background.
        sidebar = tk.Frame(shell, bg="#081626", width=190, highlightbackground="#123958", highlightthickness=1)
        sidebar.pack(side="left", fill="y", padx=(0, 12))
        sidebar.pack_propagate(False)
        tk.Label(sidebar, text="ROBO  /  iOS", bg="#081626", fg=CYAN, font=("Segoe UI", 16, "bold")).pack(pady=(24, 2))
        tk.Label(sidebar, text="CONTROL CENTER", bg="#081626", fg=MUTED, font=("Segoe UI", 8, "bold")).pack(pady=(0, 24))
        for name, glyph in [("Aimbot","◎"),("ESP","◈"),("Brutal Features","✦"),("Settings","⚙"),("About","ⓘ")]:
            tk.Button(sidebar, text=f"  {glyph}   {name}", anchor="w", command=lambda n=name: self._page(n), bg="#10243a", fg=TEXT, activebackground=BLUE, activeforeground="white", relief="flat", cursor="hand2", font=("Segoe UI", 10, "bold"), padx=12, pady=10).pack(fill="x", padx=12, pady=4)
        tk.Button(sidebar, text="LOG OUT", command=self._show_login, bg="#14283d", fg="#ff9eb1", activebackground="#5c2032", relief="flat", cursor="hand2", font=("Segoe UI", 9, "bold")).pack(side="bottom", fill="x", padx=12, pady=18)
        content = tk.Frame(shell, bg="#091727", highlightbackground="#123958", highlightthickness=1)
        content.pack(side="left", fill="both", expand=True)
        self.content = content
        self.username = username
        self._page("Aimbot")

    def _page(self, name):
        self.page = name
        for child in self.content.winfo_children():
            child.destroy()
        header = tk.Frame(self.content, bg="#091727")
        header.pack(fill="x", padx=24, pady=(22, 12))
        tk.Label(header, text=name.upper(), bg="#091727", fg=CYAN, font=("Segoe UI", 19, "bold")).pack(side="left")
        tk.Label(header, text=f"USER  {self.username.upper()}", bg="#091727", fg=MUTED, font=("Segoe UI", 9, "bold")).pack(side="right", pady=8)
        tk.Frame(self.content, bg="#174a77", height=1).pack(fill="x", padx=24, pady=(0, 18))
        body = tk.Frame(self.content, bg="#091727")
        body.pack(fill="both", expand=True, padx=24, pady=(0, 22))
        if name == "Aimbot":
            self._section(body, "AIM SETTINGS", ["Aim Silent", "Aim Vector", "Aim Legend", "Aim Kill"])
            self._section(body, "TARGET SELECTION", ["Head", "Body", "Head (Front)", "Body (Front)", "Chest"], radio=True)
            tk.Label(body, text="FO / FOV SIZE", bg="#091727", fg=TEXT, font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(14, 4))
            scale = tk.Scale(body, from_=1, to=300, orient="horizontal", bg="#091727", fg=CYAN, troughcolor="#153a5d", highlightthickness=0, activebackground=BLUE, length=360)
            scale.set(90); scale.pack(anchor="w")
        elif name == "ESP":
            self._section(body, "VISUAL OPTIONS", ["Health", "Name", "Line", "Box", "Target", "Skeleton", "Distance"])
        elif name == "Brutal Features":
            self._section(body, "DEMO FEATURES", ["Magnet Light", "Down Player", "Enemy Player Fly", "Feature Preview"])
            tk.Label(body, text="These are UI demo toggles only; no game interaction is implemented.", bg="#091727", fg=MUTED, font=("Segoe UI", 9)).pack(anchor="w", pady=12)
        elif name == "Settings":
            self._info_card(body, "ACCOUNT", f"Username: {self.username}\nSubscription: Basic Demo\nStatus: Active demo\nExpiry: Not connected to a subscription server")
            self._info_card(body, "DEVICE", f"Operating system: {self.root.tk.call('tk', 'windowingsystem').title()}\nWindow: Compact desktop UI\nBackground: Animated blue particles")
            tk.Button(body, text="CHECK FOR UPDATES", command=lambda: messagebox.showinfo("Updates", "This demo has no update server configured."), bg=BLUE, fg="white", relief="flat", padx=18, pady=9).pack(anchor="w", pady=8)
        else:
            self._info_card(body, "ABOUT ROBO iOS", "Glass-style desktop UI demo\nBlue neon controls and animated particles\nBuilt as a starter project for Windows EXE packaging.")
            tk.Label(body, text="No game manipulation or anti-cheat bypass is included.", bg="#091727", fg=MUTED, font=("Segoe UI", 9)).pack(anchor="w", pady=8)

    def _section(self, parent, title, items, radio=False):
        card = tk.Frame(parent, bg=PANEL, highlightbackground="#153b5e", highlightthickness=1)
        card.pack(fill="x", pady=6)
        tk.Label(card, text=title, bg=PANEL, fg=CYAN, font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=15, pady=(12, 8))
        inner = tk.Frame(card, bg=PANEL)
        inner.pack(fill="x", padx=12, pady=(0, 12))
        if radio:
            var = tk.StringVar(value="Head")
            for item in items:
                tk.Radiobutton(inner, text=item, variable=var, value=item, bg=PANEL, fg=TEXT, selectcolor="#123858", activebackground=PANEL, activeforeground=CYAN, font=("Segoe UI", 9)).pack(side="left", padx=4)
        else:
            for i, item in enumerate(items):
                var = tk.BooleanVar(value=False)
                tk.Checkbutton(inner, text=item, variable=var, bg=PANEL, fg=TEXT, selectcolor="#123858", activebackground=PANEL, activeforeground=CYAN, font=("Segoe UI", 9), padx=5).grid(row=i//3, column=i%3, sticky="w", padx=4, pady=3)

    def _info_card(self, parent, title, content):
        card = tk.Frame(parent, bg=PANEL, highlightbackground="#153b5e", highlightthickness=1)
        card.pack(fill="x", pady=7)
        tk.Label(card, text=title, bg=PANEL, fg=CYAN, font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=15, pady=(12, 5))
        tk.Label(card, text=content, justify="left", bg=PANEL, fg=TEXT, font=("Segoe UI", 10)).pack(anchor="w", padx=15, pady=(0, 14))

if __name__ == "__main__":
    root = tk.Tk()
    app = RoboApp(root)
    root.mainloop()
