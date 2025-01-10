# myapp/menu.py
from django.urls import reverse

SIDEBAR_MENU_ITEMS = [
    {
        "header_name": "カイル研究所",
        "icon": "",
        "menus":[{
            "name": "API",
            "icon": "fas fa-users",
            "url": "#",
            "children": [
                {
                    "name": "Chat with GPT",
                    "icon": "fas fa-shield-dog",
                    "url": reverse("kairu_chat:chat"),
                },
                {
                    "name": "Weather API",
                    "icon": "fas fa-shield-dog",
                    "url": reverse("weather_report:weather_list"),
                },
            ],
        },]
    },
]
