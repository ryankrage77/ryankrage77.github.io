import winsound
import random

# A list of notes
#         A  Bb   B   C  Db   D  Eb   E   F  Gb   G  Ab
notes = [440,466,493,523,554,587,622,659,698,739,783,830]

# Each note has an array with other notes that can be chosen next.
# Some notes appear more than once to adjust the probabilities.
A = [659,659,659,587,587,830]
Bb= [698,698,622]
B = [587,587,587,659,659,440]
C = [587,587,587,587,783,783,783,440,440,493,466,698]
Db= [830,830]
D = [440,659]
Eb= [466,830]
E = [440,587]
F = [783,783,783,783,440,440,440,659,659,587]
Gb= [554,493]
G = [587,587,440,440,659]
Ab= [554,554,554,554,440,440,440,783,783,587]

# A list of note durations
times = [150,150,150,300,300,600]

# An array for the notes and one for the times
notelist = []
timelist = []

# Create a tune - an array for the notes and one for times
x = 1
newnote = notes[random.randint(0,10)]
notelist.append(newnote)
timelist.append( times[ random.randint( 0,len(times) - 1 ) ] )
while x < 8:
    if newnote == 440:
        newnote = A[random.randint(0,len(A)-1)]
    elif newnote == 466:
        newnote = Bb[random.randint(0,len(Bb)-1)]
    elif newnote == 493:
        newnote = B[random.randint(0,len(B)-1)]
    elif newnote == 523:
        newnote = C[random.randint(0,len(C)-1)]
    elif newnote == 554:
        newnote = Db[random.randint(0,len(Db)-1)]
    elif newnote == 587:
        newnote = D[random.randint(0,len(D)-1)]
    elif newnote == 622:
        newnote = Eb[random.randint(0,len(Eb)-1)]
    elif newnote == 659:
        newnote = E[random.randint(0,len(E)-1)]
    elif newnote == 698:
        newnote = F[random.randint(0,len(F)-1)]
    elif newnote == 739:
        newnote = Gb[random.randint(0,len(Gb)-1)]
    elif newnote == 783:
        newnote = G[random.randint(0,len(G)-1)]
    elif newnote == 830:
        newnote = Ab[random.randint(0,len(Ab)-1)]
    notelist.append(newnote)
    timelist.append(times[random.randint(0,len(times) - 1)])
    x = x + 1

# Show the notes and times
print(notelist)
print(timelist)

# Play the tune! Forever!
a = 0
b = 1
while True:
    if a < 8:
        print(notelist[a],timelist[a])
        winsound.Beep(notelist[a], timelist[a])
        a += 1
    else:
        a = 1
        b += 1
        print("bar", b)
