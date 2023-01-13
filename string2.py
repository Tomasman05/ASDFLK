text1 = "     Első Szöveg"
text2 = "Második Szöveg "
text3 = " Harmadik Szöveg "

print(text1.lstrip ())
print(text2.rstrip() + "_" )
print(text3.rstrip().lstrip() + "_" )#ez a 2 ugyan azt tudja 
print(text3.strip() + "_" )          #|

