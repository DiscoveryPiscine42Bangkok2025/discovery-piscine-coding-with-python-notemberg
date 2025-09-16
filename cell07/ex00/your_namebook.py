def array_of_names(p):
    return[f"{f.capitalize()} {l.capitalize()}"for f,l in p.items()]

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier":"niel",
    "fifi":"brindacier"
}

print(array_of_names(persons))