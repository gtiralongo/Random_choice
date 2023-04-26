import flet as ft
import random as r

def main(page: ft.Page):
    page.title = "Deciciones"
    page.window_center()
    page.window_height = 200
    page.window_width = 300    
    

    page.update()
    def btn_dec(e):
        num = r.randint(0,1)
        if num == 0:
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
                ft.ElevatedButton(text="Decicion", on_click= btn_dec, color=ft.colors.RED_100,bgcolor=ft.colors.BLUE_GREY)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
            
        elif num == 1:
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
                dec_btn
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)