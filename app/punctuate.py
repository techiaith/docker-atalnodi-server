from deepmultilingualpunctuation import PunctuationModel

MODEL_PATH = "techiaith/fullstop-welsh-punctuation-prediction"

class Punctuation:

    def __init__(self):
        self.model = PunctuationModel(model = MODEL_PATH)


    def punctuate(self, raw_text):
        clean_text = self.model.preprocess(raw_text)
        labelled_text = self.model.predict(clean_text)
        
        s=''
        for wl in labelled_text:
            s = s + wl[0]

            if wl[1]=='LABEL_0':
                s = s + " "
            elif wl[1] == 'LABEL_1':
                s = s + ". " 
            elif wl[1] == 'LABEL_2':
                s = s + ", "
            elif wl[1] == 'LABEL_3':
                s = s + "? "
            elif wl[1] == 'LABEL_4':
                s = s + "-"
            elif wl[1] == 'LABEL_5':
                s = s + ": "
            elif wl[1] == 'LABEL_6':
                s = s + "! "
            elif wl[1] == 'LABEL_7':
                s = s + "; "
                     
        return s



if __name__ == "__main__":
 
    p = Punctuation()

    print ("Rhowch frawddeg i fewn i'w atalnodi")
    try:
        while True:
            raw_text = input('> ')
            print (p.punctuate(raw_text))
        
    except KeyboardInterrupt:
        pass
