Jobs = {'AAAAAAAAAA' : "",
        'AAAAAAAAAB' : "",
        'AAAAAAAABB' : "",
        'AAAAAAABBB' : "",
        'AAAAAABBBB' : "",
        'AAAAABBBBB' : "",
        'AAAABBBBBB' : "",
        'AAABBBBBBB' : "",
        'AABBBBBBBB' : "",
        'ABBBBBBBBB' : "",
        'BBBBBBBBBB' : "",
        'BBBBBBBBBA' : "",
        'BBBBBBBBAA' : "",
        'BBBBBBBAAA' : "",
        'BBBBBBAAAA' : "",
        'BBBBBAAAAA'  :"",
        'BBBBAAAAAA' : "",
        'BBBAAAAAAA' : "",
        'BBAAAAAAAA' : "",
        'BAAAAAAAAA' : "",
        'AAAAAAAABA' : "",
        'AAAAAAABBA' : "",
        'AAAAAABBBA' : "",
        'AAAAABBBBA' : "",
        'AAAABBBBBA' : "",
        'AAABBBBBBA' : "",
        'AABBBBBBBA' : "",
        'ABBBBBBBBA' : "",
        'AAAAAAABAA' : "",
        'AAAAAABBAA' : "",
        'AAAAABBBAA' : "",
        'AAAABBBBAA' : "",
        'AAABBBBBAA' : "",
        'AABBBBBBAA' : "",
        'ABBBBBBBAA' : "",
        'AAAAAABAAA' : "",
        'AAAAABBAAA' : "",
        'AAAABBBAAA' : "",
        'AAABBBBAAA' : "",
        'AABBBBBAAA' : "",
        'ABBBBBBAAA' : "",
        'AAAAABAAAA' : "",
        'AAAABBAAAA' : "",
        'AAABBBAAAA' : "",
        'AABBBBAAAA' : "",
        'ABBBBBAAAA' : "",
        'AAAABAAAAA' : "",
        'AAABBAAAAA' : "",
        'AABBBAAAAA' : "",
        'ABBBBAAAAA' : "",
        'AAABAAAAAA' : "",
        'AABBAAAAAA' : "",
        'ABBBAAAAAA' : "",
        'AABAAAAAAA' : "",
        'ABBAAAAAAA' : "",
        'ABAAAAAAAA' : "",
        'BBBBBBBBAB' : "",
        'BBBBBBBAAB' : "",
        'BBBBBBAAAB' : "",
        'BBBBBAAAAB' : "",
        'BBBBAAAAAB' : "",
        'BBBAAAAAAB' : "",
        'BBAAAAAAAB' : "",
        'BAAAAAAAAB' : "",
        'BBBBBBBABB' : "",
        'BBBBBBAABB' : "",
        'BBBBBAAABB' : "",
        'BBBBAAAABB' : "",
        'BBBAAAAABB' : "",
        'BBAAAAAABB' : "",
        'BAAAAAAABB' : "",
        'BBBBBBABBB' : "",
        'BBBBBAABBB' : "",
        'BBBBAAABBB' : "",
        'BBBAAAABBB' : "",
        'BBAAAAABBB' : "",
        'BAAAAAABBB' : "",
        'BBBBBABBBB' : "",
        'BBBBAABBBB' : "",
        'BBBAAABBBB' : "",
        'BBAAAABBBB' : "",
        'BAAAAABBBB' : "",
        'BBBBABBBBB' : "",
        'BBBAABBBBB' : "",
        'BBAAABBBBB' : "",
        'BAAAABBBBB' : "",
        'BBBABBBBBB' : "",
        'BBAABBBBBB' : "",
        'BAAABBBBBB' : "",
        'BBABBBBBBB' : "",
        'BAABBBBBBB' : "",
        'BABBBBBBBB' : "",
        'BBBBBBABAB' : "",
        'BBBBABABAB' : "",
        'BBABABABAB' : "",
        'BABABABABA' : "",
        'BBBBBBBABA' : "",
        'BBBBBABABA' : "",
        'BBBABABABA' : "",
        'AAAAAABABA' : "",
        'AAAABABABA' : "",
        'AABABABABA' : "",
        'ABABABABAB' : "",
        'AAAAAAABAB' : "",
        'AAAAABABAB' : "",
        'AAABABABAB' : ""}


name = input ("What is your name?\n")
game = input ("Hi, " + name + " do you want to play a game? Y/N\n")

if game.upper() == "Y":
  Start = input ("Sweet, this game is about finding the best job for you, lest get started!! OK?\n")

  if Start.upper() == "OK":
     q1 = input ('k')
  q2 = input ()
  q3 = input ()
  q4 = input ()
  q5 = input ()
  q6 = input ()
  q7 = input ()
  q8 = input ()
  q9 = input ()
  q10 = input ()

  Choice = q1 + q2 + q3 + q4 + q5 + q6 + q7 + q8 + q9 + q10

  print (name + ", the best job for you is " + Jobs[Choice])
 



else:
  print ("WHY!!!!!!!!! :( BYE!!!!!!!!!!!")

  
  


