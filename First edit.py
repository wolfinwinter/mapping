start=["Frosting cafe","resto bazzoka","University of mysore","Pelican Pub","Mall of mysore"]

destination=list(start)
x=len(destination)
y=x+1
destination.insert(y,destination.pop(0))
print(start)
print(destination)
for i in range(len(start)):
  print("https://www.google.co.in/maps/dir/"+start[i]+"/"+destination[i])

 
