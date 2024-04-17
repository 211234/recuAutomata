class AFD:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3', 'q4'} 
        self.alphabet = {'a', 'b', 'c'}  
        self.transitions = {
            'q0': {'a': 'q1', 'b': 'q0', 'c': 'q4'},
            'q1': {'a': 'q1', 'b': 'q2', 'c': 'q4'},
            'q2': {'a': 'q1', 'b': 'q3', 'c': 'q4'},
            'q3': {'a': 'q3', 'b': 'q3', 'c': 'q4'},
            'q4': {'a': 'q1', 'b': 'q0', 'c': 'q4'}
        }  
        self.start_state = 'q0' 
        self.accept_states = {'q1', 'q2', 'q3'}
        self.path = []  # Lista para almacenar el camino seguido

    def run(self, input_string):
        current_state = self.start_state
        self.path = [current_state]  # Inicializa la lista de camino
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False, self.path  # Retorna el camino seguido hasta ahora
            if current_state not in self.transitions or symbol not in self.transitions[current_state]:
                return False, self.path  # Retorna el camino seguido hasta ahora
            current_state = self.transitions[current_state][symbol]
            self.path.append(current_state)  # Agrega el estado al camino
        return current_state in self.accept_states, self.path  # Retorna el resultado y el camino seguido

def verificar_cadena(afd, cadena):
    # Verificar si la cadena es aceptada por el AFD
    result, _ = afd.run(cadena)  # Usamos el método run() en lugar de accepts_input()
    if result and (cadena.startswith('ac') or cadena.endswith('ab') or ('ac' in cadena and 'ab' in cadena)):
        print(f"La cadena '{cadena}' es aceptada por el AFD.")
    else:
        print(f"La cadena '{cadena}' no es aceptada por el AFD.")

def main():
    # Crear el AFD
    afd = AFD()

    # Ingresar la cadena a verificar
    cadena = input("Ingrese una cadena: ")

    # Verificar la cadena ingresada
    verificar_cadena(afd, cadena)

if __name__ == "__main__":
    main()
