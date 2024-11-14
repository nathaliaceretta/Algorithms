import java.util.HashSet;
import java.util.Set;

public class salao2 {

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
        System.out.println(salao(b, c, board, solutions, true)); // Começa com 'b'
        long tempoFinal = System.currentTimeMillis();
        long tempoTotal = tempoFinal - tempoInicial;
        System.out.println("Tempo total de execução: " + tempoTotal + " milissegundos");

    }

    private static int salao(int b, int c, char[][] map, Set<String> solutions, boolean placeB) {
        if (b == 0 && c == 0) {
            if (checaTabuleiro(map)) {
                solutions.add(boardToString(map));
            }
            return solutions.size();
        }

        for (int i = 0; i < map.length; i++) {
            for (int j = 0; j < map.length; j++) {
                if (map[i][j] == '_') {
                    if (placeB && b > 0 && isValid(i, j, map, 'b', 'c')) {
                        map[i][j] = 'b';
                        salao(b - 1, c, map, solutions, false); // Alterna para 'c'
                        map[i][j] = '_';
                    } else if (!placeB && c > 0 && isValid(i, j, map, 'c', 'b')) {
                        map[i][j] = 'c';
                        salao(b, c - 1, map, solutions, true); // Alterna para 'b'
                        map[i][j] = '_';
                    }
                }
            }
        }

        return solutions.size();
    }

    private static boolean isValid(int l, int c, char[][] map, char pistoleiro, char enemy) {
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
                    break;
                }
            }
        }
        return true;
    }

    private static boolean checaTabuleiro(char[][] map) {
        for (int i = 0; i < map.length; i++) {
            for (int j = 0; j < map.length; j++) {
                if (map[i][j] == 'b' || map[i][j] == 'c') {
                    if (!contaInimigos(i, j, map, map[i][j])) {
                        return false;
                    }
                }
            }
        }
        return true;
    }

    private static boolean contaInimigos(int l, int c, char[][] map, char pistoleiro) {
        char enemy = pistoleiro == 'b' ? 'c' : 'b';
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
                if (map[newRow][newCol] == enemy) {
                    enemySeen++;
                    break;
                }
                if (map[newRow][newCol] == pistoleiro) {
                    break;
                }
            }
        }

        return enemySeen >= 2;
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
