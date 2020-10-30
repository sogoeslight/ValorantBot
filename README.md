# Valorant bot

### Features! (v1.11 compatible :heavy_check_mark:)
- Done:
    - Anti-afk simulation!
    - Relaunches game in case of error and continues working!
    - Handles updates too!
    - Statistics!
    - 0 bans since since beginning of September!
    - ...
    - Goes well with pizza!
- Coming soon:
    - Timer
    - Support of different game modes
    - Trigger bot
    - App interface
    - Special mode "Bilbo Teabaggins"


Supposed only for Deathmatches  
Currently supports FullHD and QHD screens

---

## Requirements:
- [Valorant](https://playvalorant.com/en-us/ "https://playvalorant.com/en-us/")
- [Python v3.7.9*](https://www.python.org/downloads/ "https://www.python.org/downloads/release/python-379/") 
(Was tested with Python v3.7.9 and v3.8.5)  
[Direct link for Windows 10 installer*](https://www.python.org/ftp/python/3.7.9/python-3.7.9-amd64.exe)  
*Do not forget to check "Add Python to PATH"
- [PC](https://downloadmoreram.com/ "Go on, do it")
- Screen

## Setup:
0. [**Download latest release**](https://github.com/sogoeslight/ValorantBot/archive/1.3.zip) and unzip it anywhere
1. Make sure you have python installed
2. Launch -> Installer.bat
3. Valorant -> Settings -> Video -> Display Mode: **Windowed**;  
Resolution: your native resolution, so game should be on whole screen, but in window  
### Additional:
- If you want script to launch Valorant for you - set `valorant_is_opened` in /scripts/settings.py to `False`,  
but don't forget that it will open in the last used resolution and display mode!
- Also, you can adjust `average_valorant_load_time` 
and `average_match_load_time` (/scripts/settings.py 20 and 21 lines)

## Launch:
0. Launch -> Launcher.bat

## Hints:
- Press `ctrl+c` in console window to stop bot
- Launching it by simply `bot.py` may cause unpredictable errors

Since bot is graphically-based, if anything doesn't work for you - try next graphic quality settings:
- Everything: High
- Vignette: On
- Anti-Aliasing: MSAA 4x
- Anisotropic Filtering: 8x
- Improve Clarity: Off
- Experimental Sharpening: Off
- Bloom: On
- Distortion: On 

### Contacts:
[E-mail](mailto:SoGoesLight@gmail.com)