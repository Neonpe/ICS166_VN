# Vincent Cheng
label Start_chp5:
    $ CurrentChapter = 5
    $ craterInfo = False

    scene Farmhouse_Day
    with fade

    "Stupid rooster. Can't [MCname] just eat it already?"

    if jd_dead == False:
        show VampySprite at left
        with dissolve

        show JD at right
        with dissolve

        jd "Mornin' [MCname]! Any plans today?"

        menu:
            "Nay" if bonfire_invite == False: #No
                jd "Well, I don't have anything for ya to do today. ya can just wander around town."
                jump meetSteve
            "Seeth the crat'r in the woods i hath appeared in": #See the crater in the woods I appeared in
                jd "Alright, ya going home? *scoffs*"
                jump crater
            "Seeth the Psychic" if ana_dead == False: #See the Psychic
                jd "Ya actually believe in that mumbo jumbo. That girl's a hack. Her grandma was pretty good but she ain't."
                jump meetAnna
            "Jane did invite me to a bonfire tonight" if bonfire_invite == True: #Jane invited me to a bonfire tonight
                jd "Oh, got a date, huh? Good for ya."
                jump bonfire
    else:
        mc "What shalt i doth the present day?" #What shall i do today?
        menu:
            "Wand'r 'round town" if bonfire_invite == False: #Wander around town
                jump meetSteve
            "Seeth the crat'r in the woods i hath appeared in": #See the crater in the woods I appeared in
                jump craterssss
            "Seekth the Psychic" if ana_dead == False: #See the Psychic
                jump meetAnna
            "Receiveth eft f'r bonefire" if bonfire_invite == True: #Get ready for the bonfire
                jump bonfire

label meetSteve:
    scene Strip_Mall
    with fade

    "Although, wandering around town really just means wandering around the mall"
    "Suddenly a voice calls out for [MCname] in the distance."

    show VampySprite at left
    with dissolve

    Steve "Hey, can you stop for a moment? I got to ask you a few questions."

    show Steve at right
    with dissolve

    mc "Who is't art thee?" #Who are you?
    Steve "The name's Steve. I am the cop in this area. You new here right? And you are staying with the Does?"
    mc "Aye." #Yes

    if jd_dead == True:
        Steve "Have you seen the Does these last couple of days?"
        menu:
            "Tell the Truth":
                mc "I hath killed those folk." #I killed them.
                Steve "You did what? Put your hands behind you back!"
                jump Arrest
            "Tell a Lie":
                mc "I am a relative of John's.  Sir and Madam Doe has't gone to traveleth 'round the w'rld" #I am a relative of John's. John and Jannet have gone to travel around the world.
    if janeD_dead == True:
        Steve "Have you seen the clerk at the clothing store? Her name was Jane Dough."
        menu:
            "Tell the Truth":
                mc "I hath killed h'r." #I killed her.
                Steve "You did what? Put your hands behind you back!"
                jump Arrest
            "Tell a Lie":
                mc "I has't not seen misseth dough." #I have not seen Miss Dough
    if ana_dead == True:
        Steve "Have you seen [AnnaName]. She's the local Psychic."
        menu:
            "Tell the Truth":
                mc "I hath killed h'r." #I killed her.
                Steve "You did what? Put your hands behind you back!"
                jump Arrest
            "Tell a Lie":
                mc "I has't not seen Anna 'round." #I have not seen Anna around.

    Steve "When did you get here?"
    mc "I arriv'd a couple weeks ago." #I arrived a couple weeks ago.
    Steve "How did you get here?"
    mc "I am not sure. I doth not rememb'r aught. " #I am not sure. I don't remember anything.
    Steve "Well that's weird. You don't remember anything. So what are you gonna do now?"
    mc "I shall gath'r inf'rmation and figure out how I did get h're." #I will gather information and figure out how I got here.
    Steve "I guess that's better than Johnny..."
    Steve "Well I'll see if I can find out more information for you. Also, don't leave town!"

    mc "Well, what shouldst i doth anon?" #Well, what should I do now?

    menu:
        "Check Crater":
            jump crater
        "See Anna" if ana_dead == False:
            jump meetAnna
        "Head Home":
            jump chp5_end

label Arrest:
    scene Jail
    with fade

    "[MCname] was sent to jail, however, his growing hunger soon sent him into frenzy."
    "With no other choice, the local cop, Steve, made the decision to shoot [MCname] in the head."
    "Even with his supernatural healing, [MCname] succumbed to his imprisonment from lack of human blood."
    "The End"
    jump end

label crater:
    scene Woods_Sunset
    with fade

    "After a brisk walk through the woods, [MCname] arrives at the crater he landed at"

    show VampySprite
    with dissolve

    mc "wh're shouldst i checketh?" #Where should i check?

    menu:
        "Bushes around the crater":
            mc "What is this?"
            "After roughing up some bushes, some scraps of burnt paper were found"
            "They read:"
            "In a time, before time..."
            "I'm the prince of the night!"
            "TALKING LOUD SHOULD DO THE TRICK!"
            "I can help for one small fee."
            "Give four to me."
            mc "These pieces of paper seem to be pages from a book."
            mc "But why are they burnt, and are these instructions?"
            $ crater_info = True
        "The crater itself":
            mc "Th're's nothing h're.  This wast a wasteth of timeth." #There's nothing here. This was a waste of time.
    mc "Timeth to headeth backeth"

    if bonfire_invite == True:
        mc "What doth I doth anon?" #What do I do now?
        menu:
            "Wend to the bonfire": #Go to the bonfire
                jump bonfire
            "Timeth to wend home": #Time to go home
                jump chp5_end
    jump chp5_end

label meetAnna:
    scene Psychic_store
    with fade

    show Anna at right
    with dissolve

    show VampySprite at left
    with dissolve

    Anna "Welcome Back, dear customer. What can I do for you today?"
    menu:
        "Thy pow'rs art wond'rful.  Can thee holp me?": #Your powers are wonderful. Can you help me?
            $ total_trust += 1
            $ trust_for_anna += 1
            #trust +1

        "I hadst nay plans the present day so i cameth h're": #I had no plans today so I came here
            $ total_trust -= 1
            $ trust_for_anna -= 1
            #trust -1
    Anna "Of Course! What would you like me to help you with?"
    menu:
        "Ask Anna some questions - $1":
            if money >= 1:
                $ choice_with_ana  = 1
                $ total_trust += 1
                $ trust_for_anna += 1
                #trust + 1
            elif money < 1:
                Anna "Sorry hun, it appears you don't have enough money. Stop by again sometime."
                jump chp5_end

        "Consult the crystal ball - $5":
            if money >= 5:
                $ choice_with_ana = 2
            if money < 5:
                Anna "Sorry hun, it appears you don't have enough money. Stop by again sometime."
                jump chp5_end


    if choice_with_ana == 1:
        menu:
            "Who is't Jane?":
                Anna "My best friend, I'm always lending some of my grandma's books to her. She loves them"
                "[MCname] hands over one dollar with no complaint."
                $ money = money - 1
            "Who is't wast thy grandma?":
                Anna "haaah, the real fortun teller here. She was amazing! She could cast away spirits and bring people luck"
                Anna "I can try but I don't think I'll ever be like her"
                "[MCname] hands over one dollar with no complaint."
                $ money = money - 1

    if choice_with_ana == 2:
        hide Anna
        with dissolve

        hide VampySprite
        with dissolve

        scene Crystal_ball
        with fade

        unknow "\nThe time for us to part is nearly hear."
        unknow  "\nThe hands of fate will bind you once more."

        scene Psychic_store
        with fade

        "[MCname] thanks Anna and pays her for her services."
        $ money = money - 5

    show VampySprite at left
    with dissolve

    show Anna at right
    with dissolve

    mc "Once again, thee has't been a most wondrous holp." #Once again, you have been a great help
    Anna "Of course. Please come again."

    hide Anna
    with dissolve

    hide VampySprite
    with dissolve

    scene Strip_Mall
    with fade

    show VampySprite
    with dissolve

    if bonfire_invite == True:
        mc "Lets wend to the bonfire" #Lets go to the bonfire.
    else:
        mc "Lets head home"
        jump chp5_end

label bonfire:
    scene bonfire
    with fade

    show VampySprite at left
    with dissolve

    show JaneD at right
    with dissolve

    janed "Hey [MCname]! I'm glad you could make it."
    mc "Thanketh thee f'r inviting me" #Thank you for inviting me
    janed "How have you been? Are you fitting in ok?"
    mc "I am still trying to figure out wh're i cameth from.  Who is't is this?" #I am still trying to figure out where I came from. Who is this?
    janed "Aw that sucks. Oh, this is my friend, Steve. He is the local cop in our town."

    hide JaneD
    with dissolve

    show Steve at right
    with dissolve

    Steve "Hi, the name's Steve. You new here right? And you are staying with the Doesssss?"
    mc "Aye." #Yes
    Steve "Do you mind stepping aside so I can ask you a couple questions?"
    mc "Sure."

    if jd_dead == True:
        Steve "Have you seen the Does these last couple of days?"
        menu:
            "Tell the Truth":
                mc "I hath killed those folk." #I killed them.
                Steve "You did what? Put your hands behind your back!"
                jump Arrest
            "Tell a Lie":
                mc "I am a relative of John's.  Sir and Madam Doe has't gone to traveleth 'round the w'rld" #I am a relative of John's. John and Jannet have gone to travel around the world.
    if ana_dead == True:
        Steve "Have you seen [AnnaName]. She's the local Psychic."
        menu:
            "Tell the Truth":
                mc "I hath killed h'r." #I killed her.
                Steve "You did what? Put your hands behind you back!"
                jump Arrest
            "Tell a Lie":
                mc "I has't not seen Anna 'round." #I have not seen Anna around.

    Steve "When did you get here?"
    mc "I arriv'd a couple days ago." #I arrived a couple days ago.
    Steve "How did you get here?"
    mc "I am not sure. I doth not rememb'r aught. " #I am not sure. I don't remember anything.
    Steve "Heh, just like Johnny. Ah sorry, I'm not judging you or anything. You're working so you're already better than that shit stain"
    mc "tis fine.  I can figure it out on mine owneth." #It's fine. I can figure it out on my own.

    hide Steve
    with dissolve

    show JaneD at right
    with dissolve

    janed "Come on guys. Stop talking about boring stuff and lets have some fun."

    hide JaneD
    with dissolve

    "The bonfire is quite enjoyable, having a fun time in the darkness is pretty nice"

    show VampySprite at center
    with dissolve

    mc "Tis timeth to wend home" #its time to go home
    jump chp5_end

label chp5_end:
    scene Drak_pic
    with fade

    unknow "Tomorrow, my dreams come true"
    jump Start_chp6
