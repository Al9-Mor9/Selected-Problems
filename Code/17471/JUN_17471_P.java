import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class JUN_17471_P {
	static int N, n;
	static int[] population;
	static int[] parent;
	static int[] size;
	static boolean[][] adj;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		
		adj = new boolean[N + 1][N + 1];
	
		parent = new int[N + 1];
		population = new int[N + 1];
		for (int i = 1; i <= N; i++) parent[i] = i;
			
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 1; i <= N; i++) {
			population[i] = Integer.parseInt(st.nextToken());
		}
		
		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			for (int j = 0; j < n; j++) {
				int next = Integer.parseInt(st.nextToken());
				adj[i][next] = true;
				adj[next][i] = true;
				union(i, next);
			}
		}
		
		int setCnt = 0;
		int root = 0;
		for (int i = 1; i <= N; i++) {
			if (find(i) == i) {
				root = i;
				setCnt++;
			}
		}
		
		int ans = -1;
		if (setCnt == 2) {
			int pop1 = 0, pop2 = 0;
			for (int i = 1; i <= N; i++) {
				if (find(i) == root) pop1 += population[i];
				else pop2 += population[i];
			}
			ans = Math.abs(pop1 - pop2);
		}
		else if (setCnt == 1){
			ans = Integer.MAX_VALUE;
			for (int i = 1; i < (1 << N) - 1; i++) {
				int size1 = 0, size2 = 0;
				int pop1 = 0, pop2 = 0;
				int []set1 = new int[N + 1];
				int []set2 = new int[N + 1];
				
				for (int j = 0; j < N; j++) {
					if ((i & (1 << j)) != 0) {//1인 경우 set1, 0인 경우 set2라고 하자
						set1[size1++] = j + 1;
						pop1 += population[j + 1];
					}
					else {
						set2[size2++] = j + 1;
						pop2 += population[j + 1];
					}
				}
				if (isConnected(set1, size1) && isConnected(set2, size2)) {
					ans = Math.min(ans, Math.abs(pop1 - pop2));
				}
			}
		}
		
		System.out.println(ans);
	}
	
	private static boolean isConnected(int []set, int setSize) {
		Queue<Integer> q = new ArrayDeque<Integer>();
		boolean visited[] = new boolean[N + 1];
		q.add(set[0]);
		int visitedCnt = 0;
		
		while (!q.isEmpty()) {
			int front = q.poll();
			if (visited[front]) continue;
			visitedCnt++;
			visited[front] = true;
			for (int j = 1; j <= N; j++) {
				if (adj[front][j] && !visited[j]) {
					for (int k = 0; k < setSize; k++) {
						if (set[k] == j) {
							q.add(j);
						}
					}
				}
			}
		}
		return visitedCnt == setSize;
	}
	
	private static void union(int a, int b) {
		a = find(a);
		b = find(b);
		if (a == b) return;
		parent[b] = a;
	}
	
	private static int find(int a) {
		if (parent[a] == a) return a;
		return parent[a] = find(parent[a]);
	}
}
