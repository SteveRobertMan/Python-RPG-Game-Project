from rich.panel import Panel
from rich.text import Text
from rich.align import Align
import config 

def show_story_box(speaker, text, affiliation="", is_thought=False, is_narrator=False, color_override=None):
    """
    Renders a single dialogue box.
    """
    config.console.clear()
    
    # Narrator Style
    if is_narrator:
        box_color = "white"
        text_style = "italic white"
        header = None 
        
        panel = Panel(
            Text(text, style=text_style),
            title=header,
            border_style=box_color,
            padding=(1, 2)
        )
    else:
        # Character Style
        if color_override:
            box_color = color_override
        else:
            # --- UNIQUE CHARACTER COLORS ---
            if speaker == "Akasuke":
                box_color = "bright_red"
            elif speaker == "Yuri":
                box_color = "sky_blue1"
            elif speaker == "Shigemura":
                box_color = "plum2"
            elif speaker == "Yamashita":
                box_color = "purple"
            elif speaker == "Naganohara":
                box_color = "magenta"
            elif speaker == "Benikawa" or speaker == "Ayame Benikawa":
                box_color = "orange1"
            elif speaker == "Nishida":
                box_color = "tan"
            elif speaker == "Kojima-sensei":
                box_color = "dodger_blue2"
            elif speaker == "Kageyama":
                box_color = "cyan"
            elif speaker == "Natsume" or speaker == "Yokubukai Natsume":
                box_color = "navy_blue"
            elif speaker == "Hana":
                box_color = "gold1"
            elif speaker == "Masayoshi":
                box_color = "cornflower_blue"
            elif speaker == "Kagaku":
                box_color = "dark_green"
            elif speaker == "Forest Guardian Ayako":
                box_color = "royal_blue1"
            elif speaker == "Lake Strider Sumiko":
                box_color = "gold3"
            elif speaker == "Nocturnal Companion Rina":
                box_color = "sky_blue2"
            elif speaker == "Aina":
                box_color = "plum2"
            elif speaker == "Hisayuki":
                box_color = "orange_red1"
            elif speaker in ["Young Man", "Adam"]:
                box_color = "cyan1"
            elif speaker == "Rara":
                box_color = "khaki1"
            elif speaker == "Midori":
                box_color = "green3"
            elif speaker == "Fuyuki":
                box_color = "turquoise2"
            elif speaker in ["Boss of Riposte", "Kesler"]:
                box_color = "blue_violet"
            elif speaker == "Hazuki":
                box_color = "sea_green2"
            
            # --- COMMON ENEMY CHARACTERS ---
            elif speaker in ["Underwear Thief", "Freshman 1", "Freshman 2", "Freshman 3", "Goons", "Gang Member 1", "Gang Member 2", "Gang Member 3", "Gang Member 4", "Henchman A", "Henchman B"]:
                box_color = "red"
            elif speaker in ["Raven", "Falcon", "Eagle"]:
                box_color = "dark_violet"

            # --- DEFAULTS / MINOR CHARACTERS ---
            elif speaker in ["Hanefuji Kurona", "Kiryoku Girl 1", "Kiryoku Girl 2", "Kiryoku Girl 3", "Council Aide", "Committee Member A", "Committee Member B", "Staff Teacher"]:
                box_color = "green"
            else:
                box_color = "white"
            # -------------------------------
            
        text_style = "white"
        if is_thought:
            text = f"({text})"
            text_style = "italic white"
        
        header = f"[bold {box_color}]{speaker}[/bold {box_color}]"
        if affiliation:
            header += f" [dim gray]<{affiliation}>[/dim gray]"

        panel = Panel(
            Text(text, style=text_style),
            title=header,
            title_align="left",
            border_style=box_color,
            padding=(1, 2)
        )
    
    config.console.print(Align.center(panel, vertical="middle"))
    config.console.input("[dim]Press Enter to advance...[/dim]")

def play_prologue():
    show_story_box("???", "There! Behind the gym, Yuri-chan!", color_override="bright_red")
    
    show_story_box("", "It was low, confident, and laced with burning irritation. Heavy boots thundered against the gravel.", is_narrator=True)
    
    show_story_box("Yuri", "Akasuke-kun, wait! Don't kick him in the face yet!", affiliation="Kasakura High School Student")
    show_story_box("", "Another voice—higher, lively, and athletic—echoed after the first.", is_narrator=True)
    
    show_story_box("Yuri", "We need him conscious!", affiliation="Kasakura High School Student")
    
    show_story_box("", "The thief's breath caught. That voice again. Those two had been hunting him every night for three days now.", is_narrator=True)
    show_story_box("", "They were supposed to be students.", is_narrator=True, is_thought=True)

    show_story_box("Akasuke", "Block off the left!", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "Already there!", affiliation="Kasakura High School Student")

    show_story_box("Underwear Thief", "Why are they so fast?!")
    
    show_story_box("", "The answer came a second later—in the form of a high-speed judo sweep from behind.", is_narrator=True)
    
    show_story_box("Yuri", "Gotcha!", affiliation="Kasakura High School Student")
    show_story_box("Underwear Thief", "GUH..!! I’m not going down without a fight!")

def play_stage_1_1_story():
    # Intro
    show_story_box("???", "Good work as always, you two.")
    show_story_box("", "The man named Kageyama adjusted his glasses with a sheepish smile... His raven-black hair was slicked back with near obsessive neatness...", is_narrator=True)
    show_story_box("", "He looked like someone who’d never raised his voice in his life—and probably hadn’t. But his words often carried the weight of silent authority.", is_narrator=True)
    
    show_story_box("Akasuke", "You say it like this isn’t the third time this week.", affiliation="Kasakura High School Student")
    show_story_box("", "Akasuke muttered, brushing dirt from his red coat. His tone was sharp, but controlled... The black eyepatch covering his left eye made his scowl look even more intense...", is_narrator=True)
    show_story_box("", "He was tall, broad-shouldered, and carried himself like a seasoned fighter... When he rolled his neck with a dry crack, the thief on the ground whimpered audibly.", is_narrator=True)
    
    show_story_box("Kageyama", "Technically, you volunteered.", affiliation="Kasakura High School Student Council")
    
    show_story_box("Yuri", "Ya voluntold us.", affiliation="Kasakura High School Student")
    show_story_box("", "Yuri had just finished tying the unconscious thief’s arms behind his back with a suspiciously professional knot.", is_narrator=True)
    show_story_box("", "Yuri had the look of a tomboy who could bench-press her problems... She clapped her hands clean and stretched lazily...", is_narrator=True)
    
    show_story_box("Yuri", "Ya said, and I quote…", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "‘The Disciplinary Committee is swamped with real threats. Please help us deal with this low-level pest.’", affiliation="Kasakura High School Student")
    
    show_story_box("Kageyama", "That does sound like me.", affiliation="Kasakura High School Student Council")
    show_story_box("Yuri", "Ya owe us melon bread for this. The good kind. From the station.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "At least.", affiliation="Kasakura High School Student")
    show_story_box("Kageyama", "Fine. I’ll buy you both melon bread. And juice. Please don’t write another complaint letter.", affiliation="Kasakura High School Student Council")
    
    show_story_box("", "********* ◆ *********\nAkasuke’s POV", is_narrator=True)
    show_story_box("", "By the time the whole thing was dealt with, it was already dark out.", is_narrator=True)
    
    show_story_box("Yuri", "Hah…that was exhaustin’.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Yeah. The guy was surprisingly fast for an underwear thief.", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "Even though ya could easily catch ‘im and save us the trouble if ya had seriously run…", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Haha, sorry about that.", affiliation="Kasakura High School Student")
    
    show_story_box("", "It had been like this since our first year. Getting dragged into matters that should have been handled by the student council.", is_narrator=True)
    
    show_story_box("Yuri", "Next time, end it quicker.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Noted.", affiliation="Kasakura High School Student")
    
    show_story_box("", "We walked in comfortable silence for a moment. The night air was cool, the streets empty.", is_narrator=True)
    
    show_story_box("Akasuke", "It’s pretty late. How about staying at my place?", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "Mm! It’s a pain waitin’ for the train alone at night anyway.", affiliation="Kasakura High School Student")
    
    show_story_box("", "We’ve been together since childhood. So long to the point where we could casually invite each other to have a sleepover.", is_narrator=True)
    
    show_story_box("Yuri", "Hold on a minute, I gotta tell ma first.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Take your time.", affiliation="Kasakura High School Student")
    
    show_story_box("", "Yuri stepped a few paces away, turning on her phone. Her voice dropped into that gentle, sing-song Kansai she only ever used with her family.", is_narrator=True)
    
    show_story_box("Yuri", "Ma? Yeah, it’s me. I’m stayin’ over at Akasuke-kun’s again. Mmhm. Nah, nothin’ weird. We caught a weirdo. Again. …Yeah, ya believe that? …All right. Tell Pops I said hi. Love ya.", affiliation="Kasakura High School Student")
    
    show_story_box("Yuri", "She said I better not be causin’ trouble for ya.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Yep, better listen to your mom.", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "Oi, what’s that supposed to mean?", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Kidding~.", affiliation="Kasakura High School Student")
    
    show_story_box("", "The walk home was quiet for the most part. Yuri was walking a little bit ahead of me... We turned the corner.", is_narrator=True)
    
    show_story_box("Akasuke", "Yuri. You got something on your face.", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "Huh? Where?", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "Did that creep smear somethin’ on me? I swear if it’s—", affiliation="Kasakura High School Student")
    
    show_story_box("", "Akasuke reached out, brushing his thumb just under her eye. A smudge of dirt from where she caught the guy.", is_narrator=True)
    
    show_story_box("Akasuke", "There. Got it.", affiliation="Kasakura High School Student")
    show_story_box("", "Yuri’s hands froze midair. And then her face lit up red.", is_narrator=True)
    
    show_story_box("Yuri", "Y-ya can’t just…d-do stuff like that all casual-like…", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Ah…sorry. Habit, I guess.", affiliation="Kasakura High School Student")
    
    show_story_box("", "She didn’t say anything more. But she slowed her pace down just so we could walk side-by-side.", is_narrator=True)
    
    show_story_box("", "********* ◆ *********\nYuri’s POV", is_narrator=True)
    show_story_box("Yuri", "Stupid Akasuke... My heart hadn’t stopped racin’ since he wiped that dirt off my face.", affiliation="Kasakura High School Student", is_thought=True)
    show_story_box("Yuri", "‘Habit,’ he says…", affiliation="Kasakura High School Student")
    
    show_story_box("", "When we turned the last corner toward his house, the porch light was already on. Before Akasuke-kun could even reach the gate—", is_narrator=True)
    
    show_story_box("Hanefuji Kurona", "Welcome back, Onii-chan!", affiliation="Hanefuji Family")
    show_story_box("Akasuke", "Ack! Kurona!?", affiliation="Kasakura High School Student")
    
    show_story_box("", "Akasuke barely caught the flyin’ gremlin that was his little sister... Hanefuji Kurona, the middle school devil and chaos incarnate...", is_narrator=True)
    
    show_story_box("Hanefuji Kurona", "You’re late! I’m starving here! Did you get stabbed!?", affiliation="Hanefuji Family")
    show_story_box("Akasuke", "No. We just caught another thief.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Why are you outside?", affiliation="Kasakura High School Student")
    
    show_story_box("Hanefuji Kurona", "Because I was about to go to the convenience store to buy something because you weren’t here! Then I saw you from afar so I thought of scaring yo—youch!", affiliation="Hanefuji Family")
    
    show_story_box("", "Akasuke pinched her left cheek. After that he decided to play with it just to get back at her.", is_narrator=True)
    
    show_story_box("Hanefuji Kurona", "Yhuri-nhee~, help me~", affiliation="Hanefuji Family")
    show_story_box("", "And so, as a good big sister I was, I joined in pinching her right.", is_narrator=True)
    
    show_story_box("Hanefuji Kurona", "Argh! You bohth are sho meahn!", affiliation="Hanefuji Family")
    show_story_box("Akasuke", "Be a good girl and apologize.", affiliation="Kasakura High School Student")
    show_story_box("Hanefuji Kurona", "I’m showwy…pleash forghive me.", affiliation="Hanefuji Family")
    show_story_box("Akasuke", "Good.", affiliation="Kasakura High School Student")
    
    show_story_box("", "Kurona puffed up her cheeks while rubbing them after we let go, tears welling up in her eyes.", is_narrator=True)
    
    show_story_box("Hanefuji Kurona", "I’m telling grandma…", affiliation="Hanefuji Family")
    show_story_box("Akasuke", "If you do, I won’t be cooking tonight.", affiliation="Kasakura High School Student")
    show_story_box("Hanefuji Kurona", "Geh!?", affiliation="Hanefuji Family")
    
    show_story_box("", "Kurona then walked back into the house, dejected.", is_narrator=True)
    
    show_story_box("Akasuke", "Hah…and she used to be such a cute girl.", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "Well, kids grow right?", affiliation="Kasakura High School Student")
    
    show_story_box("", "We stepped inside. I got hit with scents of spices and warm rice. They reminded me why I love staying over.", is_narrator=True)

def play_stage_1_2_start():
    # Akasuke's POV - Morning
    show_story_box("", "The alarm buzzed at 5 AM sharp.", is_narrator=True)
    show_story_box("Akasuke", "Yeah yeah…", affiliation="Kasakura High School Student")
    show_story_box("", "I muttered, turning it off. The house was quiet, peaceful even, save for Kurona snoring upstairs...", is_narrator=True)
    
    show_story_box("", "I got up from the couch—my back protested with a dull ache... I didn’t mind. It wasn’t the first time.", is_narrator=True)
    show_story_box("", "After splashing cold water on my face, I changed into running gear and slipped out silently.", is_narrator=True)
    
    show_story_box("", "The streets were dark, silent... I ran my usual route... Fifteen minutes in, I reached the park.", is_narrator=True)
    show_story_box("", "Two hundred sit-ups. One hundred fifty push-ups. Two hundred squats. Two-minute plank.", is_narrator=True)
    show_story_box("", "Then kata—Taikyoku through Jion... Hellish training that forged what I am now.", is_narrator=True)
    
    show_story_box("", "Stretching finished, I jogged back. Watch read 6:45 AM. Earlier than usual.", is_narrator=True)
    show_story_box("", "By 7 AM I was in uniform, apron on, in the kitchen.", is_narrator=True)
    show_story_box("", "Gyudon, simple and quick... The smell hit hard.", is_narrator=True)
    
    show_story_box("Akasuke", "Sometimes my genius frightens me.", affiliation="Kasakura High School Student")
    show_story_box("", "Now the hard part: waking them.", is_narrator=True)
    
    # Waking Kurona
    show_story_box("", "First, Kurona. I knocked hard.", is_narrator=True)
    show_story_box("Akasuke", "Kurona, wake up. Or you’ll be late.", affiliation="Kasakura High School Student")
    show_story_box("", "Snoring.", is_narrator=True)
    show_story_box("Akasuke", "Breakfast is ready. Come before it gets cold.", affiliation="Kasakura High School Student")
    show_story_box("", "Still snoring.", is_narrator=True)
    
    show_story_box("Akasuke", "Alright. You asked for it.", affiliation="Kasakura High School Student")
    show_story_box("", "I swung the door open. Chaos... I kicked—controlled, precise. She landed perfectly on a pillow.", is_narrator=True)
    show_story_box("Akasuke", "Hanefuji Family Waking Technique: Awakening Kick!", affiliation="Kasakura High School Student")
    
    show_story_box("Hanefuji Kurona", "GAH!", affiliation="Hanefuji Family")
    show_story_box("Hanefuji Kurona", "Onii-chan, what the heck!?", affiliation="Hanefuji Family")
    
    show_story_box("Akasuke", "I’ve been calling you. And what is this mess? I told you to clean last week.", affiliation="Kasakura High School Student")
    show_story_box("Hanefuji Kurona", "Ugh…I-I was busy.", affiliation="Hanefuji Family")
    show_story_box("Akasuke", "Whatever. Talk after school. Dress properly and come eat.", affiliation="Kasakura High School Student")
    show_story_box("Hanefuji Kurona", "Y-yes, aniue…", affiliation="Hanefuji Family")
    show_story_box("Akasuke", "Being formal won’t lessen the scolding.", affiliation="Kasakura High School Student")
    
    # Waking Yuri
    show_story_box("", "Next: Yuri. I knocked gently.", is_narrator=True)
    show_story_box("Akasuke", "Yuri. It’s 7. Wake up.", affiliation="Kasakura High School Student")
    show_story_box("", "Rustling. Nothing else.", is_narrator=True)
    show_story_box("Akasuke", "Get up. Or I’m coming in.", affiliation="Kasakura High School Student")
    show_story_box("", "Silence. I opened the door slowly.", is_narrator=True)
    
    show_story_box("", "She was curled in my futon... Silver hair loose... Wearing my oversized shirt, a shoulder slipped bare.", is_narrator=True)
    show_story_box("", "I froze.", is_narrator=True)
    
    show_story_box("Akasuke", "…So beautiful…", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "Mnngh…?", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "Akasuke-kun… g’mornin’.", affiliation="Kasakura High School Student")
    
    show_story_box("Akasuke", "Hey… Breakfast is ready. Get ready or we’ll be late.", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "M’kay…", affiliation="Kasakura High School Student")
    
    show_story_box("", "She sat up slowly, rubbing her eyes.", is_narrator=True)
    show_story_box("Akasuke", "I-I’ll wait downstairs.", affiliation="Kasakura High School Student")
    show_story_box("", "I turned and left quickly.", is_narrator=True)
    show_story_box("Akasuke", "Seriously, what was wrong with me?", affiliation="Kasakura High School Student")
    
    # Walk to School
    show_story_box("", "After breakfast, we left. Kurona split off near the old cigarette shop, waving lazily.", is_narrator=True)
    show_story_box("Hanefuji Kurona", "Don’t cause trouble, okay?", affiliation="Hanefuji Family")
    show_story_box("Akasuke", "I won’t even if you don’t tell me!", affiliation="Kasakura High School Student")
    
    show_story_box("", "She bolted toward middle school.", is_narrator=True)
    show_story_box("Akasuke", "Alright… let’s go, Yuri.", affiliation="Kasakura High School Student")
    
    show_story_box("Yuri", "Ugh…I don’t wanna sit through class again…", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Ditto. First period is history.", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "I swear the teacher’s tryin’ to put us all into cryo-sleep.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Right? Ancient tax systems. Useless unless we time-travel.", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "In which case, I’d open my own dojo and get rich.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Honestly, I can respect that.", affiliation="Kasakura High School Student")
    
    show_story_box("", "We laughed quietly.", is_narrator=True)
    show_story_box("Yuri", "But really, I’m lookin’ forward to club hours. Been wantin’ to try that move I saw online.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Fake low, pivot mid-grab?", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "Ya saw it too!?", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Yeah. Pretty amazing. You could pull it off.", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "Ya say that ’cause it’s me, or ’cause ya wanna see someone get slammed?", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "…I have the right not to answer.", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "Knew it.", affiliation="Kasakura High School Student")
    
    show_story_box("Akasuke", "But yeah, I’m looking forward to it too. Haven’t been to club in a while because prez kept calling us. Can’t wait to beat those guys up again.", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "Who’re ya sparrin’ with today?", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Probably Benikawa again. That girl never gives up.", affiliation="Kasakura High School Student")
    
    show_story_box("", "Yuri went quiet and looked away. She kicked a pebble.", is_narrator=True)
    show_story_box("Akasuke", "Yuri?", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "H-Huh? What?", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "You went quiet.", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "Nothin’… just spaced out.", affiliation="Kasakura High School Student")
    
    show_story_box("", "Obvious lie. She always kicked pebbles when hiding something.", is_narrator=True)
    show_story_box("Akasuke", "Do you dislike Benikawa?", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "H-Hah!? Why would I? I-I don’t even know her that much!", affiliation="Kasakura High School Student")
    show_story_box("", "Ears red.", is_narrator=True)
    
    show_story_box("Akasuke", "Uh-huh. You sure? You always react when I say her name.", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "I do not!", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Yuri.", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "What.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Do you dislike her?", affiliation="Kasakura High School Student")
    
    show_story_box("Yuri", "I told ya it’s not like I don’t like her! I….I just…", affiliation="Kasakura High School Student")
    show_story_box("", "Long pause.", is_narrator=True)
    show_story_box("Yuri", "I just don’t like the way she looked at ya.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "…Huh?", affiliation="Kasakura High School Student")
    
    show_story_box("Yuri", "She always stares. Laughs too much at your jokes. Challenges ya all the way to our class… That’s all.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "…", affiliation="Kasakura High School Student")
    show_story_box("", "I didn’t respond. Didn’t know what to say.", is_narrator=True)
    
    show_story_box("", "The bell rang in the distance.", is_narrator=True)
    show_story_box("Yuri", "Crap! The bell’s ringin’!", affiliation="Kasakura High School Student")
    show_story_box("", "She grabbed my wrist.", is_narrator=True)
    show_story_box("Yuri", "C’mon, if we’re late, the gate’ll close!", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "O-oi!", affiliation="Kasakura High School Student")
    show_story_box("", "Too late. She sprinted, dragging me along.", is_narrator=True)
    show_story_box("Yuri", "Move those legs, Akasuke-kun! I am not doin’ another dogeza in front of the attendance lady!", affiliation="Kasakura High School Student")
    show_story_box("", "The moment slipped away.", is_narrator=True)
    
    # Evening
    show_story_box("", "Evening – After Classes", is_narrator=True)
    show_story_box("Kageyama", "Akasuke. Yuri. A moment.", affiliation="Kasakura High School Student Council")
    show_story_box("", "We were summoned to the student council room just as the sun dipped low. Kageyama stood at the window, backlit, arms crossed.", is_narrator=True)
    
    show_story_box("Kageyama", "Its just a small situation. Three freshmen—class-skippers. They’ve been loitering behind the old science building, intimidating underclassmen and picking fights.", affiliation="Kasakura High School Student Council")
    show_story_box("Kageyama", "The Disciplinary Committee is tied up with a larger incident. I need you two to handle it. No excessive force. Just make them understand they need to return to class.", affiliation="Kasakura High School Student Council")
    
    show_story_box("Akasuke", "Understood.", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "Finally, somethin’ straightforward.", affiliation="Kasakura High School Student")
    
    show_story_box("", "We left immediately. The back of the campus was shadowed... Three freshmen—uniforms untucked, cigarettes, smirks—leaned against the wall.", is_narrator=True)
    
    show_story_box("Freshman 1", "Look who’s here. The council’s pet fighters.", affiliation="Kasakura High School Freshman")
    show_story_box("Freshman 2", "Heard you two took down that thief last week. Think you’re tough?", affiliation="Kasakura High School Freshman")
    
    show_story_box("Akasuke", "We’re not here to play. Return to class. Now.", affiliation="Kasakura High School Student")
    show_story_box("Freshman 3", "Or what? ‘You gonna cry to ‘prez?", affiliation="Kasakura High School Freshman")
    
    show_story_box("", "Yuri stepped forward first.", is_narrator=True)
    show_story_box("Yuri", "Last warning.", affiliation="Kasakura High School Student")
    show_story_box("", "The freshmen smiled, then lunged with sloppy punches, overconfident.", is_narrator=True)

def play_stage_1_2_end():
    show_story_box("Akasuke", "You three have two choices. Walk back to class under your own power… or we carry you. Your decision.", affiliation="Kasakura High School Student")
    show_story_box("", "The freshmen froze. Eyes wide.", is_narrator=True)
    show_story_box("Freshman 1", "…We’re going.", affiliation="Kasakura High School Freshman")
    
    show_story_box("", "They scrambled away, heads low. Yuri dusted her hands.", is_narrator=True)
    
    show_story_box("Yuri", "That was too easy.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "They’re freshmen. They talk big until someone bigger shows up.", affiliation="Kasakura High School Student")
    
    show_story_box("", "We headed back toward the main building, the evening light fading.", is_narrator=True)
    
    show_story_box("Yuri", "Still…it felt good to stretch my legs a little.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Yeah. Been a while since we fought.", affiliation="Kasakura High School Student")

def play_stage_1_3_story():
    # Scene 1: Classroom
    show_story_box("Kojima-sensei", "Did you know that people whose hair weren't black or brown used to get hunted back in the day?", affiliation="Kasakura High School Teacher")
    show_story_box("", "The history teacher started the first period with that line. A few students looked up from their textbooks, caught off guard.", is_narrator=True)
    
    show_story_box("Classmate", "Hunted?", affiliation="")
    show_story_box("", "Someone muttered from the back.", is_narrator=True)
    
    show_story_box("Kojima-sensei", "Believe it or not, back in the day, people could only be born with black, brown, blonde, white, red, and gray hair.", affiliation="Kasakura High School Teacher")
    show_story_box("", "Classmates tilted their heads. A girl with teal hair near the window blinked.", is_narrator=True)
    
    show_story_box("Kojima-sensei", "Alright, pipe down. I know it sounds ridiculous now. But before the 1600s, there were no records—none at all—of natural hair or eye colors outside some limited range.", affiliation="Kasakura High School Teacher")
    show_story_box("Kojima-sensei", "Then, sometime in the early 17th century, the phenomenon began. Around the world, children started being born with other colors—blue, apple-shaded red, green, violet—and with no reason or genetic cause. Scientists still haven’t found the exact answer.", affiliation="Kasakura High School Teacher")
    
    show_story_box("", "He tapped the chalkboard. “Chromatic Divergence Phenomenon” was written in neat kanji.", is_narrator=True)
    
    show_story_box("Kojima-sensei", "Nowadays, we take it for granted. But back then, it was seen as a curse, or an omen.", affiliation="Kasakura High School Teacher")
    show_story_box("Kojima-sensei", "Entire villages drove out families with children who had unusual features. In Europe, they were labeled as changelings. In Edo-period Japan, some were even accused of being yokai in disguise.", affiliation="Kasakura High School Teacher")
    
    # Yuri's Internal Monologue
    show_story_box("Yuri", "I should’ve been taking notes. I really should’ve.", affiliation="Kasakura High School Student", is_thought=True)
    show_story_box("", "I looked down at the ends of my silver ponytail.", is_narrator=True)
    show_story_box("Yuri", "Yeah. I guess I’d be labeled a demon too, huh?", affiliation="Kasakura High School Student", is_thought=True)
    
    show_story_box("", "Still, it wasn’t the weird history that had my chest feeling tight. It was something else.", is_narrator=True)
    
    show_story_box("Yuri", "I don’t like the way she looks at ya.", affiliation="Kasakura High School Student", is_thought=True)
    show_story_box("Yuri", "That dumb line was still ringing in my head. Benikawa.", affiliation="Kasakura High School Student", is_thought=True)
    
    show_story_box("Yuri", "I ain’t gonna say I hate her or anything. That’d be petty.", affiliation="Kasakura High School Student", is_thought=True)
    show_story_box("Yuri", "But every time I see her hanging around Akasuke-kun with that soft smile and the way she leans in when she talks to him—", affiliation="Kasakura High School Student", is_thought=True)
    show_story_box("Yuri", "Ugh…I was doing it again… Get it together, Yuri.", affiliation="Kasakura High School Student", is_thought=True)
    
    show_story_box("Yuri", "What’s wrong with me? I mean, it’s not like we’re together… Me and Akasuke-kun.", affiliation="Kasakura High School Student", is_thought=True)
    show_story_box("Yuri", "We’re just childhood friends, training partners, fellow fighters. But then again.", affiliation="Kasakura High School Student", is_thought=True)
    
    show_story_box("Yuri", "Not everyone wipes dirt off your face so gently it makes your whole head go blank. And not everyone looks at you like you matter more than dinner.", affiliation="Kasakura High School Student", is_thought=True)
    
    show_story_box("", "I slouched a little in my seat, resting my chin in my hand, staring at Akasuke-kun’s back a few seats ahead.", is_narrator=True)
    show_story_box("", "He sat straight as always, jotting notes down in that calm, quiet way of his. So focused. So steady.", is_narrator=True)
    
    show_story_box("Kojima-sensei", "Inami.", affiliation="Kasakura High School Teacher")
    show_story_box("Yuri", "Eh–whuhh!?", affiliation="Kasakura High School Student")
    show_story_box("", "I nearly fell out of my chair.", is_narrator=True)
    
    show_story_box("Kojima-sensei", "Can you repeat what I just said about the European terminology for children born with chromatic traits?", affiliation="Kasakura High School Teacher")
    show_story_box("Yuri", "U-Uh… C-Changelings?", affiliation="Kasakura High School Student")
    show_story_box("Kojima-sensei", "Correct. But stop spacing out next time. I’m gonna make you write a report if you fall behind.", affiliation="Kasakura High School Teacher")
    show_story_box("Yuri", "Y-Yes sensei…", affiliation="Kasakura High School Student")
    
    show_story_box("Yuri", "Great. Now I’m jealous and embarrassed. I want to dig a hole and hide.", affiliation="Kasakura High School Student", is_thought=True)
    
    show_story_box("", "********* ◆ *********\nAkasuke’s POV", is_narrator=True)
    
    # Akasuke's Lunch Scene
    show_story_box("Kojima-sensei", "That will be all for today. Enjoy your lunch.", affiliation="Kasakura High School Teacher")
    show_story_box("", "…Finally, after four long periods, lunch break was here. To be perfectly honest, other than history class, I completely zoned out.", is_narrator=True)
    show_story_box("", "Anyway, better hurry up before that special curry runs out. It’s been pretty popular among students lately and I’ve been dying to try it myself.", is_narrator=True)
    
    show_story_box("Akasuke", "Shigemura, Nishida! Let’s go get lunch.", affiliation="Kasakura High School Student")
    
    show_story_box("", "Shigemura looked up from his book, purple eyes tired as ever.", is_narrator=True)
    show_story_box("Shigemura", "Can that wait until I finish this page?", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Nuh uh. I let you last time and we missed the limited edition nikujaga jumbo-sized! I can’t let that happen again.", affiliation="Kasakura High School Student")
    show_story_box("Nishida", "I think we should listen to him. Hanefuji is a big foodie, he’ll chew us out if he misses it again this time.", affiliation="Kasakura High School Student")
    show_story_box("Shigemura", "Ugh…that would be a pain.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "If you don’t want that, then you better come with me.", affiliation="Kasakura High School Student")
    
    show_story_box("", "So with that, I led my gang to the cafeteria.", is_narrator=True)
    show_story_box("", "Our school would sometimes make special dishes for us students in a limited amount. And of course, I, as a certified food lover, have to try all of it.", is_narrator=True)
    show_story_box("", "But eating alone wouldn’t be very fulfilling so I also have to bring my friends along to enjoy it together. Yuri-chan is always with her own friend group so I brought these guys every time.", is_narrator=True)
    
    show_story_box("Akasuke", "Curry…curry~♪", affiliation="Kasakura High School Student")
    show_story_box("", "I hummed excitedly while practically skipping through the hallway... A girl wearing glasses from one of the groups in the hallway shouted.", is_narrator=True)
    
    show_story_box("Girl", "Ah- Hanefuji-senpai!", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Hm? Can I help you?", affiliation="Kasakura High School Student")
    show_story_box("Girl", "U-Um…! W-Would you…accept this…!?", affiliation="Kasakura High School Student")
    show_story_box("", "She handed a bento box to me.", is_narrator=True)
    
    show_story_box("Akasuke", "…This is…!", affiliation="Kasakura High School Student")
    show_story_box("", "Just from the smell alone I could tell that it was made with love and care.", is_narrator=True)
    
    show_story_box("Akasuke", "This is…for me?", affiliation="Kasakura High School Student")
    show_story_box("Girl", "Y-Yes! I-I made it myself and I want you to have it! A-and, um! About the box…you can keep it.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Really!? Thanks! I’ll gladly accept it then~!", affiliation="Kasakura High School Student")
    
    show_story_box("", "I took the box from her hand with maximum caution... The girl ran back to her group with a loud squeak...", is_narrator=True)
    
    show_story_box("Nishida", "Hanefuji… Why would you accept it?", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Hah? I mean, why not? She went out of her way to make it for me. Plus, I wanted to try it.", affiliation="Kasakura High School Student")
    show_story_box("Shigemura", "Give it up, Nishida. No matter how much you explain to him about ‘giving false hope’, he wouldn’t get it.", affiliation="Kasakura High School Student")
    
    show_story_box("", "After a while, we reached the cafeteria. As expected, it was packed... And, luckily, there it was.", is_narrator=True)
    show_story_box("Akasuke", "Guys, come on! There is still enough left for the three of us!", affiliation="Kasakura High School Student")
    
    show_story_box("", "After an excruciatingly long wait, we finally got our special curry... We managed to find an empty table.", is_narrator=True)
    
    show_story_box("Shigemura", "So…how’s the taste?", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "It’s art.", affiliation="Kasakura High School Student")
    show_story_box("", "I started, preparing for the most detailed description known to mankind.", is_narrator=True)
    
    show_story_box("Akasuke", "First, the sweetness from the caramelized onions and grated apples, it was subtle but just enough to coat my tongue in a kind of soft warmth.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Then came the depth; cumin, garam masala, and something I couldn’t quite figure out what it was... The beef was thick and tender, it basically melted in my mouth.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "You could tell it had been stewed for hours. It was so soft I barely had to chew. The spice built slowly... Just enough heat to—", affiliation="Kasakura High School Student")
    
    show_story_box("Shigemura", "Okay, okay. We get it, it’s delicious.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Whaaaaat~? I wasn’t even finished!", affiliation="Kasakura High School Student")
    show_story_box("Shigemura", "We don’t need to hear you gushing about it for more than 4 sentences.", affiliation="Kasakura High School Student")
    
    show_story_box("", "Hmph, such rude people! Anyway…about the Donburi. Guess I could just take it home and have it for dinner. Ding!", is_narrator=True)
    show_story_box("Akasuke", "Mm?", affiliation="Kasakura High School Student")
    show_story_box("", "I pulled out my phone... It was a message. From Kageyama. <Come see me at the council room. Bring Inami.>", is_narrator=True)
    
    show_story_box("Akasuke", "Great….", affiliation="Kasakura High School Student")
    show_story_box("Nishida", "Hm? What’s up?", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Gotta run some errand for prez again…", affiliation="Kasakura High School Student")
    show_story_box("Shigemura", "You got it rough buddy. And you handled that underwear thief just yesterday.", affiliation="Kasakura High School Student")
    
    show_story_box("", "I quickly finished my curry... It was a shame but it was what it was.", is_narrator=True)
    show_story_box("Akasuke", "I’m going to find Yuri. See you in class.", affiliation="Kasakura High School Student")
    show_story_box("Shigemura & Nishida", "‘Kay.", affiliation="Kasakura High School Students")
    
    show_story_box("", "********* ◆ *********\nYuri’s POV", is_narrator=True)
    
    # Yuri's Lunch Scene
    show_story_box("Naganohara", "How long has she been that way?", affiliation="Kasakura High School Student")
    show_story_box("Yamashita", "Since this morning~. Don’t mind her, it’s probably about that Benikawa girl again!", affiliation="Kasakura High School Student")
    
    show_story_box("", "She was half right. I was more so agonizin’ over the fact that I said somethin’ totally embarrassin’ to him and gettin’ called out during class.", is_narrator=True)
    show_story_box("", "I chomped into my onigiri that I bought on the way to school with Akasuke-kun grumpily.", is_narrator=True)
    
    show_story_box("Naganohara", "Sooooo, what’s actually going on? Was I right on the money☆?", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "Not exactly… It’s just…I said somethin’ that I shouldn’t have to him.", affiliation="Kasakura High School Student")
    show_story_box("Yamashita", "Oh? That’s new. What was it?", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "What does it matter to y’all!?", affiliation="Kasakura High School Student")
    show_story_box("Naganohara", "Because we’re your friends, Yuririn! And we deserve to know every bit of your love life♡!", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "I hate ya two…", affiliation="Kasakura High School Student")
    
    show_story_box("", "Still…these two always give me valuable advice whenever I ask for it. Maybe it wouldn’t hurt to tell ‘em about this.", is_narrator=True)
    
    show_story_box("Yuri", "So…we were kinda walkin’ to school together as usual, yeah?", affiliation="Kasakura High School Student")
    show_story_box("Naganohara", "Yeah, after a totally platonic sleepover like always.", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "Would ya seriously cut that out!?", affiliation="Kasakura High School Student")
    
    show_story_box("Yuri", "Anyway…I asked ‘im about who he would be sparrin’ with. And lo and behold, it’s the homegirl Benikawa again.", affiliation="Kasakura High School Student")
    show_story_box("Naganohara & Yamashita", "Uwah, you’re making a scary face…", affiliation="Kasakura High School Students")
    show_story_box("Yuri", "Then I kind of went quiet? So he asked if I disliked the girl…I told him I don’t like the way she looks at him…", affiliation="Kasakura High School Student")
    show_story_box("Naganohara", "Yuririn! That’s practically a confession, isn’t it!?", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "That’s the problem! I dunno if he even realized it…!", affiliation="Kasakura High School Student")
    show_story_box("Yamashita", "Knowing the guy, he probably doesn’t…", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "And I’m an idiot for bein’ the only one still thinkin’ about it…", affiliation="Kasakura High School Student")
    
    show_story_box("", "Yamashita patted me on the back while Naganohara tried comfortin’ me...", is_narrator=True)
    
    show_story_box("Yamashita", "How about you try being more honest like you did today?", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "Huh?", affiliation="Kasakura High School Student")
    show_story_box("Naganohara", "I agree with Hanacchi’s sentiment! Stop beating around the bush and go straight to the goal!", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "If only ya two can apply these divine advice ya gave me to yerselves.", affiliation="Kasakura High School Student")
    show_story_box("Naganohara & Yamashita", "Oh shut it.", affiliation="Kasakura High School Students")
    
    show_story_box("", "But still…", is_narrator=True)
    show_story_box("Yuri", "Thanks, y’all. I’ll try doin’ just that.", affiliation="Kasakura High School Student")
    show_story_box("Naganohara", "That’s the spirit☆! Can’t wait to see how Akasuke reacts when he sees you being all honest.", affiliation="Kasakura High School Student")
    
    show_story_box("Akasuke", "What’s this about me?", affiliation="Kasakura High School Student")
    show_story_box("Naganohara, Yamashita & Yuri", "EEKKK!?", affiliation="Kasakura High School Students")
    show_story_box("", "Akasuke suddenly materialized behind us with a curious expression. Did he overhear our conversation!? It’s so over!", is_narrator=True)
    
    show_story_box("Yuri", "W-when did ya get here…?", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Just in time to hear something about going straight to the goal.", affiliation="Kasakura High School Student")
    show_story_box("", "Thank god he didn’t hear all of it…", is_narrator=True)
    
    show_story_box("Akasuke", "Anyway, prez called us.", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "Hah? Again? Can’t he give us a break?", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Can’t really defy his order now, can we?", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "Ugh…", affiliation="Kasakura High School Student")
    
    show_story_box("", "It has been like this since last year. We got involved in an incident... Prez took a likin’ to us cuz of that so he kept askin’ us for help.", is_narrator=True)
    
    show_story_box("Yuri", "Sorry ya two, seems like it’s goin’ to be busy again.", affiliation="Kasakura High School Student")
    show_story_box("Naganohara", "Nah, it’s cool. You guys already are having it rough. We can’t possibly complain.", affiliation="Kasakura High School Student")
    show_story_box("Yamashita", "Yeah! Let’s hang out again when you have time, ‘kay~?", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "Yeah. See ya.", affiliation="Kasakura High School Student")

def play_stage_1_4_start():
    # Akasuke POV
    show_story_box("", "Akasuke’s POV", is_narrator=True)
    show_story_box("", "We were in the school library, the victim list spread across the table like a battlefield map. Names, schools, last seen locations—all athletes, all gone without a trace.", is_narrator=True)
    
    show_story_box("Akasuke", "…This is definitely a kidnapping case.", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "Yeah. For sure.", affiliation="Kasakura High School Student")
    
    show_story_box("", "The urgency hit harder now. Survival odds for these victims were low. We were out of leads. The police had nothing. Even calling in the third-years felt too slow.", is_narrator=True)
    show_story_box("", "Then—", is_narrator=True)
    
    show_story_box("Benikawa", "What are you doing, Hanefuji-kun?", affiliation="Kasakura High School Student")
    show_story_box("", "We both snapped around.", is_narrator=True)
    show_story_box("", "Benikawa Ayame stood in the doorway, still in her karate dougi, black belt tied tight. Caramel-colored hair in a high ponytail, purple eyes curious and bright.", is_narrator=True)
    
    show_story_box("Akasuke", "Benikawa? Why are you here?", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "To drag your slacking ass to practice, that’s what! You know how bored I am right now? The feeling of having no one to spar with!", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "We do have 10 other members available.", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "But they are not of your caliber!", affiliation="Kasakura High School Student")
    
    show_story_box("", "She stepped forward and lightly punched my arm repeatedly—annoying, not painful.", is_narrator=True)
    
    show_story_box("Yuri", "Benikawa-san? If ya don’t mind, we have some business to do so can this wait ‘til another time?", affiliation="Kasakura High School Student")
    show_story_box("", "Her tone was clipped. Polite, but edged.", is_narrator=True)
    
    show_story_box("", "Benikawa peeked over my shoulder at the list.", is_narrator=True)
    show_story_box("Benikawa", "Missing people?", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Yeah. It’s serious. I’ll appreciate it if you can leave us be. I promise I’ll get this done as soon as—", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "I can help you with that!", affiliation="Kasakura High School Student")
    show_story_box("Akasuke & Yuri", "How?", affiliation="Kasakura High School Students")
    
    # Yuri POV
    show_story_box("", "Yuri’s POV", is_narrator=True)
    show_story_box("Yuri", "Akasuke-kun. Ya sure ‘bout this…?", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "It doesn’t hurt to try, right?", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "I know that but…it still doesn’t sit right with me…", affiliation="Kasakura High School Student")
    
    show_story_box("", "Benikawa’s smile was too bright. Too eager. I didn’t trust it.", is_narrator=True)
    show_story_box("", "Akasuke handed her one of the victim’s glasses left at a scene—how Kageyama got it, I didn’t ask.", is_narrator=True)
    
    show_story_box("Benikawa", "Alright! Watch this.", affiliation="Kasakura High School Student")
    show_story_box("", "She brought the glasses close to her face.", is_narrator=True)
    show_story_box("Benikawa", "Sniff sniff.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke & Yuri", "Hah?", affiliation="Kasakura High School Students")
    show_story_box("Benikawa", "My sense of smell is extraordinarily good, you see.", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "Are ya a dog…?", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "Haha! You’re funny, Inami-chan.", affiliation="Kasakura High School Student")
    show_story_box("", "She handed the glasses back.", is_narrator=True)
    show_story_box("Benikawa", "Now that I’ve got the scent, all you have to do is follow me!", affiliation="Kasakura High School Student")
    
    # Akasuke POV
    show_story_box("", "Akasuke’s POV", is_narrator=True)
    show_story_box("", "We followed. Forty-five minutes later, we stood behind an abandoned building...", is_narrator=True)
    
    show_story_box("Yuri", "Talk about bein’ obvious.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Still. Benikawa, you really are amazing. I couldn’t thank you enough.", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "Oh you don’t have to say that! Now I’m all flustered~.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "No really. Is there any way I could return the favor?", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "Wellllll, actually I do have one thing to ask of you.", affiliation="Kasakura High School Student")
    show_story_box("", "My gut tightened.", is_narrator=True)
    
    show_story_box("Benikawa", "Meet me at Kikyo Station this Saturday at 7AM! We’ll have our private karate match! Just you and me!", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "Hahhhh!?", affiliation="Kasakura High School Student")
    show_story_box("", "Yuri’s shout echoed. Her face twisted—frustration, anger, something sharper.", is_narrator=True)
    
    show_story_box("Akasuke", "Yuri?", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "Ah-oh, nothin’! Um…how ‘bout we just go inside and get this over with, yeah? Then y’all can talk later.", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "I agree with Inami-chan! Let’s go in~.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "You are going in with us?", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "Oh come on. I can fight too, y’know? I’m not a black belt for nothing.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "…Well, be careful there.", affiliation="Kasakura High School Student")
    
    show_story_box("", "I kicked the door open. A dark staircase descended underground. We went down.", is_narrator=True)
    show_story_box("", "The air grew thick, stale, metallic... Six goons waited—cheap pipes and bats. They grinned.", is_narrator=True)
    
    show_story_box("Goons", "Hehe, three high schoolers coming here out of their own volition. Save us the trouble of going out hunting for one.", affiliation="Kidnappers")
    show_story_box("Goons", "They look athletic, too. We hit a jackpot today.", affiliation="Kidnappers")
    show_story_box("Akasuke", "Let’s just beat the shit out of them.", affiliation="Kasakura High School Student")

def play_stage_1_4_end():
    show_story_box("", "It took less than two minutes. All six were down.", is_narrator=True)
    show_story_box("", "Yuri pulled ropes from her jacket pocket—standard gear by now—and started tying them up.", is_narrator=True)
    
    show_story_box("Yuri", "Y’all can go further down to look for the missin’ people. I’ll handle this.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Right. I’ll leave this to you then.", affiliation="Kasakura High School Student")
    
    show_story_box("", "Benikawa and I ran deeper.", is_narrator=True)
    show_story_box("Benikawa", "So, Hanefuji-kun. About this Saturday.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Yeah, I’ll go. There is no reason for me to refuse, is there?", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "For real? Hell yeah!", affiliation="Kasakura High School Student")
    
    show_story_box("", "We reached the final door. Benikawa kicked it down without hesitation.", is_narrator=True)
    show_story_box("", "Inside: bound students—fewer than the list, some already gone. Eyes wide, too weak to speak.", is_narrator=True)
    show_story_box("Akasuke", "We’re here to get you out.", affiliation="Kasakura High School Student")
    
    show_story_box("", "I pulled out my phone and called the police and Kageyama.", is_narrator=True)
    show_story_box("", "The kidnappers had targeted athletes for organ harvesting. We’d stopped it early. Casualties were low. But not zero.", is_narrator=True)

def play_stage_1_5_start():
    # Akasuke POV
    show_story_box("", "Akasuke’s POV", is_narrator=True)
    show_story_box("", "The sun had already dipped below the school buildings when Kageyama’s message came through again. Same curt tone as always.", is_narrator=True)
    
    show_story_box("Kageyama", "Please report to the council room, and bring Inami.", affiliation="Kasakura High School Student Council")
    
    show_story_box("", "Yuri groaned the moment I showed her the screen.", is_narrator=True)
    show_story_box("Yuri", "Again? He’s gonna run us ragged before the trip even starts.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Let’s just get it over with.", affiliation="Kasakura High School Student")
    
    show_story_box("", "We slipped through the emptying hallways. The council room door was already ajar. Kageyama stood at the head of the table, arms crossed, looking more tired than usual.", is_narrator=True)
    
    show_story_box("Kageyama", "...Two loose ends from the kidnapping case. Three of the goons slipped away before police arrived.", affiliation="Kasakura High School Student Council")
    show_story_box("Kageyama", "They’re still in the area—low-level muscle, but they know too much.", affiliation="Kasakura High School Student Council")
    show_story_box("Kageyama", "And…there are reports of freshmen skipping class again, loitering behind the science building, intimidating underclassmen. They might be connected, might not.", affiliation="Kasakura High School Student Council")
    
    show_story_box("", "We turned to leave, having received the assignment.", is_narrator=True)
    show_story_box("", "Benikawa was leaning against the doorframe, arms folded, smiling like she’d been waiting for us.", is_narrator=True)
    
    show_story_box("Benikawa", "Going hunting without me?", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Benikawa? You’re not needed for this.", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "Let me help! I’ll behave! Promise!", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "…I guess it’s fine. But stay in line.", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "I Always do~.", affiliation="Kasakura High School Student")
    
    show_story_box("Benikawa", "Besides, I still have that Saturday date at Kikyo Station. Seven sharp. I wouldn't want anything to happen to my sparring partner before then, would I?", affiliation="Kasakura High School Student")
    
    show_story_box("", "We headed toward the back of campus.", is_narrator=True)

def play_stage_1_6_start():
    # Part 1: Yuri's POV - Post-Incident
    show_story_box("", "Yuri’s POV", is_narrator=True)
    
    show_story_box("", "After dealing with the police and their endless questions, we were finally let go.", is_narrator=True)
    show_story_box("", "It turned out the kidnappers were targeting healthy, athletic students for organ harvesting. Thankfully, the operation hadn’t been running long, so casualties were low.", is_narrator=True)

    show_story_box("Yuri", "Hah~, that was tirin’.", affiliation="Kasakura High School Student")

    show_story_box("", "Akasuke had been quiet since we left the scene. Benikawa had slipped away earlier, nonchalant as ever. It unsettled me.", is_narrator=True)

    show_story_box("Yuri", "Still shaken up from that?", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "…Just thinking that if we’d taken the case earlier, maybe we could have saved more of them.", affiliation="Kasakura High School Student")

    show_story_box("", "His voice was low. Sad. He always carried that weight—wanting to protect everyone, even strangers. It was one of the things I admired most about him. And one of the things that hurt him most.", is_narrator=True)
    show_story_box("", "He blamed himself for things beyond his control.", is_narrator=True)
    show_story_box("", "I stepped closer, stood on tiptoes, and flicked his forehead hard.", is_narrator=True)

    show_story_box("Akasuke", "Ow! What was that for!?", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "Snappin’ ya out of it, that’s what.", affiliation="Kasakura High School Student")

    show_story_box("", "I teased, trying to lighten the mood.", is_narrator=True)

    show_story_box("Yuri", "So what if ya didn’t save all of them? What matters is that ya did save some.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "You’re really bad at comforting people, you know that?", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "I’m tryin’ in my own way, okay!?", affiliation="Kasakura High School Student")

    show_story_box("", "He gave a crooked smile, rubbing his forehead.", is_narrator=True)

    show_story_box("Akasuke", "Well, your way hurts.", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "Better than lettin’ ya spiral.", affiliation="Kasakura High School Student")

    show_story_box("", "I stuck my tongue out.", is_narrator=True)

    show_story_box("Yuri", "Ya want me to let ya sulk all night and stew in guilt? ‘Cause I can leave, y’know.", affiliation="Kasakura High School Student")

    show_story_box("", "I turned dramatically, taking two steps away.", is_narrator=True)
    show_story_box("", "His fingers caught the edge of my jacket—light, hesitant.", is_narrator=True)

    show_story_box("Akasuke", "…Don’t.", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "Hm?", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Don’t leave.", affiliation="Kasakura High School Student")

    show_story_box("", "His voice was quiet, almost lost in the evening wind. He wasn’t looking at me—eyes off to the side, like saying it was hard.", is_narrator=True)
    show_story_box("", "My chest tightened.", is_narrator=True)
    show_story_box("", "I stepped back beside him, bumped his arm gently.", is_narrator=True)

    show_story_box("Yuri", "I ain’t goin’ anywhere.", affiliation="Kasakura High School Student")

    show_story_box("", "I said it softly.", is_narrator=True)

    show_story_box("Yuri", "So stop makin’ that face, yeah? Ya look like someone stole yer free ramen coupon.", affiliation="Kasakura High School Student")

    show_story_box("", "He chuckled—small, real.", is_narrator=True)

    show_story_box("Akasuke", "That bad, huh?", affiliation="Kasakura High School Student")

    show_story_box("", "We walked in silence after that. The sky darkened, stars peeking through.", is_narrator=True)

    show_story_box("Yuri", "Akasuke-kun… ya remember that time in middle school? Ya know what I’m referrin’ to, right?", affiliation="Kasakura High School Student")

    show_story_box("", "His steps faltered. Just for a second.", is_narrator=True)

    show_story_box("Akasuke", "Yeah.", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "Even though ya were just a kid. Even though ya had no backup. Even though ya… lost somethin’ important to ya. Ya still told me ya would do it all over again.", affiliation="Kasakura High School Student")

    show_story_box("", "He didn’t answer. He didn’t need to.", is_narrator=True)

    show_story_box("Yuri", "I blamed myself for that for a long time. Thought I was a burden. That if I’d been more careful, none of it would’ve happened.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Yuri—", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "But ya never blamed me. Not even once. So don’t ya think it’s a little unfair? That ya can forgive me, but ya can’t forgive yerself?", affiliation="Kasakura High School Student")

    show_story_box("", "He looked like he wanted to argue.", is_narrator=True)
    show_story_box("", "Then he sighed.", is_narrator=True)

    show_story_box("Akasuke", "…You’re right.", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "‘Course I am.", affiliation="Kasakura High School Student")

    show_story_box("", "Another small laugh. He finally looked at me, the streetlight catching his eye.", is_narrator=True)

    show_story_box("Akasuke", "Thanks, Yuri.", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "Anytime.", affiliation="Kasakura High School Student")

    show_story_box("", "We walked the rest of the way like that—side by side, quiet. When we reached the train station where I’d head home, I stopped.", is_narrator=True)

    show_story_box("Yuri", "Well. See ya next Monday, Akasuke-kun.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Yeah. Later.", affiliation="Kasakura High School Student")

    show_story_box("", "He waved. I turned away.", is_narrator=True)
    show_story_box("", "But my heart stayed heavy.", is_narrator=True)

    # Part 2: Akasuke's POV - Saturday Morning
    show_story_box("", "********* ◆ *********\nAkasuke’s POV", is_narrator=True)
    
    show_story_box("", "Saturday came too fast.", is_narrator=True)
    show_story_box("", "I arrived at Kikyo Station ten minutes early.", is_narrator=True)
    show_story_box("", "Black turtleneck, red bomber jacket (力 kanji on the back), dark gray cargo pants, black high-top sneakers with red accents—scuffed from use. Practical, comfortable, and ready.", is_narrator=True)
    
    show_story_box("", "Benikawa showed up right on time.", is_narrator=True)

    show_story_box("Benikawa", "Hanefuji-kun! Sorry, were you waiting long?", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Not at all. I just arrived myself.", affiliation="Kasakura High School Student")

    show_story_box("", "A small lie.", is_narrator=True)
    show_story_box("", "She wore a cropped burnt-orange bomber jacket with quirky patches—smiley faces, band-aids, a big \"ドカン!\" bubble—over a dark purple sports crop top. Loose olive-green cargo joggers, mismatched laces on black sneakers. Casual. Energetic.", is_narrator=True)

    show_story_box("Benikawa", "Practical choice of clothes you have there.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "You too. Well, we are here for sparring after all.", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "But first!", affiliation="Kasakura High School Student")

    show_story_box("", "She interrupted, grinning wide.", is_narrator=True)

    show_story_box("Benikawa", "Let’s hang out first! It’s the weekend after all.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Are you serious right now?", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "Dead serious.", affiliation="Kasakura High School Student")

    show_story_box("", "I sighed.", is_narrator=True)

    show_story_box("Akasuke", "I was wondering why you’d ask to meet so early in the morning.", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "Bingo! One point for Hanefuji-kun.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "It’s not that hard to figure out…", affiliation="Kasakura High School Student")

    show_story_box("", "First time hanging out with her outside school on a weekend. I didn’t mind the change of pace.", is_narrator=True)
    show_story_box("", "She pointed toward the shopping district.", is_narrator=True)

    show_story_box("Benikawa", "First stop: Fried Mochi Stick Stand!", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Ah. So you’re the type to eat sweets to fuel up before training.", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "Yep! It helps boost my punch!", affiliation="Kasakura High School Student")

    show_story_box("", "We walked through the early-morning crowd. Most people still half-asleep. Benikawa moved like she owned the streets—waving at vendors, pointing at random things.", is_narrator=True)

    show_story_box("Benikawa", "Hey look at that crane game machine over there, it has a big cockroach doll as a reward! Should we get one for Inami-chan?", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "She would throw it right back at you.", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "Good point!", affiliation="Kasakura High School Student")

    show_story_box("", "I shook my head. Hanging out with her was like being caught in a storm—unpredictable, chaotic, but not unpleasant.", is_narrator=True)
    show_story_box("", "We reached the small stall behind the bookstore. The shopkeeper—burly, sleepy—grunted a greeting.", is_narrator=True)

    show_story_box("Benikawa", "Two mochi sticks. Extra sauce.", affiliation="Kasakura High School Student")
    show_story_box("Shopkeeper", "Like usual, I see.")
    show_story_box("Akasuke", "So you’ve been here multiple times before.", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "Yep! I always come here first thing in the morning before school.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "So that’s why you’re always late.", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "Worth it, though.", affiliation="Kasakura High School Student")

    show_story_box("", "The mochi arrived steaming, glossy.", is_narrator=True)
    show_story_box("", "I took a bite.", is_narrator=True)
    show_story_box("", "Heaven.", is_narrator=True)

    show_story_box("Akasuke", "Whoa—hold on.", affiliation="Kasakura High School Student")

    show_story_box("", "I chewed slower, savoring.", is_narrator=True)

    show_story_box("Akasuke", "Crispy on the outside, gooey on the inside… That’s illegal. That crunch? Like the first clash of a match, then—bam—it melts into sweet, chewy surrender. The glaze has that sweet-salty balance… confused, but in the best way.", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "Illegal, huh?", affiliation="Kasakura High School Student")

    show_story_box("", "She laughed.", is_narrator=True)

    show_story_box("Benikawa", "You think about food way too deeply.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Says the girl who dragged me here before training.", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "I regret nothing.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "…Neither do I.", affiliation="Kasakura High School Student")

    show_story_box("", "We wandered more—arcade (both terrible, won nothing), street food, more nerding out from me.", is_narrator=True)
    show_story_box("", "By noon we stood at the quiet riverside. Almost no one around. Just us.", is_narrator=True)
    show_story_box("", "Benikawa bounced barefoot, hair tied up.", is_narrator=True)

    show_story_box("Benikawa", "Alright. Do your worst.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Okay. I will.", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "Good. If you don’t, I’ll be disappointed.", affiliation="Kasakura High School Student")

    show_story_box("", "We stepped into the invisible ring.", is_narrator=True)
    show_story_box("", "Silence.", is_narrator=True)
    show_story_box("", "She dashed first.", is_narrator=True)

def play_stage_1_6_end():
    show_story_box("", "I blocked the jab, deflected the sweep. Her movements smooth—almost lazy—but every strike had intent.", is_narrator=True)
    show_story_box("", "I twisted into a low hook kick. She ducked, went for my legs. Nearly caught them.", is_narrator=True)
    show_story_box("", "I backflipped once, steadied.", is_narrator=True)

    show_story_box("Akasuke", "You’re more aggressive than usual.", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "I ate the mochi.", affiliation="Kasakura High School Student")

    show_story_box("", "She grinned, lunged again.", is_narrator=True)
    show_story_box("", "Flurry of hits—open palm strikes, low punches, feints. She laughed even when I grazed her ribs.", is_narrator=True)
    show_story_box("", "Her grin was maddening.", is_narrator=True)
    show_story_box("", "She faked a side kick, spun, heel flying toward my head. I blocked—impact rattled my bones—but I charged into her blind spot.", is_narrator=True)
    show_story_box("", "Elbow strike—narrowly dodged.", is_narrator=True)
    show_story_box("", "She countered with a knee to my gut. I caught it. Twisted.", is_narrator=True)
    show_story_box("", "She hit the ground.", is_narrator=True)
    show_story_box("", "But she swept my legs as I backed off. I landed hard, rolled, stood.", is_narrator=True)

    show_story_box("Benikawa", "Still standing.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "You too.", affiliation="Kasakura High School Student")

    show_story_box("", "She rushed faster.", is_narrator=True)
    show_story_box("", "I read her—shoulders dipped slightly before the strike. The tell.", is_narrator=True)
    show_story_box("", "I caught her wrist, ducked low, flipped her clean over my shoulder.", is_narrator=True)
    show_story_box("", "She hit with a thud, air leaving her lungs.", is_narrator=True)
    show_story_box("", "I hovered, ready.", is_narrator=True)
    show_story_box("", "She lay there, staring at the sky, then sighed.", is_narrator=True)

    show_story_box("Benikawa", "Dang. That was sick.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "You done?", affiliation="Kasakura High School Student")

    show_story_box("", "She held up a peace sign.", is_narrator=True)

    show_story_box("Benikawa", "I yield. You got me fair and square~", affiliation="Kasakura High School Student")

def play_stage_1_7_start():
    # --- AKASUKE POV ---
    show_story_box("", "********* ◆ *********\nAkasuke’s POV", is_narrator=True)
    show_story_box("", "I offered my hand. She took it. I pulled her up.", is_narrator=True)
    
    show_story_box("Benikawa", "You’ve gotten better. Didn’t think you’d predict that spinning heel.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "I’ve seen it too many times.", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "Still, you win this time, Hanefuji-sensei.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Don’t call me that.", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "Hanefuji-sama~?", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Stop.", affiliation="Kasakura High School Student")
    
    show_story_box("", "She laughed—long and bright—then looked straight at me.", is_narrator=True)
    
    show_story_box("Benikawa", "Actually, can you do me another favor?", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Hm? What now?", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "Can you stay still and take a hit real quick? I wanna test how effective the move I came up with is.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "…So you expect me to just stand here and take an unknown attack from you?", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "Ugh, fine. You can block or dodge it. If you can do either, I’ll refine it.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Right. Hit me with it already.", affiliation="Kasakura High School Student")
    
    show_story_box("", "Her smile vanished. She closed her eyes. Breathed in, then out.", is_narrator=True)
    show_story_box("", "I blinked.\nShe was gone.", is_narrator=True)
    
    show_story_box("Akasuke", "Wha—", affiliation="Kasakura High School Student")
    
    show_story_box("", "A chop—strong, precise—landed at the back of my neck.\nPainless.\nBut my legs failed.", is_narrator=True)
    show_story_box("", "I collapsed, body refusing commands. Benikawa walked in front of me, her smile unsettling—it was too calm.", is_narrator=True)
    
    show_story_box("Benikawa", "Now then, Hanefuji-kun. Let’s get to the real fun part, shall we?", affiliation="Kasakura High School Student")
    
    show_story_box("", "My fingers twitched again. Or—no. That wasn’t right.\nI tried to twitch my fingers, but my right leg jolted instead.", is_narrator=True)
    
    show_story_box("Akasuke", "What… the hell…", affiliation="Kasakura High School Student")
    
    show_story_box("", "I clenched my jaw—at least that still worked—and tried again.\nLeft arm. Go.\nMy right shoulder shifted slightly.\nMy entire motor coordination was scrambled.", is_narrator=True)
    
    show_story_box("Benikawa", "That strike I gave you earlier?", affiliation="Kasakura High School Student")
    show_story_box("", "She said it sweetly.", is_narrator=True)
    show_story_box("Benikawa", "It was a brain interference strike. One of the tricks I just came up with recently.", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "Basically, your body isn’t paralyzed—your wiring’s just crossed. When you think ‘arm,’ your brain still sends the signal… just to the wrong part of the body. Fun, right?", affiliation="Kasakura High School Student")
    
    show_story_box("Akasuke", "Fun my ass…", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "…Why are you doing this?", affiliation="Kasakura High School Student")
    
    show_story_box("", "Benikawa tilted her head with a sigh, almost wistful.", is_narrator=True)
    
    show_story_box("Benikawa", "Because I was hired.", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "To eliminate the Seven Wonders of Kasakura High.", affiliation="Kasakura High School Student")
    
    show_story_box("", "The Seven Wonders. A dumb nickname for the strongest, weirdest, or most iconic students in school.\nYuri. Kageyama. Me. And four others.", is_narrator=True)
    
    show_story_box("Akasuke", "Who hired you?", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "Wouldn’t you like to know?", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "You probably also want to know who I am to be hired, right? Don’t tell anyone else, okay? Not like you could tell anyone after this anyway!", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "Monomi, Nokizaru, Rappa, Kusa, Iga-mono… those are names we’ve been called throughout history.", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "But we are known as Ninjas in this era.", affiliation="Kasakura High School Student")
    
    show_story_box("", "She took a step closer, staring at me with that infuriatingly bright smile.", is_narrator=True)
    
    show_story_box("Benikawa", "I didn’t expect to like one of my targets, though. You’re strong. Calm. Kind. Handsome, even.", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "But job’s a job. Nothing personal, yeah?", affiliation="Kasakura High School Student")
    
    show_story_box("", "Damn it. Benikawa slowly turned her head to the side.", is_narrator=True)
    
    show_story_box("Benikawa", "Oh, and by the way—", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "—you can come out now, Inami-chan.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "What?", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "I noticed you’ve been tailing us since the fried mochi stand. You’re good at keeping distance, but nothing escapes my nose.", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "Lucky me! Two Wonders for the price of one! Let’s have some fun, shall we?", affiliation="Kasakura High School Student")
    
    # --- YURI POV ---
    show_story_box("", "********* ◆ *********\nYuri’s POV", is_narrator=True)
    show_story_box("Yuri", "…Huh?", affiliation="Kasakura High School Student")
    show_story_box("", "I froze behind the hedge. Benikawa stood in the clearing, smiling like she just won a lottery. And Akasuke-kun… He was just lying there.", is_narrator=True)
    
    show_story_box("Yuri", "What’s goin’ on? Benikawa, what the hell ya—", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "Ohhh, good! You didn’t run. That makes this way more convenient.", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "What did ya do to him?", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "Just scrambled his wire a bit. A little strike here… and poof! All mixed up. He’s not really hurt—he’s just confused. You can still have him back after I kill you both.", affiliation="Kasakura High School Student")
    
    show_story_box("Yuri", "…Kill?", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "Yep! I did say it. I’m a ninja. Real deal. Benikawa clan, all that stuff. And you Wonders are my targets.", affiliation="Kasakura High School Student")
    
    show_story_box("", "My brain tried to catch up… Deep down, I wasn’t even surprised. There’d always been something off about Benikawa.", is_narrator=True)
    
    show_story_box("Benikawa", "Still, if it makes you feel better—all the people I’ve gotta kill, you two are probably the ones I’ll regret the most.", affiliation="Kasakura High School Student")
    
    show_story_box("", "I clenched my fists. Heat rose in my chest. She hurt Akasuke-kun. She was threatening to kill me. And she acted like it was a game.", is_narrator=True)
    
    show_story_box("Yuri", "Regret this, huh? Yeah. I bet ya will.", affiliation="Kasakura High School Student")
    
    show_story_box("", "My body moved before my brain caught up. Sharp stomp forward. Ducked under her lazy swing. Hooked my arm under her elbow.", is_narrator=True)
    show_story_box("Yuri", "Seoi-nage!", affiliation="Kasakura High School Student")
    show_story_box("", "I slammed her into the ground with force that cracked air. But she didn’t scream. Her body twitched, folded—and disintegrated into paper talismans.", is_narrator=True)
    
    show_story_box("Yuri", "…What? Ya gotta be kiddin’ me.", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "Not bad~", affiliation="Kasakura High School Student")
    
    show_story_box("", "The voice came from both sides. I spun instinctively—just in time. Two fingers tapped me. One on each side of my neck.\nThe world flipped. Literally.", is_narrator=True)
    
    show_story_box("Yuri", "Aagh—wh-what the hell!?", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "Your brain’s confused, huh? Fun biology fact: technically, the human retina receives visual input upside-down. Your brain flips it right back up automatically.", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "So I just… temporarily shut off that lil’ flipping function. You’re welcome.", affiliation="Kasakura High School Student")
    
    show_story_box("", "My stomach flipped—probably because the sky looked like it was beneath me now.", is_narrator=True)
    
    show_story_box("Yuri", "Ya think this’s gonna stop me?", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "No. I know it won’t. That’s why this is fun. Let’s see if Kasakura’s Wonder Girl can still fight when the whole world’s upside down.", affiliation="Kasakura High School Student")
    
    show_story_box("", "I lunged. Or tried to. My foot shot forward but the ground was suddenly above me. I tumbled sideways.", is_narrator=True)
    show_story_box("Yuri", "Agh—dammit!", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "Aww, c’mon~ You’re not giving up already, are you?", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "I ain’t… done yet.", affiliation="Kasakura High School Student")
    
    show_story_box("", "The world still flipped—every movement guesswork. Right was left. Up was down. When I raised a fist, it nearly smacked my own forehead.", is_narrator=True)
    show_story_box("Benikawa", "Balance is off. Striking angle’s warped. Peripheral depth is compromised…", affiliation="Kasakura High School Student")
    show_story_box("", "She took a step forward and vanished—just disappeared into a blur.", is_narrator=True)
    
    show_story_box("Yuri", "Y’think… this is enough to stop me?", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "…Wow. You really are one of the Seven Wonders, huh?", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "I was hoping to drag this out. But if you’re gonna get serious even like this… Guess I’ll put you down quickly.", affiliation="Kasakura High School Student")
    
    # --- AKASUKE POV ---
    show_story_box("", "********* ◆ *********\nAkasuke’s POV", is_narrator=True)
    show_story_box("Akasuke", "Yuri-chan—!", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "I could barely speak. Tongue thick. Legs refused commands. Arms twitched out of sync like a broken marionette.", affiliation="Kasakura High School Student", is_thought=True)
    
    show_story_box("", "I was stuck in someone else’s body. Forced to watch as Benikawa played with her like a cat with a half-dead bird.", is_narrator=True)
    
    show_story_box("Akasuke", "No. This isn’t how it ends.", affiliation="Kasakura High School Student", is_thought=True)
    show_story_box("Akasuke", "Think, damn it. Left arm triggers right leg. Right arm jerks left shoulder. Connections scrambled—but not cut.", affiliation="Kasakura High School Student", is_thought=True)
    
    show_story_box("", "I closed my eyes. Mind raced faster than it had in years. Yuri took a hit to the gut, stumbled back, coughing. That was the last straw.", is_narrator=True)
    show_story_box("", "One wild, janky step forward. Another step. Then another. Pushed through scrambled feedback, syncing action and misfire into rhythm.", is_narrator=True)
    
    show_story_box("Benikawa", "Whoa? You’re—?", affiliation="Kasakura High School Student")
    show_story_box("", "Too late. I surged forward. Perfect feint-jump combo, redirected through the glitch.", is_narrator=True)
    
    show_story_box("Akasuke", "HAAA!", affiliation="Kasakura High School Student")
    show_story_box("", "Knee slammed ground beside her as I twisted mid-air. Elbow came down—but in my brain, I raised my leg. It worked.\nCRACK!", is_narrator=True)
    
    show_story_box("", "Benikawa stumbled back with a surprised grunt. I landed in a three-point crouch, panting. But I was back. I stood between Yuri and Benikawa.", is_narrator=True)
    
    show_story_box("Akasuke", "…Round two. Let’s see how well you really fight.", affiliation="Kasakura High School Student")
    
    show_story_box("", "The moment I stepped forward, shadows twitched. More of them. Puppets slipped out from behind trees, fences, bushes. All wore Benikawa’s smile.", is_narrator=True)
    show_story_box("Yuri", "There’s more of her!?", affiliation="Kasakura High School Student")

def play_stage_1_7_end():
    show_story_box("Akasuke", "Don’t let them circle us.", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "They already are!", affiliation="Kasakura High School Student")
    
    show_story_box("", "She flipped one over her shoulder—stumbled sideways, barely caught footing. I moved beside her, knocked another puppet off her blindside with misfired left-hook-turned-right-heel-kick.", is_narrator=True)
    
    show_story_box("Yuri", "Okay, this is gettin’ real annoyin’. She’s not fightin’ fair.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "She’s not even fighting right now. She’s controlling them remotely—they react instantly too.", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "So she’s close?", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Has to be. Watching. Feeding them data directly.", affiliation="Kasakura High School Student")
    
    show_story_box("", "One leapt from right. I side-stepped, smashed elbow into its back—it disintegrated into paper talismans mid-fall. Right eye scanned area as I blocked two more blows.", is_narrator=True)
    show_story_box("", "Then I saw it. Shadowy figure behind bushes deep in forest. Purple eyes. Benikawa’s eye color.", is_narrator=True)
    
    show_story_box("Akasuke", "There! Cover me, I’ll charge her!", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "On it!", affiliation="Kasakura High School Student")
    
    show_story_box("", "She tightened stance, threw two puppets in opposite directions. I broke into sprint—every limb still firing wrong, but rhythm adjusted.", is_narrator=True)
    show_story_box("", "Benikawa noticed. Stepped out from tree and smiled.", is_narrator=True)
    
    show_story_box("Benikawa", "Aw~ You’re sharper than I thought, Hanefuji-kun!", affiliation="Kasakura High School Student")
    
    show_story_box("", "I barely twisted torso in time to block open-palm strike. CRACK! Whole arm went numb.", is_narrator=True)
    
    show_story_box("Akasuke", "What the hell?", affiliation="Kasakura High School Student")
    show_story_box("", "I skidded back. She didn’t chase right away. Stood in smoke, fingers curled, legs low stance. Not like puppets. No wasted motion. This… this was the real deal.", is_narrator=True)
    
    show_story_box("Benikawa", "I did say I was a ninja, remember? No way I’m wasting time making puppets meant for distraction match my full power.", affiliation="Kasakura High School Student")
    
    show_story_box("", "Another tap came fast—aimed for temple. I ducked. Legs buckled instead. Tch—dammit, scrambled signal! Her foot caught my shoulder. WHAM!", is_narrator=True)
    
    show_story_box("Benikawa", "Still adapting, huh? You’re amazing, you know? But that won’t last forever.", affiliation="Kasakura High School Student")
    
    show_story_box("", "I growled, forced myself to feet. She was fast. Reading broken rhythm like sheet music. But I stared her down, blood dripping from lip.", is_narrator=True)
    
    show_story_box("Akasuke", "I won’t lose. Not with Yuri fighting back there.", affiliation="Kasakura High School Student", is_thought=True)
    
    show_story_box("Akasuke", "Benikawa… No more games.", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "Oh~? Is this where the scary side comes out?", affiliation="Kasakura High School Student")
    
    show_story_box("", "I shifted into half-step stance—adjusted for reversed coordination.", is_narrator=True)
    
    show_story_box("Akasuke", "You haven’t seen scary yet.", affiliation="Kasakura High School Student")

def play_stage_1_8_story():
    # --- Part 1: Ayame's POV / Waking Up ---
    show_story_box("", "Ayame’s POV", is_narrator=True)
    
    show_story_box("???", "You sure you didn’t put her in a coma?")
    show_story_box("???", "Nah, she isn’t that weak.")
    
    show_story_box("", "…That was surprising. I never expected him to be able to use it.", is_narrator=True)
    show_story_box("", "I mean, I had my suspicions that he had been using it unconsciously all this time, but to think he could pull it off to that extent.", is_narrator=True)
    show_story_box("", "Now I see why the employer wanted him gone. He probably posed a threat to whatever their plan was.", is_narrator=True)
    
    show_story_box("Ayame Benikawa", "Ah~, I failed my mission for the first time in my life. Father is going to scold me to no end, and my rank is going to drop after I tried so hard to climb up this far…", affiliation="Benikawa Ninja Clan", is_thought=True)
    show_story_box("Ayame Benikawa", "Well! No matter! I will just climb right back up in no time!", affiliation="Benikawa Ninja Clan", is_thought=True)
    
    show_story_box("", "For now… let me think about getting out of this situation.", is_narrator=True)
    show_story_box("", "I woke up about an hour ago but didn’t open my eyes right away. Good thing they still haven’t noticed anything.", is_narrator=True)
    show_story_box("", "And it looked like the effect of my brain tempering technique had also worn off. I really should upgrade it so the effect would be permanent.", is_narrator=True)
    
    show_story_box("???", "So why isn’t she waking up? This is taking too long, you are wasting my time here.")
    
    show_story_box("Akasuke", "How should I know?! No one has ever been knocked out this long by my kick!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Yuri", "Alright, alright. Calm down ya two, let’s just be patient, yeah?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Judging from what I was hearing, there are four people in this room. Me, Hanefuji, Inami, and… Yokubukai Natsume. Another member of the Seven Wonders.", is_narrator=True)
    show_story_box("", "Most people in this school know her for her intelligence, lack of appearance on campus, and more. But her most well-known feat was the creation of the ‘Kasalink’ application.", is_narrator=True)
    show_story_box("", "But if we dig deeper, that wasn’t all there was to her. She was dubbed ‘The Queen of Information’ in the underworld.", is_narrator=True)
    show_story_box("", "The real purpose of that application was to store the students’ personal information for herself. Normally, her real identity is unknown even to underworlders, but a simple thing like that can’t escape a ninja like me.", is_narrator=True)
    show_story_box("", "The fact that Hanefuji was in cahoots with her was news to me, though. Guess I haven’t been that updated.", is_narrator=True)
    
    # --- Part 2: The Interrogation Begins ---
    show_story_box("Yuri", "Ugh. I’m losing patience. Akasuke-kun, do the thing.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Akasuke", "…Fine.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Yuri", "Oi, Akasuke-kun! Wait—", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Hm? What are they talking about? What’s he going to—", is_narrator=True)
    show_story_box("", "WHAM!", is_narrator=True)
    
    show_story_box("Ayame Benikawa", "OUCH!", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Akasuke", "Finally awake, huh?", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "His fist still high in the air.", is_narrator=True)
    
    show_story_box("Ayame Benikawa", "Ah… You little—! You do know I can just untie myself right now, right!?", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Akasuke", "But you won’t. You know damn well that you wouldn’t be able to catch me off guard again and therefore can’t defeat me.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "He smirked.", is_narrator=True)
    show_story_box("Akasuke", "Isn’t that right? Or you wouldn’t have gone through all the trouble getting me to trust you and take your hit.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "This guy… he was way sharper than I thought.", is_narrator=True)
    show_story_box("", "He leaned in close, his smile—usually so gentle—felt strangely unsettling.", is_narrator=True)
    
    show_story_box("Akasuke", "So, be a good little puppy and answer our question truthfully… or I’ll break every bone in your body.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "…Not good. He was absolutely serious. Whatever. Guess I’ll just tell them everything they ask.", is_narrator=True)
    
    # --- Part 3: Natsume and the Plot ---
    show_story_box("Natsume", "Still, what a great catch, Hanefuji. I’ve been investigating these little macaques but didn’t find anything useful. So be sure to get lots of data out of her.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Ayame Benikawa", "Macaques… Well, I suppose that wasn’t an inaccurate description of us.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Natsume", "Firstly, who hired you? What’s their purpose?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Ayame Benikawa", "Dunno, they didn’t give a name, and I didn’t care to ask. They just gave me the mission and the cash. I took it and gave my word. That was that.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Yuri", "Are you serious? Ya just accept a job like that without checkin’ who it was from?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Ayame Benikawa", "Of course. A job’s a job. That’s what us ninjas do. We don’t question anything, just move according to the orders.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Ayame Benikawa", "Look here. I won’t try anything, yeah? I already failed my mission and that’s that. I have no obligation to do anything to you all anymore.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Natsume", "Tch, how convenient. If so, at least leave us with something we can work with—like why are they targeting us?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Ayame Benikawa", "Don’t know—", affiliation="Benikawa Ninja Clan")
    show_story_box("Akasuke", "—at least let me finish, you savage!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "His fist stopped inches from my face.", is_narrator=True)
    
    show_story_box("Ayame Benikawa", "Sigh. If I have to guess, you all are obstacles in their plans.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "The room fell into silence for a little while before it was interrupted by Yokubukai.", is_narrator=True)
    
    show_story_box("Natsume", "Plan?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Ayame Benikawa", "Yeah. I mean, come on. Don’t pretend like you all aren’t a bunch of absolute powerhouses. If they are planning to do anything, of course they are going to have to get rid of you all. And it probably wouldn’t be just me, either.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Yuri", "So…what yer sayin’ is that…there will be more to come.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Natsume", "If that is so, at least tell us how to distinguish ninjas from normal people.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Ayame Benikawa", "Nope. That, I can’t say.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "CRACK!!", is_narrator=True)
    show_story_box("Ayame Benikawa", "GUH—!?", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "One of my fingers was broken by Hanefuji-kun. He really wasn’t kidding when he said he was going to break every bone in my body.", is_narrator=True)
    
    show_story_box("Ayame Benikawa", "…Do that all you want but I won’t say i–AGH!", affiliation="Benikawa Ninja Clan")
    show_story_box("Akasuke", "Oh really? How about I just break three of them at the same time?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "No mercy for the wicked… was his motto, wasn’t it? And I was the wicked in his eye, so him being this rough wasn’t that unnatural… But what could I have done? I literally couldn’t say it!", is_narrator=True)
    
    show_story_box("Ayame Benikawa", "Hah…fine. I will tell you this… us ninjas can’t interfere with each others’ mission, unless the mission requires us to…", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "That silence again. Akasuke loosened his grip on my hand, though the sting from my fingers still throbbed like a heartbeat in my skull.", is_narrator=True)
    
    show_story_box("Ayame Benikawa", "That’s all I’ll say. And you can twist my whole arm off if you want, I’m not breaking that law. We’re not allowed to out each other. You should feel lucky I even said this much…", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Yuri", "Why? What’s so sacred about yer rules? Yer just assassins, right?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Ayame Benikawa", "It’s for my own survival. If we break even one of the sacred rules, no matter how minor it is, we get hunted down by the entirety of the ninja society labeled as ‘Ibara’.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Akasuke", "And how many of you are already in this school?", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Ayame Benikawa", "I’m not saying. But it’s more than you think.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Natsume", "We’ll need to go back through data archives. I’ll try to figure out how to distinguish ninjas from normal people by myself.", affiliation="Kasakura High School Student / Seven Wonders")
    
    # --- Part 4: Ayame's Reaction ---
    show_story_box("Ayame Benikawa", "So…what now? You’re gonna kill me?", affiliation="Benikawa Ninja Clan")
    show_story_box("Akasuke", "No, we are not like you.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Ayame Benikawa", "Aw. I was kinda hoping for something dramatic.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "Being told that by the person I liked should hurt. But somehow that kind of… turned me on? What the hell?", is_narrator=True)
    
    show_story_box("Akasuke", "Keep an eye on her. Don’t let her out of this room.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Natsume", "Don’t underestimate my security system. Why do you think no one has found this place yet?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Yokubukai really was terrifying. Probably the only person in this room scarier than Hanefuji-kun.", is_narrator=True)
    
    show_story_box("Akasuke", "I meant what I said earlier. If I see you hurting anyone again, even once, it won’t matter if you’re under contract or not.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Ayame Benikawa", "Noted~.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "He didn’t reply. Just walked out of the room, Inami followed right after. Ah…I think he awakened something inside me. Felt kinda sticky down there.", is_narrator=True)
    
    show_story_box("", "A-Anyway. That left me alone with Yokubukai. And she was just staring.", is_narrator=True)
    
    show_story_box("Natsume", "…What?", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Natsume", "You’re horny right now, aren’t you?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "She said it. She actually said it.", is_narrator=True)
    
    show_story_box("Ayame Benikawa", "E-Excuse me!? What kind of opening line is that!?", affiliation="Benikawa Ninja Clan")
    show_story_box("Natsume", "I’m right, aren’t I?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I wanted to deny it. Really, I did. But I was pretty sure my face betrayed me. It was heating up fast.", is_narrator=True)
    
    show_story_box("Ayame Benikawa", "I-I mean, what, so you monitor body temperature now!?", affiliation="Benikawa Ninja Clan")
    show_story_box("Natsume", "Nah, I just heard it. Your breathing got more erratic, your pupils dilated more than they should when Hanefuji threatened you. And I definitely heard a squelching sound down ther—", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Ayame Benikawa", "Don’t say it!", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Natsume", "Well, anyway.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "She clapped her hands.", is_narrator=True)
    show_story_box("Natsume", "Kagaku, you’re up.", affiliation="Kasakura High School Student / Seven Wonders")
    
    # --- Part 5: Kurona's POV ---
    show_story_box("", "********* ◆ *********\nKurona’s POV\nHanefuji Residence – A Day in Life", is_narrator=True)
    
    show_story_box("Hanefuji Kurona", "Whatever you make is fine.", affiliation="Hanefuji Family")
    
    show_story_box("", "It was a peaceful Sunday evening in our house. At the moment, I was trying to find inspiration for my next work by listening to various songs. Believe it or not, I’m actually a fairly popular Vocaloid producer by the name of KokuiP on YouTube.", is_narrator=True)
    show_story_box("", "Of course, I kept it a secret from everyone, including my own big brother. If he ever found out his little sister was secretly writing dark, lovesick lyrics and mixing electronic beats at two in the morning, he’d probably lose his mind.", is_narrator=True)
    show_story_box("", "I checked my YouTube dashboard. New comments had piled up under my latest upload... My fingers itched to type out replies, but I forced myself to log off.", is_narrator=True)
    show_story_box("", "From the kitchen, I heard the familiar clatter of pans. The smell of garlic and onion hit almost immediately, spreading through the whole house like magic.", is_narrator=True)
    
    show_story_box("", "My big brother, even though I rarely say it to him, is very reliable. He basically filled in every role in the house. Our parents are rarely ever home because of their work.", is_narrator=True)
    show_story_box("", "Honestly, I felt a little guilty about it. I even tried to ask him if I could help out sometime, but…every time I tried, I ended up ruining everything.", is_narrator=True)
    show_story_box("", "With that kind of personality, I’m not surprised at all that he’s so popular at school... Any girl who has him as a boyfriend would be very lucky.", is_narrator=True)
    show_story_box("Hanefuji Kurona", "So…Yuri-nee, hurry up and make him yours already. You’ve got competition.", affiliation="Hanefuji Family", is_thought=True)
    
    show_story_box("Akasuke", "GYAHHHHHHHHH!?", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Hanefuji Kurona", "Huh, Onii-chan!? What’s wrong?", affiliation="Hanefuji Family")
    
    show_story_box("", "I quickly rushed down the stairs to see what was going on for my invincible big brother to scream like a girl like that. What I saw was almost comical to see.", is_narrator=True)
    show_story_box("", "Right. I completely forgot. There was a frog standing by the kitchen door to the backyard staring at Onii-chan, who was on the completely opposite side of the room.", is_narrator=True)
    
    show_story_box("Akasuke", "K-K-Kurona…g-get it out I beg you…", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Hanefuji Kurona", "Okay, okay, calm down, aniki.", affiliation="Hanefuji Family")
    
    show_story_box("", "I better hurry and get it out before he starts vomiting everywhere. I picked it up and dropped it off at the bush near our house.", is_narrator=True)
    show_story_box("", "When I was back to our house, he returned to his usual self, placing down plates on our table.", is_narrator=True)
    
    show_story_box("Akasuke", "Dinner’s ready.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Hanefuji Kurona", "Wah~, looks delicious! I’m drooling.", affiliation="Hanefuji Family")
    show_story_box("Akasuke", "Well, come and eat up.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "We just ignored what just happened. I don’t know why his reaction to seeing a frog would be this strong, but I guess even my ever-so-reliable big brother has his own weakness. Funny how nature balances things out, huh?", is_narrator=True)
    
    show_story_box("", "Still, as I dug into my dinner, I couldn’t help but to poke fun at him a little.", is_narrator=True)
    
    show_story_box("Hanefuji Kurona", "Anija, you should’ve seen your face back there.", affiliation="Hanefuji Family")
    show_story_box("Akasuke", "Shut up and eat your vegetables. Also, settle with one way of addressing me already.", affiliation="Kasakura High School Student / Seven Wonders")

def play_stage_1_9_story():
    # --- Part 1: The Meeting Begins ---
    show_story_box("", "Akasuke’s POV", is_narrator=True)
    show_story_box("", "Two days after the incident, Kageyama called all the members of the Seven Wonders of Kasakura High to gather for a meeting in the student council room.", is_narrator=True)
    
    show_story_box("", "Akasuke and Yuri arrived and found that there were already two people waiting. The first one was Kageyama and the other was a female third year student with long blonde hair and a pair of orange eyes.", is_narrator=True)
    show_story_box("", "She’s Kaoru Hana, the sole member of the gardening club and a part of the Seven Wonders.", is_narrator=True)
    
    show_story_box("Hana", "Hanefuji-kun! Inami-chan! You're here!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Akasuke", "Long time no see, Kaoru-senpai.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Hana", "I hope things have been peaceful for the two of you!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Yuri", "Haha. If ya don’t count what happened on Saturday then sure.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Akasuke", "So where are the others?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Hana", "They’ll arrive shortly. You guys can sit down and wait.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "While they were waiting they chatted about unrelated matters, like how their lives have been going. Hana recounted that one time when a rowdy first year came into the greenhouse behind the school without permission and destroyed half her garden after.", is_narrator=True)
    show_story_box("", "Her face turned into that of a monster just from thinking about it but quickly turned back her usual gentle one, mentioning that she had ‘punished’ him for it. Akasuke and Yuri didn’t dare to ask what she did.", is_narrator=True)
    
    # --- Part 2: Masayoshi Arrives ---
    show_story_box("", "After a short while, a man with long white hair tied in a ponytail entered the room. He wore a white kimono with Kasakura logo on the left chest, a bokken sheathed on his waist.", is_narrator=True)
    show_story_box("", "No doubt, this is Masayoshi Kouhei, the head of the disciplinary committee.", is_narrator=True)
    
    show_story_box("Akasuke", "Masayoshi-senpai.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Masayoshi", "I have arrived as per your request, President.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    show_story_box("Kageyama", "Nice to see you still healthy, Kouhei. And again, quit the formality and call me Kageyama already. We’re friends, aren’t we?", affiliation="Kasakura High School Student Council / Seven Wonders")
    
    show_story_box("Masayoshi", "Nay. It would be quite unscrupulous of me to act in that kind of manner, for this is an official meeting. I must address you appropriately.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    show_story_box("Yuri", "Still as uptight as ever, huh, senpai?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Masayoshi", "Formality preserves order. That is the core of discipline.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    show_story_box("", "The room fell silent after that, the five of them sitting and waiting for the other two latecomers to appear.", is_narrator=True)
    
    # --- Part 3: Natsume and Kagaku ---
    show_story_box("", "Finally, after what felt like an eternity for them, the last two arrived.", is_narrator=True)
    show_story_box("", "The first girl was Yokubukai Natsume, dressed up properly this time but her pink eyes still look as sleepy as ever and her long dark blue hair still looks like a mess.", is_narrator=True)
    show_story_box("", "The girl that followed behind was even shorter than her. She has long green hair, two shades of them actually, with most of her hair being dark while some parts are lighter. For her short stature, she sure is stacked in her chest area.", is_narrator=True)
    
    show_story_box("Kagaku", "Hanefuji-kun! Thanks for the catch, I got to play around with that girl to my heart’s content!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Yuri", "Kagaku-san…I hope ya didn’t kill her or somethin’.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Kagaku Shamiko, a crazy scientist. She loves experimenting with all sorts of stuff. She invented so many things that would’ve been great for the public to have but she only limited the use and recognition to her trusted friends, the reason being her distrust for misuse.", is_narrator=True)
    
    show_story_box("Kagaku", "Relax! No one’s been harmed, Inami-chi! Just a little injection and examination here and there is all!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Yuri", "Eh…", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Kagaku", "And speaking of which! Look who we brought along!", affiliation="Kasakura High School Student / Seven Wonders")
    
    # --- Part 4: Ayame Returns ---
    show_story_box("Everyone", "!!", affiliation="Seven Wonders & Student Council")
    
    show_story_box("", "The third figure appeared. It was Benikawa Ayame, whom they thought was still confined in Natsume’s lair.", is_narrator=True)
    show_story_box("", "Everyone’s reaction varies: Akasuke kicked the chair behind, ready to strike at any moment, Yuri was the same. Hana remained seated but her guard was obviously up, her smile was nowhere to be seen. Kouhei’s right hand was already gripped on his bokken.", is_narrator=True)
    show_story_box("", "Kageyama was the one with the least tense expression out of five of them.", is_narrator=True)
    
    show_story_box("Ayame Benikawa", "Yahoo~, everyone! Hah~, it’s been a while since I’ve seen sunlight, sure feels refreshing, huh?", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Akasuke", "What’s the meaning of this, Yokubukai?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Yokubukai Natsume", "Relax, Hanefuji. I’ll explain everything right now. You two go and sit.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Natsume explained that during the two days they’ve confined Ayame, they tried to investigate her further but she wouldn’t say anything more than she already had.", is_narrator=True)
    show_story_box("", "So she had a bright idea to just hire Ayame to be their bodyguard, that way she will be their ally and could give more information to them since she’s now technically a business partner.", is_narrator=True)
    
    show_story_box("Masayoshi", "And how can we be certain that this woman will not turn her blade against us?", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    show_story_box("", "He asked with a stern voice, his right eye opening.", is_narrator=True)
    
    show_story_box("Ayame Benikawa", "Ninja Rule Article 2 line 39: ‘A good ninja must not betray one’s client. Ones who dare to break the rule shall be branded as Ibara.’ There we have it~", affiliation="Benikawa Ninja Clan")
    show_story_box("", "She said with a smile.", is_narrator=True)
    
    show_story_box("Masayoshi", "If what she says is true, then the code itself binds her. However…", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    show_story_box("Ayame Benikawa", "Trust is not easily earned, is that right, Masayoshi-se-n-pai~", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Masayoshi", "Tch… Ah. Pardon my impoliteness, president.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    show_story_box("Kageyama", "Like I said, it’s fine.", affiliation="Kasakura High School Student Council / Seven Wonders")
    
    show_story_box("", "Akasuke glared at Ayame, he was still angry about her betrayal. To think he was having genuine fun with her all morning, to think he once thought of this woman as his friend, it didn’t sit right with him to suddenly have her as an ally again.", is_narrator=True)
    
    show_story_box("Ayame Benikawa", "Come on, what’s with that scary look, Hanefuji-kun? Don’t tell me you don’t trust lil’ ol’ me~?", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Akasuke", "Not even a little.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Yuri", "I second that.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Ayame Benikawa", "That glare of yours though, Hanefuji-kun… mm, I can feel it all over. Makes me wanna squirm in my seat.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Akasuke", "Hah?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Akasuke was obviously creeped out by that so he immediately stopped every interaction with her.", is_narrator=True)
    
    show_story_box("Yokubukai Natsume", "Are you all done? If so, let me continue.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Natsume further explained how the ninja world works. After officially hiring her, she instantly became open about the information.", is_narrator=True)
    
    show_story_box("Yokubukai Natsume", "Now that she’s our bodyguard, meaning we are all her employers, we can ask her anything and she would answer. I’ve already asked what I wanted to know, I wrote a list of all the important things for you all to read.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Natsume then tossed six stacks of paper at each and every member other than her.", is_narrator=True)
    
    show_story_box("Yokubukai Natsume", "One thing that she wouldn’t tell me, though…is how to differentiate ninjas from normal people.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Ayame Benikawa", "That one is against the rules, you know~ We ninjas aren’t allowed to rat each other out! Not unless the other party reveals themselves anyway!", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Yokubukai Natsume", "What she said.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "After some deep thoughtful minutes passed, Kageyama finally made the decision.", is_narrator=True)
    
    show_story_box("Kageyama", "For now, we’ll have to trust her. Benikawa may not be trustworthy in spirit, but in contract, she cannot betray us. That will have to suffice.", affiliation="Kasakura High School Student Council / Seven Wonders")
    
    show_story_box("Akasuke", "Prez, you can’t be serious!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Kageyama", "I am. If there is a storm coming, we need every weapon we can gather. Even if that weapon is a double-edged blade.", affiliation="Kasakura High School Student Council / Seven Wonders")
    
    show_story_box("", "The room fell quiet at his words. Nobody argued but nobody was satisfied either. Until Hana decided to break the silence with a chilling smile.", is_narrator=True)
    
    show_story_box("Hana", "If she steps out of line…I’ll bury her in my garden.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Ayame Benikawa", "Ooh~ I like that threat!", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Kageyama", "Then it’s decided. From today onward, Benikawa Ayame is under our employment as a bodyguard for the Seven Wonders.", affiliation="Kasakura High School Student Council / Seven Wonders")
    
    show_story_box("Masayoshi", "Very well. But I shall watch her like a hawk.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    show_story_box("", "And with that, the meeting was officially over.", is_narrator=True)
    
    # --- Part 5: The Dojo Scene ---
    show_story_box("", "********* ◆ *********\nAkasuke’s POV", is_narrator=True)
    
    show_story_box("", "\"Your fingers. They’re all healed.\"", is_narrator=True)
    
    show_story_box("", "It was after school. Benikawa and I were in our club dojo like we used to do back then. No one knew what happened between us so we tried to act as normal as we possibly could.", is_narrator=True)
    show_story_box("", "That being said. Her fingers, the ones I broke, were completely healed. It should’ve taken her six weeks at least but it’s only been two days.", is_narrator=True)
    
    show_story_box("Ayame Benikawa", "Oh that… Yikes! I don’t wanna think about it…", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Akasuke", "Let me guess…something to do with Kagaku?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Kagaku…where do I start? She’s an interesting girl to say the least.", is_narrator=True)
    show_story_box("", "The first time we met was quite eventful, she bombarded me with a bunch of questions like ‘How many times can you heal from third-degree burns before your cells start mutating?’ or ‘If I tore off your nails, would they regrow faster than average?’", is_narrator=True)
    show_story_box("", "Not exactly the kind of first impression I want.", is_narrator=True)
    show_story_box("", "So when I say she’s interesting, I mean she’s absolutely terrifying.", is_narrator=True)
    
    show_story_box("Ayame Benikawa", "…So right after you guys left, Natsume-chan called her and had her inject something into me. And what do you know, my fingers started healing. She said it was from your cells or something.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Akasuke", "Ah…yeah.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "So that was what it was for. I remembered her approaching me saying something like ‘Hanefuji-kun! Please, please, please, please, let me have a little bit of your blood sample! I wanna test something with it!’", is_narrator=True)
    show_story_box("", "I denied her several times but eventually gave in because it started to get annoying. So she was developing a healing serum with it. Great, I guess?", is_narrator=True)
    
    show_story_box("Ayame Benikawa", "And then…she made me do all sorts of things like test her newest potion which turned me into a guy for an hour… Do a full body examination, inside and out because she was curious about how I could scramble your brain by just smacking you.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Akasuke", "Yeah, not just her, me too. How did you do that?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Ayame Benikawa", "Hm…I’m not too sure myself~. I only discovered this ability recently.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "She raised her index finger up in the air.", is_narrator=True)
    
    show_story_box("Ayame Benikawa", "But basically, I just released some kind of electrical signal from my hand into your nervous system and then bam it just works.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Akasuke", "So even you don’t know the principle behind it.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Ayame Benikawa", "Yep! And I can’t even stack up another effect on the same person. For example, if I’ve already scrambled your motor function, then I can’t disable the flipping function in your brain.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Akasuke", "That’s more limiting than I thought.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Ayame Benikawa", "Enough to mess you up back then.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Akasuke", "True…", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Still…was it really okay to be sitting and talking with her so casually like this? She literally tried to kill us a few days ago. There was no guarantee if she wouldn’t try it again.", is_narrator=True)
    show_story_box("", "But still, from what I’ve read in Yokubukai’s list of ‘things to know about the ninja world’, it seems like they are just ordinary people living their lives in society but with a little twist in it.", is_narrator=True)
    show_story_box("", "They will receive education like normal people do, work an honest job like normal people do but when they were given a mission by their employer, they have to do it.", is_narrator=True)
    show_story_box("", "Each ninja can accept, at most, two missions at the same time and if they fail the mission, they wouldn’t lose their life or anything, they just lose their credibility, thus reducing the chance for them being hired again.", is_narrator=True)
    show_story_box("", "So following that, what Benikawa did was just that—her job. It didn’t matter if she wanted to do it or not, it was that she had to do it. If she defied the order she’ll be branded as an Ibara and get hunted down.", is_narrator=True)
    show_story_box("", "If that was true…then I feel kinda bad for her.", is_narrator=True)
    
    show_story_box("Akasuke", "Hey.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Ayame Benikawa", "Hm?", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Akasuke", "Back then. When you said you would regret killing us the most, how true was that?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Benikawa’s smile faded. She looked down on the ground.", is_narrator=True)
    
    show_story_box("Ayame Benikawa", "Why does that matter?", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Akasuke", "It matters because I need to know. If you were just saying that to get under my skin then fine. But…", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "I looked her in the eye.", is_narrator=True)
    
    show_story_box("Akasuke", "…if it was true then…I’ll treat you differently.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "She blinked, then gave me a strange look.", is_narrator=True)
    
    show_story_box("Ayame Benikawa", "Differently, huh? What, you gonna start being nice to me? Let me sit on your lap during breaks?", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Akasuke", "I’m serious, Benikawa.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "After a long silence, Benikawa let out a long sigh.", is_narrator=True)
    
    show_story_box("Ayame Benikawa", "It’s true. I would’ve regretted it. Not because I’m some saint or anything. Don’t get me wrong, killing is just part of the job sometimes. But you…you made me drop my guard. No one’s ever done that before.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Akasuke", "Drop your guard?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Ayame Benikawa", "Yeah. The whole time I was with you, I kept forgetting I was supposed to kill you. You were just so fun to be with…like I could live my life as a normal high school girl, y’know?", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "Benikawa smiled faintly, though it wasn’t her usual cheeky grin.", is_narrator=True)
    
    show_story_box("Ayame Benikawa", "Pathetic, huh? A ninja who forgets her mission because she was having too much fun.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "I stayed quiet. She sounded so genuine it caught me off-guard.", is_narrator=True)
    
    show_story_box("Ayame Benikawa", "You…don’t trust me, do you?", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Akasuke", "Of course not.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Ayame Benikawa", "Brutal.", affiliation="Benikawa Ninja Clan")
    show_story_box("", "She let out a little chuckle.", is_narrator=True)
    
    show_story_box("Ayame Benikawa", "And here I thought we were bonding.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Akasuke", "I’m not saying I never will. But trust isn’t something you’d earn after a few conversations. Especially not after you tried to kill me.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Ayame Benikawa", "Fair, hehe…", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "She shrugged, then leaned forward with a mischievous glint in her eyes.", is_narrator=True)
    
    show_story_box("Ayame Benikawa", "So I’ll just have to make you trust me. Bit by bit. Until one day you’ll let me sit on your lap during breaks.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Akasuke", "Why are you obsessed with that idea?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Ayame Benikawa", "Cuz that would annoy you.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "I shot her a glare, and just like before, she shivered slightly, her cheeks turning faintly pink.", is_narrator=True)
    
    show_story_box("Ayame Benikawa", "Mmh…there it is again. That glare. Don’t stop.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Akasuke", "You’re seriously creeping me out with that.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Ayame Benikawa", "That’s what makes it better~!", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "I sighed, deciding not to dignify that with a response.", is_narrator=True)

def play_stage_1_10_start():
    # Scene 1: Classroom - The Announcement
    show_story_box("Kojima-sensei", "So for the second-year’s school trip, we’re going to our school’s private island.", affiliation="Kasakura High School Teacher")
    
    show_story_box("", "The class erupted into cheers after Kojima-sensei’s declaration. Naganohara was practically shaking Shigemura who was sitting in front of her. On the other hand, he didn’t seem too excited about it. Typical.", is_narrator=True)
    show_story_box("", "What about me? Well, I would’ve been more hyped about it if we weren’t being targeted by some unknown forces at the moment.", is_narrator=True)
    show_story_box("", "And a new worry arose during these past few days. I realized that if there were people looking to kill me, then wouldn’t Kurona be in danger too? That thought alone made me scared.", is_narrator=True)
    
    show_story_box("", "I haven’t told her about it, of course. I didn’t want her to be overly scared and paranoid.", is_narrator=True)
    show_story_box("", "I consulted the third-year Wonders about it, they said she would be receiving full protection from them while I was gone. That put me in a little bit of relief.", is_narrator=True)
    show_story_box("", "So now the only worry we would have to think about was if someone’s going to sneak up on us second-year Wonders during the trip.", is_narrator=True)

    show_story_box("Kojima-sensei", "Alright, shut up. Pay attention to what I’m about to say.", affiliation="Kasakura High School Teacher")
    show_story_box("", "He hit the blackboard with his hand. The sheer loudness of it startled the entire class.", is_narrator=True)
    
    show_story_box("Kojima-sensei", "This is going to be a joint trip. We’re going with Heiwa Seiritsu, Kiryoku Gakuen, and Miyabi Academy.", affiliation="Kasakura High School Teacher")
    
    show_story_box("", "The class, which was filled with excitement before, was now filled with dissatisfaction.", is_narrator=True)
    show_story_box("", "This was probably to continue to foster the goodwill between the four schools.", is_narrator=True)
    show_story_box("", "The former Kasakura High’s student council president from five years ago had an idea to turn many schools into our school’s branches. The three schools Kojima-sensei mentioned earlier were included.", is_narrator=True)
    show_story_box("", "Needless to say, Heiwa Seiritsu and Kiryoku Gakuen didn’t take it too well and so those two teamed up and wreaked havoc on Kasakura.", is_narrator=True)
    
    show_story_box("", "Eventually, no one ended up becoming branches or anything, but they all came to peace and signed a treaty.", is_narrator=True)
    show_story_box("", "But a treaty that the higher-ups made without even listening to their respective general student bodies was just that, a treaty. It doesn’t mean anything. Tension was still high.", is_narrator=True)
    show_story_box("", "Until three years ago, Miyabi Academy, the one that sided with Kasakura from the very beginning, came up with an idea to ease the tension. Whenever there is a school trip, if possible, all four of the schools would all go together.", is_narrator=True)
    
    show_story_box("", "It worked, but not as effective as they expected. There was still some tension left. That was why right now, in this classroom, everyone wasn’t too happy about it.", is_narrator=True)
    show_story_box("", "For me? I didn’t have any personal grudge with them. Sure, I might have kicked some of Heiwa Seiritsu’s students asses but that was because they suddenly punched our first-year.", is_narrator=True)
    
    show_story_box("", "After Kojima-sensei discussed a few more things, the bell rang. Lunch break was here and he just left without even saying ‘that’s all’ or anything. Classic Kojima-sensei.", is_narrator=True)

    # Scene 2: Lunch Break
    show_story_box("", "Shigemura, Naganohara, Nishida, Yamashita, and Yuri were now forming a group at my desk.", is_narrator=True)
    
    show_story_box("Naganohara", "Aren’t you excited, Hanefuji-kun?", affiliation="Kasakura High School Student")
    show_story_box("", "Her golden eyes filled with restless excitement even after knowing that it was a joint trip.", is_narrator=True)
    show_story_box("Naganohara", "A private island, can you believe that!? Traveling on a cruise too!", affiliation="Kasakura High School Student")
    
    show_story_box("Shigemura", "What’s wrong, Hanefuji? You haven’t been smiling too well lately.", affiliation="Kasakura High School Student")
    show_story_box("", "He cut in, then glanced at Yuri.", is_narrator=True)
    show_story_box("Shigemura", "You too, Inami.", affiliation="Kasakura High School Student")
    
    show_story_box("", "This guy. Sharp as usual.", is_narrator=True)
    show_story_box("Yuri", "It’s nothin’!", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "It’s just prez’s been orderin’ us ‘round a lot without any break lately so we are just tired.", affiliation="Kasakura High School Student")
    
    show_story_box("Akasuke", "Yeah. What she said.", affiliation="Kasakura High School Student")
    show_story_box("Nishida", "Well, that’s true. You’ve been in the council room more often lately.", affiliation="Kasakura High School Student")
    show_story_box("Yamashita", "Yeah. Next time, ask for a break, yeah?", affiliation="Kasakura High School Student")
    show_story_box("", "Her eyes had a little hint of worry.", is_narrator=True)
    
    show_story_box("Akasuke", "That being said.", affiliation="Kasakura High School Student")
    show_story_box("", "I changed the subject. Didn’t want to linger on it for too long.", is_narrator=True)
    show_story_box("Akasuke", "How’s weapon-making club formation going?", affiliation="Kasakura High School Student")
    
    show_story_box("Shigemura & Nishida", "...", affiliation="Kasakura High School Student")
    show_story_box("", "Both Yamashita and Nishida fell to silence before Yamashita broke it.", is_narrator=True)
    
    show_story_box("Yamashita", "We can’t really officially form it… I mean, we only have two members and not many people are interested in becoming a weapon-maker in the future…", affiliation="Kasakura High School Student")
    
    show_story_box("", "So, no progress, huh? That sucks. I thought many people would take interest in it. Weapon-maker as a job makes more money than a CEO of a company can.", is_narrator=True)
    show_story_box("", "Yamashita and Nishida are childhood friends. They found a mutual interest in becoming weapon-makers after seeing a cop using a pair of jet-installed shoes to catch criminals.", is_narrator=True)
    
    show_story_box("Yamashita", "We thought people would line up once we announced it. Turns out most of the students here don’t wanna touch the subject. They’d rather join music clubs or sports clubs. Anything but sitting down, studying alloys, and melting steel.", affiliation="Kasakura High School Student")
    
    show_story_box("Yuri & Akasuke", "Oi, oi, don’t lump sports clubs into that.", affiliation="Kasakura High School Student")
    show_story_box("", "We glared at her.", is_narrator=True)
    show_story_box("Yamashita", "I meant no offense.", affiliation="Kasakura High School Student")
    
    show_story_box("Nishida", "I think the problem is the reputation too. Weapon-making sounds…y’know…shady. Like people immediately assume we’re supplying gangs or something.", affiliation="Kasakura High School Student")
    
    show_story_box("", "That was ridiculous, but I could kinda see why. If someone walked up to you and said, ‘Hey, wanna join the weapon-making club?’, it did sound like an underground syndicate.", is_narrator=True)
    show_story_box("", "I leaned back in my chair, folding my arms.", is_narrator=True)
    
    show_story_box("Akasuke", "Then you guys just need to change how you market it. Sell it as something flashy. Don’t call it Weapon-making club. Call it, I dunno, the Future Engineering Society or something.", affiliation="Kasakura High School Student")
    
    show_story_box("Nishida", "…That’s not bad.", affiliation="Kasakura High School Student")
    show_story_box("", "His eyes lighting up a bit.", is_narrator=True)
    
    show_story_box("Naganohara", "Anyway, wanna eat as a group~?", affiliation="Kasakura High School Student")
    show_story_box("Naganohara", "It’s been a while since the six of us have eaten together!", affiliation="Kasakura High School Student")
    
    show_story_box("", "Lunch together, huh? Yeah. A little relaxation with friends didn’t sound bad after everything that happened.", is_narrator=True)
    show_story_box("Akasuke", "That’s true. Let’s do that. Food’s on me.", affiliation="Kasakura High School Student")
    show_story_box("Naganohara", "For real!? Yer payin’, Akasuke-kun!? Yer the best!", affiliation="Kasakura High School Student")
    show_story_box("", "And with that, we left the classroom for the cafeteria and enjoyed our lunch.", is_narrator=True)

    # Time Jump
    show_story_box("", "********* ◆ *********", is_narrator=True)
    show_story_box("", "Akasuke’s POV – A Few Days Later", is_narrator=True)

    # Scene 3: Emergency Council Meeting
    show_story_box("", "The evening bell had just rung. Yuri, Benikawa, and I were heading toward the school gate when Kageyama’s voice cut through the hallway.", is_narrator=True)
    
    show_story_box("Kageyama", "Akasuke, Yuri, Benikawa. A moment. Council room. Now.", affiliation="Kasakura High School Student Council President")
    show_story_box("", "We exchanged glances. Benikawa raised an eyebrow, but we followed without question.", is_narrator=True)
    show_story_box("", "Inside, Kageyama stood by the window, arms crossed, expression grim.", is_narrator=True)
    
    show_story_box("Kageyama", "It's an emergency. Heiwa Seiritsu students are acting on their own. A large group—dozens, maybe more—crossed the boundary and are attacking the school grounds. They’re organized, this time even armed with improvised weapons. It’s not a prank.", affiliation="Kasakura High School Student Council President / Seven Wonders")
    
    show_story_box("Yuri", "Attacking? Now? The trip’s in a few days!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Akasuke", "If this escalates, the joint trip gets canceled. No way the higher-ups will let two schools that got at each other’s throats go on a cruise together.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Kageyama", "Exactly. Masayoshi has already deployed the Disciplinary Committee. They’ve suppressed most of the forces closest to campus. But the main group is still pushing toward the school from the direction of Heiwa Seiritsu.", affiliation="Kasakura High School Student Council President / Seven Wonders")
    show_story_box("Kageyama", "I need you three to run ahead to Heiwa Seiritsu High. Assess the situation on their end. Find out if their higher-ups know what’s happening. Contact them directly if possible. We need answers before this turns into a full war.", affiliation="Kasakura High School Student Council President / Seven Wonders")
    
    show_story_box("Akasuke", "Understood.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Yuri", "Let’s move.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Benikawa", "I’m in. Bodyguard duties, right?", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "We didn’t wait for more. We bolted out of the room, out the gate, and sprinted toward Heiwa Seiritsu High.", is_narrator=True)
    show_story_box("", "The run was short but tense—streets blurring, heart pounding. No words. Just purpose.", is_narrator=True)
    show_story_box("", "We reached their front yard in minutes.", is_narrator=True)
    
    show_story_box("", "A crowd of delinquent goons—uniforms untucked, makeshift weapons (bats, pipes, chains)—already waited, blocking the path to the main building.", is_narrator=True)
    show_story_box("", "No time for questions. They charged.", is_narrator=True)
    
    show_story_box("Akasuke", "Clear them.", affiliation="Kasakura High School Student / Seven Wonders")

def play_stage_1_10_end():
    show_story_box("", "Yuri moved first—ducked a bat swing, grabbed the wielder’s arm, twisted, threw him into two others with a clean ippon seoi-nage. Bodies crashed.", is_narrator=True)
    
    show_story_box("", "I stepped in—caught a pipe mid-swing, yanked the attacker forward, drove a knee into his gut. He dropped gasping. Another swung a chain; I sidestepped, palm-strike to throat—controlled, enough to choke him out without permanent damage.", is_narrator=True)
    
    show_story_box("", "Benikawa blurred past—Ryuusei Ken snapping out in rapid succession, three goons staggered back clutching ribs. Kagerou Geri whipped upward, heel cracking against a jaw. One went down hard.", is_narrator=True)
    
    show_story_box("", "No hesitation. No banter.", is_narrator=True)
    show_story_box("", "We carved through them—efficient, brutal when needed. Bodies hit the ground, weapons clattered.", is_narrator=True)
    
    show_story_box("", "The last few scattered, retreating toward the gates.", is_narrator=True)
    
    show_story_box("Akasuke", "Main building. Now.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "We broke into a run again, heading straight for Heiwa Seiritsu’s central structure—toward the higher-ups who had to know something.", is_narrator=True)

def play_stage_1_11_story():
    # --- Part 1: The Breach ---
    show_story_box("", "Akasuke’s POV", is_narrator=True)
    
    show_story_box("", "We burst through the double doors of Heiwa Seiritsu High’s main building.", is_narrator=True)
    
    show_story_box("", "The interior was a single massive structure—long, wide hallways lined with classrooms on both sides, connected directly to adjacent buildings without ever stepping outside. No elevators. Just endless flights of concrete stairs stretching upward. The kind of place built for people who think “musclebrained” is a compliment.", is_narrator=True)
    
    show_story_box("Akasuke", "Stairs. Lots of them.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Yuri", "Figures. No shortcuts in a school full of meatheads.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Ayame Benikawa", "Up we go then~.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "The higher-ups’ office was on the top floor. We didn’t have time to admire the architecture.\n\nThe moment our feet hit the lobby tiles, the remaining crowd of Heiwa Seiritsu delinquents turned as one.", is_narrator=True)
    
    show_story_box("", "Thirty, maybe forty of them—uniforms ripped, metal pipes, baseball bats, chains wrapped around fists. They filled the hallway like a wall of noise and rage. No words. No posturing. Just immediate, coordinated violence.", is_narrator=True)
    
    show_story_box("Akasuke", "Through them. Fast.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Yuri cracked her knuckles.", is_narrator=True)
    
    show_story_box("Yuri", "Got it.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Benikawa’s smile turned sharp.", is_narrator=True)
    
    show_story_box("Ayame Benikawa", "Finally~.", affiliation="Benikawa Ninja Clan")
    
    # --- Part 2: The Brawl ---
    show_story_box("", "They charged.", is_narrator=True)
    
    show_story_box("", "I met the first wave head-on. A pipe swung at my skull—I caught it mid-arc, twisted the wielder’s wrist until it popped, then drove my elbow into his sternum. He folded like paper. Another came from the left with a chain whip—I ducked low, swept his legs, and stomped down on his knee as he fell. Crack. He screamed.", is_narrator=True)
    
    show_story_box("", "Yuri flowed like water through the chaos. A delinquent lunged with a bat—she sidestepped, grabbed his arm, spun, and threw him shoulder-first into three others with a textbook ippon seoi-nage. The four crashed into a locker bank in a tangle of limbs and metal.", is_narrator=True)
    
    show_story_box("", "Benikawa danced. Ryuusei Ken snapped out in rapid bursts—three punches, three goons reeling back clutching solar plexuses. Kagerou Geri whipped upward in a crescent arc; a chain-wielder’s jaw snapped shut as her heel cracked against it. He dropped like a sack.", is_narrator=True)
    
    show_story_box("", "We pushed forward. Step by brutal step.", is_narrator=True)
    
    show_story_box("", "I knocked a pipe aside, drove a knee into a stomach, followed with an uppercut that lifted the guy off his feet. Yuri flipped another over her hip, slamming him into the wall. Benikawa blurred past me—her elbow slammed down like a hammer on a delinquent’s collarbone. He crumpled.", is_narrator=True)
    
    show_story_box("", "We were winning.\n\nBut something felt wrong.", is_narrator=True)
    
    # --- Part 3: The Knight ---
    show_story_box("", "A shadow passed my right side. It was fast, for a normal delinquent. It moved toward Yuri.", is_narrator=True)
    
    show_story_box("", "But I registered it in peripheral vision. Must've just been another enemy trying to flank.\nI kept my focus on the three in front of me.", is_thought=True)
    
    show_story_box("", "Blocked a bat, countered with a palm strike to the throat, spun and kicked another in the chest. He flew back into his friends.\n\nA few seconds passed.\nThen the feeling hit me like ice water.", is_narrator=True)
    
    show_story_box("", "Why didn’t he attack me?\nI was closer. Blind spot wide open. Any sane attacker would’ve taken the free shot.", is_thought=True)
    
    show_story_box("", "I turned my head—just a glance.", is_narrator=True)
    
    show_story_box("Akasuke", "Yur-", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Yuri was still standing.\nBut she wasn’t fighting.", is_narrator=True)
    
    show_story_box("", "A massive, clean hole had been torn straight through her torso—through her chest, through her spine, exiting out the back in a perfect circle of shredded uniform and blood.", is_narrator=True)
    
    show_story_box("", "Benikawa stood beside her—same wound. Same hole. Same lifeless expression frozen on her face as she collapsed forward.", is_narrator=True)
    
    show_story_box("", "They hit the floor together. Hard.", is_narrator=True)
    
    show_story_box("", "My brain stalled.\nThen I looked down.", is_narrator=True)
    
    show_story_box("", "A thick, chipped blade of cold steel ran through my own body—entered from behind, exited just below my ribs. The wound was already bleeding freely. I hadn’t even felt it.", is_narrator=True)
    
    show_story_box("", "Only now did the pain arrive—white-hot, drowning everything.\nI coughed. Blood sprayed across the tiles.", is_narrator=True)
    
    show_story_box("", "The sword slid out behind me with a wet scrape.\nRage took over before reason could.", is_narrator=True)
    
    show_story_box("", "I spun—full torque, right fist whipping around in a desperate haymaker aimed at the assailant’s face.\n\nIt never landed.", is_narrator=True)
    
    show_story_box("", "My body was already falling—knees buckling, vision tunneling.\nThe last thing I saw was him.", is_narrator=True)
    
    show_story_box("", "A literal medieval knight.\n\nOld, heavy armor—chipped white and cyan plates, dented gauntlets, a longsword still dripping red. He stood motionless, watching me fall, slowly sheathing the blade with deliberate calm.", is_narrator=True)
    
    show_story_box("", "What the hell..?\nwe never even made it to the trip...\nI never told Yuri…", is_thought=True)
    
    show_story_box("", "...\n.....\n.......", is_narrator=True)
    
    # --- Part 4: The Void & The Voice ---
    show_story_box("", "In the black, there's a voice.\nNot ethereal. Not saintly.\nA female voice..? It was normal. Slightly reverberated...though.", is_narrator=True)
    
    mystery_style1 = "dark_sea_green4" # Color for the mystery voice
    
    show_story_box("???", "Hmm...You weren’t supposed to die from that.", color_override=mystery_style1)
    
    show_story_box("", "I couldn’t speak. Couldn’t move. But I could think.", is_narrator=True)
    
    show_story_box("???", "Nobody was. That blade… it wasn’t meant to kill all of you.", color_override=mystery_style1)
    
    show_story_box("", "Pause.", is_narrator=True)
    
    show_story_box("???", "Anyways~, I’ll take responsibility. I’ll fix it, 'kay.", color_override=mystery_style1)
    
    show_story_box("", "She sounded exhausted.", is_narrator=True)
    
    show_story_box("???", "I’m so tired of this duty…though. I just want to stop.", color_override=mystery_style1)
    
    show_story_box("", "I wanted to scream. To demand answers.\nTo ask about Yuri.\nBut I couldn’t.", is_narrator=True)
    
    show_story_box("???", "So, yeah. Rest now. Just let me handle the rest.", color_override=mystery_style1)
    
    show_story_box("", "...\nRest?\nNo.\nYuri. Kurona. The others.\nI refused.", is_narrator=True)
    
    show_story_box("", "Suddenly—feeling returned, my voice worked.", is_narrator=True)
    
    show_story_box("Akasuke", "If I wasn’t supposed to die like that… then fix it.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "The voice sounded surprised.", is_narrator=True)
    
    show_story_box("???", "Ehh…You’re awake already?", color_override=mystery_style1)
    
    show_story_box("Akasuke", "Bring me back. Bring them back. Yuri...and Benikawa, too.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("???", "I can. But what comes next… won’t be easy-", color_override=mystery_style1)
    
    show_story_box("Akasuke", "-What do I have to do?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "She laughed—soft, tired, almost fond.", is_narrator=True)
    
    show_story_box("???", "You still can’t figure it out? Of course—go beat the hell out of the one that killed you~.", color_override=mystery_style1)
    
    # --- Part 5: Awakening ---
    show_story_box("", "Light exploded behind my eyes.\nI woke up gasping.", is_narrator=True)
    
    show_story_box("", "White ceiling. Antiseptic smell. Bandages wrapped tight around my chest. Patient gown.\n\n...Heiwa Seiritsu’s medical ward?", is_narrator=True)
    
    show_story_box("", "I sat up too fast—pain lanced through me, but it was dull. Manageable.", is_narrator=True)
    
    show_story_box("", "I was alive.\n\nWhat the hell happened?", is_narrator=True)

def play_stage_2_1_story():
    # --- Part 1: No Heartbeat ---
    show_story_box("", "Akasuke’s POV", is_narrator=True)
    
    show_story_box("", "Pain hit first.", is_narrator=True)
    
    show_story_box("", "Sharp, burning, right through the center of my chest.", is_narrator=True)
    
    show_story_box("", "I tried to sit up—bandages pulled tight, stitches tugging skin. Every breath felt like someone was twisting a knife still lodged between my ribs. I hissed, forced myself upright anyway, leaning back against the headboard of the narrow medical bed.", is_narrator=True)
    
    show_story_box("", "Grayed walls. Antiseptic smell. Thin curtains. This must be Heiwa Seiritsu’s infirmary.", is_narrator=True)
    
    show_story_box("", "I placed my right hand over my chest—right where the blade had gone through.\n\nNo heartbeat.", is_narrator=True)
    
    show_story_box("", "Just… silence.", is_narrator=True)
    
    show_story_box("", "My palm pressed harder. Nothing. No thump, no rhythm. Only the faint rustle of bandages and my own shallow breathing.", is_narrator=True)
    
    show_story_box("", "I stared at my hand like it belonged to someone else.", is_narrator=True)
    
    show_story_box("", "I remembered the sword. Clean through. Exited the front. Blood everywhere. Yuri and Benikawa were already down—holes were punched straight through them like paper.", is_thought=True)
    
    show_story_box("", "And then darkness.\nAnd that tired woman’s voice.", is_thought=True)
    
    show_story_box("Akasuke", "…I’m alive.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "The words felt stupid coming out. Of course I was alive. I was breathing. Hurting. Thinking.", is_thought=True)
    
    show_story_box("", "But no heartbeat.", is_thought=True)
    
    # --- Part 2: The Delinquent Nurse ---
    show_story_box("", "The door opened.", is_narrator=True)
    
    show_story_box("", "A girl walked in—messy uniform, tie loose, skirt hiked up one side like she didn’t care. She crossed her arms and leaned against the doorframe, legs crossed even though the pose looked ridiculous with a skirt.", is_narrator=True)
    
    show_story_box("", "Heiwa Seiritsu student. Definitely.", is_thought=True)
    
    # Define a style for the new minor character
    heiwa_girl_style = "khaki1"
    
    show_story_box("Heiwa Seiritsu Girl", "You finally woke up.", affiliation="Heiwa Seiritsu High School Student", color_override=heiwa_girl_style)
    
    show_story_box("Akasuke", "…Yeah..?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "She tilted her head.", is_narrator=True)
    
    show_story_box("Heiwa Seiritsu Girl", "You gonna move or what?", affiliation="Heiwa Seiritsu High School Student", color_override=heiwa_girl_style)
    
    show_story_box("Akasuke", "No…I can’t. Thanks to whoever did this horrible bandage work.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "She then pointed at herself.", is_narrator=True)
    
    show_story_box("Heiwa Seiritsu Girl", "Oh, yeah? That was me, idiot.", affiliation="Heiwa Seiritsu High School Student", color_override=heiwa_girl_style)
    
    show_story_box("Akasuke", "Eh? Ah…Sorry.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I winced, but not just from the pain.\nShort silence.", is_narrator=True)
    
    show_story_box("Akasuke", "You wouldn’t happen to know—", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "She cut me off before I finished.", is_narrator=True)
    
    show_story_box("Heiwa Seiritsu Girl", "No.", affiliation="Heiwa Seiritsu High School Student", color_override=heiwa_girl_style)
    
    show_story_box("Heiwa Seiritsu Girl", "The only thing I was told was: stay here and keep watch until the Kasakura guy wakes up. If he can walk, job done. If not, tell him to stay in bed while I go report back.", affiliation="Heiwa Seiritsu High School Student", color_override=heiwa_girl_style)
    
    show_story_box("", "She pushed off the doorframe.", is_narrator=True)
    
    show_story_box("Heiwa Seiritsu Girl", "So??? Can you walk?", affiliation="Heiwa Seiritsu High School Student", color_override=heiwa_girl_style)
    
    show_story_box("", "I tried to swing my legs off the bed. Pain lanced up my spine. I hissed, gripping the mattress.", is_narrator=True)
    
    show_story_box("Akasuke", "…Not yet.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Heiwa Seiritsu Girl", "Hahh…Figures.", affiliation="Heiwa Seiritsu High School Student", color_override=heiwa_girl_style)
    
    show_story_box("", "She turned.", is_narrator=True)
    
    show_story_box("Heiwa Seiritsu Girl", "Stay put. I’ll tell them you’re awake.", affiliation="Heiwa Seiritsu High School Student", color_override=heiwa_girl_style)
    
    show_story_box("", "The door clicked shut behind her.", is_narrator=True)
    
    show_story_box("", "I lay back slowly. Stared at the ceiling.", is_narrator=True)
    
    show_story_box("", "Yuri. Benikawa.\nMy friends at Kasakura.\nThe raid.\nWhat happened after I blacked out?", is_thought=True)
    
    # --- Part 3: Kagaku Enters ---
    show_story_box("", "The door opened again.", is_narrator=True)
    
    show_story_box("", "The same girl walked in—followed by someone I recognized instantly.\n\nKagaku Shamiko.", is_narrator=True)
    
    show_story_box("Kagaku", "She’s done her job. I promised her the school would let her off on the grade deduction for participating in the raid.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "The Heiwa girl grinned, gave a lazy wave, and left.\nNow it was just us.", is_narrator=True)
    
    show_story_box("Akasuke", "Kagaku… what the hell is going on?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Kagaku", "First off, nobody died.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "She said it casually, like reporting lab results.", is_narrator=True)
    
    show_story_box("Kagaku", "Well…a lot of people are heavily injured. But no one died.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I thought of the knight. The blade. The holes in Yuri and Benikawa.", is_thought=True)
    
    show_story_box("Akasuke", "The knight—", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Kagaku", "—wasn’t the main cause of the casualties.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "She pulled up a chair, sat backward on it, arms folded on the backrest.", is_narrator=True)
    
    show_story_box("Kagaku", "Heiwa Seiritsu brought a lot of strong fighters. The Disciplinary Committee did their best—suppressed most of them quickly. But the raid was well-coordinated. Way too coordinated.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Kagaku", "The Student Council thinks their delinquent top brass held some kind of meeting. If your group hadn’t cut straight into their campus and disrupted their momentum, it would’ve turned into real open war.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Akasuke", "Where’s Yuri? Benikawa? The others?", affiliation="Kasakura High School Student / Seven Wonders")
    
    # --- Part 4: Reunion ---
    show_story_box("", "Before she could answer, the door opened again.", is_narrator=True)
    
    show_story_box("", "Yuri walked in first—in patient gown, bandages wrapped around her chest, moving stiffly but alive. Behind her: Benikawa, same gown, same bandages. Then Shigemura and Naganohara—both looking pale but upright.", is_narrator=True)
    
    show_story_box("", "All of them. Alive.\nThank god.", is_thought=True)
    
    show_story_box("Yuri", "You’re awake.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Her voice cracked—just a little.", is_narrator=True)
    
    show_story_box("Shigemura", "We all got run through. Same guy, right?", affiliation="Kasakura High School Student")
    
    show_story_box("Naganohara", "Blue-white knight. Chipped old armor. Almost invisible presence. Sword came out of nowhere. Didn’t even give us a chance to fight!", affiliation="Kasakura High School Student")
    
    show_story_box("Akasuke", "Who else were attacked?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Kagaku", "Eight confirmed so far.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "She lifted the hem of her shirt just enough to show bandages wrapped around her own chest—same spot.", is_narrator=True)
    
    show_story_box("Kagaku", "Me too. I have a theory that I was first. I woke up first, patched myself, then went looking for the rest.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Akasuke", "Then…the raid?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Kagaku", "It was stopped. The Disciplinary Committee shut it down fast after you three went in and disrupted their main force. But…", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "She looked at me.", is_narrator=True)
    
    show_story_box("Akasuke", "...I want to go back to Kasakura. See the others in our medical ward.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Kagaku", "Well…", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "She smiled—small, almost apologetic.", is_narrator=True)
    
    show_story_box("Kagaku", "…I did say the battle was put to a swift end, but…", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "She didn’t say we won.", is_narrator=True)

def play_stage_2_2_story():
    # --- Part 1: The Situation Report ---
    show_story_box("", "Akasuke's POV", is_narrator=True)
    show_story_box("", "I stared at Kagaku.", is_narrator=True)
    show_story_box("Akasuke", "What do you mean Kasakura didn’t win?", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Kagaku", "Calm down. It’s a stalemate right now.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "She leaned forward, elbows on knees.", is_narrator=True)
    show_story_box("Kagaku", "Most of Heiwa Seiritsu’s main forces are lurking just outside Kasakura’s campus grounds. They haven’t made a move around the time…since the knight appeared.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Kagaku", "Around the same time that happened, one of the victims was Kaoru Hana—one of the Seven Wonders. That put a huge dent in our fighting power.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Akasuke", "Kaoru-senpai…", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Kagaku", "Masayoshi Kouhei went out alone to retrieve her once she was revived. He ordered the Disciplinary Committee to pull back and concentrate all remaining forces at Kasakura’s main buildings—regroup and fortify. That’s why Heiwa hasn’t been able to overrun us completely.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "She gave a small grin.", is_narrator=True)
    show_story_box("Kagaku", "And they never will. Not while the combat-capable Seven Wonders are still standing. You know this~. Hana’s probably recovered by now. Kouhei and the President weren’t even attacked by the knight.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Kagaku", "Kasakura isn’t falling anytime soon.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Akasuke", "Then how did you get out?", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Kagaku", "I escaped the encirclement with Shigemura and Naganohara. They’ve already recovered enough to come help your group here. I’m a genius, after all—so I sent that Heiwa girl ahead to patch you three up before we even arrived.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "She shrugged, almost proud.", is_narrator=True)

    # --- Part 2: The 8th Victim ---
    show_story_box("Akasuke", "Who was the last one attacked? You said eight confirmed.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Kagaku", "Ah…Natsume. Yokubukai Natsume.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "Her expression darkened slightly.", is_narrator=True)
    show_story_box("Kagaku", "She’s…doing the worst physically. Me and her are ‘Seven Wonders’, but weren’t combatants to begin with. I’m still suppressing pain from my own wound right now…but I had to get everyone up to speed.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Akasuke", "Where was she when it happened?", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Kagaku", "Alone in her hidden base. I was the only one who knew the location. I figured she might’ve been targeted, so I went looking. She was the last to get treated, sooo…wounds took longer to stabilize.", affiliation="Kasakura High School Student / Seven Wonders")

    # --- Part 3: Moving Forward ---
    show_story_box("", "I exhaled slowly.", is_narrator=True)
    show_story_box("", "My healing factor had already kicked in hard—stitches pulling, pain dulling to a deep ache. Mixed with the anger, the fear for Yuri, all the confusion—I could move. I just have to move.", is_narrator=True)
    show_story_box("", "I swung my legs off the bed…and stood. I wobbled once, but caught myself on the rail.", is_narrator=True)
    show_story_box("Kagaku", "Eh? Hey—stay in bed! You’re still—", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Yuri", "Let him. Once he starts movin’, he can’t be stopped.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "She gave me a small, tired smile.", is_narrator=True)
    show_story_box("", "I nodded. I took a step. Then another. The pain was there, but bearable.", is_narrator=True)
    show_story_box("Akasuke", "Let’s go.", affiliation="Kasakura High School Student / Seven Wonders")

    # --- Part 4: Departure ---
    show_story_box("", "We left the infirmary together—Yuri, Benikawa, Shigemura, Naganohara, Kagaku, and me.", is_narrator=True)
    show_story_box("", "The hallways of Heiwa Seiritsu were empty. Kagaku explained as we walked.", is_narrator=True)
    show_story_box("Kagaku", "It’s only obvious both schools would issue stay-home orders to all unaffected students after all that. No one’s on campus right now. Safer that way.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "We reached the main lobby—same place we’d been cut down.", is_narrator=True)
    show_story_box("", "Bloodstains still on the tiles. Dried and dark.", is_narrator=True)
    show_story_box("", "Our uniforms were there—folded on a bench by the wall, blood crusted but intact.", is_narrator=True)
    show_story_box("", "We changed quickly. No words. Just purpose.", is_narrator=True)
    show_story_box("Yuri", "Back to Kasakura.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Akasuke", "Right now.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "We stepped out of Heiwa Seiritsu’s front gate.", is_narrator=True)

def play_stage_2_3_start():
    # --- Scene 1: Masayoshi at the Gate ---
    show_story_box("", "Kasakura High School’s front yard looked wrong.", is_narrator=True)
    show_story_box("", "Heiwa Seiritsu delinquents—twenty, maybe thirty—lounged around the gate like they owned the place.", is_narrator=True)
    show_story_box("", "Untucked uniforms, metal pipes dangling from belts, cigarettes glowing in the evening haze. They laughed too loud, shoving each other, eyes flicking toward the main building.", is_narrator=True)
    show_story_box("", "One of them—a tall guy with a shaved head and a scar across his eyebrow—grinned at his friends.", is_narrator=True)
    
    # Generic enemies usually get red boxes
    enemy_style = "red"
    
    show_story_box("Heiwa Delinquent", "Hundred yen says I can run inside, touch the lobby floor, and get back out before anyone notices.", affiliation="Heiwa Seiritsu High School Student", color_override=enemy_style)
    show_story_box("", "Another laughed.", is_narrator=True)
    show_story_box("Heiwa Delinquent", "No one’s even guarding the front. Easy money.", affiliation="Heiwa Seiritsu High School Student", color_override=enemy_style)
    show_story_box("", "Scar-eyebrow cracked his neck.", is_narrator=True)
    show_story_box("Heiwa Delinquent", "Watch this.", affiliation="Heiwa Seiritsu High School Student", color_override=enemy_style)
    
    show_story_box("", "He sprinted forward—fast, cocky, boots slapping pavement. Reached the double doors. One foot crossed the threshold—\n\nCRACK!", is_narrator=True)
    show_story_box("", "A wooden bokken whipped out from the shadows inside, slamming into his ankle with surgical precision. Bone crunched. He screamed, stumbling.", is_narrator=True)
    show_story_box("", "Before he could fall, the bokken retracted—and snapped forward again, striking the back of his neck in a perfect follow-through. Lights out. He dropped like a puppet with cut strings.", is_narrator=True)
    
    show_story_box("", "Masayoshi Kouhei stepped into view.", is_narrator=True)
    show_story_box("", "White kimono pristine despite the chaos. Long white ponytail swaying slightly. Bokken already back at his side, held with effortless poise.", is_narrator=True)
    show_story_box("Masayoshi", "Nay. Thou shalt not step foot within these halls.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    show_story_box("", "His voice carried—old-fashioned, calm, absolute.", is_narrator=True)
    show_story_box("Masayoshi", "I shall be watching like a hawk.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    show_story_box("", "He gently nudged the unconscious delinquent with his foot, rolling him back toward his stunned friends.", is_narrator=True)
    show_story_box("Masayoshi", "Take thy comrade and depart. Lest further indiscipline require sterner correction.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    show_story_box("", "The group hesitated—then backed off, dragging their fallen friend away, muttering curses under their breath.", is_narrator=True)

    # --- Scene 2: On the Road ---
    show_story_box("", "On the Road Between Heiwa Seiritsu and Kasakura\nAkasuke’s POV", is_narrator=True)
    show_story_box("", "We moved fast—side streets, alleys, avoiding main roads where patrols might spot us.", is_narrator=True)
    show_story_box("", "Stray Heiwa delinquents were everywhere—small groups on lookout, specifically hunting for us after our earlier raid.", is_narrator=True)
    show_story_box("Akasuke", "More ahead.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Yuri", "Let’s clear them.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Benikawa", "On it~.", affiliation="Benikawa Ninja Clan")

def play_stage_2_3_end():
    # --- Scene 3: Skirmish Aftermath ---
    show_story_box("", "The fights were quick, brutal, efficient.", is_narrator=True)
    show_story_box("", "I took point—bursts staggering two at once, followed by a low sweep that dropped a third. Yuri flipped one over her shoulder into a wall. Benikawa danced through them—kicks cracking jaws, Enryū Ha downward elbows sending bodies flying.", is_narrator=True)
    show_story_box("", "Naganohara stayed at the back with Kagaku. Shigemura was in front, guarding them.", is_narrator=True)
    show_story_box("Akasuke", "Shigemura—you okay hanging back? Can you fight if needed?", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Shigemura", "Yeah…somewhat. It’s gonna be a pain, though.", affiliation="Kasakura High School Student")
    show_story_box("", "His usual tone—nonchalant, almost bored.", is_narrator=True)
    show_story_box("Benikawa", "Oh! He’ll be fine.", affiliation="Benikawa Ninja Clan")
    show_story_box("", "She didn’t elaborate. Just smiled.", is_narrator=True)
    show_story_box("", "We kept moving. Every encounter ended the same: Heiwa goons down, us advancing.", is_narrator=True)
    show_story_box("", "We picked up the pace.", is_narrator=True)

def play_stage_2_4_start():
    # --- Scene 1: The Infirmary ---
    show_story_box("", "Kasakura High School’s infirmary firmly smelled of old linens.", is_narrator=True)
    
    show_story_box("", "Natsume lay in the far bed, bandages wrapped thick around her chest. She looked small under the sheets—pale, breathing shallow. Hana sat beside her, chair pulled close, a small tray of food on her lap: rice porridge, steamed vegetables, miso soup. Gentle and patient.", is_narrator=True)
    
    show_story_box("Hana", "You’re finally awake.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Natsume’s pink eyes fluttered open. She winced as she tried to sit up.", is_narrator=True)
    
    show_story_box("Yokubukai Natsume", "…Hana.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Hana", "Don’t move too fast. Eat something first.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "She spooned a small portion of porridge, held it out.", is_narrator=True)
    
    show_story_box("Hana", "You’ve been out a while.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Natsume stared at the spoon, then at Hana.", is_narrator=True)
    
    show_story_box("Yokubukai Natsume", "I’m… fine for now.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "She took the spoon with trembling fingers, and ate slowly.", is_narrator=True)
    
    show_story_box("Yokubukai Natsume", "The situation?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Hana", "It’s a stalemate. Heiwa’s forces are still outside the perimeter—spread thin but not retreating. They’re waiting. Watching.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Natsume exhaled.", is_narrator=True)
    
    show_story_box("Yokubukai Natsume", "And inside?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Hana", "Kouhei pulled everyone back to the main buildings. Concentrated defense. No one’s broken through yet.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Natsume closed her eyes briefly.", is_narrator=True)
    
    show_story_box("Yokubukai Natsume", "There was…a ‘knight’..?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Hana", "Gone. No trace since it took out eight of us. We’re all by some miracle back like you, though.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Natsume nodded once. Then:", is_narrator=True)
    
    show_story_box("Yokubukai Natsume", "Give me the earbud.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Hana handed her a tiny red-star-decorated device—Natsume’s own invention. Long-range, encrypted, crystal-clear.\nNatsume pressed it to her ear.", is_narrator=True)
    
    show_story_box("Yokubukai Natsume", "Kagaku. Status.", affiliation="Kasakura High School Student / Seven Wonders")
    
    # --- Scene 2: The Strategy ---
    show_story_box("", "On the Road to Kasakura\nKagaku’s earbud chimed. She tapped it once.", is_narrator=True)
    
    show_story_box("Kagaku", "Natsume. You’re awake!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Natsume", "Obviously. You recovered too, no? Now, enemy ranks?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Kagaku", "Perimeter’s choked with fodder. The skilled combatants seem to be spaced far apart—like lookouts, not frontline. They’re not pressing in.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Natsume", "The issue isn’t strength. It’s numbers. Kasakura’s main buildings only have half the Disciplinary Committee right now. The rest are elite—indispensable.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Natsume", "If we sally out, Heiwa floods the interior. Then we lose the stronghold.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Akasuke", "Can’t we just hold inside until higher-ups or authorities force a resolution?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Natsume", "No. Heiwa has nothing to lose. They’ll wait, then rush everything at once sooner or later. Even if they lose in the end, Kasakura’s buildings will be trashed. No one wants that.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Kagaku", "Sooo…?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Natsume", "Your group breaks through the front. Disrupt their formation. They’re musclebrained—once they hear Akasuke’s back inside their turf, they’ll swarm to your position.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Natsume", "That’s when the forces inside Kasakura sally out and encircle them. Stalemate becomes victory.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Akasuke", "...What’s their motive?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Natsume", "I.D.K. I want to know as well.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Her voice tightened.", is_narrator=True)
    
    show_story_box("Natsume", "It’s strange. Heiwa delinquents are hotheaded, not patient. They should’ve rushed in or gotten bored and left by now. This level of coordination, this persistence… it’s not them.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Kagaku", "End goal.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Natsume", "Hm?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Kagaku", "They’re not just here to smash Kasakura. They probably want something inside. Something specific. If we figure out what they’re after—beyond just hurting a rival school—we might cut the root.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Natsume was silent for a moment.", is_narrator=True)
    
    show_story_box("Natsume", "Hm. Agreed. I’ll dig from here. You push forward.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "The line clicked off.", is_narrator=True)
    
    show_story_box("Akasuke", "Let’s move.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "The school’s silhouette grew closer.", is_narrator=True)

    # --- Scene 3: The Charge ---
    show_story_box("", "Kasakura High\n\nThe front gates of Kasakura High loomed ahead—wide open, and only a scattering of Heiwa Seiritsu fodder delinquents loitering like they already owned the place.", is_narrator=True)
    
    show_story_box("Akasuke", "Through them. No hesitation.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Yuri", "Got it.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Benikawa", "Let’s go~!", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "We charged.", is_narrator=True)
    
    show_story_box("", "The first wave spotted us—eyes widening, mouths opening in stupid grins.", is_narrator=True)
    
    enemy_style = "red"
    show_story_box("Heiwa Delinquent", "It’s them! The Kasakura ‘Wonders’!", affiliation="Heiwa Seiritsu High School Student", color_override=enemy_style)
    
    show_story_box("", "They rushed—bats raised, pipes swinging, chains whipping.", is_narrator=True)

def play_stage_2_4_end():
    # --- Scene 4: The Breach ---
    show_story_box("", "I met the center head-on. Ryuusei Ken snapped out three times—three goons staggered back clutching ribs. I followed with a low hook kick, sweeping legs out from under two more. They hit the ground hard.", is_narrator=True)
    
    show_story_box("", "Yuri flowed left flank—ippon after ippon. Bodies flew over her shoulder into each other like dominoes.", is_narrator=True)
    
    show_story_box("", "Benikawa danced right—kicks and elbows slamming down like hammers. Three down in seconds.", is_narrator=True)
    
    show_story_box("", "Shigemura stayed near the back with Naganohara and Kagaku, expression calm, hands in pockets that occasionally swung out to suppress any strays.", is_narrator=True)
    
    enemy_style = "red"
    show_story_box("Heiwa Delinquent", "Get ‘em! Surround ‘em!", affiliation="Heiwa Seiritsu High School Student", color_override=enemy_style)
    
    show_story_box("", "More poured in from the sides—twenty, thirty now. They harassed, circled, and tried to overwhelm with numbers.", is_narrator=True)
    
    show_story_box("", "But we pushed.\nStep by step. Blow by blow.", is_narrator=True)
    
    show_story_box("", "They were fodder—stronger than average high-schoolers, but not “Seven Wonders” level. Not us.\nWe carved forward—toward the main building.", is_narrator=True)
    
    # --- Scene 5: Natsume's Investigation ---
    show_story_box("", "Natsume’s POV\n\nInside Kasakura’s main building—ground floor hallway—security monitors glowed in the dimly lit council monitoring room.", is_narrator=True)
    
    show_story_box("", "Prez is at the central console, arms crossed, watching feeds. A new student council member—quiet, glasses, clipboard in hand—stood beside him, noting timestamps. Good to know he’s got hard working ‘freshies this year.", is_narrator=True)
    
    show_story_box("Natsume", "Any change?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Kageyama", "The perimeter is still surrounded. No major push since the incident with the ‘knight’ you mentioned. They’re waiting.", affiliation="Kasakura High School Student Council President / Seven Wonders")
    
    show_story_box("", "I limped forward—bandages tight around my chest. My breathing has been shallow. Pain throbbed with every step…but I have ignored it.", is_narrator=True)
    
    show_story_box("Natsume", "Good. Keep your eyes on the front gate.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I turned toward the hallway exit—then froze.", is_narrator=True)
    
    show_story_box("", "Footsteps. Multiple. Running.\nHeiwa Seiritsu delinquents burst around the corner—six, maybe seven—pipes and bats raised, eyes wild.", is_narrator=True)
    
    show_story_box("Natsume", "…How?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Before the closest one could swing, a figure flashed past from behind.", is_narrator=True)
    
    show_story_box("Masayoshi", "Nay.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    show_story_box("", "His bokken whipped out—first strike cracked against a wrist, disarming. Second snapped across a neck—perfect follow-through. The goon dropped.", is_narrator=True)
    
    show_story_box("", "Two more lunged.", is_narrator=True)
    
    show_story_box("", "He moved like water—bokken spinning, blocking one pipe, redirecting it into another attacker’s knee. Crack. He spun, reverse strike to the temple. Lights out.", is_narrator=True)
    
    show_story_box("", "The rest hesitated.", is_narrator=True)
    
    show_story_box("Masayoshi", "Thou shalt not pass.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    show_story_box("", "He stood between us—bokken steady, posture flawless.", is_narrator=True)
    
    show_story_box("Masayoshi", "What are you doing here, Natsume?", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    show_story_box("Natsume", "Investigating. Cover me. I need to reach Kagaku’s labs.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Masayoshi’s eyes narrowed.", is_narrator=True)
    
    show_story_box("Masayoshi", "I recall there being two facilities. Both of them?", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    show_story_box("Natsume", "Yes. They’re on opposite ends of the school. I need to see if anything was taken—or planted.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "He nodded once.", is_narrator=True)
    
    show_story_box("Masayoshi", "Then let us move. I shall guard thy path.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    show_story_box("", "We started forward—Masayoshi leading, bokken ready.", is_narrator=True)
    
    show_story_box("Natsume", "Hm. They didn’t take the bait.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Masayoshi", "Indeed. Akasuke’s charge at the front should have drawn them like moths. Instead, they mobilized inward, as if planned.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    show_story_box("Natsume", "This isn’t their usual musclebrain chaos. Someone planned this.", affiliation="Kasakura High School Student / Seven Wonders")
    
    # --- Scene 6: The Iron Fist & The Transformation ---
    show_story_box("", "Akasuke’s POV\nFront yard of Kasakura.", is_narrator=True)
    
    show_story_box("", "We were winning—easily.\nGoons fell in waves. But reinforcements weren’t flooding toward us like Natsume predicted.", is_narrator=True)
    
    show_story_box("Akasuke", "They’re not biting. Something’s wrong.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Yuri", "They’re holding back—", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "A new figure broke from the side—fast, skilled.\nHe rushed towards Shigemura.", is_narrator=True)
    
    show_story_box("", "He barely glanced.", is_narrator=True)
    
    show_story_box("Shigemura", "Come on.", affiliation="Kasakura High School Student")
    
    show_story_box("", "The new enemy—taller, better stance—threw a clean, tricky hook.\nShigemura blocked late—took the punch square to the face. He snapped back, blood from his lip.", is_narrator=True)
    
    boss_style = "red"
    show_story_box("Heiwa Seiritsu Gang Leader", "Heh, ‘name’s Kuroda. ‘Iron Fist of Heiwa.’ Remember it when ya are on the ground.", affiliation="Heiwa Seiritsu High School Student", color_override=boss_style)
    
    show_story_box("", "His minions cheered.", is_narrator=True)
    
    show_story_box("", "Kuroda assaulted—rapid fists that quickly retract and extend like pistons. Shigemura blocked most, but faltered—took another hit to the ribs and staggered.", is_narrator=True)
    
    show_story_box("Akasuke", "Shigemura!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "We wanted to help—but our hands were full. Goons pressed us from all sides.", is_narrator=True)
    
    show_story_box("", "Then Kuroda suddenly broke off—dashing toward the backline.\nToward Naganohara and Kagaku.", is_narrator=True)
    
    show_story_box("", "Damnit!", is_thought=True)
    
    show_story_box("", "Shigemura chased—too slow.\nKuroda’s fist reared back—aimed straight for Naganohara’s face.\n\n..!", is_narrator=True)
    
    show_story_box("", "Then…there was a blue light.\nIt flared from her chest—right where the knight’s blade had long punched through.", is_narrator=True)
    
    show_story_box("", "Naganohara’s hand snapped up—caught Kuroda’s wrist mid-punch. Stopped it cold.", is_narrator=True)
    
    show_story_box("", "The blue light spread—covered her body like liquid fire, then dissipated.\nWhen it cleared—\nShe wasn’t Naganohara anymore.", is_narrator=True)
    
    show_story_box("", "No. It was more like she’s…a different Naganohara.", is_narrator=True)
    
    show_story_box("", "Her outfit had changed…Heiwa Seiritsu delinquent style—untucked shirt, loose tie, skirt hiked. Hair restyled…\n…Same messy ponytail as the girl who’d bandaged me in the infirmary.", is_narrator=True)
    
    show_story_box("", "Same face. Same eyes as Naganohara.\nBut still different.", is_narrator=True)
    
    # Naganohara retains her default text/name color despite the affiliation change
    show_story_box("Naganohara", "…Gotcha.", affiliation="???")
    
    show_story_box("", "Her voice—lower, rougher. Heiwa accent.", is_narrator=True)
    
    show_story_box("Naganohara", "You really thought you could touch me?", affiliation="???")
    
    show_story_box("", "Kuroda froze. Confused like everyone else.", is_narrator=True)
    
    show_story_box("", "She twisted his wrist. Bone popped.\nHe screamed.", is_narrator=True)
    
    show_story_box("", "She slammed him, sending the thug sliding meters away.\nThe front yard went quiet.", is_narrator=True)
    
    show_story_box("Akasuke", "…Naganohara?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "She turned—smirked.", is_narrator=True)
    
    show_story_box("Naganohara", "Uh? Ah, yeah. But, not quite…", affiliation="???")

def play_stage_2_5_start():
    # --- Scene 1: Kagaku's First Lab ---
    show_story_box("", "Natsume’s POV\n\nKagaku’s first lab was a mess—exactly as expected.", is_narrator=True)
    show_story_box("", "Shelves crammed with half-finished prototypes, scattered circuit boards, vials of glowing liquids labeled with Kagaku’s chaotic handwriting. I limped through the clutter, chest aching under the bandages, scanning for anything out of place.", is_narrator=True)
    show_story_box("", "Nothing obvious stolen. No signs of forced entry. Just her usual disaster zone.", is_narrator=True)
    show_story_box("", "I found a black box gadget’s blueprints buried under a pile of failed blueprints—big red marker scrawl across the top:\n\"Lost, dunno where. ¯\_(ツ)_/¯\"", is_narrator=True)
    show_story_box("", "Typical Kagaku.", is_narrator=True)
    show_story_box("", "I pocketed her research notebook/diary instead—thick, dog-eared, filled with sketches and rants. Might be useful later.", is_narrator=True)
    show_story_box("", "I stepped back into the hallway.", is_narrator=True)
    show_story_box("", "Masayoshi leaned against the wall—bokken resting on his shoulder, surrounded by a semicircle of unconscious Heiwa delinquents sprawled on the floor like broken dolls.", is_narrator=True)
    show_story_box("Masayoshi", "Hast thou concluded thy search?", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    show_story_box("Natsume", "Nothing of note here. We probably need the second lab—on the other side of campus.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "He nodded once. Straightened.", is_narrator=True)
    show_story_box("Masayoshi", "Let us make haste.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    # --- Scene 2: The Chase ---
    show_story_box("", "We moved—him in front, bokken ready. I followed, steps measured to hide the pain.", is_narrator=True)
    show_story_box("", "Halfway down the next corridor, we heard them—boots pounding, voices shouting. Another group of Heiwa delinquents rounded the corner—eight this time—but only running in the same direction we were headed.", is_narrator=True)
    show_story_box("", "Hm.", is_thought=True)
    show_story_box("Natsume", "…They’re all converging on Kagaku’s second lab.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "Masayoshi didn’t hesitate.", is_narrator=True)
    show_story_box("Masayoshi", "Stay behind me.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    show_story_box("", "He surged forward—bokken a blur. First swing disarmed two at once. Second cracked ribs. Third swept legs. Bodies hit the floor in seconds.", is_narrator=True)
    show_story_box("", "No wasted motion. No mercy.", is_narrator=True)
    show_story_box("Natsume", "This is both good and bad.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Masayoshi", "Speak.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    show_story_box("Natsume", "The ‘good’—they’re confirming the second lab is definitely our target. ‘Bad’—someone may already be inside. We need to move faster.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "I looked up at him.", is_narrator=True)
    show_story_box("Natsume", "Alright. Carry me. Run full speed.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "He didn’t question it.", is_narrator=True)
    show_story_box("Masayoshi", "As thou command.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    show_story_box("", "He scooped me up—princess carry, surprisingly gentle despite the armor-like formality—and broke into a sprint.", is_narrator=True)
    show_story_box("", "Wind rushed past. Pain flared, but I gritted my teeth.\nWe had to reach that lab.", is_narrator=True)

    # --- Scene 3: Akasuke's POV - The Confirmation ---
    show_story_box("", "Akasuke’s POV", is_narrator=True)
    show_story_box("Shigemura", "…Naganohara?", affiliation="Kasakura High School Student")
    show_story_box("", "She turned—smirked, then suddenly nervous, eyes wide, hands waving.", is_narrator=True)
    show_story_box("Naganohara", "Y-Yeah! It’s me! It’s really me!", affiliation="???")
    show_story_box("", "She bounced on her toes—extroverted, exaggerated, same pure Naganohara energy despite the new look.", is_narrator=True)
    show_story_box("Naganohara", "Ask me anything! Lunch a few days ago? Melon bread and curry! Right? Favorite color? Pink—like my hair!", affiliation="???")
    show_story_box("Shigemura", "…It’s her.", affiliation="Kasakura High School Student")
    show_story_box("", "No time for more talk.\nRemaining thugs rushed again—desperate now.", is_narrator=True)
    show_story_box("", "We met them head-on.", is_narrator=True)

def play_stage_2_5_end():
    # --- Scene 4: Post-Battle Reversion ---
    show_story_box("", "Naganohara fought too—surprisingly well. Same level as Shigemura: quick dodges, sharp counters, nothing flashy but effective.", is_narrator=True)
    show_story_box("", "Goons fell fast.", is_narrator=True)
    show_story_box("", "When the last one dropped, blue light flared again—from her chest.\nIt spread—covered her—then dissipated.", is_narrator=True)
    show_story_box("", "And she was back.\nNormal uniform. Normal hair. Normal Naganohara.", is_narrator=True)
    show_story_box("", "She swayed—exhausted.\nShigemura caught her gently before she hit the ground.", is_narrator=True)
    show_story_box("Naganohara", "…Tired…", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Akasuke", "What was that?", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "She smiled weakly.", is_narrator=True)
    show_story_box("Naganohara", "I…don’t know either…", affiliation="Kasakura High School Student / Seven Wonders")

def play_stage_2_6_story():
    # --- Scene 1: Arrival at the Second Lab ---
    show_story_box("", "Natsume’s POV\n\nMasayoshi carried me at full sprint—wind whipping past, pain flaring in my chest with every jolt. I gritted my teeth and focused on the path ahead.", is_narrator=True)
    show_story_box("", "We reached Kagaku’s second lab—the old experimental classroom the school had handed over years ago after building a newer one elsewhere. Massive room. High ceilings. Long workbenches. Space for entire classes to run simple experiments.", is_narrator=True)
    show_story_box("", "The door was ajar.\nInside: chaos.", is_narrator=True)
    show_story_box("", "Heiwa goons—ten, twelve—trashed the place. Smashing equipment. Rifling through drawers. Tearing open boxes of scrap. Searching. Desperate.", is_narrator=True)
    show_story_box("", "Masayoshi set me down gently against the hallway wall.", is_narrator=True)
    show_story_box("Masayoshi", "Remain outside.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    show_story_box("", "I nodded.\nHe stepped inside.", is_narrator=True)

    # --- Scene 2: Masayoshi Cleans House ---
    show_story_box("", "The first goon turned—too slow. Bokken cracked across his wrist. Weapon clattered. Second swing—temple. Down. Third—neck. Out.", is_narrator=True)
    show_story_box("", "They rushed him.", is_narrator=True)
    show_story_box("", "He moved like water through stone—bokken spinning, parrying, striking vital points with surgical precision. Bodies dropped in seconds. No wasted motion. No mercy.", is_narrator=True)

    # --- Scene 3: The Notebook ---
    show_story_box("", "I stayed outside—watching through the cracked door—while I pulled out Kagaku’s research notebook.", is_narrator=True)
    show_story_box("", "I flipped to the latest pages.\nScribbled theories. Diagrams. Equations.", is_narrator=True)
    show_story_box("", "One section jumped out:\n\n**Parallel Universes**", is_narrator=True)
    show_story_box("", "Kagaku’s handwriting—messy, excited:\n\n\"Infinite timelines. Every possibility exists somewhere, I just know it!. If we can bridge even one gap—access another version of reality—materials, energy, even people could cross over.\"", is_narrator=True)
    show_story_box("", "\"Theory only. Need stable anchor point. Materials list: rare isotopes, quantum stabilizer core (?), dimensional resonance crystal…(fake name lol). If I can stabilize the breach…\"", is_narrator=True)
    show_story_box("", "I skimmed faster—searching for the \"materials\" section.", is_narrator=True)

    # --- Scene 4: The Upperclassman ---
    show_story_box("", "Before I could finish—\nA massive hand snatched the notebook from my grip.", is_narrator=True)
    show_story_box("", "I looked up.\nTowering over me: a Heiwa student.", is_narrator=True)
    show_story_box("", "No, it wasn’t just any Heiwa thug.\nTall. Muscular. Built like a wall. Brown bob-cut hair. Sharp chin. Cold eyes. Old scars crisscrossing knuckles.", is_narrator=True)
    show_story_box("", "I knew him instantly.", is_narrator=True)
    show_story_box("", "As ‘Queen of Information’, I made it my business to know every major fighter across schools. Heiwa Seiritsu’s environment—“violence is king”—bred monsters. The ones who rose above the rest? They didn’t stay students long. Dropouts. Alumni. Legends among delinquents.", is_narrator=True)
    show_story_box("", "They called them “Upperclassmen”.", is_narrator=True)
    show_story_box("", "This one—\"Crusher\" Tetsuo—was infamous. Rumored to have caved in concrete walls with bare fists. Never lost a fight. Never stayed in school long enough to graduate.", is_narrator=True)
    
    boss_style = "red"
    show_story_box("Tetsuo", "This book got what we’re lookin’ for?", affiliation="Heiwa Seiritsu Upperclassman", color_override=boss_style)
    
    show_story_box("", "His voice was low. Gravelly.", is_narrator=True)
    show_story_box("", "I calculated escape routes—none viable. He was too close. Too fast.\nMy first instinct: run.\nNot good.", is_narrator=True)
    show_story_box("", "I twitched.\nHis fist crashed down—aimed straight for my face.", is_narrator=True)

    # --- Scene 5: The Rescue and Escape ---
    show_story_box("", "Then—\nCRASH!", is_narrator=True)
    show_story_box("", "Two bodies flew through the window—unconscious Heiwa goons—slamming into Tetsuo’s back. He staggered, if I can call it that.", is_narrator=True)
    show_story_box("", "Masayoshi landed between us—bokken already drawn.", is_narrator=True)
    show_story_box("", "Tetsuo recovered—threw another punch.\nMasayoshi parried.", is_narrator=True)
    show_story_box("", "CRACK!", is_narrator=True)
    show_story_box("", "The bokken snapped in half—a shockwave echoing through the hall.", is_narrator=True)
    show_story_box("", "Masayoshi didn’t hesitate. He scooped me up—princess carry again—and bolted.", is_narrator=True)
    show_story_box("Masayoshi", "We have no time to engage an elite foe.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    show_story_box("", "I clutched his shoulder—heart pounding.", is_narrator=True)
    show_story_box("Natsume", "H-He still has Kagaku’s diary..!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Masayoshi", "Let him keep it.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    show_story_box("", "He opened his closed fist—just enough for me to see.", is_narrator=True)
    show_story_box("", "Inside: a small, glowing shard.\nBlue. Pulsing faintly. Was it Kagaku’s \"anchor point?\"", is_narrator=True)
    show_story_box("Masayoshi", "I extracted the ‘end goal’ before they could.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    show_story_box("", "We ran.\nBehind us—Tetsuo’s eyes simply glared.\nBut we were already gone.", is_narrator=True)

def play_stage_2_7_start():
    # --- Scene 1: Kagaku's Explanation ---
    show_story_box("", "Akasuke’s POV", is_narrator=True)
    show_story_box("", "The earbud in Kagaku’s ear chimed—sharp, encrypted tone.", is_narrator=True)
    
    show_story_box("Kagaku", "Natsume? You’re—", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Natsume’s voice cut in—calm, but urgent.", is_narrator=True)
    show_story_box("Natsume", "Kagaku. Report—", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "But Kagaku spoke first—voice bubbling with excitement.", is_narrator=True)
    show_story_box("Kagaku", "YOU’RE NOT GONNA BELIEVE THIS!! I was running that ‘parallel universes’ experiment—y’know, the one with the resonance anchor? Infinite timelines, every possibility branching out, all that jazz—and something just happened! Like, actually, actually happened! The theory’s real! I mean, Naganohara literally—", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Akasuke", "Kagaku.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "My voice came out dull. Tired. Like I’d asked this question a thousand times before.", is_narrator=True)
    show_story_box("Akasuke", "Was this your doing?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Silence on the line.\nThen Kagaku laughed—nervous, cute, guilty.", is_narrator=True)
    show_story_box("Kagaku", "…Maybe? Teehee~!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Yuri’s eyes twitched.", is_narrator=True)
    show_story_box("Yuri", "Kagaku…", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Shigemura sighed.", is_narrator=True)
    show_story_box("Shigemura", "Of course.", affiliation="Kasakura High School Student")
    
    show_story_box("", "Benikawa just giggled.", is_narrator=True)
    
    show_story_box("", "But I didn’t explode. None of us did.\nWe were long used to her antics.", is_narrator=True)
    show_story_box("", "And—truthfully—she’d contributed more to research, tech, and our survival than almost anyone. One reckless experiment didn’t erase that.", is_narrator=True)
    
    show_story_box("Akasuke", "…Just tell us what you know.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Kagaku", "Okay, okay! Serious mode!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "She cleared her throat dramatically.", is_narrator=True)
    
    show_story_box("Kagaku", "Short version: there are infinite versions of us across infinite universes. Parallel timelines. Every choice, every possibility—exists somewhere. Personality and looks stay roughly the same, but “life stories” diverge wildly.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Akasuke", "With Naganohara.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Kagaku", "Exactly! For a moment, she swapped places with a version of herself from another universe. One where she was born in a different environment, enrolled in Heiwa Seiritsu instead of Kasakura, and became a delinquent badass because her fighting talent got nurtured that way.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Naganohara", "…So that was me? But… not me?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Kagaku", "Still you. Think of it like acting. You’re wearing a different ‘role’—different body, different skills, different memories—but inside? Same core. Same Naganohara. The ‘Heiwa girl’ you met in the infirmary? That was just the surface. The real you borrowed that form for a bit.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Akasuke", "How about the ‘knight’? What’s it got to do with this?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Kagaku", "I don’t know yet. But the biggest clue? He targeted our hearts, right? All eight of us. And right after, the blue light—the “crossover”’s energy—came from the wound where our hearts used to be.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "She paused.", is_narrator=True)
    
    show_story_box("Kagaku", "Alright! I’m calling it ‘Kokoro.’ Heart. Soul. Whatever you want. The knight took our Kokoro—our original hearts—from this universe. That should leave us in a ‘weakened, illegitimate Kata’—our base form without its anchor.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Kagaku", "Borrowing another universe’s Kokoro lets us temporarily wear a stronger ‘Kata’—like Naganohara’s Heiwa delinquent form. But it drains us. Fast. When the borrowed Kokoro runs out… we snap back. And every snap back hurts more. Weakens us more.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Akasuke", "If we don’t get them back…", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Kagaku", "…We die. Slowly. The body can’t sustain itself without its original Kokoro.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I thought of that tired woman’s voice.\n\"The path will not be easy.\"", is_narrator=True)
    
    show_story_box("Akasuke", "...We must find the ‘knight’.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Yuri", "And take back what’s ours.", affiliation="Kasakura High School Student / Seven Wonders")
    
    # --- Scene 2: Regrouping ---
    show_story_box("", "Natsume’s POV\n\nWe emerged from the main building—Masayoshi still carrying me.", is_narrator=True)
    
    show_story_box("", "The group spotted us—eyes wide.", is_narrator=True)
    
    show_story_box("Akasuke", "Natsume?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Natsume", "Long story. Kagaku.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I held up the glowing blue shard Masayoshi had extracted.", is_narrator=True)
    
    show_story_box("Natsume", "This. From your second lab.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Kagaku’s eyes lit up.", is_narrator=True)
    
    show_story_box("Kagaku", "That’s it! The resonance crystal—my anchor prototype!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "As Kagaku excitedly takes her glowing ‘anchor’, Yuri seems to be in thought while looking our way.", is_narrator=True)
    
    show_story_box("Yuri", "Huh? If ya had the long-distance communication thingy, why go outta ya way to leave the building?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Natsume", "...Heiwa didn’t take the bait. They ignored Akasuke’s charge at the front. Instead, they mobilized inward—coordinated. Strategic. That’s not their style.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Masayoshi", "Indeed. An “Upperclassman” was present. ‘Crusher’ Tetsuo. An elite enemy. He broke my bokken.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    show_story_box("Shigemura", "Prez Kageyama is still inside.", affiliation="Kasakura High School Student")
    
    show_story_box("Akasuke", "We go in. Now.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Naganohara", "Wait—", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "She wobbled.\nShigemura caught her again.", is_narrator=True)
    
    show_story_box("Shigemura", "...Infirmary first.", affiliation="Kasakura High School Student")
    
    show_story_box("Akasuke", "We’ll regroup. Then retake.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "We nodded.\nKasakura’s main building now waited—silent, surrounded, full of enemies.", is_narrator=True)
    
    show_story_box("", "And our Kokoro.\nWe weren’t leaving without it.", is_narrator=True)

def play_stage_2_7_end():
    # --- Scene 3: Kageyama and the Secretary ---
    show_story_box("", "Kageyama’s POV", is_narrator=True)
    show_story_box("", "The student council office on the top floor was silent except for the low hum of security monitors.", is_narrator=True)
    
    show_story_box("", "All council members had volunteered to leave—fighting downstairs, protecting the building, protecting me. I watched them go without protest. They were capable. Loyal. I am thankful for them.", is_narrator=True)
    
    show_story_box("", "But I had my own role. Even as President, I should get my hands dirty from time to time.", is_narrator=True)
    
    show_story_box("", "I stood. Adjusted my glasses. Left the room.", is_narrator=True)
    
    show_story_box("", "Hallways were dim—emergency lights only.", is_narrator=True)
    
    show_story_box("", "Then blood trails began on the third floor—small drops at first, then smears, then pools. The scent of iron grew stronger.", is_narrator=True)
    
    show_story_box("", "Fighting sounds echoed from below—grunts, impacts, bodies hitting walls.\n…No. Not fighting.\nOne-sided torture.", is_narrator=True)
    
    show_story_box("", "I walked toward it—calm. Steps measured. Observing.", is_narrator=True)
    
    show_story_box("", "I turned the corner.\nThat’s…", is_narrator=True)
    
    show_story_box("", "An Upperclassman of Heiwa Seiritsu stood in the center of the corridor.", is_narrator=True)
    
    show_story_box("", "Smaller build than the reported ‘Tetsuo’—lean, wiry—but wrapped head to toe in chains. Links coiled around fists, elbows, knees. Chains extended like living tendrils, binding fallen council members to the floor.", is_narrator=True)
    
    show_story_box("", "He struck—a chain-wrapped elbow slammed into a boy’s ribs. Crack. Blood sprayed. Another chain lashed out—wrapped a fleeing girl’s ankle, yanked her back, swung her into the wall. Thud. She didn’t get up.", is_narrator=True)
    
    show_story_box("", "It was brutal. Simple. Effective.", is_narrator=True)
    
    show_story_box("", "He noticed me.", is_narrator=True)
    
    boss_style = "red"
    show_story_box("Upperclassman", "President Kageyama.", affiliation="Heiwa Seiritsu Upperclassman", color_override=boss_style)
    
    show_story_box("", "He grinned—teeth red.", is_narrator=True)
    
    show_story_box("Upperclassman", "Why ain’t you helpin’ your precious underlings?", affiliation="Heiwa Seiritsu Upperclassman", color_override=boss_style)
    
    show_story_box("", "I tilted my head slightly.", is_narrator=True)
    
    show_story_box("Kageyama", "Believe me. I was scared.", affiliation="Kasakura High School Student Council President / Seven Wonders")
    
    show_story_box("", "He barked a laugh—loud, mocking.", is_narrator=True)
    
    show_story_box("Upperclassman", "Don’t fuck with me. You ain’t scared. Not even a little.", affiliation="Heiwa Seiritsu Upperclassman", color_override=boss_style)
    
    show_story_box("", "I smiled—small, polite.", is_narrator=True)
    
    show_story_box("Kageyama", "Given the situation. I’m going to run away now.", affiliation="Kasakura High School Student Council President / Seven Wonders")
    
    show_story_box("", "I turned, walked, then sped up.", is_narrator=True)
    
    show_story_box("", "He stared—confused—then furious.", is_narrator=True)
    
    show_story_box("Upperclassman", "Haaahhh?!! You little—!", affiliation="Heiwa Seiritsu Upperclassman", color_override=boss_style)
    
    show_story_box("", "He charged—chains rattling.\nI didn’t look back.\nFootsteps closed in—fast.", is_narrator=True)
    
    show_story_box("", "I have to do something.\n…But right before he reached me—", is_narrator=True)
    
    show_story_box("", "A hand flashed from the side.\nGrabbed his neck and slammed him down.\nThe floor cratered.", is_narrator=True)
    
    show_story_box("", "The Upperclassman went limp.", is_narrator=True)
    
    show_story_box("", "The new figure stood over him—short, long black hair with red streaks, glasses slightly askew. Expression calm. Professional.\n…Not good.", is_narrator=True)
    
    show_story_box("Kageyama", "Why are you here, Secretary Miyu?", affiliation="Kasakura High School Student Council President / Seven Wonders")
    
    show_story_box("", "She adjusted her glasses.", is_narrator=True)
    
    show_story_box("Secretary Miyu", "You’re late with your report on the latest incident.", affiliation="Kasakura High School Student Council")
    
    show_story_box("", "I smiled wider.", is_narrator=True)
    
    show_story_box("Kageyama", "I was running from a dangerous beastly gangster. Luckily, my reliable secretary came to help.", affiliation="Kasakura High School Student Council President / Seven Wonders")
    
    show_story_box("", "She didn’t smile back.", is_narrator=True)
    
    show_story_box("Secretary Miyu", "The ‘Boss’ is very interested in recent events. Hurry on the report.", affiliation="Kasakura High School Student Council")
    
    show_story_box("", "She stepped to the window.\nJumped.\nGone—without a trace.", is_narrator=True)
    
    show_story_box("", "I looked down at the unconscious Upperclassman.", is_narrator=True)
    
    show_story_box("Kageyama", "That was scary. Thought I was done for.", affiliation="Kasakura High School Student Council President / Seven Wonders")
    
    show_story_box("", "I continued walking.", is_narrator=True)

def play_stage_2_8_start():
    # --- Scene 1: Yuri's POV & The Hallway ---
    show_story_box("", "Yuri’s POV\n\nI didn’t get most of what Kagaku was yappin’ about earlier—parallel universes, Kokoro, Kata, borrowin’ other versions of ourselves… it all sounded like one of her mad-science rambles that always go way over my head.", is_narrator=True)
    show_story_box("", "But I understood the important part.\nWe had to take Kasakura back.\nAnd we had to save the President.", is_narrator=True)
    show_story_box("", "The ground floor was hell—more Heiwa fodder than I could count. We carved through them in waves. Akasuke leading with those fast, heavy strikes. Benikawa dancin’ around like it was a game. Shigemura coverin’ the back, quiet but precise. Naganohara and Kagaku stayin’ protected.", is_narrator=True)
    show_story_box("", "That ‘Tetsuo’ big one still hadn’t shown.", is_narrator=True)

    # --- Scene 2: The Cafeteria & Hana ---
    show_story_box("", "We reached the cafeteria.\nHana was there.", is_narrator=True)
    show_story_box("", "Surrounded by dozens of knocked-out Heiwa thugs—bodies piled like discarded trash. She stood over the last conscious one, nose bleeding, eyes half-lidded, barely clinging to awareness.", is_narrator=True)
    show_story_box("Hana", "Come on now. Just tell me what you were after, please! I promise I’ll be gentle.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "Her voice was soft. Kind. Like she was coaxing a scared first-year.", is_narrator=True)
    show_story_box("", "The thug coughed blood—then grinned weakly.", is_narrator=True)
    
    enemy_style = "red"
    show_story_box("Heiwa Thug", "You’re… really nice. And super beautiful…lady…", affiliation="Heiwa Seiritsu High School Student", color_override=enemy_style)
    
    show_story_box("", "Hana sighed—long, maiden-like.", is_narrator=True)
    show_story_box("Hana", "Oh, no…it was all useless banter.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "She dropped him. He hit the floor unconscious.\nThen she turned—saw us.", is_narrator=True)
    show_story_box("Hana", "Oh! Akasuke-kun! Inami-chan!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "She rushed over—eyes scanning us, worry creasing her brow.", is_narrator=True)
    show_story_box("Hana", "You’re all alive… Thank goodness.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "Her gaze landed on Naganohara—still slumped against Shigemura.", is_narrator=True)
    show_story_box("Hana", "Who…?", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Yuri", "Name’s Naganohara. A friend of ours. Long story.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Hana", "She needs the infirmary. I’ll take her.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "Shigemura nodded—shifted Naganohara’s weight to Hana.", is_narrator=True)
    show_story_box("Natsume", "My…wounds are at their limit too. I so need to lie down.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "She looked pale—sweat on her brow.", is_narrator=True)
    show_story_box("Akasuke", "Then Hana and Natsume guard the infirmary. The rest of us—me, Yuri, Benikawa, Masayoshi—push deeper. Save Kageyama.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "Kagaku stepped forward—then pulled the earbud from her ear and the blue jewel from her pocket.", is_narrator=True)
    show_story_box("Kagaku", "Take these.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "She pressed them into Akasuke’s hand.", is_narrator=True)
    show_story_box("Kagaku", "The earbud’s encrypted. Listen to my instructions. The jewel might also come in useful.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Akasuke", "…Got it.", affiliation="Kasakura High School Student / Seven Wonders")

    # --- Scene 3: Separation ---
    show_story_box("", "We separated.", is_narrator=True)
    show_story_box("", "Hana and Natsume headed toward the infirmary with Naganohara.", is_narrator=True)
    show_story_box("", "We turned deeper into the building.", is_narrator=True)

def play_stage_2_8_end():
    # --- Scene 4: Masayoshi's Stand ---
    show_story_box("", "Masayoshi’s POV\n\nI stayed at the rear as we climbed.", is_narrator=True)
    show_story_box("", "Akasuke, Yuri, Benikawa—ambitious. Strong minds. Even after the “Kokoro”’s theft, the ‘knight’, the ‘Kata’ explanations—they pressed forward without faltering.", is_narrator=True)
    show_story_box("", "Admirable.", is_narrator=True)
    show_story_box("", "The stairs were littered with weaklings—unconscious or groaning. I cleared stragglers with minimal effort. Bokken strikes to vital points. Efficient and clean like routine.", is_narrator=True)
    show_story_box("", "Then—I felt it.\nPresence.\nHeavy. Controlled. Watching.", is_narrator=True)
    show_story_box("", "Tetsuo, huh?", is_thought=True)
    show_story_box("", "I stopped.", is_narrator=True)
    show_story_box("Masayoshi", "Go on without me.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    show_story_box("Akasuke", "Masayoshi-senpai?", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Masayoshi", "I will clear the ‘fodder’ here. You three should hurry to the President.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    show_story_box("", "They hesitated—then nodded.", is_narrator=True)
    show_story_box("Akasuke", "Be careful.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "They continued upward.\nI turned.", is_narrator=True)
    
    # --- Scene 5: The Duel ---
    show_story_box("", "Tetsuo stepped from the shadows—calm, unreadable.", is_narrator=True)
    
    boss_style = "red"
    show_story_box("Tetsuo", "...The one who ran.", affiliation="Heiwa Seiritsu Upperclassman", color_override=boss_style)
    
    show_story_box("", "I drew a new bokken—spare from my belt.", is_narrator=True)
    show_story_box("Masayoshi", "I did not run. I retreated strategically.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    show_story_box("", "He cracked his knuckles.", is_narrator=True)
    show_story_box("Tetsuo", "Same thing.", affiliation="Heiwa Seiritsu Upperclassman", color_override=boss_style)
    show_story_box("", "I settled into a stance.", is_narrator=True)
    show_story_box("Masayoshi", "Let us settle this.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    show_story_box("", "He charged.", is_narrator=True)
    show_story_box("", "I met him.", is_narrator=True)
    show_story_box("", "Bokken and fists collided—shockwave echoing through the stairwell.", is_narrator=True)

def play_stage_2_9_start():
    # --- Scene 1: The Angry Chain User ---
    show_story_box("", "Yuri’s POV", is_narrator=True)
    show_story_box("", "We reached the hallway where the crater was.", is_narrator=True)
    show_story_box("", "Chains everywhere—coiled around unconscious student council members, draped across broken lockers. There was a bloodied crater meters away from the scene.", is_narrator=True)
    show_story_box("", "Someone stood in the center—chains rattling softly, eyes burning with rage.", is_narrator=True)
    
    boss_style = "red"
    show_story_box("Upperclassman", "WHO THE HELL TOOK ME OUT LIKE THAT?!", affiliation="Heiwa Seiritsu Upperclassman", color_override=boss_style)
    
    show_story_box("", "He roared—voice echoing down the corridor.", is_narrator=True)
    
    show_story_box("Akasuke", "This one’s bad news.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Yuri", "No choice. We gotta go through him.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Benikawa", "Even injured, he’s dangerous, like a cornered animal~.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "The Upperclassman locked eyes on us.", is_narrator=True)
    
    show_story_box("Upperclassman", "You three…Kasakura’s Wonders..! Perfect. I’ll crush you and prove I ain’t some weakling who gets dropped by one hit!", affiliation="Heiwa Seiritsu Upperclassman", color_override=boss_style)
    
    show_story_box("", "Chains whipped out—fast, brutal.\nWe met him head-on.", is_narrator=True)

def play_stage_2_9_end():
    # --- Scene 2: Masayoshi vs. Tetsuo ---
    show_story_box("", "Masayoshi’s POV", is_narrator=True)
    
    boss_style = "red"    
    show_story_box("", "I settled into a stance.", is_narrator=True)
    show_story_box("Masayoshi", "Let us settle this.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    show_story_box("", "He charged.\nI met him.", is_narrator=True)
    show_story_box("", "Bokken and chains collided—shockwave echoing through the stairwell.", is_narrator=True)
    show_story_box("", "He punched—fast. I parried.\nCRACK!", is_narrator=True)
    show_story_box("", "The bokken snapped again.", is_narrator=True)
    
    show_story_box("", "I drew another—prepared this time.\nForget parrying.", is_narrator=True)
    show_story_box("", "Dodged the next strike. Slipped inside his guard. Clean strike—jugular.\nCRACK!", is_narrator=True)
    show_story_box("", "The bokken shattered on impact. No significant damage.\nSurprise flickered through me.", is_narrator=True)
    
    show_story_box("", "No time to react.", is_narrator=True)
    show_story_box("", "His fist connected—side of my ribs.\nMassive force. I flew—crashed through a wall. Plaster rained. Pain exploded across my torso.", is_narrator=True)
    
    show_story_box("Tetsuo", "Weapon users are weak. Rely on your little toys to fight. Lose the toy…", affiliation="Heiwa Seiritsu Upperclassman", color_override=boss_style)
    show_story_box("", "He cracked his neck.", is_narrator=True)
    show_story_box("Tetsuo", "…and you’re nothing.", affiliation="Heiwa Seiritsu Upperclassman", color_override=boss_style)
    
    show_story_box("", "I rose—slowly.", is_narrator=True)
    show_story_box("Masayoshi", "By that standard…", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    show_story_box("", "I met his eyes.", is_narrator=True)
    show_story_box("Masayoshi", "…everyone is a weapon user.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    show_story_box("", "Tetsuo blinked—confused.\nThen furious.", is_narrator=True)
    
    show_story_box("Tetsuo", "Little disciplinary rat. You can still stand and talk back?", affiliation="Heiwa Seiritsu Upperclassman", color_override=boss_style)
    
    show_story_box("", "He threw a punch.\nI caught it—bare-handed.\nTwisted.", is_narrator=True)
    show_story_box("", "Then the arm snapped.", is_narrator=True)
    
    show_story_box("", "Tetsuo grunted—then threw another.\nI dodged—grazed my shoulder, but a sharp pain flared.", is_narrator=True)
    show_story_box("", "I countered—bare-handed now. Strikes to joints. Pressure points. Precise. Controlled.", is_narrator=True)
    show_story_box("", "CRACK!\nHis other arm finally broke.", is_narrator=True)
    
    show_story_box("Tetsuo", "You bastard—!", affiliation="Heiwa Seiritsu Upperclassman", color_override=boss_style)
    show_story_box("", "He rushed—rage overtaking reason.", is_narrator=True)
    
    show_story_box("", "I picked up a broken bokken shard.\nJabbed—straight into his eye.", is_narrator=True)
    show_story_box("", "Blind.\nHe screamed.", is_narrator=True)
    show_story_box("", "I slipped behind—arm around his neck.\nChokehold.", is_narrator=True)
    
    show_story_box("Masayoshi", "Now that you have lost your weapon…", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    show_story_box("", "I tightened.", is_narrator=True)
    
    # Name change for emphasis as per script
    show_story_box("Masayoshi Kouhei", "…your body—sight, limbs—you should be nothing.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    show_story_box("", "He struggled—then went limp.\nUnconscious.", is_narrator=True)
    show_story_box("", "I released him.\nStood over the body.", is_narrator=True)
    
    show_story_box("Masayoshi", "…Well fought.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    show_story_box("", "I turned.\nThe President waited.", is_narrator=True)

def play_stage_2_10_start():
    # --- Scene 1: The Chain Reaper ---
    show_story_box("", "Akasuke’s POV", is_narrator=True)
    show_story_box("", "The hallway was narrow—chains rattling, metal scraping concrete, air thick with sweat and blood.", is_narrator=True)
    show_story_box("", "The Upperclassman stood at the far end—chains coiled around his arms, torso, legs—like living armor. Eyes wild. Breath heavy.", is_narrator=True)
    
    boss_style = "red"
    show_story_box("Upperclassman", "I’M LITERALLY KUROGANE! ‘CHAIN REAPER OF HEIWA’!", affiliation="Heiwa Seiritsu Upperclassman", color_override=boss_style)
    
    show_story_box("", "He roared—voice echoing off the lockers.", is_narrator=True)
    
    show_story_box("Kurogane", "You think some lucky shot takes me out?! I’M UNBREAKABLE! YOU SHOULD ALL FEAR ME!", affiliation="Heiwa Seiritsu Upperclassman", color_override=boss_style)
    
    show_story_box("", "We didn’t respond.\nCouldn’t.\nEvery ounce of focus was put on surviving.", is_narrator=True)
    
    show_story_box("", "Chains whipped out—three at once. One toward my head, one low at my legs, one arcing toward Yuri.", is_narrator=True)
    
    show_story_box("", "I ducked the high strike—felt the wind of it. Sidestepped the low sweep. Blocked the third with my forearm—chain wrapped tight, links biting skin. Pain flared.", is_narrator=True)
    
    show_story_box("", "Yuri dodged left—chain grazed her shoulder, tore fabric. She hissed, rolled, and came up swinging.", is_narrator=True)
    
    show_story_box("", "Benikawa blurred right—Ryuusei Ken snapping out, shattering one chain link. But another wrapped her ankle—yanked. She twisted mid-air, landed on one foot, Kagerou Geri kicking the chain away.", is_narrator=True)
    
    show_story_box("", "We couldn’t get any closer.\nHe laughed.", is_narrator=True)
    
    show_story_box("Kurogane", "THREE ON ONE AND YOU’RE STILL STRUGGLING?!", affiliation="Heiwa Seiritsu Upperclassman", color_override=boss_style)
    
    show_story_box("", "He was right.\nEven injured—arm bandaged, ribs taped—he held the advantage.", is_narrator=True)
    show_story_box("", "Chains everywhere. Extending reach. Binding. Whipping. No blind spots. No openings.", is_narrator=True)
    
    show_story_box("Akasuke", "…Explains the council members on the ground.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "They were scattered—bloodied, unconscious. Office workers. Errand-runners. Document handlers. Not frontline fighters.", is_narrator=True)
    show_story_box("", "Not made for monsters like this.\nI pitied them.\nAnd I admired them.\nThey’d fought anyway.", is_narrator=True)
    
    show_story_box("", "Chains lashed again—toward my chest.\nI blocked—barely. Links went a bit deeper.", is_narrator=True)
    
    # --- Scene 2: The Earbud and the Kata ---
    show_story_box("", "Then—the earbud chimed.", is_narrator=True)
    
    show_story_box("Kagaku", "Akasuke! Situation?", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Akasuke", "We’re engaging an Upperclassman. He uses chains. We’re…struggling.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Kagaku", "Perfect timing. Use the jewel, then!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Akasuke", "Now?", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Kagaku", "Yes! Borrow a Kata! Hold it to your chest—think of your duties, what you fight for. Picture the ‘knight’. You’ll picture beating the hell out of him, right?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I pulled the blue jewel from my pocket—small, glowing, warm.\nPressed it to my chest.", is_narrator=True)
    show_story_box("", "I closed my eyes.", is_narrator=True)
    show_story_box("", "Duty. Friends. Yuri. Kurona. Kasakura. The President.", is_narrator=True)
    show_story_box("", "The knight—cold armor, chipped blade, piercing my heart.\nI will beat the hell out of him.", is_narrator=True)
    
    show_story_box("", "Blue light erupted—from my chest. Covered me. Warm. Electric.\nThen—dissipated.", is_narrator=True)
    show_story_box("", "I opened my eyes.", is_narrator=True)
    
    show_story_box("", "New uniform—Heiwa style. Untucked shirt, loose tie. Hair restyled.\nSame as Kuroda’s, huh?\nThat ‘Iron Fist of Heiwa’ from the battle at the front yard.", is_narrator=True)
    
    show_story_box("Yuri", "…Akasuke?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Benikawa", "That’s…that dude…Kuroda’s look. The one from the yard.", affiliation="Benikawa Ninja Clan")
    show_story_box("", "She frowned.", is_narrator=True)
    show_story_box("Benikawa", "Um, he wasn’t even an Upperclassman. You should even be stronger than him.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Akasuke", "...It’s fine.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "I flexed my hands—felt the difference. Strength. Speed. But more—instincts.", is_narrator=True)
    show_story_box("Akasuke", "I can take his techniques… combine them with mine.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "The Upperclassman stared—confused, then furious.", is_narrator=True)
    
    show_story_box("Upperclassman", "What the hell are y’all doing now? You ‘mocking me?!", affiliation="Heiwa Seiritsu Upperclassman", color_override=boss_style)
    
    show_story_box("", "He charged—chains whipping.", is_narrator=True)
    show_story_box("", "I moved. We moved.\nFaster.", is_narrator=True)

def play_stage_2_10_end():
    # --- Scene 3: The Beatdown ---
    show_story_box("", "His first chain—high lash—I slipped under it. Kuroda’s rapid jabs flowed through me—left, right, left, right—fists blurring, hitting ribs, solar plexus, collarbone. Each strike precise—Kuroda’s childish spam turned lethal by my karate foundation.", is_narrator=True)
    
    show_story_box("", "He staggered.", is_narrator=True)
    
    show_story_box("", "Chains lashed—desperate.", is_narrator=True)
    
    show_story_box("", "I caught one—twisted—yanked him forward. Knee to gut, then add elbow to jaw. Would’ve never thought of that without all the time ‘he’ spent fighting on the streets.", is_narrator=True)
    
    show_story_box("", "He flew back—crashed into lockers.\nDidn’t get up.", is_narrator=True)
    
    show_story_box("Akasuke", "…Clear.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Yuri exhaled.", is_narrator=True)
    show_story_box("Yuri", "That was… insane.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Benikawa", "You okay?", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "I nodded—feeling the drain already. Chest ached. Vision blurred at the edges.", is_narrator=True)
    
    show_story_box("Akasuke", "Let’s keep moving. President’s waiting.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "We ran.\nTop floor.\nKageyama.", is_narrator=True)

def play_stage_2_11_story():
    # --- Scene 1: The Aftermath and Kageyama ---
    show_story_box("", "Masayoshi’s POV\n\nThe last Heiwa thug hit the floor—chains clattered uselessly around his broken body.", is_narrator=True)
    show_story_box("", "Cleanup was swift after that.\nThe remaining delinquents either fled or surrendered the moment word spread their Upperclassmen were down. The Disciplinary Committee rounded them up. The school fell quiet.", is_narrator=True)
    
    show_story_box("", "I found Kageyama not in the council office…but in the file archives room—surrounded by scattered folders, monitors flickering with information.", is_narrator=True)
    
    show_story_box("Masayoshi", "President. Why are you here?", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    show_story_box("Kageyama", "The council office is too obvious a target. Here, I blend with the background. Safer.", affiliation="Kasakura High School Student Council President / Seven Wonders")
    
    show_story_box("", "His tone was calm. Calculating. As always.", is_narrator=True)
    
    show_story_box("Masayoshi", "...You should have remained fortified.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    show_story_box("Kageyama", "And miss the chance to observe their movements firsthand? Unacceptable for my position. I had to do something.", affiliation="Kasakura High School Student Council President / Seven Wonders")
    
    show_story_box("", "Before I could press further, footsteps echoed—Akasuke’s group arrived.", is_narrator=True)
    
    show_story_box("Akasuke", "President!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Yuri", "You’re safe!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "It must have been nothing.", is_thought=True)
    
    show_story_box("", "We regrouped. Cleaned. Repaired what we could.\nBy evening, Kasakura stood once more.", is_narrator=True)
    
    # --- Scene 2: The Missing Diary ---
    show_story_box("", "Disciplinary Committee temporary office", is_narrator=True)
    show_story_box("", "The room was quiet—save for the scratch of my pen against report forms.\nStacks of papers: injury logs, arrest tallies, property damage assessments. Routine. Necessary.", is_narrator=True)
    
    show_story_box("", "The door slid open.\nYokubukai Natsume entered first—limping slightly, bandages visible under her uniform, but she looked much better than last time. Kagaku Shamiko followed, eyes bright despite the eyebags, clutching a half-eaten melon bread.", is_narrator=True)
    
    show_story_box("Kagaku", "Masayoshi-senpai! We’re here for my diary!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Right. The diary.\nI set the pen down.", is_narrator=True)
    
    show_story_box("Masayoshi Kouhei", "I forgot to tell you. Tetsuo did not have it when I apprehended him.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    show_story_box("", "Natsume froze mid-step.", is_narrator=True)
    show_story_box("Natsume", "Ehh…This might be worse than we think.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Her voice was low. Calculating.", is_narrator=True)
    
    show_story_box("Natsume", "Heiwa raided files, labs, archives over the last few days. If Kagaku’s diary fell into their hands…", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Kagaku", "Ahh, yeah! My diary has everything! Parallel universe theories, notes explaining what would be the Kokoro and Kata, resonance crystal specs—", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "She trailed off, eyes wide.", is_narrator=True)
    show_story_box("Kagaku", "They have it.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I folded my hands.", is_narrator=True)
    show_story_box("Masayoshi", "Indeed. The orchestrator behind Heiwa’s strategic movements during the battle must possess it now.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    show_story_box("", "I leaned back slightly.", is_narrator=True)
    show_story_box("Masayoshi", "They came not just for dominance. They came for the power of the Katas.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    show_story_box("", "Natsume’s eyes narrowed.", is_narrator=True)
    show_story_box("Natsume", "Then we assume they know everything Kagaku documented.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Masayoshi", "Then we proceed carefully. The enemy holds information, but we hold the means to use and counter it.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    show_story_box("", "Natsume exhaled.", is_narrator=True)
    show_story_box("Natsume", "We’ll need to accelerate the research. And prepare for retaliation.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Kagaku", "Already on it!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "She grinned—wild, determined.", is_narrator=True)
    show_story_box("Kagaku", "Let’s get our Kokoro back! And make them regret ever touching my diary!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I returned to the reports.", is_narrator=True)
    show_story_box("Masayoshi Kouhei", "Agreed.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    # --- Scene 3: The Parallaxis Scorer ---
    show_story_box("", "A Few Days Later – Kagaku’s Lab\n\nAkasuke’s POV", is_narrator=True)
    
    show_story_box("", "The eight of us—those who lost our Kokoro—gathered in Kagaku’s second lab. Masayoshi and Kageyama stood at the back, observing.", is_narrator=True)
    show_story_box("", "Kagaku hadn’t slept. Eyebags deep. Hair wild. Empty melon bread wrappers and coffee cans everywhere.", is_narrator=True)
    show_story_box("", "Yet her eyes burned with pure, manic passion.", is_narrator=True)
    
    show_story_box("Kagaku", "Behold!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "She gestured dramatically to the machine in the center—a towering contraption of wires, crystals, glowing panels. The “Parallaxis Scorer”.", is_narrator=True)
    
    show_story_box("Kagaku", "Theoretically finds, defines, and attunes us to our possible Katas. It lets us borrow them at will! In battle. Anytime!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Akasuke", "How does it work? Oh, and explain simply.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Kagaku", "Stand on the platform. I insert a specially made Microchip. The machine scans. Extracts, and attunes your Kata.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "She held up a small chip—glowing faintly.", is_narrator=True)
    
    show_story_box("", "Shigemura stepped forward—hands still in pockets, expression neutral.", is_narrator=True)
    show_story_box("Shigemura", "I’ll go first.", affiliation="Kasakura High School Student")
    
    show_story_box("", "Silence.", is_narrator=True)
    show_story_box("Yuri", "Shigemura…?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "He didn’t look at Naganohara.", is_narrator=True)
    show_story_box("Shigemura", "Couldn’t really protect her last time.", affiliation="Kasakura High School Student")
    
    show_story_box("", "His voice was quiet. Almost embarrassed.\nOnly I and Yuri caught the flush on his ears.", is_narrator=True)
    
    show_story_box("Kagaku", "Oh! A Volunteer! Perfect, perfect!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "She grinned and inserted the Microchip.\nThe machine whirred.", is_narrator=True)
    
    show_story_box("Kagaku", "Oh, yeah! Everyone, you should close your eyes! It’s bright!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Shigemura", "Wha—", affiliation="Kasakura High School Student")
    
    show_story_box("", "Blue light exploded—blinding, searing.\nFilling the whole lab and leaking outwards like a bomb had gone off.", is_narrator=True)
    
    # --- Scene 4: The Transformation ---
    show_story_box("", "When it faded…\nShigemura stood, transformed.", is_narrator=True)
    
    show_story_box("", "Old, tattered Heiwa Seiritsu uniform—a very late edition. Chains wrapped around knees, elbows, and torso, then more coiled in his pockets where his hands now rested.", is_narrator=True)
    
    show_story_box("", "Kurogane’s Kata.\n‘The Chain Reaper’ we fought.", is_narrator=True)
    
    show_story_box("", "Kagaku reached for the Microchip, but yanked back instantly.", is_narrator=True)
    show_story_box("Kagaku", "Owwie! Hot!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "The chip was charred—burned to crisp.", is_narrator=True)
    
    show_story_box("Akasuke", "So… we can properly borrow Katas now.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Kagaku", "Exactly! And the stronger the enemy we defeat… the stronger the Kata we can claim! I believe it always has to do with our current situation, as if meeting the person increases the chances of that other universe’s self meeting us!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "She spun—eyes manic.", is_narrator=True)
    
    show_story_box("Natsume", "More enemies will come. They want this power. Then the knight for sure. The ones behind Heiwa’s latest coordinated raid. They’ll keep coming.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Akasuke", "Then we get stronger.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Akasuke", "We master these Katas. We fund Kagaku’s research. We build the Scorer with…materials. And we take back our Kokoro.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Yuri", "And we beat the hell out of the knight, right?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Kagaku", "That’s the spirit!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "She pumped her fist—then remembered something.", is_narrator=True)
    
    show_story_box("Kagaku", "Oh! And forget the diary, if you think we can’t keep working that way. Everything important is…", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "She tapped her temple.", is_narrator=True)
    show_story_box("Kagaku", "…right here~. I’m a genius, after all!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I smiled—small, determined.", is_narrator=True)
    show_story_box("Akasuke", "Then let’s get to work.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "The war had only just begun.", is_narrator=True)

def play_stage_3_1_story():
    # --- SCENE 1: HEIWA SEIRITSU GANG ---
    show_story_box("", "Heiwa Seiritsu Gang – Dark Alleyway\nThe narrow alley stank of rust, garbage, and dried blood.", is_narrator=True)
    show_story_box("", "Four Heiwa delinquents huddled against the wall—bruised, bandaged, uniforms torn. One leaned on a dented pipe for support. Another nursed a swollen eye. Cigarette smoke curled lazily upward.", is_narrator=True)

    show_story_box("Gang Member 1", "Man… it’s over. Even our own school’s probably sweepin’ up the leftovers now. Kasakura and Heiwa workin’ together? Never thought I’d see the day.", affiliation="Heiwa Seiritsu High School Student")
    show_story_box("Gang Member 2", "Yeah. Authorities are out. Students too. We’re the last idiots still runnin’.", affiliation="Heiwa Seiritsu High School Student")
    
    show_story_box("Gang Member 3", "This is bullshit! Why the hell did we have to play it slow and smart?! We could’ve just rushed in like always—overwhelmed ‘em with numbers and power! We’d have won by now!", affiliation="Heiwa Seiritsu High School Student")
    show_story_box("", "He slammed his fist into the brick—cracking it slightly.", is_narrator=True)
    show_story_box("Gang Member 3", "Who the fuck convinced the Upperclassmen to listen to strategy anyway? Those guys live for raw strength! They don’t do plans! Someone’s pullin’ strings—and it ain’t one of us.", affiliation="Heiwa Seiritsu High School Student")
    
    show_story_box("Gang Member 4", "…I heard about somethin’.", affiliation="Heiwa Seiritsu High School Student")
    show_story_box("", "The others turned.", is_narrator=True)
    show_story_box("Gang Member 4", "Word from the guys who got close to the brass. The Upperclassmen were told about some ‘tech’ or ‘item’ in Kasakura. Said if they extract it properly, they’d get power beyond anything we’ve ever seen. Unfathomable shit.", affiliation="Heiwa Seiritsu High School Student")
    
    show_story_box("", "Silence.", is_narrator=True)
    
    show_story_box("Gang Member 1", "No way. The Upperclassmen trustin’ some random stranger? Throwin’ away their pride for a promise? Sounds like nothin’ but a scam.", affiliation="Heiwa Seiritsu High School Student")
    show_story_box("Gang Member 4", "Maybe. But you know how Heiwa works. Power is king.", affiliation="Heiwa Seiritsu High School Student")
    show_story_box("Gang Member 4", "If someone’s stronger than the Upperclassmen—strong enough to maybe even force ‘em, not just convince ‘em…then, yeah. They’d follow…", affiliation="Heiwa Seiritsu High School Student")
    
    show_story_box("Gang Member 3", "Someone stronger than Tetsuo-san? “Crusher”? “Chain Reaper”? ‘You serious?", affiliation="Heiwa Seiritsu High School Student")
    show_story_box("Gang Member 4", "We’re stupid, sure. But I’m not blind. If someone out there can make legends kneel…we never stood a chance.", affiliation="Heiwa Seiritsu High School Student")
    
    show_story_box("", "A boot scraped concrete.\nThey froze.", is_narrator=True)
    show_story_box("", "Kasakura Disciplinary Committee members flooded the alley from both ends—uniforms crisp, bokken raised, eyes hard.\nRapid motion and authoritative shouting.\nBokken swung. Bodies dropped. Chains clattered uselessly.", is_narrator=True)
    
    show_story_box("Gang Member 1", "GAAHHH!!", affiliation="Heiwa Seiritsu High School Student")
    
    show_story_box("", "In seconds, the last remnants were down.\nThe alley fell silent again.", is_narrator=True)

    # --- SCENE 2: KAGAKU'S LAB ---
    show_story_box("", "********* ◆ *********\nKagaku’s POV", is_narrator=True)
    
    show_story_box("", "The lab lights buzzed softly overhead—familiar, comforting, almost like white noise after sixteen straight hours of work.", is_narrator=True)
    show_story_box("", "I blinked hard. Neck stiff. Eyes dry. The Parallaxis Scorer prototype sat in the center of the room, wires neatly coiled, crystal array still faintly glowing blue from the last test run.", is_narrator=True)
    show_story_box("", "Tools scattered across the workbench: soldering iron, multimeter, half-empty coffee cans (two of them), and crumpled melon bread wrappers.", is_narrator=True)
    show_story_box("", "I rubbed my face and stood. Legs wobbly.", is_narrator=True)
    
    show_story_box("Kagaku", "Coffee…more coffee…then maybe sleep…or not. Probably not…", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I gathered the empty cans—two in one hand, one in the other—and shuffled toward the door. The campus should be empty by now. Nighttime. Quiet. Perfect for thinking.", is_narrator=True)
    show_story_box("", "The hallway outside was dim—only emergency lights. I headed for the nearest vending machine, humming absentmindedly.\nThen I heard voices.", is_narrator=True)
    show_story_box("", "Low. Formal. Measured.\nI peeked around the corner.", is_narrator=True)
    
    show_story_box("Kagaku", "Oh..?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Masayoshi Kouhei stood in the corridor with three other Disciplinary Committee members—two boys, one girl—all in uniform, arms crossed, listening as he gave quiet instructions.\nI stepped out.", is_narrator=True)
    
    show_story_box("Kagaku", "Masayoshi-senpai..! Still here?...You guys haven’t gotten anything out of the Heiwa dudes yet?", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "They turned.", is_narrator=True)
    
    show_story_box("Masayoshi", "Kagaku. We have interrogated them thoroughly.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    show_story_box("Kagaku", "And…?", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Masayoshi", "They know nothing. They were low-level pawns, after all. Expendable. They were given orders and nothing more.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    show_story_box("", "I sighed.", is_narrator=True)
    show_story_box("Kagaku", "Figures. What about the Upperclassmen? Tetsuo? Kurogane?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Masayoshi", "Tetsuo revealed only this: your diary was handed over to ‘Heiwa’s larger connections’ shortly after our first encounter.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    show_story_box("Masayoshi", "By the time I returned for the rematch, it was gone. He claimed tracing it now is nearly impossible—the network is too complex.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    show_story_box("", "I stopped walking.", is_narrator=True)
    show_story_box("Kagaku", "…Ahh, yeah. The ‘Larger connections.’", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "We reached the vending machine together. I fed coins in. Pressed the button. A coffee can clunked down.", is_narrator=True)
    show_story_box("Kagaku", "I know a little about that term…‘Heiwa Seiritsu’s Connections’ isn’t just “random ex-thugs scattered across the city”. It’s…actually organized. Controlled. They call it the ‘Big Picture.’", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Masayoshi tilted his head slightly—listening.", is_narrator=True)
    show_story_box("Kagaku", "Correct me if I’m wrong, but… Heiwa’s delinquent world isn’t actually chaos. It’s a system. Every lowlife, mid-tier fighter, Upperclassman—they’re all part of one massive structure.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Kagaku", "And…at the very top…is a myth barely whispered about. “The Alumnae”. Female ex-students, former Upperclasswomen. Even higher rank than the usual Upperclassmen.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Kagaku", "They’re the core. The ones holding the entire machine together. Never seen any reports that confirm their existence, though…", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I yawned.", is_narrator=True)
    show_story_box("Masayoshi", "You are… remarkably accurate.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    show_story_box("Kagaku", "I try~.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I took a sip. Hot. Bitter. Perfect.", is_narrator=True)
    show_story_box("Kagaku", "So if the diary’s with them… with those…Alumnae… that’s bad. Really bad. They don’t just want to trash Kasakura. It’s probably them that want the Katas. The power. And now they have my notes, too.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Masayoshi", "Indeed. The strategic precision of their raid was no accident. Someone—or something—far above the Upperclassmen orchestrated it.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    show_story_box("", "We stood in silence for a moment. The vending machine hummed behind us.", is_narrator=True)
    show_story_box("Masayoshi", "Get some rest, Kagaku. You’ve done enough today.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    show_story_box("Kagaku", "You too, senpai. Don’t stay up writing reports all night.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "He gave the smallest nod.\nI turned back toward the lab—cans in hand, mind racing.", is_narrator=True)
    show_story_box("", "The door slid shut behind me.\nI set the fresh coffee on the desk…but didn’t open it.", is_narrator=True)
    show_story_box("", "Just… collapsed forward. Forehead on cool metal. Eyes closed.\nSleep hit instantly.\n…", is_narrator=True)
    
    # --- SCENE 3: THE KIDNAPPING ---
    show_story_box("", "Then—\nA hand clamped over my mouth.", is_narrator=True)
    show_story_box("Kagaku", "!!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Strong. Fast.\nI jolted—too late.", is_narrator=True)
    show_story_box("", "Another arm wrapped around my waist and pulled.\nThe window was long opened without me noticing.", is_narrator=True)
    show_story_box("", "Cold night air rushed in. Darkness swallowed me.\nI was gone.", is_narrator=True)

def play_stage_3_2_story():
    # --- SCENE 1: KASAKURA LAB INVESTIGATION ---
    show_story_box("", "********* ◆ *********\nAkasuke’s POV", is_narrator=True)
    show_story_box("", "Kasakura High School – Next Day\nThe lab looked pristine, aside from the tools scattered and papers thrown on the ground.", is_narrator=True)
    show_story_box("", "There was no blood nor signs of struggle, only vending machine coffee stains and their cans lay crushed in the corner.", is_narrator=True)
    show_story_box("", "The Parallaxis Scorer stood untouched—its crystal array still faintly pulsing blue—but the back window was open to the entire night.", is_narrator=True)
    show_story_box("", "The Seven Wonders of Kasakura—plus Benikawa, Shigemura, Naganohara, and the rest of us who’d lost our Kokoro—stood in tense silence around the scene.", is_narrator=True)
    
    show_story_box("", "Masayoshi-senpai bowed his head slightly.", is_narrator=True)
    show_story_box("Masayoshi", "I failed to notice the intrusion. I must apologize.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    show_story_box("", "Before anyone could respond, his phone buzzed—sharp, insistent.\nHe answered immediately.", is_narrator=True)
    show_story_box("Masayoshi", "...President.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    show_story_box("", "Kageyama’s voice crackled through—calm, clipped.", is_narrator=True)
    show_story_box("Kageyama", "Masayoshi. Come to the interrogation office. Where Tetsuo is.", affiliation="Kasakura High School Student Council President / Seven Wonders")
    show_story_box("Masayoshi", "Understood.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    show_story_box("", "He lowered the phone. Turned to us.", is_narrator=True)
    show_story_box("Masayoshi", "Pardon me. I must attend to this.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    show_story_box("", "He left—quick, purposeful steps echoing down the hall.\nWe stayed.", is_narrator=True)
    
    show_story_box("Akasuke", "Let the Committee and Natsume handle the scene. We need to figure out what happened.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Yuri", "Obvious first suspect: Heiwa Seiritsu.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Akasuke", "At first glance, yeah. But think about it. Heiwa’s hotheaded and reckless. They can’t do stealth kidnappings in literal enemy territory without leaving a mess. This was clean. Silent. No alarms. No witnesses.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Yuri", "So…maybe the same person who orchestrated the raid?", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Akasuke", "Exactly. Whoever’s pulling Heiwa’s strings now—they’re smart. Resourceful. They banded a chaotic school together for the first time. That takes real influence.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Naganohara", "Hmm…Could it be someone else targeting Kasakura? Not just Heiwa?", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Shigemura", "That’s possible. Kasakura’s had beef with two schools before. Heiwa Seiritsu we know. The other was Kiryoku Gakuen.", affiliation="Kasakura High School Student")
    show_story_box("Yuri", "Kiryoku? The girls-only school?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Shigemura", "Yeah. Most people think “girls school” means elegant, refined. But that’s wrong. Kiryoku’s students are athletic, competitive, battle-hungry, sporty—barely elegant.", affiliation="Kasakura High School Student")
    show_story_box("Shigemura", "Almost like Heiwa Seiritsu but all girls. But don’t say that in front of one. They’re still mostly kind, compassionate people. Just… very strong. And very proud. Comparing them to delinquents is a good way to get thrown through a wall.", affiliation="Kasakura High School Student")
    
    show_story_box("Akasuke", "So what’s the motive? Kagaku’s kidnapping has to be about the ‘Kata’s. They want the power. They’d hide her location—no hostage situation for sure. No demands, just extraction of information from her.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Yuri", "...Then we’re stuck. No leads. No idea where she is.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Naganohara", "...We’ll find her. We have to!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "We stood in silence—thinking, planning, grasping at nothing.", is_narrator=True)

    # --- SCENE 2: UNKNOWN LOCATION (DESERT/JUNGLE) ---
    show_story_box("", "Unknown Location – Yesterday Night\nSand crunched under boots.", is_narrator=True)
    show_story_box("", "A lone tent stood in the middle of nowhere—canvas sagging under weeks of dust, sand piled in corners, gear half-buried.", is_narrator=True)
    show_story_box("", "The girl stepped outside—long black hair tied back, face smudged with dirt, eyes tired but sharp.", is_narrator=True)

    mystery_style2 = "sea_green2"
    
    show_story_box("???", "Ugh… over a week already. This place is a sandbox. Everything’s covered. Can’t even sleep without sand in my mouth.", color_override=mystery_style2)
    show_story_box("", "She kicked at a dune half-heartedly.", is_narrator=True)
    show_story_box("???", "And I’m too lazy to clean it…Thought I’d be gone by now.", color_override=mystery_style2)
    
    show_story_box("", "A device outside beeped—sharp, insistent. Red light flashing on a complicated rig of wires, screens, solar panels, and camping gear: foldable chair, portable stove, small satchel.", is_narrator=True)
    show_story_box("", "She froze.\nThen smiled—slow, dangerous.", is_narrator=True)
    
    show_story_box("???", "Finally… they’re here~.", color_override=mystery_style2)
    show_story_box("", "She grabbed a satchel—small, light—and walked into the jungle.\nDarkness swallowed her.", is_narrator=True)

    # --- SCENE 3: KAGAKU'S INTERROGATION ---
    show_story_box("", "********* ◆ *********\nKagaku’s POV", is_narrator=True)
    show_story_box("", "…\nI woke up slowly—head heavy, mouth dry, the faint smell of expensive carpet and sea salt in the air.", is_narrator=True)
    show_story_box("Kagaku", "Where am I..?", affiliation="Kasakura High School Student / Seven Wonders", is_thought=True)
    
    show_story_box("", "…The room was small. Cramped. Fancy, but not comfortable.\nA red velvet sofa is underneath me, and a matching seat across from me. Dim golden lighting...no windows I could see right away.", is_narrator=True)
    show_story_box("", "A man sat opposite—maybe my age, or a year or two older. Light blue curtain-bangs haircut, idol-like, almost too perfect. Legs spread slightly. Back slouched forward toward me. Hands clasped together. Staring straight into my eyes.", is_narrator=True)
    show_story_box("Kagaku", "Uwah…classic gangster pose.", affiliation="Kasakura High School Student / Seven Wonders", is_thought=True)
    
    show_story_box("", "Long sandy-yellow coat reached his black boots. White shirt underneath. Red tie. Dangerous in a quiet way.\nBehind him—three, four guys I assume to be the henchmen. Same outfit. Less threatening. Standing still and watching.", is_narrator=True)
    show_story_box("", "I didn’t recognize the style. Not a school uniform. Not any faction I knew.", is_narrator=True)
    show_story_box("", "He spoke first—stern, serious, straight to the point. But there was a naivety in his tone. Like he hadn’t been in this world long enough to lose the innocence yet.", is_narrator=True)
    
    show_story_box("Young Man", "You should already know why we took you.", affiliation="Unknown Faction")
    show_story_box("", "He raised his hand.\nIn it—my diary.\nMy stomach dropped.", is_narrator=True)
    
    show_story_box("Kagaku", "Who…uh, this is going beyond simple feuds between school students...", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Young Man", "Hurry up and tell me everything in that book.", affiliation="Unknown Faction")
    
    show_story_box("", "I smiled—small, teasing.", is_narrator=True)
    show_story_box("Kagaku", "I get it. You guys couldn’t understand my notes, could you~?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "His eyes twitched.\nHe reached to the side—pulled a long metal rapier from beside the sofa. Pointed it right at my throat.\nCold steel hovered a millimeter from my skin.", is_narrator=True)
    show_story_box("Kagaku", "Uwahh–", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "I broke into a cold sweat. An awkward smile was frozen on my face.\n…", is_narrator=True)
    
    show_story_box("Kagaku", "Well, okay. Teasing worked. He’s hotheaded. Impatient. Good. I can use that.", affiliation="Kasakura High School Student / Seven Wonders", is_thought=True)
    show_story_box("Kagaku", "I’ll dramatize the unimportant stuff. Bury the critical info in noise. Survive while I leak as little info as possible..!", affiliation="Kasakura High School Student / Seven Wonders", is_thought=True)
    
    show_story_box("", "He stared—furious—then pulled the rapier back.", is_narrator=True)
    show_story_box("Young Man", "Open it.", affiliation="Unknown Faction")
    show_story_box("", "He tossed the diary into my lap.\nI caught it. Flipped to the first page.", is_narrator=True)
    
    show_story_box("Kagaku", "Huh?", affiliation="Kasakura High School Student / Seven Wonders", is_thought=True)
    show_story_box("", "A piece of sand-dirtied paper was taped inside.\nNot my handwriting.", is_narrator=True)
    show_story_box("", "| Help is coming. Just stay alive. |\n\nWith a little heart emoji.", is_narrator=True)
    show_story_box("", "My pulse spiked. I flipped the page fast—nervous, flustered.", is_narrator=True)
    
    show_story_box("Young Man", "Why are you stuck on that page?", affiliation="Unknown Faction")
    show_story_box("Kagaku", "N-nothing! Just… checking my doodles. Heh.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "I forced a laugh…and kept flipping.\nHe didn’t buy it.\nBut he didn’t push. Not yet.", is_narrator=True)

    # --- SCENE 4: BACK AT KASAKURA ---
    show_story_box("", "********* ◆ *********\nYuri’s POV", is_narrator=True)
    show_story_box("", "Kasakura High School – History Class", is_narrator=True)
    
    show_story_box("Kojima-sensei", "…and so the Chromatic Divergence Phenomenon remains unexplained to this day, like I’ve already explained. Any questions?", affiliation="Kasakura High School Teacher")
    
    show_story_box("", "Akasuke’s phone beeped.\nHe ignored it—eyes fixed on the board. Focused. Jaw tight.", is_narrator=True)
    show_story_box("Yuri", "Gotta focus on class. All the chaos… the knight… Kagaku… none of it’s an excuse to skip studies.", affiliation="Kasakura High School Student / Seven Wonders", is_thought=True)
    show_story_box("", "I sighed.\nI looked at him.\nMy phone had gotten the same message. It’s important, ya know.", is_narrator=True)
    
    show_story_box("", "I pulled out my phone under the desk and sent him three quick texts.\n| Look at your phone. |\n| Now. |\n| Seriously. |", is_narrator=True)
    show_story_box("", "Beep. Beep. Beep.\nAkasuke-kun finally glanced down, annoyed.\nHis eyes widened.", is_narrator=True)
    
    show_story_box("Akasuke", "HUHHH?!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "He shot out of his chair—loud enough that the whole class froze, creating the biggest awkward silence ever.", is_narrator=True)
    show_story_box("Kojima-sensei", "What the hell are you doing, Hanefuji?", affiliation="Kasakura High School Teacher")
    
    show_story_box("", "Akasuke didn’t answer.\nHe marched straight to the front—grabbed Kojima-sensei’s sleeve—and dragged him toward the door.", is_narrator=True)
    show_story_box("Akasuke", "Sensei. Outside. Now.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Kojima-sensei", "Ah? Damn, the hell–", affiliation="Kasakura High School Teacher")
    show_story_box("Yuri", "I’m coming too!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I followed.\nIn the hallway, Akasuke showed Kojima the message.", is_narrator=True)
    show_story_box("", "It was from Natsume.\nNatsume had been investigating Kagaku’s lab today. Kagaku’s own phone suddenly buzzed—a message from an unknown sender.\nIt told her exact location.", is_narrator=True)
    
    show_story_box("Akasuke", "...It’s the island. The same private island the four schools were supposed to go on the joint goodwill trip to. Before Heiwa’s raid ruined everything.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Kojima-sensei", "…Good grief.", affiliation="Kasakura High School Teacher")
    show_story_box("", "He scratched his head—annoyed, tired.", is_narrator=True)
    show_story_box("Kojima-sensei", "Alright. Calm down. The school will look into it. But first—tell me everything you know.", affiliation="Kasakura High School Teacher")
    show_story_box("", "We did.", is_narrator=True)

def play_stage_3_3_start():
    # --- SCENE 1: OUTSIDE CLASSROOM ---
    show_story_box("", "********* ◆ *********\nAkasuke’s POV", is_narrator=True)
    show_story_box("", "Outside Classroom – Kasakura High School\nThe hallway was quiet after class—only the distant echo of lockers slamming and footsteps fading down the corridor.", is_narrator=True)
    show_story_box("", "Kojima-sensei stood with his arms crossed, head tilted back, staring at the ceiling like he was trying to find answers in the fluorescent lights.", is_narrator=True)
    
    show_story_box("Kojima-sensei", "…So let me get this straight. Kagaku’s crazy experiments opened some kind of parallel-universe borrowing system. Eight of you—including her—lost your hearts to a…a medieval knight.", affiliation="Kasakura High School Teacher")
    show_story_box("", "He sighed again.", is_narrator=True)
    show_story_box("Kojima-sensei", "...You can temporarily steal alternate versions of yourselves to fight better, but it’s killing you slowly…and now Kagaku’s been damn kidnapped, probably for her notes on the whole thing.", affiliation="Kasakura High School Teacher")
    
    show_story_box("", "He scratched his head again—harder this time.", is_narrator=True)
    show_story_box("Kojima-sensei", "Kagaku… that damn girl. Always one insane experiment away from blowing up the school. Or the world.", affiliation="Kasakura High School Teacher")
    show_story_box("Yuri", "Sensei…", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Kojima-sensei", "I’m not mad. But fine. You two—and your group—have a role now. Listen carefully.", affiliation="Kasakura High School Teacher")
    
    show_story_box("", "He pointed at me first.", is_narrator=True)
    show_story_box("Kojima-sensei", "Akasuke. You and a few trusted friends will accompany President Kageyama to Kiryoku Gakuen. Re-establish relations. Officially inform the student body the trip is still on. Smooth things over. Make it clear we’re not the bad guys here.", affiliation="Kasakura High School Teacher")
    
    show_story_box("", "Then at Yuri.", is_narrator=True)
    show_story_box("Kojima-sensei", "Inami. You’re with him. Watch his back. And keep him from doing anything stupid.", affiliation="Kasakura High School Teacher")
    show_story_box("Akasuke", "Hey…", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Kojima-sensei", "I’ll handle the negotiations with the higher-ups and the inter-school affairs committee. We’re trying to revive the joint trip. The cruise ship was already booked long ago. Meals pre-ordered. And so the supplies are still sitting unused.", affiliation="Kasakura High School Teacher")
    show_story_box("Kojima-sensei", "The trip was supposed to mend relations with not just Heiwa. Now it’s even more important. We use it to prove we’re not at war. Even if this whole thing’s a stretch since Kasakura was attacked. People were hurt. But we can’t let this escalate.", affiliation="Kasakura High School Teacher")
    
    show_story_box("Akasuke", "Sensei, why can’t we just go to the island ourselves? Private trip. Small group. We handle Kagaku quietly.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Kojima-sensei", "Because it’s suicide.", affiliation="Kasakura High School Teacher")
    
    show_story_box("", "He met my eyes—serious.", is_narrator=True)
    show_story_box("Kojima-sensei", "The cost is astronomical. And worse—we know almost nothing about the enemy. The ‘knight’ you talked about. The ones pulling Heiwa’s strings. There could be far more than even the Seven Wonders can handle.", affiliation="Kasakura High School Teacher")
    show_story_box("Kojima-sensei", "You’d be walking straight into enemy territory. Better to move under cover of a large group. Send in operatives. Get close. Blend in, watch, and wait. Strike when we know what we’re dealing with.", affiliation="Kasakura High School Teacher")
    
    show_story_box("", "He took a step past me—preparing to leave—then paused.", is_narrator=True)
    show_story_box("Kojima-sensei", "One more thing.", affiliation="Kasakura High School Teacher")
    show_story_box("", "He turned back.", is_narrator=True)
    
    show_story_box("Kojima-sensei", "Don’t tell anyone else about the ‘Kata’s. Not a soul.", affiliation="Kasakura High School Teacher")
    show_story_box("Akasuke", "That’s obvious—", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Kojima-sensei", "Including the higher-ups. From any school.", affiliation="Kasakura High School Teacher")
    
    show_story_box("", "I froze.", is_narrator=True)
    show_story_box("Akasuke", "…Sensei?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "He kept walking—voice lower now, almost muttering.", is_narrator=True)
    show_story_box("Kojima-sensei", "I don’t really trust them. Any of them.", affiliation="Kasakura High School Teacher")
    
    show_story_box("", "He disappeared around the corner.\nYuri and I stood in silence.", is_narrator=True)
    show_story_box("Yuri", "…He’s serious.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Akasuke", "Yeah.", affiliation="Kasakura High School Student / Seven Wonders")

    # --- SCENE 2: KIRYOKU GAKUEN ---
    show_story_box("", "Next Day – Kiryoku Gakuen Courtyard\nThe gate was open. No guards. Just a wide courtyard filled with girls—athletic, focused, moving with purpose.", is_narrator=True)
    show_story_box("", "But the atmosphere was heavy.\nStudents passing by either stared warily or deliberately looked away. Some whispered. Others crossed to the far side of the path when they saw us.", is_narrator=True)
    
    show_story_box("Kageyama", "Don’t worry. They allow men on official business. It’s not the gender rules. It’s trust.", affiliation="Kasakura High School Student Council President / Seven Wonders")
    show_story_box("", "He walked ahead—voice calm.", is_narrator=True)
    show_story_box("Kageyama", "Kiryoku believes the trip cancellation might even be deliberate—Heiwa and Kasakura stirring trouble on purpose right at that timing. They’re upset, don’t blame them.", affiliation="Kasakura High School Student Council President / Seven Wonders")
    show_story_box("Kageyama", "And don’t blame Heiwa either. Everyone knows now—they were manipulated by a third party.", affiliation="Kasakura High School Student Council President / Seven Wonders")
    
    show_story_box("Akasuke", "So we’re here to fix that?", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Kageyama", "Exactly. Mend relations. Inform them the trip is still on. Prove we’re not the enemy.", affiliation="Kasakura High School Student Council President / Seven Wonders")
    
    show_story_box("", "He and Masayoshi turned toward the student council building.", is_narrator=True)
    show_story_box("Kageyama", "We’ll handle the council. You four—head to the Self-Defense Club Room. They requested you go straight there. No wandering.", affiliation="Kasakura High School Student Council President / Seven Wonders")
    
    show_story_box("", "We were reluctant to hear it, but nodded.\nYou’d think we’d get to explore the school a little bit.", is_narrator=True)

    # --- SCENE 3: SELF-DEFENSE CLUB ROOM ---
    show_story_box("", "The Self-Defense Club Room was large—mats on the floor, punching bags hanging, mirrors along one wall.", is_narrator=True)
    show_story_box("", "Girls everywhere—most in practitioner uniforms, muscles toned, eyes focused. Some still in school uniforms, sleeves rolled up, practicing forms with fierce intensity.", is_narrator=True)
    show_story_box("", "They were training like their lives depended on it.", is_narrator=True)
    
    show_story_box("Akasuke", "...Anyone who messes with these girls is the one who needs self-defense.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Yuri", "No kidding…", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "They noticed us.\nTraining stopped instantly.\nAll eyes turned to Hana.", is_narrator=True)
    show_story_box("", "Then—they rushed her.", is_narrator=True)
    
    show_story_box("Kiryoku Girl 1", "Hana-senpai! It’s you! You’re here!", affiliation="Kiryoku Gakuen Student")
    show_story_box("Kiryoku Girl 2", "Your arms are insane! Look at that definition!", affiliation="Kiryoku Gakuen Student")
    show_story_box("Kiryoku Girl 3", "Can you show us that shoulder throw again? Please!", affiliation="Kiryoku Gakuen Student")
    
    show_story_box("", "Hana flushed—smiling shyly.", is_narrator=True)
    show_story_box("Hana", "Ahaha…T-thank you… I’d be happy to.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "They turned to us.", is_narrator=True)
    show_story_box("Kiryoku Girl 1", "Ah! You’re Kasakura’s fighters, right? Want a friendly spar~? Between schools~?", affiliation="Kiryoku Gakuen Student")
    
    show_story_box("Akasuke", "…We’d be honored.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "Yuri grinned.", is_narrator=True)
    show_story_box("Yuri", "Bring it.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Benikawa", "Oh~? This’ll be fun.", affiliation="Benikawa Ninja Clan")
    show_story_box("Hana", "Let’s keep it clean, everyone!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "The girls cheered.\nMats were cleared.\nFriendly sparring match—between schools.", is_narrator=True)
    show_story_box("", "But the tension in the air was real.", is_narrator=True)

def play_stage_3_4_start():
    # --- SCENE 1: THE APPROACH ---
    show_story_box("", "********* ◆ *********\nKageyama’s POV", is_narrator=True)
    show_story_box("", "The path to Kiryoku Gakuen’s student council office began ordinarily enough—polished marble floors, clean white walls, the faint scent of cherry blossoms drifting from somewhere unseen.", is_narrator=True)
    show_story_box("", "Then we crossed an invisible line.\nFifty meters from the double doors, everything changed.\nThe corridor ahead transformed.", is_narrator=True)
    
    show_story_box("", "Walls become cascading vines and moss-covered stone. The ceiling became a canopy of artificial leaves and twinkling turquoise lights mimicking stars.", is_narrator=True)
    show_story_box("", "Fountains bubbled with crystal water, real and fake plants intertwined in perfect harmony, bushes trimmed into elegant spirals. Marble paths alternated with cobblestone trails that wound like forest streams.", is_narrator=True)
    show_story_box("", "It felt like stepping through a portal into another world.", is_narrator=True)
    
    show_story_box("", "Masayoshi stopped short—his bokken hand tightening slightly.", is_narrator=True)
    show_story_box("Masayoshi", "…What is this?", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    show_story_box("", "I adjusted my glasses. Smiled faintly.", is_narrator=True)
    show_story_box("Kageyama", "Kiryoku Gakuen’s student council theme. It’s a kind of ‘Fantasy Nature.’", affiliation="Kasakura High School Student Council President / Seven Wonders")
    
    show_story_box("", "He glanced at the nearest fountain—real water, real koi swimming lazily beneath lily pads.", is_narrator=True)
    show_story_box("Masayoshi", "This is… excessive.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    show_story_box("Kageyama", "Not to them. Kasakura’s council is red carpet, paperwork, and workaholics.", affiliation="Kasakura High School Student Council President / Seven Wonders")
    show_story_box("Kageyama", "Kiryoku promotes so many ‘masculine’ activities—sports, combat, competition. The council balances that image. They cultivate the ‘elegant, pretty’ side of a girls-only school. It’s deliberate. Morale booster for students. Intriguing for outsiders.", affiliation="Kasakura High School Student Council President / Seven Wonders")
    
    show_story_box("", "We walked deeper.\nArtificial birds chirped from hidden speakers. Flowers bloomed in impossible colors. A small bridge arched over a shallow stream—real water, real pebbles.", is_narrator=True)
    
    show_story_box("Masayoshi", "...And the members?", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    show_story_box("Kageyama", "They’re rarely called ‘Student Council members.’ Every executive is a ‘Fairy.’ Children’s-book gentle, pretty little guardians, you do know, yes? Kind-hearted, all-powerful, ‘every student’s best friend.’", affiliation="Kasakura High School Student Council President / Seven Wonders")
    show_story_box("", "I glanced sideways.", is_narrator=True)
    show_story_box("Kageyama", "In reality? They are popular, capable girls voted in by the student body. Same as any school. But the theme works. It’s mysterious. Intriguing. It builds loyalty and draws attention.", affiliation="Kasakura High School Student Council President / Seven Wonders")

    # --- SCENE 2: THE AMBUSH / ENTRANCE ---
    show_story_box("", "We reached the end.\nWhite marble double doors—taller than both of us combined—stood before us. Intricate carvings of vines and wings wrapped around the frame.", is_narrator=True)
    
    show_story_box("", "Masayoshi stepped forward.", is_narrator=True)
    show_story_box("Masayoshi", "I shall open for you, President.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    show_story_box("Kageyama", "Wait—", affiliation="Kasakura High School Student Council President / Seven Wonders")
    
    show_story_box("", "Too late.\nHe pushed.\nThe doors parted.", is_narrator=True)
    show_story_box("", "A figure exploded from the gap—a weapon already swinging toward Masayoshi’s head.", is_narrator=True)
    show_story_box("", "CRACK!\nLoud impact—wood on wood.", is_narrator=True)
    
    show_story_box("", "Masayoshi’s bokken was up—but too slow to fully block.\nAnother bokken had been intercepted—\nStopped dead by my hand.", is_narrator=True)
    show_story_box("", "I stood between them—left hand gripping the attacker’s weapon, right adjusting my glasses.", is_narrator=True)
    
    show_story_box("", "The assailant—a beautiful short girl, pink eyes, long white hair tied at the ends—froze. Then grinned, showing one sharp fang on the left.", is_narrator=True)
    
    show_story_box("Forest Guardian Ayako", "Kageyama~! Long time no see!", affiliation="Kiryoku Gakuen Fairy")
    show_story_box("", "She lowered her bokken cheerfully.", is_narrator=True)
    show_story_box("Forest Guardian Ayako", "You know the rules. No riddle answered, no magic word—no entry.", affiliation="Kiryoku Gakuen Fairy")
    
    show_story_box("Kageyama", "Apologies. He’s new here.", affiliation="Kasakura High School Student Council President / Seven Wonders")
    
    show_story_box("", "Masayoshi lowered his bokken—expression calm, but eyes sharp.", is_narrator=True)
    show_story_box("Masayoshi", "…Impressive speed.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    show_story_box("", "Ayako laughed—bright and carefree.", is_narrator=True)
    show_story_box("Forest Guardian Ayako", "Come in, come in! The others are waiting.", affiliation="Kiryoku Gakuen Fairy")
    
    show_story_box("", "She stepped aside.\nWe entered.", is_narrator=True)

    # --- SCENE 3: THE COUNCIL MEETING ---
    show_story_box("", "The council room was—unsurprisingly—more of the same.\nArtificial forest ceiling. Vines draping marble pillars. Waterfall feature against one wall. Fairy lights floating like fireflies. Long table carved from what looked like living wood. Chairs upholstered in moss-green velvet.", is_narrator=True)
    
    show_story_box("", "Ayako bounded back to her seat—bokken resting across her lap like a toy.", is_narrator=True)
    show_story_box("Forest Guardian Ayako", "Forest Guardian Ayako, head of Kiryoku’s security division! Basically our Disciplinary Committee equivalent~.", affiliation="Kiryoku Gakuen Fairy")
    
    show_story_box("", "She twirled her bokken playfully—looking straight at Masayoshi.", is_narrator=True)
    show_story_box("Forest Guardian Ayako", "We apprehend thugs, patrol the grounds, stop fights, check infrastructure safety, all that good stuff. Same as you guys, right, Mr. Formal?", affiliation="Kiryoku Gakuen Fairy")
    show_story_box("", "Masayoshi gave the smallest nod.", is_narrator=True)
    
    show_story_box("", "Next to her sat a taller girl—short blonde hair tied into cute long pigtails, golden eyes calm and steady. Flat, well-toned build that could almost pass for a boy’s if not for the gentle curves. She radiated big-sister energy.", is_narrator=True)
    
    show_story_box("Lake Strider Sumiko", "Lake Strider Sumiko. Our Treasurer~.", affiliation="Kiryoku Gakuen Fairy")
    show_story_box("", "She waved to us and spoke softly—composed.", is_narrator=True)
    show_story_box("Lake Strider Sumiko", "Kiryoku’s more advanced than Heiwa Seiritsu, but not as much as Kasakura. I heard your technological geniuses like Natsume and Kagaku keep pushing boundaries.", affiliation="Kiryoku Gakuen Fairy")
    
    show_story_box("Forest Guardian Ayako", "Our economy’s chaotic—carefree students, constant spending on sports and clubs! She handles incoming funds, expenses and budgets.", affiliation="Kiryoku Gakuen Fairy")
    
    show_story_box("Lake Strider Sumiko", "The most exhausting project? Funding this entire ‘fantasy nature’ theme zone around the council…students loved the idea, though. They donated heavily.", affiliation="Kiryoku Gakuen Fairy")
    show_story_box("", "She smiled faintly and proud.", is_narrator=True)
    
    show_story_box("", "Opposite her sat the third.", is_narrator=True)
    show_story_box("Nocturnal Companion Rina", "Ah, I don’t need much introduction.", affiliation="Kiryoku Gakuen Fairy")
    show_story_box("", "Black hair, gray eyes, cool red beret tilted at a stylish angle. Build similar to Yuri or Hana—athletic, strong. Quiet confidence.", is_narrator=True)
    show_story_box("Nocturnal Companion Rina", "Secretary to the council president. I assist. And protect the prez.", affiliation="Kiryoku Gakuen Fairy")
    
    show_story_box("", "Kageyama raised an eyebrow.", is_narrator=True)
    show_story_box("Kageyama", "Ayako…you aren’t sitting in the usual seat. Have you stepped down?", affiliation="Kasakura High School Student Council President / Seven Wonders")
    
    show_story_box("", "Ayako grinned—fang flashing again.", is_narrator=True)
    show_story_box("Forest Guardian Ayako", "Yup! Third year now. I wanted to be free. Less paperwork, more action.", affiliation="Kiryoku Gakuen Fairy")
    show_story_box("Masayoshi", "Then… who is the current president?", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    show_story_box("", "Ayako’s eyes sparkled with mischief.", is_narrator=True)
    show_story_box("Forest Guardian Ayako", "That’s…Oh! She just woke up from her nap~.", affiliation="Kiryoku Gakuen Fairy")
    
    show_story_box("", "The side door opened.\nA small figure shuffled in—white hair, pink eyes, sleepy kuudere expression. “Loli”-sized. Looked like Ayako but half her age.", is_narrator=True)
    
    show_story_box("Forest Guardian Ayako", "Everyone, meet the ‘Queen of Fairies’, Aina. My little sister~.", affiliation="Kiryoku Gakuen Fairy")
    show_story_box("", "Aina rubbed her eyes—yawning.", is_narrator=True)
    show_story_box("Aina", "Mm…Morning.", affiliation="Queen Of Fairies")
    
    show_story_box("", "Kageyama stared.", is_narrator=True)
    show_story_box("Kageyama", "You…?", affiliation="Kasakura High School Student Council President / Seven Wonders")
    
    show_story_box("", "Ayako laughed.", is_narrator=True)
    show_story_box("Forest Guardian Ayako", "Yup! First-year. Two years younger than me. I handed the position over.", affiliation="Kiryoku Gakuen Fairy")
    show_story_box("Masayoshi", "…A first-year president?", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    show_story_box("", "Sumiko and Rina immediately began pampering her—adjusting her seat, offering tea, fixing her hair—like she was a friend’s little sibling visiting.", is_narrator=True)
    show_story_box("", "But she was literally the president.", is_narrator=True)
    
    show_story_box("", "Ayako leaned back—smiling proudly.", is_narrator=True)
    show_story_box("Forest Guardian Ayako", "We handle the paperwork, obviously. But Aina’s image? She’s adorable. Students adore her! That means massive support for the council. At the end of the day—even Kiryoku girls like cute things.", affiliation="Kiryoku Gakuen Fairy")
    
    show_story_box("", "Aina yawned again—head dropping onto the table.\n…And she’s already asleep.", is_narrator=True)
    
    show_story_box("", "Ayako clapped her hands.", is_narrator=True)
    show_story_box("Forest Guardian Ayako", "Right! Then let’s get to serious business~.", affiliation="Kiryoku Gakuen Fairy")
    
    show_story_box("", "Nonetheless, the room settled, and the meeting began.", is_narrator=True)

def play_stage_3_5_story():
    # --- SCENE 1: PRESENT (AFTER THE INTERROGATION) ---
    show_story_box("", "********* ◆ *********\nKagaku’s POV", is_narrator=True)
    show_story_box("", "The heavy mahogany door clicked shut.\nThe young man in the sandy coat was gone.\nFinally.", is_narrator=True)
    show_story_box("", "I slumped back into the red velvet sofa, my spine practically turning to jelly. The two henchmen by the door didn’t even twitch—statues in suits, watching me with bored, dead eyes.", is_narrator=True)
    show_story_box("", "I let out a long, shaky breath that I’d been holding for what felt like an hour.", is_narrator=True)
    
    show_story_box("Kagaku", "Haah…! Hah… I thought I was dead. I actually thought I was dead.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "My hands were trembling. I hid them under my diary, clutching the leather cover until my knuckles turned white.", is_narrator=True)
    show_story_box("", "I glanced down at the note in the book.\n‘Help is coming.’", is_narrator=True)
    
    show_story_box("Kagaku", "Yeah. But until then… I have to survive this.", affiliation="Kasakura High School Student / Seven Wonders", is_thought=True)
    
    show_story_box("", "I closed my eyes, replaying the last ten minutes in my head. Analyzing.\nChecking for holes in my own lies.", is_narrator=True)

    # --- SCENE 2: FLASHBACK ---
    show_story_box("", "(Flashback – Minutes Earlier)\nThe rapier tip was gone from my throat, but he was still holding it loose at his side.", is_narrator=True)
    
    show_story_box("Young Man", "So. Explain. What is a ‘Kata’?", affiliation="Unknown Faction")
    
    show_story_box("", "He asked it so casually. Like asking for a weather report.", is_narrator=True)
    show_story_box("", "I decided right then: mix truth with fiction. If I lie about everything, he’ll catch me. The ‘Parallel Universe’ theory is too complex to make up on the fly anyway.", is_narrator=True)
    
    show_story_box("Kagaku", "It’s… a form. A shell. You know how there are infinite universes? Infinite possibilities?", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Kagaku", "Uhh…so…A ‘Kata’ is basically…borrowing the strength and skills of ‘yourself’ from another timeline. A version of you that made different choices. A version that became stronger.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "He nodded slowly.", is_narrator=True)
    
    show_story_box("Young Man", "And that explains the sudden power boost we witnessed during the raid. The girl who changed appearance. The boy with the chains.", affiliation="Unknown Faction")
    
    show_story_box("", "He accepted the term immediately. He didn’t question the science behind. He just wanted the result.", is_narrator=True)
    
    show_story_box("Young Man", "How do we use it?", affiliation="Unknown Faction")
    
    show_story_box("", "There it was. The million-dollar question.\nI froze.", is_narrator=True)
    
    show_story_box("Kagaku", "Should I tell him the truth?", affiliation="Kasakura High School Student / Seven Wonders", is_thought=True)
    show_story_box("Kagaku", "I’ll have to tell him: ‘You can’t. Unless you get your heart ripped out by this…ghost knight and survive by a miracle.’", affiliation="Kasakura High School Student / Seven Wonders", is_thought=True)
    show_story_box("Kagaku", "If I told him all that, I'd become useless. And useless hostages get disposed of.", affiliation="Kasakura High School Student / Seven Wonders", is_thought=True)
    
    show_story_box("", "I swallowed hard.", is_narrator=True)
    
    show_story_box("Kagaku", "It’s… complicated. It’s not magic. It’s science. It requires specific resonance frequencies. Biological anchors. And…yeah, rare materials.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "He didn’t blink. He just reached into his coat pocket.\nAnd pulled out a blue jewel.\nMy breath hitched.", is_narrator=True)
    show_story_box("", "The Anchor. The one Masayoshi-senpai took from the lab.\nI had it with me when I was kidnapped..!", is_narrator=True)
    
    show_story_box("Young Man", "We have the ‘anchor’. Your notes say this acts as the bridge.", affiliation="Unknown Faction")
    show_story_box("", "He held it up. It pulsed faintly.", is_narrator=True)
    show_story_box("Young Man", "So make it work. Now.", affiliation="Unknown Faction")
    
    show_story_box("", "Panic spiked in my chest.", is_narrator=True)
    show_story_box("Kagaku", "Think, Kagaku. Think!", affiliation="Kasakura High School Student / Seven Wonders", is_thought=True)
    
    show_story_box("Kagaku", "Ahh! I-I can’t! Not yet!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "The rapier moved. Fast.\nThe tip rested against my collarbone once again.", is_narrator=True)
    
    show_story_box("Young Man", "Excuse me?", affiliation="Unknown Faction")
    
    show_story_box("Kagaku", "It’s… it’s out of charge! Look at the pulse! It’s faint, right?!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "I blurted it out. Total nonsense. But scientific-sounding nonsense.", is_narrator=True)
    show_story_box("Kagaku", "Dimensional bridging takes massive energy! The crystal is drained from the last time Akasuke used it! If you force it now, it’ll shatter. Then you get nothing. Zero. Nada!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "He paused, looked at the crystal, then looked at me.", is_narrator=True)
    
    show_story_box("Young Man", "Recharging… How long?", affiliation="Unknown Faction")
    
    show_story_box("", "I did the math in my head. How long will it take for Natsume to find me? A week? Two weeks?", is_narrator=True)
    
    show_story_box("Kagaku", "Uhh…seven…days, minimum. It needs to absorb ambient—GAH!—", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "The blade pressed harder. A drop of blood welled up.", is_narrator=True)
    
    show_story_box("Young Man", "Too long.", affiliation="Unknown Faction")
    show_story_box("Kagaku", "F-Five days?!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "He narrowed his eyes.", is_narrator=True)
    
    show_story_box("Kagaku", "Three! Give me three days! I can… I can rig a catalyst! Speed up the process! But less than that and it blows up! I swear!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Silence.\nHeavy, suffocating silence.\nHe withdrew the blade, sheathing it with a sharp click.", is_narrator=True)
    
    show_story_box("Young Man", "Three days.", affiliation="Unknown Faction")
    show_story_box("", "He checked his watch—gold, expensive.", is_narrator=True)
    show_story_box("Young Man", "Acceptable. The Boss arrives in three days to claim the power personally. Have it ready by then.", affiliation="Unknown Faction")
    
    show_story_box("", "He turned and walked to the door.", is_narrator=True)
    
    show_story_box("Young Man", "If it’s not ready… I’ll carve the theory out of you instead.", affiliation="Unknown Faction")
    show_story_box("", "Then he left.", is_narrator=True)

    # --- SCENE 3: BACK TO PRESENT ---
    show_story_box("", "(Present Time)\nI opened my eyes.", is_narrator=True)
    show_story_box("", "Three days.\nI bought myself seventy-two hours.\nI looked at the diary again.", is_narrator=True)
    
    show_story_box("Kagaku", "The ‘Boss’, huh.", affiliation="Kasakura High School Student / Seven Wonders", is_thought=True)
    show_story_box("Kagaku", "Whoever that guy is… he’s the one pulling the strings. The Heiwa raid. The Knight. My kidnapping. It’s probably all leading to him. And he’s coming here.", affiliation="Kasakura High School Student / Seven Wonders", is_thought=True)
    show_story_box("Kagaku", "If I’m still here when he arrives… I have a feeling a rapier to the throat will be the least of my worries.", affiliation="Kasakura High School Student / Seven Wonders", is_thought=True)
    
    show_story_box("", "I traced the heart emoji on the note.\n‘Help is coming.’", is_narrator=True)
    show_story_box("Kagaku", "Someone slipped this in after Natsume lost the book. Meaning… someone is here. Inside their organization? Or a shadow trailing them?", affiliation="Kasakura High School Student / Seven Wonders", is_thought=True)
    
    show_story_box("Kagaku", "...Please hurry.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I hugged the book to my chest.", is_narrator=True)
    
    show_story_box("Kagaku", "I don’t know if I can talk my way out of ‘The Boss’, haha...", affiliation="Kasakura High School Student / Seven Wonders")

def play_stage_3_6_start():
    # --- SCENE 1: HANA'S POV (AFTER THE SPAR) ---
    show_story_box("", "********* ◆ *********\nHana’s POV", is_narrator=True)
    show_story_box("", "Kiryoku Gakuen – Self-Defense Club Room\nThe sound of heavy breathing and shifting mats filled the large room, but the atmosphere was… strangely bright.", is_narrator=True)
    show_story_box("", "The sparring was over.\nWe had won. Decisively.", is_narrator=True)
    
    show_story_box("", "Yuri-chan had thrown their strongest grapplers with pure, unadulterated power. Akasuke-kun had dismantled their strikers with technique so overwhelming it looked like he was fighting in slow motion. And Benikawa-san… well, she had used every dirty trick, feint, and unorthodox movement in the book to leave her opponents tripping over their own feet.", is_narrator=True)
    show_story_box("", "Yet, as we wiped sweat from our brows, the Kiryoku girls weren’t sulking. They weren’t frustrated.\nThey were beaming.", is_narrator=True)
    
    show_story_box("Kiryoku Girl 1", "Hana-senpai! That throw you did at the end—the way you used my own momentum? That was incredible!", affiliation="Kiryoku Gakuen Student")
    show_story_box("Kiryoku Girl 2", "Please teach us more next time! We’ve never seen flowers bloom in a dojo before!", affiliation="Kiryoku Gakuen Student")
    
    show_story_box("", "I smiled, bowing slightly, feeling my cheeks heat up.", is_narrator=True)
    show_story_box("Hana", "Ah… thank you. You all have excellent foundations. I barely kept up.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "We packed our gear and headed for the exit. The girls waved us off with terrifying amounts of energy.", is_narrator=True)
    show_story_box("", "I walked a half-step behind Akasuke-kun, thinking.\nSomething was… off.", is_narrator=True)
    
    show_story_box("Hana", "...Akasuke-kun. Everyone.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "They stopped and turned.", is_narrator=True)
    
    show_story_box("Akasuke", "Hm? What is it, Hana-senpai?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Hana", "Did you… notice anything strange about the students?", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Yuri", "Strange? Well, they were energetic as heck! Almost reminded me of Benikawa on a sugar rush.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Benikawa", "Hey!", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Hana", "That’s just it. They lost. Badly. Benikawa-san was using painful joint locks. Yuri-chan was slamming them onto mats hard enough to shake the floor. And Akasuke-kun… you completely shut down their pride as fighters with pure technique.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "I looked back at the closed club door.", is_narrator=True)
    show_story_box("Hana", "Usually, there would be frustration. Anger. A little bit of fear, maybe. But there was none. Only… optimism.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Akasuke frowned, crossing his arms.", is_narrator=True)
    show_story_box("Akasuke", "You think they’re being mind-controlled, or something? Forced to be happy?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I waved my hands frantically, feeling heat rise to my face.", is_narrator=True)
    show_story_box("Hana", "N-No! Not exactly! That’s—I didn’t mean it like some sci-fi movie!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "I took a breath to calm down.", is_narrator=True)
    
    show_story_box("Hana", "I mean… it’s not that they are being  forced to be happy. It feels more like… the negative emotions that supposedly come with defeat—shame, hesitation, fear—simply just…didn’t exist for them back then…", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Hana", "Their morale is impenetrable because they lack the capacity to be discouraged.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Benikawa tilted her head, tapping her chin.", is_narrator=True)
    show_story_box("Benikawa", "Hana-senpai might be onto something~. Usually, when I hit someone with a kick to the kidney, they hesitate before attacking again. These girls? They just bounced back up instantly. If the spar hadn’t ended, they would’ve figured out my tricks eventually just by brute-forcing through the pain~.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Akasuke", "A lack of negative inhibition… That’s dangerous in a fight. It makes them fearless.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Just then—the hallway doors burst open.\nA girl in a Kiryoku uniform—wearing an armband that marked her as a Council aide—sprinted toward us, panting.", is_narrator=True)
    
    show_story_box("Council Aide", "Kasakura representatives! Emergency!", affiliation="Kiryoku Gakuen Student Council")
    
    show_story_box("", "Akasuke stepped forward.", is_narrator=True)
    show_story_box("Akasuke", "What’s happened?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Council Aide", "The Student Council Office! Please, hurry! There’s… a situation with your President!", affiliation="Kiryoku Gakuen Student Council")
    
    show_story_box("", "We exchanged one look.\nThen we ran.", is_narrator=True)

    # --- SCENE 2: KAGEYAMA's POV (FLASHBACK TO MEETING) ---
    show_story_box("", "********* ◆ *********\nKageyama’s POV", is_narrator=True)
    show_story_box("", "Kiryoku Gakuen – Student Council Office (A Few Minutes Prior)", is_narrator=True)
    show_story_box("", "The meeting seems to be proceeding well.\nThe tea Aina-san had been served was getting cold. She remained asleep, head resting on her arms, breathing rhythmically.", is_narrator=True)
    show_story_box("", "I sat opposite the ‘Fairies,’ keeping my posture relaxed despite the unnerving fantasy décor surrounding us.", is_narrator=True)
    
    show_story_box("Kageyama", "To summarize: Kasakura High School had no deliberate hand in the conflict that disrupted the original trip schedule. The raid on our school was orchestrated entirely by Heiwa Seiritsu… and a third party manipulating them.", affiliation="Kasakura High School Student Council President / Seven Wonders")
    
    show_story_box("Lake Strider Sumiko", "A third party?", affiliation="Kiryoku Gakuen Fairy")
    
    show_story_box("Kageyama", "An individual—or group—who strategically controlled Heiwa’s forces. Their goal was to deal a crippling blow to Kasakura’s infrastructure.", affiliation="Kasakura High School Student Council President / Seven Wonders")
    show_story_box("", "I paused.", is_narrator=True)
    show_story_box("Kageyama", "I’ll purposefully leave out the Katas. Kojima-sensei’s warning to everyone was clear: Trust no one.", affiliation="Kasakura High School Student Council President / Seven Wonders", is_thought=True)
    
    show_story_box("", "Sumiko nodded slowly.", is_narrator=True)
    show_story_box("Lake Strider Sumiko", "Relax, President Kageyama. We believe you. The Fairies—and the student body—know Kasakura wouldn’t break a treaty so recklessly.", affiliation="Kiryoku Gakuen Fairy")
    
    show_story_box("Forest Guardian Ayako", "But you’re still holding something back, aren’t you?", affiliation="Kiryoku Gakuen Fairy")
    show_story_box("", "Ayako was leaning forward, her chin resting on her hand, grinning. Her fang glinted.", is_narrator=True)
    show_story_box("Forest Guardian Ayako", "Trust goes both ways, Kageyama. If you want us to fully back this reinstatement, you need to spill the whole tea. Not just the parts that make you look like victims~.", affiliation="Kiryoku Gakuen Fairy")
    
    show_story_box("Kageyama", "Sharp. Very sharp.", affiliation="Kasakura High School Student Council President / Seven Wonders", is_thought=True)
    show_story_box("", "I adjusted my glasses.", is_narrator=True)
    show_story_box("Kageyama", "Rest assured, the investigation into the mastermind is ongoing. Once we have concrete names, Kiryoku Gakuen, and Miyabi Academy, will be the first to know.", affiliation="Kasakura High School Student Council President / Seven Wonders")
    show_story_box("", "I smoothly shifted the topic.", is_narrator=True)
    show_story_box("Kageyama", "–And regarding the joint trip. Since the supplies are pre-booked, reinstating the event is logically the best course to repair inter-school relations.", affiliation="Kasakura High School Student Council President / Seven Wonders")
    
    show_story_box("Nocturnal Companion Rina", "...Yeah. Agreed. We’ve been discussing themes. Since Heiwa and Kasakura are… volatile…we suggest hosting sporty events.", affiliation="Kiryoku Gakuen Fairy")
    show_story_box("Nocturnal Companion Rina", "Competitive, but structured. It brings students together through rivalry rather than politics. What do you say?", affiliation="Kiryoku Gakuen Fairy")
    
    show_story_box("Kageyama", "An excellent proposal. Speaking of structure… is Kiryoku considering updating its enrollment policies? Perhaps becoming co-ed in the future?", affiliation="Kasakura High School Student Council President / Seven Wonders")
    
    show_story_box("", "Rina blinked, seemingly caught off guard by the detour.", is_narrator=True)
    show_story_box("Nocturnal Companion Rina", "I… do not know. Obviously. That decision lies solely with the board of directors and the other higher ups of the school.", affiliation="Kiryoku Gakuen Fairy")
    
    show_story_box("", "I opened my mouth to press further regarding these ‘higher ups’—", is_narrator=True)
    
    show_story_box("Forest Guardian Ayako", "Stop.", affiliation="Kiryoku Gakuen Fairy")
    show_story_box("", "The playful grin vanished from Ayako’s face.\nThe air in the room dropped ten degrees. Even the artificial bird sounds seemed to stop.", is_narrator=True)
    show_story_box("", "She sat up straight, eyes boring into me. Intense. Predatory.", is_narrator=True)
    
    show_story_box("", "Masayoshi shifted in his seat.", is_narrator=True)
    show_story_box("Masayoshi", "...Is something amiss, Ayako-dono? The sudden hostility is palpable.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    show_story_box("", "Ayako didn’t answer him. She pointed a finger at the sleeping girl next to her.", is_narrator=True)
    show_story_box("Forest Guardian Ayako", "Aina. My sister. Our Queen.", affiliation="Kiryoku Gakuen Fairy")
    
    show_story_box("Kageyama", "Yes? She is… sleeping. As she has been for the duration of this meeting.", affiliation="Kasakura High School Student Council President / Seven Wonders")
    
    show_story_box("Forest Guardian Ayako", "Aina possesses a gift. She’s powerfully empathetic. The ‘Queen of Fairies’ constantly absorbs ‘malice’—hostility, bloodlust, negative intent—from people nearby. Like a sponge.", affiliation="Kiryoku Gakuen Fairy")
    show_story_box("", "Ayako’s hand drifted to the bokken on the table.", is_narrator=True)
    show_story_box("Forest Guardian Ayako", "So, when she suddenly gets tired? It means she absorbed a massive amount in a short time. Or… an individual with overflowing malice just entered her range.", affiliation="Kiryoku Gakuen Fairy")
    
    show_story_box("", "She narrowed her pink eyes.", is_narrator=True)
    show_story_box("Forest Guardian Ayako", "She woke up soon after you two entered the room and sat here. Then, she passed out almost immediately after. That means one of you is hiding enough darkness to overwhelm her in seconds.", affiliation="Kiryoku Gakuen Fairy")
    show_story_box("Forest Guardian Ayako", "...What’s the meaning of this?", affiliation="Kiryoku Gakuen Fairy")
    
    show_story_box("", "Masayoshi stood up—offended.", is_narrator=True)
    show_story_box("Masayoshi", "That is preposterous..! To accuse us based on a supernatural hunch—", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    show_story_box("", "I chuckled.\nIt was a dry sound.", is_narrator=True)
    show_story_box("Kageyama", "Well, Masayoshi. It must be you. You always were too uptight for your own good. All that repressed anger regarding dress codes finally leaking out?", affiliation="Kasakura High School Student Council President / Seven Wonders")
    show_story_box("", "I said it with a deliberate, deadpan seriousness.", is_narrator=True)
    
    show_story_box("", "Masayoshi looked at me, betrayed.", is_narrator=True)
    show_story_box("Masayoshi", "President—!?", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    show_story_box("", "Ayako didn’t laugh.\nShe moved.\nFaster than before.", is_narrator=True)
    show_story_box("", "She vaulted over the table—bokken drawn in a blur—swinging straight for my neck.", is_narrator=True)
    
    show_story_box("", "Masayoshi reacted instantly. He stepped in, drawing his own bokken to intercept.", is_narrator=True)
    show_story_box("", "CRACK!\nThe sound was like a gunshot.", is_narrator=True)
    
    show_story_box("", "Their weapons locked—wood grinding against wood. Masayoshi’s stance was solid, but Ayako was pressing him back, her grin returning, feral and wide.", is_narrator=True)
    
    show_story_box("Masayoshi", "Guh…! Her strength…!", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    show_story_box("", "Sumiko and Rina stayed seated, hands on their weapons, watching coldly. They weren’t stopping her.", is_narrator=True)
    
    show_story_box("", "BANG!\nThe double doors burst open.", is_narrator=True)
    show_story_box("", "Akasuke, Yuri, Hana, and Benikawa skidded to a halt in the doorway.", is_narrator=True)
    
    show_story_box("Akasuke", "Prez?!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "They took in the scene: Masayoshi locked in combat with the former Kiryoku President, the other Fairies hostile, and me sitting calmly in the eye of the storm.", is_narrator=True)
    
    show_story_box("", "I adjusted my glasses.", is_narrator=True)
    show_story_box("Kageyama", "Ah. Excellent timing.", affiliation="Kasakura High School Student Council President / Seven Wonders")
    show_story_box("", "I gestured to the Fairies.", is_narrator=True)
    show_story_box("Kageyama", "Could you help me suppress our hosts? We need to have a… calm discussion.", affiliation="Kasakura High School Student Council President / Seven Wonders")

def play_stage_3_7_end():
    # --- SCENE 1: THE FIGHT (MASAYOSHI'S POV) ---
    show_story_box("", "********* ◆ *********\nMasayoshi’s POV", is_narrator=True)
    show_story_box("", "The \"Forest of the Fairies\" had turned into a warzone.\nArtificial vines were shredded. Water from the koi pond splashed onto the marble floor as bodies moved at blinding speeds.", is_narrator=True)
    
    show_story_box("", "Sumiko—the Treasurer—was a terror.\nOne moment she was five meters away; the next, she was inside Akasuke’s guard. Her movement wasn’t a run—it was a glide.", is_narrator=True)
    show_story_box("", "Shukuchi. Instant acceleration that ignored inertia.", is_narrator=True)
    show_story_box("", "Akasuke, Yuri, and Benikawa were giving their all just to keep her at bay.", is_narrator=True)
    
    show_story_box("Akasuke", "Back! Don’t let her get behind us!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Yuri", "She’s fast! Like, ninja fast!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Benikawa", "Hey! I’m right here! But yeah—she’s slippery!", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "Meanwhile, I had my own problems.\nHana stood beside me, deflecting blows with open-palm strikes, but Ayako—the Security Head—was overwhelming.", is_narrator=True)
    show_story_box("", "She didn’t just move fast; she bounced. Off pillars, off tables, off the floor. Her trajectory was chaos. Trying to meet her head-on was like trying to catch a hurricane in a bottle.", is_narrator=True)
    
    show_story_box("Hana", "Masayoshi-kun! Left!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "I raised my bokken just in time.\nCRACK!", is_narrator=True)
    
    show_story_box("", "Ayako’s strike vibrated through my bones. She grinned, pushed off my guard, and landed on the Council table, looking down at us.", is_narrator=True)
    show_story_box("Forest Guardian Ayako", "Too slow, Mr. Formal! Is that all the Disciplinary Committee has to offer?", affiliation="Kiryoku Gakuen Fairy")
    
    show_story_box("", "In the corner of my eye, I saw the President.\nKageyama stood near the entrance, dodging Rina’s strikes with minimal movement. A tilt of the head. A step to the side. He wasn’t fighting back—he was analyzing.", is_narrator=True)
    
    show_story_box("Kageyama", "Rina-san favors her right side. She glances at Aina every three seconds. Her focus is divided. Keep your distance, she won’t chase.", affiliation="Kasakura High School Student Council President / Seven Wonders")
    show_story_box("", "He was shouting commands to us while dodging a bokken aimed at his temple.", is_narrator=True)
    
    show_story_box("", "Rina—the Secretary—remained calm. She swung, missed, but didn’t pursue. Her eyes darted back to the sleeping Aina.", is_narrator=True)
    show_story_box("Nocturnal Companion Rina", "Stop analyzing me like a lab rat.", affiliation="Kiryoku Gakuen Fairy")
    
    show_story_box("", "I realized it then.\nRina wasn’t trying to win. She was guarding Aina.", is_narrator=True)
    show_story_box("", "I glanced at Sumiko. Despite her ferocity, she never strayed too far from the center table where Aina slept. She was keeping Akasuke’s group pushed back—creating a perimeter.", is_narrator=True)
    show_story_box("Masayoshi", "They aren’t fighting to destroy us. They are fighting to protect their ‘Queen’.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders", is_thought=True)
    
    show_story_box("", "The issue… was Ayako.\nShe launched herself off the table—a blur of white hair and manic energy. She was hunting. She truly believed Kageyama harbored evil intentions.", is_narrator=True)
    
    show_story_box("Masayoshi", "I must end this. Forgive me, Ayako-dono.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders", is_thought=True)
    show_story_box("", "I gripped my bokken. I would not use the blade—even a wooden one can break bones. I hoped not to disarm her. Incapacitate her.", is_narrator=True)
    show_story_box("", "I stepped forward, meeting her rush.\nParry. Deflect. Strike.", is_narrator=True)
    show_story_box("", "I pushed her back, weaving through her chaotic rhythm. Hana flanked her, cutting off her escape with quick punches and kicks.\nWe had her.", is_narrator=True)
    
    show_story_box("", "As I moved for the takedown, my mind betrayed me.", is_narrator=True)
    show_story_box("", "| The President harbored malice. |", is_narrator=True)
    show_story_box("", "Ayako’s accusation echoed in my head.", is_narrator=True)
    
    show_story_box("Masayoshi", "I thought of Kageyama. My friend. My leader. I had never doubted him.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders", is_thought=True)
    show_story_box("Masayoshi", "But…\nI remembered…at the end of the Heiwa Seiritsu raid.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders", is_thought=True)
    show_story_box("Masayoshi", "When Akasuke and I found him, he wasn’t in the Council Room. He was in the Archives. Alone. Surrounded by files.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders", is_thought=True)
    show_story_box("Masayoshi", "He said it was safer.\nBut was it? Or was he looking for something?", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders", is_thought=True)
    show_story_box("Masayoshi", "If he truly harbored enough malice to knock out Aina-dono… who is it directed at?", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders", is_thought=True)
    show_story_box("Masayoshi", "Why?\nIs there something I do not know?", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders", is_thought=True)
    
    show_story_box("", "The hesitation lasted a fraction of a second.", is_narrator=True)
    show_story_box("Masayoshi", "! I have to––", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders", is_thought=True)
    
    show_story_box("", "No, just that was enough for her..! Ayako saw the opening.", is_narrator=True)
    show_story_box("", "She didn’t feint. She didn’t dodge. She lunged straight through my guard.\nWHAM!", is_narrator=True)
    show_story_box("", "Her bokken connected cleanly with the point of my chin.", is_narrator=True)
    
    show_story_box("Masayoshi", "Guh—!", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    show_story_box("", "The world spun. My legs turned to water.\nI hit the floor. Darkness crept in my vision.", is_narrator=True)

    # --- SCENE 2: THE INTERRUPTION (AKASUKE'S POV) ---
    show_story_box("", "********* ◆ *********\nAkasuke’s POV", is_narrator=True)
    show_story_box("", "!!\nMasayoshi-senpai went down hard.", is_narrator=True)
    
    show_story_box("Akasuke", "Senpai!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Ayako landed lightly beside him, spinning her bokken. She didn’t celebrate. Her eyes immediately locked onto me.", is_narrator=True)
    show_story_box("Forest Guardian Ayako", "One down. Three to go~.", affiliation="Kiryoku Gakuen Fairy")
    
    show_story_box("", "She coiled her legs to spring—\nSLAM!\nThe double doors burst open again.", is_narrator=True)
    
    show_story_box("???", "WAIT!! STOP!!", affiliation="")
    show_story_box("", "A flood of girls in gi and athletic wear poured into the room. The Self-Defense Club members—the ones we’d just sparred with.", is_narrator=True)
    show_story_box("", "They rushed between us and the Fairies, arms waved frantically.", is_narrator=True)
    
    show_story_box("Kiryoku Club Member A", "Ayako-sama! Please stop! It’s a misunderstanding!", affiliation="Kiryoku Gakuen Student")
    show_story_box("", "Ayako froze mid-step.", is_narrator=True)
    
    show_story_box("Forest Guardian Ayako", "Huh? Move! These intruders hurt Aina!", affiliation="Kiryoku Gakuen Fairy")
    show_story_box("Kiryoku Club Member B", "No! No, they didn’t!", affiliation="Kiryoku Gakuen Student")
    
    show_story_box("", "Kageyama stepped forward—unruffled, despite having been attacked seconds ago.", is_narrator=True)
    show_story_box("Kageyama", "It seems your student body has an explanation for Aina-san’s condition.", affiliation="Kasakura High School Student Council President / Seven Wonders")
    
    show_story_box("", "The club leader—a tall girl with a ponytail—bowed frantically to Ayako.", is_narrator=True)
    show_story_box("Club Leader", "It was us! The sparring session earlier…it was so, so intense! We must have been so excited! We were projecting so much fighting spirit and adrenaline!", affiliation="Kiryoku Gakuen Student")
    show_story_box("Kiryoku Club Member A", "Yeah! Aina-sama must have been working overtime to filter out our aggression and keep the mood friendly! We exhausted her!", affiliation="Kiryoku Gakuen Student")
    
    show_story_box("", "Ayako blinked. She lowered her bokken.", is_narrator=True)
    show_story_box("Forest Guardian Ayako", "...You guys did?", affiliation="Kiryoku Gakuen Fairy")
    
    show_story_box("", "She looked at her sister.\nAt that moment, Aina also stirred.", is_narrator=True)
    show_story_box("Aina", "Mm…?", affiliation="Queen Of Fairies")
    
    show_story_box("", "She sat up, rubbing her eyes sleepily. She looked at the chaotic room—Masayoshi on the floor, Fairies armed, club members panting.\nShe tilted her head.", is_narrator=True)
    show_story_box("Aina", "Are we… fighting again…?", affiliation="Queen Of Fairies")
    
    show_story_box("", "Her voice was soft. Innocent.\nThe tension in the room evaporated instantly.", is_narrator=True)
    show_story_box("", "Sumiko put away her weapon. Rina rushed to Aina’s side. The club members followed suit and squealed.", is_narrator=True)
    
    show_story_box("Club Members", "Aina-sama~! No! We’re just… playing! Playing tag!", affiliation="Kiryoku Gakuen Students")
    show_story_box("Club Members", "Here, have a pillow! Go back to sleep!", affiliation="Kiryoku Gakuen Students")
    
    show_story_box("", "Ayako sighed—long and loud. The demonic aura vanished, replaced by her usual cheerfulness.", is_narrator=True)
    show_story_box("Forest Guardian Ayako", "Aww, man. And I was just getting warmed up.", affiliation="Kiryoku Gakuen Fairy")
    
    show_story_box("", "She walked over to Masayoshi, who was groaning and trying to sit up. She grabbed his hand and hauled him to his feet.", is_narrator=True)
    show_story_box("Forest Guardian Ayako", "Good match, Mr. Formal! You got a hard chin.", affiliation="Kiryoku Gakuen Fairy")
    show_story_box("", "She flashed a fang, grinning.\nMasayoshi rubbed his jaw, swaying slightly.", is_narrator=True)
    
    show_story_box("Masayoshi", "I… thank you… I think.", affiliation="Kasakura High School Disciplinary Committee / Seven Wonders")
    
    show_story_box("", "I turned to Sumiko. She was dusting off her skirt, looking calm again.", is_narrator=True)
    show_story_box("Akasuke", "You were holding back, weren’t you?", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "Sumiko smiled—polite and sisterly.", is_narrator=True)
    show_story_box("Lake Strider Sumiko", "We have a treaty, Akasuke-kun. Escalating this to serious injury would be… fiscally irresponsible for the school’s reputation.", affiliation="Kiryoku Gakuen Fairy")
    show_story_box("", "She shook my hand. Her grip was iron.", is_narrator=True)
    show_story_box("Akasuke", "Right. Thanks.", affiliation="Kasakura High School Student / Seven Wonders")

    # --- SCENE 3: THE SUSPICION ---
    show_story_box("", "The room slowly returned to order. The club members ushered themselves out. The Fairies returned to their seats.\nWe moved to join them.", is_narrator=True)
    
    show_story_box("", "I ended up walking behind Kageyama. Rina was standing next to him, straightening her beret.\nShe leaned in close to him.\nI barely caught the whisper.", is_narrator=True)
    
    show_story_box("Nocturnal Companion Rina", "The ‘Boss’ didn’t like your report. What will you do now?", affiliation="Kiryoku Gakuen Fairy")
    
    show_story_box("", "I froze.\nWhat’s she talking about?", is_narrator=True)
    show_story_box("", "Kageyama didn’t flinch. He smiled—his usual, unreadable smile.", is_narrator=True)
    
    show_story_box("Kageyama", "...Ah! By ‘Boss’... you mean Aina-san, correct?", affiliation="Kasakura High School Student Council President / Seven Wonders")
    show_story_box("", "He spoke loud enough for me to hear.", is_narrator=True)
    show_story_box("Kageyama", "Haha, please assure her that all future documents will be routed directly through Treasurer Sumiko. And I’ll attach some premium candy for Aina-san next time.", affiliation="Kasakura High School Student Council President / Seven Wonders")
    
    show_story_box("", "Rina stared at him for a second. Then she stepped back.", is_narrator=True)
    show_story_box("Nocturnal Companion Rina", "…I see.", affiliation="Kiryoku Gakuen Fairy")
    
    show_story_box("", "My stomach tightened.\n‘Report’? ‘The Boss’?", is_narrator=True)
    show_story_box("", "Kageyama was playing dumb. And Rina… she knew something.", is_narrator=True)
    show_story_box("", "I looked at the President’s back.", is_narrator=True)
    show_story_box("", "Masayoshi-senpai was rubbing his chin, looking dazed. Yuri was chatting with Hana. Benikawa was poking a fake plant.\nEveryone was acting like it was over.", is_narrator=True)
    
    show_story_box("", "But as I looked at Kageyama, I remembered Kojima-sensei’s words.", is_narrator=True)
    show_story_box("", "\"I don’t really trust them. Any of them.\"", is_narrator=True)
    show_story_box("", "Something was wrong.", is_narrator=True)

def play_stage_3_8_story():
    # --- SCENE 1: KAGAKU'S POV (THE PRISON) ---
    show_story_box("", "********* ◆ *********\nKagaku’s POV", is_narrator=True)
    show_story_box("", "The early morning sun filtered through the high windows of my ‘prison’—casting long, golden bars of light across the expensive carpet.", is_narrator=True)
    show_story_box("", "I stretched, my spine popping in three different places.", is_narrator=True)
    
    show_story_box("Kagaku", "Nnngh… Surprisingly comfy.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I patted the red velvet sofa. Who knew captivity came with high-thread-count pillows? Usually, all-nighters involving the Parallaxis Scorer ended with me face-planting onto a desk covered in circuit boards and cold solder. This was… an upgrade, to say the least.", is_narrator=True)
    show_story_box("", "The heavy mahogany door clicked open.", is_narrator=True)
    show_story_box("", "I tensed immediately, scrambling to sit up, my mind racing through the lies I’d concocted overnight.", is_narrator=True)
    
    show_story_box("Kagaku", "What should I say first? ‘The crystal needs resonance.’ ‘The frequency is unstable.’ ‘I need a specific alloy.’...", affiliation="Kasakura High School Student / Seven Wonders", is_thought=True)
    
    show_story_box("", "But it wasn’t a new interrogator who walked in.", is_narrator=True)
    show_story_box("", "It was the sandy-coat guy again. The one with the rapier.\nHe didn’t have the weapon drawn. In fact, he was carrying… a silver tray?", is_narrator=True)
    show_story_box("", "He set it down on the low table in front of me with a soft clink.", is_narrator=True)
    
    show_story_box("Young Man", "Eat.", affiliation="Unknown Faction")
    
    show_story_box("", "I stared.", is_narrator=True)
    show_story_box("", "This is…Premium shrimp Alfredo pasta. Creamy sauce, perfectly cooked shrimp, a dusting of parsley. Beside it, a crisp Caesar salad with generous parmesan shavings and two slices of garlic bread, toasted golden-brown. A glass of iced orange juice sat sweating condensation next to the plate.", is_narrator=True)
    
    show_story_box("Kagaku", "Uh…", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "I looked up at him. His expression was as unreadable as ever.", is_narrator=True)
    
    show_story_box("Kagaku", "No morning torture session? No ‘tell me the secrets of the universe or die’?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "He turned to leave, hands in his pockets.", is_narrator=True)
    show_story_box("Young Man", "I extracted what I needed yesterday. The timeline is set. Three days. Until then, you are an asset to be maintained.", affiliation="Unknown Faction")
    
    show_story_box("Kagaku", "So… I’m a pet now?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "He paused at the door.", is_narrator=True)
    show_story_box("Young Man", "Call it what you want. Just have the anchor ready.", affiliation="Unknown Faction")
    show_story_box("", "He glanced back at the food.", is_narrator=True)
    show_story_box("Young Man", "And eat. I made it myself.", affiliation="Unknown Faction")
    
    show_story_box("", "The door clicked shut.\nSilence returned to the room.", is_narrator=True)
    show_story_box("", "I looked at the pasta. Then at the door. Then back at the pasta.", is_narrator=True)
    
    show_story_box("Kagaku", "He… cooked this?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "It smelled divine.", is_narrator=True)
    show_story_box("Kagaku", "I hesitated. Is it poisoned? Drugged?", affiliation="Kasakura High School Student / Seven Wonders", is_thought=True)
    show_story_box("", "I leaned in, sniffing. Garlic. Cream. Cheese. No bitter almond scent hinting cyanide. No odd chemical sweetness leading to arsenic. Visually consistent texture.", is_narrator=True)
    
    show_story_box("Kagaku", "Ughh…this is way too suspicious…", affiliation="Kasakura High School Student / Seven Wonders", is_thought=True)
    
    show_story_box("", "But my stomach growled—loudly.", is_narrator=True)
    show_story_box("Kagaku", "Well… scientific method requires testing.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I took a bite.\nMy eyes widened.", is_narrator=True)
    show_story_box("Kagaku", "Oh my god. That’s five-star restaurant quality.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I shoveled another forkful into my mouth. For a moment, I forgot I was a hostage of a mysterious, violent organization bent on stealing parallel universe powers. I was just a girl eating really, really good pasta.", is_narrator=True)
    show_story_box("", "But as the initial hunger faded, the reality settled back in.\nThree days, huh.", is_narrator=True)
    show_story_box("", "I checked the crystal in my pocket—still dull.\nThe message.\n‘Help is coming.’", is_narrator=True)
    show_story_box("", "I took a sip of orange juice.", is_narrator=True)
    
    show_story_box("Kagaku", "Akasuke… everyone… please hurry. This guy cooks great, but he’s definitely going to kill me later.", affiliation="Kasakura High School Student / Seven Wonders")

    # --- SCENE 2: YURI'S POV (FLASHFORWARD/THE RAIN) ---
    show_story_box("", "********* ◆ *********\nYuri’s POV", is_narrator=True)
    
    show_story_box("Yuri", "Akasuke-kun! Wake up!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Yuri", "Please…wake up.", affiliation="Kasakura High School Student / Seven Wonders", is_thought=True)
    
    show_story_box("", "The downpour showed no mercy, each droplet hammerin’ into the pavement and bouncin’ off his body. His red hair stuck flat against his forehead, the eyepatch over his left eye soaked through, the black tie around his neck limp like it had given up too.", is_narrator=True)
    show_story_box("", "I dropped to my knees beside him, water splashin’ up around us. My hands grabbed his collar, clenchin’ so hard that all ten of my fingers turned bone-white. They trembled uncontrollably, but I couldn’t let go.", is_narrator=True)
    show_story_box("", "Not like this.", is_narrator=True)
    show_story_box("", "His skin felt cold under my touch. My breath hitched as I shook him again and again, droplets of rain mixin’ with the tears already fallin’ down my face.", is_narrator=True)
    
    show_story_box("Yuri", "Please, Akasuke-kun…ya can’t leave me like this…", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Lightning tore across the sky, the thunder that followed rattlin’ my bones. For a moment, the whole world lit up — his face pale, lips slightly parted.", is_narrator=True)
    show_story_box("", "My heart screamed.", is_narrator=True)
    show_story_box("", "I called out to him, my voice breakin’, raw from shoutin’ his name over and over.", is_narrator=True)
    
    show_story_box("Yuri", "I can’t let him die like this…", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Yuri", "Not when I…not when we—", affiliation="Kasakura High School Student / Seven Wonders", is_thought=True)

    # --- SCENE 3: AKASUKE'S POV (3 DAYS AGO) ---
    show_story_box("", "********* ◆ *********\nThree days ago\nAkasuke’s POV", is_narrator=True)
    
    show_story_box("Classmate", "Woah…it’s huge…", affiliation="Kasakura High School Student")
    
    show_story_box("", "In front of us was our school’s private cruise ship. A midsized vessel gleaming under the sun, able to carry close to 2,000 people.", is_narrator=True)
    show_story_box("", "Perfect for hosting second-year students from four schools—plus one unlucky teacher tasked with babysitting all of us.", is_narrator=True)
    
    show_story_box("Kojima-sensei", "Listen up, brats!", affiliation="Kasakura High School Teacher")
    
    show_story_box("", "The familiar shout of Kojima-sensei echoed across the deck, cutting through the chattering voices of hundreds of students.", is_narrator=True)
    show_story_box("", "The man stood near the ship’s railing with a rolled-up stack of papers in his hand like a makeshift baton. Even in the sea breeze that whipped our hair and uniform, his voice still carried clear.", is_narrator=True)
    
    show_story_box("Kojima-sensei", "I’m Kojima Takeshi, your teacher, your caretaker, and unfortunately, your jailer for this entire trip.", affiliation="Kasakura High School Teacher")
    show_story_box("", "He adjusted his glasses, eyeing the restless crowd like a general sizing up an undisciplined army.", is_narrator=True)
    show_story_box("Kojima-sensei", "If any of you think this is a vacation, you’d better change your mind right now.", affiliation="Kasakura High School Teacher")
    show_story_box("Kojima-sensei", "This is a school trip that the four schools went out of their way to reinstate together, which took a miracle! Learn something, don’t cause trouble, and if you fall overboard, don’t expect me to jump in after you.", affiliation="Kasakura High School Teacher")
    
    show_story_box("", "That earned a few laughs from other schools as if he was cracking a joke. But any students from our school know that he wasn’t kidding, if we do fall, he would just leave us.", is_narrator=True)
    
    show_story_box("Kojima-sensei", "Here’s how we’re going to do things. You’re all getting on this cruise ship in line. If I see someone being off the line even for just one centimeter, they’ll be helping me out with charity work.", affiliation="Kasakura High School Teacher")
    show_story_box("", "He then proceeded to pull out a whiteboard out of nowhere and placed it beside him.", is_narrator=True)
    show_story_box("Kojima-sensei", "See this? This is your schedule. Once you all get on the ship, you’ll be given a full day free time. And when we get on the island the next day, we’ll be grouping.", affiliation="Kasakura High School Teacher")
    show_story_box("Kojima-sensei", "You will not—I repeat, not—spend the entire time huddled with only your little buddies. That defeats the purpose of this exchange. To avoid that, all of you will be assigned into groups of four.", affiliation="Kasakura High School Teacher")
    
    show_story_box("", "Groans erupted immediately. The students from our school weren't shy about expressing their displeasure, and judging by the expressions of the other schools, they weren’t any happier either.", is_narrator=True)
    show_story_box("", "Kojima-sensei smacked the papers against the railing, the crack sharp enough to silence most of the noise.", is_narrator=True)
    
    show_story_box("Kojima-sensei", "Each group of four will consist of students from different schools. That means one student from Kasakura, one from Heiwa Seiritsu, one from Kiryoku Gakuen and one from Miyabi Academy.", affiliation="Kasakura High School Teacher")
    show_story_box("Kojima-sensei", "This isn’t negotiable. You’ll be working, eating, and doing activities together. Consider this your chance to build bridges or at least to not kill each other.", affiliation="Kasakura High School Teacher")
    
    show_story_box("", "Well…that made sense. One small problem, though, people didn’t seem to be happy about it. Some of our guys narrowed their eyes at Heiwa Seiritsu’s uniforms.", is_narrator=True)
    show_story_box("", "The ones from Kiryoku had their arms crossed, looking smug. Miyabi, as always, just smiled politely like they were too good for this nonsense.", is_narrator=True)
    show_story_box("", "In the end, we are just students attending our own schools. I don’t see the point in all this hostility, honestly.", is_narrator=True)
    show_story_box("", "But then again, I didn’t know what went down with these four schools in the past. Neither do they.", is_narrator=True)
    
    show_story_box("Kojima-sensei", "Alright, I’ll call you all by your school. Remember, line up properly.", affiliation="Kasakura High School Teacher")
    
    show_story_box("", "After what felt like forever, we all finally got on the ship. Well, not all. Some Heiwa Seiritsu students got caught by Kojima-sensei and were now in a scolding session down at the dock. Poor fellas.", is_narrator=True)
    show_story_box("", "Anyway…I don’t know how many times I had to stress this, but the ship was really huge. Huge enough to host all 1,200 of us.", is_narrator=True)
    show_story_box("", "We had a whole day ahead of us. Let’s make use of it.", is_narrator=True)

    # --- SCENE 4: YURI'S POV (CRUISE SHIP DECK) ---
    show_story_box("", "********* ◆ *********\nYuri’s POV", is_narrator=True)
    show_story_box("", "We were now in the middle of the ocean.", is_narrator=True)
    show_story_box("", "The view was surreal, there was water everywhere we could see. This was the first time I’d been on a cruise ship so I was pretty excited.", is_narrator=True)
    
    show_story_box("Yuri", "Akasuke-kun, this is amazin’!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Akasuke", "Yeah, it really is. I want to take a picture of this and set it as my wallpaper.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Yuri", "Ah! Talk ‘bout pictures. How ‘bout a selfie?", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Akasuke", "Hm? Yeah, sure, why not?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I grabbed my phone out of my pocket and lifted the arm holdin’ it up in the air.", is_narrator=True)
    
    show_story_box("Yuri", "Alright, do a pose or somethin’! Don’t just stand there like a statue!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "Akasuke-kun just smiled and did a little peace sign. I did the same thing. Hehe…I’m gonna set this as my lock screen.", is_narrator=True)
    
    show_story_box("Yuri", "So…any plan? We basically got a whole day of explorin’ to ourselves.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Akasuke", "Hm…I’m not too sure. I guess I’ll just walk around and see what this place has to offer.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Yuri", "Yeah. Same thought. Wanna walk together then?", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Akasuke", "Yeah. I was about to ask the same thing.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "We smiled at each other and took off.", is_narrator=True)
    show_story_box("", "We started walkin’, shoulder to shoulder, the salty breeze hittin’ our faces. The deck was wide enough to host a marathon, with fancy chairs neatly lined up and a glass railin’ givin’ us a clear view of the ocean stretchin’ into infinity.", is_narrator=True)
    show_story_box("", "Students from the other schools were around too, some takin’ photos, some whisperin’, some already lookin’ like they were plannin’ trouble. Hope they don’t try anythin’.", is_narrator=True)
    
    show_story_box("", "Akasuke-kun suddenly stopped walkin’.", is_narrator=True)
    show_story_box("Yuri", "Hm? Somethin’ wrong?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "He was starin’ at the horizon, brows furrowed slightly. Not in a brooding way…but in that “I am thinkin’ too much” kinda way he always gets when he tries to hide his worries from me.", is_narrator=True)
    
    show_story_box("Yuri", "Ya okay?", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Akasuke", "Yeah.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "But that smile…it wasn’t his real one.", is_narrator=True)
    
    show_story_box("Akasuke", "Just thinking about…things. Security. The Four Schools situation. Potential threats...then the 'knight', and all that stuff around Kokoros and Katas.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "Of course. He’d always do that. Shoulders tense, eyes on alert. Always protectin’, even when it wasn’t his responsibility. Not his alone anyway.", is_narrator=True)
    
    show_story_box("", "I grabbed his hand.\nNot too tight. Just enough for him to feel I was there.", is_narrator=True)
    
    show_story_box("Yuri", "Hey. It’s a school trip. Relax a bit, okay? I’m here too. We got our friends, our Wonders seniors, and the disciplinary team. Nothin’s gonna happen.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "He blinked, looked at our hands, then at me.", is_narrator=True)
    show_story_box("Akasuke", "…Right.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "He exhaled, tension softenin’.", is_narrator=True)
    show_story_box("Akasuke", "Sorry. Habit.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Yuri", "Heh~ You can apologize by buyin’ me ice cream later.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Akasuke", "Oh? Is that extortion?", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Yuri", "Nope! It’s called friendship tax.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "He chuckled softly. That was better. That was him.", is_narrator=True)
    show_story_box("", "We kept walkin’, passin’ groups of students. Some from Heiwa Seiritsu glanced at us and whispered, and I resisted the urge to glare back. Not worth the drama.", is_narrator=True)
    show_story_box("", "We eventually stopped at the outdoor snack bar. A soft jingle played as we got closer, and the smell of baked pastries and soft serve hit us.", is_narrator=True)
    
    show_story_box("Akasuke", "Two vanilla cones, please.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Yuri", "H-Huh? I didn’t even remind ya.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Akasuke", "You were going to.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Yuri", "…True.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "We grabbed our cones and walked to the railin’ again. The ship hummed beneath us, the ocean glistenin’ like crushed diamonds. For a moment, everything felt perfect.", is_narrator=True)
    show_story_box("", "Then—\nTap tap.", is_narrator=True)
    
    show_story_box("", "I turned to see a guy from Heiwa Seiritsu tappin’ Akasuke-kun’s shoulder with a smug grin. Blue streaks hair, jacket slung over one shoulder like he practiced that pose every mornin’.", is_narrator=True)
    
    show_story_box("Heiwa Student", "Yer that Kasakura guy, right?", affiliation="Heiwa Seiritsu High School Student")
    show_story_box("", "Akasuke-kun licked his ice cream calmly.", is_narrator=True)
    show_story_box("Akasuke", "...Yeah?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Heiwa Student", "Heh. Thought so. Yer the karate freak. Wanna spar sometime? Heard yer tough. Let’s see if that’s real.", affiliation="Heiwa Seiritsu High School Student")
    show_story_box("", "I narrowed my eyes.", is_narrator=True)
    show_story_box("Yuri", "Can ya not pick fights on a school trip?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "He ignored me completely.", is_narrator=True)
    show_story_box("Heiwa Student", "Or are those rumors exaggerated, hm?", affiliation="Heiwa Seiritsu High School Student")
    
    show_story_box("", "Akasuke-kun didn’t react. Didn’t even blink.", is_narrator=True)
    show_story_box("Akasuke", "I’m on vacation.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "The guy clicked his tongue.", is_narrator=True)
    show_story_box("Heiwa Student", "Tch. Figures. Kasakura’s ‘Wonder’ is all talk.", affiliation="Heiwa Seiritsu High School Student")
    
    show_story_box("", "Akasuke-kun just kept eatin’. Not givin’ him what he wanted.", is_narrator=True)
    show_story_box("", "I admired that. Really did.\nThat didn’t mean I could let it slide.", is_narrator=True)
    show_story_box("", "I walked right up to the guy, leaned forward, and whispered—", is_narrator=True)
    
    show_story_box("Yuri", "One more word, and I’ll fold ya like clean laundry.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "He froze.\nThen he backed off, muttering somethin’ under his breath as he walked away fast.", is_narrator=True)
    
    show_story_box("", "Akasuke-kun blinked at me.", is_narrator=True)
    show_story_box("Akasuke", "…Laundry?", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Yuri", "Shut up.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "He snorted, almost droppin’ his ice cream.", is_narrator=True)
    show_story_box("Akasuke", "That was cute.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Yuri", "IT WASN’T CUTE!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "He laughed harder. I tried to be mad but…hearin’ him laugh like that made my chest warm.", is_narrator=True)
    
    show_story_box("Akasuke", "C’mon, let’s go see the arcade next.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Yuri", "Yeah.", affiliation="Kasakura High School Student / Seven Wonders")

def play_stage_3_9_start():
    # --- SCENE 1: AKASUKE'S POV (THE LOUNGE) ---
    show_story_box("", "********* ◆ *********\nAkasuke’s POV", is_narrator=True)
    show_story_box("", "The ship’s lounge was surprisingly quiet, save for the hum of the engine and the occasional turn of a page.", is_narrator=True)
    show_story_box("", "While Yuri and the girls went off to do… whatever girls do on a luxury cruise, I was stuck here.", is_narrator=True)
    show_story_box("", "I sat on a plush leather chair, watching Nishida hunch over a table covered in wires, screws, and microchips.", is_narrator=True)
    
    show_story_box("Akasuke", "How long are you going to fiddle with that thing, Nishida?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Nishida didn’t look up. He adjusted his goggles, tweaking a tiny screw with a precision screwdriver.", is_narrator=True)
    show_story_box("Nishida", "As long as it takes to finish it.", affiliation="Kasakura High School Student")
    
    show_story_box("Akasuke", "We’re on a cruise ship. Sun. Ocean. All-you-can-eat buffets. And you’re doing engineering?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Shigemura, lying on the couch opposite us with a thick hardcover book, flipped a page without breaking rhythm.", is_narrator=True)
    show_story_box("Shigemura", "Let him be. He’s been obsessing over this particular project for weeks. It better be good.", affiliation="Kasakura High School Student")
    
    show_story_box("", "Nishida finally looked up, a manic grin spreading across his face.", is_narrator=True)
    show_story_box("Nishida", "Good? Oh, Shigemura. It’ll be a masterpiece. I’m telling you… this baby is going to change the game.", affiliation="Kasakura High School Student")

    # --- SCENE 2: NAGANOHARA'S POV (SHOPPING AREA) ---
    show_story_box("", "********* ◆ *********\nNaganohara’s POV", is_narrator=True)
    show_story_box("", "“It’s Shanel! Mermes! Vouis Luitton!”", is_narrator=True)
    show_story_box("", "I ran down the hallway, pressing my face against the glass display of every luxury store we passed.", is_narrator=True)
    
    show_story_box("Naganohara", "Look at that bag! It sparkles! It’s calling my name!", affiliation="Kasakura High School Student")
    show_story_box("", "Behind me, Yamashita laughed.", is_narrator=True)
    show_story_box("Yamashita", "It’s calling your wallet, Naganohara. And your wallet is saying ‘please, no’.", affiliation="Kasakura High School Student")
    
    show_story_box("", "I pouted, turning back to them.", is_narrator=True)
    show_story_box("Naganohara", "But looking is free~! Right, Yuri-chan?", affiliation="Kasakura High School Student")
    
    show_story_box("", "Yuri-chan was walking a few steps behind, looking at the brand names with a confused expression.", is_narrator=True)
    show_story_box("Yuri", "I don’t get it. Why does a purse cost as much as a used car? Does it cook dinner for ya?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I giggled. Classic Yuri-chan.", is_narrator=True)
    show_story_box("Naganohara", "It’s about the status, Yuri-chan! The vibes!", affiliation="Kasakura High School Student")
    
    show_story_box("", "I skipped over to her, hooking my arm through hers.", is_narrator=True)
    show_story_box("Naganohara", "Speaking of vibes… how’s the progress?", affiliation="Kasakura High School Student")
    
    show_story_box("", "Yuri blinked.", is_narrator=True)
    show_story_box("Yuri", "...Progress?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Yamashita grinned, leaning in from the other side.", is_narrator=True)
    show_story_box("Yamashita", "You know. Him. The eyepatch. The red coat. The guy you were totally flirting with on the deck earlier. Akasuke-kun~.", affiliation="Kasakura High School Student")
    
    show_story_box("", "Yuri’s face went fifty shades of red instantly.", is_narrator=True)
    show_story_box("Yuri", "W-We weren’t flirtin’! We were just eatin’ ice cream!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Naganohara", "That’s basically a date! So? Did he say anything? Did you make a move?", affiliation="Kasakura High School Student")
    
    show_story_box("", "Yuri looked away, her expression dimming slightly. She kicked at the carpet.", is_narrator=True)
    show_story_box("Yuri", "...Not yet. It’s… complicated right now.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "She rubbed her arm, looking troubled.", is_narrator=True)
    show_story_box("Yuri", "With the ‘Knight’ appearin’… and our hearts… and the Katas… I feel like it ain’t the right time to push for romance. We gotta survive first, ya know? Haha.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "The mood dipped. I saw the worry in her eyes.\nI exchanged a look with Yamashita.\nNope! No sad faces allowed on the trip!", is_narrator=True)
    show_story_box("", "I slapped Yuri on the back—gently, because she’s made of steel and I’d break my hand.", is_narrator=True)
    
    show_story_box("Naganohara", "Okay! Retreat! Strategic retreat on the romance topic!", affiliation="Kasakura High School Student")
    show_story_box("Yamashita", "Agreed. Heavy stuff is banned for the next hour.", affiliation="Kasakura High School Student")
    
    show_story_box("", "I pointed down the hall.", is_narrator=True)
    show_story_box("Naganohara", "I saw a cafe that serves pancakes stacked as high as a tower. We’re going there. We’re eating them. And we are forgetting about knights and hearts and all that!!", affiliation="Kasakura High School Student")
    
    show_story_box("", "Yuri blinked, then smiled—a real one this time.", is_narrator=True)
    show_story_box("Yuri", "‘Pancakes’ does sound good.", affiliation="Kasakura High School Student / Seven Wonders")

    # --- SCENE 3: BENIKAWA'S POV (THE OBSERVATION DECK) ---
    show_story_box("", "********* ◆ *********\nBenikawa’s POV", is_narrator=True)
    show_story_box("", "The wind up here was refreshing and strong, whipping my orange tie around like a streamer.", is_narrator=True)
    show_story_box("", "I stood on the highest vantage point of the deck, arms crossed, scanning the crowd below.", is_narrator=True)
    show_story_box("", "For once, I wasn’t in my usual loose, comfortable gear, even though I wanted to run it. White shirt, sleeves tucked back perfectly today. Black trousers pressed. Hair tied back so tight it felt like a facelift.", is_narrator=True)
    
    show_story_box("Benikawa", "Ugh. Modern formal wear. The ninja’s natural enemy.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "But orders were orders.", is_narrator=True)
    show_story_box("", "Below me, the VIPs were lounging.\nKojima-sensei was drinking something that looked suspiciously like a mojito. Next to him was Takai-sensei from Heiwa Seiritsu.", is_narrator=True)
    show_story_box("", "If I didn’t know better, I’d think Takai-sensei was a middle schooler who got lost. He was tiny. But the man was a legend in Heiwa.", is_narrator=True)
    show_story_box("", "Staff members bustled around them, carrying trays.\nBeep.\nA sharp sound in my right ear.", is_narrator=True)
    
    show_story_box("Natsume", "Benikawa. Status report.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Benikawa", "Status is ‘bored out of my mind’. The VIPs are safe. Takai-sensei is ordering another juice.", affiliation="Benikawa Ninja Clan")
    show_story_box("Natsume", "Cut the chatter. On my side, I’m tracking suspicious signal interference. Lower decks. Sector 4.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I sighed, tapping the earbud.", is_narrator=True)
    show_story_box("Benikawa", "Natsume-san, we’re, like, on a whole cruise. Can’t a girl enjoy the sun?", affiliation="Benikawa Ninja Clan")
    show_story_box("Natsume", "There are unlisted bio-signatures moving in staff-only areas. Proceed with caution. The enemy could be anyone. Heiwa. Kiryoku. Or even Kasakura.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "My eyes narrowed.\nOkay. Now I’m interested.", is_narrator=True)
    show_story_box("Benikawa", "Roger that~. Going dark.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "I slipped away from the railing and headed for the service stairs.", is_narrator=True)
    show_story_box("", "The lower decks were a different world.\nNo luxury carpets here. Just steel grating, pipes hissing steam, and the overwhelming smell of oil and rust.", is_narrator=True)
    
    show_story_box("Benikawa", "Great. This is going to stick to my uniform.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "I walked deeper into the machinery room. Shadows stretched long and flickering.\nThen, I saw them.", is_narrator=True)
    show_story_box("", "Five guys. Heiwa Seiritsu uniforms. Field trip issued armbands on. They were messing with a pressure valve.", is_narrator=True)
    
    show_story_box("Benikawa", "The usual suspects, eh~?", affiliation="Benikawa Ninja Clan")
    show_story_box("", "They spun around.", is_narrator=True)
    
    show_story_box("Goons", "K-K-Kasakura?!", affiliation="Heiwa Seiritsu High School Student")
    show_story_box("Benikawa", "You boys look lost~. The buffet is upstairs.", affiliation="Benikawa Ninja Clan")

def play_stage_3_9_end():
    # --- SCENE 4: BENIKAWA'S POV (THE AMBUSH) ---
    show_story_box("", "They didn’t talk. They just rushed me, shouting and grunting throughout the fight.\nToo slow.", is_narrator=True)
    show_story_box("", "I ducked a punch, swept the first guy’s legs, and palmed the second guy in the solar plexus.", is_narrator=True)
    
    show_story_box("Benikawa", "Boring.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "I grabbed the third guy’s wrist, twisting it until he yelped, and shoved him into the fourth.\nWithin thirty seconds, four of them were groaning on the metal grate.", is_narrator=True)
    
    show_story_box("Benikawa", "Is that it? Seriously?", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "I sensed it a split second before it happened.\nAir displacement. Behind me.\nWhoosh.", is_narrator=True)
    show_story_box("", "I dropped low—instinct taking over. A metal bat swung through the space where my head just was.", is_narrator=True)
    
    show_story_box("Benikawa", "Woah!", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "I spun on my heel, launching a kick upward. It connected with the assailant’s stomach, sending them skidding back.", is_narrator=True)
    show_story_box("", "I stood up, dusting off my hands.", is_narrator=True)
    
    show_story_box("Benikawa", "Nice swing. But you forgot to hide your breathing—", affiliation="Benikawa Ninja Clan")
    show_story_box("", "I froze.", is_narrator=True)
    
    show_story_box("", "The attacker wasn’t Heiwa.\nShe was wearing a Kiryoku Gakuen athletic uniform.", is_narrator=True)
    show_story_box("Benikawa", "Ohh..? Kiryoku? What are you doing down here with these guys?", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "She didn’t answer. She just raised her bat again. Frustrated.", is_narrator=True)
    show_story_box("", "And then, from the shadows, more stepped out.\nSix Heiwa thugs. Three more Kiryoku girls.", is_narrator=True)
    
    show_story_box("Benikawa", "...Okay. That’s a lot.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Natsume", "Benikawa. Heart rates are spiking all around you. You’re outnumbered.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Benikawa", "Tell me something I don’t know!", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "I dodged another swing, parried a punch, and backflipped onto a catwalk.", is_narrator=True)
    
    show_story_box("Natsume", "Escape route has been calculated. Maintenance hatch to your left. Go. Now.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Benikawa", "Roger!", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "I sprinted, sliding under a pipe and kicking the hatch open. I scrambled through just as a wrench clanged against the metal frame behind me.", is_narrator=True)

    # --- SCENE 5: UPPER DECK ---
    show_story_box("", "Upper Deck Hallway – Staff Quarters\nI leaned against the wall, catching my breath.", is_narrator=True)
    
    show_story_box("Benikawa", "What a mess. Heiwa and Kiryoku…thugs? Working together below decks? This reeks of a setup.", affiliation="Benikawa Ninja Clan")
    show_story_box("Natsume", "Agreed. Regroup with Akasuke and the others. We need to clear them out before they sabotage the ship.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Benikawa", "On it. My fighting spirit is finally awake.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "I straightened my tie and stepped out into the main corridor.", is_narrator=True)
    show_story_box("", "Then three students happened to walk past me.\nThey wore Kasakura High uniforms. Boys. Walking casually.", is_narrator=True)
    show_story_box("", "But they didn’t look at each other. They didn’t talk. Their eyes were scanning the exits, the cameras, the blind spots.", is_narrator=True)
    show_story_box("", "Their footsteps were silent. Perfectly synchronized.", is_narrator=True)
    
    show_story_box("", "I stopped.\nMy skin crawled. A specific kind of chill that only hits you when you recognize your own kind.", is_narrator=True)
    
    show_story_box("Natsume", "Benikawa? Why did you stop?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I watched them disappear around the corner.", is_narrator=True)
    
    show_story_box("Benikawa", "...Natsume. We have a bigger problem.", affiliation="Benikawa Ninja Clan")
    show_story_box("Natsume", "Explain.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Benikawa", "I just passed three students. Kasakura uniforms.", affiliation="Benikawa Ninja Clan")
    show_story_box("Benikawa", "They’re Ninjas.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "Silence on the line.", is_narrator=True)
    
    show_story_box("Benikawa", "Not just trained fighters. Ninjas. I can tell. The walk. The gaze. They’re active.", affiliation="Benikawa Ninja Clan")
    show_story_box("Benikawa", "The enemy isn’t just outside. They’re already inside Kasakura.", affiliation="Benikawa Ninja Clan")

def play_stage_3_10_start():
    # --- SCENE 1: AKASUKE'S POV (NIGHT ON THE DECK) ---
    show_story_box("", "********* ◆ *********\nAkasuke’s POV", is_narrator=True)
    show_story_box("", "Night had fallen over the ocean. The cruise ship was a beacon of light in the endless dark, humming with the energy of over a thousand students.", is_narrator=True)
    show_story_box("", "Kojima-sensei stood on the main stage of the deck, microphone in hand.", is_narrator=True)
    
    show_story_box("Kojima-sensei", "Alright, listen up. You have two more hours. The facilities are open—arcade, pool, buffet. But at 22:00 sharp, you are in your cabins. Lights out.", affiliation="Kasakura High School Teacher")
    show_story_box("", "He glared at the crowd.", is_narrator=True)
    show_story_box("Kojima-sensei", "And if I catch anyone causing trouble, jumping off the side, or trying to reenact scenes from ‘Gigantic’…you’re scrubbing toilets until graduation. Dismissed.", affiliation="Kasakura High School Teacher")
    
    show_story_box("", "A cheer went up, and the students scattered like ants finding sugar.", is_narrator=True)
    show_story_box("", "I turned to Nishida, who was—predictably—still soldering something at a table.", is_narrator=True)
    
    show_story_box("Akasuke", "Hey, Nishida. Shigemura and I are gonna go help Kojima-sensei… uh, clean the decks. You good here?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Nishida didn’t even look up.", is_narrator=True)
    show_story_box("Nishida", "Yeah, yeah. Just don’t touch my wires.", affiliation="Kasakura High School Student")
    
    show_story_box("", "We walked away. Once we were out of earshot, Shigemura closed his book.", is_narrator=True)
    
    show_story_box("Shigemura", "‘Cleaning the decks’? That’s the best you could come up with?", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Eh? It worked, didn’t it?", affiliation="Kasakura High School Student / Seven Wonders")

    # --- SCENE 2: VIP LOUNGE BRIEFING ---
    show_story_box("", "We headed for the VIP lounge—restricted access.\nInside, the atmosphere was heavy.", is_narrator=True)
    
    show_story_box("", "Yuri and Benikawa were already there, dressed in formal Kasakura gear—white shirts, black trousers, ties. They looked sharp.", is_narrator=True)
    show_story_box("", "On the table, a tablet was propped up. Natsume’s face filled the screen. She was wrapped in two fluffy blankets, looking like a tech-savvy burrito.", is_narrator=True)
    
    show_story_box("Natsume", "...took you long enough. It’s cold in the server room.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I looked at Benikawa, then at Shigemura.", is_narrator=True)
    show_story_box("Akasuke", "Benikawa. Are you sure about this? Shigemura is… well, Shigemura. He’s not a fighter. He doesn’t have to do this.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Benikawa", "Like I said. He’ll be fine.", affiliation="Benikawa Ninja Clan")
    show_story_box("", "Her voice was firm. Absolute.", is_narrator=True)
    show_story_box("Benikawa", "Trust me. He’s more capable than he looks. Absolutely fine.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "Shigemura clicked his tongue, looking annoyed.", is_narrator=True)
    show_story_box("Shigemura", "Stop overselling it…I’m just observant.", affiliation="Kasakura High School Student")
    
    show_story_box("", "He turned to me, his expression humble again.", is_narrator=True)
    show_story_box("Shigemura", "I’ll cover your blind spots, Akasuke. Just… if we find an opponent too strong, please protect me. I am just a bookworm, after all.", affiliation="Kasakura High School Student")
    
    show_story_box("", "I sighed, smiling.", is_narrator=True)
    show_story_box("Akasuke", "Yeah. I got you.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Kojima-sensei walked in, closing the blinds.", is_narrator=True)
    show_story_box("Kojima-sensei", "Good. We’re all here. Natsume, sitrep.", affiliation="Kasakura High School Teacher")
    
    show_story_box("Natsume", "I’ve scanned the ship’s bio-signatures. We have infiltrators. Estimate… fifty plus.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Yuri", "Fifty?! That’s a small army!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Natsume", "Uniforms match Kasakura, Heiwa Seiritsu, and Kiryoku Gakuen.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Yuri", "Uhh…wait. What about Miyabi Academy? The fourth school?", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "Natsume sighed, shifting in her blankets.", is_narrator=True)
    show_story_box("Natsume", "Zero. Miyabi is… clean. For now.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Akasuke", "Clean? Or just better at hiding?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Natsume", "Likely just clean. Listen, Miyabi Academy is… different. They’re too goddamn powerful to care about petty turf wars.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Kojima-sensei nodded.", is_narrator=True)
    show_story_box("Kojima-sensei", "Miyabi is the ‘Paradise’ of this district. Highest grades. Endless funding. Elites only. They have no bad blood with anyone because no one is stupid enough to pick a fight with them.", affiliation="Kasakura High School Teacher")
    
    show_story_box("Natsume", "Their internal structure is a black box. Despite being ‘close partners’, we know nothing about them. Do they have a Student Council? A Disciplinary Committee? Who knows. But rumors say they can be monsters on par with Heiwa’s ‘Upperclassmen’ and our Seven Wonders…maybe even stronger.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Natsume", "They helped supply us during a great raid, also from Heiwa years ago, but they never got involved directly. They sit on their throne and watch. So, forget Miyabi. Focus on the other three.", affiliation="Kasakura High School Student / Seven Wonders")

    # --- SCENE 3: THE NINJA DILEMMA ---
    show_story_box("", "Kojima-sensei turned to Benikawa.", is_narrator=True)
    show_story_box("Kojima-sensei", "Now. The Ninjas.", affiliation="Kasakura High School Teacher")
    
    show_story_box("", "I stepped forward.", is_narrator=True)
    show_story_box("Akasuke", "Benikawa saw three of them. Kasakura uniforms. If they’re onboard, we need to know who they are.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "I looked at Natsume.", is_narrator=True)
    show_story_box("Akasuke", "Pull up the student database. Benikawa can point them out.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Benikawa", "No.", affiliation="Benikawa Ninja Clan")
    show_story_box("", "I blinked.", is_narrator=True)
    show_story_box("Akasuke", "What?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Benikawa", "I can’t. If I show you three faces at once… you’ll see the pattern. You’ll realize the ‘tell’. The method we use to identify each other.", affiliation="Benikawa Ninja Clan")
    show_story_box("", "She looked down.", is_narrator=True)
    show_story_box("Benikawa", "That violates the Code. I can’t risk the clan branding me.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Akasuke", "Benikawa, people’s lives are at stake.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Benikawa", "I know! But—", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "Kojima-sensei raised his hand.", is_narrator=True)
    show_story_box("Kojima-sensei", "Enough. Benikawa, compromise. If the group encounters one of them directly… you point them out then. Deal?", affiliation="Kasakura High School Teacher")
    
    show_story_box("", "Benikawa hesitated.", is_narrator=True)
    show_story_box("Benikawa", "…Deal. One at a time is fine.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Kojima-sensei", "Alright. Everyone, go get changed. Meet at the Staff Sector entrance in ten minutes.", affiliation="Kasakura High School Teacher")
    show_story_box("", "We filed out.\nI lingered for a second near the door, waiting for Shigemura.", is_narrator=True)

    # --- SCENE 4: KOJIMA AND BENIKAWA ---
    show_story_box("", "Inside, Kojima-sensei walked up to Benikawa. His voice was low, soft.", is_narrator=True)
    show_story_box("Kojima-sensei", "Don’t beat yourself up, kid.", affiliation="Kasakura High School Teacher")
    
    show_story_box("", "Benikawa looked at him, surprised.", is_narrator=True)
    show_story_box("Kojima-sensei", "I had a friend once. A ninja, too. ‘Long time ago. He broke the code to help me out of a bind. Revealed the secret.", affiliation="Kasakura High School Teacher")
    
    show_story_box("Benikawa", "...What happened to him?", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Kojima-sensei", "You already know. Branded an ‘Ibara’. A thorn. An outcast. He suffered for it. I won’t ask you, a kid, to make that same sacrifice.", affiliation="Kasakura High School Teacher")
    show_story_box("Kojima-sensei", "Yeah, I know the ‘tell’. But out of respect for him… I keep my mouth shut too.", affiliation="Kasakura High School Teacher")
    
    show_story_box("", "Benikawa stared at him, eyes wide.", is_narrator=True)
    show_story_box("Benikawa", "Sensei… you…?", affiliation="Benikawa Ninja Clan")
    show_story_box("Kojima-sensei", "Go. Protect your friends.", affiliation="Kasakura High School Teacher")
    
    show_story_box("", "She paused, then nodded, a new fire in her eyes, and ran past me.", is_narrator=True)

    # --- SCENE 5: THE DESCENT ---
    show_story_box("", "Two Hours Later – Staff Sector Entrance\nThe ship was silent.", is_narrator=True)
    show_story_box("", "We stood in the dim light of the service corridor. I adjusted my black tie. Shigemura was checking his gloves. Yuri was stretching. Benikawa was tapping her earpiece.", is_narrator=True)
    show_story_box("", "We were all in matching formal wear. It felt… official.", is_narrator=True)
    
    show_story_box("", "Kojima-sensei leaned against the bulkhead.", is_narrator=True)
    show_story_box("Kojima-sensei", "Remember. Stealth first. If that fails… hit hard and fast.", affiliation="Kasakura High School Teacher")
    
    show_story_box("Akasuke", "Sensei. Are you sure you’ll be okay up here? All the fighters are going down.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "He smirked.", is_narrator=True)
    show_story_box("Kojima-sensei", "Don’t worry about the VIPs. I know some self-defense here and there.", affiliation="Kasakura High School Teacher")
    show_story_box("Kojima-sensei", "Plus, the school hired some small-time bodyguards to watch the upper decks. We’re covered. Go.", affiliation="Kasakura High School Teacher")
    
    show_story_box("", "I nodded.", is_narrator=True)
    show_story_box("Akasuke", "Let’s move.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "We descended into the belly of the ship.\nThe air grew hotter. The smell of oil stronger.", is_narrator=True)
    
    show_story_box("Natsume", "Contacts. Straight ahead. Two Heiwa, one Kiryoku.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "We turned the corner.\nThey were there—standing guard by a pressure valve.", is_narrator=True)
    
    show_story_box("Akasuke", "Yuri. Left.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Yuri", "Got it!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Akasuke", "Benikawa. Right.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Benikawa", "Too easy.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Akasuke", "Shigemura. Stay behind me.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Shigemura", "With pleasure.", affiliation="Kasakura High School Student")
    
    show_story_box("", "We rushed them.", is_narrator=True)

def play_stage_3_11_start():
    # --- SCENE 1: SHIGEMURA'S POV (THE CORRIDOR) ---
    show_story_box("", "********* ◆ *********\nShigemura’s POV", is_narrator=True)
    show_story_box("", "The maintenance corridor was a blur of motion.\nAkasuke, Yuri, and Benikawa were an unstoppable force. Frontline decimation.", is_narrator=True)
    show_story_box("", "Heiwa thugs and Kiryoku athletes dropped like flies before they could even finish their war cries.", is_narrator=True)
    show_story_box("", "I stayed back, as promised.", is_narrator=True)
    
    show_story_box("Shigemura", "Right flank clear. Left flank… clear.", affiliation="Kasakura High School Student")
    show_story_box("", "I adjusted my clothes, stepping over an unconscious delinquent.", is_narrator=True)
    show_story_box("", "My job was simple: watch their backs. And so far, I hadn’t needed to lift a finger.", is_narrator=True)
    
    show_story_box("", "Through the earpiece, Natsume’s voice was tight with anxiety.", is_narrator=True)
    show_story_box("Natsume", "This is… too easy.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Akasuke", "Don’t jinx it, Natsume.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Natsume", "No, seriously. You’ve cleared 80% of the fodder. Where are the Ninjas? The enemy wouldn’t just throw away their pawns without a counter-play.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Shigemura", "Perhaps they’re waiting for us to tire out?", affiliation="Kasakura High School Student")
    
    show_story_box("Natsume", "Wait. New contacts. Three signals. Moving fast. Very fast.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Benikawa", "Fast? Like my speed?", affiliation="Benikawa Ninja Clan")
    show_story_box("Natsume", "Maybe faster. They’re grouped together. Moving… erratically. No clear direction. Just speed.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Akasuke", "That has to be them. The Ninjas.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Natsume", "Sector 7. Intercept them.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "We changed course, sprinting down a long service hallway lined with steam pipes.", is_narrator=True)
    show_story_box("Akasuke", "Ready yourselves!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "We rounded the corner, fist raised.", is_narrator=True)

    # --- SCENE 2: THE DECOY ---
    show_story_box("", "But there were no ninjas.\nInstead, there was… a guy.", is_narrator=True)
    show_story_box("", "A Heiwa Seiritsu student. Buzzcut. Shirtless. Wearing military-style camo pants.", is_narrator=True)
    show_story_box("", "He was sprinting. Full tilt. Breathing rhythmically.", is_narrator=True)
    show_story_box("", "And in each hand, he was gripping the back of a shirt—dragging two unconscious Heiwa students behind him like they were plastic grocery bags.", is_narrator=True)
    
    show_story_box("", "He ran past us without even looking.", is_narrator=True)
    show_story_box("???", "HUP! TWO! THREE! FOUR! HUP! TWO! THREE! FOUR!", affiliation="Heiwa Seiritsu High School Student")
    show_story_box("", "He disappeared around the bend.\nWe stood there, blinking.", is_narrator=True)
    
    show_story_box("Yuri", "...What was that?", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Akasuke", "Natsume. Did you see that?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Silence for a second. Then Natsume swore. Loudly.", is_narrator=True)
    show_story_box("Natsume", "Damn it! I’ve been played!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Shigemura", "Played?", affiliation="Kasakura High School Student")
    
    show_story_box("Natsume", "That idiot isn’t just running! He’s carrying two bodies! That creates a combined bio-signature of three people moving at high speed! He’s a decoy!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "My stomach dropped.\nIf the fast signal was a decoy… where were the real ninjas?", is_narrator=True)
    
    show_story_box("Akasuke", "Natsume! Where are the other signals?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Natsume", "Checking… all remaining signals are slow. Scattered. They look like normal students or staff. I can’t—wait.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Natsume", "Three signals. Just appeared. Sector… Zero.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Sector Zero. The Control Room.", is_narrator=True)
    show_story_box("Shigemura", "Natsume! They’re behind you!", affiliation="Kasakura High School Student")
    
    show_story_box("Natsume", "Huh? Wha—", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "Static.", is_narrator=True)

    # --- SCENE 3: THE BRIDGE INFILTRATION ---
    show_story_box("", "On the tablet screen, I saw it.\nThree figures in Kasakura uniforms stepped out from the shadows behind her chair.", is_narrator=True)
    show_story_box("", "Silent. Efficient.\nOne hand covered her mouth. Another disconnected the camera feed.\nThe screen went black.", is_narrator=True)
    
    show_story_box("Yuri", "Natsume-chan!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Benikawa", "They got her. They used the runner to distract her while they infiltrated the bridge.", affiliation="Benikawa Ninja Clan")
    show_story_box("Akasuke", "We have to go. Now.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Benikawa", "I know the layout. Follow me!", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "We turned to run back the way we came.\nTHUD. THUD. THUD.", is_narrator=True)
    show_story_box("", "Heavy, rhythmic footsteps echoed from the corridor ahead. Getting louder. Fast.", is_narrator=True)
    show_story_box("", "The runner was back.", is_narrator=True)
    
    show_story_box("", "He drifted around the corner like a race car, sweat flying off his buzzcut.", is_narrator=True)
    show_story_box("???", "LAP TWO COMPLETE! OBSTACLE DETECTED!", affiliation="Heiwa Seiritsu High School Student")
    
    show_story_box("", "He didn’t stop. He didn’t slow down.\nHe swung his arms forward, releasing the two unconscious bodies. They flew through the air like projectiles.", is_narrator=True)
    
    show_story_box("Akasuke", "Dodge!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "We scattered. The bodies slammed into the wall where we had just been standing.", is_narrator=True)
    show_story_box("", "But the runner kept coming.\nHe didn’t turn. He just crashed straight into the metal bulkhead at full sprinting speed.", is_narrator=True)
    
    show_story_box("", "CLANG!\nThe entire wall shuddered. A dent the shape of a human shoulder appeared in the steel.", is_narrator=True)
    show_story_box("", "He bounced off, landed on his feet, and immediately started shaking out his limbs.", is_narrator=True)
    
    show_story_box("???", "Oof. Good impact. Solid resistance. 8/10.", affiliation="Heiwa Seiritsu High School Student")
    show_story_box("", "He started doing high knees in place.", is_narrator=True)
    show_story_box("???", "Warm-up complete! Ready for engagement!", affiliation="Heiwa Seiritsu High School Student")
    
    show_story_box("Shigemura", "...Who the hell are you?", affiliation="Kasakura High School Student")
    
    show_story_box("", "He snapped to attention, saluting with terrifying enthusiasm.", is_narrator=True)
    show_story_box("Hisayuki", "Sir! Hisayuki Tadamasa! Second Year, Heiwa Seiritsu High School! Sir!", affiliation="Heiwa Seiritsu High School Student")
    
    show_story_box("Akasuke", "That speed… that durability… he’s gotta be an ‘Upperclassman’!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Hisayuki", "Negative, sir! I am but a lowly grunt! I aspire to reach the heights of the Upperclassmen one day! But for now, I just run!", affiliation="Heiwa Seiritsu High School Student")
    show_story_box("", "He dropped into a sprinter’s stance.", is_narrator=True)
    
    show_story_box("Hisayuki", "Target acquired. Kasakura High School representatives. Mission: Impediment.", affiliation="Heiwa Seiritsu High School Student")
    show_story_box("", "He grinned—a wide, simple, eager grin.", is_narrator=True)
    show_story_box("Hisayuki", "Catch me if you can!", affiliation="Heiwa Seiritsu High School Student")
    
    show_story_box("", "He bolted. Not towards us—but away. Down a side corridor.", is_narrator=True)
    
    show_story_box("Yuri", "He’s runnin’ away?", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Benikawa", "No. He’s circling back. He needs room to accelerate.", affiliation="Benikawa Ninja Clan")
    show_story_box("Akasuke", "He’s going to use himself as a battering ram. Again and again.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Akasuke looked at the dented wall.", is_narrator=True)
    show_story_box("Akasuke", "We don’t have time for this. We need to save Natsume.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Shigemura", "Then we have to stop him. Now.", affiliation="Kasakura High School Student")
    show_story_box("", "Hisayuki’s footsteps were already getting louder again.\nHe was coming back.", is_narrator=True)


def play_stage_3_11_end():
    # --- SCENE 4: AKASUKE'S POV (THE BATTLE AGAINST HISAYUKI) ---
    show_story_box("", "********* ◆ *********\nAkasuke’s POV", is_narrator=True)
    show_story_box("", "CLANG!\nThe sound of flesh hitting steel echoed for the tenth time.", is_narrator=True)
    
    show_story_box("", "Hisayuki bounced off the bulkhead, shook his head like a wet dog, and immediately dropped back into a sprinter’s crouch.", is_narrator=True)
    show_story_box("Hisayuki", "Damage report: Negligible! Stamina: 98%...resuming!!", affiliation="Heiwa Seiritsu High School Student")
    
    show_story_box("Akasuke", "You have got to be kidding me.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "I wiped sweat from my forehead. This guy wasn’t a fighter. He was a human pinball.", is_narrator=True)
    show_story_box("", "He launched himself again.", is_narrator=True)
    
    show_story_box("Akasuke", "Side step!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "I lunged, catching him with a hook to the jaw as he flew past. It was a clean hit—enough to knock out a normal person.", is_narrator=True)
    show_story_box("", "He flipped backward, crashed onto the floor, skidded three meters… and then twitched.", is_narrator=True)
    
    show_story_box("", "One second later, he popped back up.", is_narrator=True)
    show_story_box("Hisayuki", "Phew...recovery complete.", affiliation="Heiwa Seiritsu High School Student")
    
    show_story_box("Akasuke", "Tsk! Grab him!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "Yuri and I jumped on him. Yuri locked his arms; I grabbed his waist. We tried to pin him to the ground.", is_narrator=True)
    
    show_story_box("Hisayuki", "Additional weight detected. Engaging…power sprint!!", affiliation="Heiwa Seiritsu High School Student")
    show_story_box("", "He started running. With us on his back.", is_narrator=True)
    
    show_story_box("Yuri", "W-woahh..! He’s draggin’ us like luggage!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "We bailed out just before he smashed into a support pillar.\nBANG!", is_narrator=True)
    
    show_story_box("", "Benikawa landed beside us, looking frustrated.", is_narrator=True)
    show_story_box("Benikawa", "He’s like a rampaging bull! I can’t hit a vital point if he’s vibrating at mach speed! If he would just stand still for two seconds, I could paralyze him!", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "Shigemura stepped forward.\nHe was rolling up his sleeves, cracking his knuckles with a grim expression.", is_narrator=True)
    show_story_box("Shigemura", "Two seconds. That’s all you need?", affiliation="Kasakura High School Student")
    show_story_box("Benikawa", "Huh? Yeah. But stopping him is impossible.", affiliation="Benikawa Ninja Clan")
    show_story_box("Shigemura", "Not impossible. Just…it’s gonna be a pain.", affiliation="Kasakura High School Student")
    
    show_story_box("", "He walked into the center of the corridor. Right in Hisayuki’s path.", is_narrator=True)
    show_story_box("Akasuke", "Shigemura! Don’t! You’re not built for tanking hits!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "He ignored me. He stood with his legs shoulder-width apart, arms loose at his sides.", is_narrator=True)
    show_story_box("", "Hisayuki turned the corner, seeing the new obstacle.", is_narrator=True)
    show_story_box("Hisayuki", "HOH?!", affiliation="Heiwa Seiritsu High School Student")
    
    show_story_box("", "Shigemura didn’t flinch. He just beckoned with one hand. Casual. Arrogant. Like a matador inviting the bull.", is_narrator=True)
    show_story_box("Shigemura", "Come on.", affiliation="Kasakura High School Student")
    
    show_story_box("", "Hisayuki roared and accelerated.\nThe impact was sickening.\nCRASH!", is_narrator=True)
    
    show_story_box("", "Shigemura didn’t try to block. He crouched slightly and caught Hisayuki’s torso, wrapping his arms around the runner’s chest.", is_narrator=True)
    show_story_box("", "They slid backward. Ten feet. Twenty feet.\nCRUNCH.", is_narrator=True)
    
    show_story_box("", "Shigemura’s back hit the wall. The metal dented behind him. The wind was knocked out of him instantly.", is_narrator=True)
    show_story_box("", "But he didn’t let go.\nHe gritted his teeth, veins bulging on his neck, and locked his arm around Hisayuki’s throat.", is_narrator=True)
    
    show_story_box("Shigemura", "N…now! Benikawa!", affiliation="Kasakura High School Student")
    
    show_story_box("", "Benikawa was already moving.\nShe blurred forward, her fingers stiffened into spear-hands.", is_narrator=True)
    show_story_box("", "THWACK. THWACK. THWACK.", is_narrator=True)
    show_story_box("", "She jammed her fingers into the nerves of Hisayuki’s thighs and calves with surgical precision.", is_narrator=True)
    
    show_story_box("Shigemura", "Guh—!", affiliation="Kasakura High School Student")
    show_story_box("", "He couldn’t hold it any longer. His grip failed, and he slid to the floor, gasping for air.", is_narrator=True)
    
    show_story_box("", "Hisayuki stumbled back.", is_narrator=True)
    show_story_box("Hisayuki", "Motor functions compromised..!", affiliation="Heiwa Seiritsu High School Student")
    show_story_box("", "He tried to run. He shook his legs. But the explosive speed was gone. He was limping.", is_narrator=True)
    
    show_story_box("Benikawa", "Leg power cut by more than half. He’s yours, Akasuke!", affiliation="Benikawa Ninja Clan")
    show_story_box("", "I stepped in.", is_narrator=True)
    show_story_box("Hisayuki", "Guh!—", affiliation="Heiwa Seiritsu High School Student")
    
    show_story_box("", "Hisayuki threw a punch—slow, telegraphed. I deflected it easily, countering with a strike to his elbow. Then his knee. Wearing him down.", is_narrator=True)
    show_story_box("", "Desperate, he dropped low.", is_narrator=True)
    
    show_story_box("Hisayuki", "—Let’s see how you like this!", affiliation="Heiwa Seiritsu High School Student")
    show_story_box("", "A low tackle. He lunged for my legs.", is_narrator=True)
    show_story_box("", "I didn’t move.\nI didn’t need to.", is_narrator=True)
    
    show_story_box("", "Yuri appeared between us like a guardian angel.\nThis is her turf, after all.", is_narrator=True)
    show_story_box("", "She caught his shoulders, used his own momentum, and spun.", is_narrator=True)
    
    show_story_box("Yuri", "Sit DOWN!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "She slammed him into the wall of pipes. Hard.\nBLAM!\nHISSSSSS!", is_narrator=True)
    
    show_story_box("", "Steam erupted as the pipes burst. Hisayuki slid down the wall, eyes rolling back into his head.", is_narrator=True)
    show_story_box("Hisayuki", "Shutting… down…", affiliation="Heiwa Seiritsu High School Student")
    show_story_box("", "Silence.", is_narrator=True)
    
    show_story_box("", "I helped Shigemura up. He was bruised already, but he managed a weak smile.", is_narrator=True)
    show_story_box("Akasuke", "You crazy bastard. That was amazing.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Shigemura", "I… prefer reading… to wrestling.", affiliation="Kasakura High School Student")
    
    show_story_box("Benikawa", "Come on. Natsume needs us.", affiliation="Benikawa Ninja Clan")
    show_story_box("", "Benikawa took point, leading us through the maze of corridors toward Sector Zero.", is_narrator=True)

def play_stage_3_12_start():
    # --- SCENE 1: AKASUKE'S POV (THE CONTROL ROOM) ---
    show_story_box("", "********* ◆ *********\nAkasuke’s POV", is_narrator=True)
    show_story_box("", "As we ran, I couldn’t help but think.", is_narrator=True)
    
    show_story_box("Akasuke", "Why? Why go to these lengths? The decoys. The infiltration.", affiliation="Kasakura High School Student / Seven Wonders", is_thought=True)
    show_story_box("Akasuke", "This time, what is on this ship that matters so much?", affiliation="Kasakura High School Student / Seven Wonders", is_thought=True)
    
    show_story_box("", "We reached the Control Room. The door was locked.", is_narrator=True)
    
    show_story_box("Yuri", "Let me!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "She kicked the lock. The door flew open.\nWe burst in, ready for a fight.", is_narrator=True)
    
    show_story_box("Akasuke", "Natsume!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "The room was dark. Monitors dead.\nBut there were no ninjas. Just a bundle of blankets on the floor.", is_narrator=True)
    show_story_box("", "Natsume was sleeping soundly.", is_narrator=True)
    show_story_box("", "Shigemura checked her pulse.", is_narrator=True)
    
    show_story_box("Shigemura", "She’s fine. Just unconscious. No injuries.", affiliation="Kasakura High School Student")
    
    show_story_box("", "I hit the light switch. The overheads flickered on.\nNatsume groaned, shielding her eyes.", is_narrator=True)
    
    show_story_box("Natsume", "Ugh… too bright…", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "She sat up, rubbing her neck.", is_narrator=True)
    
    show_story_box("Akasuke", "Natsume! Are you okay? The ninjas?", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Natsume", "They… they just knocked me out. Gentle touch. No pain.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "She looked at the blank screens.", is_narrator=True)
    show_story_box("Natsume", "Hm. So they didn’t want me…they wanted the admin console.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "She crawled over to the desk, typing furiously on a dead keyboard.", is_narrator=True)
    show_story_box("Natsume", "Damn. They cut the power to bypass the logs. They were searching for something in the ship’s manifest. Something specific.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Akasuke", "Manifest? Cargo?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Before she could answer, my pocket buzzed.\nI pulled out my phone.\n| Caller ID: Nishida. |", is_narrator=True)

    # --- SCENE 2: NAGANOHARA'S POV (FLASHBACK) ---
    show_story_box("", "********* ◆ *********\nNaganohara’s POV\n(A few minutes ago)", is_narrator=True)
    show_story_box("", "Guest Cabin 304\nI sat on the edge of the bed, hugging a pillow.", is_narrator=True)
    
    show_story_box("Naganohara", "Yuri-chan still isn’t back…", affiliation="Kasakura High School Student")
    
    show_story_box("", "Yamashita was sitting at the desk, sketching something on a notepad. Nishida was pacing, checking his phone after being called over to our room temporarily.", is_narrator=True)
    
    show_story_box("Naganohara", "It’s been hours! She said she was ‘helping Kojima-sensei clean the decks’. But… does cleaning decks take this long? At night?", affiliation="Kasakura High School Student")
    
    show_story_box("", "Nishida stopped pacing. He sighed.", is_narrator=True)
    show_story_box("Nishida", "Naganohara. You know that’s a lie, right?", affiliation="Kasakura High School Student")
    
    show_story_box("", "I blinked.", is_narrator=True)
    show_story_box("Naganohara", "Eh?", affiliation="Kasakura High School Student")
    show_story_box("Nishida", "Akasuke and Shigemura used the exact same excuse. ‘Cleaning decks’. It’s obviously code for ‘We are going to fight bad guys and play heroes’ again.", affiliation="Kasakura High School Student")
    
    show_story_box("", "My eyes widened.", is_narrator=True)
    show_story_box("Naganohara", "F-Fight?! But Shigemura-kun is… he’s fragile! He can’t fight!", affiliation="Kasakura High School Student")
    
    show_story_box("", "Yamashita spun her chair around.", is_narrator=True)
    show_story_box("Yamashita", "Yeah…well, fragile or not, they’re out there. And we all know why this time, right?", affiliation="Kasakura High School Student")
    
    show_story_box("Naganohara", "...N-no? Why?! What kind of crime happens on a cruise ship? Are they stealing the buffet shrimp?", affiliation="Kasakura High School Student")
    
    show_story_box("", "Nishida shook his head.", is_narrator=True)
    show_story_box("Nishida", "Think about it. The two of us’ve been geeking out over this ship all day. Why?", affiliation="Kasakura High School Student")
    
    show_story_box("Naganohara", "Because… the shops are expensive?", affiliation="Kasakura High School Student")
    
    show_story_box("Nishida", "Mmm, no, but maybe a little for Hanae. It’s because the facilities are insane. There’s a machine shop on Deck 4 with industrial lathes. There’s a chem lab on Deck 2. There are stockpiles of high-grade steel and gunpowder in the cargo hold.", affiliation="Kasakura High School Student")
    show_story_box("Yamashita", "Cruise ships don’t need weapon-grade manufacturing plants, Naganohara. This ship…we swear it’s a floating arsenal.", affiliation="Kasakura High School Student")
    show_story_box("Nishida", "It’s a supply cache. For the schools. Or maybe specifically for their defense projects.", affiliation="Kasakura High School Student")
    
    show_story_box("", "Nishida pulled out his phone.", is_narrator=True)
    show_story_box("Nishida", "The enemy is here to steal the weapons. That’s the only thing worth this much trouble.", affiliation="Kasakura High School Student")
    
    show_story_box("Naganohara", "Does… does Akasuke-kun know that?", affiliation="Kasakura High School Student")
    
    show_story_box("", "Nishida paused.", is_narrator=True)
    show_story_box("Nishida", "Knowing him? Probably not. He’s probably just punching things and wondering why they keep coming.", affiliation="Kasakura High School Student")
    
    show_story_box("", "He dialed a number.", is_narrator=True)
    show_story_box("Nishida", "Right, guess I better tell him. Before he punches the wrong thing.", affiliation="Kasakura High School Student")

    # --- SCENE 3: AKASUKE'S POV (PRESENT) ---
    show_story_box("", "********* ◆ *********\nAkasuke’s POV\n(Present Time)", is_narrator=True)
    show_story_box("", "I put the phone to my ear.", is_narrator=True)
    
    show_story_box("Akasuke", "Nishida? It’s a bad time…right now.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Nishida", "Yeah, yeah. Good work playing hero. Just listen.", affiliation="Kasakura High School Student")
    
    show_story_box("", "His voice was serious.", is_narrator=True)
    show_story_box("Nishida", "You guys are fighting blind. Me n’ Yamashita know what they’re after.", affiliation="Kasakura High School Student")
    
    show_story_box("Akasuke", "You do?", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Nishida", "Weapons, dude. The ship is loaded with manufacturing equipment and raw materials. It’s a mobile armory. They aren’t here to kidnap anyone or sink the ship. They’re here for a robbery.", affiliation="Kasakura High School Student")
    
    show_story_box("", "I froze.\nIt all made sense. The maintenance corridors. The search in the admin system. It must’ve been used to find their storage.", is_narrator=True)
    
    show_story_box("Akasuke", "Weapons supply… Thanks, Nishida. That’s a major help.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I hung up and turned to the group.", is_narrator=True)
    show_story_box("Akasuke", "They’re after the weapons cache. Natsume, where are the armories?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Natsume was already rebooting a backup terminal on her tablet instead.", is_narrator=True)
    show_story_box("Natsume", "Weapons… weapons… Got it. Three possible storage zones in the lowest sectors. Cargo Bay A, B, and the Hazard Vault.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Benikawa stood up, cracking her neck.", is_narrator=True)
    show_story_box("Benikawa", "Lowest sectors? I memorized those layouts for the whole day. Follow me.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "We moved out. Natsume grabbed her tablet and scrambled after us.", is_narrator=True)
    show_story_box("Natsume", "Wait! I’m coming too! I am not staying here to get knocked out again!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "We descended into the dark.", is_narrator=True)

def play_stage_3_13_start():
    # --- SCENE 1: NATSUME'S POV (THE DESCENT) ---
    show_story_box("", "********* ◆ *********\nNatsume’s POV", is_narrator=True)
    show_story_box("", "The air grew heavier as we descended.", is_narrator=True)
    show_story_box("", "The sleek, polished corridors of the upper decks were gone. Here, in the bowels of the ship, everything was industrial gray, smelling of grease and ozone.", is_narrator=True)
    show_story_box("", "Benikawa took point, moving with a predator’s grace. Akasuke and Yuri flanked her. Shigemura and I brought up the rear.", is_narrator=True)
    
    show_story_box("Natsume", "Shigemura. Watch the left.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Shigemura", "On it.", affiliation="Kasakura High School Student")
    
    show_story_box("", "The resistance was stiffening.", is_narrator=True)
    show_story_box("", "We weren’t fighting mindless thugs anymore. The Heiwa students here wore the faces of squad leaders—coordinated, hitting hard. The Kiryoku girls moved with the precision of the Self-Defense Club’s aces.", is_narrator=True)
    show_story_box("", "And the Kasakura infiltrators…\nI watched one step out of the shadows, wielding a stun baton with a distinct telescopic grip.", is_narrator=True)
    
    show_story_box("Natsume", "That's the Disciplinary Committee’s standard issue. Model 4-B..!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Akasuke deflected the baton strike, shattering the weapon with a karate chop.", is_narrator=True)
    show_story_box("Akasuke", "They raided our armory before coming here? Or are they the Committee’s defectors..?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Natsume", "Keep moving.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "We pushed through, leaving a trail of unconscious bodies.", is_narrator=True)
    show_story_box("", "Ahead, a massive blast door marked ‘CARGO BAY A’ loomed.\nI pulled up the ship’s schematic on my tablet.", is_narrator=True)
    
    show_story_box("Natsume", "Hold up.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "They stopped.", is_narrator=True)
    show_story_box("Natsume", "There are three main weapon storage vaults on this level. Bay A, Bay B, and the Hazard Vault.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I looked at Benikawa.", is_narrator=True)
    show_story_box("Natsume", "Three vaults. Three ninjas. It’s not rocket science.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Benikawa", "One for each. Makes sense. They’re overseeing the extraction.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "Yuri cracked her knuckles.", is_narrator=True)
    show_story_box("Yuri", "Then let’s go say hi.", affiliation="Kasakura High School Student / Seven Wonders")

    # --- SCENE 2: CARGO BAY A & RAVEN ---
    show_story_box("", "She hit the door release.\nThe hydraulics hissed, and the heavy doors groaned open.", is_narrator=True)
    
    show_story_box("", "Inside, it was a cavern of steel crates. Dozens of students were rushing back and forth, loading weapons onto hover-dollies.", is_narrator=True)
    show_story_box("", "But in the center of the chaos, sitting atop a stack of ammo crates, was one figure.", is_narrator=True)
    show_story_box("", "He wasn’t moving. He was just… watching.\nHe wore the Kasakura uniform, but the blazer was draped over his shoulders like a cape.", is_narrator=True)
    
    show_story_box("Benikawa", "Target confirmed. It’s one of them.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "He looked up.\nShort, spiky black hair. Tall—easily Akasuke’s height.", is_narrator=True)
    show_story_box("", "And his eyes…\nThey were a piercing, deadly purple.", is_narrator=True)
    show_story_box("", "He hopped down, landing silently. He tossed the coat aside, revealing a tactical vest over his shirt. He stretched his neck, cracking it loudly.", is_narrator=True)
    
    show_story_box("Raven", "Code Name: Raven.", affiliation="Ninja Clan Infiltrator")
    
    show_story_box("", "He waved a hand, and the workers stopped loading. They drew weapons—crowbars, batons, knives.", is_narrator=True)
    show_story_box("Raven", "I gave you a chance, you know. To play nice upstairs. Eat at the buffet. Enjoy the cruise.", affiliation="Ninja Clan Infiltrator")
    
    show_story_box("", "He drew a short, straight blade from his belt.", is_narrator=True)
    show_story_box("Raven", "This is not your business. You should have stayed in the light.", affiliation="Ninja Clan Infiltrator")
    
    show_story_box("", "Akasuke stepped forward, his eyepatch glinting.", is_narrator=True)
    show_story_box("Akasuke", "Sorry. We prefer the deep end.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "The brawl erupted.", is_narrator=True)

def play_stage_3_13_end():
    # --- SCENE 3: AFTERMATH OF BAY A ---
    show_story_box("", "CRASH!\nRaven slammed into a stack of crates, coughing blood.", is_narrator=True)
    show_story_box("", "He looked at us—at Akasuke’s glowing blue aura, at Yuri’s impossible strength, at Benikawa’s speed.", is_narrator=True)
    
    show_story_box("Raven", "Tsk! Monsters… all of you.", affiliation="Ninja Clan Infiltrator")
    
    show_story_box("", "He was hurt. Badly. His left arm hung limp, and he was favoring his right leg.", is_narrator=True)
    show_story_box("", "He threw a smoke bomb at his feet.\nPOOF.\nThick gray smoke filled the bay.", is_narrator=True)
    
    show_story_box("Raven", "This isn’t over.", affiliation="Ninja Clan Infiltrator")
    
    show_story_box("", "When the smoke cleared, he was gone.", is_narrator=True)
    
    show_story_box("Benikawa", "He’s retreating. To the next post.", affiliation="Benikawa Ninja Clan")
    show_story_box("Natsume", "Regrouping. He’s going to Bay B to reinforce the next ninja.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Akasuke", "Then we chase him.", affiliation="Kasakura High School Student / Seven Wonders")

    # --- SCENE 4: CARGO BAY B & FALCON ---
    show_story_box("", "CARGO BAY B\nWe didn’t bother with the door release this time. Yuri just punched the lock mechanism, and Akasuke kicked the doors open.", is_narrator=True)
    show_story_box("", "The scene was similar—more crates, more goons.\nBut the air felt… sharper.", is_narrator=True)
    
    show_story_box("", "Raven was there, leaning against a forklift, wrapping a bandage around his arm.\nAnd standing next to him was another boy.", is_narrator=True)
    show_story_box("", "Kasakura uniform. Short, messy blonde hair. He had stripped off his shirt, wrapping the sleeves around his waist, revealing a lean, scarred torso prepped for war.", is_narrator=True)
    
    show_story_box("", "He turned to face us.\nHis eyes were the same.\nDetermined, glowing purple.", is_narrator=True)
    
    show_story_box("", "I glanced at Benikawa. She looked tense.", is_narrator=True)
    show_story_box("Benikawa", "...Yeah. Another one.", affiliation="Benikawa Ninja Clan")
    show_story_box("", "She wasn’t looking at the enemy. She was glancing sideways at me. At Akasuke.", is_narrator=True)
    
    show_story_box("Natsume", "Benikawa… are you worried we’ll notice?", affiliation="Kasakura High School Student / Seven Wonders", is_thought=True)
    
    show_story_box("", "Two ninjas. Both with purple eyes. It was becoming a pattern.", is_narrator=True)
    show_story_box("", "The blonde ninja stepped forward, cracking his knuckles.", is_narrator=True)
    
    show_story_box("Falcon", "Code Name: Falcon.", affiliation="Ninja Clan Infiltrator")
    show_story_box("", "He looked at Raven.", is_narrator=True)
    show_story_box("Falcon", "You look like trash, Raven.", affiliation="Ninja Clan Infiltrator")
    show_story_box("Raven", "Shut up. They’re strong. Watch the redhead.", affiliation="Ninja Clan Infiltrator")
    
    show_story_box("", "Falcon grinned, shifting into a combat stance that looked eerily similar to Akasuke’s karate style, but lower, more feral.", is_narrator=True)
    show_story_box("Falcon", "Strong? Good. I was getting bored.", affiliation="Ninja Clan Infiltrator")
    
    show_story_box("", "He signaled the goons—a mix of Heiwa thugs, Kiryoku fighters, and Kasakura traitors.", is_narrator=True)
    show_story_box("Falcon", "Kill them.", affiliation="Ninja Clan Infiltrator")
    
    show_story_box("", "Akasuke took a breath, blue energy flickering around him.", is_narrator=True)
    show_story_box("Akasuke", "Two ninjas. One army. And us.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Yuri grinned.", is_narrator=True)
    show_story_box("Yuri", "Sounds fair.", affiliation="Kasakura High School Student / Seven Wonders")

def play_stage_3_14_start():
    # --- SCENE 1: NATSUME'S POV (THE CHASE) ---
    show_story_box("", "********* ◆ *********\nNatsume’s POV", is_narrator=True)
    show_story_box("", "The metal corridor vibrated with the sound of retreating footsteps.", is_narrator=True)
    show_story_box("", "Raven and Falcon were running. But they weren’t just running—they were bickering.", is_narrator=True)
    
    show_story_box("Raven", "You got in my way, Falcon! If you hadn’t blocked my smoke line, I would have gutted the redhead!", affiliation="Ninja Clan Infiltrator")
    show_story_box("Falcon", "In your dreams! You were limping like a wounded dog! I had to cover your sorry ass!", affiliation="Ninja Clan Infiltrator")
    
    show_story_box("", "Akasuke slowed down, watching them disappear around the bend toward the final sector.", is_narrator=True)
    show_story_box("Akasuke", "They’re fighting each other more than us.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Benikawa sighed, shaking her head.", is_narrator=True)
    show_story_box("Benikawa", "It’s the ego. Ninjas are solitary creatures by nature. Secrecy is our armor, but pride is our weapon.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "She gestured vaguely at the retreating figures.", is_narrator=True)
    show_story_box("Benikawa", "We don’t play well with others. When you force multiple elites to work together without a clear hierarchy? They clash. They compete for the kill. It makes them sloppy.", affiliation="Benikawa Ninja Clan")
    show_story_box("Benikawa", "If just one of them had fought us alone with full focus… it might have been deadlier. But their pride won’t let them support each other.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Yuri", "So… they’re doin’ our job for us?", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Benikawa", "Basically.", affiliation="Benikawa Ninja Clan")

    # --- SCENE 2: THE HAZARD VAULT ---
    show_story_box("", "We reached the end of the line.", is_narrator=True)
    show_story_box("", "A massive blast door, painted in black and yellow stripes. HAZARD VAULT.", is_narrator=True)
    show_story_box("", "The highest security clearance on the ship. Explosives, experimental fuel, heavy ordnance.", is_narrator=True)
    show_story_box("", "The door was already open.\nWe stepped inside.", is_narrator=True)
    
    show_story_box("", "The room was a vast, circular chamber lined with reinforced containment cells.", is_narrator=True)
    show_story_box("", "Raven and Falcon were there, panting, bleeding, standing on opposite sides of the central platform.", is_narrator=True)
    show_story_box("", "And between them stood the third one.", is_narrator=True)
    show_story_box("", "He was leaning against a large explosive casing, arms crossed. He wore the Kasakura uniform, but his brown hair was tied back in a sharp ponytail—mirroring Benikawa’s style.", is_narrator=True)
    
    show_story_box("", "He looked up.\nHis eyes glowed with that same, unmistakable, deadly purple light.", is_narrator=True)
    
    show_story_box("", "Benikawa stiffened beside me. I could feel her anxiety radiating off her like heat.", is_narrator=True)
    show_story_box("Benikawa", "...He’s here. The last ninja.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "She looked nervous. The ‘Code’ was weighing on her. If we recognized the pattern, she’d be implicated.", is_narrator=True)
    show_story_box("", "I leaned in, whispering so only she could hear.", is_narrator=True)
    
    show_story_box("Natsume", "Relax, Benikawa.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Natsume", "Let’s say I’ve been recording and researching. Their eyes are practically flashlights. They leaked the intel, not you.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Natsume", "You’re in the clear.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "She let out a breath she’d been holding.", is_narrator=True)
    show_story_box("Benikawa", "...Ahh, Thanks! Natsume.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("???", "Look at you two. Pathetic.", affiliation="Ninja Clan Infiltrator")
    
    show_story_box("", "The ponytail ninja spoke. His voice was calm, smooth, and utterly cold.", is_narrator=True)
    show_story_box("Eagle", "Code Name: Eagle. You led the wolves right to our doorstep.", affiliation="Ninja Clan Infiltrator")
    
    show_story_box("Raven", "Shut up, Eagle! They’re monsters!", affiliation="Ninja Clan Infiltrator")
    show_story_box("Falcon", "Just kill them!", affiliation="Ninja Clan Infiltrator")
    
    show_story_box("", "Eagle stepped forward, his purple eyes locking onto Akasuke.", is_narrator=True)
    show_story_box("Eagle", "Three against four. Plus the analyst. I suppose we’ll have to—", affiliation="Ninja Clan Infiltrator")

    # --- SCENE 3: YURI's REALIZATION & SHIGEMURA'S SECRET ---
    show_story_box("Yuri", "AHHHH!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "Yuri pointed a finger at Eagle. Then at Raven. Then at Falcon.", is_narrator=True)
    show_story_box("", "Everyone froze. Even the ninjas.", is_narrator=True)
    
    show_story_box("Yuri", "I get it! I finally get it!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Akasuke", "Yuri?", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Yuri", "It’s the eyes! They all got purple eyes! That’s the secret tell, ain’t it?! All ninjas have purple eyes!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Silence.\nAbsolute, deafening silence.", is_narrator=True)
    show_story_box("", "Benikawa slapped her forehead. The enemy ninjas looked stunned that she just shouted it out loud.", is_narrator=True)
    
    show_story_box("", "Akasuke blinked. He turned his head slowly.\nTo Shigemura.", is_narrator=True)
    show_story_box("", "Shigemura stood there, dusting off his sleeves.", is_narrator=True)
    show_story_box("", "His eyes, usually hidden or overlooked in the chaos, were fully visible under the vault lights.\nDeep. Violet. Purple.", is_narrator=True)
    
    show_story_box("", "He noticed Akasuke staring. He flinched, looking away shyly, scratching his cheek.", is_narrator=True)
    show_story_box("Shigemura", "Ah… well…", affiliation="Kasakura High School Student")
    
    show_story_box("", "Akasuke stared for a second longer. Then he smiled. A soft, trusting smile.", is_narrator=True)
    show_story_box("Akasuke", "So that’s why.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Shigemura", "...You’re not surprised?", affiliation="Kasakura High School Student")
    
    show_story_box("Akasuke", "I am. But it makes sense now. Why Benikawa vouched for you. Why you were able to hold that runner back.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Akasuke stepped up, patting Shigemura’s shoulder.", is_narrator=True)
    show_story_box("Akasuke", "I’m glad. Knowing you’re this strong… means I can really entrust Naganohara’s safety to you. You’ve been protecting us from the shadows this whole time, haven’t you?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Shigemura’s eyes widened. He looked at Akasuke, then bowed his head slightly, a faint smile touching his lips.", is_narrator=True)
    show_story_box("Shigemura", "…Thank you, Akasuke. I’ll do my best to live up to that.", affiliation="Kasakura High School Student")
    
    show_story_box("", "Eagle drew two long daggers.", is_narrator=True)
    show_story_box("Eagle", "Enough touching reunions. You know the secret. That means none of you leave this vault alive.", affiliation="Ninja Clan Infiltrator")
    
    show_story_box("", "Raven and Falcon readied their weapons. The remaining infiltration force—dozens of elites—stepped out from behind the crates.", is_narrator=True)
    
    show_story_box("", "Akasuke raised his fists, blue aura flaring to life.", is_narrator=True)
    show_story_box("Akasuke", "Let’s go, everyone. One last push.", affiliation="Kasakura High School Student / Seven Wonders")

def play_stage_3_15_story():
    # --- SCENE 1: AKASUKE'S POV (THE HAZARD VAULT AFTERMATH) ---
    show_story_box("", "********* ◆ *********\nAkasuke’s POV", is_narrator=True)
    show_story_box("", "The battle in the Hazard Vault was finally over.", is_narrator=True)
    show_story_box("", "Falcon lay unconscious near the missile casing. Raven was slumped against a crate, out cold. The elite infiltration force was scattered, groaning in pain on the steel floor.", is_narrator=True)
    
    show_story_box("Akasuke", "It’s over, ‘Eagle’. Give it up.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Eagle stood alone in the center of the carnage. He was panting heavily, clutching his side where Yuri had landed a solid kick. His purple eyes darted around—looking for an opening.", is_narrator=True)
    show_story_box("Eagle", "Ghh...Not yet.", affiliation="Ninja Clan Infiltrator")
    show_story_box("", "He dropped into a low stance.", is_narrator=True)
    
    show_story_box("Akasuke", "Don’t do it. You can’t win.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "He ignored me. With a desperate roar, he dashed forward.", is_narrator=True)
    show_story_box("Benikawa", "He’s going for a suicide charge!", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "We braced ourselves. Shigemura raised his guard. Yuri wound up a punch.", is_narrator=True)
    show_story_box("", "But at the last second, Eagle didn’t attack.", is_narrator=True)
    show_story_box("", "He feinted left, ducked under Yuri’s swing, and sprinted right past us—straight for the open blast door.", is_narrator=True)
    
    show_story_box("Eagle", "I’m not dying in this hole..!!", affiliation="Ninja Clan Infiltrator")
    show_story_box("", "He was running away.", is_narrator=True)
    
    show_story_box("Akasuke", "He’s fleeing! I’m going after him!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Benikawa", "Huh? Wait!", affiliation="Benikawa Ninja Clan")
    show_story_box("Akasuke", "You guys just tie these guys up! I’ll handle him alone!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I didn’t wait for an answer. I bolted out the door, chasing the retreating footsteps echoing up the stairwell.", is_narrator=True)

    # --- SCENE 2: THE CHASE TO THE UPPER DECKS ---
    show_story_box("", "We raced up the ship’s layers—past the cargo decks, through the maintenance levels, all the way to the upper passenger decks.", is_narrator=True)
    show_story_box("", "He was fast, being a ninja, and I could barely keep up.", is_narrator=True)
    show_story_box("", "My lungs burned, but I couldn’t stop.", is_narrator=True)
    show_story_box("", "If a desperate, cornered ninja fighter gets loose among the sleeping students or the VIP guests… it would be a disaster.", is_narrator=True)
    
    show_story_box("Akasuke", "Stop! You have nowhere to go!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Eagle didn’t listen. He burst onto the top deck area, sweating—onto the exclusive VIP sector.", is_narrator=True)
    show_story_box("", "He turned a corner sharply.", is_narrator=True)
    show_story_box("", "I skidded around the bend just in time to see the tail of his coat disappear into a room. The heavy metal door slammed shut.", is_narrator=True)
    
    show_story_box("Akasuke", "Got you.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "I rushed the door, throwing it open.", is_narrator=True)
    show_story_box("Akasuke", "It’s over! Surren—", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I froze.", is_narrator=True)
    show_story_box("", "The room was a luxurious VIP lounge. Leather sofas, dim lighting, crystal glasses on the table.", is_narrator=True)
    show_story_box("", "But Eagle wasn’t fighting.", is_narrator=True)
    show_story_box("", "He was on the floor. Face pressed into the expensive carpet. Screaming.", is_narrator=True)
    
    show_story_box("Eagle", "GAAAAHHH!! MY BACK! IT’S BREAKING!", affiliation="Ninja Clan Infiltrator")

    # --- SCENE 3: THE STARGUARDS ---
    show_story_box("", "Standing over him was a man.", is_narrator=True)
    show_story_box("", "He looked about my age—maybe a year older. But the atmosphere around him… it was heavy. Mature. Like standing next to Kageyama or Masayoshi, but much, much darker.", is_narrator=True)
    show_story_box("", "He wore a pristine white suit, tailored perfectly, like he was dressed for a wedding.", is_narrator=True)
    show_story_box("", "His hair was messy pitch-black, cut in a mullet style, with streaks of azure blue running through it.", is_narrator=True)
    show_story_box("", "He had one foot planted firmly in the center of Eagle’s spine. He wasn’t stomping. He was just leaning his weight on it, casual and lazy.", is_narrator=True)
    
    mystery_style3 = "dark_slate_gray1"
    
    show_story_box("Man in White Suit", "So noisy. I was trying to nap.", affiliation="???", color_override=mystery_style3)
    
    show_story_box("", "His voice was lax, bored. Unpredictable like Shigemura’s, but… cold. There was zero kindness in it.", is_narrator=True)
    show_story_box("", "He looked up at me.\nHis eyes were dark. Empty.", is_narrator=True)
    
    show_story_box("Akasuke", "Uh…", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "My throat went dry. My instincts were screaming at me.", is_narrator=True)
    show_story_box("", "Dangerous. This guy is dangerous.", is_narrator=True)
    show_story_box("", "But Eagle was writhing in agony, even if he is an enemy.", is_narrator=True)
    
    show_story_box("Akasuke", "Hey… could you… maybe take your foot off him? He’s already down.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "The man blinked. Slowly.", is_narrator=True)
    show_story_box("Man in White Suit", "Hm? Oh.", affiliation="???", color_override=mystery_style3)
    
    show_story_box("", "He lifted his foot.\nEagle gasped, curling into a ball, clutching his back.", is_narrator=True)
    show_story_box("", "The man adjusted his white jacket, looking at me with mild curiosity.", is_narrator=True)
    
    show_story_box("Man in White Suit", "I was just surprised. Usually, people don’t barge into our room this late. We especially didn’t expect loud ones.", affiliation="???", color_override=mystery_style3)
    
    show_story_box("", "I looked past him.", is_narrator=True)
    show_story_box("", "Further back in the lounge, sitting on the long black leather sofas, were others.", is_narrator=True)
    show_story_box("", "Three… no, four more people. Boys and girls. All high school age. All wearing the same fancy white suits.", is_narrator=True)
    show_story_box("", "They were sipping unknown amber drinks or fidgeting with coins and lighters. They looked at me, then at Eagle, with expressions of total indifference.", is_narrator=True)
    show_story_box("", "No shock. No fear. No friendliness nor hostility. Just… void.", is_narrator=True)
    show_story_box("", "I couldn’t move. I couldn’t just grab Eagle and leave. The air in the room was suffocating.", is_narrator=True)

    # --- SCENE 4: KOJIMA-SENSEI INTERVENES ---
    show_story_box("Kojima-sensei", "Akasuke!", affiliation="Kasakura High School Teacher")
    show_story_box("", "Kojima-sensei appeared in the doorway behind me, panting slightly.", is_narrator=True)
    
    show_story_box("Kojima-sensei", "Don’t run off like that! What’s the situation—oh.", affiliation="Kasakura High School Teacher")
    show_story_box("", "He saw the man in the white suit. He stopped.", is_narrator=True)
    
    show_story_box("Kojima-sensei", "Ah. Apologies for the intrusion.", affiliation="Kasakura High School Teacher")
    
    show_story_box("", "The man in the suit waved a hand dismissively.", is_narrator=True)
    show_story_box("Man in White Suit", "It’s fine. Just keep the noise down, yeah?", affiliation="???", color_override=mystery_style3)
    
    show_story_box("", "Kojima-sensei grabbed my shoulder and pulled me back a step.", is_narrator=True)
    show_story_box("Akasuke", "Sensei…w-who…who are these guys?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Kojima-sensei leaned in, whispering.", is_narrator=True)
    show_story_box("Kojima-sensei", "Remember the ‘small-time bodyguards’ I told you about? The ones hired to protect the VIPs?", affiliation="Kasakura High School Teacher")
    
    show_story_box("", "I stared at him.", is_narrator=True)
    show_story_box("Akasuke", "‘Small time’? Sensei, look at them! They radiate ‘bad news’!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Kojima-sensei", "I know. Anyone with eyes can see that. But the higher-ups of all four schools unanimously agreed on hiring them.", affiliation="Kasakura High School Teacher")
    show_story_box("", "The ‘higher ups’ again.", is_narrator=True)
    
    show_story_box("", "He straightened up, addressing the room with a polite nod.", is_narrator=True)
    show_story_box("Kojima-sensei", "Relax, Akasuke. They aren’t random criminals. They work for a premium, first-class security service. A family only business.", affiliation="Kasakura High School Teacher")
    show_story_box("Kojima-sensei", "They go by many names. But on the official payroll tonight, they are the ‘Starguards’.", affiliation="Kasakura High School Teacher")

    # --- SCENE 5: THE STARRY EYED ---
    show_story_box("", "The man in the mullet smirked.", is_narrator=True)
    show_story_box("", "He looked at us. The others on the sofa looked up too.", is_narrator=True)
    show_story_box("", "They blinked once.\nSuddenly, their pupils changed.", is_narrator=True)
    show_story_box("", "The dark irises vanished, replaced by glowing, neon plasma-blue shapes.\nStars.", is_narrator=True)
    show_story_box("", "Literal stars shining in their eyes.", is_narrator=True)
    
    show_story_box("Kojima-sensei", "Though… I use their older nickname. The ‘Starry Eyed’. It’s a genetic trait. Chromatic Divergence exclusive to their bloodline.", affiliation="Kasakura High School Teacher")
    
    show_story_box("", "The man’s star-shaped pupils pulsed with a cold, blue light.", is_narrator=True)
    show_story_box("Man in White Suit", "We’re just doing a job, ‘Teach. Clean up your trash so we can go back to relaxing.", affiliation="Starguards", color_override=mystery_style3)
    
    show_story_box("", "He kicked Eagle’s unconscious body toward us gently.", is_narrator=True)
    show_story_box("", "Kojima-sensei hoisted the ninja over his shoulder like a sack of potatoes.", is_narrator=True)
    show_story_box("Kojima-sensei", "Yeah, ‘understood. Come on, Akasuke.", affiliation="Kasakura High School Teacher")
    
    show_story_box("", "He steered me out of the room.\nAs the door clicked shut, cutting off the blue glow, Kojima-sensei let out a long sigh.", is_narrator=True)
    
    show_story_box("Kojima-sensei", "Listen to me, kid. Forget about them.", affiliation="Kasakura High School Teacher")
    show_story_box("Akasuke", "Forget them..? Sensei, their eyes were literal glowing stars.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Kojima-sensei", "I know, they’re overkill for a field trip, even if it is a joint one between four major schools. Once we hit the island, they’ll disperse to do their own thing. You won’t see them again.", affiliation="Kasakura High School Teacher")
    
    show_story_box("", "He looked at me, serious.", is_narrator=True)
    show_story_box("Kojima-sensei", "Go back to your room. Sleep. We have a long day tomorrow.", affiliation="Kasakura High School Teacher")
    
    show_story_box("", "He walked away, carrying the ninja.", is_narrator=True)
    show_story_box("", "I stood in the hallway for a moment, staring at the closed VIP door.", is_narrator=True)
    show_story_box("", "‘Starguards’...\n‘Starry Eyed’...", is_narrator=True)
    show_story_box("", "I turned and headed for the cabins.", is_narrator=True)
    show_story_box("", "There was no way I was forgetting that.", is_narrator=True)

def play_stage_3_16_start():
    # --- SCENE 1: KAGAKU'S POV (THE MORNING AFTER) ---
    show_story_box("", "********* ◆ *********\nKagaku’s POV", is_narrator=True)
    show_story_box("", "The door creaked open at the exact same time as yesterday.", is_narrator=True)
    show_story_box("", "The young man in the sandy coat stepped in, balancing another silver tray.", is_narrator=True)
    
    show_story_box("Kagaku", "Room service is punctual, I see.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "He didn’t smile. He set the tray down on the low table.", is_narrator=True)
    show_story_box("", "Today’s menu: Fluffy souffle pancakes with fresh berries, maple syrup, and a side of crispy bacon. The smell was intoxicating.", is_narrator=True)
    
    show_story_box("Kagaku", "Wow. You really are wasted as a kidnapper. You should open a cafe.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Young Man", "Thank you.", affiliation="Unknown Faction")
    show_story_box("", "He bowed his head slightly—a simple, polite gesture that felt completely out of place given he was holding me prisoner.", is_narrator=True)
    show_story_box("", "He turned to the door. Hand on the handle.\nThen he stopped.", is_narrator=True)
    
    show_story_box("Young Man", "Enjoy the meal. Because tomorrow, we will proceed as planned.", affiliation="Unknown Faction")
    show_story_box("Kagaku", "Planned..? Oh.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Young Man", "The Boss arrives tomorrow. Have the anchor ready by then.", affiliation="Unknown Faction")
    
    show_story_box("", "The door clicked shut.", is_narrator=True)
    show_story_box("", "My appetite vanished instantly.\nTomorrow.\nThe word hung in the air like a guillotine blade.", is_narrator=True)
    show_story_box("", "I slumped back onto the sofa, staring at the pancakes.", is_narrator=True)
    
    show_story_box("Kagaku", "Tomorrow… means my deadline is up. My lies expire.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I pulled the diary out from under the cushion. I reread the note.", is_narrator=True)
    show_story_box("", "| Help is coming. Just stay alive. |", is_narrator=True)
    
    show_story_box("Kagaku", "‘Just stay alive’... easy for you to say! If I wait all the way for their Boss, I’m dead!", affiliation="Kasakura High School Student / Seven Wonders", is_thought=True)
    show_story_box("Kagaku", "I felt a flare of anger. Whoever wrote this… if I ever meet them, they are getting a stern lecture. And maybe a punch in the arm, damnit~!!", affiliation="Kasakura High School Student / Seven Wonders", is_thought=True)
    
    show_story_box("", "I looked at the blue pendant in my pocket.\nIt was still dull, looking ‘uncharged’.", is_narrator=True)
    show_story_box("", "But…did that ever matter?", is_narrator=True)
    show_story_box("", "I closed my eyes, running the theory through my head again.", is_narrator=True)
    show_story_box("", "The Anchor isn’t a battery. It’s a receiver.", is_narrator=True)
    show_story_box("", "Borrowing a ‘Kata’—contacting a self from another universe—doesn’t drain the jewel. It would drain me. The user. The energy comes from willpower and physical stamina.", is_narrator=True)
    show_story_box("", "It’s like… a smartphone.", is_narrator=True)
    
    show_story_box("Kagaku", "Using a phone…", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "The phone is always in your pocket, and let’s say it has a massive to infinite battery storage. You can make business calls whenever you want.", is_narrator=True)
    show_story_box("", "The limiting part isn’t the battery… it’s the conversations. Preparing the content. Negotiating with the other side. That’s what drains you.", is_narrator=True)
    show_story_box("", "Which meant… I didn’t need to wait.\nI could fight. Right now.", is_narrator=True)
    
    show_story_box("", "I looked at the four henchmen standing guard around the room. They looked bored. Complacent.", is_narrator=True)
    show_story_box("", "I took a deep breath.\nThen, I grabbed my throat.", is_narrator=True)
    
    show_story_box("Kagaku", "Guh—! Ack! Cough!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I doubled over, making the most horrific choking noises I could muster.", is_narrator=True)
    
    show_story_box("Henchman A", "Hey! What’s wrong?", affiliation="Unknown Faction")
    show_story_box("Henchman B", "Is she choking? The boss said not to damage her!", affiliation="Unknown Faction")
    
    show_story_box("", "They rushed over, panic in their eyes.\nCloser. Closer.", is_narrator=True)
    show_story_box("", "When they were within arm’s reach, I stopped coughing.", is_narrator=True)
    
    show_story_box("Kagaku", "...Here goes nothing..!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I focused.\nNot on a specific person. But on a concept.", is_narrator=True)
    show_story_box("", "I saw something, learned something. Discipline. Order. The standard infantry of Kasakura High.", is_narrator=True)
    show_story_box("", "Transformation. The familiar blue light was enveloping me this time.", is_narrator=True)
    show_story_box("", "Power surged through my limbs. My vision sharpened. My muscles hardened.", is_narrator=True)
    show_story_box("", "The henchmen froze.", is_narrator=True)
    
    show_story_box("Henchman A", "What the—!!", affiliation="Unknown Faction")
    
    show_story_box("", "I grabbed the heavy silver tray with one hand.\nWHAM!", is_narrator=True)
    show_story_box("", "I slammed it into a henchman’s face. He crumpled instantly.", is_narrator=True)
    
    show_story_box("Henchman B", "She’s armed! Get the weapons!", affiliation="Unknown Faction")
    
    show_story_box("", "I scrambled back, creating distance. My eyes darted around the room. I needed a weapon. A sword. A stick. Anything.", is_narrator=True)
    show_story_box("", "There. In the corner. A cleaning broom left by the maid service.", is_narrator=True)
    show_story_box("", "I grabbed it. Snap-kicked the bristle end off.\nNow I had a stick.", is_narrator=True)
    show_story_box("", "It felt… right. Like a bokken.", is_narrator=True)
    show_story_box("", "Another henchman lunged.", is_narrator=True)
    show_story_box("", "I parried, then immediately landed a hit with a loud crack.", is_narrator=True)
    show_story_box("", "Step in. Strike the wrist. Strike the temple.\nTHWACK– THWACK–", is_narrator=True)
    show_story_box("", "He went down.\nTwo left.\nThey hesitated.", is_narrator=True)
    
    show_story_box("Kagaku", "Alrighty…class…is in session.", affiliation="Kasakura High School Student / Seven Wonders")

def play_stage_3_16_end():
    # --- SCENE 2: KAGAKU'S ESCAPE ---
    show_story_box("", "It was messy. I wasn’t a fighter. My form was sloppy. I took a punch to the ribs that made me see stars.", is_narrator=True)
    show_story_box("", "But the Kata knew what to do. I just had to trust in it.", is_narrator=True)
    show_story_box("", "Minutes later, the room was silent. Four men lay unconscious on the expensive carpet.", is_narrator=True)
    show_story_box("", "I stood there, panting, clutching my broomstick.", is_narrator=True)
    
    show_story_box("Kagaku", "I… I did it.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I looked at the door.\nBeyond that must be an entire suite full of enemies.", is_narrator=True)
    show_story_box("", "I swallowed the lump in my throat.", is_narrator=True)
    
    show_story_box("Kagaku", "Time to go.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I opened the door and ran.", is_narrator=True)

    # --- SCENE 3: AKASUKE'S POV (ARRIVAL AT THE ISLAND) ---
    show_story_box("", "********* ◆ *********\nAkasuke’s POV", is_narrator=True)
    show_story_box("", "The sun was blinding.", is_narrator=True)
    show_story_box("", "The ferry ramp lowered, and the warm, tropical air of the private island hit us.", is_narrator=True)
    show_story_box("", "White sand. Palm trees. Crystal clear water.", is_narrator=True)
    show_story_box("", "Staff members were lined up on the dock, waving flags. It looked like paradise.", is_narrator=True)
    show_story_box("", "But I felt like a zombie.", is_narrator=True)
    show_story_box("", "I rubbed my eyes, suppressing a yawn.", is_narrator=True)
    
    show_story_box("Akasuke", "...So bright.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I hadn’t slept a wink. Every time I closed my eyes, I saw those neon blue star-pupils.", is_narrator=True)
    show_story_box("", "The “Starguards”.", is_narrator=True)
    show_story_box("", "My family’s instructors used to tell me: “There is always a bigger fish out there in the world.”", is_narrator=True)
    show_story_box("", "I thought I understood that. But seeing it… feeling that overwhelming pressure… it was different.", is_narrator=True)
    
    show_story_box("", "Yuri popped up beside me, peering into my face.", is_narrator=True)
    show_story_box("Yuri", "Akasuke-kun? Ya look terrible.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Akasuke", "Thanks. You look great.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Yuri", "I’m serious. Those bags under your eyes are heavy enough to carry luggage. Are ya okay? Maybe ya should see the infirmary first?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Her voice was soft. Genuine worry.\nIt cut through the fog in my brain.", is_narrator=True)
    show_story_box("", "I smiled, straightening up.", is_narrator=True)
    
    show_story_box("Akasuke", "I’m fine, Yuri. You know I wouldn’t lie to you about this. It’s just jet lag. Or… boat lag?", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Yuri", "Boat lag ain’t a thing.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "We laughed.\nThen I heard snickering.", is_narrator=True)
    show_story_box("", "I looked over. Naganohara, Nishida, Shigemura, and Yamashita were standing in a huddle nearby, watching us with grins plastered on their faces.", is_narrator=True)
    
    show_story_box("Naganohara", "Look at them~. Domestic dispute already?", affiliation="Kasakura High School Student")
    show_story_box("Yamashita", "Young love is so tiring~.", affiliation="Kasakura High School Student")
    
    show_story_box("", "Yuri turned beet red.", is_narrator=True)
    show_story_box("Yuri", "A-anyway! If ya say you’re fine then you’re fine! We’re dispersin’!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "She shoved me gently and ran off toward the girls. I walked away, scratching my head, feeling the heat in my cheeks.", is_narrator=True)
    
    show_story_box("Kojima-sensei", "Alright! Groups! NOW! Find your designated numbers!", affiliation="Kasakura High School Teacher")
    
    show_story_box("", "I looked at my slip of paper. Group 12.\nI headed to the designated palm tree.", is_narrator=True)

    # --- SCENE 4: MEETING GROUP 12 ---
    show_story_box("", "Three people were waiting.\nFirst, a girl from Kiryoku Gakuen.", is_narrator=True)
    show_story_box("", "She didn’t look like the fighters I’d met. She had long, lime-green hair and thick glasses. She was hugging a backpack to her chest.", is_narrator=True)
    
    show_story_box("Midori", "U-Um… nice to meet you. I’m Midori.", affiliation="Kiryoku Gakuen Student")
    show_story_box("Akasuke", "Hey. Akasuke. Nice to meet you.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Midori", "Y-You’re from Kasakura? Have you… have you seen Aina-sama recently?", affiliation="Kiryoku Gakuen Student")
    show_story_box("Akasuke", "Aina? The President?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Midori’s eyes lit up behind her glasses.", is_narrator=True)
    show_story_box("Midori", "Yes! The ‘Queen of Fairies’! I’m her biggest fan! I have all her merch! I wonder if she really glows?!", affiliation="Kiryoku Gakuen Student")
    
    show_story_box("", "I remembered the meeting. The brawl, with the sleeping child at the center of the entire room.", is_narrator=True)
    show_story_box("Akasuke", "Uh… yeah. She’s very… cute. And sleepy.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "Midori squealed quietly. Okay. She’s harmless. We can get along easily.", is_narrator=True)
    
    show_story_box("", "Next was a guy from Miyabi Academy.", is_narrator=True)
    show_story_box("", "He stood tall, posture perfect. Handsome in that effortless, rich-kid way.", is_narrator=True)
    show_story_box("", "But he was wearing a thick, fur-lined winter jacket over his uniform. On a tropical beach.", is_narrator=True)
    show_story_box("", "He smiled politely.", is_narrator=True)
    
    show_story_box("Fuyuki", "Greetings. I am Fuyuki. A pleasure to be in your group.", affiliation="Miyabi Academy Student")
    show_story_box("Akasuke", "Likewise. Uh… Fuyuki? Are you…not feeling hot?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "He frowned slightly, touching his collar.", is_narrator=True)
    show_story_box("Fuyuki", "My apologies. I have a… constitution. My body temperature runs impossibly low. Even this sun feels like a mild autumn breeze to me.", affiliation="Miyabi Academy Student")
    show_story_box("Akasuke", "Oh. That sounds rough.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Fuyuki", "It has its challenges. I hope my attire does not disturb the group dynamic.", affiliation="Miyabi Academy Student")
    show_story_box("Akasuke", "Not at all, man. You do you.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "He seemed chill. Literally and figuratively.", is_narrator=True)
    show_story_box("", "And finally… the Heiwa Seiritsu member.\nI turned around.", is_narrator=True)
    
    show_story_box("Heiwa Girl", "Oi. Found ya.", affiliation="Heiwa Seiritsu High School Student")
    
    show_story_box("", "I flinched.\nA delinquent. Great.", is_narrator=True)
    show_story_box("", "I mentally prepared for a fight. I turned—\nTHWACK.", is_narrator=True)
    show_story_box("", "She kicked me right in the shin. Hard.", is_narrator=True)
    
    show_story_box("Akasuke", "Ow! What was that for?!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "I looked up.", is_narrator=True)
    show_story_box("", "Messy black ponytail. Untidy uniform. Bandages on her wrists.", is_narrator=True)
    show_story_box("", "It was her.\nThe girl from the Heiwa infirmary. The one who patched me up after the Knight stabbed me.", is_narrator=True)
    
    show_story_box("???", "That’s for makin’ me look for ya. Do you know how hard it is to find a redhead in a crowd of idiots?", affiliation="Heiwa Seiritsu High School Student")
    show_story_box("", "She smirked, hands on her hips.", is_narrator=True)
    
    show_story_box("Akasuke", "You…", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "My tension melted away.", is_narrator=True)
    show_story_box("Akasuke", "You’re the one from the infirmary. Rara, right?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Rara", "Took ya long enough to remember.", affiliation="Heiwa Seiritsu High School Student")
    show_story_box("", "She looked me up and down, her expression softening just a fraction.", is_narrator=True)
    
    show_story_box("Rara", "So? You healed up? No holes in your chest anymore?", affiliation="Heiwa Seiritsu High School Student")
    show_story_box("Akasuke", "Yeah. Thanks to you.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Rara", "Good. Don’t go dyin’ on me during the trip, got it?", affiliation="Heiwa Seiritsu High School Student")
    
    show_story_box("", "She punched my arm. Friendly.", is_narrator=True)
    show_story_box("", "I rubbed my shin, smiling.", is_narrator=True)
    
    show_story_box("Akasuke", "Ah, yeah. Loud and clear.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Kojima-sensei", "Alright! Groups formed! Head to your assigned cabins and prepare for the Scavenger Hunt!", affiliation="Kasakura High School Teacher")
    show_story_box("", "Our group—an exhausted karateka, an otaku, a freezing rich kid, and a rough-edged nurse—headed into the island.", is_narrator=True)

def play_stage_3_17_start():
    # --- SCENE 1: AKASUKE'S POV (THE RESORT LOBBY & RULES) ---
    show_story_box("", "********* ◆ *********\nAkasuke’s POV", is_narrator=True)
    show_story_box("", "The resort lobby was a chaotic sea of luggage and excited students. After dumping our bags in the cabins, we gathered on the main lawn, where a jungle loomed ahead like a green wall.", is_narrator=True)
    
    show_story_box("", "Kojima-sensei stood on a crate, holding a megaphone.", is_narrator=True)
    show_story_box("Kojima-sensei", "Alright, listen up! The first activity of this ‘Goodwill Trip’ is a Scavenger Hunt!", affiliation="Kasakura High School Teacher")
    
    show_story_box("", "Groans from the lazy students. Cheers from the energetic ones.", is_narrator=True)
    
    show_story_box("Kojima-sensei", "The jungle has been cleared of threats. No bears, no tigers, and hopefully no hidden ninja clans. But it does have puzzles, riddles, and hidden items. You have five whole hours.", affiliation="Kasakura High School Teacher")
    
    show_story_box("", "He grinned—a smile that promised pain.", is_narrator=True)
    show_story_box("Kojima-sensei", "Fail to finish? Break the rules? FIGHTING? You’ll be spending the rest of this trip doing manual labor with me. And tonight, I’m looking for brave volunteers to stand guard outside the resort until dawn. Any takers?", affiliation="Kasakura High School Teacher")
    
    show_story_box("", "Silence. Absolute, terrified silence.", is_narrator=True)
    show_story_box("Kojima-sensei", "Didn’t think so. Now GET MOVING!", affiliation="Kasakura High School Teacher")

    # --- SCENE 2: THE SCAVENGER HUNT BEGINS ---
    show_story_box("", "Our group set off at a leisurely pace.", is_narrator=True)
    show_story_box("", "Midori, the Kiryoku otaku, was already panting five minutes in. She clutched her backpack straps, looking at the dense foliage with trepidation.", is_narrator=True)
    
    show_story_box("Akasuke", "Let’s take it slow. No need to rush. We solve the riddles as we go.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Rara", "Yeah. Fine by me. Runnin’ in sand sucks anyway.", affiliation="Heiwa Seiritsu High School Student")
    
    show_story_box("Fuyuki", "I appreciate the consideration, Akasuke-kun. The humidity is… stifling.", affiliation="Miyabi Academy Student")
    show_story_box("", "He was still wearing that thick winter jacket. Just looking at him made me sweat.", is_narrator=True)
    
    show_story_box("", "We ticked off items on the list one by one. A specific shell. A photo of a rare bird. A coconut with a smiley face carved into it.", is_narrator=True)
    show_story_box("", "Along the path, we bumped into other groups.", is_narrator=True)

    # --- SCENE 3: BUMPING INTO FRIENDS ---
    show_story_box("", "Yuri-chan waved from a clearing. She was surrounded by three girls—one from each school—who were all gushing over her.", is_narrator=True)
    
    show_story_box("Yuri", "Hey, Akasuke-kun! Look what we found!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "She held up a bright blue flower. Her groupmates were fixing her hair and asking about her workout routine.", is_narrator=True)
    
    show_story_box("Akasuke", "Looks like you’re popular, Yuri.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Yuri", "They’re fashion fans I can’t understand like Naganohara…but they think I’m ‘cool’. Being a leader is exhausting, but not bad!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "She beamed. I waved goodbye and moved on.", is_narrator=True)
    
    show_story_box("", "A bit further down, we found Shigemura.", is_narrator=True)
    show_story_box("", "He looked miserable.", is_narrator=True)
    show_story_box("", "His group consisted of a Heiwa thug who wouldn’t stop talking about his motorcycle, a Kiryoku fighter who kept challenging the thug to arm wrestles, and a Miyabi girl who… just smiled.", is_narrator=True)
    show_story_box("", "She had that \"anime closed-eyes\" look. Graceful. Silent. Unreadable.", is_narrator=True)
    
    show_story_box("Shigemura", "...Kill me.", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "Good luck, buddy.", affiliation="Kasakura High School Student / Seven Wonders")

    # --- SCENE 4: THE MONSTER ENCOUNTER ---
    show_story_box("", "Our next clue led us to a small clearing where a \"Monster\" waited.", is_narrator=True)
    show_story_box("", "It was obviously a Kasakura senior in a cheap ‘Zodgilla’ costume.", is_narrator=True)
    
    show_story_box("Deadly Laser Beam World-Threatening Monster", "ROAR! To pass, you must defeat the Guardian of the Coconut!", affiliation="Kasakura High School Senior")
    
    show_story_box("", "Rara rolled her eyes. Midori hid behind Fuyuki.", is_narrator=True)
    
    show_story_box("Akasuke", "I got this.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "I stepped forward. The senior winked through the eyehole.", is_narrator=True)


def play_stage_3_17_end():
    # --- SCENE 5: AFTER THE "BATTLE" ---
    show_story_box("", "We \"sparred\". I threw a slow-motion punch. He did a dramatic backflip and collapsed.", is_narrator=True)
    
    show_story_box("Deadly Laser Beam World-Threatening Monster", "GAAH! The hero is too strong! Take the loot!", affiliation="Kasakura High School Senior")
    
    show_story_box("", "Midori clapped her hands, eyes sparkling.", is_narrator=True)
    show_story_box("Midori", "So cool, Akasuke-san! Just like an anime protagonist!", affiliation="Kiryoku Gakuen Student")
    
    show_story_box("Rara", "You guys are dorks.", affiliation="Heiwa Seiritsu High School Student")
    show_story_box("", "But she was smiling.", is_narrator=True)
    
    show_story_box("", "As we walked, I noticed something surprising. Rara—the rough delinquent nurse—was actually listening quite well to Midori.", is_narrator=True)
    
    show_story_box("Midori", "...and then Aina-sama sneezed! It was the cutest sound in the universe! Like a kitten!", affiliation="Kiryoku Gakuen Student")
    show_story_box("Rara", "Yeah? ‘Must be nice having a cute president. Our ‘Upperclassmen’ just grunt and break stuff.", affiliation="Heiwa Seiritsu High School Student")
    show_story_box("Midori", "OH! but the gap moe! You know?! Scary guys being clumsy is cute too!", affiliation="Kiryoku Gakuen Student")
    
    show_story_box("", "Rara laughed.", is_narrator=True)
    
    show_story_box("", "I fell back to walk beside Fuyuki.", is_narrator=True)
    show_story_box("Akasuke", "You holding up okay, man? That coat…", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Fuyuki", "Ahaha…I am managing. Thank you.", affiliation="Miyabi Academy Student")
    
    show_story_box("Akasuke", "So, Miyabi Academy. What’s it actually like? We hear rumors about science clubs and tech.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Fuyuki", "Ah, it is… focused. Yes, our programs are advanced. Robotics, chemistry, bio-engineering.", affiliation="Miyabi Academy Student")
    show_story_box("Akasuke", "And the Student Council? Do you guys have one?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Fuyuki paused.", is_narrator=True)
    show_story_box("Fuyuki", "Hmm, we do, but their operations are opaque. Even to me. I fear I cannot tell you much about the system.", affiliation="Miyabi Academy Student")
    
    show_story_box("", "His tone was polite, and final. I decided not to push.", is_narrator=True)
    show_story_box("Akasuke", "No worries. Just curious.", affiliation="Kasakura High School Student / Seven Wonders")

    # --- SCENE 6: THE REST STATION & THE SUMMONS ---
    show_story_box("", "Two hours in.\nWe reached a rest station—a large tent with coolers full of drinks.", is_narrator=True)
    
    show_story_box("Staff Teacher", "Great work, everyone! Take a break!", affiliation="Joint School Staff")
    
    show_story_box("", "Rara flopped onto the grass, pulling Midori down with her. Midori was napping in seconds, head on Rara’s lap.", is_narrator=True)
    
    show_story_box("Akasuke", "I’ll grab drinks.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "I walked to the cooler. A teacher handed me four sports bottles, then leaned in.", is_narrator=True)
    
    show_story_box("Staff Teacher", "Hanefuji, right? Kojima-sensei wants to see you. He’s at the staff tent.", affiliation="Joint School Staff")
    
    show_story_box("", "I nodded.", is_narrator=True)
    show_story_box("Akasuke", "Hey guys! I… uh… need to use the specialized restroom! Back in a bit!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Rara waved me off without looking up.", is_narrator=True)

    # --- SCENE 7: THE STAFF TENT ---
    show_story_box("", "Kojima’s Staff Tent\nKojima-sensei was sitting at a folding table covered in maps.", is_narrator=True)
    
    show_story_box("Kojima-sensei", "Good. You’re here.", affiliation="Kasakura High School Teacher")
    show_story_box("", "He pointed to a spot on the map—a far corner of the island.", is_narrator=True)
    
    show_story_box("Kojima-sensei", "The Disciplinary Committee advance team found something. There’s a hotel in the shopping district. Not around the main resort. A smaller, less well-known one.", affiliation="Kasakura High School Teacher")
    show_story_box("Akasuke", "The enemy?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Kojima-sensei", "We checked the guest logs. Names match the aliases used by the infiltrators we caught last night. It’s too frequent to be a coincidence.", affiliation="Kasakura High School Teacher")
    show_story_box("", "He frowned.", is_narrator=True)
    show_story_box("Kojima-sensei", "We tried to send a team in. Hotel staff blocked them. Aggressively. If we push harder, we risk starting a war in a civilian area. But we think they must be in there.", affiliation="Kasakura High School Teacher")
    
    show_story_box("", "I peeked into the back of the tent.\nNatsume was there.", is_narrator=True)
    show_story_box("", "She was buried in a mountain of pillows, plushies, and snacks, surrounded by military-grade communication servers. She gave me a lazy thumbs-up.", is_narrator=True)
    
    show_story_box("Natsume", "Yo. This is the life. No hiking for me.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Kojima-sensei", "She’s here as support, obviously. I’m keeping her here where it’s safe. You go back to your group. Continue to act normal for the day. But be ready.", affiliation="Kasakura High School Teacher")

    # --- SCENE 8: THE RETURN & SUSPICION ---
    show_story_box("", "I jogged back toward the rest area.\nThe path was narrow, winding through thick ferns.", is_narrator=True)
    show_story_box("", "Suddenly, I saw someone ahead.\nWalking the same direction. Same winter coat.", is_narrator=True)
    
    show_story_box("Akasuke", "Fuyuki?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "He stiffened. He turned around slowly.", is_narrator=True)
    show_story_box("Fuyuki", "Ah. Akasuke-kun.", affiliation="Miyabi Academy Student")
    
    show_story_box("Akasuke", "Where were you? You weren’t at the rest spot.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Fuyuki", "I needed the restroom as well. My condition affects my metabolism, I apologize.", affiliation="Miyabi Academy Student")
    show_story_box("Akasuke", "Right.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "We walked back together.\nWhen we reached the group, Rara glared at us.", is_narrator=True)
    
    show_story_box("Rara", "OI! Where the hell were you two?!", affiliation="Heiwa Seiritsu High School Student")
    show_story_box("", "She pointed at her watch.", is_narrator=True)
    show_story_box("Rara", "Thirty minutes! You left me here with Sleeping Beauty for thirty minutes!", affiliation="Heiwa Seiritsu High School Student")
    
    show_story_box("Akasuke", "Sorry! The line was long!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Fuyuki", "Apologies..! Health reasons.", affiliation="Miyabi Academy Student")
    
    show_story_box("", "Rara sighed, shaking Midori awake.", is_narrator=True)
    show_story_box("Rara", "Whatever. Let’s just finish this.", affiliation="Heiwa Seiritsu High School Student")
    
    show_story_box("", "Fuyuki smiled his usual polite smile.\nBut as I looked at him…", is_narrator=True)
    show_story_box("", "Thirty minutes? For a restroom break? Just as I was meeting Kojima?", is_narrator=True)
    show_story_box("", "A cold feeling settled in my gut. And it wasn’t from his jacket.", is_narrator=True)

def play_stage_3_18_story():
    # --- SCENE 1: THE FOOD STALLS (AKASUKE'S COMEDIC CRITIQUE) ---
    show_story_box("", "********* ◆ *********\nAkasuke’s POV", is_narrator=True)
    show_story_box("", "We finished the scavenger hunt with an hour to spare.", is_narrator=True)
    show_story_box("", "Our group sat at a rest area filled with food stalls, the smell of yakisoba and takoyaki wafting through the air.", is_narrator=True)
    
    show_story_box("Akasuke", "...Now, observe the takoyaki. The exterior crispness is essential, providing a textural counterpoint to the molten interior. However, this particular vendor has over-sauced, drowning the delicate umami of the bonito flakes in a sea of unnecessary sweetness. A tragedy, really.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Midori blinked, holding her skewer.", is_narrator=True)
    show_story_box("Midori", "Um… Akasuke-san? It’s just octopus balls.", affiliation="Kiryoku Gakuen Student")
    
    show_story_box("Fuyuki", "I find the heat distribution quite adequate.", affiliation="Miyabi Academy Student")
    show_story_box("Rara", "Just eat the damn food, Akasuke.", affiliation="Heiwa Seiritsu High School Student")
    
    show_story_box("", "I was about to launch into a dissertation on the proper viscosity of mayonnaise when a student sprinted up to our table.", is_narrator=True)
    show_story_box("", "He wore a Kasakura uniform for disguise, but his face was pale and sweating.", is_narrator=True)
    
    show_story_box("Committee Member A", "Hanefuji! Kojima-sensei needs you. Now. Urgent.", affiliation="Kasakura High School Disciplinary Committee")
    
    show_story_box("", "Midori tilted her head.", is_narrator=True)
    show_story_box("Midori", "Again? Why are you always getting called away? Are you secretly a spy?", affiliation="Kiryoku Gakuen Student")
    
    show_story_box("", "Rara snorted, taking a bite of her yakisoba.", is_narrator=True)
    show_story_box("Rara", "Spy? Nah. He’s just a big shot. So called legendary fighter of Kasakura. The guy who stopped the Heiwa Seiritsu raid and stuff.", affiliation="Heiwa Seiritsu High School Student")
    show_story_box("", "She smirked at me.", is_narrator=True)
    show_story_box("Rara", "Honestly, I’m glad I retreated before meeting you in battle that day. It would've ended badly for me.", affiliation="Heiwa Seiritsu High School Student")
    
    show_story_box("", "Midori dropped her skewer.", is_narrator=True)
    show_story_box("Midori", "Ehh?! Rara-chan, you were in the raid?!", affiliation="Kiryoku Gakuen Student")
    
    show_story_box("", "Rara froze.", is_narrator=True)
    show_story_box("Rara", "Uh… I mean… I heard about it! Yeah! Heard the stories! Scary stuff!", affiliation="Heiwa Seiritsu High School Student")
    show_story_box("", "She looked at me, eyes pleading. Save me.", is_narrator=True)
    
    show_story_box("Akasuke", "Yeah. Rara has a… vivid imagination. She writes fanfiction about battles. Right?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Rara", "YES! Fanfiction! Huge nerd! That’s me! I just wanted a taste of that battle!!", affiliation="Heiwa Seiritsu High School Student")
    
    show_story_box("", "Midori’s eyes sparkled.", is_narrator=True)
    show_story_box("Midori", "Really?! Can I read it sometime? Do you write romance too!?", affiliation="Kiryoku Gakuen Student")
    
    show_story_box("", "Rara groaned, burying her face in her hands. Fuyuki sipped his tea, looking completely indifferent.", is_narrator=True)
    show_story_box("Akasuke", "Anyways…sorry, guys. Duty calls.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I grabbed my bag and ran.", is_narrator=True)

    # --- SCENE 2: KOJIMA'S STAFF TENT (THE BRIEFING) ---
    show_story_box("", "Kojima’s Staff Tent\nKojima-sensei was pacing when I arrived. He looked agitated.", is_narrator=True)
    
    show_story_box("Kojima-sensei", "The advance team reported sounds of battle from the hotel. Commotion inside. Someone is fighting.", affiliation="Kasakura High School Teacher")
    show_story_box("Akasuke", "Kagaku?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Kojima-sensei", "Has to be. She’s making her move.", affiliation="Kasakura High School Teacher")
    show_story_box("", "He slammed a hand on the table.", is_narrator=True)
    show_story_box("Kojima-sensei", "Permission granted. You, Yuri, Benikawa, Shigemura, Naganohara, and Natsume are cleared to engage. Full force.", affiliation="Kasakura High School Teacher")
    
    show_story_box("", "I blinked.", is_narrator=True)
    show_story_box("Akasuke", "Wait. Naganohara?", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "I looked behind me.", is_narrator=True)
    
    show_story_box("", "Shigemura, Yuri, Benikawa, and Naganohara stepped into the tent. They were already changing into proper uniforms (or in Naganohara’s case, tightening her sneakers).", is_narrator=True)
    
    show_story_box("Akasuke", "Shigemura…I get you, but why is she here? It’s dangerous.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Naganohara stepped up, fists clenched.", is_narrator=True)
    show_story_box("Naganohara", "I-I volunteered! I can use Katas too, remember? I-I can help!", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "But—", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Shigemura", "She stays.", affiliation="Kasakura High School Student")
    show_story_box("", "His voice was firm. Serious.", is_narrator=True)
    show_story_box("Shigemura", "I will protect her.", affiliation="Kasakura High School Student")
    
    show_story_box("", "Benikawa leaned against a crate, smirking.", is_narrator=True)
    show_story_box("Benikawa", "Ninja rule: A ninja can take on two missions at once. And he takes them seriously.", affiliation="Benikawa Ninja Clan")
    show_story_box("", "She nudged Shigemura.", is_narrator=True)
    show_story_box("Benikawa", "Protecting the girl’s one of them. Right, Shigemura?", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "Shigemura realized what he’d just said. His face turned bright red.", is_narrator=True)
    show_story_box("Shigemura", "I… that came out wrong. I meant strategically… as an asset…", affiliation="Kasakura High School Student")
    
    show_story_box("", "Naganohara was blushing too, twirling a lock of hair.", is_narrator=True)
    show_story_box("Naganohara", "O-Oh. Okay. Thanks, Shigemura-kun.", affiliation="Kasakura High School Student")
    
    show_story_box("", "Yuri elbowed me, grinning.", is_narrator=True)
    show_story_box("Yuri", "They’re totally compatible, huh?", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Akasuke", "Totally.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I turned back to them.", is_narrator=True)
    show_story_box("Akasuke", "Alright. Shigemura, you stick to Naganohara like glue. We’ll also help watch your backs.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Shigemura nodded, regaining his composure, mostly.", is_narrator=True)
    show_story_box("Shigemura", "...Understood.", affiliation="Kasakura High School Student")
    
    show_story_box("", "Natsume waved from her pillow fort.", is_narrator=True)
    show_story_box("Natsume", "Good luck out there~. I’ll guide you from here.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Kojima-sensei threw a bundle of clothes at her.", is_narrator=True)
    show_story_box("Kojima-sensei", "Nope. Get dressed. You’re working outside. Fresh air helps focus.", affiliation="Kasakura High School Teacher")
    show_story_box("Natsume", "Ughhhhhh. Worst field trip ever.", affiliation="Kasakura High School Student / Seven Wonders")

    # --- SCENE 3: KAGAKU'S POV (THE DESCENT) ---
    show_story_box("", "********* ◆ *********\nKagaku’s POV", is_narrator=True)
    show_story_box("", "Hotel Corridor – 14th Floor", is_narrator=True)
    show_story_box("Kagaku", "Hah… hah… why… are there… so many stairss?!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I swung the broken broom handle.\nWhack!\nAnother henchman went down.", is_narrator=True)
    show_story_box("", "I had been running for an hour. Fighting my way down from the top floor. But every stairwell was blocked. Every elevator was locked down.", is_narrator=True)
    
    show_story_box("Kagaku", "I’m a scientist! Not an action hero! This sucks!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "My transformation was flickering. My muscles burned. My lungs felt like they were full of broken glass.", is_narrator=True)
    show_story_box("", "I turned the corner—and ran straight into him.", is_narrator=True)
    show_story_box("", "The sandy coat. The rapier.\nHe stood there, calm as ever.", is_narrator=True)
    
    show_story_box("Young Man", "You’ve caused quite a mess.", affiliation="Unknown Faction")
    show_story_box("Kagaku", "Out of my way!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I swung the broom.\nHe stepped inside my guard effortlessly. A blur of motion.\nThud.", is_narrator=True)
    show_story_box("", "He swept my legs. I hit the carpet hard. Before I could scramble up, the tip of his rapier was at my throat.", is_narrator=True)
    
    show_story_box("Young Man", "Enough.", affiliation="Unknown Faction")
    
    show_story_box("", "The transformation faded. I shrank back to my normal, exhausted self.", is_narrator=True)
    show_story_box("Kagaku", "I… I give up. Fighting is terrible. 0/10. ‘Would not recommend.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "He sheathed his sword and scooped me up like a bag of rice.", is_narrator=True)
    show_story_box("Young Man", "You’re going back to the interrogation room.", affiliation="Unknown Faction")
    
    show_story_box("", "He carried me down the hall. I was too tired to struggle.", is_narrator=True)
    show_story_box("", "Just as we reached the suite door, a henchman sprinted up the stairs.", is_narrator=True)
    
    show_story_box("Henchman A", "Sir! Emergency! Enemy forces have breached the lobby! They’re pushing hard!", affiliation="Unknown Faction")
    
    show_story_box("", "The man stopped.", is_narrator=True)
    show_story_box("Young Man", "Already?", affiliation="Unknown Faction")
    show_story_box("", "He looked at me, then at the door.", is_narrator=True)
    show_story_box("", "He dumped me onto a velvet sofa in the hallway lounge area.", is_narrator=True)
    
    show_story_box("Young Man", "Stay here.", affiliation="Unknown Faction")
    show_story_box("", "He reached into my pocket and snatched the blue pendant.", is_narrator=True)
    
    show_story_box("Kagaku", "Hey!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Young Man", "I don’t have time to tie you up. Don’t move.", affiliation="Unknown Faction")
    
    show_story_box("", "He turned and ran for the stairs, coat billowing behind him.", is_narrator=True)
    show_story_box("", "I lay there, staring at the ceiling.", is_narrator=True)
    
    show_story_box("Kagaku", "...He took the anchor.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Kagaku", "But the door's still open.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I sat up slowly.", is_narrator=True)
    show_story_box("Kagaku", "Help is here, right?", affiliation="Kasakura High School Student / Seven Wonders")

def play_stage_3_19_start():
    # --- SCENE 1: AKASUKE'S POV (THE LOBBY BREACH) ---
    show_story_box("", "********* ◆ *********\nAkasuke’s POV", is_narrator=True)
    show_story_box("", "The hotel lobby doors exploded inward.", is_narrator=True)
    show_story_box("", "We didn’t knock. We didn’t sneak. We crashed through the front entrance like a natural disaster.", is_narrator=True)
    
    show_story_box("", "Four guards in sandy-colored coats stood by the reception desk. They barely had time to draw their weapons before Benikawa and Yuri were on them.", is_narrator=True)
    show_story_box("", "CRASH!\nBAM!\nBodies hit the marble floor.", is_narrator=True)
    
    show_story_box("", "But the alarm was already blaring. From the corridors, the elevators, the staff rooms—more men poured in. Same coats. Same thin, needle-like swords.", is_narrator=True)
    
    show_story_box("Yuri", "There’s so many of ‘em! Is this a hotel or a barracks?!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "A wave of enemies rushed us. Rapiers flashed like silver lightning.", is_narrator=True)
    
    show_story_box("Benikawa", "Formation! Protect the ‘VIP’s!", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "Shigemura stepped in front of Naganohara, deflecting a thrust with his reinforced gloves. Naganohara, to her credit, didn’t shrink back. She threw an enhanced punch over his shoulder, knocking a guy’s teeth out, expression already serious, assuming another Kata’s.", is_narrator=True)
    show_story_box("", "Just as we were about to get bogged down, the glass windows shattered.", is_narrator=True)
    
    show_story_box("Committee Member A", "Reinforcements have arrived!", affiliation="Kasakura High School Disciplinary Committee")
    show_story_box("Committee Member B", "Push them back!", affiliation="Kasakura High School Disciplinary Committee")
    
    show_story_box("", "A squad of Disciplinary Committee members—armed with stun batons and light riot shields—rappelled in or vaulted the window sills. They formed a shield wall, driving the sandy-coats back.", is_narrator=True)
    
    show_story_box("Committee Member A", "Hanefuji-san! Go! We’ll hold the ground floor!", affiliation="Kasakura High School Disciplinary Committee")
    
    show_story_box("Akasuke", "You guys are lifesavers! Come on!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "We sprinted for the elevator bank.", is_narrator=True)
    
    show_story_box("Shigemura", "Akasuke! The elevator is faster!", affiliation="Kasakura High School Student")
    show_story_box("Akasuke", "No! We don’t know what floor Kagaku is on! If we bypass her, we might never find her!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I kicked the door to the stairwell open.", is_narrator=True)
    
    show_story_box("Akasuke", "We take the stairs! Floor by floor! We check every nook and cranny!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Benikawa", "Cardio workout from hell, huh~. Got it.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("", "We charged up the stairs.\nBeep.\nNatsume’s voice crackled in our ears. Clear. Calm.", is_narrator=True)
    
    show_story_box("Natsume", "I’ve ID’d them. Sandy coats. Rapiers. Organized movements…Akasuke, listen closely.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Akasuke", "Kinda busy punching people, Natsume!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I ducked under a rapier thrust and slammed my elbow into a guy’s ribs. He grunted but didn’t go down. They were all tough so far.", is_narrator=True)
    
    show_story_box("Natsume", "Make time. You need to know what you’re fighting. Have you heard of the term ‘Absconders’?", affiliation="Kasakura High School Student / Seven Wonders")

    # --- SCENE 2: THE ABSCONDERS EXPLAINED ---
    show_story_box("", "We reached the second-floor landing. More enemies waiting.", is_narrator=True)
    
    show_story_box("Yuri", "Absconders? Like… runaways?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Natsume", "In the underworld, it’s a classification. Delinquent groups. High schoolers who stepped off the moral path and never could look back. They aren’t just bullies. They’re criminals at that point.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Natsume", "From petty thieves to full-blown organized criminal syndicates. The kidnapping ring you busted months ago? That was just the tip of the iceberg. They were low-level Absconders working for the larger system.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I parried a blade with my forearm guard. The steel sparked.", is_narrator=True)
    
    show_story_box("Akasuke", "And these guys?", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Natsume", "They’re the ‘Riposte Gang’. Popular lately. They do kidnapping, smuggling, and shady bodyguard work.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Natsume", "Their style is in the name. ‘Riposte’. They don’t block. They counter.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "As she said it, I watched Shigemura engage a henchman.\nShigemura threw a jab. The henchman didn’t dodge. He took the hit on his shoulder, flinching slightly, but used that split second to lunge.\nHis rapier darted forward—aiming right for Shigemura’s throat.\nBenikawa threw a shuriken, deflecting the blade just in time.", is_narrator=True)
    
    show_story_box("Benikawa", "They’re baiting us! They take a hit to create an opening!", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Natsume", "Exactly. They’re tough. They sacrifice defense for a guaranteed lethal strike. Piercing attacks to vital points. If you attack sloppily, they’ll trade a bruise for your life.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Akasuke", "So we don’t give them the chance to trade.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I grit my teeth. Blue light flared around my fists.", is_narrator=True)
    
    show_story_box("Akasuke", "We’ll do things with one hit. Heavy enough to shut the lights out instantly.", affiliation="Kasakura High School Student / Seven Wonders")


def play_stage_3_19_end():
    # --- SCENE 3: THE FIGHT CONTINUES ---
    show_story_box("", "We hit the third floor corridor. A dozen Riposte members blocked the hall.", is_narrator=True)
    
    show_story_box("Akasuke", "Yuri! Smash them!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Yuri", "On it!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "She charged, slamming two guys together like cymbals. They dropped instantly. No chance to counter.\nI moved to the next one.\nHe raised his rapier, stance loose, inviting me in.\nI didn’t hesitate. I stepped in deep, ignoring the tip of his blade hovering near my eye.\nBOOM.\nA straight right to the jaw.\nHe folded like a lawn chair.", is_narrator=True)
    
    show_story_box("Akasuke", "Next!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Another one stepped up. I swung a hook.\nHe stepped into it.\nMy fist connected with his forehead—hard—but people’s skulls are thick. He didn’t drop.\nHis eyes widened. He grinned through the blood.", is_narrator=True)
    
    show_story_box("Riposte Henchman", "Gotcha!!", affiliation="Riposte Gang")
    
    show_story_box("", "Zip.\nHis rapier flashed.\nI tried to pull back, but I was overextended.\nA line seared across my torso. The blade sliced through my shirt and skin.", is_narrator=True)
    
    show_story_box("Akasuke", "Guh—!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "I stumbled back.", is_narrator=True)
    
    show_story_box("Yuri", "Akasuke-kun!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "She looked terrified, seeing the blood welling up on my white shirt.\nThe henchman raised his sword for the finisher.\nI didn’t let him take it.\nI planted my foot. Ignored the pain. And drove a front kick into his solar plexus.\nHe flew backward, crashing through a hotel room door.\nI clutched my torso, breathing heavily.\nYuri was at my side in a second.", is_narrator=True)
    
    show_story_box("Yuri", "You’re bleedin’! That’s deep!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I checked the wound. It stung like crazy, but…", is_narrator=True)
    show_story_box("Akasuke", "It’s fine. Just a scratch.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Yuri", "A scratch?! He sliced you!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Akasuke", "I flexed my abs right before impact. Muscle density stopped it from hitting anything important.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "I gave her a thumbs up, though my hand was shaking slightly.", is_narrator=True)
    show_story_box("Akasuke", "See? shallow.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Yuri looked like she wanted to hit me herself, but she nodded, her eyes fierce.", is_narrator=True)
    show_story_box("Yuri", "Don’t scare me like that, idiot.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Benikawa kicked a downed enemy out of the way.", is_narrator=True)
    show_story_box("Benikawa", "Save the flirting for later! We have ten more floors to go!", affiliation="Benikawa Ninja Clan")
    show_story_box("Akasuke", "Huh?! R-right, let’s move!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "We pushed upward. Leaving a trail of unconscious bodies and shattered drywall in our wake.", is_narrator=True)

def play_stage_3_20_start():
    # --- SCENE 1: AKASUKE'S POV (THE 6TH FLOOR CORRIDOR) ---
    show_story_box("", "********* ◆ *********\nAkasuke’s POV", is_narrator=True)
    show_story_box("", "6th Floor Corridor\nThe hallway was a choke point of flashing steel.", is_narrator=True)
    
    show_story_box("Riposte Squad Leader", "Don’t let them pass! Pin them down!", affiliation="Riposte Gang")
    
    show_story_box("", "The man shouting orders wasn’t like the others. His coat was darker, his stance lower. A seasoned veteran.", is_narrator=True)
    show_story_box("", "Behind him, the elevator dinged. Two more men with the same dark coats stepped out.", is_narrator=True)
    
    show_story_box("Natsume", "Akasuke! Two more Squad Leaders! These guys are full-blown career criminals! Be careful!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Yuri", "Guh! There’s no end to ‘em!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "We were stalling. Even with our Katas, the sheer number of blades coming from every angle was overwhelming.", is_narrator=True)
    show_story_box("", "My breath hitched.", is_narrator=True)
    show_story_box("", "For a split second, the hotel corridor faded.", is_narrator=True)
    
    show_story_box("Akasuke", "I see a vision of the VIP room on the ship. The white suits. The neon blue star-shaped pupils staring through me.", affiliation="Kasakura High School Student / Seven Wonders", is_thought=True)
    show_story_box("Akasuke", "“There is always a bigger fish.”", affiliation="Kasakura High School Student / Seven Wonders", is_thought=True)
    show_story_box("Akasuke", "My instructors’ voices echoed in my head. The Starguards… these Riposte leaders… the Knight…", affiliation="Kasakura High School Student / Seven Wonders", is_thought=True)
    
    show_story_box("", "My movements slowed. A rapier grazed my cheek.", is_narrator=True)
    
    show_story_box("Yuri", "Akasuke-kun!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "She slammed a henchman into the wall, then grabbed my shoulder, shaking me.", is_narrator=True)
    
    show_story_box("Yuri", "Snap out of it! You’re spacin’ out again! Look at me!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I blinked. Yuri’s fierce, worried eyes filled my vision.", is_narrator=True)
    
    show_story_box("Yuri", "Whatever you’re scared of… it ain’t here right now! We are!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Akasuke", "...Right.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I took a deep breath. The cold dread in my chest loosened.", is_narrator=True)
    
    show_story_box("Akasuke", "She was right. I have a duty. I have to protect the peace. Protect them.", affiliation="Kasakura High School Student / Seven Wonders", is_thought=True)
    
    show_story_box("", "I looked at the Riposte Squad Leader.", is_narrator=True)
    show_story_box("", "His movements… the counter-riposte style… the rhythm…", is_narrator=True)
    show_story_box("", "I closed my eyes.\nI can see it.", is_narrator=True)
    
    show_story_box("Akasuke", "...Dispelling Kata.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "The blue aura around me vanished.", is_narrator=True)
    
    show_story_box("Natsume", "Akasuke?! What are you doing?! You’ll get skewered!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Akasuke", "No. I’m adapting.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I focused. Not on my own alternate self… but on the form in front of me.", is_narrator=True)
    show_story_box("", "Sharp. Precise. Ruthless.\nBorrow the Kata.", is_narrator=True)
    show_story_box("", "Power surged back—but it felt different. Sharper. Lighter.", is_narrator=True)
    show_story_box("", "I opened my eyes. My stance shifted automatically. One hand behind my back, the other extended like I was holding a blade.", is_narrator=True)
    
    show_story_box("Natsume", "You… you borrowed a Riposte Gang Leader’s?! That’s crazy! But…mixing Katas like that is reckless!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Akasuke", "Being crazy…works.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "The Squad Leader lunged.", is_narrator=True)
    show_story_box("", "I didn’t block. I stepped into his guard—mirroring his own technique—and drove a stiffened hand into his throat.", is_narrator=True)
    show_story_box("", "It worked. I see the vision of training your counterattacks.", is_narrator=True)
    show_story_box("", "He collapsed.", is_narrator=True)
    
    show_story_box("Akasuke", "Push forward! Now!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Using their own techniques against them, we carved a path to the stairwell.", is_narrator=True)

    # --- SCENE 2: THE 8TH FLOOR LANDING & NAGANOHARA ---
    show_story_box("", "8th Floor Landing\nWe burst onto the eighth floor, panting but moving with renewed momentum.", is_narrator=True)
    
    show_story_box("Naganohara", "Woah… Akasuke-kun was so cool! Changing forms like bam!", affiliation="Kasakura High School Student")
    show_story_box("", "She stopped, eyes lighting up.", is_narrator=True)
    show_story_box("Naganohara", "I…I want to try too!", affiliation="Kasakura High School Student")
    
    show_story_box("Shigemura", "Naganohara..?!, wait—", affiliation="Kasakura High School Student")
    show_story_box("", "She closed her eyes.", is_narrator=True)
    
    show_story_box("Naganohara", "Transformation!", affiliation="Kasakura High School Student")
    show_story_box("", "Her aura shifted. Her stance dropped low, mimicking the Squad Leaders we just fought.", is_narrator=True)
    
    show_story_box("Naganohara", "I feel it! I’m, like, totally a gang leader now!", affiliation="Kasakura High School Student")
    
    show_story_box("", "She pointed at a figure standing calmly at the end of the hall.", is_narrator=True)
    show_story_box("", "He wasn’t attacking. He was just watching.", is_narrator=True)
    
    show_story_box("Naganohara", "There’s another one! I got him!", affiliation="Kasakura High School Student")
    show_story_box("Shigemura", "Huh?! Don’t engage! Something’s wrong with that one!", affiliation="Kasakura High School Student")
    
    show_story_box("", "Too late. She dashed forward.\nThe figure didn’t flinch.", is_narrator=True)
    show_story_box("", "As Naganohara threw a punch, the man simply side-stepped—a movement so graceful it looked like he was dancing—and drove the hilt of his rapier into her stomach. Multiple times.", is_narrator=True)
    
    show_story_box("Naganohara", "Gah—!", affiliation="Kasakura High School Student")
    
    show_story_box("", "She stumbled back, gasping.\nThe man raised his blade for a follow-up thrust.", is_narrator=True)
    show_story_box("", "CLANG!", is_narrator=True)
    
    show_story_box("", "Shigemura was there. He caught the rapier blade between his reinforced gloves, sparks flying.", is_narrator=True)
    
    show_story_box("Shigemura", "I told you not to rush!", affiliation="Kasakura High School Student")
    show_story_box("", "He shoved the man back, shielding Naganohara.", is_narrator=True)
    show_story_box("Shigemura", "Are you okay?", affiliation="Kasakura High School Student")
    
    show_story_box("Naganohara", "Y-Yeah… the Kata’s toughness shielded the damage… but he’s strong…", affiliation="Kasakura High School Student")
    show_story_box("Shigemura", "Of course he is. Look at him.", affiliation="Kasakura High School Student")
    
    show_story_box("", "Shigemura glared at the enemy, then his friends, then glanced back at her.", is_narrator=True)
    
    show_story_box("Shigemura", "We aren’t monsters like Akasuke or Benikawa. We have to work together.", affiliation="Kasakura High School Student")
    show_story_box("", "He moves closer to her face.", is_narrator=True)
    show_story_box("Shigemura", "Prove your ‘usefulness’ with me, not alone.", affiliation="Kasakura High School Student")
    
    show_story_box("", "Naganohara flushed red, looking down.", is_narrator=True)
    show_story_box("Naganohara", "O-Okay… sorry.", affiliation="Kasakura High School Student")

    # --- SCENE 3: THE COMEDIC RELIEF & THE EXECUTIVE ---
    show_story_box("", "Benikawa whistled from the side, ducking a henchman’s swing.", is_narrator=True)
    show_story_box("Benikawa", "Oh~? Love dispute on the battlefield? Spicy~.", affiliation="Benikawa Ninja Clan")
    
    show_story_box("Riposte Henchman", "Gah! Where the hell’re ya looking, ninja?!", affiliation="Riposte Gang")
    
    show_story_box("Benikawa", "Oops. Sorry~~.", affiliation="Benikawa Ninja Clan")
    show_story_box("", "She kicked him in the head without looking.", is_narrator=True)
    
    show_story_box("", "We regrouped, staring down the new enemy.", is_narrator=True)
    show_story_box("", "It was the young man. The one with the sandy coat and the curtain-bangs hair.", is_narrator=True)
    show_story_box("", "He put his hand on his chin, tapping his rapier against his leg.", is_narrator=True)
    
    show_story_box("Young Man", "Fascinating. The girl and her diary were telling the truth. You really can change into stronger forms.", affiliation="Riposte Gang")
    
    show_story_box("Akasuke", "...You’re the one who took Kagaku.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Young Man", "I am. And I must say, seeing the theory in practice is quite impressive.", affiliation="Riposte Gang")
    show_story_box("", "He raised his rapier, assuming a stance that was perfect. Flawless.", is_narrator=True)
    show_story_box("Young Man", "But you’ll have to get past me to retrieve her.", affiliation="Riposte Gang")
    
    show_story_box("", "The pressure coming off him was intense. He wasn’t a Squad Leader. He was a core executive.", is_narrator=True)
    show_story_box("", "We tensed, ready for a desperate fight.", is_narrator=True)

    # --- SCENE 4: KAGAKU'S SURPRISE ATTACK ---
    show_story_box("", "Suddenly—\nWHOOSH.", is_narrator=True)
    show_story_box("", "A shadow dropped from the stairwell railing above.\nCRACK!", is_narrator=True)
    show_story_box("", "A metal rapier handle smashed directly onto the young man’s head.", is_narrator=True)
    
    show_story_box("Young Man", "Guh?!", affiliation="Riposte Gang")
    show_story_box("", "He stumbled backward, stunned, clutching his skull.", is_narrator=True)
    
    show_story_box("", "A figure landed gracefully (mostly) behind him.\nIt was Kagaku.", is_narrator=True)
    show_story_box("", "She was battered, bruised, and holding a stolen rapier. Her aura was flaring…", is_narrator=True)
    show_story_box("", "She was also using a Riposte Squad Leader Kata.", is_narrator=True)
    
    show_story_box("Kagaku", "You have terrible manners, you know that?!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "She pointed her blade at him, panting heavily.", is_narrator=True)
    show_story_box("Kagaku", "You kidnap me! You threaten me! You feed me delicious pancakes! And you never even introduced yourself!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Akasuke", "...Kagaku?", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "She ignored me, glaring at the man.", is_narrator=True)
    show_story_box("Kagaku", "I liked your cooking! But I’m putting an end to your criminal antics right now!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I blinked.", is_narrator=True)
    show_story_box("Akasuke", "She… sure has a history with her kidnapper.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "The young man rubbed his head, wincing. He turned to face her.", is_narrator=True)
    show_story_box("", "He blinked. Then, he sighed.", is_narrator=True)
    show_story_box("", "He straightened his coat. He sheathed his rapier.\nAnd he bowed. Deeply. To all of us.", is_narrator=True)
    
    show_story_box("Young Man", "My apologies. You are absolutely right. Where are my manners?", affiliation="Riposte Gang")
    show_story_box("", "He stood up, his expression shifting from pained to professionally cold.", is_narrator=True)
    
    show_story_box("Adam", "I am Adam. Executive of the Riposte Gang.", affiliation="Riposte Gang Executive")
    
    show_story_box("", "He drew his blade again. The air in the corridor grew heavy.", is_narrator=True)
    show_story_box("", "Ugh..!\nMy Kata had just run out of time, too, but Kagaku and Naganohara seems to still be holding on to hers...", is_narrator=True)

    show_story_box("Adam", "My Boss will be arriving soon. I hope to have a proud victory to report to him.", affiliation="Riposte Gang Executive")
    show_story_box("Adam", "En garde.", affiliation="Riposte Gang Executive")

def play_stage_3_21_story():
    # --- SCENE 1: KAGAKU'S POV (THE END OF ADAM) ---
    show_story_box("", "********* ◆ *********\nKagaku’s POV", is_narrator=True)
    show_story_box("", "Adam was crumbling.", is_narrator=True)
    show_story_box("", "The flawless, graceful Riposte Executive was gone. In his place was a desperate young man, gasping for air, his rapier trembling in his grip.", is_narrator=True)
    show_story_box("", "His parries were a fraction of a second too slow. His stance was widening, losing its tension.", is_narrator=True)
    
    show_story_box("Kagaku", "...He’s at his limit.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I watched him deflect a strike from Yuri, only to stumble back into Akasuke’s range.", is_narrator=True)
    show_story_box("", "Six of us. Six Kata users were ganging up on one man. And with Natsume whispering tactical data in our ears every second, and we had to give it our all to keep up with him.", is_narrator=True)
    show_story_box("", "It was still overkill, though. And honestly? He deserved it for kidnapping me!", is_narrator=True)
    
    show_story_box("", "But…\nI remembered the pancakes. The shrimp alfredo. The way he bowed when he brought me breakfast.", is_narrator=True)
    
    show_story_box("Kagaku", "You’re an idiot, you know that?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Adam froze, panting, sweat dripping from his bangs.", is_narrator=True)
    show_story_box("Adam", "Haah...Excuse me?", affiliation="Riposte Gang Executive")
    
    show_story_box("Kagaku", "You have talent. Real talent. Not this criminal stuff. I mean the cooking. And your discipline.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "I lowered the rapier in my hand slightly.", is_narrator=True)
    show_story_box("Kagaku", "You’re young. You’re just following orders because you have nowhere else to go, right? That’s a waste.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "He blinked. The aggression in his eyes wavered.", is_narrator=True)
    
    show_story_box("Kagaku", "Kasakura High could use a chef. Or a student. Why don’t you quit this ‘Riposte’ nonsense and come get a normal life?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Adam", "I…", affiliation="Riposte Gang Executive")
    show_story_box("", "He hesitated. For one fatal second, he lowered his guard.", is_narrator=True)
    
    show_story_box("Akasuke", "An opening.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "Akasuke lunged. A clean, decisive thrust with the hilt of his weapon into Adam’s chest.", is_narrator=True)
    
    show_story_box("", "THUD.\nAdam collapsed to his knees, coughing. His rapier clattered to the floor.", is_narrator=True)
    show_story_box("", "Silence fell over the corridor.\nThe battle was over.", is_narrator=True)
    
    show_story_box("", "I walked up to him. He didn’t look up. He just stared at the carpet, defeated.", is_narrator=True)
    
    show_story_box("Kagaku", "The Anchor. Please.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "I held out my hand.", is_narrator=True)
    show_story_box("", "Adam reached into his coat pocket. His hand was shaking. He pulled out the blue pendant and placed it in my palm.", is_narrator=True)
    
    show_story_box("Adam", "...You win.", affiliation="Riposte Gang Executive")
    show_story_box("", "It was a gesture of respect. A duelist acknowledging his loss, even though the fight was not a duel at all.", is_narrator=True)

    # --- SCENE 2: THE HENCHMAN'S WARNING ---
    show_story_box("", "Just then—\nTHUD THUD THUD—", is_narrator=True)
    show_story_box("", "Footsteps resounded from the stairwell.\nWe all spun around, weapons raised.", is_narrator=True)
    
    show_story_box("", "But it wasn’t an army. It was a single henchman. He looked disheveled, like he’d sprinted up fourteen flights of stairs. Well, that’s probably what we went through, though.", is_narrator=True)
    show_story_box("", "He saw us—saw his unconscious comrades, saw his Executive on his knees—but he didn’t care.", is_narrator=True)
    
    show_story_box("Henchman", "Adam-sir! Wait! Don’t engage!", affiliation="Riposte Gang")
    
    show_story_box("", "Yuri stepped forward, cracking her knuckles.", is_narrator=True)
    show_story_box("Yuri", "Too late, buddy. The party's over.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Henchman", "NO! You don’t understand! The Boss! The Boss is HERE!", affiliation="Riposte Gang")
    
    show_story_box("", "The air in the room froze.", is_narrator=True)
    show_story_box("", "Adam’s head snapped up. His eyes widened in genuine terror.", is_narrator=True)
    
    show_story_box("Adam", "...What?", affiliation="Riposte Gang Executive")
    show_story_box("Kagaku", "You said tomorrow! You said he was arriving tomorrow!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Adam", "I… I thought he was..! That was the schedule!", affiliation="Riposte Gang Executive")
    
    show_story_box("", "Adam looked at the floor, his face draining of color.", is_narrator=True)
    
    show_story_box("Adam", "He’s here… today? Now?", affiliation="Riposte Gang Executive")
    show_story_box("", "He started to tremble.", is_narrator=True)
    
    show_story_box("Adam", "No…he was on the island. The whole time. He’s been watching.", affiliation="Riposte Gang Executive")
    show_story_box("Adam", "He used us as bait. He watched us scramble… watched us fight… just to confirm the Katas were real. And now that you have the Anchor here…", affiliation="Riposte Gang Executive")
    
    show_story_box("", "He looked at me.", is_narrator=True)
    show_story_box("Adam", "...He’s coming to collect it.", affiliation="Riposte Gang Executive")

    # --- SCENE 3: AKASUKE'S POV (THE BOSS ARRIVES) ---
    show_story_box("", "…\n********* ◆ *********\nAkasuke’s POV", is_narrator=True)
    
    show_story_box("", "“The ‘Boss’.”\nThe word hung in the air like a curse.", is_narrator=True)
    show_story_box("", "We formed a circle, facing the stairwell door. The henchman had come from there. Logic dictated the Boss would follow.", is_narrator=True)
    
    show_story_box("Akasuke", "Ready yourselves! He’s coming up the stairs!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Yuri", "Got it! I’ll smash him the second he shows his face!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "We stared at the door. Unblinking. Muscles coiled.", is_narrator=True)
    show_story_box("", "DING.\nThe sound came from behind us.\nA soft, gentle chime.", is_narrator=True)
    
    show_story_box("", "Cold sweat erupted on my back.\nWe turned around slowly.", is_narrator=True)
    show_story_box("", "The elevator doors slid open.", is_narrator=True)
    show_story_box("", "There was no army. No bodyguards.\nJust one man.", is_narrator=True)
    
    show_story_box("", "He looked… western. Middle-aged.", is_narrator=True)
    show_story_box("", "He had short, military-style navy blue hair with a skin fade, streaked with lighter blue that seemed to blend into the shadows.", is_narrator=True)
    show_story_box("", "He wore a long, pristine white leather coat—buttoned at the top like a cloak—over a sharp navy suit. A white fedora with a black band was tipped low over his eyes.", is_narrator=True)
    
    show_story_box("", "He didn’t look at us. He didn’t look at Adam.", is_narrator=True)
    show_story_box("", "He looked… bored. Depressed. Like he was waiting for a bus in the rain.", is_narrator=True)
    show_story_box("", "Two rapiers were sheathed at his hips.", is_narrator=True)
    
    show_story_box("", "My instincts screamed.", is_narrator=True)
    show_story_box("", "It wasn’t the ‘Knight’. I knew that.\nThe ‘Knight’ was something else—something supernatural.", is_narrator=True)
    show_story_box("", "But the dread?\nThe feeling that death was standing in the elevator?\nThat was exactly the same.", is_narrator=True)
    
    show_story_box("", "The Boss stepped out.", is_narrator=True)
    show_story_box("", "CLICK.\nThe sound of swords loosening in their sheaths.", is_narrator=True)
    
    show_story_box("", "I opened my mouth to shout “Attack!”\nI never got the chance.", is_narrator=True)
    
    show_story_box("", "The world blurred.\nSilver lines crisscrossed the air. Beautiful. Geometric. Impossible.", is_narrator=True)
    show_story_box("", "SPLAT.", is_narrator=True)
    
    show_story_box("", "I didn’t feel the pain. Not at first.\nI just saw the blood.", is_narrator=True)
    show_story_box("", "It exploded from my chest. My arms. My legs.", is_narrator=True)
    show_story_box("", "I looked to my left. Yuri was falling, a red spray erupting from her neck. Benikawa. Shigemura. Naganohara. Kagaku.", is_narrator=True)
    show_story_box("", "All six of us. Cut down in a single heartbeat.", is_narrator=True)
    
    show_story_box("", "We hit the floor in a wet heap.\nNot this again.", is_narrator=True)
    
    show_story_box("", "Adam was still kneeling, staring in horror. The Boss was long past us, his white coat unstained.", is_narrator=True)
    show_story_box("", "He stopped in front of Adam. He extended a hand.", is_narrator=True)
    
    show_story_box("Boss of Riposte", "The Anchor.", affiliation="Riposte Gang")
    
    show_story_box("", "His voice was flat. Empty.", is_narrator=True)
    show_story_box("", "My vision faded. The red carpet turned black.\nDarkness.", is_narrator=True)

    # --- SCENE 4: THE VOID AND THE MYSTERIOUS WOMAN ---
    show_story_box("", "…\n……", is_narrator=True)
    show_story_box("Akasuke", "...", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I was floating.\nNo pain. No sound. Just the endless dark.", is_narrator=True)
    
    mystery_style1 = "dark_sea_green4"
    
    show_story_box("???", "My, my. I told you the path wouldn’t be easy~.", affiliation="???", color_override=mystery_style1)
    
    show_story_box("", "I opened my ‘eyes’, although I’m seeing nothing.", is_narrator=True)
    show_story_box("", "It was her. The tired woman’s voice. The one who spoke to me when the Knight ‘killed’ me.", is_narrator=True)
    
    show_story_box("Akasuke", "...You again.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("???", "Me again. You really have a habit of getting sliced into ribbons, don’t you?", affiliation="???", color_override=mystery_style1)
    
    show_story_box("", "I didn’t panic. I didn’t scream.\nIt’s not over yet.", is_narrator=True)
    
    show_story_box("Akasuke", "My friends. How are they?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("???", "Oh, you know. Chopped up. Bleeding out on a hotel carpet. Dead in about… three seconds.", affiliation="???", color_override=mystery_style1)
    show_story_box("", "She sounded bored.", is_narrator=True)
    
    show_story_box("Akasuke", "...Can I fix it?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "The Void was silent for a moment.", is_narrator=True)
    show_story_box("???", "...Hah. You really are interesting. Most people would be crying, breaking down by now.", affiliation="???", color_override=mystery_style1)
    
    show_story_box("", "She sighed.", is_narrator=True)
    show_story_box("???", "Here’s a secret, Akasuke. The power you’re using? The ‘Kata’? You aren’t just ‘borrowing’ a form. I wouldn’t say that.", affiliation="???", color_override=mystery_style1)
    show_story_box("???", "You are rather ‘swapping’. You are pulling a version of yourself from another universe to take your place, while you inhabit their potential.", affiliation="???", color_override=mystery_style1)
    
    show_story_box("Akasuke", "Swapping..?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("???", "Usually, it’s temporary. You wager your own body to use the ‘Kata’ because you’ll eventually swap back. No harm done. But to save a life that’s already ended… to stitch meat back together that’s been severed…", affiliation="???", color_override=mystery_style1)
    show_story_box("", "Her voice dropped low.", is_narrator=True)
    
    show_story_box("???", "You have to be selfish~.", affiliation="???", color_override=mystery_style1)
    
    show_story_box("Akasuke", "Selfish?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("???", "You use your remaining life force to pull a Kata—a healthy, living version of you and your friends—from another world. And then… you cut the line.", affiliation="???", color_override=mystery_style1)
    show_story_box("???", "You steal their status. You overwrite your death with their life. And in doing so… you extinguish that timeline. You kill that version of yourself to save this one.", affiliation="???", color_override=mystery_style1)
    
    show_story_box("", "I froze.", is_narrator=True)
    show_story_box("Akasuke", "Kill another me? Destroy a whole world? Just to survive? I can do something like…that?", affiliation="Kasakura High School Student / Seven Wonders", is_thought=True)
    
    show_story_box("???", "Well? Do you have the resolve? Or do you die here, righteous and empty?", affiliation="???", color_override=mystery_style1)
    
    show_story_box("", "I thought of Yuri. Shigemura. Naganohara. Kagaku. Benikawa.", is_narrator=True)
    show_story_box("", "I thought of the ‘Boss’ standing over them.", is_narrator=True)
    
    show_story_box("Akasuke", "...Would any Akasuke… in any universe… do the same?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "The woman chuckled. A dry, amused sound.", is_narrator=True)
    show_story_box("???", "You already know the answer to that.", affiliation="???", color_override=mystery_style1)
    
    show_story_box("", "Yeah. I did.", is_narrator=True)
    show_story_box("Akasuke", "If it means saving Yuri… I’d burn a thousand worlds.", affiliation="Kasakura High School Student / Seven Wonders", is_thought=True)
    
    show_story_box("Akasuke", "...Sorry, other me.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("???", "That’s the spirit.", affiliation="???", color_override=mystery_style1)

    # --- SCENE 5: RESURRECTION ---
    show_story_box("", "Hotel Corridor\nGASPPP!", is_narrator=True)
    show_story_box("", "Air rushed into my lungs.", is_narrator=True)
    show_story_box("", "I bolted upright, clutching my chest.", is_narrator=True)
    show_story_box("", "Wet. Warm. Sticky.", is_narrator=True)
    
    show_story_box("", "I was covered in blood. My own blood. A pool of it soaking into my clothes.", is_narrator=True)
    show_story_box("", "But the wounds… were gone.", is_narrator=True)
    
    show_story_box("", "I looked around.", is_narrator=True)
    show_story_box("", "Yuri was gasping, feeling her neck. Shigemura was staring at his hands. Kagaku was checking her torso.", is_narrator=True)
    show_story_box("", "Alive. All of us.", is_narrator=True)
    
    show_story_box("", "I touched my chest.\nStill no heartbeat.", is_narrator=True)
    show_story_box("", "I looked up.", is_narrator=True)
    
    show_story_box("", "The Boss of Riposte was standing there, the blue Anchor in his hand.", is_narrator=True)
    show_story_box("", "He paused.", is_narrator=True)
    show_story_box("", "He turned slowly, looking down at us. For the first time, the indifference in his eyes cracked.", is_narrator=True)
    show_story_box("", "He looked intrigued.", is_narrator=True)
    
    show_story_box("Boss of Riposte", "...Hoh?", affiliation="Riposte Gang")

def play_stage_3_22_story():
    # --- SCENE 1: AKASUKE'S POV (THE AFTERMATH OF THE 'WIPE') ---
    show_story_box("", "********* ◆ *********\nAkasuke’s POV", is_narrator=True)
    show_story_box("", "Hotel Corridor\nThe air in the hallway was suffocating.", is_narrator=True)
    show_story_box("", "My chest heaved, sucking in air that I shouldn’t need, pumping blood that shouldn’t be flowing.", is_narrator=True)
    
    show_story_box("", "The Boss of Riposte stood over us. He hadn’t moved. He hadn’t broken a sweat.", is_narrator=True)
    show_story_box("", "He had just killed six Kata users in the span of a single breath.", is_narrator=True)
    
    show_story_box("", "Adam was staring at us, his jaw slack, eyes wide with a mixture of horror and confusion. I couldn’t blame him. Watching six corpses suddenly sit up and gasp for air isn’t something you see every day.", is_narrator=True)
    
    show_story_box("", "The Boss turned his head slightly, addressing his Executive.", is_narrator=True)
    show_story_box("Boss of Riposte", "Observe, Adam. This is the extent of the power everyone is chasing. It seems to even bend the rules of life itself.", affiliation="Riposte Gang")
    
    show_story_box("", "He rested a hand on the hilt of his rapier.\nHe looked down at me. His eyes were empty, depressed voids.", is_narrator=True)
    
    show_story_box("Boss of Riposte", "Tell me, boy. How did you come back? You were dead. I cut your heart in two.", affiliation="Riposte Gang")
    
    show_story_box("", "I wanted to open my mouth to answer—but a sound interrupted me.", is_narrator=True)
    show_story_box("", "Ding.\nThe elevator chimed again.", is_narrator=True)
    show_story_box("", "Not the one the Boss came from. The one right next to it.", is_narrator=True)
    show_story_box("", "The doors slid open.", is_narrator=True)

    # --- SCENE 2: HAZUKI'S ENTRANCE ---
    show_story_box("", "BOOM!\nA figure exploded out of the elevator car.", is_narrator=True)
    show_story_box("", "It wasn’t a run. It was a launch.\nA weapon smashed down toward the Boss’s head.", is_narrator=True)
    
    show_story_box("", "He drew his rapier—a blur of silver—to block.", is_narrator=True)
    show_story_box("", "CLANG-ZZZRRT!", is_narrator=True)
    
    show_story_box("", "A massive shockwave rippled through the corridor. The floor tiles cracked. Adam and the rest of us were sent sliding backward by the sheer force. The henchman who had been guarding the stairs was blown off his feet and tumbled down the stairwell.", is_narrator=True)
    show_story_box("", "Dust and debris filled the air.", is_narrator=True)
    
    show_story_box("", "Standing in the center of the crater was a girl.", is_narrator=True)
    show_story_box("", "She was tall. Black hair whipping around her face. She wore a long black coat over a simple tracksuit.", is_narrator=True)
    
    show_story_box("", "She looked up.\nHer eyes.", is_narrator=True)
    show_story_box("", "They weren’t normal. They were emerald green—but they looked like engraved, polished jewels. Intricate. Artificial. Beautiful.", is_narrator=True)
    
    show_story_box("", "She was pressing a weapon down against the Boss’s blade.", is_narrator=True)
    show_story_box("", "It looked like a metal pipe. But it was pitch black, pulsing with neon green circuitry lines that flowed like digital blood.", is_narrator=True)
    
    show_story_box("Boss of Riposte", "...", affiliation="Riposte Gang")
    
    show_story_box("", "Green sparks flew as the weapons ground against each other.\nThe girl grinned.", is_narrator=True)
    
    mystery_style2 = "sea_green2"
    show_story_box("???", "You finally showed up yourself, Kesler~!", affiliation="???", color_override=mystery_style2)
    
    show_story_box("", "The Boss—Kesler—didn’t panic. His voice remained monotone.", is_narrator=True)
    show_story_box("Kesler", "How long will you continue to pester me, Miyabi Hazuki?", affiliation="Riposte Gang Boss")
    
    show_story_box("Akasuke", "Miyabi? Like the Academy? No… that’s…her family name?", affiliation="Kasakura High School Student / Seven Wonders", is_thought=True)
    
    show_story_box("", "Hazuki pushed off, flipping backward to create distance.", is_narrator=True)
    show_story_box("Hazuki", "Until I beat you down, obviously!", affiliation="Miyabi Hazuki")
    show_story_box("", "She landed lightly.", is_narrator=True)

    # --- SCENE 3: THE BLACK BOX BATTLE ---
    show_story_box("", "Then, the weapon changed.", is_narrator=True)
    show_story_box("", "It happened in a blink. The metal pipe shifted. It expanded, plates sliding over plates, mass appearing out of nowhere.", is_narrator=True)
    show_story_box("", "In her hands, she now held a massive, black broadsword.", is_narrator=True)
    
    show_story_box("Akasuke", "What the…?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "She swung.", is_narrator=True)
    show_story_box("", "It was too fast to track. Kesler parried, but the weight of the broadsword forced him to slide back.", is_narrator=True)
    
    show_story_box("", "Hazuki didn’t let up. She spun, releasing the sword with one hand.", is_narrator=True)
    show_story_box("", "Click-whirrr.\nThe sword collapsed, elongated, and curved.\nA bow.", is_narrator=True)
    
    show_story_box("", "She pulled a digital string. A neon green arrow materialized.\nPEWW—\nA laser shot.", is_narrator=True)
    
    show_story_box("", "Kesler tilted his head. The beam singed his fedora.\nHe dashed forward.", is_narrator=True)
    
    show_story_box("", "Hazuki smirked. The bow shifted again—barrels extending, stock locking into place.\nA long-barreled rifle.\nBANG.\nAnother laser.", is_narrator=True)
    
    show_story_box("", "Kesler twisted his body, but not fast enough. The beam grazed his shoulder.", is_narrator=True)
    show_story_box("", "Blood—real, red blood—splattered onto his white coat.", is_narrator=True)
    
    show_story_box("", "Kagaku, who was crouching next to me, grabbed my arm. Her eyes were sparkling.", is_narrator=True)
    show_story_box("Kagaku", "Ahh!! That weapon! That’s the ‘Black Box’! My lost project!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Akasuke", "Your own project?!", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Kagaku", "The transforming alloy! I thought it was destroyed years ago!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Hazuki didn’t hear her. She was too focused on the kill.", is_narrator=True)
    
    show_story_box("", "Kesler touched his shoulder. He looked at the blood on his fingers.", is_narrator=True)
    show_story_box("", "His expression darkened. Just a fraction.", is_narrator=True)
    show_story_box("Kesler", "Irritating.", affiliation="Riposte Gang Boss")
    
    show_story_box("", "He vanished.", is_narrator=True)
    show_story_box("", "No—he moved. Faster than before.\nHe appeared directly in front of Hazuki.", is_narrator=True)
    show_story_box("", "He didn’t use his sword. He threw a simple front kick.", is_narrator=True)
    
    show_story_box("", "FSHHHHH—\nDark, blue-ish steam erupted from the impact point.", is_narrator=True)
    show_story_box("", "The entire floor shook.", is_narrator=True)
    
    show_story_box("Hazuki", "Oh, crap.", affiliation="Miyabi Hazuki")
    
    show_story_box("", "The weapon shifted again—expanding into a towering, hexagonal shield.\nBOOOOM!", is_narrator=True)
    
    show_story_box("", "The impact hit the shield. Hazuki dug her heels in, sliding back ten meters, carving deep grooves into the floor.", is_narrator=True)
    show_story_box("", "The corridor was filled with the dark blue steam. It was thick, heavy, obscuring everything.", is_narrator=True)
    
    show_story_box("Hazuki", "Tch!", affiliation="Miyabi Hazuki")
    show_story_box("", "She waved her hand, and the shield vented a blast of air, clearing the mist.", is_narrator=True)

    # --- SCENE 4: THE AFTERMATH ---
    show_story_box("", "The corridor was empty.", is_narrator=True)
    show_story_box("", "Kesler was gone.\nAdam was gone.\nAnd the Anchor was gone.", is_narrator=True)
    
    show_story_box("", "Hazuki stood there for a moment, scanning the area.", is_narrator=True)
    show_story_box("", "Then, she sighed. A long, exaggerated sigh of relief.", is_narrator=True)
    
    show_story_box("Hazuki", "Whew. That guy hits like a truck.", affiliation="Miyabi Hazuki")
    
    show_story_box("", "Click-click-click.\nThe massive shield folded in on itself. Smaller. Smaller. Until it was just a black cube with glowing green lines, no bigger than a Rubik’s cube.", is_narrator=True)
    show_story_box("", "She picked it up and tossed it into a small satchel at her hip.", is_narrator=True)
    
    show_story_box("", "She turned to us, flashing a bright, toothy grin.", is_narrator=True)
    show_story_box("Hazuki", "Yo! Sorry I’m late! I accidentally fell asleep this mornin’, but I made it just in time~!", affiliation="Miyabi Hazuki")
    
    show_story_box("", "She looked at Kagaku and winked.", is_narrator=True)
    show_story_box("Hazuki", "‘Help’. Is. Finally here~! How’d ya like it?", affiliation="Miyabi Hazuki")
    
    show_story_box("", "We stared at her.", is_narrator=True)
    show_story_box("", "Kagaku looked at the empty spot where the Anchor used to be. Then back at Hazuki.", is_narrator=True)
    
    show_story_box("Kagaku", "...You let him get away with the pendant.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Yuri", "And you nearly blew us up.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Hazuki blinked.", is_narrator=True)
    show_story_box("Hazuki", "But I saved you, right? Details, details!", affiliation="Miyabi Hazuki")
    show_story_box("", "She laughed.", is_narrator=True)
    
    show_story_box("", "We exchanged looks.\nConfused. Exhausted. And definitely annoyed.", is_narrator=True)

def play_stage_3_23_story():
    # --- SCENE 1: AKASUKE'S POV (MEETING HAZUKI) ---
    show_story_box("", "********* ◆ *********\nAkasuke’s POV", is_narrator=True)
    show_story_box("", "Hotel Corridor – 14th Floor", is_narrator=True)
    show_story_box("", "The smoke cleared, but the silence that followed was deafening.", is_narrator=True)
    show_story_box("", "Me, Yuri, Benikawa, Shigemura, Naganohara, and Kagaku—all six of us stood there, staring dumbfounded at the mature, black-haired girl who had just chased off the Boss of Riposte.", is_narrator=True)
    
    show_story_box("", "Hazuki brushed some dust off her tracksuit, completely unfazed by the destruction around her.", is_narrator=True)
    show_story_box("Hazuki", "Man, that Kesler guy was always such a pain in the neck to track down. Now I gotta do it all over again~.", affiliation="Miyabi Hazuki")
    
    show_story_box("", "She turned to us, flashing a bright smile.", is_narrator=True)
    show_story_box("Hazuki", "Anyway! I should properly introduce myself. Miyabi Hazuki. Kiryoku Gakuen graduate!", affiliation="Miyabi Hazuki")
    
    show_story_box("Yuri", "Kiryoku? You’re an alumna?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Hazuki", "Yup! Back in the day, I ran around as a vigilante. ‘Called myself ‘JK Mask’. I wore a cool and mysterious Otafuku mask then and ran around beating up small-time kidnappers and delinquents.", affiliation="Miyabi Hazuki")
    show_story_box("", "She stretched her arms over her head, popping her shoulders.", is_narrator=True)
    show_story_box("Hazuki", "Theeen…A lot happened since then, but I’m a little stronger now. I mostly focus on hunting down super-big-shot criminals hiding behind the scenes. Like Kesler.", affiliation="Miyabi Hazuki")
    
    show_story_box("Akasuke", "This girl…", affiliation="Kasakura High School Student / Seven Wonders", is_thought=True)
    show_story_box("", "I crossed my arms, feeling a vein throb in my forehead.", is_narrator=True)
    show_story_box("Akasuke", "So… let me get this straight. You used us. You used our rescue operation, our fight, and our near-deaths just to lure the ‘Boss’ out. And then you let him get away?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Hazuki winced, rubbing the back of her head sheepishly.", is_narrator=True)
    show_story_box("Hazuki", "Ahaha… sorry about that! Timing was a bit off. Tell you what, I guess I owe you one.", affiliation="Miyabi Hazuki")
    
    show_story_box("", "She dug into her pocket and pulled out a crumpled, stained, incredibly crappy-looking business card.", is_narrator=True)
    show_story_box("", "She flicked it to me. I barely caught the card and all the sand that came along with it.", is_narrator=True)
    show_story_box("Hazuki", "Call me if you ever need a favor! Now, if you’ll excuse me, I’m busy. Gotta go track my next targets~.", affiliation="Miyabi Hazuki")
    
    show_story_box("", "She turned toward a shattered window.", is_narrator=True)
    show_story_box("", "Kagaku stepped forward, eyes locked on the small black cube sitting in Hazuki’s satchel.", is_narrator=True)
    
    show_story_box("Kagaku", "Wait! The ‘Black Box’ weapon you’re using! That’s one of my creations! Where did you get it?!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Hazuki paused, looking back over her shoulder.", is_narrator=True)
    show_story_box("Hazuki", "Oh, this? I found it in a garbage dumpster a long time ago, back when I was in high school.", affiliation="Miyabi Hazuki")
    
    show_story_box("Kagaku", "A dumpster?!–Ah! Yeah, I think I’m starting to remember now…", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Hazuki", "Yeah! It almost felt like the box called out to me. Like it found a compatible user. We’ve been stuck together ever since.", affiliation="Miyabi Hazuki")
    show_story_box("Kagaku", "I… I need to take a close look at it someday. Please!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Hazuki grinned and gave a two-finger salute.", is_narrator=True)
    show_story_box("Hazuki", "Sure thing, kid. See ya around!", affiliation="Miyabi Hazuki")
    
    show_story_box("", "With a powerful leap, she vaulted out the window, disappearing into the night air.", is_narrator=True)

    # --- SCENE 2: LATER THAT NIGHT & THE NEXT DAY ---
    show_story_box("", "Later That Night - The Resort", is_narrator=True)
    show_story_box("", "Hours later, our group sneaked back into the field trip area. We blended into the crowd, participating in the rest of the evening activities as if nothing had happened.", is_narrator=True)
    show_story_box("", "When night finally fell, I collapsed into my bed like a felled tree.", is_narrator=True)
    show_story_box("", "Room assignments were up to us, so I was sharing a cabin with Shigemura and Nishida. Nishida was still tinkering with his weapon parts, and Shigemura was reading.", is_narrator=True)
    show_story_box("", "The others didn’t ask questions. They knew exactly what we’d been up to all day—the same old fighting, just this time, to protect the peace between four major schools.", is_narrator=True)
    show_story_box("", "I closed my eyes and slept like a log.", is_narrator=True)
    
    show_story_box("", "The Next Day - Shopping District", is_narrator=True)
    show_story_box("", "Kojima-sensei and the staff decided to change the itinerary. Since they were still secretly cleaning up the hotel and apprehending Riposte’s remnants, safety was the priority. We were given the entire day to roam the luxurious shopping district—an activity originally saved for the end of the trip.", is_narrator=True)
    show_story_box("", "Nobody complained. The extroverts dragged their friends through every boutique, while the introverts found quiet cafes to hole up in.", is_narrator=True)
    
    show_story_box("", "I was just about to find a food stall when my phone buzzed. Then it buzzed again. And again.\nSpammed.", is_narrator=True)
    show_story_box("", "Over ten messages in a row. All from Natsume.", is_narrator=True)
    show_story_box("", "| Meet me. |\n| Now. |\n| Secluded cafe. South alley. |\n| Hurry up. |\n| Don’t make me come find you. |", is_narrator=True)
    
    show_story_box("", "I sighed, abandoning my lunch plans, and navigated through the crowds.", is_narrator=True)

    # --- SCENE 3: THE SECRET MEETING ---
    show_story_box("", "At the darkest, most unpopular corner of an obscure cafe, I found them. Natsume and Kagaku were sitting at a small table, completely surrounded by empty coffee cups. Caffeine addicts, through and through.", is_narrator=True)
    show_story_box("", "I slid into the booth across from them.", is_narrator=True)
    
    show_story_box("Akasuke", "This better be good. I skipped lunch for this.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Natsume took a slow sip of her espresso. Her eyes were dark.", is_narrator=True)
    show_story_box("Natsume", "It’s not good, Akasuke. It’s ominous.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "She pulled out her tablet, sliding it across the table.", is_narrator=True)
    show_story_box("Natsume", "We finished interrogating the Riposte gangsters. I compared their statements with the thugs who infiltrated the cruise ship to steal the weapons.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Kagaku", "They aren’t connected.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I blinked.", is_narrator=True)
    show_story_box("Akasuke", "What do you mean? They didn’t work together?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Natsume", "I mean, they don’t even know the other group exists. Riposte Gang was after Kagaku and the Katas. The ship infiltrators were just after the weapons. It’s two completely separate enemy factions moving at the same time.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "A chill ran down my spine.", is_narrator=True)
    show_story_box("Akasuke", "Who were the ship infiltrators really?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Natsume shook her head, frustrated.", is_narrator=True)
    show_story_box("Natsume", "We don’t know. The thugs we caught are clueless pawns. Just like the Heiwa delinquents during the school raid—they didn’t even know about the Katas.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Natsume", "We traced their orders back to only washed-up kidnapping gang leaders and low-tier Upperclassmen. Guys so harmless they aren’t even registered in my main database.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Kagaku", "Whoever is pulling their strings is incredibly good at hiding.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Akasuke", "And the three ninjas on the ship? Falcon, Raven, and Eagle?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("Natsume", "They were only hired mercenaries, even more unrelated to the mastermind. Like with Benikawa, Kasakura respected the Ninja Code—we didn’t pry into their superior’s identity so they wouldn’t be branded as ‘Ibara’.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I leaned back in the booth, rubbing my temples.", is_narrator=True)
    show_story_box("", "Multiple masterminds. Multiple threats. And Kasakura was sitting right in the middle of it all.", is_narrator=True)

    # --- SCENE 4: THAT NIGHT (THE RESOLVE) ---
    show_story_box("", "That Night - Resort Cabin", is_narrator=True)
    show_story_box("", "I couldn’t sleep.", is_narrator=True)
    show_story_box("", "I lay on my back, staring at the ceiling fan spinning lazily above. My mind was a chaotic loop of the last 48 hours.", is_narrator=True)
    show_story_box("", "The organized syndicate of the Riposte Gang.", is_narrator=True)
    show_story_box("", "The true, horrifying nature of the Katas—reviving oneself by literally sacrificing another version of me from an alternate world.", is_narrator=True)
    show_story_box("", "But mostly, it was the \"Bigger Fish.\"", is_narrator=True)
    show_story_box("", "The ‘Starguards’, whose mere aura on the ship made me forget how to breathe.", is_narrator=True)
    show_story_box("", "Kesler, who moved so fast I couldn’t even perceive the blade that cut me to ribbons.", is_narrator=True)
    show_story_box("", "Hazuki Miyabi, who thank god, was an ally, but her unobservable prowess showed me just how incredibly wide the gap I had to cross was.", is_narrator=True)
    show_story_box("", "She said she hunted criminals on Kesler’s level. That meant there were more monsters like him out there, huh? Monsters I couldn’t hope to match, even with the Katas.", is_narrator=True)
    
    show_story_box("Shigemura", "Can’t sleep?", affiliation="Kasakura High School Student")
    
    show_story_box("", "I glanced over. Shigemura was sitting up in the dark, adjusting his blanket.", is_narrator=True)
    show_story_box("Akasuke", "Yeah. Just thinking.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "We went outside to the balcony, watching the scenery of the island’s jungle illuminated by moonlight.", is_narrator=True)
    show_story_box("Akasuke", "Shigemura…what do you do when you meet an enemy you literally cannot beat? When the gap is just too big?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Shigemura thought for a moment. He knew I was thinking about yesterday.", is_narrator=True)
    show_story_box("Shigemura", "Rationally speaking? You have two options when encountering a ridiculously strong individual. One: Make sure that ‘enemy’ is your ally in the first place. Two: Find an ally who has similar strength to handle them for you.", affiliation="Kasakura High School Student")
    
    show_story_box("Akasuke", "And if there isn’t one? I was thinking…what if Hazuki-san hadn’t shown up at the hotel?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Shigemura didn’t hesitate.", is_narrator=True)
    show_story_box("Shigemura", "Then there is nothing to do. You simply fight to the best of your ability, and you go out with a bang.", affiliation="Kasakura High School Student")
    
    show_story_box("", "I stared at him for a second, then chuckled. It was so simple. So honest.", is_narrator=True)
    show_story_box("Akasuke", "Go out with a bang, huh?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "Shigemura smiled faintly.", is_narrator=True)
    show_story_box("Shigemura", "But for now, Akasuke… we were given a second chance. So we just have to get stronger, and stronger, until the next time. Because we won’t have any excuses by then.", affiliation="Kasakura High School Student")
    
    show_story_box("", "I nodded, feeling a heavy weight lift off my chest.", is_narrator=True)
    show_story_box("Akasuke", "You’re right.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "I reached my hand out in the moonlight. He met it.", is_narrator=True)
    show_story_box("", "We dapped up—a simple promise between guys who swore to look out for each other.", is_narrator=True)

    # --- SCENE 5: THE DEPARTURE & THE REVELATION ---
    show_story_box("", "The Next Morning - Shoreline Boarding Area", is_narrator=True)
    show_story_box("", "The trip was over.\nThe shoreline was packed with 1,200 students boarding the massive cruise ship.", is_narrator=True)
    
    show_story_box("", "I spotted Rara in the crowd.", is_narrator=True)
    show_story_box("Akasuke", "Hey! Rara..! Safe travels!", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "She looked at me like I was insane.", is_narrator=True)
    show_story_box("Rara", "Are you an idiot? We’re gettin’ on the same ship.", affiliation="Heiwa Seiritsu High School Student")
    
    show_story_box("Akasuke", "I know! I just…the ship is huge! We might not cross paths on the way back.", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("", "She rolled her eyes but smirked.", is_narrator=True)
    
    show_story_box("", "I volunteered to stay behind with Kojima-sensei and the staff to help monitor the boarding process and ensure no one got left behind.", is_narrator=True)
    show_story_box("", "As the crowd thinned out, I walked along the lower deck. That’s when I saw them.", is_narrator=True)
    show_story_box("", "My other two groupmates: Midori from Kiryoku Gakuen, and Fuyuki from Miyabi Academy.", is_narrator=True)
    
    show_story_box("", "They were standing in a secluded corner of the deck, talking. I raised a hand to go say proper goodbyes, but as I got closer, their voices drifted over the ocean breeze.", is_narrator=True)
    show_story_box("", "It wasn’t casual banter.", is_narrator=True)
    
    show_story_box("Midori", "Are you just clueless o-or an idiot..? Y-You better tread carefully from now on, Fuyuki-san…the four schools…they were my target. My prey in the first place.", affiliation="Kiryoku Gakuen Student?")
    show_story_box("", "She was still using her shy, timid, stuttering fangirl voice. But the words were venomous.", is_narrator=True)
    
    show_story_box("", "Fuyuki laughed—a light, polite, rich-boy sound.", is_narrator=True)
    show_story_box("Fuyuki", "My, my. Were you not expecting a factor like the ‘power of Katas’ to be so troublesome for your report? How frustrating for you.", affiliation="Miyabi Academy Student?")
    
    show_story_box("Midori", "Damnit all…I-I pondered for a very long time how I was going to write my ‘Rescue Observation Report’... If I had known, I would have left the job of observing Riposte Gang and Hanefuji Akasuke’s rescue operation on the island to someone else…", affiliation="Kiryoku Gakuen Student?")
    
    show_story_box("", "I stopped dead in my tracks.", is_narrator=True)
    show_story_box("", "My blood ran cold.", is_narrator=True)
    show_story_box("", "A Rescue Observation Report.\nMidori… was observing us?", is_narrator=True)
    
    show_story_box("Midori", "M-more importantly… I never thought you would be interested in observing as well…f-finding some Miyabi lapdog competing with me…uwaa…it’s the last thing I’ll ever need for my report…", affiliation="Kiryoku Gakuen Student?")
    
    show_story_box("Fuyuki", "As you know, they were revived without a single injury back at the hotel. I am quite glad I chose to come along on this field trip to observe it firsthand.", affiliation="Miyabi Academy Student?")
    
    show_story_box("", "The aura around them had completely changed. It was suffocating. Threatening.", is_narrator=True)
    show_story_box("", "My suspicions from the scavenger hunt hit me all at once. Fuyuki’s \"thirty-minute restroom break.\"...but I didn’t think Midori was on it as well.", is_narrator=True)
    show_story_box("", "They weren’t just students. They were traitors.", is_narrator=True)
    show_story_box("", "Bastards rigged to be in my group from the very beginning.", is_narrator=True)
    show_story_box("", "I clenched my fist.", is_narrator=True)
    
    show_story_box("Fuyuki", "Still… how foolish your ‘Boss’ was~, sending mere thugs as school infiltrators to steal the ship’s weapons—", affiliation="Miyabi Academy Student?")
    
    show_story_box("", "Before the sentence even finished, Midori moved.", is_narrator=True)
    show_story_box("", "Her shy demeanor temporarily vanished as she threw a lethal spear-hand strike directly at Fuyuki’s throat.", is_narrator=True)
    show_story_box("", "SMACK.", is_narrator=True)
    show_story_box("", "Fuyuki caught her wrist nonchalantly. The impact was so loud, and the speed of the clash so intense, that a hiss of steam fizzled from the friction between their skin.", is_narrator=True)
    
    show_story_box("Midori", "Khh…M-My Boss may not be cute like Aina-sama… but I won’t let anyone insult my benefactor. My ‘Boss’ is just as important to me… as your ‘Pacesetter’ is to you.", affiliation="Kiryoku Gakuen Student?")
    
    show_story_box("", "Fuyuki smiled, his eyes still half-closed. He leaned in extremely close to Midori and whispered something.", is_narrator=True)
    show_story_box("", "I strained to hear it, leaning forward—", is_narrator=True)
    show_story_box("", "—!!", is_narrator=True)
    
    show_story_box("", "A hand clamped onto the back of my collar and yanked me violently backward into the shadows of the hallway.", is_narrator=True)
    show_story_box("", "It was Kojima-sensei.", is_narrator=True)
    
    show_story_box("Kojima-sensei", "That was close.", affiliation="Kasakura High School Teacher")
    show_story_box("", "He dragged me quickly into the main crowd, blending us in perfectly.", is_narrator=True)
    
    show_story_box("Akasuke", "Sensei! They were—", affiliation="Kasakura High School Student / Seven Wonders")
    show_story_box("Kojima-sensei", "I know. You did well eavesdropping on the enemy, Akasuke. But you were doing it all wrong.", affiliation="Kasakura High School Teacher")
    
    show_story_box("", "He pushed his glasses up, looking back toward the secluded deck.", is_narrator=True)
    show_story_box("Kojima-sensei", "You almost got yourself killed.", affiliation="Kasakura High School Teacher")

    # --- SCENE 6: THE TRAITORS' AWARENESS ---
    show_story_box("", "…\nOn the secluded deck, Fuyuki kept his grip on Midori’s wrist. He leaned back after whispering to her.", is_narrator=True)
    show_story_box("", "What he had whispered was simple: “Someone is eavesdropping.”", is_narrator=True)
    
    show_story_box("", "He released her wrist smoothly, adjusting his thick winter jacket.", is_narrator=True)
    show_story_box("Fuyuki", "I sensed a faint trace of bloodlust in the air. So, I taunted your own highly concentrated bloodlust to create a contrast. It allowed me to differentiate and pinpoint the direction of our listener’s weaker, but existent, hostility.", affiliation="Miyabi Academy Student?")
    
    show_story_box("", "Midori rubbed her wrist, her timid facade still replaced by cold, calculating eyes.", is_narrator=True)
    show_story_box("Midori", "I noticed it as well. But the bastard’s already gone. Tch.", affiliation="Kiryoku Gakuen Student?")
    show_story_box("", "She glanced toward the hallway entrance.", is_narrator=True)
    
    show_story_box("Midori", "Another figure—smarter, and much calmer—pulled the idiot listener away just in time.", affiliation="Kiryoku Gakuen Student?")
    show_story_box("Midori", "...How fortunate for them.", affiliation="Kiryoku Gakuen Student?")