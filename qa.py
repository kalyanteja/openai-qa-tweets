import os
from pydoc import cli
import openai
import click

# Get a secret from: https://beta.openai.com/overview 
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_me_something(question):
    response = openai.Completion.create(
        engine="text-davinci-001",
        prompt=f"I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with \"Unknown\".\n\nQ: {question}\nA:",
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )
    
    return response["choices"][0]["text"]

def tweet_me(hash):
    response = openai.Completion.create(
        engine="text-davinci-001",
        prompt=f"tweet something cool for {hash}",
        max_tokens=64,
    )
    
    return response["choices"][0]["text"]

@click.command()
@click.option('--entry', default="#valentinesday")
def entry(entry):
    click.echo(f"Your entry: {entry}")
    answer = tweet_me(entry)
    click.echo(f"Tweet:: {answer}")


if __name__ == "__main__":
    entry()