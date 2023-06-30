import json
import customtkinter as ctk
from googletrans import Translator

# Preparing translator and library
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
    """Translator app that translates text from chosen source to chosen destination and saves it in library"""

    def __init__(self):
        super().__init__()

        # Root
        self.geometry("350x740")
        self.title("Customtkinter Translator")
        self.resizable(False, False)

        # Appearance
        self.appearance = ctk.set_appearance_mode("dark")
        self.theme = ctk.set_default_color_theme("dark-blue")

        # Frames
        self.frame1 = ctk.CTkFrame(master=self)
        self.frame1.pack(pady=20, padx=20, fill="both")

        self.frame2 = ctk.CTkFrame(master=self)
        self.frame2.pack(padx=20, fill="x")

        # Frame1 widgets
        self.title = ctk.CTkLabel(master=self.frame1, text="Ctk Translator", font=ctk.CTkFont(size=30, weight="bold"))
        self.title.pack(pady=30)

        self.library_frame = ctk.CTkScrollableFrame(master=self.frame1, width=265, height=480, corner_radius=0)
        self.library_frame.pack()

        self.user_input = ctk.CTkEntry(master=self.frame1, width=285,
                                       placeholder_text="Input text you want to translate",
                                       corner_radius=0)
        self.user_input.pack()
        self.button = ctk.CTkButton(master=self.frame1, width=285, text="Enter", corner_radius=0,
                                    command=lambda: translate())
        self.button.pack()

        # Frame2 widgets
        self.source_title = ctk.CTkLabel(master=self.frame2, text="Source", font=ctk.CTkFont(size=13))
        self.source_title.grid(row=0, column=0, padx=15)

        self.destination_title = ctk.CTkLabel(master=self.frame2, text="Destination", font=ctk.CTkFont(size=13))
        self.destination_title.grid(row=0, column=1, padx=10)
        self.source = ctk.CTkOptionMenu(master=self.frame2, width=125, corner_radius=0,
                                        values=["en", "fr", "it", "de", "es", "pl"])

        self.source.grid(row=1, column=0, padx=18)

        self.destination = ctk.CTkOptionMenu(master=self.frame2, width=125, corner_radius=0,
                                             values=["pl", "es", "de", "it", "fr", "en"])
        self.destination.grid(row=1, column=1, padx=8)

        # Spawning previous translations
        for i in range(num):
            element = ctk.CTkButton(master=self.library_frame, width=200, text=(keys[i], "-", values[i]))
            element.configure(command=lambda button=element, txt=keys[i]: delete_self(button, txt))
            element.pack(pady=10)

        def translate():
            """Function that translates input from user, adds it to library and saves it"""

            # Translation, avoiding translating blank input
            to_translate = self.user_input.get()
            if to_translate:
                translated = translator.translate(text=to_translate, src=self.source.get(), dest=self.destination.get())
                # Getting rid of spaces that causes curly braces to appear
                to_translate = to_translate.replace(" ", " ")
                translated.text = translated.text.replace(" ", " ")
                source = "".join("(" + str(self.source.get()) + ") " + str(to_translate))
                destination = "".join(str(translated.text) + " (" + str(self.destination.get()) + ")")
                library[source] = destination
                # Configuring result button
                result_text = "(" + self.source.get() + ") " + to_translate, "-", \
                              translated.text + " (" + self.destination.get() + ")"
                result = ctk.CTkButton(master=self.library_frame, width=200, text=result_text)
                result.configure(command=lambda button=result: delete_self(button, source))
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
