import flet as ft
import random as r
from time import sleep

def main(page: ft.Page):
    page.title = "Deciciones"
    page.window_center()
    page.window_height = 200
    page.window_width = 300    
    
    page.update()

    pr = ft.ProgressRing(width=50, height=50, stroke_width = 2)
    # ft.Row([pr],alignment=ft.MainAxisAlignment.CENTER,)
    for i in range(0, 4):
        pr.value = i * 0.01
        sleep(0.1)
        page.update()

    def btn_dec(e):
        num = r.randint(0,1)
        if num == 0:
            page.clean()
            page.bgcolor = ft.colors.BACKGROUND
            page.add(ft.Row([pr],alignment=ft.MainAxisAlignment.CENTER,))
            for i in range(0, 9):
                pr.value = i * .20
                sleep(0.1)
                page.update()
            page.bgcolor = ft.colors.RED_800
            page.update()
            dec = ft.Row(
            [   
                ft.Text("NO",size=50)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
            dec_btn = ft.Row(
            [   
                ft.ElevatedButton(text="Decisión", on_click= btn_dec, color=ft.colors.RED_100,bgcolor=ft.colors.BLUE_GREY)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
            
        elif num == 1:
            page.clean()
            page.bgcolor = ft.colors.BACKGROUND
            page.add(ft.Row([pr],alignment=ft.MainAxisAlignment.CENTER,))
            for i in range(0, 9):
                pr.value = i * .20
                sleep(0.1)
                page.update()
            page.bgcolor = ft.colors.GREEN_800
            page.update()
            dec = ft.Row(
            [   
                ft.Text("YES!",size=50)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            )
            dec_btn = ft.Row(
            [   
                ft.ElevatedButton(text="Decicion", on_click= btn_dec,color=ft.colors.GREEN_100,bgcolor=ft.colors.BLUE_GREY)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        page.clean()
        page.add(
                dec,
                dec_btn
                )
    dec_btn = ft.Row(
            [   
                ft.ElevatedButton(text="Decicion", on_click= btn_dec)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    page.add(
        ft.Row(
            [   
                ft.Text("Choice",size=50)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            ),
        ft.Row(
            [   
                dec_btn
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )
ft.app(target=main)
