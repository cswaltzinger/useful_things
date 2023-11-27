public class color{
	//text colors
	public static final String[] textColors = {
		"\u001B[0m",//reset 	0
		"\u001B[30m",//black 	1
		"\u001B[31m",//red 		2
		"\u001B[32m",//green 	3
		"\u001B[33m",//yellow 	4
		"\u001B[34m",//blue 	5
		"\u001B[35m",//purple 	6
		"\u001B[36m",//cayan 	7
		"\u001B[37m"//white 	8
	};
	//background colors
	public static final String[] backgrounds={
		"\u001B[40m",//black 	0
		"\u001B[41m",//RED 		1
		"\u001B[42m",//green 	2
		"\u001B[43m",//yellow 	3
		"\u001B[44m",//blue 	4
		"\u001B[45m",//purple 	5
		"\u001B[46m",//cyan 	6
		"\u001B[47m"//white 	7
	};
	public static void main(String[] args) {
		while(!args[0].equals("reset")){
			System.out.print(in());
		}
		System.out.println(backgrounds[0]);
		System.out.println(textColors[3]);
	}
	public static String in(){
		return backgrounds[(int)(Math.random()*backgrounds.length)] + 
		textColors[(int)(Math.random()*textColors.length)] + 
		(Math.random()*100<50 ? 0:1);
	}
}