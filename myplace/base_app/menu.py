# myapp/menu.py
from django.urls import reverse

SIDEBAR_MENU_ITEMS = [
    {
        "header_name": "カイル研究所",
        "icon": "",
        "menus":[
            {
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
            },
            {
                "name": "分析",
                "icon": "fa-solid fa-chart-simple",
                "url": "#",
                "children": [
                    {
                        "name": "かーしか",
                        "icon": "fa-solid fa-magnifying-glass-chart",
                        "url": reverse("kashika:upload"),
                    },
                ],
            },
            {
                "name": "管理",
                "icon": "fa-solid fa-gear",
                "url": "#",
                "children": [
                    {
                        "name": "Django管理サイト",
                        "icon": "fa-solid fa-screwdriver-wrench",
                        "url": "/admin",
                    },
                ],
            },
        ]
    },
]
