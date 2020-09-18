# Valorant bot

### Features!
- Done:
    - Anti-afk simulation!
    - Relaunches game in case of error and continues working!
    - ...
    - Goes well with pizza!
- Coming soon:
    - Statistics
    - Timer
    - Handling updates
    - Support of different game modes
    - Support of different screen resolutions
    - Trigger bot
    - App interface
    - Special mode "Bilbo Teabaggins"


Currently supposed only for Deathmatches

---

## Requirements:
- [Valorant](https://playvalorant.com/en-us/ "https://playvalorant.com/en-us/")
- [Python](https://www.python.org/downloads/ "https://www.python.org/downloads/")
- [PC](https://downloadmoreram.com/ "Go on, do it")
- Screen

## Setup:
1. In bot directory -> command line: `pip install -r requirements.txt`
2. Valorant -> Settings -> Video -> Display Mode: **Windowed**, Resolution: **1920 x 1080 16:9**
3. If you have a different monitor resolution - put game window into the left top corner
4. If you want script to launch Valorant for you - set `valorant_is_opened` in settings.py to `False`,  
but don't forget that it will open in the last used resolution and display mode!
5. Also, is recommended to adjust `average_valorant_load_time` 
and `average_match_load_time` (settings.py 11 and 12 lines)

## Launch:
From a bot directory > `python bot.py`  

## Hints:
- To stop script press `ctrl+c` in console window
- `alt+enter` shortcut switches Valorant to a windowed mode
- Don't launch it by simply `bot.py`
