from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot(name="PyBot",
              #read_only=True,
              storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
              logic_adapters=[
              {
                        'import_path' : 'chatterbot.logic.MathematicalEvaluation'
              }


                              #'chatterbot.logic.TimeLogicAdapter'
                              ],
              database_uri='mongodb://localhost:27017/chatterbot-database')

GREETINGS = [
             'hi there',
             'hi!',
             'i\'m cool.',
             'fine, you?',
             'always cool.',
             'i\'m ok',
             'glad to hear that.',
             'i\'m fine',
             'glad to hear that.',
             'i feel awesome',
             'excellent, glad to hear that.',
             'not so good',
             'sorry to hear that.',
             'what\'s your name?',
             'i\'m Bot. I present you our services and product, ask me a question, please.']

question = [
                'How are you?',
                'I am good.',
                'That is good to hear.',
                'Thank you.',
                'You are welcome.'
]


talk_1 = [' I services',
            'we have services after sells, we deliver to you, your product']

talk_2 = ['products',
            'we have many phone like iphone, xiaomi and samsung phone. Which brand of phone are you interested in?']

talk_3 = ['meeting',
            'We can arrange a meeting with you? are you interested?']

talk_4 = ['feedback et avis',
            'vous pouvez donnez un feedback sur les produit et sevices que nous offrons.']

#=============== create and train the bot by writing an instance of ListTraine
model = ListTrainer(bot)
for item in (GREETINGS, talk_1, talk_2, talk_3, question):
    model.train(item)
# corpus = ChatterBotCorpusTrainer(bot)
# corpus.train('chatterbot.corpus.engish')

st = True

while st:
    query = input("You : ")
    if query != "quit":
        print("Bot : ", bot.get_response(query))
    else:
        st = False
        print("Bot : Bye")
