import random
lives=6
def generate_blankspace(word):
    blank_space=[]
    i=1
    while i<=length_of_word_selected:
        blank_space.append('_')
        i+=1
    return blank_space


def checking_guessed_letter(guessed_letter):

    index_of_letter=word_selected.find(guessed_letter)
    count_of_guessed_letter=word_selected.count(guessed_letter)
   
    if index_of_letter>=0:
          fill_letter_blankspace(index_of_letter,guessed_letter)
          draw_hangman(lives)
    else:
           lives-=1
           print(f"you guessed {guessed_letter} that is not present in the word.So you lose a life")
           print(generated_blankspace)
           draw_hangman(lives)
    

   
    
def fill_letter_blankspace(index,correct_letter):
     generated_blankspace.pop(index)
     generated_blankspace.insert(index,correct_letter)
     print(generated_blankspace)
     draw_hangman(lives)
    
def draw_hangman(live):
     if live==6: 
      print("""          *---*
                         |    |
                              |
                              |
                              |
                              |
                    ==============    """
            )
     elif live==5:
      print("""          *---*
                         |    |
                         O    |
                              |
                              |
                              |
                    ==============    """
            )
     elif live==4:
      print("""          *---*
                         |    |
                         O    |
                         |    |
                              |
                              |
                    ==============    """
            )
     elif live==3:
      print("""          *---*
                         |    |
                         O    |
                        /|    |
                              |
                              |
                    ==============    """
            )
     elif live==2:
      print("""          *---*
                         |    |
                         O    |
                        /|\   |
                              |
                              |
                    ==============    """
            )
     elif live==1:
      print("""          *---*
                         |    |
                         O    |
                        /|\   |
                        /     |
                              |
                    ==============    """
            )
     else:
       print("""         *---*
                         |    |
                         O    |
                        /|\   |
                        / \   |
                              |
                    ==============    """
            )
  

print("let's play hangman!!")
print('you have only 6 lives so try to guess the word within 6 attempts!Good Luck!!')
word_list=['apple','mango','guava','hello','airport','train','eating','flower','rupees','chicago','delhi','newyork','trees','sand','adulthood','leaves','pineapple','painting','greens']
word_selected=random.choice(word_list)
length_of_word_selected=len(word_selected)
print(word_selected)
generated_blankspace=generate_blankspace(word_selected)
print(generated_blankspace)
game_over=False

while lives!=0:
  letter=input("Guess a letter:")
  checking_guessed_letter(letter) 







    