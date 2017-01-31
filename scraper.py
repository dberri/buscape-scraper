import bs4 as bs
import requests

try:
    url = 'http://www.buscape.com.br/'

    word = 'gato'

    data = requests.get(url + word)

    soup = bs.BeautifulSoup(data.content, 'lxml')

    divs = soup.find_all('div', { 'class' : 'bui-card'})
    a = soup.find_all('a', {'class':'bui-product__link--outer'})

    nomes = {}

    for i in a:
        nome = i['title']
        preco = i['data-preco']
        nomes[nome] =  preco

    for k, v in nomes.items():
        print(k,' R$ ',v)

    mini = min(nomes, key=nomes.get)
    print('lowest: ', mini)



    # savefile = open('skoob.txt', 'w')
    # savefile.write(str(data.content))
    # savefile.close()

except Exception as e:
    print(str(e))
