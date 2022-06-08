#inicianod as variáveis
contagemId = 0
contagemId1=0
contagemId2 = 0
itenAtualizar=0
itenAtualizar1=0
itenAtualizar2 = 0
opcao = 0
iten = 0
iten1 = 0
iten2 = 0


#iniciando o dicionário
cadastroC = [{'CLIENTE': 'Jeferson Cristo', 'CPF': '179.297.807-32', 'END.': 'Doutor Leal', 'TELEFONE':'(21)987131977', 'EMAIL PARA CONTATO': 'meirellesisabella@gmail.com'}]
cadastroM = [{'MARCA': 'Yamaha', 'MODEL0': 'xtz', 'ANO':'2021', 'COR': 'Azul', 'QTD': '2'}]
cadastroV = [{'COMPRADOR': 'Kevin', 'VENDEDOR': 'Isabela', 'MARCA':'HONDA', 'MODELO':'PCX', 'VALOR':'HONDA' }]



while opcao != 'D':
    print('''
                      MENU:

                      [A]- Clientes
                      [B]- Motocicleta
                      [C]- Efetuar Venda
                      [D]- Sair''')
    opcao = str(input('Escolha uma Opção:'))

#=====================================================================================================================================================    
    if opcao == 'A' or opcao == 'a':
        while iten != 5:
            print('''
                      OPÇÕES:

                      [1]- Cadastrar Cliente
                      [2]- Consultar Cadastros
                      [3]- atualizar Cadastro
                      [4]- apagar Cadastro
                      [5]- Sair ''')
            iten = int(input('Escolha uma Opção:'))
            if iten == 1:

                nome=input("Nome:")
                cpf=input("CPF:")
                endereco=input("END.:")
                telefone = input("TELEFONE:")
                email= input("EMAIL PARA CONTATO:")
                cadastroC.append({'CLIENTE': nome, 'CPF': cpf, 'END': endereco, 'TELEFONE': telefone, 'EMAIL PARA CONTATO': email})
                #print(cadastroC)

            if iten ==2:
                
                for c in cadastroC:
                    contagemId += 1
                    print("id:", contagemId ,c)
                
                contagemId = 0

            if iten ==3:
    
                while itenAtualizar != 6:
                   
                    
                    print('''
                      OPÇÕES:

                      [1]- Atualizar NOME
                      [2]- Atualizar CPF
                      [3]- Atualizar ENDEREÇO
                      [4]- Atualizar TELEFONE
                      [5]- Atualizar EMAIL
                      [6]- Voltar ''')
                    itenAtualizar = int(input('Escolha uma Opção:'))
                    if itenAtualizar == 1:
                        
                        id=int(input("Id do usuario:"))
                        id = id - 1
                        valor=input("NOME: ")       
                        cadastroC[id].update({"CLIENTE":valor})
                        
                    if itenAtualizar == 2:
                        id=int(input("Id do usuario:"))
                        id = id - 1
                        valor=input("CPF: ")       
                        cadastroC[id].update({"CPF":valor})
                        
                    if itenAtualizar == 3:
                        id=int(input("Id do usuario:"))
                        id = id - 1
                        valor=input("END: ")       
                        cadastroC[id].update({"END.":valor})

                    if itenAtualizar == 4:
                        id=int(input("Id do usuario:"))
                        id = id - 1
                        valor=input("TELEFONE: ")       
                        cadastroC[id].update({"TELEFONE":valor})

                    if itenAtualizar == 5:
                        id=int(input("Id do usuario:"))
                        id = id - 1
                        valor=input("EMAIL PARA CONTATO: ")       
                        cadastroC[id].update({"EMAIL PARA CONTATO":valor})
            
            if iten ==4:
    

                id=int(input("Id do usuario:"))
                id = id - 1
                print("O cadastro do cliente", cadastroC[id].get('CLIENTE'), "irá ser apagado")
                apagar=input("Digite sim[s] para apagar: ")
                if (apagar=="s"):
                    del cadastroC[id]
                
                    
#===============================================================================================================================
             
    if opcao == 'B' or opcao =='b':
        while iten1 != 5:
            print('''
                      OPÇÕES:

                      [1]- Cadastrar Motocicleta
                      [2]- Consultar Cadastros
                      [3]- atualizar Cadastro
                      [4]- apagar Cadastro
                      [5]- Sair ''')
            iten1 = int(input('Escolha uma Opção:'))
            if iten1 == 1:

                marca=input("MARCA:")
                modelo=input("MODELO:")
                ano=input("ANO:")
                cor = input("COR:")
                quantidade= input("QTD:")
                cadastroM.append({'MARCA': marca, 'MODELO': modelo, 'ANO': ano, 'COR': cor, 'QTD':quantidade})
                #print(cadastroC)

            if iten1 ==2:
                for d in cadastroM:
                    contagemId1 += 1
                    print("id:", contagemId1 ,d)
                
                contagemId1 = 0

            if iten1 ==3:
                
                while itenAtualizar1 != 6:
                    print('''
                      OPÇÕES:

                      [1]- Atualizar MARCA
                      [2]- Atualizar MODELO
                      [3]- Atualizar ANO
                      [4]- Atualizar COR
                      [5]- Atualizar QUANTIDADE
                      [6]- Voltar ''')
                    itenAtualizar1 = int(input('Escolha uma Opção:'))
                    if itenAtualizar1 == 1:
                        
                        id=int(input("Id do usuario:"))
                        id = id - 1
                        valor=input("MARCA: ")       
                        cadastroM[id].update({"MARCA":valor})
                        
                    if itenAtualizar1 == 2:
                        id=int(input("Id do usuario:"))
                        id = id - 1
                        valor=input("MODELO: ")       
                        cadastroM[id].update({"MODELO":valor})
                        
                    if itenAtualizar1 == 3:
                        id=int(input("Id do usuario:"))
                        id = id - 1
                        valor=input("ANO: ")       
                        cadastroM[id].update({"ANO":valor})

                    if itenAtualizar1 == 4:
                        id=int(input("Id do usuario:"))
                        id = id - 1
                        valor=input("COR: ")       
                        cadastroM[id].update({"COR":valor})

                    if itenAtualizar1 == 5:
                        id=int(input("Id do usuario:"))
                        id = id - 1
                        valor=input("QUANTIDADE: ")       
                        cadastroM[id].update({"QTD":valor})
            
            if iten1 ==4:
    

                id=int(input("Id do usuario:"))
                id = id - 1
                print("O cadastro do cliente", cadastroM[id].get('MODELO'), "irá ser apagado")
                apagar=input("Digite sim[s] para apagar: ")
                if (apagar=="s"):
                    del cadastroM[id]
                
#======================================================================================================================

    if opcao == 'C' or opcao == 'c':
        while iten2 != 5:
            print('''
                      OPÇÕES:

                      [1]- Cadastrar Venda
                      [2]- Consultar Cadastros
                      [3]- atualizar Cadastro
                      [4]- apagar Cadastro
                      [5]- Sair ''')
            iten2 = int(input('Escolha uma Opção:'))
            if iten2 == 1:

                comprador=input("COMPRADOR:")
                vendedor=input("VENDEDOR:")
                marca=input("MARCA:")
                modelo = input("MODELO:")
                valor= input("VALOR:")
                cadastroV.append({'COMPRADOR': comprador, 'VENDEDOR': vendedor, 'MARCA': marca, 'MODELO': modelo, 'VALOR': valor})
               

            if iten2 ==2:
                
                for e in cadastroV:
                    contagemId2 += 1
                    print("id:", contagemId2 ,e)
                
                contagemId2 = 0

            if iten2 ==3:
                
                while itenAtualizar2 != 6:
                   
                    
                    print('''
                      OPÇÕES:

                      [1]- Atualizar COMPRADOR
                      [2]- Atualizar VENDEDOR
                      [3]- Atualizar MARCA
                      [4]- Atualizar MODELO
                      [5]- Atualizar VALOR
                      [6]- Voltar ''')
                    itenAtualizar2 = int(input('Escolha uma Opção:'))
                    if itenAtualizar2 == 1:
                        id=int(input("Id do usuario:"))
                        id = id - 1
                        valor=input("COMPRADOR: ")       
                        cadastroV[id].update({"COMPRADOR":valor})
                            
                    if itenAtualizar2 == 2:
                        id=int(input("Id do usuario:"))
                        id = id - 1
                        valor=input("VENDEDOR: ")       
                        cadastroV[id].update({"VENDEDOR":valor})
                        
                    if itenAtualizar2 == 3:
                        id=int(input("Id do usuario:"))
                        id = id - 1
                        valor=input("MARCA: ")       
                        cadastroV[id].update({"MARCA":valor})

                    if itenAtualizar2 == 4:
                        id=int(input("Id do usuario:"))
                        id = id - 1
                        valor=input("MODELO: ")       
                        cadastroV[id].update({"MODELO":valor})

                    if itenAtualizar2 == 5:
                        id=int(input("Id do usuario:"))
                        id = id - 1
                        valor=input("VALOR: ")       
                        cadastroV[id].update({"VALOR":valor})
                        
                        
                    
            
            if iten2 ==4:
                id=int(input("Id do usuario:"))
                id = id - 1
                print("O cadastro do cliente", cadastroV[id].get('COMPRADOR'), "irá ser apagado")
                apagar=input("Digite sim[s] para apagar: ")
                if (apagar=="s"):
                    del cadastroV[id]


    if opcao == 'D':
        print('fim')
        
        
               
       
       

        
            

        
