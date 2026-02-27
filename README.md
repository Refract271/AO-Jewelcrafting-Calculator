# AO-Jewelcrafting-Calculator
an implementation of the jewelcrafting system in the game [Arcane Odyssey](https://www.roblox.com/games/3272915504/Arcane-Odyssey). But in python and with unlimited ressources ofc   
Created by Refract271

## How to use?  

Simply download or copy-paste the [gemCalculator.py](https://github.com/Refract271/AO-Jewelcrafting-Calculator/blob/main/gemCalculator.py), [gemData.json](https://github.com/Refract271/AO-Jewelcrafting-Calculator/blob/main/gemData.json) and [reagantData.json](https://github.com/Refract271/AO-Jewelcrafting-Calculator/blob/main/reagantData.json)file.  
Running the program will print out the gem but it's **not formatted nicely yet**.  
If you are already familiar with python it's all explained in it but down below is a *slightly* more in-depth explanation.

### Calling the function :

You will need to edit the line that calls the function and give it the arguments you want to then run the code:

```python
firstJewel = makeJewel("malachite", "arcane_salt", "bone")
secondJewel = makeJewel("lapis_lazuli", "seaweed", "toxic_seawater_bottle")
```

> [!NOTE]
> You will obviously need python to run it, any modern version should work

  
### The arguments :

All the arguments are explained in the code but here is a run-through, **the names can be found in the json files but they are the same as in-game and a space is replaced by "_"**:

- **gem** : *string*      -> the gem you want to use

- **reagant1** : *string* -> the first reagant

- **reagant2** : *string* -> the second reagant

> [!CAUTION]
> Respect the *types* of the **arguments** or it will just error and not work.

## Future Updates + Contact 
This still need to be made easilty compatible with my gem set calculator and the output looks trash rn. If someone knows how to make an interfact for it don't hesitate to DM on discord.

If you have questions DM **Refract271** in the Official AO discord server.
