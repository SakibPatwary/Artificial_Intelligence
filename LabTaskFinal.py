colors = ['Red', 'Blue', 'Green']

states = ['WA', 'Q', 'T', 'V', 'SA', 'NT', 'NSW']

neighbors = {}
neighbors['WA'] = ['SA', 'NT']
neighbors['Q'] = ['SA', 'NT', 'NSW']
neighbors['T'] = []
neighbors['V'] = ['SA', 'NSW']
neighbors['SA'] = ['WA', 'NT', 'Q', 'NSW', 'V']
neighbors['NT'] = ['Q', 'WA', 'SA']
neighbors['NSW'] = ['Q', 'V', 'SA']

colors_of_states = {}

def promising(state, color):
    for neighbor in neighbors.get(state): 
        color_of_neighbor = colors_of_states.get(neighbor)
        if color_of_neighbor == color:
            return False

    return True

def get_color_for_state(state):
    for color in colors:
        if promising(state, color):
            return color

def main():
    for state in states:
        colors_of_states[state] = get_color_for_state(state)

    print (colors_of_states)


main()
