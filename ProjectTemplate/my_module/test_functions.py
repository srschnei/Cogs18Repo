from my_module.functions import dogmode, what_fact, who_fact, where_fact, why_fact, when_fact, cat_bot


"""Test for my functions.
"""

def test_dogmode():
    assert callable(dogmode)
    input_list = ('My dog would chase you')
    assert dogmode(input_list) == True
    
    
def test_dogmode():
    assert callable(dogmode)
    input_list = ('My cat would chase you')
    assert dogmode(input_list) == False


def test_what_fact(input_string):
    whatfacts = ['A group of cats is called a clowder.', "A cat's brain is 90% similar to a human's — more similar than to a dog's.", "The world's largest cat measured 48.5 inches long.", "A cat's cerebral cortex (the part of the brain in charge of cognitive information processing) has 300 million neurons, compared with a dog's 160 million.", 'Cats sleep 70% of their lives.', 'Cats have over 20 muscles that control their ears.', 'Cats are the most popular pet in the United States: There are 88 million pet cats and 74 million dogs.', "Cats can't taste sweetness.", 'There are cats who have survived falls from over 32 stories (320 meters) onto concrete.']
    return random.choice(whatfacts)
    msg = 'what'
    if question == True:
      if 'what' in  msg_list:
          assert out_msg == what_fact(msg)