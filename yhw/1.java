class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        int wMax = 0;
		int hMax = 0;
		for (int i = 0; i < sizes.length; i++) {
			if(sizes[i][0] > sizes[i][1]) {
				wMax = Math.max(sizes[i][0],wMax);
				hMax = Math.max(sizes[i][1],hMax);
			}
			else {
				wMax = Math.max(sizes[i][1],wMax);
				hMax = Math.max(sizes[i][0],hMax);
			}
		}
		answer = wMax * hMax;
        return answer;
    }
}