# variables.rpy
default route_type = "observer"

default aff_harin = 0
default aff_yuna = 0
default aff_seola = 0
default aff_gaeun = 0

default und_harin = 0
default und_yuna = 0
default und_seola = 0
default und_gaeun = 0

default collectibles = []

default chapter = 0
default current_scene = ""

init python:
    def add_item(item):
        if item not in collectibles:
            collectibles.append(item)
