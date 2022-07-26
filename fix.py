with open('build/index.html', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('/static/', '/pc5_sulca/static/')

# Write the file out again
with open('build/index.html', 'w') as file:
  file.write(filedata)