# Chris Goebel
label Start_chp6:
    $ CurrentChap = 6
    $ visitChoice = "Anna"
    $ dialogueChoice = 0
    $ answerJane = ""

    scene Farmhouse_Bed
    with fade

    show VampySprite at left
    with dissolve

    "Once again, [MCname] completely forgets about the obnoxious rooster until the familiar rude awakening."

    mc "Hmm, what should I do today."

#    if jd_dead == False and ana_dead == False:
    if jc_dead == True and janeD_dead == True:
        mc "Maybe I'll head to town and ask Anna if she can tell me anything else about where I came from."
        jump Does_And_Anna_Alive

#    elif jd_dead == False and jc_dead == False:
    elif ana_dead == True and janeD_dead == True:
        mc "Maybe I'll head down to the creek and ask Johnny if he noticed anything in the woods to help find out where I came from."
        jump Does_And_Johnny_Alive

#    elif jd_dead == False and janeD_dead == False:
    elif ana_dead == True and jc_dead == True:
        mc "Maybe I'll head to the supplies store and ask Jane if Anna ever mentioned anything about where I came from."
        jump Does_And_Jane_Alive

#    elif ana_dead == False and jc_dead = False:
    elif jd_dead == True and janeD_dead == True:
        menu:
            "I'll vist Anna and see if she can tell me anything else about where I came from":
                $ visitChoice = "Anna"
            "I'll head down to the creek and ask Johnny if he noticed anything in the woods to help find out where I came from.":
                $ visitChoice = "Johnny"
        jump Anna_And_Johnny_Alive

#    elif ana_dead == False and janeD_dead == False:
    elif jd_dead == True and jc_dead == True:
        mc "Maybe I'll head to the supplies store and ask Jane if Anna ever mentioned anything about where I came from."
        jump Anna_And_Jane_Alive

#    elif jc_dead == False and janeD_dead == False:
    elif jd_dead == True and ana_dead == True:
        mc "Maybe I'll head to the supplies store and ask Jane if Anna ever mentioned anything about where I came from."
        jump Johnny_And_Jane_Alive


label Does_And_Anna_Alive:
    scene Psychic_store
    with fade

    show VampySprite at left
    with dissolve

    mc "Um hello? Anna?"

    show Anna at right
    with dissolve

    Anna "Oh it's you again!? Unexpected but welcome company!"
    Anna "Say, do you keep coming in because you heard something from Jane?"


    menu:
        "Was she supposed to tell me something?":
            $ dialogueChoice = 1
        "I'm not sure what you're talking about.":
            $ dialogueChoice = 2

    if dialogueChoice == 1:
        Anna "Oh no no, I just assumed, since she comes here often as well."
        Anna "She had been quite curious about summoning a supernatural being, pestering me all the time if I knew of anything about that."

    elif dialogueChoice == 2:
        Anna "Oh don't mind me, I was just thinking you might be curious about the same things she was."
        Anna "She'd been quite interested in summoning a supernatural being if you could believe that."

    Anna "Then again, she's never had much luck with relationships in this town, maybe she was just a little lonely."

    Anna "What was it you came in for then?"

    menu:
        "Do you have any other information about where I could've come from?":
            $ dialogueChoice = 1
        "I was just in town and decided to stop in to say hello.":
            $ dialogueChoice = 2
        "Actually I think I have what I need, thank you.":
            $ dialogueChoice = 3

    if dialogueChoice == 1:
        Anna "Sorry hun, I've already told you everything I know."
    elif dialogueChoice == 2:
        Anna "My that's sweet of you, thanks for checking in."
    elif dialogueChoice == 3:
        Anna "Well that makes my job easy. If you need anything else be sure to stop by again."

    mc "Thanks for your help, I'll be heading home for now."

    scene Farmhouse_Day
    with fade

    show VampySprite at left
    with dissolve

    mc "Hmm, Jane was attempting to summon a supernatural being because she was lonely?"
    mc "She must be the reason I crashed here. That explains why she kept calling me \"QT\" and seemed so forward."

    jump MC_Back_Home_Does_Alive



label Does_And_Johnny_Alive:
    scene Creek_Bridge
    with fade

    show VampySprite at left
    with dissolve

    mc "Uh hello? You still here Johnny?"

    show JC at right
    with dissolve

    jc "Ayyee- *cough cough*, yeaa man you know I am. What's goin on, came to chill?"

    menu:
        "Actually I have a quick question for you.":
            $ dialogueChoice = 1;
        "Yeah I am, how'd you know?":
            $ dialogueChoice = 2;

    if dialogueChoice == 1:
        jc "oohh yeeaaah man? *cough* Well I got one for you man."
    elif dialogueChoice == 2:
        jc "Aayyee, just got those instincts you know man."

    jc "Just a dude to dude thing you know mannn."
    jc "Yooo you seeing anyone right now man?"

    mc "I'm afraid I'm not quite familiar with the phrase \"seeing anyone\"."

    jc "Mannn, like dating man. You got a *cough* girlfriend, boyfriend, something?"

    menu:
        "Not currently, I'm not very close to many people in this place to be honest.":
            jc "Ayee don't worry about it mannn, there's somebody for everyone ya knoww."
        "I am particularly interested in someone.":
            jc "Oooohhh lucky person mannn."

    mc "What about you, are you \"seeing anyone\"?"

    jc "Ha ha, naaahh man, I'm just chillllin man"
    jc "I did have my eye on that one Jane chick ya feeel, but she shut me down real quick."

    mc "Oh I'm quite sorry about that Johnny, are you ok?"

    jc "Honestly I'm kinda glad man, chick was crazzyy. Kept goin on about \"summoning someone special to be with\" or something like that ha."

    mc "My she sounds quite odd from what you're saying."

    jc "Ha ha, yeeaah man, it iss what it isss though ya know."

    mc "Well I better get going, I think John Doe wanted to talk to me about something tonight."

    jc "Awww man, aight. Make sure *cough cough* you're careful around girls like that man ha ha."

    scene Farmhouse_Day
    with fade

    show VampySprite at left
    with dissolve

    mc "Hmm, Johnny mentioned Jane wanted to summon someone special to be with?"
    mc "Maybe she summoned me somehow. That would explain why I crashed in the woods with no recollection of who I am or where I'm from."
    mc "And she kept calling me \"QT\" or something like that and seemed so forward with me."

    jump MC_Back_Home_Does_Alive

label Does_And_Jane_Alive:
    scene Farmhouse_Day
    with fade

    show VampySprite at left
    with dissolve

    janed "Hey QT!"

    show JaneD at right
    with dissolve

    janed "Where are you headed off to?"

    menu:
        "I'm not sure yet, maybe work on the farm or head to town.":
            janed "Ooh busy day? Well I just had a quick thing to tell you before you leave."
        "I was actually on my way to see you.":
            janed "Wow really?! I'll be honest, I came here to see you too."
            janed "I have something important to tell you that I've been thinking about for a while."

    mc "Oh really, do you need help with something?"

    janed "Umm, well kind of. Can we go somewhere more private to talk?"

    mc "Sure we can take a walk to the forest near the farm."

    scene Sad_Farm_1
    with fade

    show VampySprite at left
    with dissolve

    show JaneD at right
    with dissolve

    "[MCname] and Jane walk awkwardly across the farm to reach the forest. Each sneaking glances at the other trying to read what they're thinking."

    menu:
        "...":
            "Jane catches [MCname]'s eye as he glances sideways at her, but quickly looks away."

        "I wonder what John is doing?":
            janed "Must be tending to the horses or something, I haven't seen him out here."

        "You're quite the interesting girl you know that?":
            janed "Ha ha, thats funny coming from the king of mystery himself."
            mc "It's not my fault, I don't even remember myself."
            janed "Well that's kind of the reason I wanted to talk to you to be honest."

        "Wow I'm starving. You look delicious.":
            janed "Oh my, you're quite forward aren't you. *blushes, misunderstanding what [MCname] meant*."
            mc "I could say the same to you with all the \"QTs\"."

    scene Creek_Bridge
    with fade

    show VampySprite at left
    with dissolve

    show JaneD at right
    with dissolve

    mc "Alright, this should be private enough. What was it you wanted to tell me?"

    janed "Isn't this the place that weird man always lurks around"

    mc "Who Johnny? Oh no, this is further up the stream from there. This is actually closer to where John Doe first found me."

    janed "I see, this place seems perfect then."

    janed "So you really don't remember who you are or where you came from then?"

    menu:
        "I honestly have no idea":
            janed "Well maybe I can try to explain some things."

        "Anna kept mentioning something about fate, but I don't know what that means":
            janed "I think fate may be part of it."

        "Do you know anything that might help?":
            janed "Actually I think so, that's what I came to talk to you about."

    mc "I'll gladly accept whatever information you have."

    janed "Well, I hope you don't get upset, but I may be the reason you showed up here."

    janed "To be honest, recently I've been really lonely."

    janed "This town is so small, but even then theres not many people my age who I'd be interested in."

    menu:
        "What does that have to do with me?":
            janed "Well you know you showed up out of the blue, coincidentally when I'm looking for a relationship."
        "Are you saying you're looking for a relationship?":
            janed "Um, yeah. This town doesn't really have many options is what I mean."
        "Can you get to the point? I have things to do.":
            janed "Sorry, sorry, I'm just kind of nervous."

    janed "So I had talked to Anna about summoning a vampire since I thought she'd know something to help me."
    janed "Unfortunately she didn't, but she gave me one of her grandmother's books, who was supposed to be a better psychic than her."
    janed "Anyway, I tried some things from the book, but nothing seemed to work so I gave up."
    janed "That was until you showed up in my store and said you were working for the Does."

    menu:
        "How did you know I wasn't a relative or friend from somewhere else?":
            janed "[MCname] this is a small town in the middle of nowhere North Dakota. No one would willingly take a vacation or move here."
            mc "You do have a point there. Though I'm still not sure I fully trust you."

        "So you're saying that you summoned me so you'd have someone to date?":
            janed "I know it sounds strange or desperate, but it's true. And interacting with you when I've had the chance has made me more sure of my decision."
            mc "Well I'm not saying talking to you hasn't been enjoyable, but is that enough to trust you."

        "Why would I believe that it was you, or that I was even summoned in the first place?":
            janed "But you are a vampire right? People started disappearing when you showed up, I'm guessing you had to feed."
            mc "That's not something I'd normally admit, but you seem to already know this. I'm still very skeptical of this situation."

    janed "That's ok, I understand, but if you just take this chance, I'll prove you can trust me."
    janed "So what do you think? Are you willing to give me a chance?"

    menu:
        "Sure I guess?":
            mc "I guess we can try, I don't see much risk in that. I am a vampire, I can just eat you if anything happens."
            $ answerJane = "Yes"
            $ dialogueChoice = 1

        "I've actually been interested in you too":
            mc "I'll be honest, I've been interested in you as well, so I think we can make this work."
            $ answerJane = "Yes"
            $ dialogueChoice = 1

        "This is quite weird":
            mc "Um it's kind of weird, so I'm going to have to decline, sorry."
            $ answerJane = "No"
            $ dialogueChoice = 2

        "Let your instincts take over":
            mc "Well you know I'm a vampire, and right now I'm feeling quite... hungry"
            $ answerJane = "No"
            $ dialogueChoice = 3

    if dialogueChoice == 1:
        janed "*To self* Oh my god yes, finally."
        janed "Thank you [MCname], I promise I'll gain your trust and show you I really care."

        mc "Hold on, if you summoned me what was that strange voice in my head talking about \"I have found you\" and \"my dreams lie within you\"?"
        janed "Wait you heard all of that? Oh that's embarrassing, the link when I summoned you must've lingered so you could hear what I was thinking."
        mc "Actually that's a relief. I was afraid it was increasing my hunger and driving me to kill more often."
        mc "And what about Anna, I hate to tell you this, but I was the one who killed her."
        janed "Oh I kind of expected it was you, but I'm not completely bothered by it. I became closer with her to find out more about summoning."
        janed "It was pretty hard to connect with her anyway. She was much older than me so we didn't share many common interests."
        mc "Well I apologize anyway, it's required that I feed to stay alive, but in that case I'm going to head back to the farm, you should come over sometime soon."
        janed "That sounds perfect [MCname], I'll be looking forward to it."

    elif dialogueChoice == 2:
        janed "Oh... Ok, I understand."
        janed "Well, it was worth a shot, sorry for taking up your time [MCname]."
        mc "Sorry, I need to get back to the farm."

    elif dialogueChoice == 3:
        janed "Wait what..."
        janed "Please no, I didn't mean for this to happ-"
        "Jane is cut off abruptly as [MCname]'s hunger drives him into a frenzy."
        mc "She was right, secluded, no one around, this place was perfect."
        "After feeding on Jane, [MCname] heads back to the farm to rest."


    jd "[MCname] you're back!"

    show JD at right
    with dissolve

    jd "Jannet and I need to talk to you. Let's head inside."

    scene Farmhouse_Bed
    with fade

    show JDW at right
    with dissolve

    show JD at center
    with dissolve

    show VampySprite at left
    with dissolve

    jdw "So [MCname], you've been helping us out for a while without asking for anything in return."
    jdw "John and I decided we could use your help for a bit longer, with pay of course."
    jdw "At least until we can help you get set up with a farm of your own, if that's something you'd be interested in."

    mc "Really? Are you serious?"

    jd "It's true [MCname]. I'll admit, I was skeptical when Jannet first brought it up to me, but after mulling it over a bit I agreed."
    jd "Jannet and I aren't the spring chickens we used to be. Your help working on the farm and gathering supplies really lightened the load for us."

    jdw "What do you think [MCname]? Maybe one day you'll have your own farm and possibly take over for us when we can't keep it up anymore."

    menu:
        "Agree to take on the job and secure a future for yourself":
            $ dialogueChoice = 1
        "Give in to your darkest instincts and take the farm for yourself":
            $ dialogueChoice = 2

    if dialogueChoice == 1:
        mc "I can't pass up on this opportunity, I promise I'll keep up the hard work."
        mc "You two have been nothing but kind to me, even when I didn't know where I came from, I can't thank you enough."

        hide VampySprite
        with dissolve

        "[MCname] heads to bed after a long but exciting day."

        jd "Wait, does that mean he found out where he came from?"
        jdw "I have no idea honey, he's quite the mystery isn't he."

        scene Farmhouse_Night
        with fade

        if answerJane == "Yes":
            "[MCname] continues working on the Doe farm and saving up money for the next couple years."
            "Eventually, with some help from the Does, he purchases one of the shutdown farms and moves in together with Jane, happily living out his life."
            "After reading more into the summoning book she obtained, Jane discovers a way to reduce [MCname]'s hunger which strengthens their bond."

            scene Black_Wall
            with fade

            "(Now he only eats people for fun.)"
            "The End"
            jump end

        elif answerJane == "No":
            "[MCname] continues working on the Doe farm and saving up money for the next couple years."
            "Eventually, with some help from the Does, he purchases one of the shutdown farms and \"peacefully\" lives out his life."
            "What, did you forget he was a vampire? He's got to satisfy his instincts somehow."

            scene Black_Wall
            with fade

            "Some time passes before [MCname] realizes he never asked Jane about the dark voice in his head."
            "Was it really just his deepest instincts, or was something else at play?"
            "The End"
            jump end


    elif dialogueChoice == 2:
        mc "It was a delightful offer, but honestly..."
        mc "... you two are looking quite delicious and after today I am Starving."

        jdw "Huh?"
        jd "What is that supposed to mea-"

        "John is cut off as [MCname] lunges towards him before he has a chance to grab his rifle."

        hide JD
        with dissolve

        jdw "John was right! What are you!?"

        "Jannet barely gets out a sentence before [MCname] turns to her and treats her with the same aggression he showed her husband."

        hide JDW
        with dissolve

        mc "Why keep up the tedious labor and wait when I could have everything now?"

        "[MCname] inquires to the now empty room."
        "After finishing feasting on his former hosts, [MCname] heads to bed."

        scene Farmhouse_Night
        with fade


        if answerJane == "Yes":
            "With the Does out of the way, [MCname] takes over the farm and eventually Jane moves in with him."
            "Of course, the townspeople began to notice the Does' absence and rumors started circulating."
            "But they were all too quick to believe [MCname] was a distant relative, watching over the farm while the Does travelled abroad."

            scene Black_Wall
            with fade

            "The End"
            jump end

        elif answerJane == "No":
            "With the Does out of the way, [MCname] takes over the farm and lives unrestricted for the rest of his days."
            "Of course, the townspeople began to notice the Does' absence and rumors started circulating."
            "But they were all too quick to believe [MCname] was a distant relative, watching over the farm while the Does travelled abroad."

            scene Black_Wall
            with fade

            "Some time passes before [MCname] realizes he never asked Jane about the dark voice in his head."
            "Was it really just his deepest instincts, or was something else at play?"
            "The End"
            jump end



label Anna_And_Johnny_Alive:

    if visitChoice == "Anna":
        scene Psychic_store
        with fade

        show VampySprite at left
        with dissolve

        mc "Um hello? Anna?"

        show Anna at right
        with dissolve

        Anna "Oh it's you again!? Unexpected but welcome company!"
        Anna "Say, do you keep coming in because you heard something from Jane?"

        menu:
            "Was she supposed to tell me something?":
                $ dialogueChoice = 1
            "I'm not sure what you're talking about.":
                $ dialogueChoice = 2

        if dialogueChoice == 1:
            Anna "Oh no no, I just assumed, since she comes here often as well."
            Anna "She had been quite curious about summoning a supernatural being, pestering me all the time if I knew of anything about that."

        elif dialogueChoice == 2:
            Anna "Oh don't mind me, I was just thinking you might be curious about the same things she was."
            Anna "She'd been quite interested in summoning a supernatural being if you could believe that."

        Anna "Then again, she's never had much luck with relationships in this town, maybe she was just a little lonely."

        Anna "What was it you came in for then?"

        menu:
            "Do you have any other information about where I could've come from?":
                $ dialogueChoice = 1
            "I was just in town and decided to stop in to say hello.":
                $ dialogueChoice = 2
            "Actually I think I have what I need, thank you.":
                $ dialogueChoice = 3

        if dialogueChoice == 1:
            Anna "Sorry hun, I've already told you everything I know."
        elif dialogueChoice == 2:
            Anna "My that's sweet of you, thanks for checking in."
        elif dialogueChoice == 3:
            Anna "Well that makes my job easy. If you need anything else be sure to stop by again."

        mc "Thanks for your help, I'll be heading home for now."

        scene Farmhouse_Day
        with fade

        show VampySprite at left
        with dissolve

        mc "Hmm, Jane was attempting to summon a supernatural being because she was lonely?"
        mc "She must be the reason I crashed here. That explains why she kept calling me \"QT\" and seemed so forward."

        scene Farmhouse_Bed
        with fade

        show VampySprite at left
        with dissolve

        mc "Well I have a lot to think about. It's getting late though so I'll sleep on it for now."

        hide VampySprite
        with dissolve

        "[MCname] quickly falls asleep, piecing together information pointing to Jane summoning him."

        scene Black_Wall
        with fade

        "After his surprising discovery, [MCname] continues to run the Does' farm in their \"absence\", living out the rest of his days in peace."
        "(With the exception of consistently feeding on the townspeople)"

        "But if Jane was the one who someoned him, was she also behind the that dark voice in his head? Or was it something else entirely?"
        "The End"
        jump end


    elif visitChoice == "Johnny":
        scene Creek_Bridge
        with fade

        show VampySprite at left
        with dissolve

        mc "Uh hello? You still here Johnny?"

        show JC at right
        with dissolve

        jc "Ayyee- *cough cough*, yeaa man you know I am. What's goin on, came to chill?"

        menu:
            "Actually I have a quick question for you.":
                $ dialogueChoice = 1;
            "Yeah I am, how'd you know?":
                $ dialogueChoice = 2;

        if dialogueChoice == 1:
            jc "oohh yeeaaah man? *cough* Well I got one for you man."
        elif dialogueChoice == 2:
            jc "Aayyee, just got those instincts you know man."

        jc "Just a dude to dude thing you know mannn."
        jc "Yooo you seeing anyone right now man?"

        mc "I'm afraid I'm not quite familiar with the phrase \"seeing anyone\"."

        jc "Mannn, like dating man. You got a *cough* girlfriend, boyfriend, something?"

        menu:
            "Not currently, I'm not very close to many people in this place to be honest.":
                jc "Ayee don't worry about it mannn, there's somebody for everyone ya knoww."
            "I am particularly interested in someone.":
                jc "Oooohhh lucky person mannn."

        mc "What about you, are you \"seeing anyone\"?"

        jc "Ha ha, naaahh man, I'm just chillllin man"
        jc "I did have my eye on that one Jane chick ya feeel, but she shut me down real quick."

        mc "Oh I'm quite sorry about that Johnny, are you ok?"

        jc "Honestly I'm kinda glad man, chick was crazzyy. Kept goin on about \"summoning someone special to be with\" or something like that ha."

        mc "My she sounds quite odd from what you're saying."

        jc "Ha ha, yeeaah man, it iss what it isss though ya know."

        mc "Well I better get going, I think John Doe wanted to talk to me about something tonight."

        jc "Awww man, aight. Make sure *cough cough* you're careful around girls like that man ha ha."

        scene Farmhouse_Day
        with fade

        show VampySprite at left
        with dissolve

        mc "Hmm, Johnny mentioned Jane wanted to summon someone special to be with?"
        mc "Maybe she summoned me somehow. That would explain why I crashed in the woods with no recollection of who I am or where I'm from."
        mc "And she kept calling me \"QT\" or something like that and seemed so forward with me."

        scene Farmhouse_Bed
        with fade

        show VampySprite at left
        with dissolve

        mc "Well I have a lot to think about. It's getting late though so I'll sleep on it for now."

        hide VampySprite
        with dissolve

        "[MCname] quickly falls asleep, piecing together information pointing to Jane summoning him."

        scene Black_Wall
        with fade

        "After his surprising discovery, [MCname] continues to run the Does' farm in their \"absence\", living out the rest of his days in peace."
        "(With the exception of consistently feeding on the townspeople)"

        "But if Jane was the one who someoned him, was she also behind the that dark voice in his head? Or was it something else entirely?"
        "The End"
        jump end


label Anna_And_Jane_Alive:

    scene Farmhouse_Day
    with fade

    show VampySprite at left
    with dissolve

    janed "Hey QT!"

    show JaneD at right
    with dissolve

    janed "Where are you headed off to?"

    menu:
        "I'm not sure yet, maybe work on the farm or head to town.":
            janed "Ooh busy day? Well I just had a quick thing to tell you before you leave."
        "I was actually on my way to see you.":
            janed "Wow really?! I'll be honest, I came here to see you too."
            janed "I have something important to tell you that I've been thinking about for a while."

    mc "Oh really, do you need help with something?"

    janed "Umm, well kind of. Can we go somewhere more private to talk?"

    mc "Sure we can take a walk to the forest near the farm."

    scene Sad_Farm_1
    with fade

    show VampySprite at left
    with dissolve

    show JaneD at right
    with dissolve

    "[MCname] and Jane walk awkwardly across the farm to reach the forest. Each sneaking glances at the other trying to read what they're thinking."

    menu:
        "...":
            "Jane catches [MCname]'s eye as he glances sideways at her, but quickly looks away."

        "I wonder what John is doing?":
            janed "Must be tending to the horses or something, I haven't seen him out here."

        "You're quite the interesting girl you know that?":
            janed "Ha ha, thats funny coming from the king of mystery himself."
            mc "It's not my fault, I don't even remember myself."
            janed "Well that's kind of the reason I wanted to talk to you to be honest."

        "Wow I'm starving. You look delicious.":
            janed "Oh my, you're quite forward aren't you. *blushes, misunderstanding what [MCname] meant*."
            mc "I could say the same to you with all the \"QTs\"."

    scene Creek_Bridge
    with fade

    show VampySprite at left
    with dissolve

    show JaneD at right
    with dissolve

    mc "Alright, this should be private enough. What was it you wanted to tell me?"

    janed "Isn't this the place that weird man always lurks around?"

    mc "Who Johnny? Oh no, this is further up the stream from there. This is actually closer to where John Doe first found me."

    janed "I see, this place seems perfect then."

    janed "So you really don't remember who you are or where you came from then?"

    menu:
        "I honestly have no idea":
            janed "Well maybe I can try to explain some things."

        "Anna kept mentioning something about fate, but I don't know what that means":
            janed "I think fate may be part of it."

        "Do you know anything that might help?":
            janed "Actually I think so, that's what I came to talk to you about."

    mc "I'll gladly accept whatever information you have."

    janed "Well, I hope you don't get upset, but I may be the reason you showed up here."

    janed "To be honest, recently I've been really lonely."

    janed "This town is so small, but even then theres not many people my age who I'd be interested in."

    menu:
        "What does that have to do with me?":
            janed "Well you know you showed up out of the blue, coincidentally when I'm looking for a relationship."
        "Are you saying you're looking for a relationship?":
            janed "Um, yeah. This town doesn't really have many options is what I mean."
        "Can you get to the point? I have things to do.":
            janed "Sorry, sorry, I'm just kind of nervous."

    janed "So I had talked to Anna about summoning a vampire since I thought she'd know something to help me."
    janed "Unfortunately she didn't, but she gave me one of her grandmother's books, who was supposed to be a better psychic than her."
    janed "Anyway, I tried some things from the book, but nothing seemed to work so I gave up."
    janed "That was until you showed up in my store and said you were working for the Does."

    menu:
        "How did you know I wasn't a relative or friend from somewhere else?":
            janed "[MCname] this is a small town in the middle of nowhere North Dakota. No one would willingly take a vacation or move here."
            mc "You do have a point there. Though I'm still not sure I fully trust you."

        "So you're saying that you summoned me so you'd have someone to date?":
            janed "I know it sounds strange or desperate, but it's true. And interacting with you when I've had the chance has made me more sure of my decision."
            mc "Well I'm not saying talking to you hasn't been enjoyable, but is that enough to trust you."

        "Why would I believe that it was you, or that I was even summoned in the first place?":
            janed "But you are a vampire right? People started disappearing when you showed up, I'm guessing you had to feed."
            mc "That's not something I'd normally admit, but you seem to already know this. I'm still very skeptical of this situation."

    janed "That's ok, I understand, but if you just take this chance, I'll prove you can trust me."
    janed "So what do you think? Are you willing to give me a chance?"

    menu:
        "Sure I guess?":
            mc "I guess we can try, I don't see much risk in that. I am a vampire, I can just eat you if anything happens."
            $ answerJane = "Yes"
            $ dialogueChoice = 1

        "I've actually been interested in you too":
            mc "I'll be honest, I've been interested in you as well, so I think we can make this work."
            $ answerJane = "Yes"
            $ dialogueChoice = 1

        "This is quite weird":
            mc "Um it's kind of weird, so I'm going to have to decline, sorry."
            $ answerJane = "No"
            $ dialogueChoice = 2

        "Let your instincts take over":
            mc "Well you know I'm a vampire, and right now I'm feeling quite... hungry"
            $ answerJane = "No"
            $ dialogueChoice = 3

    if dialogueChoice == 1:
        janed "*To self* Oh my god yes, finally."
        janed "Thank you [MCname], I promise I'll gain your trust and show you I really care."

        mc "Hold on, if you summoned me what was that strange voice in my head talking about \"I have found you\" and \"my dreams lie within you\"?"
        janed "Wait you heard all of that? Oh that's embarrassing, the link when I summoned you must've lingered so you could hear what I was thinking."
        mc "Actually that's a relief. I was afraid it was increasing my hunger and driving me to kill more often."
        mc "In that case I'm going to head back to the farm, you should come over sometime soon."
        janed "That sounds perfect [MCname], I'll be looking forward to it."

    elif dialogueChoice == 2:
        janed "Oh... Ok, I understand."
        janed "Well, it was worth a shot, sorry for taking up your time [MCname]."
        mc "Sorry, I need to get back to the farm."

    elif dialogueChoice == 3:
        janed "Wait what..."
        janed "Please no, I didn't mean for this to happ-"
        "Jane is cut off abruptly as [MCname]'s hunger drives him into a frenzy."
        mc "She was right, secluded, no one around, this place was perfect."
        "After feeding on Jane, [MCname] heads back to the farm to rest."

    scene Farmhouse_Bed
    with fade

    show VampySprite at left
    with dissolve

    mc "Well I have a lot to think about. It's getting late though so I'll sleep on it for now."

    hide VampySprite
    with dissolve

    "[MCname] quickly falls asleep, reminiscing about the events leading up to this point."

    scene Black_Wall
    with fade

    if answerJane == "Yes":
        "After the wild series of events from the past few days, [MCname] continues to run the Does' farm in their \"absence\"."
        "Jane soon moves in with him and they live out the rest of their days in peace."
        "(With the exception of consistently feeding on the townspeople)"
        "The End"
        jump end

    elif answerJane == "No":
        "After the wild series of events from the past few days, [MCname] continues to run the Does' farm in their \"absence\", living out the rest of his days in peace."
        "(With the exception of consistently feeding on the townspeople)"

        "But if Jane was the one who someoned him, was she also behind that dark voice in his head? Or was it something else entirely?"
        "The End"
        jump end


label Johnny_And_Jane_Alive:

    scene Farmhouse_Day
    with fade

    show VampySprite at left
    with dissolve

    janed "Hey QT!"

    show JaneD at right
    with dissolve

    janed "Where are you headed off to?"

    menu:
        "I'm not sure yet, maybe work on the farm or head to town.":
            janed "Ooh busy day? Well I just had a quick thing to tell you before you leave."
        "I was actually on my way to see you.":
            janed "Wow really?! I'll be honest, I came here to see you too."
            janed "I have something important to tell you that I've been thinking about for a while."

    mc "Oh really, do you need help with something?"

    janed "Umm, well kind of. Can we go somewhere more private to talk?"

    mc "Sure we can take a walk to the forest near the farm."

    scene Sad_Farm_1
    with fade

    show VampySprite at left
    with dissolve

    show JaneD at right
    with dissolve

    "[MCname] and Jane walk awkwardly across the farm to reach the forest. Each sneaking glances at the other trying to read what they're thinking."

    menu:
        "...":
            "Jane catches [MCname]'s eye as he glances sideways at her, but quickly looks away."

        "I wonder what John is doing?":
            janed "Must be tending to the horses or something, I haven't seen him out here."

        "You're quite the interesting girl you know that?":
            janed "Ha ha, thats funny coming from the king of mystery himself."
            mc "It's not my fault, I don't even remember myself."
            janed "Well that's kind of the reason I wanted to talk to you to be honest."

        "Wow I'm starving. You look delicious.":
            janed "Oh my, you're quite forward aren't you. *blushes, misunderstanding what [MCname] meant*."
            mc "I could say the same to you with all the \"QTs\"."

    scene Creek_Bridge
    with fade

    show VampySprite at left
    with dissolve

    show JaneD at right
    with dissolve

    mc "Alright, this should be private enough. What was it you wanted to tell me?"

    janed "Isn't this the place that weird man always lurks around"

    mc "Who Johnny? Oh no, this is further up the stream from there. This is actually closer to where John Doe first found me."

    janed "I see, this place seems perfect then."

    janed "So you really don't remember who you are or where you came from then?"

    menu:
        "I honestly have no idea":
            janed "Well maybe I can try to explain some things."

        "Anna kept mentioning something about fate, but I don't know what that means":
            janed "I think fate may be part of it."

        "Do you know anything that might help?":
            janed "Actually I think so, that's what I came to talk to you about."

    mc "I'll gladly accept whatever information you have."

    janed "Well, I hope you don't get upset, but I may be the reason you showed up here."

    janed "To be honest, recently I've been really lonely."

    janed "This town is so small, but even then theres not many people my age who I'd be interested in."

    menu:
        "What does that have to do with me?":
            janed "Well you know you showed up out of the blue, coincidentally when I'm looking for a relationship."
        "Are you saying you're looking for a relationship?":
            janed "Um, yeah. This town doesn't really have many options is what I mean."
        "Can you get to the point? I have things to do.":
            janed "Sorry, sorry, I'm just kind of nervous."

    janed "So I had talked to Anna about summoning a vampire since I thought she'd know something to help me."
    janed "Unfortunately she didn't, but she gave me one of her grandmother's books, who was supposed to be a better psychic than her."
    janed "Anyway, I tried some things from the book, but nothing seemed to work so I gave up."
    janed "That was until you showed up in my store and said you were working for the Does."

    menu:
        "How did you know I wasn't a relative or friend from somewhere else?":
            janed "[MCname] this is a small town in the middle of nowhere North Dakota. No one would willingly take a vacation or move here."
            mc "You do have a point there. Though I'm still not sure I fully trust you."

        "So you're saying that you summoned me so you'd have someone to date?":
            janed "I know it sounds strange or desperate, but it's true. And interacting with you when I've had the chance has made me more sure of my decision."
            mc "Well I'm not saying talking to you hasn't been enjoyable, but is that enough to trust you."

        "Why would I believe that it was you, or that I was even summoned in the first place?":
            janed "But you are a vampire right? People started disappearing when you showed up, I'm guessing you had to feed."
            mc "That's not something I'd normally admit, but you seem to already know this. I'm still very skeptical of this situation."

    janed "That's ok, I understand, but if you just take this chance, I'll prove you can trust me."
    janed "So what do you think? Are you willing to give me a chance?"

    menu:
        "Sure I guess?":
            mc "I guess we can try, I don't see much risk in that. I am a vampire, I can just eat you if anything happens."
            $ answerJane = "Yes"
            $ dialogueChoice = 1

        "I've actually been interested in you too":
            mc "I'll be honest, I've been interested in you as well, so I think we can make this work."
            $ answerJane = "Yes"
            $ dialogueChoice = 1

        "This is quite weird":
            mc "Um it's kind of weird, so I'm going to have to decline, sorry."
            $ answerJane = "No"
            $ dialogueChoice = 2

        "Let your instincts take over":
            mc "Well you know I'm a vampire, and right now I'm feeling quite... hungry"
            $ answerJane = "No"
            $ dialogueChoice = 3

    if dialogueChoice == 1:
        janed "*To self* Oh my god yes, finally."
        janed "Thank you [MCname], I promise I'll gain your trust and show you I really care."

        mc "Hold on, if you summoned me what was that strange voice in my head talking about \"I have found you\" and \"my dreams lie within you\"?"
        janed "Wait you heard all of that? Oh that's embarrassing, the link when I summoned you must've lingered so you could hear what I was thinking."
        mc "Actually that's a relief. I was afraid it was increasing my hunger and driving me to kill more often."
        mc "And what about Anna, I hate to tell you this, but I was the one who killed her."
        janed "Oh I kind of expected it was you, but I'm not completely bothered by it. I became closer with her to find out more about summoning."
        janed "It was pretty hard to connect with her anyway. She was much older than me so we didn't share many common interests."
        mc "Well I apologize anyway, it's required that I feed to stay alive, but in that case I'm going to head back to the farm, you should come over sometime soon."
        janed "That sounds perfect [MCname], I'll be looking forward to it."

    elif dialogueChoice == 2:
        janed "Oh... Ok, I understand."
        janed "Well, it was worth a shot, sorry for taking up your time [MCname]."
        mc "Sorry, I need to get back to the farm."

    elif dialogueChoice == 3:
        janed "Wait what..."
        janed "Please no, I didn't mean for this to happ-"
        "Jane is cut off abruptly as [MCname]'s hunger drives him into a frenzy."
        mc "She was right, secluded, no one around, this place was perfect."
        "After feeding on Jane, [MCname] heads back to the farm to rest."


    scene Farmhouse_Bed
    with fade

    show VampySprite at left
    with dissolve

    mc "Well I have a lot to think about. It's getting late though so I'll sleep on it for now."

    hide VampySprite
    with dissolve

    "[MCname] quickly falls asleep, reminiscing about the events leading up to this point."

    scene Black_Wall
    with fade

    if answerJane == "Yes":
        "After the wild series of events from the past few days, [MCname] continues to run the Does' farm in their \"absence\"."
        "Jane soon moves in with him and they live out the rest of their days in peace."
        "(With the exception of consistently feeding on the townspeople)"
        "The End"
        jump end

    elif answerJane == "No":
        "After the wild series of events from the past few days, [MCname] continues to run the Does' farm in their \"absence\", living out the rest of his days in peace."
        "(With the exception of consistently feeding on the townspeople)"

        "But if Jane was the one who someoned him, was she also behind that dark voice in his head? Or was it something else entirely?"
        "The End"
        jump end


label MC_Back_Home_Does_Alive:

    jd "[MCname] you're back!"

    show JD at right
    with dissolve

    jd "Jannet and I need to talk to you. Let's head inside."

    scene Farmhouse_Bed
    with fade

    show JDW at right
    with dissolve

    show JD at center
    with dissolve

    show VampySprite at left
    with dissolve

    jdw "So [MCname], you've been helping us out for a while without asking for anything in return."
    jdw "John and I decided we could use your help for a bit longer, with pay of course."
    jdw "At least until we can help you get set up with a farm of your own, if that's something you'd be interested in."

    mc "Really? Are you serious?"

    jd "It's true [MCname]. I'll admit, I was skeptical when Jannet first brought it up to me, but after mulling it over a bit I agreed."
    jd "Jannet and I aren't the spring chickens we used to be. Your help working on the farm and gathering supplies really lightened the load for us."

    jdw "What do you think [MCname]? Maybe one day you'll have your own farm and possibly take over for us when we can't keep it up anymore."

    menu:
        "Agree to take on the job and secure a future for yourself":
            $ dialogueChoice = 1
        "Decline the offer but continue helping out on the farm until you find a true calling":
            $ dialogueChoice = 2
        "Decline the offer and part ways with the Doe couple to set out on your own":
            $ dialogueChoice = 3
        "Give in to your darkest instincts and take the farm for yourself":
            $ dialogueChoice = 4

    if dialogueChoice == 1:
        mc "I can't pass up on this opportunity, I promise I'll keep up the hard work."
        mc "You two have been nothing but kind to me, even when I didn't know where I came from, I can't thank you enough."

        hide VampySprite
        with dissolve

        "[MCname] heads to bed after a long but exciting day."

        jd "Wait, does that mean he found out where he came from?"
        jdw "I have no idea honey, he's quite the mystery isn't he."

        scene Farmhouse_Night
        with fade

        "[MCname] continues working on the Doe farm and saving up money for the next couple years."
        "Eventually, with some help from the Does, he purchases one of the shutdown farms and \"peacefully\" lives out his life."
        "What, did you forget he was a vampire? He's got to satisfy his instincts somehow."

        scene Black_Wall
        with fade

        "Then again, what did happen to that dark voice? Was it really just [MCname]'s deepest instincts?"
        "The End"
        jump end

    elif dialogueChoice == 2:
        mc "I'm sorry, I can't accept your payment. I am very grateful for the offer and I have thoroughly enjoyed the time I've spent here."
        mc "I know my true calling is elsewhere, however, but I'll provide all the help I can until it is my time to depart."

        hide VampySprite
        with dissolve

        "[MCname] heads to bed after a long but exciting day."

        jdw "What an interesting man Honey."
        jd "Hey, at least we still don't have to pay him."

        scene Farmhouse_Night
        with fade

        "[MCname] continues working on the Doe farm until the day comes for him to head off on his own."
        "Who knows where his path will take him from here."

        scene Black_Wall
        with fade

        "Whatever did happen to that dark voice? Was it really just [MCname]'s deepest instincts?"
        "The End"
        jump end

    elif dialogueChoice == 3:
        mc "I apologize that I'm only bringing this up now, but I've been planning to head out on my own recently."
        mc "I appreciate everything you two have done for me, but I don't want to overstay my welcome."

        jdw "Are you sure [MCname]? You've been a huge help around the farm, you're perfectly welcome here."
        jd "Where do you plan on going anyway?"

        mc "Truth be told, I'm not quite so sure myself, but I know there's a life waiting for me out there."

        hide VampySprite
        with dissolve

        "[MCname] heads to bed after a long but exciting day."

        scene Farmhouse_Day
        with fade

        "The next day [MCname] gathers up what little belongings he has and prepares some supplies for the road."
        "After a quick farewell to the Does he sets off on his own to discover what life has in store for him."

        scene Black_Wall
        with fade

        "But what did happen to that dark voice? Was it really just [MCname]'s deepest instincts?"
        "The End"
        jump end

    elif dialogueChoice == 4:
        mc "It was a delightful offer, but honestly..."
        mc "... you two are looking quite delicious and after today I am Starving."

        jdw "Huh?"
        jd "What is that supposed to mea-"

        "John is cut off as [MCname] lunges towards him before he has a chance to grab his rifle."

        hide JD
        with dissolve

        jdw "John was right! What are you!?"

        "Jannet barely gets out a sentence before [MCname] turns to her and treats her with the same aggression he showed her husband."

        hide JDW
        with dissolve

        mc "Why keep up the tedious labor and wait when I could have everything now?"

        "[MCname] inquires to the now empty room."
        "After finishing feasting on his former hosts, [MCname] heads to bed."

        scene Farmhouse_Night
        with fade

        "With the Does out of the way, [MCname] takes over the farm and lives unrestricted for the rest of his days."
        "Of course, the townspeople began to notice the Does' absence and rumors started circulating."
        "But they were all too quick to believe [MCname] was a distant relative, watching over the farm while the Does travelled abroad."

        scene Black_Wall
        with fade

        "But was it that dark voice that caused [MCname]'s frenzy that night? What really was that voice?"
        "The End"
        jump end
