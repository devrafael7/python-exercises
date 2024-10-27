class UndoRedo:
    def __init__(self):
        self.undo_stack = []  
        self.redo_stack = []  

    def do_action(self, action):
        self.undo_stack.append(action) 
        self.redo_stack.clear() 

    def undo(self):
        if self.undo_stack:
            action = self.undo_stack.pop() 
            self.redo_stack.append(action)  
            return action
        return None

    def redo(self):
        if self.redo_stack:
            action = self.redo_stack.pop()
            self.undo_stack.append(action)  
            return action
        return None

def main():
    editor = UndoRedo()
    current_name = None  

    while True:
        name = input("Digite seu nome: ")
        editor.do_action(name)
        current_name = name 
        print(f"Seu nome é: {current_name}")

        while True:
            choice = input("Deseja desfazer (d), refazer (r) ou sair (s)? ").lower()
            if choice == 'd':
                undone = editor.undo()
                if undone:
                    current_name = undone  
                    print(f"Ação desfeita. Último nome: {current_name}")
                else:
                    print("Nada para desfazer.")
            elif choice == 'r':
                redone = editor.redo()
                if redone:
                    current_name = redone  
                    print(f"Ação refeita. Nome: {current_name}")
                else:
                    print("Nada para refazer.")
            elif choice == 's':
                print(f"Nome final: {current_name}")  
                print("Saindo do programa.")
                return
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
