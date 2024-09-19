from spellchecker import SpellChecker;


class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker();
        
    def correct_text(self, text):
        words = text.split();
        correced_word = [];
        
        for word in words:
            correced_word = self.spell.correction(word);
            if correced_word != word.lower():
                print(f"Correcting '{words}' to '{correced_word}'");
                correced_word.append(correced_word);
    
        return ' '.join(correced_word);
    
    def run(self):
        print("------------------------------")
        print("----- Spell Checker App ------")
        print("------------------------------")
        
        while True:
            text = input("Enter the text to check (or type 'exit' to quit): ");
            
            if text.lower() == "exit":
                print("Closing the program...");
                break;
            
            corrected_text = self.correct_text(text);
            print(f"Corrected Text : {corrected_text}");

if __name__ == "__main__":
    app = SpellChecker();
    app.run();
    
    # SpellChecker().run()