import flet as ft

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self._languageDropDown = None
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None
        self._searchDropDown = None
        self._txtIn = None
        self._txtOut = None
        self._btnIn = None

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )

        # Add your stuff here
        def handleSpellCheck(e):
            infoMancante = False
            # controllo sulla lingua
            if self._languageDropDown.value=="None":
                txt = ft.Text(value="No language selected", color="red")
                self.page.add(txt)
                infoMancante = True

            # controllo sulla modalita di ricerca
            if self._searchDropDown.value=="None":
                txt = ft.Text(value="No search modality selected", color="red")
                self.page.add(txt)
                infoMancante = True

            # controllo sulla frase
            print(self._txtIn)
            if self._txtIn.value=="":
                txt = ft.Text(value="No sentence written", color="red")
                self.page.add(txt)
                infoMancante = True
            self.page.update()

            if not infoMancante:
                sentence = self._txtIn.value
                printSentence = ft.Text(value=f"Sentence: {sentence}")
                self.page.add(ft.Row(controls=[printSentence], alignment=ft.MainAxisAlignment.START))
                wrongWords = self.__controller.handleSentence(sentence, self._languageDropDown.value.lower(), self._searchDropDown.value)
                txtWW = ft.Text(value=f"Wrong words: {wrongWords[0]}")
                self.page.add(ft.Row(controls=[txtWW], alignment=ft.MainAxisAlignment.START))
                txtTime = ft.Text(value=f"Time: {wrongWords[1]}")
                self.page.add(ft.Row(controls=[txtTime], alignment=ft.MainAxisAlignment.START))
                self.page.update()

        self._languageDropDown = ft.Dropdown(label="Lingua", hint_text="Select language", value="None", expand=True,
                                   options=[ft.dropdown.Option("Italian"), ft.dropdown.Option("English"),
                                            ft.dropdown.Option("Spanish")])
        self.page.add(self._languageDropDown)
        self._searchDropDown = ft.Dropdown(label="Search modality", hint_text="Select modality", value="None",
                                   options=[ft.dropdown.Option("Default"), ft.dropdown.Option("Linear"),
                                            ft.dropdown.Option("Dichotomic")])
        self._txtIn = ft.TextField(label="Write a sentence")
        self._btnIn = ft.CupertinoButton(text="Spell check", on_click=handleSpellCheck)
        self.page.add(ft.Row(controls=[self._searchDropDown, self._txtIn, self._btnIn]))
        self.page.update()

    def update(self):
        self.page.update()
    def setController(self, controller):
        self.__controller = controller
    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
