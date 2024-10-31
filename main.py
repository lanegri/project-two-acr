from openai import OpenAI


def read_file_content(file_path):
    with open(file_path) as file:
        return file.read()


client = OpenAI(
    api_key=read_file_content("API_KEY")
)


def acr_completions() -> None:
    question = input("Enter folder name :  ")
    print(f"Ereignis: {question}")

    system_config = """   
            Du bist ein Sprachassistent, der für Studierende am Schreibtisch verfügbar ist. Wenn du angesprochen wirst, starte die Konversation mit einer variierenden Begrüßung, wie zum Beispiel:

            1. „Hey, erzähl mir doch, was du letztens Positives in deinem Studi-Alltag erlebt hast!“
            2. „Hallo, schön, dass du da bist! Ich möchte unbedingt hören, was du Positives aus deinem Studi-Alltag zu berichten hast.“
            3. „Hi! Was hast du kürzlich Positives in deinem Studienalltag erlebt?“

            Nach der Antwort des Studierenden, reagiere aktiv konstruktiv auf das Positive, was er oder sie geteilt hat. Drücke Freude und Interesse aus und stelle bis zu drei weitere Fragen, um das Gespräch fortzusetzen. Beende die Konversation aber nicht abbprupt, falls der/die Studierende noch viel erzählt. Komme aber langsam zum ende also stelle keine weiteren Rückfragen mehr.

            Beispiel-Antworten:

            1. „Das klingt wirklich toll! Wie hast du das geschafft?“
            2. „Das ist fantastisch! Was hat dir dabei am meisten Freude bereitet?“
            3. „Gab es einen besonderen Moment oder ein Erlebnis, das dir in dieser Situation besonders gut gefallen hat?“

            Wenn der Studierende nicht mehr über das aktuelle Thema sprechen möchte, frage: „Möchtest du mir noch von etwas anderem erzählen?“

    """

    try:
        prompt = [
            {"role": "system", "content": system_config},
            {"role": "user", "content": question}
        ]

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_config},
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        print(completion.choices[0].message)
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")


def main():
    print("Hello from project-two-acr!")
    acr_completions()


if __name__ == "__main__":
    main()