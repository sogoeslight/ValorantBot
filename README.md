# Valorant bot

### Features!
- Done:
    - Anti-afk simulation!
    - Relaunches game in case of error and continues working!
    - Statistics!
    - ...
    - Goes well with pizza!
- Coming soon:
    - Timer
    - Handling updates
    - Support of different game modes
    - Support of different screen resolutions
    - Trigger bot
    - App interface
    - Special mode "Bilbo Teabaggins"


Supposed only for Deathmatches
Currently supports only FullHD and QHD screens

---

## Requirements:
- [Valorant](https://playvalorant.com/en-us/ "https://playvalorant.com/en-us/")
- [Python](https://www.python.org/downloads/ "https://www.python.org/downloads/")
- [PC](https://downloadmoreram.com/ "Go on, do it")
- Screen

## Setup:
1. In bot directory -> command line: `pip install -r requirements.txt`
2. Valorant -> Settings -> Video -> Display Mode: **Windowed**, Resolution - your native resolution, so game should be
on whole screen, but in window
3. If you want script to launch Valorant for you - set `valorant_is_opened` in settings.py to `False`,  
but don't forget that it will open in the last used resolution and display mode!
4. Also, you can adjust `average_valorant_load_time` 
and `average_match_load_time` (settings.py 20 and 21 lines)

## Launch:
From a bot directory > `python bot.py`  

## Hints:
- To stop script press `ctrl+c` in console window
- `alt+enter` shortcut switches Valorant to a windowed mode
- Don't launch it by simply `bot.py`
