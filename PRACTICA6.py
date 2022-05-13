#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup


def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    return BeautifulSoup(response.content, "html.parser")

def clima():
    codigo = (
        "mx"  # str(input("introduzca el codigo del pais que desea conocer la Hora: "))
    )
    base = "https://cambiohorario.com/zonas/"
    response = requests.get(base + codigo)
    soup = BeautifulSoup(response.content, "html.parser")
    tr = soup.find_all("table")[2].find_all("tr")
    timezone = tr[0]
    for row in tr[1:]:
        cols = row.find_all("td")
        t = [ele.text.strip() for ele in cols]
        print(f"{t}")
    print(tr)


if __name__ == "__main__":
    clima()
