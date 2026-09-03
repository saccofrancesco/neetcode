class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def build(row: int, col: int, size: int) -> 'Node':
            # Una singola cella è sempre uniforme
            if size == 1:
                return Node(
                    bool(grid[row][col]),
                    True,
                    None,
                    None,
                    None,
                    None
                )

            half = size // 2

            topLeft = build(row, col, half)
            topRight = build(row, col + half, half)
            bottomLeft = build(row + half, col, half)
            bottomRight = build(row + half, col + half, half)

            # Se i 4 quadranti sono foglie e hanno lo stesso valore,
            # possiamo comprimerli in una singola foglia.
            children = [topLeft, topRight, bottomLeft, bottomRight]

            if (
                all(child.isLeaf for child in children)
                and len({child.val for child in children}) == 1
            ):
                return Node(
                    topLeft.val,
                    True,
                    None,
                    None,
                    None,
                    None
                )

            # Altrimenti serve un nodo interno
            return Node(
                True,       # val può essere qualsiasi valore se isLeaf=False
                False,
                topLeft,
                topRight,
                bottomLeft,
                bottomRight
            )

        return build(0, 0, len(grid))