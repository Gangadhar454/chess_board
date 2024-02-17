from rest_framework.views import APIView
from rest_framework.response import Response
from .chess_moves import ChessBoard
from .serializers import PositionsSerializer

class ChessBoardView(APIView):
    def validate_slug(self, slug):
        if slug not in ['knight', 'rook', 'queen', 'bishop']:
            return False
        return True
    def post(self, request, slug):

        positions = request.data.get('positions', None)
        if not positions:
            return Response({
                "message": "please send positions"
            })
        serializer = PositionsSerializer(data=positions)
        if not serializer.is_valid():
            return Response({
                "status": False,
                "message": serializer.errors
                },
                status=200
            )
        is_valid_slug = self.validate_slug(slug)
        if not is_valid_slug:
            return Response({
                "status": False,
                "message": "Invalid slug in URL"
                },
                status=200
            )
        
        chess_board = ChessBoard(positions, slug)
        valid_moves_of_slug = chess_board.valid_moves()

        return Response({
            "valid_moves":valid_moves_of_slug
        })