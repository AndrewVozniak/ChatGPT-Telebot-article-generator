import openai
import time
import handlers.app as app

openai.api_key = "key"

model_engine = "text-davinci-003" 
max_tokens = 1024 
temperature = 0.9

def generate_text(prompt):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        temperature=temperature,
    )
    return response.choices[0].text

def generate_article(topic, language, lenght):
    print("Generating...")
    prompt = f"Write an article. Topic: {topic}. Language: {language}. Lenght: {lenght} symbols. Finish the text in a natural way so that it has a complete structure and does not break off in the middle of a sentence:\n\n"
    generated_text = ""

    while len(generated_text) < lenght:
        chunk = generate_text(prompt)
        generated_text += chunk
        print("----------------------------------------------")
        print(generated_text)
        prompt = chunk[len(chunk) - 1000 :] + f"\nWrite the next 1000 words on {topic}:\n\n{generated_text}"
        time.sleep(5)


    final_text = app.truncate_last_sentence(generated_text)

    print("---------------------------------------------- FINAL TEXT ----------------------------------------------")
    print(final_text)
    print("---------------------------------------------- FINAL TEXT ----------------------------------------------")
    return final_text
