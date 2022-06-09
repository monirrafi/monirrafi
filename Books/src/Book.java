import javax.swing.JOptionPane;

public class Book {

	private int num ;
	private String titre;
	private int pages;
	public static int nbBook=0;
	Book(){
		++nbBook;
	}
	Book(int num, String titre, int pages){
		this.num = num;
		this.titre = titre;
		this.pages = pages;
		++nbBook;
	}
	Book(int num, String titre){
		this(num,titre,0);
		++nbBook;
	}
	public int getNum() {
		return num;
	}
	public String getTitre() {
		return titre;
	}
	public int getPages() {
		return pages;
	}
	public void setNum(int num) {
		if(num>=0) {
			this.num = num;
		}else {
			JOptionPane.showMessageDialog(null, "Le numero ne peut pas etre 0 ou negatif!!!");
		}
	}
	public void setTitre(String titre) {
			this.titre = titre;
	}
	public void setPages(int pages) {
		if(pages>0) {
			this.pages = pages;
		}else {
			JOptionPane.showMessageDialog(null, "Le nombre des pages ne peut pas etre 0 ou negatif!!!");
		}
	}
	public String toString() {
		return this.getNum() +"\t" + this.getTitre() +"\t" + this.getPages() +"\n"; 
	}
}
