define c = Character("Cubbie", color='#c7be0c')
define f = Character("?", color='#54c70c')
define r = Character("Bwaine Jockson", color='#54c70c')
define d = Character("?", color='#c7820c')
define k = Character("Kaktus", color='#c7820c')

define f_whisper = Character("?", who_color='#54c70c', what_size=18)
define r_shout = Character("Bwaine Jockson", who_color='#54c70c', what_size=50)
define c_whisper = Character("Cubbie", who_color='#c7be0c', what_size=18)
define c_shout = Character("Cubbie", who_color='#c7be0c', what_size=50)
define d_shout = Character("?", who_color='#c7820c', what_size=50)

define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')

# The game starts here.

label start:

    play music "audio/beginning.mp3" fadeout 1
    scene bg calesports

    show cubbie huh:
        size (200,200)
        xalign .90
        yalign .90

    "{i}I've always wondered where I belonged...{/i}"

    c "I love everyone in CWG but I just feel so out of place... {p}It's so lonely being the only cubbie here. I wish there were other cubbies out there."

    hide cubbie huh
    show cubbie:
        size (200,200)
        xalign .90
        yalign .90

    c "I want to meet someone just like me. {p}Let the cubbie search begin!"

    stop music

    hide cubbie
    show scared:
        size (200,200)
        xalign .9 yalign .9
        linear 1.0 xalign .75 yalign -1.0

    "{i} Cubbie takes a deep breath and leaps up to the sky{/i}"

    scene space

    show scared:
        size (150,150)
        xalign 1.5 yalign .5
        linear 5.0 xalign -1.9 yalign .7

    play sound "audio/flying.mp3" volume 2.0

    c_shout "AHHHH!"

    scene bg black
    play sound "audio/crash.mp3" volume .5
    with hpunch

    "..."

    f_whisper "{i}Are you okay?{/i}"

    c_whisper "Huh?"

    f "Did it hurt when you fell from heaven?"

    c "Excuse me?"

    scene bg forest
    with Dissolve(.5)

    play music "audio/forest.mp3"

    show forest npc:
        xalign .75
        yalign .5

    f "You literally fell down from the sky"

    "{i} Cubbie gets up and brushes the mud off her body.{/i}"

    with vpunch

    c_shout "YUCK!"

    "{i} Even though they're really dirty and probably needs another bath soon, they is determined to find more cubbies.{/i}"

    show thinking:
        size (200,200)
        xalign .15
        yalign .5

    with fade

    c "Where am I? {p}Do you know if there are other cubbies here? {p}Can you help me find them?"

    f "Woah, slow down there, little one. Let me introduce myself first."

    r "My name is Bwaine Jockson but you can call me the Rock. {p}We are currently in the {b}Great Forest{/b}, home to rocks, rocks, and more rocks!"

    r "And... {p}This cubbie you're looking for... {p}Wait, what's a cubbie?"

    hide thinking

    show cubbie norm:
        size (200,200)
        xalign .15
        yalign .5

    c "Someone who is just like me"

    r "Hmm, there are plenty of folks out here! I'm sure you would find someone."

    c "Can you help me then?"

    r "My help doesn't come for free, little one! {p}I will help you in search if you do me a favor."

    menu:

        "Yes, I'm on it! What is the favor?":
            jump choice1_yes

        "Nuh-uh {p}I'm not gonna do you a favor! Just tell me where to find more cubbies!":
            jump choice1_no

    label choice1_yes:
        $ menu_flag = True
        r "I need you to get me some wood to cook my dinner tonight"
        jump choice1_done

    label choice1_no:
        $ menu_flag = False

        hide forest npc
        show forest huh:
            xalign .75
            yalign .5

        hide cubbie norm
        show scared:
            size (200,200)
            xalign .15
            yalign .5

        r_shout "How dare you talk back to me!"

        r "You will do my bidding because I am the powerful Rock in this forest."

        r "Get me some wood to cook my dinner tonight and I will consider giving you answers"

        c_whisper "okay"

        jump choice1_yes

    label choice1_done:
    hide scared
    hide forest huh
    show cubbie norm:
        size (200,200)
        xalign .75
        yalign .5

    show forest npc:
        xalign .75
        yalign .5

    show screen gameUI

    show cubbie:
        size (200,200)
        xalign .15
        yalign .5

    r "Click on the top right button to see the map. You aren't able to go to different areas yet but I have highlighted the area you need to go to. good luck!"

    return

#Forest after the descision
label world1_pressed:
    stop music fadeout 1
    hide forest npc
    hide cubbie norm
    play music "audio/forest2.mp3"
    show bg forest2
    with fade
    #walking forest
    "{i}Cubbie makes her way to the other part of the forest{/i}"

    show cubbie:
        size (200,200)
        xalign .45
        yalign .75

    "{i}Cubbie strolls through the forest searching for wood. They feels the cool wind and listens to the chirping birds. It's quite peaceful here...{/i}"

    hide cubbie
    show cubbie huh:
        size (200,200)
        xalign .45
        yalign .75

    "{i}But They can't help but feel lonely{/i}"

    c "I feel so alone. It was fun talking to the Rock but he’s not like me."

    c "I guess I’ll never find anyone like me…"

    "{i}You make your way back to the Rock with the wood you collected{/i}"

    hide huh

    show bg forest
    with fade
    play music "audio/forest.mp3"

    show forest npc:
        xalign .75
        yalign .5

    show cubbie:
        size (200,200)
        xalign .15
        yalign .55

    c "Hey, I got that wood you wanted. Now, can you help me find more cubbies?"

    r "This wood is perfect! Thank you, little one. {p}I’m going to cook a special dinner tonight."

    r "As for my help, what I can give you is this piece of advice."

    r " Trust me on this. I have lived for a thousand years."

    r "I have met others like you who wind up here when they feel lost in life. And they all had the same goal: {p}to feel like they belong."

    r "However, no one will achieve that goal if they only look for the exact replica of themselves."

    r "You need to find people who love and accept you for who you are despite your differences"

    hide cubbie
    show cubbie surprised:
        size (200,200)
        xalign .15
        yalign .55

    c_shout "Really? {p}How do I find those people?"

    "{i}The Rock gives Cubbie a sincere smile{/i}"

    r "They're closer than you think. {p}You just need to look in the right direction. {p}Self-acceptance is the key to that path."

    r "Here, take this. This piece will help you on your journey in finding yourself."

    r "..."

    play sound "audio/item.mp3" volume .5

    show headphones:
        size(100,90)
        xalign .75 yalign .5
        linear 1.5 xalign .25 yalign .55

    "**You have obtained {color=#0080c0}gaming headphones{/color}**"

    r "Your first piece is this pair of gaming headphones."
    #new headphones
    "{i}Cubbie stares at the headphones for a bit. {p}These headphones remind her of home"

    hide headphones
    hide cubbie
    show cubbie1:
        size(200,200)
        xalign .15
        yalign .55

    c "{i}You start to feel a little warm inside once you put them on. They fit perfectly.{/i}"

    r "So I take it that you like them?"

    c "They are perfect. {p}Thank you"

    r "Good! This is farewell. {p}Until next time, little one. {p}Good luck on your journey. I believe in you."

    hide cubbie1
    stop music fadeout 1
    show scared:
        size (200,200)
        xalign .15 yalign .55
        linear 5.0 xalign -1.9 yalign .7

    c "wait whaaaaaaaaaaaaaaaaaaaaaaaa"


    jump world2
#Desert
label world2:
    scene space

    show cubbie norm:
        size (150,150)
        xalign 1.5 yalign .5
        linear 5.0 xalign -1.9 yalign .7

    c_shout "WEEEEEEEEEEEEEEEEEEEEE"

    with hpunch
    play sound "audio/crash2.mp3" fadeout 1


    c "Aha, I might've landed on my face the first time, but not this time!"

    scene bg desert
    with fade

    show cubbie surprised:
        size(150,150)
        xalign .75
        yalign .65

    c "Wow, this area is so pretty! {p}The sky is clear and the sand is a beautiful golden color! {p}Just like me ;)"

    hide cubbie surprised

    show cubbie norm:
        size(150,150)
        xalign .75
        yalign .65

    "{i}Cubbie beathes in the earthy dry smell, determined to continue their search for their fellow cubbies.{/i}"

    "{i}They march on forwards with determination swelling their heart{/i}"

    play music "audio/desert.mp3" volume 7.5

    hide cubbie norm
    show scared:
        size(200,200)
        xalign .75
        yalign .65
        linear 3.0 xpos .25 ypos .75

    c "*Huff, huff, huff...*"

    c "The sun sure is strong, and my throat feels so dry. {p}I've never thought about this until now, but do cubbies need water?"

    "{i} Cubbie spots an oasis and quickly runs to it{/i}"

    stop music
    play music "audio/oasis.mp3"
    show bg oasis
    with fade

    hide scared
    show cubbie norm:
        size(200,200)
        xalign .25
        yalign .65

    menu:
        "{i}Should they drink the delicious looking H20?{/i}"

        "Of course! Hydrate or diedrate.":
            jump choice2_yes

        "Nuh-uh, I don’t know what’s in there…!":
            jump choice2_no

    label choice2_yes:
        $ menu_flag = True
        "{i}Cubbie gulps down the water from the oasis, feeling fully refreshed afterwards. Turns out Cubbies do, in fact, need water to live.{/i}"

    label choice2_no:
        $ menu_flag = False

        hide cubbie norm
        show scared:
            size(200,200)
            xalign .25
            yalign .65

        "{i}Cubbie turns away from the tempting oasis. The dry feeling persists in their throat.{/i}"

    stop music
    jump choice2_done

#Desert after the descision
label choice2_done:
    scene bg desert
    with fade

    show desert npc:
        size(600,550)
        xalign .25
        yalign .25

    d "Looks like you are lost here!"

    hide scared
    show cubbie surprised:
        size (200,200)
        xalign .75
        yalign .65

    with vpunch
    c_shout "AHHHHHHHHH"

    hide desert npc
    show desert talking:
        size(600,550)
        xalign .25
        yalign .25

    with vpunch
    d_shout "AH! WHY ARE YOU YELLING?!"

    c "Why are you a talking cactus?"

    d "Why are you a talking lemon mochi?"

    hide cubbie surprised
    show thinking:
        size(200,200)
        xalign .75
        yalign .65

    c "Oh... {p}touché"

    hide desert talking
    show desert npc:
        size(600,550)
        xalign .25
        yalign .25

    d "See? {p}Anyways, I'm Kaktus"

    hide thinking
    show cubbie1:
        size(200,200)
        xalign .75
        yalign .65

    c "I'm Cubbie, the mascot of CWG! {p}Just to be clear, I'm not a yellow mochi!"

    c "I'm here to find the place where I belong"

    hide desert npc
    show desert talking:
        size(600,550)
        xalign .25
        yalign .25

    k "Oh, how interesting"

    "{i} Kaktus shifts their sunglasses and looks throughtfully at Cubbie{/i}"

    k "Well, as the friendly cactus around here, I'll help you. {p}But before I do, you'll have to exchange something."

    c "What do you want?"

    k "Give me that pair of headphones you have there, and I’ll help you."

    hide desert talking
    show desert npc:
        size(600,550)
        xalign .25
        yalign .25

    menu:
        "... Fine":
         jump choice3_yes

        "What! No, this is a gift from my friend!":
         jump choice3_no

    label choice3_yes:
        $ menu_flag = True
        k "Haha, I’m not that mean, just keep ‘em! Your reaction was funny."

        jump choice3_done

    label choice3_no:
        $ menu_flag = False

        hide cubbie1
        show scared:
            size(200,200)
            xalign .75
            yalign .65

        k "You’re a mochi of morals, I see. It was a joke anyway, so I’ll help you."

        hide scared
        show cubbie huh:
            size(200,200)
            xalign .75
            yalign .65

        "{i}Cubbie glares at Kaktus.{/i}"

        c "Again, I'm CUBBIE, not a mochi. {p}You're such a prick!"

        "{i}Cubbie rolls their eyes{/i}"

        jump choice3_done

#Meditation section
label choice3_done:
    k "Anyway, to find where you belong you have to sit down and close your eyes."

    k "Go on now, sit"

    c "You expect me to trust you now?"

    k "Yup!"

    "{i}Cubbie shakes her head but sits down in the hot sand. {p}Taking a deep breath, they close their eyes{/i}"

    hide desert animated
    play music "audio/head.mp3" volume 2.0
    scene thoughts
    with fade

    show cubbie calm:
        size(150,150)
        xalign 0.5
        yalign 0.5

    k "Think about where you left and why you left."

    c "{i}I left {b}Cal Esports{/b} to find those who are like me. {p}Whenever the CWGers did workshops or had LANS, I felt isolated.{/i}"

    c "{i}All I could do was cheer from the discord and weekly emails{/i}"

    c "{i}I'm the face of CWG... {p}but am I truly a part of CWG?{/i}"

    hide cubbie

    k "What in the world is this?"
    stop music
    play sound "audio/hold.mp3"
    with hpunch

    k "Hey, mochi look at this!"

    show message:
        size(520,500)
        xalign .5
        yalign .3

    "{i}Cubbie cradles the message carefully as a tear falls from their eye.{/i}"

    "{i}Kaktus averts their eyes and whistles softly{/i}"

    c "It's from {b}Cal Women in Gaming, at UC Berkeley{/b}."

    k "So basically... just a bunch of gamer girls?"

    c "Not JUST! {p}They're an amazing, kind, passionate and talented group of women and minority genders."

    c "You better watch it, Kaktus"

    hide message
    scene bg desert
    play music "audio/desert2.mp3"

    show cubbie1:
        size(200,200)
        xalign .75
        yalign .65

    show desert talking:
        size(600,550)
        xalign .25
        yalign .25

    k "Seems like you're pretty protective of 'em. I guess you'll find better use for this than me, here!"

    play sound "audio/item.mp3" volume .5

    show controller:
        size(115,100)
        xalign .25 yalign .25
        linear 1.0 xalign .80 yalign .75

    "**You have obtained a {color=#0080c0}gaming controller{/color}**"

    hide desert talking
    show desert npc:
        size(600,550)
        xalign .25
        yalign .25

    c "Woah! {p}These will go great with my headphones. {p}Thanks!"

    hide controller
    hide cubbie1
    show cubbie2:
        size(200,200)
        xalign .75
        yalign .65

    "{i}Cubbie holds the controller and feels warm and fuzzy{/i}"

    scene space
    with squares
    show cubbie surprised:
        size(200,200)
        xalign .75
        yalign .65

    "{i}Realization washes over Cubbie{/i}"

    c "{i}We’re all different and unique, whether we like it or not{/i}"

    c "{i}So, it’s not about finding those who are exactly like you, but finding those who accept you for who you are.{/i}"

    menu:
         "Cubbie can’t believe that the answer was here all along. Cubbie should…"

         "Return to CWG!":
            jump choice4_yes

         "Continue traveling to find other cubbies":
            jump choice4_no

    label choice4_yes:
        $ menu_flag = True
        k "I knew you’d choose that!"

        scene ending1
        "{i}Cubbie returns to CWG, who welcomes them with open arms{/i}"
        jump choice4_done

    label choice4_no:
        $ menu_flag = False
        k "Hmmm, not surprising. But, good luck I guess"

        #cubbie continues searching

        jump choice4_done

    label choice4_done:
        jump end

label end:
    "Thank you for playing :)"
    return
