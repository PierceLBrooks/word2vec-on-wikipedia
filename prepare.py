import subprocess

for i in range(0, 15):
  s = str(i)
  while (len(s) < 2):
    s = "0"+s
  command = []
  command.append("python")
  command.append("wiki-corpus-prepare.py")
  command.append("extracted/AA/wiki_"+s)
  command.append("processed/wiki_"+s)
  print(str(command))
  result = subprocess.check_output(command)
  print(result.decode())
  print(str(i))

