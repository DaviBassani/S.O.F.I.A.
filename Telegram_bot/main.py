import telebot
import openai
import SOFIA_TOKEN
import os
import PyPDF2

CHAVE_API = SOFIA_TOKEN.token_api()
CHAVE_OPENAI = SOFIA_TOKEN.openai_api()

bot = telebot.TeleBot(CHAVE_API)
openai
import telebot
import openai
import SOFIA_TOKEN
import os
import PyPDF2

CHAVE_API = SOFIA_TOKEN.token_api()
CHAVE_OPENAI = SOFIA_TOKEN.openai_api()

bot = telebot.TeleBot(CHAVE_API)
openai.api_key = CHAVE_OPENAI
user = bot.get_me()
versao = "Versão: BETA 2.0"
model_id = 'gpt-3.5-turbo'

print("=-" * 20)
print('''
S.O.F.I.A. STATUS: ON
AUTHOR: DAVI BASSANI
CREDITS: OpenAI
''')
print("=-" * 20)

def generate_response(conversation):
    try: 
        response = openai.ChatCompletion.create(
            model=model_id,
            messages=conversation
        )
        conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
        return response
    except:
        return 'Ocorreu um erro. Tente novamente!'

conversation = []

def verificar(mensagem):
    return True
@bot.message_handler(func=verificar)
def responder(mensagem):
    user_message = {'role': 'user', 'content': mensagem.text}
    conversation.append(user_message)

    # Gera a resposta da IA e
    # adiciona a resposta da IA à conversa.
    bot.send_chat_action(mensagem.chat.id, 'typing')
    try: 
        response = generate_response(conversation)
        ai_message = response['choices'][0]['message']
        conversation.append({'role': ai_message['role'], 'content': ai_message['content']})

        #Envia a reposta para o usuário no Telegram
        bot.reply_to(mensagem, ai_message['content'])
    except Exception:
        bot.reply_to(mensagem, "Desculpe, ocorreu um erro. Tente novamente!")



bot.infinity_polling()