
  
<p align="center">  
  <img src="https://cdn.discordapp.com/attachments/795703051427643404/1071102275512172596/Axontic.png">  
</p>  
  
<p style="text-align: center">
Axontic is a general bot that supports you and your server well. Easy to use and extremely simple in design.
</p>
  
## 🧾| Installation  
  
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the Python requirements.  
  
```bash  
pip install -r requirements.txt
```

To fully use the bot you need a Dagpi API key. You can get it at [https://dagpi.xyz/dashboard](https://dagpi.xyz/dashboard). Please enter this key in the config.json file.
  
## ✨ | Usage  
  
Add your bot token in the config.json.  
```json  
"token": "INSERT YOUR TOKEN HERE"  
```  
You can also change your prefix for the bot there.  
```json  
"prefix": "-"  
```  
You can also personalize the status in the main.py. 
```python  
await client.change_presence(activity=discord.Game(name='with Discord!'), status=discord.Status.do_not_disturb)  
```  
At Name, you can enter what you will see later in the status. Status shows how the bot is displayed. (Online, Idle, Do Not Disturb)  
  
To start the Bot type in the Console:  
```bash
python3 main.py
```
## 📞 | Help needed?
In case of error, please open an issue.

If you have any questions, feel free to come to my Discord server.  
[https://discord.gg/DypJbNXWMx](https://discord.gg/DypJbNXWMx)  
  
## 🔭 | License  
  
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/) [![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/) [![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)
