# Reverse Word Order 

frase = "dennis rinaldim barbosa guimaraes"

def reverter():
    a = frase.split()
    n = -1
    b = []
    frase_contrario = ""
    
    for palavras in a:
        b.append(a[n])
        n -= 1
    
    for palavras in b:
        frase_contrario = " ".join(b)
    
    return frase_contrario

print(reverter())