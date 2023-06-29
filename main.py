import json
import customtkinter as ctk
from googletrans import Translator

translator = Translator()
library = {}

# Opening library
try:
    with open("library.json", "r") as file:
        library = json.load(file)
except:
    pass


# Preparing previous cases
keys = []
values = []
for key, value in library.items():
    keys.append(key)
    values.append(value)

num = len(library)


class TranslatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Root
        self.geometry("350x700")
        self.title("Customtkinter Translator")

        # Appearance
        self.appearance = ctk.set_appearance_mode("dark")
        self.theme = ctk.set_default_color_theme("dark-blue")
        # Frame
        self.frame = ctk.CTkFrame(master=self)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Frame widgets
        self.title = ctk.CTkLabel(master=self.frame, text="Ctk Translator", font=ctk.CTkFont(size=30, weight="bold"))
        self.title.pack(pady=30)

        self.library_frame = ctk.CTkScrollableFrame(master=self.frame, width=260, height=480, corner_radius=0)
        self.library_frame.pack()

        # Spawning previous cases
        for i in range(num):
            element = ctk.CTkButton(master=self.library_frame, width=200, text=(keys[i], "-", values[i]))
            element.configure(command=lambda button=element, txt=keys[i]: delete_self(button, txt))
            element.pack(pady=10)

        self.user_input = ctk.CTkEntry(master=self.frame, width=280,
                                       placeholder_text="Input text you want to translate",
                                       corner_radius=0)
        self.user_input.pack()
        self.button = ctk.CTkButton(master=self.frame, width=280, text="Enter", corner_radius=0,
                                    command=lambda: translate())
        self.button.pack()

        def translate():
            """Function that translates input from user, adds it to library and saves it"""
            # Translation, adding it to library
            to_translate = self.user_input.get()
            if to_translate:
                # Default source is English and destination is Polish
                # Use language codes like en/pl/de/fr in src="en", dest="pl"
                translated = translator.translate(text=to_translate, src="en", dest="pl")
                library[to_translate] = translated.text

                result = ctk.CTkButton(master=self.library_frame, width=200,
                                       text=(self.user_input.get(), "-", translated.text))
                result.configure(command=lambda button=result: delete_self(button, to_translate))
                result.pack(pady=10)

            # Saves previous cases
            with open("library.json", "w") as file:
                json.dump(library, file)

            # Clears input box
            self.user_input.delete(0, ctk.END)

        def delete_self(button, text):
            """Deletes button with translation, deletes translation from library"""
            button.destroy()
            del library[text]
            with open("library.json", "w") as file:
                json.dump(library, file)


if __name__ == "__main__":
    translator_app = TranslatorApp()
    translator_app.mainloop()
