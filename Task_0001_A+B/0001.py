# -*- coding: utf-8 -*-

	
fin  = open("input.txt", "r")
fout = open("output.txt","w")

a, b = map(int, fin.readline().split());
fin.close();

fout.write(str(a+b));

fout.close();

 
