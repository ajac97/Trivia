class question:
    def __init__(self,question,ans1,ans2,ans3,ans4,correct):
        self.question=question
        self.ans1=ans1
        self.ans2=ans2
        self.ans3=ans3
        self.ans4=ans4
        self.correct=correct
    def __str__(self):
        ques_str=self.question
        ques_str += " 1) "+self.ans1
        ques_str += " 2) "+self.ans2
        ques_str += " 3) "+self.ans3
        ques_str += " 4) "+self.ans4
        return ques_str
    def is_correct(self, user_answer):
        if user_answer == self.correct:
            return True
        else:
            return False
def get_questions():
    questions=[question('How many days are in a lunar year?', '354', '365', '243', '379', 1),
                         question('What is the largest planet?', 'Mars', 'Jupiter', 'Earth', 'Pluto', 2),
                         question('What is the largest kind of whale?', 'Orca whale', 'Humpback whale', 'Beluga whale',
                                  'Blue whale', 4),
                         question('Which dinosaur could fly?', 'Triceratops', 'Tyranosaurus Rex', 'Pteranodon',
                                  'Diplodocus', 3),
                         question('Which of these Winnie the Pooh characters is a donkey?', 'Pooh', 'Eeyore', 'Piglet',
                                  'Kanga', 2),
                         question('What is the hottest planet?', 'Mars', 'Pluto', 'Earth', 'Venus', 4),
                         question('Which dinosaur had the largest brain compared to body size?', 'Troodon',
                                  'Stegosaurus', 'Ichthyosaurus', 'Gigantoraptor', 1),
                         question('What is the largest type of penguins?', 'Chinstrap penguins', 'Macaronipenguins',
                                  'Emperor penguins', 'White-flippered penguins', 3),
                         question("Which children's story character is a monkey?", 'Winnie the Pooh', 'CuriousGeorge',
                                  'Horton', 'Goofy', 2),
                         question('How long is a year on Mars?', '550 Earth days', '498 Earth days', '126 Earthdays',
                                  '687 Earth days', 4)]
    return questions
def get_answer1(list):
    p1=0
    for i in list[:5]:
        print (i)
        answer=int(input("Enter 1-4: "))
        if i.is_correct(answer):
            p1+=1

    return p1
def get_answer2(list):
    p2=0
    for i in list[5:]:
        print (i)
        answer=int(input("Enter 1-4: "))
        if i.is_correct(answer):
            p2+=1
    return p2
def who_won(p1,p2,p_a,p_b):
    if p1 > p2:
        print (p_a,"wins!!!")
    elif p2==p1:
        print("It's a tie Game!")
    else:
        print(p_b, "wins!!!")
def main():
    player_a=input("Player 1, enter your name: ")
    player_b=input("Player 2, enter your name: ")
    questions=get_questions()
    p1=get_answer1(questions)
    print("Now it is", player_b+"'s Turn!")
    p2=get_answer2(questions)
    print(player_a,"has",p1,"points.")
    print(player_b,"has",p2,"points.")
    who_won(p1,p2,player_a,player_b)
main()
