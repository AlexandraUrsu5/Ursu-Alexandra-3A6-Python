def Compose(notes_initial, moves, start_position):
    notes=notes_initial[start_position:len(notes_initial)]
    notes=notes+notes_initial[0:start_position]
    #print(notes)
    song = []
    for move in moves:
        song.append(notes[move-1])
    print(song)
    
def main():
    notes = ["do", "re", "mi", "fa", "sol"]
    moves = [1, -3, 4, 2]
    start_pos = 2

    Compose(notes, moves, start_pos)
    
main()