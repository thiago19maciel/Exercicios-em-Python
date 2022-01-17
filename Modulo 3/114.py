import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
    print("O site Pudim esta acessivel")
except:
    print("O site Pudim nao esta acessivel")

print("Obrigado! Volte sempre =)")