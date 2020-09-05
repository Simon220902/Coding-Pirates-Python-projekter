def faanavn():
    navn = input("Hvad er dit navn: ")
    return navn

brugeren = faanavn()

def grislatin(tekst):
    nytekst = tekst[1:] + tekst[:1] + "ay"
    return nytekst

grissebruger = grislatin(brugeren)
print("Dit navn på gris latin er: ", grissebruger)