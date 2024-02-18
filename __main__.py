import json
import spacy
from difflib import get_close_matches

def load_knowledge_database(file_path: str) -> dict:
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return {"questions": []}

def save_knowledge_database(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def encontrar_melhor_resultado(user_question: str, perguntas: list[str]) -> str | None:
    nlp = spacy.load("en_core_web_sm")
    user_question_tokens = nlp(user_question)
    melhor_correspondencia = None
    melhor_pontuacao = 0

    for pergunta in perguntas:
        pergunta_tokens = nlp(pergunta)
        pontuacao = user_question_tokens.similarity(pergunta_tokens)
        if pontuacao > melhor_pontuacao:
            melhor_correspondencia = pergunta
            melhor_pontuacao = pontuacao

    if melhor_correspondencia and melhor_pontuacao > 0.6:
        return melhor_correspondencia
    else:
        return None

def conseguir_resposta_para_pergunta(pergunta: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == pergunta:
            return q["answer"]

def kami_bot():
    knowledge_base: dict = load_knowledge_database("knowledge_database.json")

    while True:
        user_input: str = input("Você: ")
        if user_input.lower() == 'quit':
            print("Valeu pela conversa! te vejo mais tarde")
            break

        perguntas = [q["question"] for q in knowledge_base["questions"]]
        melhor_resultado: str | None = encontrar_melhor_resultado(user_input, perguntas)

        if melhor_resultado:
            answer: str = conseguir_resposta_para_pergunta(melhor_resultado, knowledge_base)
            print(f'Kami-: {answer}')
        else:
            print('Kami-: Eu não sei a resposta. Você poderia me ensinar?')
            nova_resposta: str = input('Escreva uma resposta ou escreva "skip" para pular: ')

            if nova_resposta.lower() != 'skip':
                knowledge_base["questions"].append({'question': user_input, "answer": nova_resposta})
                save_knowledge_database('knowledge_database.json', knowledge_base)
                print("Valeu agora eu sei de uma coisa nova!")
# Dar load na sua database, com base no arquivo json (é possivel trocar para outro arquivo caso necessário)
if __name__ == '__main__':
    knowledge_base: dict = load_knowledge_database("knowledge_database.json")
   # rodar o bot
    kami_bot()
