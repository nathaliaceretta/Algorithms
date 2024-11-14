import java.util.HashSet;
import java.util.Set;

public class salao {

    public static void main(String[] args) {

        long tempoInicial = System.currentTimeMillis();

        int mapSize = Integer.parseInt(args[0]);
        int b = Integer.parseInt(args[1]);
        int c = Integer.parseInt(args[2]);

        char[][] board = new char[mapSize][mapSize];
        for (int i = 0; i < mapSize; i++) {
            for (int j = 0; j < mapSize; j++) {
                board[i][j] = '_';
            }
        }

        Set<String> solutions = new HashSet<>();
        System.out.println(salao(b, c, board, solutions));
        long tempoFinal = System.currentTimeMillis();
        long tempoTotal = tempoFinal - tempoInicial;
        System.out.println("Tempo total de execução: " + tempoTotal + " milissegundos");

    }

    private static int salao(int b, int c, char[][] map, Set<String> solutions) {
        if (b == 0 && c == 0) {
            if (checaTabuleiro(map)) {
                // Add the current board state to solutions
                solutions.add(boardToString(map));
            }
            return solutions.size();
        }

        // Add b shooters
        for (int i = 0; i < map.length; i++) {
            for (int j = 0; j < map.length; j++) {
                if (b > 0 && notContiguous(i, j, map)) {
                    b--;
                    map[i][j] = 'b';
                    salao(b, c, map, solutions);
                    b++;
                    map[i][j] = '_';
                }
            }
        }

        // Add c shooters
        for (int i = 0; i < map.length; i++) {
            for (int j = 0; j < map.length; j++) {
                if (isValid(i, j, map, 'c', 'b') && c > 0) {
                    c--;
                    map[i][j] = 'c';
                    salao(b, c, map, solutions);
                    c++;
                    map[i][j] = '_';
                }
            }
        }

        return solutions.size();
    }

    private static boolean notContiguous(int l, int c, char[][] map) {
        int[][] directions = {
                { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 },
                { -1, -1 }, { -1, 1 }, { 1, -1 }, { 1, 1 }
        };

        for (int[] dir : directions) {
            int newRow = l + dir[0];
            int newCol = c + dir[1];
            if (newRow >= 0 && newRow < map.length && newCol >= 0 && newCol < map.length) {
                if (map[newRow][newCol] == 'b') {
                    return false;
                }
            }
        }
        return true;
    }

    private static boolean isValid(int l, int c, char[][] map, char pistoleiro, char enemy) {
        int enemySeen = 0;
        int[][] directions = {
                { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 },
                { -1, -1 }, { -1, 1 }, { 1, -1 }, { 1, 1 }
        };

        for (int[] dir : directions) {
            for (int step = 1; step < map.length; step++) {
                int newRow = l + dir[0] * step;
                int newCol = c + dir[1] * step;

                if (newRow < 0 || newRow >= map.length || newCol < 0 || newCol >= map.length) {
                    break;
                }
                if (map[newRow][newCol] == pistoleiro) {
                    return false;
                }
                if (map[newRow][newCol] == enemy) {
                    enemySeen++;
                    break;
                }
            }
        }
        return enemySeen >= 2;
    }

    private static boolean checaTabuleiro(char[][] map) {
        for (int i = 0; i < map.length; i++) {
            for (int j = 0; j < map.length; j++) {
                if (map[i][j] == 'b') {
                    if (!isValid(i, j, map, 'b', 'c')) {
                        return false;
                    }
                }
            }
        }
        return true;
    }

    private static String boardToString(char[][] map) {
        StringBuilder sb = new StringBuilder();
        for (char[] row : map) {
            for (char cell : row) {
                sb.append(cell);
            }
            sb.append('\n');
        }
        return sb.toString();
    }
}
