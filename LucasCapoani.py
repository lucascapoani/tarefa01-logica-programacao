lista_jovem = []
lista_adulto = []
lista_idoso = []
aluno = 0

print("Para saber o resultado digite 'fim' ")
while aluno <= 40:
    aluno = aluno + 1
    print("Digite a idade do aluno: ")

    teclado =(input(">>> "))

    if teclado == 'fim':
        media = (sum(lista_jovem) + sum(lista_adulto) + sum(lista_idoso))/(len(lista_jovem) + len(lista_adulto) + len(lista_idoso))
        print ("A media de idades da turma é : ",media)
        if media <= 25:
            print ("Portanto, pode-se dizer que a turma é jovem")
        elif media > 25 and media <= 60:
            print ("Portanto, pode-se dizer que a turma é adulta")
        else:
            print ("Portanto, a turma é de idosos.")


        print("Para essa turma, a maior idade digitada para a: ")
        try:
            maiorvalorjovem = max(lista_jovem)
            print("Primeira faixa é : ",maiorvalorjovem)
        except ValueError:
            print("Não houve alunos digitados na primeira faixa.")

        try:
            maiorvaloradulto = max(lista_adulto)
            print("Segunda faixa é: ",maiorvaloradulto)
        except ValueError:
            print("Não houve alunos digitados na segunda faixa.")

        try:
            maiorvaloridoso = max(lista_idoso)
            print("Terceira faixa é: ",maiorvaloridoso)
        except ValueError:
            print("Não houve alunos digitados na terceira faixa.")
        
        break     

    try:
        num = int(teclado)
    except:
        print("Ops, não houve idade de aluno digitada.")
        continue

    if num <= 25:
        lista_jovem.append(num)
    elif num > 25 and num <= 60:
        lista_adulto.append(num)
    else:
        lista_idoso.append(num)


    

    
    
        

    
    

    

        
        
    
    
    
    
