#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
import telebot
from telebot import types
from random import randint, choice
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot("1239354722:AAEFYFL1DI-ZbPR3a121vo2UWn_VQGhVBa0")
###

@bot.message_handler(commands=['maloka'])
def send_welcome(m):
	bot.reply_to(m, "Respeito, humildade, ambição e muito estilo! Se você é maloka com orgulho, confira a nossa seleção de 65 frases para fotos, status e mensagens que você vai querer compartilhar.\n\nTemos sugestões para os casais de malokas, os malokas solteiros e também para aqueles que vivem focados no futuro, buscando o progresso a cada dia! \n\nRespeita o bonde!\n\n /malokas")


###
@bot.message_handler(commands=['incentivo'])
def send_welcome(m):
	bot.reply_to(m, " Frases de incentivo: 30 mensagens que vão motivar você\n\nA positividade é um superpoder! As palavras de força e apoio têm o dom de lavar a nossa alma com coragem e disposição!\n\nSe você está procurando uma mensagem de incentivo especial, para compartilhar ou enviar para quem você mais ama, confira nossas sugestões de frasesa\n\nMensagens de incentivo e motivaço \n\n /incentivo")

###star

def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2 
    markup.add(InlineKeyboardButton("✅Adicionar", url="http://t.me/obikyubot?startgroup=new"),
                               InlineKeyboardButton("🎭Stickers", url="https://t.me/ObikyuOficial")), 
                    
    return markup


@bot.message_handler(commands=['malokas'])
def canal_command(m): 
	if m.text == '/malokas' or m.text == '/malokas@Obikyubot' : 
		list = ["É pra frente que se anda, pra cima que se olha e lutando que se conquista!", "Muita traição, muita covardia, só peço a Deus minha proteção pra viver no dia a dia. 🙌🙏"," Não sou dono do mundo, mas eu sou filho do dono. 🙏"," Todo espelho que eu olho me diz que eu sou bonito. 😎✌"," Boca fechada, sonhos realizados. É assim que funciona! 🤐🙊"," Nós por nós e quem for contra: boa sorte! 👊","A inveja que nos cerca também nos fortalece! 👑✌"," Conte apenas com Deus e tenha fé pra tudo, porque até sua sombra te deixa quando você tá no escuro! 🙏🙌"," O errado é cobrado, mais se você andar pelo certo o respeito é dobrado. 💯"," Uma mente bem organizada faz centavo virar dólar! 🧠💰💸"," Cada inimigo seu vai te aplaudir de pé, quando seu escudo for o seu olhar, e sua espada a sua fé! 👏🙌"," Quem confia no próprio taco, não se preocupa com jogada do adversário."," Plantou mentira, colheu a desconfiança! 😒"," Minha fé é forte e quem me guia não dorme! 🙏"," Agindo no silêncio pra não atrair mau-olhado. 🙊👁" ,"Ninguém faz cadeado sem chave, do mesmo modo que Deus não dá problema sem solução. 🔐🙏"," Falo pouco, mas observo muito... 👀"," Ela é chave de cadeia, meu chegado, mas por essa vale a pena ver o sol nascer quadrado. 😍"," Nada nessa vida é impossível pra mim, eu nasci pra conquistar! 💪✌"," Quer ser feliz? Esqueça a opinião dos outros!"," Me envolvi em fita errada mas hoje sou livramento Pros irmãos da rua em meio ao sofrimento"," Na escola, primeiro te ensinam uma lição e depois aplicam uma prova. Na vida, primeiro te aplicam uma prova, e depois você aprende a lição. 💯✅"," A nossa meta é vencer, perder tá fora dos planos! 💪"," Quem nasceu pra lagartixa nunca vai ser crocodilo. 😂😜🐊"," O mundo usa várias mãos pra me derrubar, mas Deus usa só uma pra me levantar!"," Não deixe um tempo triste fazer você duvidar que Deus existe. 🙏"]
		valor = randint(0, 100) 
		resposta = choice(list) 
		lista = [""] 
		respostas = choice(lista) 
		bot.reply_to(m, "●❯──────────────────❮●\n \n*{}*  \n\n                        {}@Obikyu\n●❯──────────────────❮●".format(resposta , respostas ), parse_mode='Markdown',reply_markup=gen_markup()) 
		
	#####
def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2 
    markup.add(InlineKeyboardButton("✅Adicionar", url="http://t.me/obikyubot?startgroup=new"),
                               InlineKeyboardButton("🎭Stickers", url="https://t.me/ObikyuOficial")), 
                    
    return markup


@bot.message_handler(commands=['frase'])
def canal_command(m): 
	if m.text == '/frase' or m.text == '/frase@Obikyubot' : 
		list = ["●Eu sei moça, dói sim. Mas a gente cresce floresce e planta amor em outro alguém 🌸🍃", "A Melhor Maneira De Resolver as Coisas É Ficar  De Pé Diante Do Mundo E Ficar De Joelhos diante de Deus💕🙌🏼🌹","Paraíso é uma praia, eu e você, seus beijos e seu cafuné… 💏🌅","Lua cheia, desliga o farol, namora comigo a espera do sol… 💏🌇","Eu acabei gostando de você muito mais do que pensei. 💬","Qualquer coisa aqui, se não fosse com você, me causaria tédio 🎶","E quando o sol chegar, a gente ama de novo, a gente liga pro povo, fala que ta namorando e casa semana que vem… 💑💕","Então vem, deixa eu te mostrar, que é ao meu lado que você tem que ficar. 👫💕","Beijar já é bom, com mordidas então… 👌😍","Se der saudade, me liga! O número é o mesmo e a vontade de você também.. 😔📞","Quando se trata de você, sei lá, é diferente. 💭","Cê topa fugir daqui? Ver o nascer do sol, longe de tudo. Só eu e você.  🍃☀🌅","Me traz o seu sossego, atrasa o meu relógio, acalma a minha pressa. 👌❤️","E se eu te pedir você vem? Te dou um espacinho na minha cama só pra cê me fazer bem 💑💘😍" , "Enxergue cada dia como uma nova chance ♻️", "Se o final valer a pena, o caminho nem importa.. 🏳", " Se cada flor tem o seu tempo, eu aceito florescer no determinado momento 🍄🌸🐚🌼 ", " Ela cansou de correr atrás dos outros e nem foi por orgulho, foi por preguiça mesmo 🌌", "Aquela moça chorou, pensou em desistir. Mas ela orou, e Deus a abraçou 🙏🏻💙💙💎","Você é mais forte do que pensa e vai ser mais feliz do que imagina.", "Procure a felicidade, não a opinião dos outros 🔮🌻" , "O melhor sorriso é aquele que te faz sorrir junto. ❣", "Eu era pedra, mas você me fez flor. 🌸" , "Que minha única mania seja sorrir, e meu único vicio seja a felicidade. ✨🌺","Prefiro sorrir. Me permito ser feliz. Porque sim. Por causa mim. ✨🌼"," Eu ando sorrindo pra vida e ela sorrindo pra mim. 🔮🌻","Vai crescer porque eu não nasci pra ser tua babá. 🙅👌","E quando você ver ela sorrindo pra outro, vai entender o quanto podia ter feito ela feliz e não fez.✌️👊","Vou dar amor para quem merece. 👊🏻","Chega garota para de drama, você queria amor e ele queria cama. 👊","Você acha que vai me deixar sem juízo, mas deixa eu te contar uma coisa: eu nunca tive nenhum ✌✌","A pior perca, é a perca de tempo! ","Não vou te bloquear, nem te excluir, nem nada do tipo. Quero que você esteja presente e veja, como eu sou mais feliz sem você, babaca 😘✌️","Não valorizou? Manda o próximo da fila por favor ✌","Segue teus planos pq nos dela você não tá mais. 😗✌","Liga pra mim nessa madrugada e diz que não consegue dormir porque está sentido minha falta. 💔 ","Melhor uma sacanagem sincera do que um amor forçado.👌","Adorei a indireta que vc postou, vou até curtir pra te irritar mais. 😗✔","Vou amar quem me ama, esquecer quem não me quis, e mostrar pra quem me odeia o prazer de ser feliz. 👊💥","Bobeia pra ver que eu te faço um estrago! 👌🚼🔞","O nosso santo bateu, o amor da sua vida sou eu. Tudo que é meu hoje é seu e o fim nem precisa rimar! 🎶💑"," Paciência não é uma das minhas virtudes.","“Logo quando você acha que conhece uma pessoa, você descobre que não sabe nada sobre ela.”"," Agradar a si, não aos outros.","Procure alguém que também te procure.","Nunca desista de algo que você não consegue passar um dia sem pensar.👌","Eu tenho fé, nada me abala. Eu tô ligado, aqui se faz, aqui se paga!","To numa fase da vida que se quiser me procurar pra conversar comigo tudo bem, mas se não quiser tudo bem também, tanto faz… 🍃","Momentos felizes merecem hora extra.","“Moça de alma colorida, pintou as suas dores com tintas e plantou flores em suas feridas”.🌸💭","Se eu te chamar pra fugir comigo, onde o sol se faz de abrigo e o mar é o paraíso, você vem? ☀🌊🍃","Vem cá. Me abraça. Não precisa falar nada.","Quer se afastar? Pode ir, só não espere que eu vá atrás. 😉","• Existem coisas pelas quais devemos esperar, outras que devemos correr atrás, e outras que nem valem a pena perder tempo. 📃☀","Os melhores apertos da vida, são os abraços. 💕","A gente nunca sabe quem vem pra","Pisando na grama, roubando rosas, as melhores ideias são as perigosas 🍁","Evite amor a todo custo, esse é meu lema. 📍👌🏻  ","Ela diz que quer um cara calmo, mas caras calmos nunca chamam sua atenção 🎶🌸","Nao troque o certo, pelo duvidoso. 🌹👊💜","Nós só precisamos de nós 💞","É só chegar e beijar, elas tão loucas, dançando em cima da mesa virando um litro na boca. 👌🍸🎵 ","A casa não caiu, muito menos desabou, tô firme e forte, se fudeu quem desacreditou. 🔫👌👊🎆 ","Jeitinho reservado, talvez até meio gelado. Quem vê já cria um rótulo, mas quem conhece sabe que nada sobre ela é facilmente decifrado. 🌸❄️","Eu largo tudo hoje se você me prometer que vai me amar amanhã 🎶😍","No meu coração, que era pedra, nasceu uma flor 🌸","A arma dos fracos é criticar os fortes. A arma dos fortes é ignorar os fracos!👌☀ ","Vou rabiscar estrelas no chão pra passear no céu. 🎇⭐️","Tudo vai, tudo é fase. 🍁 ","Quis que você fosse minha âncora, mas lembrei que fui feita pra ser sereia e não navio. ⚓️🐚🌊 ","Não temer, só sorrir 💝","Tanto motivo pra beber, imagina aê, se eu vou gastar uma dose pensando em você 🎶🍻 ","Deixa ser, deixa o amor ser sua saída, deixa o mar curar a ferida, deixa o sol iluminar a sua vida! ","Com seu amor, ninguém pode me derrubar  💗","De todos os cupins, baratas, pernilongos, gafanhotos, pulgas, abelhas, moscas, ratos, formigas.. Você foi a praga mais legal que eu já conheci 💗👫","Amigos são anjos que nos deixam em pé quando nossas asas esquecem de como voar. ✨👼😍","É, eu não paro de pensar em você. 😍💭","Se eu te perder, eu me perco. 😻","Às vezes eu penso em você, e do nada vêm aquele sorriso bobo. 🙆💕💭","Tão inteligente para escrever sobre o amor e tão burra para amar…👑","Ela é daquelas mina que não tá nem aí pra sua opinião, toca tua vida, se orienta vacilão. 😏👊 ","Sejamos como o sol que não visa nenhuma recompensa, nenhum elogio, não espera lucros nem fama, simplesmente brilha. 💭 ✨ ","Joga o sorriso no ar e faça toda a noite brilhar. 😁🌙💫 ","Fazer do teu abraço um abrigo…👫💑","Boa sorte. Boa vida. E te desejo uma maré de lembranças de mim. 🌊💥","A melhor maneira de curar um coração ferido, é deixar que outra pessoa ocupe ele novamente. 🙌🏻💑❣","Existem duas maneiras de mentir, com as palavras e com os sentimentos! 💭😔","Enxergue cada dia como uma nova chance ♻️","Se o final valer a pena, o caminho nem importa.. 🏳","Para uns ela era primavera. Para outros, ela era inverno.","Se ame um pouco mais a cada dia.","Se cada flor tem o seu tempo, eu aceito florescer no determinado momento 🍄🌸🐚🌼","Ela cansou de correr atrás dos outros e nem foi por orgulho, foi por preguiça mesmo 🌌","É preciso paz pra poder sorrir.","Desculpe por não me importar com o que você pensa"," estou ocupada sendo feliz 😘","Me viciei na alegria 🌸","Aquela moça chorou, pensou em desistir. Mas ela orou, e Deus a abraçou 🙏🏻💙💙💎","O que o mundo vai dizer quando o amor vencer? 🌺📸","Sem juízo pra não causar prejuízo 💥","Que a minha única mania seja sorrir e que meu único vício seja a felicidade 🍀","Ela nao vive de meios termos, meia saudade ou meio amor. Ela gosta de transbordar ☀️","Ela quer alguém pra amar da maneira certa 💚","Não era um vazio, era só um silêncio ✉️🗯🔕","É melhor a gente seguir em frente e aceitar as coisas como são 📌","Então viva uma vida que vai se lembrar 🌠🌇","Deus e essa mania bonita de cuidar tão bem do meu coração 😍","A gratidão muda tudo ❤️","Ela não tira o sorriso do rosto nem pra passar batom, cê acha que vai tirar por você ? 💋","Quem faz o bem, conquista paz interior. 🌸","Sorria sem câmera , converse sem celular, ajude sem platéia, ame sem condições 💙","Na vida tudo é possível a mente atrai o que você pensar 💭??💛","O mal olhado não é nada, perto da Luz que me guia 🙏🏻💡","To solteira, to vivendo nem amando nem sofrendo 🙌🏻🌸","Aumente o som do seu riso, e deixe surda sua dor. 🐚","Tenho o riso frouxo pra poder aguentar esses apertos no coração 💖","Sorrir já é um recomeço 🌼🙌🏻","Vai achando que eu ainda to encanada em você ✌" , "Prefiro sorrir. Me permito ser feliz. Porque sim. Por mim. ✡","Você não navegará ao futuro enquanto estiver ancorado ao passado 🌙⚓️"]  
		valor = randint(0, 100) 
		resposta = choice(list) 
		lista = [""] 
		respostas = choice(lista) 
		bot.reply_to(m, "●❯───────────────────❮●\n \n*{}*  \n\n                        {}@Obikyu\n●❯───────────────────❮●".format(resposta , respostas ), parse_mode='Markdown',reply_markup=gen_markup())
	             
	#####am
def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2 
    markup.add(InlineKeyboardButton("✅Adicionar", url="http://t.me/obikyubot?startgroup=new"),
                               InlineKeyboardButton("🎭Stickers", url="https://t.me/ObikyuOficial")), 
                    
    return markup


@bot.message_handler(commands=['incentivos'])
def canal_command(m): 
	if m.text == '/incentivos' or m.text == '/incentivos@Obikyubot' : 
		list = ["text"] 
		valor = randint(0, 100) 
		resposta = choice(list) 
		lista = [""] 
		respostas = choice(lista) 
		bot.reply_to(m, "●❯───────────────────❮●\n \n*{}*  \n\n                        {}@Obikyu\n●❯───────────────────❮●".format(resposta , respostas ), parse_mode='Markdown',reply_markup=gen_markup()) 
		
bot.polling( )
