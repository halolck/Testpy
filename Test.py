from cmath import tanh
from math import fabs
from turtle import width
from unicodedata import name
from cv2 import resizeWindow
import dearpygui.dearpygui as dpg
from matplotlib import image
from matplotlib.pyplot import text
from torch import deg2rad


def window_editor(sender, app_data, user_data):
    if dpg.does_item_exist("ImageSetting"):
        dpg.configure_item(
            "ImageSetting",
            width=dpg.get_value("Width"),
            height=dpg.get_value("Height"),
            pos=[dpg.get_value("Start x"), dpg.get_value("Start y")],
            autosize=dpg.get_value("No Autosize"),
            no_resize=dpg.get_value("No Resizable"),
            no_title_bar=dpg.get_value("No Title bar"),
            no_move=dpg.get_value("No Movable"),
            no_scrollbar=dpg.get_value("No Scroll bar"),
            no_collapse=dpg.get_value("No Collapse"),
            horizontal_scrollbar=dpg.get_value("Horizontal Scrollbar"),
            no_focus_on_appearing=dpg.get_value("No Focus on Appearing"),
            no_bring_to_front_on_focus=dpg.get_value("No Bring To Front on Focus"),
            menubar=dpg.get_value("Menubar"),
            no_close=dpg.get_value("No Close"),
            label=dpg.get_value("Label"))
    else:
        print("window does not exists")


def create_window():
    if dpg.does_item_exist("Setting"):
        print("already windows Open")
    else:
        with dpg.window(
                tag="Setting",
                autosize=True,
                no_close=False,
                label="Setting",
                width= 233,
                on_close=on_window_close):

           
            dpg.add_text("Size")
            dpg.add_slider_int(label="W" , max_value=2000 , min_value=0 , default_value=500 , width=200)
            dpg.add_slider_int(label="H" , max_value=2000 , min_value=0 , default_value=500 , width=200)
            dpg.add_text("Distortion")
            dpg.add_slider_int(label="K1" , max_value=100 , min_value=-100 , default_value=0 , width=200)
            dpg.add_slider_int(label="K2" , max_value=100 , min_value=-100 , default_value=0 , width=200)
            dpg.add_slider_int(label="K3" , max_value=100 , min_value=-100 , default_value=0 , width=200)
            dpg.add_slider_int(label="K4" , max_value=100 , min_value=-100 , default_value=0 , width=200)
            dpg.add_slider_int(label="K5" , max_value=100 , min_value=-100 , default_value=0 , width=200)
            dpg.add_slider_int(label="K6" , max_value=100 , min_value=-100 , default_value=0 , width=200)
            dpg.add_button(label= "Save")

def create_Datawindow():
    if dpg.does_item_exist("Data"):
        print("already windows Open")
    else:
        dpg.show_metrics()


def on_window_close(sender, app_data, user_data):
    # workaround
    children_dict = dpg.get_item_children(sender)
    for key in children_dict.keys():
        for child in children_dict[key]:
            dpg.delete_item(child)

    dpg.delete_item(sender)
    print("window was deleted")


dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=200)
width1, height1, channels, data = dpg.load_image("image.jpg") 
with dpg.texture_registry():
        texture_id = dpg.add_static_texture(width1, height1, data) 
with dpg.window(tag="Main Window", label="Main Window", autosize=True):
    with dpg.viewport_menu_bar():
        with dpg.menu(label="Tool"):
            dpg.add_menu_item(label="Setting" , callback= create_window)
            dpg.add_menu_item(label="Metrics" , callback= create_Datawindow)
            dpg.add_image
    
    dpg.add_image(texture_id)
#create_window()

dpg.create_viewport(title=f"FishEye Capture", width=1280, height=960, resizable=False)
dpg.set_primary_window("Main Window", True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
