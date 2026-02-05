# $ python a.py
print("nom module fichier a.py" + __name__)
# nom module fichier a.py __main__
import b
print(b.chiffre)
#42
print("nom module fichier b.py" + b.__name__)
# nom module fichier b.py : b
