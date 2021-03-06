#Testing Frequency to Note notation conversion
#Jake Shankman, 9/12/2012

#Finds the closest note on 4th octave
def closestNote(key, frequency):
  distance = abs(float(key.keys()[0]) - frequency)
  closest = key.keys()[0]
  i = 1
  while i < len(key.keys()):
    pitch = key.keys()[i]
    newDistance = abs(float(pitch) - frequency)
    if newDistance < distance:
      distance = newDistance
      closest = pitch
    i +=1
  return closest


#Scales closest note to appropriate octave
def scaleOctave(closest, frequency):
  scaleFactor = 0;
  if frequency < closest:
    scaleFactor = -1 * int(closest/frequency) + 1
    print "scaleFactorL", scaleFactor
  elif frequency > closest:
    scaleFactor = int(frequency/closest) - 1
    print "scaleFactorH", scaleFactor
  return 4 + scaleFactor

#Read in key; format 4th octave pitch -> corresponding note
key = {}
notes = open('frequency.txt', 'r').read().split()
i = 0
while i < len(notes):
  key[notes[i + 1]] = notes[i]
  i += 2
  
  
print key  
#Calls to utilize methods
frequency = 2
closest= closestNote(key, frequency)
print closest
#octave = scaleOctave((int)(closest), frequency)

#Prints Converted note name and frequency
print "Closest note: ", key[closest], "\nGiven frequency: ", frequency
#


#STORAGE SPACE FOR NON "Hard coded" closest method

#def closestNote(key, frequency):
  #closest = key.keys()[0];
  #distance = 0
  ##
  #if frequency > float(closest):
    #distance = frequency % float(closest)
  #else:
    #distance = float(closest) % frequency
  ##
  #i = 1
  #while i < len(key.keys()):
    #print 'closest', closest
    #pitch = key.keys()[i]
      ##
    #if frequency > float(pitch):
      #print 'hoorya'
      #if frequency%float(pitch) < distance:
	#closest = pitch
	#distance = frequency%float(pitch)
	##
    #else:
      #print 'hooray2'
      #if float(pitch)%frequency < distance:
	#closest = pitch
	#distance = float(pitch)%frequency
	##
    #i += 1
  #return closest




#End of file
#