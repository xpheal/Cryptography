import java.util.*;
import java.io.*;

public class parseHexa{
	public static void main(String args[]) throws FileNotFoundException, UnsupportedEncodingException{
		checkArg(1, args);

		ArrayList<String> file = getFile(args[0]);

		int maxLength = file.get(0).length()/2;
		for(int i = 0; i < file.size(); i++){
			if(file.get(i).length()/2 > maxLength){
				maxLength = file.get(i).length()/2;
			}
		}

		ArrayList<Integer> keys = new ArrayList<Integer>();
		ArrayList<ArrayList<String>> allCipher = new ArrayList<ArrayList<String>>();
		ArrayList<ArrayList<Integer>> keyList = new ArrayList<ArrayList<Integer>>();
		ArrayList<Integer> correctKey = new ArrayList<Integer>();

		for(int i = 0; i < file.size(); i++){
			allCipher.add(linetoHex(file.get(i)));
		}

		

		int temp = 0;
		int ctr = 0;
		for(int k = 0; k < maxLength; k++){
			keyList.add(new ArrayList<Integer>());
			// writer.println("k: " + k + " --------------------");
			for(int i = 0; i < 255; i++){
				ctr = 0;
				for(int j = 0; j < allCipher.size(); j++){
					temp = hextoDec(allCipher.get(j).get(k));
					if(checkValid(temp ^ i)){
						// System.out.println(temp ^ i);
						ctr ++;
					}
					else{
						
					}
				}
				if(ctr == allCipher.size()){
					for(int z = 0; z < allCipher.size(); z++){
						temp = hextoDec(allCipher.get(z).get(k));
						// writer.printf("%4c", (char) temp ^ i);
					}
					keyList.get(k).add(i);
					// writer.println(" i: " + i + " --------------------");
				}
			}
			// writer.println();
		}

		for(int i = 0; i < maxLength; i++){
			if(keyList.get(i).size() == 1){
				correctKey.add(keyList.get(i).get(0));
			}
			else{
				correctKey.add(0);
			}
		}

		

		// for(int i = 0; i < keyList.size(); i++){
		// 	System.out.println(i);
		// 	for(int j = 0; j < keyList.get(i).size(); j++){
		// 		System.out.println(keyList.get(i).get(j));
		// 	}
		// }

		Scanner user = new Scanner(System.in);

		int pos = 0;
		int key = 0;

		System.out.println("User interface to crack cipher, k = key, i = position");
		System.out.println("Set key at position i to the input k, 0 <= k < 256");
		System.out.println("Input i = 1000 to terminate program\n\n");

		while(true){
			for(int i = 0; i < allCipher.size(); i ++){
				for(int j = 0; j < allCipher.get(i).size(); j++){
					temp = hextoDec(allCipher.get(i).get(j));
					System.out.printf("%c", (char) temp ^ correctKey.get(j));
				}
				System.out.println();
			}

			System.out.print("i: ");
			pos = user.nextInt();

			if(pos == 1000){
				break;
			}

			System.out.print("Possible keys: ");
			for(int k = 0; k < keyList.get(pos).size(); k++){
				System.out.printf("%4d", keyList.get(pos).get(k));
			}
			System.out.println();

			System.out.print("k: ");
			key = user.nextInt();

			correctKey.remove(pos);
			correctKey.add(pos, key);			
		}

		PrintWriter writer = new PrintWriter("out1", "UTF-8");
		
		for(int i = 0; i < allCipher.size(); i ++){
			for(int j = 0; j < allCipher.get(i).size(); j++){
				temp = hextoDec(allCipher.get(i).get(j));
				writer.printf("%c", (char) temp ^ correctKey.get(j));
			}
			writer.print("\n");
		}

		writer.println("Key: ");

		for(int i = 0; i < correctKey.size(); i ++){
			writer.printf("%d, ", correctKey.get(i));
		}

		writer.close();
	}

	//check if integer is a valid ASCII char
	public static boolean checkValid(int x){
		if(x >= 65 && x <= 91 || x >= 97 && x <= 123 || x == 32 || x == 46 || x == 44){
			return true;
		}
		else{
			return false;
		}
	}

	//key generator, x = key, length = size of plaintext
	public static String keyGen(String x, int length){
		while(x.length() < length){
			x = x + x;
		}

		return x.substring(0, length);
	}

	//convert binary string to decimal
	public static int bintoDec(String x){
		return Integer.parseInt(x, 2);
	}

	//convert hex string to decimal
	public static int hextoDec(String x){
		return Integer.parseInt(x, 16);
	}

	//convert decimal to binary string
	public static String dectoBin(int x){
		return Integer.toBinaryString(x);
	}

	//read the file and store it in a string
	public static ArrayList<String> getFile(String file){
		BufferedReader br;
		ArrayList<String> temp = new ArrayList<String>();
		String tempStr = "";
		//put file into buffer
		try{
			br = new BufferedReader(new FileReader(file));
		} catch (FileNotFoundException e){
			System.out.println(e);
			return null;
		}

		try{
			while((tempStr = br.readLine()) != null){
				temp.add(tempStr);
			}
			br.close();
		} catch (IOException e){
			System.out.println(e);
			return null;
		}

		return temp;
	}

	//check for correct number of arguments
	public static void checkArg(int num, String args[]){
		if(args.length != num){
			throw new Error("Usage: java parseHexa [filename]");
		}
	}

	//convert a line to an arraylist of hex
	public static ArrayList<String> linetoHex(String line){
		ArrayList<String> arr = new ArrayList<String>();

		for(int i = 0; i < line.length(); i+=2){
			arr.add(line.substring(i, i+2));
		}
		return arr;
	}
}