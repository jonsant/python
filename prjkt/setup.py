import cx_Freeze

executables = [cx_Freeze.Executable("game.py", base = "Win32GUI")]

cx_Freeze.setup(
    name="Prjkt",
    options={"build_exe": {"packages":["pygame"], "include_files": ["images/tank1.png","images/tank2.png","images/menu_bg.png","images/settings_button.png","images/play_button.png","images/quit_button.png","images/standard_bullet.png","images/plane.png","images/heart.png","images/commie.png","images/bg.jpg", "images/meds.png", "images/settings_bg.png", "images/commie_bg.jpg", "images/bomb.png", "images/bomb_icon.png", "images/door.png", "images/door_1.png", "images/door_2.png", "images/door_3.png", "images/door_4.png", "images/ruined_door.png", "images/diamond.png", "images/missile.png", "images/meds.png", "images/regularExplosion00.png", "images/regularExplosion01.png", "images/regularExplosion02.png","images/regularExplosion03.png","images/regularExplosion04.png","images/regularExplosion05.png","images/regularExplosion06.png","images/regularExplosion07.png","images/regularExplosion08.png", "images/wall_trigger.png", "images/wall3_5.png", "images/wall3_4.png", "images/wall3_3.png", "images/wall3_2.png", "images/wall3_1.png", "images/ruined_wall.png", "images/is_commie.png", "images/is_commie2.png", "controller.txt", "blip.wav", "button.wav", "commie.mp3", "flirp.wav", "hit.wav", "missile.wav", "pause.wav", "plane.wav", "robot.wav", "shoot.wav", "song.mp3", "bomb_explosion.wav", "door.wav", "explode.wav", "victory.wav"]}},
    executables = executables

)