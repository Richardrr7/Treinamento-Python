import json


class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def mostrar_produto(self):
        print(f"Produto: {self.nome} --- Preço: {self.preco} --- Quantidade: {self.quantidade}")

    def para_dict(self):
        return {"nome":self.nome, "preco":self.preco, "quantidade":self.quantidade}


class Estoque:
    def __init__(self):
        self.lista_estoque = []

    def carregar_estoque(self):
    
        try:
            with open("estoque.json", "r") as arquivo:
                produtos = json.load(arquivo)
                self.lista_estoque = [Produto(p["nome"], p["preco"], p["quantidade"]) for p in produtos]
        except (FileNotFoundError, json.JSONDecodeError):
            self.lista_estoque = []


    def adicionar_lista_json(self):
        estoque = [
            Produto("Camisa", 100.00, 50),
            Produto("Tenis", 200.00, 20),
            Produto("Blusa", 150.00, 40)
        ]

        self.lista_estoque.extend(estoque)
        
        with open("estoque.json","w") as arquivo:
            json.dump([produto.para_dict() for produto in self.lista_estoque], arquivo, indent=4)
            print("Produto salvo em estoque.json!")

    def carregar_estoque(self):
        try:
            with open("estoque.json", "r") as arquivo:
                produtos = json.load(arquivo)
                self.lista_estoque = [Produto(p["nome"], p["preco"], p["quantidade"]) for p in produtos]
        except (FileNotFoundError, json.JSONDecodeError):
            self.lista_estoque = []


    def adicionar_estoque(self):
        try:
            produto = input("\nProduto: ")
            for item in self.lista_estoque:
                if item.nome.lower() == produto.lower():
                    print("\nEsse item já foi adicionado!!")
                    return
                    
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))

            novo_produto = Produto(produto, preco, quantidade)
            self.lista_estoque.append(novo_produto)

            with open("estoque.json","w") as arquivo:
                json.dump([produto.para_dict() for produto in self.lista_estoque], arquivo, indent=4)
                
            print("\nProduto adicionado com sucesso!!")

        except ValueError:
            print("\nCaracter inválid!")
            return
    
    def alterar_produto(self):
        try:
            item_alterar = input("Digite o item que deseja alterar: ")
            modo = int(input("(1-Entrada) / (2-Saída)"))

        except ValueError:
            print("\nCaractére inválido!")
            return

        if modo == 1:
            for item in self.lista_estoque:
                if item.nome.lower() == item_alterar.lower():
                    item_quantidade = int(input("Quantidade: "))
                    item.quantidade += item_quantidade
                    print("\nAlteração feita com sucesso!")

                    with open("estoque.json", "w") as arquivo:
                        json.dump([produto.para_dict() for produto in self.lista_estoque], arquivo, indent=4)
                    return
            print("\nEste item não foi encontrado no estoque!")
            return

        elif modo == 2:
            for item in self.lista_estoque:
                if item.nome.lower() == item_alterar.lower():
                    item_quantidade = int(input("Quantidade: "))
                    item.quantidade -= item_quantidade
                    print("\nAlteração feita com sucesso!!")

                    with open("estoque.json", "w") as arquivo:
                        json.dump([produto.para_dict() for produto in self.lista_estoque], arquivo, indent=4)
                    return
            print("\nEste item não foi encontrado no estoque!!")
            return
    
    def remover_produto(self):
        item_remover = input("Digite o item que deseja remover do estoque: ")
        for item in self.lista_estoque:
            if item.nome.lower() == item_remover.lower():
                self.lista_estoque.remove(item)

                with open("estoque.json", "w") as arquivo:
                    json.dump([produto.para_dict() for produto in self.lista_estoque], arquivo, indent=4)

                print(f"\n{item_remover} foi removido do estoque.")
                return
        print("\nEsse item não foi encontrado no estoque.")

    def exibir_estoque(self):
        try:
            # Abrindo o arquivo JSON para leitura
            with open("estoque.json", "r") as arquivo:
                estoque_carregado = json.load(arquivo)

            print("\n--------- ESTOQUE ATUAL ---------")
            for item in estoque_carregado:
                print(f"Produto: {item['nome']} --- Preço: R${item['preco']} --- Quantidade: {item['quantidade']}")

        except FileNotFoundError:
            print("\nArquivo 'estoque.json' não encontrado!")
        except json.JSONDecodeError:
            print("\nErro ao carregar o JSON! Verifique o arquivo.")

    def calcular_estoque(self):
        self.carregar_estoque()
        total = sum(item.preco * item.quantidade for item in self.lista_estoque)
        
        print(f"\nTotal Estoque: R${total:.2f}")


print("---------GERENCIAMENTO DE ESTOQUE---------")


estoque = Estoque()
estoque.carregar_estoque()

while True:
    print("\n1 - ADICIONAR PRODUTO AO ESTOQUE.")
    print("2 - REMOVER PRODUTO DO ESTOQUE.")
    print("3 - ALTERAR PRODUTO EM ESTOQUE.")
    print("4 - EXIBIR ESTOQUE.")
    print("5 - CALCULAR VALOR TOTAL DO ESTOQUE.")
    print("6 - SAIR DO SISTEMA.")
    opcao = int(input("\nOpção: "))

    try:
        if opcao == 1:
            estoque.adicionar_estoque()

        elif opcao == 2:
            estoque.remover_produto()
    
        elif opcao == 3:
            estoque.alterar_produto()
    
        elif opcao == 4:
            estoque.exibir_estoque()
    
        elif opcao == 5:
            estoque.calcular_estoque()
    
        elif opcao == 6:
            print("\nSaindo do sistema de gerenciamento de estoque!")
            break
    
    except ValueError:
        print("\nCaractére inválida. Digite um número válido!")
        continue