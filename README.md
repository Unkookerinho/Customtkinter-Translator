# Customtkinter-Translator
<hr>
Language translator made in Python using customtkinter and googletrans libraries.

## Features
<hr>
<ul>
<li>Translating a text and saving it in visible library</li> 
<li>Choosing between several languages</li> 
<li>Deleting previous translations by clicking on them</li> 
<li>Library is saved in json file, so it remembers your previous translations</li> 
</ul>

## Screenshots
<hr>
<p align="left"><img src="CtkTranslator.png"></p>

## Language
<hr>
Default source language is English and destination is Polish.<br>
You can change both of them between English(en), French(fr), Italian(it), German(de), Spanish(es) and Polish(pl).<br>
If language you want is missing, you can add it to values in this part:

```python

self.source = ctk.CTkOptionMenu(master=self.frame2, width=125, corner_radius=0,
                                values=["en", "fr", "it", "de", "es", "pl"])

self.source.grid(row=1, column=0, padx=18)

self.destination = ctk.CTkOptionMenu(master=self.frame2, width=125, corner_radius=0,
                                     values=["pl", "es", "de", "it", "fr", "en"])
self.destination.grid(row=1, column=1, padx=8)
```


## Python Pip
<hr>
<ul>
<li>pip install customtkinter</li>
<li>pip install googletrans==3.1.0a0</li>
</ul>
It needs to be that exact version of googletrans, because the newest one is not working.
