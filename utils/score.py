import requests
from bs4 import BeautifulSoup

#init(autoreset=True)  # Automatically resets color after each print

def get_score(username: str, categorie: str) -> str:

    # Step 1: Fetch the webpage
    url = f"https://www.root-me.org/{username}?inc=score"
    response = requests.get(url)

    output = ""

    # Step 2: Parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 3: Find and print the quotes

    categories = soup.select('.animated_box')

    for category in categories:
        name_elem = category.select_one('h4 a')
        info_elem = category.select_one('.gris')
        """
        for name, points in zip(names, info):
            output += f"\n**{name.text}**{points.text}\n"
            
            challenges = category.select('.txs li a')
            
            for chall in challenges:
                output += (
                    f"    🟢{chall.text}\n"
                    if "vert" in chall.get('class', [])
                    else f"    🔴{chall.text}\n"
                )
        """
        if name_elem and info_elem:
            name_text = name_elem.text.strip().lower()
            if name_text == categorie.lower():  # Case-insensitive match
                output += f"\n**{name_elem.text.strip()}** {info_elem.text.strip()}\n"
                
                challenges = category.select('.txs li a')
                
                for chall in challenges:
                    challenge_text = chall.text.strip()
                    if "vert" in chall.get('class', []):
                        output += f"    {challenge_text}\n"
                    else:
                        output += f"    {challenge_text}\n"
                break

    return output
