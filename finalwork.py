import sqlite3
import random
class PlayersDB:
    def __init__(self, dbpath):
        self.conn = sqlite3.connect(dbpath)
        self.cur = self.conn.cursor()
    def drop_table(self):
        self.cur.execute('DROP TABLE players')
    def create_tables(self):
        self.cur.execute(
            'CREATE TABLE IF NOT EXISTS players (id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT, score INTEGER)')
    def insert_player(self,username):
        self.cur.execute('INSERT INTO players (username,score ) VALUES (?, ?)', (username, 0))
        self.conn.commit()
    def update_result(self, id, score):
        self.cur.execute('UPDATE players SET score = (?) WHERE id = (?);', (score, id))
        self.conn.commit()
    def delete_player(self, name):
        self.cur.execute('DELETE FROM players WHERE username = (?);', (name,))
    def find_player(self, by_name=""):
        try:
            list_of_results = self.cur.execute('SELECT id, score FROM players WHERE username = (?);', (by_name,)).fetchall()
            id=list_of_results[-1]
        except:
            id=(0,)
        return id
    def close(self):
        self.conn.close()
class Player:
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def intro(self):
        print (f"{self.name}! Welcome to the game! Your score is {self.score}")
class GuessLetters:
    def __init__(self,sentence):
        self.sentence=sentence
    def play(self):
        result = ""
        the_name=self.sentence
        print(the_name)
        for word in the_name.split(" "):
            result += "*" * len(word) + " "
        print(result)
        while ("*" in result):
            guess = input("Guess a character: ").upper()

            if len(guess) != 1:
                print("Please enter only one char!")
            else:
                count = the_name.count(guess)  # cik tādu burtu ir vārdā?
                if count > 0:
                    process = ""
                    for c1, c2 in zip(the_name, result):
                        if c1 == guess:
                            process += c1
                        else:
                            process += c2  # create new string by adding char to old string
                    result = process
                else:
                    print(f"Sorry, no '{guess}' in the text")

                print(f"The result is {result}")
        print("Congratulations!!! You win!")
        return 1


if __name__ == '__main__':
    username=input('Enter user name: ')
    if username=='':
        print('See you later!')
        exit()
    session=PlayersDB('chinook.db')
#    session.drop_table()
    session.create_tables()
    player=session.find_player(username)
    id=player[0]
    if id==0:
        session.insert_player(username)
        player = session.find_player(username)
        id=player[0]
    score = player[1]
    player1=Player(username,score)
    player1.intro()
    # here should be a code of playing game
    with open('sentences.txt', encoding="utf-8") as f:  # create a file object
         lines = f.readlines()
#    the_name=random.choice(lines).upper()
    game=GuessLetters(random.choice(lines).replace('\n','').upper())
    repeat = 'y'
    while repeat != '':
        flag=game.play()
    #    the_name = input("Enter the text: ").upper()
        if flag==1:
            score+=1
        repeat=input('Enter any symbol to continue the game')
    print(f"Your score is {score}")
    session.update_result(id,score)
    session.close()


