text = "text"

print(text[0]) #shows character

print(text.index("t")) #show num. of index

lorem = "Lorem ipsumooo dolor sit amet, consectetur adipiscing elit. Vivamus efficitur convallis nisi, ac efficitur mauris lacinia ut. Nulla vitae venenatis velit. Mauris maximus diam ac ante blandit placerat. Aliquam ut tortor lacinia dui posuere consequat tincidunt eget sem. Maecenas metus risus, porta vitae ornare a, ullamcorper eget elit. Etiam tincidunt ipsum nulla, et lobortis elit viverra eget. Phasellus sed nunc elit. Proin sed sem ac erat finibus viverra."  

print(lorem.index("i", 0 , 15))

""" reverse index """
text = "this is some random text"
print(text.rindex("e"))
print(text.index("this"))