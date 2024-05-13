import win32gui
import numpy as np
import find_template
import search_and_click_color
import if_white

# search_and_click_color.search_and_click_color(screenshot, region)#search for orange color


if __name__ == "__main__":
    random_list= [0.75,1,0.75,2,2.757546,2,2.984,2.1541,2.5,3.541,10]
    list_wait_fish=[0.2,0.5,1.2,1.3,1.51,1,1,1,0.75,2,2.757546,2,2.1541,2.5,2]
    list_red_found=[0,0,0,0,0,0,0,0.1]
    random_list_click=np.linspace(0, 0.7, 50)
    # syntaxe 'Paladium - YOURNAMEHERE' (without the quotes)(attention aux espaces et aux majuscules)
    hwnd = win32gui.FindWindow(None, 'Paladium - YOURNAMEHERE')
    template_path = ("images/template_peche.png")
    print ("loaded")
    while True:
        result = find_template.find_template(template_path, hwnd)
        if result != False:
            result_search_and_click_color = search_and_click_color.search_and_click_color(result[1], result[0])
            if result_search_and_click_color != False:
                region = result_search_and_click_color[0]
                print("region par findandclick",region)
                color= result_search_and_click_color[1]
                if_white.if_white(region, color)
