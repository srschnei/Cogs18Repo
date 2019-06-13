"""A collection of functions to utilize for my CatBot project."""

import string
import random

# The below variables define a collection of inputs and outputs CatBot can recognize and respond to.

GREETINGS_IN = ['hello', 'hi', 'hey', 'sup', 'meow', 'mew', 'hola', 'welcome', 'bonjour', 'greetings']
GREETINGS_OUT = ["Merrow", 'Butt scratches?',  "Hi I like pets", "Have any schnacks?"]

distinguished_cats_in = ['Garfield', 'Felix', 'Grumpy', 'Chi', 'Cheshire', 'Stubbs', 'Shiro', 'Oskar', 'Klaus', 'Henri', 'Chococat']
distinguished_cats_out = ['Was a very important character.', 'Yeah, we go way back.', 'Oh goodness, nope we are not on good terms.']

fun_in = ['funny', 'hilarious', 'ha', 'haha', 'hahaha', 'lol', 'joke']
fun_out = ["I may have 9 lives but I have no sense of hu-merw"] 

nope_in = ['water', 'loud', 'bark', 'unknown', 'tummyscratch', 'enemy']
nope_out = ['*runs away*', '*hiss*', '*swat swat*', '*flicks tail*', '*growls*']

UNKNOWN = ['Mew', 'Meow', 'Merw?', 'Merrh!', '*Purrrring*', '*Nuzzles leg*', '*Chases tail*', '*yaaaawn*', '*Tisk Tisk*', '*Licks butt*', '*Swats at air*']

QUESTION = "I'm currently pondering the meaning of life. Have any other questions?"

def is_question(input_string):
    """
    This function checks if inputted string contains a ?
    This function was borrowed from A3 assignment. 
    """
    output = False
    for i in input_string:
        if i == '?':
            output = True
    return output


def remove_punctuation(input_string):
    """
    This function removes punctuation from input string.
    This function was borrowed from A3 assignment. 
    """
    out_string = ''
    for i in input_string:
        if not i in string.punctuation:
            out_string += i
    return out_string

def prepare_text(input_string):
    """
    This function utilizes the remove_punctuation function and creates a list of split strings.
    This function was borrowed from A3 assignment. 
    """
    out_list = []
    xstring = remove_punctuation(input_string).lower()
    out_list = xstring.split(' ')
    return out_list

def selector(input_list, check_list, return_list):
    """
    This function randomizes a preset output for the chatbot, given the input.
    
    Parameters 
    ---------
    input_list = a list of words 
    check_list = a list of words that will check if they appear in the input 
    return_list = a list of potential words that will output to the desired inputs 
    
    This function was borrowed from A3 assignment. 
    """
    output = None
    for i in input_list:
        if i in check_list:
            output = random.choice(return_list)
            break

#outputs bark
def dogmode(input_list):
    """
    This function removes punctuation from input string.
    Parameters 
    ---------
    out_string = string to return  
    out_list = a list of words that will be added randomly to out_string 
    numbarks = the number of times each word from out_list will be outputted (length of input) 
    """
    out_string = ''
    out_list = ['woof ', 'bark ', 'drool ', 'aruOoOoO? ', '*pant pant* ', 'arf ']
    numbarks = len(input_list)
    for i in range(numbarks):
        out_string += random.choice(out_list)
    return out_string


"""
The 5 below functions output random cat facts within the scope of who, what, where, when, and why topics.

Credit for catfacts:
URL: https://www.buzzfeed.com/chelseamarshall/meows
Title: 82 Astounding Facts About Cats
Website Host: Buzzfeed
Author: Chelsea Marshall
"""

def what_fact(input_string):
    whatfacts = ['A group of cats is called a clowder.', "A cat's brain is 90% similar to a human's — more similar than to a dog's.", "The world's largest cat measured 48.5 inches long.", "A cat's cerebral cortex (the part of the brain in charge of cognitive information processing) has 300 million neurons, compared with a dog's 160 million.", 'Cats sleep 70% of their lives.', 'Cats have over 20 muscles that control their ears.', 'Cats are the most popular pet in the United States: There are 88 million pet cats and 74 million dogs.', "Cats can't taste sweetness.", 'There are cats who have survived falls from over 32 stories (320 meters) onto concrete.']
    return random.choice(whatfacts)

def who_fact(input_string):
    whofacts = ['A cat has been mayor of Talkeetna, Alaska, for 15 years. His name is Stubbs.', "The world's richest cat is worth $13 million after his human passed away and left her fortune to him.", 'When asked if her husband had any hobbies, Mary Todd Lincoln is said to have replied "cats."', 'Isaac Newton is credited with inventing the cat door.', 'In the 15th century, Pope Innocent VIII began ordering the killing of cats, pronouncing them demonic.']
    return random.choice(whofacts)

def where_fact(input_string):
    wherefacts = ['The first cat in space was French. She was named Felicette, or "Astrocat." She survived the trip.', "There are 45 Hemingway cats living at the author's former home in Key West, Fla. Polydactyl cats are also referred to as 'Hemingway cats' because the author was so fond of them.", 'Cats were mythic symbols of divinity in ancient Egypt.']
    return random.choice(wherefacts)

def when_fact(input_string):
    whenfacts = ["Evidence suggests domesticated cats have been around since 3600 B.C., 2,000 years before Egypt's pharaohs.", 'The oldest cat video on YouTube dates back to 1894 (when it was made, not when it was uploaded, duh).', 'In the 1960s, the CIA tried to turn a cat into a bonafide spy by implanting a microphone into her ear and a radio transmitter at the base of her skull. She somehow survived the surgery but got hit by a taxi on her first mission.']
    return random.choice(whenfacts)

def why_fact(input_string):
    whyfacts = ['Owning a cat can reduce the risk of stroke and heart attack by a third.', 'Cat owners who are male tend to be luckier in love, as they are perceived as more sensitive.', "The frequency of a domestic cat's purr is the same at which muscles and bones repair themselves.", 'Cat owners are 17% more likely to have a graduate degree.']
    return random.choice(whyfacts)

def end_chat(input_list):
    """
    This function quits the conversation with CatBot. 
    
    Parameters 
    ---------
    input_list = a list of words
    'quit' is the specified word that will produce an output 
    
    Response 
    --------
    When presented with the word 'bye' the CatBot quits 
    
    This function was borrored from A3 assignment. 
    """
    output = False
    if 'bye' in input_list:
        output = True
    return output

def cat_bot():
    """
    This is the main function for the CatBot chatbot.
    It was borrowed/modified from A3 assignment with emphasis on relevance to the all powerful CatBot's wishes. 
    """
    print("Meow! I am a claw-ver cat bot! Give me your pets and your food or else!!!!!.....\
          \nI only answer to regular english human speech.\
          \nSay: 'bye' to quit, 'dog' for dogmode,\
          \nAsk me who/what/where/when/why questions for random cat facts!")
    

    chat = True
    while chat:
        
        # Get message from user
        msg = input('ME: ')
        out_msg = None
        
        # Check if the input is a question
        question = is_question(msg)
        
        # Prepare the input message
        msg = prepare_text(msg)
        
        # Check for an end msg 
        if end_chat(msg):
            out_msg = "Goodbye! \
            \nIf you want to adopt a cat, you can visit your local \
            \nHumane Society or check out petfinder.com. \
            \nCat facts provided by Buzzfeed."
            chat = False

        #Prepare and inplement outputs for specific inputs and non expected inputs
        if not out_msg:
            
        
            msg_list = []
            
#           question = False

            msg_list = prepare_text(msg)

            #for loop initializing random preset responses for undelightful inputs for CatBot
            for i in nope_in:
                if i in msg:
                    out_msg = random.choice(nope_out)

                    
            #implement dogmode function
            if 'dog' in  msg_list:
                out_msg = dogmode(msg)
                
            #implement is_question
            if is_question(msg):
                question = True

            #output what_fact function if asked 'what' (with '?')
            if question == True:
                if 'what' in  msg_list:
                    out_msg = what_fact(msg)
                    
            #output who_fact function if asked 'who' (with '?')           
            if question == True:
                if 'who' in  msg_list:
                    out_msg = who_fact(msg)    
            
            #output where_fact function if asked 'where' (with '?')           
            if question == True:
                if 'where' in  msg_list:
                    out_msg = where_fact(msg)  
                    
            #output where_fact function if asked 'when' (with '?')           
            if question == True:
                if 'when' in  msg_list:
                    out_msg = when_fact(msg)  
                    
            #output where_fact function if asked 'why' (with '?')           
            if question == True:
                if 'why' in  msg:
                    out_msg = why_fact(msg)  
                    
                                             
        # If we don't have an output yet, but the input was a question, return msg related to it being a question
        if not out_msg and question:
            out_msg = QUESTION

        # Catch-all to say something if msg not caught & processed so far
        if not out_msg:
            out_msg = random.choice(UNKNOWN)
            
        print('CatBot:', out_msg)