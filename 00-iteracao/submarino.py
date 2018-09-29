
x = 0
y = 0
z = 0
direcao = "norte"

entrada = input("");

for item in entrada:
    if direcao == "norte" and item == 'R': direcao = "leste";
    elif direcao == "norte" and item == 'L': direcao = "oeste";

    elif direcao == "oeste" and item == 'R': direcao = "norte";
    elif direcao == "oeste" and item == 'L': direcao = "sul";

    elif direcao == "sul" and item == 'R': direcao = "oeste";
    elif direcao == "sul" and item == 'L': direcao = "leste";

    elif direcao == "leste" and item == 'R': direcao = "sul";
    elif direcao == "leste" and item == 'L': direcao = "norte";

    if item == 'M':
        if direcao == "leste": x = x+1;
        elif direcao == "oeste": x = x-1;
        elif direcao == "norte": y = y+1;
        elif direcao == "sul": y = y-1;

    if item == "U": z = z+1;
    if item == "D": z = z-1;

print(x,y,z,direcao)