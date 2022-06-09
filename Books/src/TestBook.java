
import java.io.*;
import java.util.ArrayList;

import javax.swing.*;
public class TestBook {
	//final static int NB_LIVRES=30;
	final static String NOM_FICHIER="src/donnees/books.txt";
	static JTextArea sortie;
	static BufferedReader fich;
	//static Book tab[] = new Book[NB_LIVRES];
	static ArrayList<Book> listLivre = new ArrayList<Book>();
	static void chargerBooks() throws IOException   {
		
		try {
	
			String elements[]; 
			String ligne; 
			fich = new BufferedReader(new FileReader(NOM_FICHIER));
			ligne = fich.readLine();
			while(ligne != null) {
				elements= ligne.split(";");
				//Book livre = new Book(Integer.parseInt(elements[0]),elements[1],Integer.parseInt(elements[2]));
				listLivre.add(new Book(Integer.parseInt(elements[0]),elements[1],Integer.parseInt(elements[2])));
				ligne = fich.readLine();
			}// fin while
			fich.close();

		}catch(IOException e) {
			System.out.println("Fichier introuvable");
		}
		

	}
	static void afficherBooks() {
		sortie = new JTextArea();
		sortie.append("Numero du\ttitre du\tnombre\n");
		sortie.append("livre\tlivre\tpages\n\n");
		
		for(int pos=0;pos<listLivre.size();pos++) {
		sortie.append(listLivre.get(pos).toString());
		}
		
		JOptionPane.showMessageDialog(null,sortie,"Liste des livres",JOptionPane.PLAIN_MESSAGE);
	}
	

	public static void main(String[] args) throws IOException {
		chargerBooks();
		afficherBooks();
				

	}

}
/*
 * 
		Book livre1 = new Book(100,"Titanic",150);
		
		Book livre2 = new Book(200,"Route");
		Book livre3 = livre2;
		livre2.setPages(350);
		livre3.setPages(200);
		JTextArea  affiche = new JTextArea();
		affiche.append("Numero du\ttitre du\tnombre\n");
		affiche.append("livre\tlivre\tpages\n\n");
		affiche.append(livre1.toString());
		affiche.append(livre2.toString());
		affiche.append(livre3.toString());
 
		JOptionPane.showMessageDialog(null,affiche,"Liste des livres",JOptionPane.PLAIN_MESSAGE);

 */
 