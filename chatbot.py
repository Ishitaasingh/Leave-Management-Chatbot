from __future__ import print_function

from nltk.chat.util import Chat

reflections = {
    "am": "are",
    "was": "were",
    "i": "you",
    "i'd": "you'd",
    "i've": "you'v",
    "ive": "you'v",
    "i'll": "you'll",
    "my": "your",
    "are": "am",
    "you're": "i'm",
    "you've": "i've",
    "you'll": "i'll",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "u": "me",
    "ur": "my",
    "urs": "mine",
    "me": "u",
}

# Note: %1/2/etc are used without spaces prior as the chat bot seems
# to add a superfluous space when matching.

pairs = (
    (
        r'I\'m (.*)',
        (
            "Hi!%1?? What can I provide you?",
            "Hi!%1? How can I help you?",
        ),
    ),
    (
        r'I want to apply for leave(.*)',
        (
            "Specify the type of leave which you want to apply for:"
            "\n\n1.~~~~~~~~~~~~~~~~~~~~~~~~~~~~ANNUAL LEAVE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
            "\n•less than ten years of total state service= maximum annual leave balance of 240 hours."
            "\n•completed ten years of total state service=maximum annual leave balance of 288 hours."
            "\n•completed fifteen years of total state service=maximum annual leave balance of 336 hours."
            
            "\n\n2.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~SICK LEAVE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
            "\nFull-time employees=80 or more hours."
            
            "\n\n3.~~~~~~~~~~~~~~~~~~~~~~LEAVE FOR EMERGENCY SERVICES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
            "\nEmployees who are certified=max. 15 working days in any state fiscal year."
            
            "\n\n4.~~~~~~~~~~LEAVE OF ABSENCE WITHOUT PAY FOR FAMILY AND MEDICAL CARE(FMLA)~~~~~~~~~~~\n"
            "\n12 weeks of unpaid, job-protected leave to employees for certain family and medical reasons. \nTo be eligible for FMLA leave, an employee must be employed with the state for at least one year and must have worked at least 1,250 hours over the previous 12 months.  FMLA leave will be granted for the following reasons:"
            "\n•To care for the employee’s child after birth, or placement for adoption or foster care"
            "\n•To care for the employee’s spouse, son or daughter (under 18 years of age), or parent who has a serious health condition"
            "\n•For a serious health condition that makes the employee unable to perform the employee’s job"

            "\n\n5.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~SHARE LEAVE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
            "\nGranted to an employee in the agency who has experienced a catastrophic illness or injury and who has used all their accrued leave."
            "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            
            "\n\nSELECT FROM THE ONES MENTIONED ABOVE:",
            
        ),
    ),
    (r'(.*)annual leave', ("You want to apply for annual leave.",),),
    (
        #r'Do (you) want anything else (.*)\??',
        r'yes',
        ("You need to mention the duration of your leave.",
         "Okay,now you need to mention the duration of your leave.",
         "Now kindly mention the duration of your leave.",
         ),
        ),

    (r'(.*)sick leave', ("You want to apply for sick leave.",),),
   
    (r'(.*)leave for emergency services', ("You want to apply leave for emergency services.",),),
   

    (r'(.*)fmla', ("You want to apply for family and welfare leave.",),),
    

    (r'(.*)share leave', ("You want to apply for shared leave.",),),
    
    (
        r'can i apply for a leave\?',
        (
            "Yeah sure",
        ),
    ),
    (
        r'okay\,dates are(.*)',
        ("These dates available.",
         "Okay!the duration mentioned by you can be made available.",
         "Okay",),
    ),


    (
        r'confirm (.*)',
        (
            "You need to provide your email id for confirmation.",
        ),
    ),



    
    (
        r'(.*)\@(.*)\.com',
        (
            "Okay,it has been saved.A confirmation email will be sent soon.",
            "We'll confirm your application soon.",
        
        ),
    ),





    (
        r'(are) (you) (.*)',
        ("am i%1??! I'm not getting you."),
    ),
    (
        r'what (.*) confirm(.*)',
        ("You need to provide your email id.",),
    ),
    (r'how (.*) confirm(.*)', ("You need to provide your email id.",)),
    (r'(hi|hello|hey) (.*)', ("Hi! how are you?",)),





    
    (
        r'quit',
        (
            "Thanks!",
            "Thankyou!I'm glad that I could help.",
            "Thankyou!",
        ),
    ),

    (
        r'(Thanks|thanks)(.*)',
        (
            "You're welcome!I'm glad that I could help.",
            "You're welcome!",
        ),
    ),
    
    (
        r'(.*)',
        (
            "I'm sorry.I didn't get you.",
            "Can you say it again",
            "Enter a valid response",
            "Behave yourself",
        ),
    ),
)

chatbot = Chat(pairs, reflections)


def Newt_chat():
    print("*"* 27,"NEWT (Leave Application)","*"* 27)
    print('=' * 80) 
    print("Talk to the program by typing in plain English, using normal upper-")
    print('and lower-case letters and punctuation.Enter "quit" when done.')
    print('=' * 80)
    print("\n\nHi!May I know who am I talking to?")

    chatbot.converse()



def demo():
    Newt_chat()



if __name__ == "__main__":
    demo()
