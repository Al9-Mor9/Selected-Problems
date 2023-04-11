import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class JUN16236_P {
	static int N, size = 2, ans = 0, ate = 0;
	static int space[][];
	static int shark[];
	static int d[][] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		space = new int[N][N];
		
		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				space[i][j] = Integer.parseInt(st.nextToken());
				if (space[i][j] == 9) {
					shark = new int[] {i, j};
				}
			}
		}
		while (find()) {
			
		};
		System.out.println(ans);
	}
	
	static boolean find() {

		int fish[] = {-1, -1};
		int distance[][] = new int[N][N];
		int minDist = Integer.MAX_VALUE;
		
		for (int i = 0; i < N; i++) Arrays.fill(distance[i], Integer.MAX_VALUE);
		
		Queue<int[]> q = new ArrayDeque<>();
		q.offer(shark);
		distance[shark[0]][shark[1]] = 0;
		while (!q.isEmpty()) {
			int []front = q.poll();
			int x = front[0];
			int y = front[1];
			
			for (int i = 0; i < 4; i++) {
				int nx = x + d[i][0];
				int ny = y + d[i][1];
				if (nx < 0 || ny < 0 || nx >= N || ny >= N) continue;
				if (distance[nx][ny] != Integer.MAX_VALUE) continue;
				if (space[nx][ny] > size) continue;
				
				q.offer(new int[] {nx, ny});
				distance[nx][ny] = distance[x][y] + 1;
				if (space[nx][ny] != 0 && space[nx][ny] < size) {
					if (fish[0] < 0) {
						minDist = distance[nx][ny];
						fish[0] = nx;
						fish[1] = ny;
					}
					else if (distance[nx][ny] == minDist) {
						if (nx < fish[0]) {
							fish[0] = nx;
							fish[1] = ny;
						}
						else if (nx == fish[0] && ny < fish[1]) {
							fish[0] = nx;
							fish[1] = ny;
						}
					}
					else break;
				}				
			}
		}
		
		if (fish[0] < 0) return false;
		space[shark[0]][shark[1]] = 0;
		space[fish[0]][fish[1]] = 0;
		shark = fish;
		ate++;
		if (ate == size) {
			size++;
			ate = 0;
		}
		ans += distance[fish[0]][fish[1]];
		return true;
	}
}
