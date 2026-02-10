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
            elif speaker == "Hanefuji Kurona":
                box_color = "green"
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
            
            # --- ENEMIES (RED) ---
            elif speaker in ["Underwear Thief", "Freshman 1", "Freshman 2", "Freshman 3"]:
                box_color = "red"
            
            # --- DEFAULTS / MINOR CHARACTERS ---
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
    show_story_box("???", "There! Behind the gym, Yuri-chan!", affiliation="", color_override="green")
    
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
    
    mystery_style = "plum2" # Color for the mystery voice
    
    show_story_box("???", "Hmm...You weren’t supposed to die from that.", color_override=mystery_style)
    
    show_story_box("", "I couldn’t speak. Couldn’t move. But I could think.", is_narrator=True)
    
    show_story_box("???", "Nobody was. That blade… it wasn’t meant to kill all of you.", color_override=mystery_style)
    
    show_story_box("", "Pause.", is_narrator=True)
    
    show_story_box("???", "Anyways~, I’ll take responsibility. I’ll fix it, 'kay.", color_override=mystery_style)
    
    show_story_box("", "She sounded exhausted.", is_narrator=True)
    
    show_story_box("???", "I’m so tired of this duty…though. I just want to stop.", color_override=mystery_style)
    
    show_story_box("", "I wanted to scream. To demand answers.\nTo ask about Yuri.\nBut I couldn’t.", is_narrator=True)
    
    show_story_box("???", "So, yeah. Rest now. Just let me handle the rest.", color_override=mystery_style)
    
    show_story_box("", "...\nRest?\nNo.\nYuri. Kurona. The others.\nI refused.", is_narrator=True)
    
    show_story_box("", "Suddenly—feeling returned, my voice worked.", is_narrator=True)
    
    show_story_box("Akasuke", "If I wasn’t supposed to die like that… then fix it.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "The voice sounded surprised.", is_narrator=True)
    
    show_story_box("???", "Ehh…You’re awake already?", color_override=mystery_style)
    
    show_story_box("Akasuke", "Bring me back. Bring them back. Yuri...and Benikawa, too.", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("???", "I can. But what comes next… won’t be easy-", color_override=mystery_style)
    
    show_story_box("Akasuke", "-What do I have to do?", affiliation="Kasakura High School Student / Seven Wonders")
    
    show_story_box("", "She laughed—soft, tired, almost fond.", is_narrator=True)
    
    show_story_box("???", "You still can’t figure it out? Of course—go beat the hell out of the one that killed you~.", color_override=mystery_style)
    
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