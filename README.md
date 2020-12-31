# Valorant bot

### Features! (v1.14 compatible :heavy_check_mark:)
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
(Please use it as the last non-bugfix version)  
[Direct link for Windows 10 installer*](https://www.python.org/ftp/python/3.7.9/python-3.7.9-amd64.exe)  
*Do not forget to check "Add Python to PATH"
- [PC](https://downloadmoreram.com/ "Go on, do it")
- Screen
- If you are using *Windows 10 Pro **N*** you need to add **Media Feature Pack** by going to  
`Start > Settings > Apps > Apps and features > Optional features > Add a feature`,  
 and then locate Media Feature Pack in the list of available optional features.

## Setup:
0. [**Download latest release**](https://github.com/sogoeslight/ValorantBot/archive/1.41.zip) and unzip it anywhere
1. Make sure you have python installed
2. Execute -> Installer.bat
3. Valorant -> Settings -> General -> Text Language: **English (United States)**
4. Valorant -> Settings -> Video -> Display Mode: **Windowed**;  
Resolution: your native resolution, so game should be on whole screen, but in window  
### Additional:
- If you want script to launch Valorant for you - set `valorant_is_opened` in /scripts/settings.py to `False`,  
but don't forget that it will open in the last used resolution and display mode!
- Also, you can adjust `average_valorant_load_time` 
and `average_match_load_time` (/scripts/settings.py 20 and 21 lines)

## Launch:
0. Execute -> Launcher.bat

![Getting Started](./resources/bot_pic.png)

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

### You would help to this project by
- Simply leaving a star on this repo
- [Buying me a pizza](https://www.buymeacoffee.com/SoGoesLight)
<form action="https://www.paypal.com/donate" method="post" target="_top">
<input type="hidden" name="hosted_button_id" value="UT48PZQVMB5XQ" />
<input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Donate with PayPal button" />
<img alt="" border="0" src="https://www.paypal.com/en_LV/i/scr/pixel.gif" width="1" height="1" />
</form>

### Contacts:
[E-mail](mailto:SoGoesLight@gmail.com)  
