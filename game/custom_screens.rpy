screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "UI/stats_%s.png"
        action ShowMenu("MapUI")

screen MapUI():
    tag statsUI
    add "Map/bg map.png"

    imagebutton:
        xalign .80
        yalign .68
        xpos 0.25
        ypos 0.25
        idle "Map/hover.png"
        hover "Map/hover.png"
        action Jump("world1_pressed")

screen StatsUI():
    add "UI/test.png"
    frame:
        xalign 0.2
        yalign 0.5
        xpadding 30
        ypadding 30

        hbox:
            spacing 40

            vbox:
                spacing 10
                text "Pieces" size 40
                text "Inventory" size 40

            vbox:
                spacing 10
                text "[pieces]" size 40
                text "[Inventory]" size 40
