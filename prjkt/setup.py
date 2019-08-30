import cx_Freeze

executables = [cx_Freeze.Executable("game.py", base = "Win32GUI")]

cx_Freeze.setup(
    name="Prjkt",
    options={"build_exe": {"packages":["pygame"], "include_files": ["images/tank1.png","images/tank2.png","images/menu_bg.png","images/settings_button.png","images/play_button.png","images/quit_button.png","images/standard_bullet.png","images/plane.png","images/heart.png","images/commie.png","images/bg.jpg","images/settings_bg.png", "controller.txt"]}},
    executables = executables

)