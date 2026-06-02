import flet as ft 

def main_page(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = 'Мое первое приложение'

    text_hello = ft.Text(value='Hello world')


    def on_button_click(_):
        # print(name_input.value)

        if name_input.value:
            name = name_input.value.strip()
            text_hello.value = f'Hello {name}'
            name_input.value = None
            text_hello.color = None
        else: 
            text_hello.value = 'Введите имя!'
            text_hello.color = ft.Colors.RED

    name_input = ft.TextField(on_submit=on_button_click)
    button_elevated = ft.ElevatedButton('send', icon=ft.Icons.SEND, on_click=on_button_click)

    page.add(text_hello, name_input, button_elevated)

ft.run(main_page)
# ft.run(main_page, view=ft.AppView.WEB_BROWSER)