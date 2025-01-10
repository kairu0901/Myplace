# myproject/context_processors.py
from base_app.menu import SIDEBAR_MENU_ITEMS

def sidebar_menu(request):
    return {
        "sidebar_menu_items": SIDEBAR_MENU_ITEMS,
    }
