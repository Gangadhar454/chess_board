from enum import Enum


class Pieces(Enum):
    KNIGHT = 'knight'
    ROOK = 'rook'
    QUEEN = 'queen'
    BISHOP = 'bishop'

    def __str__(self):
        return self.value

class ChessBoard:

    def __init__(self, positions, slug: str):
        self.slug = slug
        self.positions_in_cordinates = self.get_numberical_coridates(positions)
        self.all_cordinates = [value for value in self.positions_in_cordinates.values()]
        self.slug_cordinates = self.positions_in_cordinates[slug.capitalize()]

    def parse_position(self, position):
        column = ord(position[0].upper()) - ord('A') + 1
        row = int(position[1])
        return column, row

    def reverse_parse_position(self, coordinates):
            column = chr(coordinates[0] + ord('A') - 1)
            row = str(coordinates[1])
            return f"{column}{row}"

    def get_numberical_coridates(self, positions):
        numerical_cordinates = {}
        for key, value in positions.items():
            numerical_cordinates[key] = self.parse_position(value)
        return numerical_cordinates

    def possible_moves_of_knight(self):
        knight_cordinates = self.positions_in_cordinates['Knight']
        all_possible_moves_of_knight = []
        x_cordinate = knight_cordinates[0]
        y_cordinate = knight_cordinates[1]
        # vertical moves
        top_left = (x_cordinate-1, y_cordinate+2)
        if (top_left[0]>=1 and top_left[1]<=8):
            all_possible_moves_of_knight.append(top_left)
        top_right = (x_cordinate+1, y_cordinate+2)
        if (top_right[0]<=8 and top_right[1]<=8):
            all_possible_moves_of_knight.append(top_right)
        bottom_left = (x_cordinate-1, y_cordinate-2)
        if (bottom_left[0]>=1 and bottom_left[1]>=1):
            all_possible_moves_of_knight.append(bottom_left)
        bottom_right = (x_cordinate+1, y_cordinate-2)
        if (bottom_right[0]<=8 and bottom_right[1]>=1):
            all_possible_moves_of_knight.append(bottom_right)

        # horizontal moves
        right_top = (x_cordinate+2, y_cordinate+1)
        if (right_top[0]<=8 and right_top[1]<=8):
            all_possible_moves_of_knight.append(right_top)
        right_bottom = (x_cordinate+2, y_cordinate-1)
        if (right_bottom[0]<=8 and right_bottom[1]>=1):
            all_possible_moves_of_knight.append(right_bottom)
        left_top = (x_cordinate-2, y_cordinate+1)
        if (left_top[0]>=1 and left_top[1]<=8):
            all_possible_moves_of_knight.append(left_top)
        left_bottom = (x_cordinate-2, y_cordinate-1)
        if (left_bottom[0]>=1 and left_bottom[1]>=1):
            all_possible_moves_of_knight.append(left_bottom)
        return all_possible_moves_of_knight

    def all_posibble_top_moves(self, current_cordinates):
        if (current_cordinates[1] == 8):
            return []
        x = current_cordinates[0]
        y = current_cordinates[1] + 1
        posibble_top_moves = []
        while y <= 8:
            posibble_top_moves.append((x,y))
            if (
                (x,y)!= self.slug_cordinates
                and (x,y) in self.all_cordinates
            ):
                break
            y+=1
        return posibble_top_moves

    def all_posibble_bottom_moves(self, current_cordinates):
        if (current_cordinates[1] == 1):
            return []
        x = current_cordinates[0]
        y = current_cordinates[1] - 1
        posibble_bottom_moves = []
        while y >= 1:
            posibble_bottom_moves.append((x,y))
            if (
                (x,y)!= self.slug_cordinates
                and (x,y) in self.all_cordinates
            ):
                break
            y-=1
        return posibble_bottom_moves

    def all_possible_right_moves(self, current_cordinates):
        if (current_cordinates[0] == 8):
            return []
        x = current_cordinates[0] + 1
        y = current_cordinates[1]
        possbile_right_moves = []
        while x<=8:
            possbile_right_moves.append((x,y))
            if (
                (x,y)!= self.slug_cordinates
                and (x,y) in self.all_cordinates
            ):
                break
            x+=1
        return possbile_right_moves

    def all_possible_left_moves(self, current_cordinates):
        if (current_cordinates[0] == 1):
            return []
        x = current_cordinates[0] -1
        y = current_cordinates[1]
        possbile_left_moves = []
        while x>=1:
            possbile_left_moves.append((x,y))
            if (
                (x,y)!= self.slug_cordinates
                and (x,y) in self.all_cordinates
            ):
                break
            x-=1
        return possbile_left_moves

    def all_possible_top_right_diagnol_moves(self, current_cordinates):
        if (current_cordinates[0] == 8 or current_cordinates[1] == 8):
            return []
        x = current_cordinates[0] + 1
        y = current_cordinates[1] + 1
        possible_top_right_diagnol_moves = []
        while (x<=8 and y<=8):
            possible_top_right_diagnol_moves.append((x,y))
            if (
                (x,y)!= self.slug_cordinates
                and (x,y) in self.all_cordinates
            ):
                break
            x+=1
            y+=1
        return possible_top_right_diagnol_moves

    def all_possible_top_left_diagnol_moves(self, current_cordinates):
        if (current_cordinates[0] == 1 or current_cordinates[1] == 8):
            return []
        x = current_cordinates[0] - 1
        y = current_cordinates[1] + 1
        possible_top_left_diagnol_moves = []
        while (x>=1 and y<=8):
            possible_top_left_diagnol_moves.append((x,y))
            if (
                (x,y)!= self.slug_cordinates
                and (x,y) in self.all_cordinates
            ):
                break
            x-=1
            y+=1
        return possible_top_left_diagnol_moves

    def all_possible_bottom_left_diagnol_moves(self, current_cordinates):
        if (current_cordinates[0] == 1 or current_cordinates[1] == 1):
            return []
        x = current_cordinates[0] - 1
        y = current_cordinates[1] - 1
        possible_top_left_diagnol_moves = []
        while (x>=1 and y>=1):
            possible_top_left_diagnol_moves.append((x,y))
            if (
                (x,y)!= self.slug_cordinates
                and (x,y) in self.all_cordinates
            ):
                break
            x-=1
            y-=1
        return possible_top_left_diagnol_moves

    def all_possible_bottom_right_diagnol_moves(self, current_cordinates):
        if (current_cordinates[0] == 8 or current_cordinates[1] == 1):
            return []
        x = current_cordinates[0] + 1
        y = current_cordinates[1] - 1
        possible_bottom_right_diagnol_moves = []
        while (x<=8 and y>=1):
            possible_bottom_right_diagnol_moves.append((x,y))
            if (
                (x,y) != self.slug_cordinates
                and (x,y) in self.all_cordinates
            ):
                break
            x+=1
            y-=1
        return possible_bottom_right_diagnol_moves

    def all_straight_moves(self, current_cordinates):
        top_moves = self.all_posibble_top_moves(current_cordinates)
        bottom_moves = self.all_posibble_bottom_moves(current_cordinates)
        left_moves = self.all_possible_left_moves(current_cordinates)
        right_moves = self.all_possible_right_moves(current_cordinates)
        return top_moves + bottom_moves + left_moves + right_moves

    def all_diagonal_moves(self, current_cordinates):
        top_right = self.all_possible_top_right_diagnol_moves(current_cordinates)
        top_left = self.all_possible_top_left_diagnol_moves(current_cordinates)
        bottom_right = self.all_possible_bottom_right_diagnol_moves(current_cordinates)
        bottom_left = self.all_possible_bottom_left_diagnol_moves(current_cordinates)
        return top_right + top_left + bottom_right + bottom_left

    def valid_moves(self):

        rook_moves = self.all_straight_moves(self.positions_in_cordinates['Rook'])
        queen_moves = self.all_straight_moves(self.positions_in_cordinates['Queen']) + self.all_diagonal_moves(self.positions_in_cordinates['Queen'])
        bishop_moves = self.all_diagonal_moves(self.positions_in_cordinates['Bishop'])
        knight_moves = self.possible_moves_of_knight()

        valid_moves_in_alphabetical = []
        if self.slug == Pieces.KNIGHT.value:
            valild_moves_of_knight = set(knight_moves) - set(rook_moves+queen_moves+bishop_moves)
            valid_moves_in_alphabetical = [self.reverse_parse_position(cordinate) for cordinate in valild_moves_of_knight ]
        elif self.slug == Pieces.QUEEN.value:
            valid_moves_of_queen = set(queen_moves) - set(rook_moves+bishop_moves+knight_moves)
            valid_moves_in_alphabetical = [self.reverse_parse_position(cordinate) for cordinate in valid_moves_of_queen ]
        elif self.slug == Pieces.ROOK.value:
            valid_moves_of_rook = set(rook_moves) - set(queen_moves+bishop_moves+knight_moves)
            valid_moves_in_alphabetical = [self.reverse_parse_position(cordinate) for cordinate in valid_moves_of_rook ]
        elif self.slug == Pieces.BISHOP.value:
            valid_moves_of_bishop = set(bishop_moves) - set(queen_moves+rook_moves+knight_moves)
            valid_moves_in_alphabetical = [self.reverse_parse_position(cordinate) for cordinate in valid_moves_of_bishop ]

        return valid_moves_in_alphabetical