# Etapa 1: Classe Livro
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True # Por padrão o livro começa disponível

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return f'O livro "{self.titulo}" foi emprestado com sucesso.'
        else:
            return f'O livro "{self.titulo}" não está disponível para empréstimo.'

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            return f'O livro "{self.titulo}" foi devolvido com sucesso.'
        else:
            return f'O livro "{self.titulo}" já está disponível.'


# Etapa 2: Classe Biblioteca
class Biblioteca:
    def __init__(self):
        self.livros = [] # lista vazia inicialmente

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f'Livro "{livro.titulo}" adicionado à biblioteca.')

    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro cadastrado na biblioteca.")
        else:
            for livro in self.livros:
                status = "Disponível" if livro.disponivel else "Indisponível"
                print(f'Título: {livro.titulo}, Autor: {livro.autor}, '
                      f'Ano: {livro.ano_publicacao}, Status: {status}')

    def buscar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                return livro
        return None


# -----------------------------
# Testando o sistema
# -----------------------------
if __name__ == "__main__":
    # Criar biblioteca
    biblioteca = Biblioteca()

    # Criar pelo menos 3 livros
    livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
    livro2 = Livro("O Hobbit", "J.R.R. Tolkien", 1937)
    livro3 = Livro("1984", "George Orwell", 1949)

    # Adicionar livros à biblioteca
    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)
    biblioteca.adicionar_livro(livro3)

    print("\n--- Lista de livros ---")
    biblioteca.listar_livros()

    # Realizar empréstimo
    print("\n--- Empréstimo ---")
    print(livro3.emprestar())

    print("\n--- Lista após empréstimo ---")
    biblioteca.listar_livros()

    # Devolver livro
    print("\n--- Devolução ---")
    print(livro3.devolver())

    print("\n--- Lista após devolução ---")
    biblioteca.listar_livros()

    # Buscar livro pelo título
    print("\n--- Buscar Livro ---")
    titulo = "1984"
    encontrado = biblioteca.buscar_livro(titulo)
    if encontrado:
        print(f'Livro encontrado: {encontrado.titulo}, Autor: {encontrado.autor}')
    else:
        print(f'Livro "{titulo}" não encontrado.')