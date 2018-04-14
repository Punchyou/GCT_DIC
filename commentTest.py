from music21 import*
n = note.Note("C#4")
n.addLyric("comment")
#n.append(tb)
#sc.append(tb)
#n.editorial.footnotes.append(c)
sc.append(n)
print("Note with comment: ", n)
sc.show()
#n.editorial.comments[0]
#better use lysics
