import requests
from bs4 import BeautifulSoup
#from colorama import init, Fore, Style

#init(autoreset=True)

def get_profile(username: str) -> str:

    # Step 1: Fetch the webpage
    url = f"https://www.root-me.org/{username}"
    response = requests.get(url)

    output = ""

    # Step 2: Parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    name = soup.select_one('.tile .txt_6forum')
    output += f"\n**{name.text}**\n\n"

    clefs = soup.select('.small-6.medium-3.columns.text-center .gras')
    valeurs = soup.select('.small-6.medium-3.columns.text-center h3')

    for clef, valeur in zip(clefs, valeurs):
        output += f"**{clef.text}** : {valeur.text}\n"

    output += "\n**Catégories :**\n\n"

    # Step 3: Find and print the quotes
    challenges = soup.select('.t-body.tb-padding .gras a[title]')

    for chall in challenges:
        if chall.has_attr("title"):
            output += f"{chall['title']} ({chall.text})\n"

    return output
