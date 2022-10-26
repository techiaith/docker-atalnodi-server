import shlex
from subprocess import Popen, PIPE

TRUE_CASE_MODEL = "/models/truecaser/tc.model"
TRUE_CASER_PATH = "/usr/local/bin/moses-scripts/scripts/recaser/truecase.perl"


class Truecaser:
    
    def __init__(self):
        pass

    def truecase_with_model(self, string):
        lc_string = string.lower()
        lc_string = lc_string + " "  # pipe looses the last character
        cmd = "{} --model {}".format(TRUE_CASER_PATH, TRUE_CASE_MODEL)
        p = Popen(shlex.split(cmd), stdin=PIPE, stdout=PIPE, encoding='utf-8', text=True)
        p.stdin.write(lc_string)
        p.stdin.close()
        return p.stdout.read()

    def truecase_nth(self, s, n):
        return s[:n] + s[n].upper() + s[n+1:]

    def index_of(self, s, ch_list):
        return [i for i, ltr in enumerate(s) if ltr in ch_list]

    def truecase_with_rules(self, string):
        # capitalise initial character if line ends with fullstop
        if string.rstrip().endswith((".","?","!")):
            string = self.truecase_nth(string, 0)

        # capitalise every character after fullstop
        for i in self.index_of(string, ['.','?','!']):
            if string[i+1] == " ":
                string = self.truecase_nth(string, i+2)

        return string

    def truecase(self, string):
        string = self.truecase_with_model(string)
        string = self.truecase_with_rules(string)
        return string


if __name__ == "__main__":
    t = Truecaser()
    print (t.truecase("mae pwllheli yn dref yn gwynedd, gogledd cymru. ac mae llandrindod ym mhowys."))
    print (t.truecase("beth yw'r dyddiad?"))
