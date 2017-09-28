#!/usr/bin/python
import sys
import getopt
import subprocess
import re
import os


def main(argv):
    
#find fdprpro  
 fdpr_file = ' '
try:  
   fdpr_file = os.environ["FDPR_BINDIR"] + "/fdprpro"
except KeyError: 
   fdpr_file = "./fdprpro"
#print   fdpr_file
  

if not os.path.isfile(fdpr_file):
    print 'define FDPR_BINDIR as path to fdprpro'
    sys.exit()

fdpr_file += " "  
fdpr_params = ''
bin_name = ' '
# read parameters
try:
      opts, args = getopt.getopt(sys.argv,"hp:a:")
except getopt.GetoptError as err:
      print 'fdpr_dl.py  <fdpr options>'
      sys.exit()
for opt, arg in opts:
    if opt in ("-h", "--help"):
         print 'fdpr_dl.py <fdpr options> '
         sys.exit()
  
  
argv_list = list(sys.argv)
if (len(argv_list) < 2):
  print 'fdpr_dl.py <fdpr options> '
  sys.exit()
del argv_list[0]
#print argv_list
fdpr_params = " ".join(argv_list)
# print fdpr_params

#analyze parameters
def findIndexByParameter(str):
  index = -1
  try:
    index = argv_list.index(str)
  except ValueError:
    index = -1
  return index	
   
p_index = findIndexByParameter("-p")  
if p_index > -1  and len(argv_list) <= p_index + 1:
   print 'fdpr parameters error (program)'
   sys.exit()

if (p_index > -1):
    bin_name =  argv_list[p_index + 1]
else:
    bin_name =  argv_list[p_index] 
	
bin_name_path = os.path.dirname(os.path.abspath(bin_name)) + "/"
output_path = ' '
try:  
   output_path = os.environ["FDPR_OUTPUT_PATH"] + "/" 
except KeyError: 
   output_path = bin_name_path
	
#print bin_name

a_index = findIndexByParameter("-a") 
if a_index < 0 or len(argv_list) <= a_index or argv_list[a_index + 1] not in ['opt', 'instr']:	
  print 'fdpr parameters error (action)'
  sys.exit()

f_index = findIndexByParameter("-f") 
o_index = findIndexByParameter("-o") 
j_index = findIndexByParameter("-j")
fd_index = findIndexByParameter("-fd")

if len(argv_list) <= max([f_index, o_index, j_index, fd_index]) + 1:
   print 'fdpr parameters error '
   sys.exit()
   
ext = ''
ext_lib = ''
instr_output_path = output_path + "Instr/"
opt_output_path  = output_path + "Opt/"

#print argv_list[a_index + 1]
if (argv_list[a_index + 1].strip() == 'opt'):
   ext = ".fdpr"
   ext_lib 
   output_path = opt_output_path
else: 
   ext = ".instr" 
   output_path = instr_output_path
   ext_lib = ".instr" 
   
def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)  
		
ensure_dir(output_path) 



#print ext  
#find libraries

ld_lib_path = os.environ.get('LD_LIBRARY_PATH')
lpathes = ld_lib_path.split(":");
lpathes.append(bin_name_path)
#print lpathes
lddOut = subprocess.check_output(['ldd', bin_name])
#print lddOut  
libraries = []
for line in lddOut.splitlines():
    match = re.match(r'\t(.*) => (.*) \(0x', line)
    if match and match.group(2):
       libraries.append(match.group(2))
    else:
      for lpath in lpathes:
        lfull_name = lpath  + line.split()[0]
        if os.path.isfile(lfull_name):
           libraries.append(lfull_name)	
           break

# print libraries

def ExecuteFdpr():
   print  command_line
   result = os.system(command_line)
   result_str = "  ERROR";
   if result == 0:
      result_str = "  SUCCESS"
   print "result = "  + result_str
   return result

fd_instr = 10;
fd_count = 0  
 
   
# call fdpr for original binary
if fd_index < 0 and ext == ".instr":    
    argv_list.append("-fd") 
    argv_list.append(str(fd_instr))

fdpr_params = " ".join(argv_list)
log_name = bin_name + ext + ".log" 
command_line = fdpr_file + " " + fdpr_params + " >" + log_name + " 2>&1"
ExecuteFdpr()

# call  fdpr 	for each library
lib_args = argv_list
fd_index = findIndexByParameter("-fd")

def ReplaceFdprParam(fd_count):
  if p_index == -1:
     lib_args[-1] = library
  else:
     lib_args[p_index + 1] = library
  if f_index >= 0:
     lib_args[f_index + 1] = instr_output_path + os.path.basename(library) + ".prof"  
  if o_index >= 0:	 
     lib_args[o_index + 1] = output_path + os.path.basename(library) + ext_lib
  if j_index >= 0: 	 
     lib_args[j_index + 1] = output_path + os.path.basename(library) + ".j.xml"  
  fd_count = fd_count + 1 
  if fd_index >= 0:
     fd_instr = int(lib_args[fd_index + 1]) 
     if fd_instr + 1 > 1000:
        fd_instr = 10
     lib_args[fd_index + 1] = str(fd_instr + 1)
  #else:
 #    if ext == ".instr":
 #      lib_args.append("-fd") 
 #      lib_args.append(str(fd_instr + fd_count))
	 
def CreateCommandLine():
  log_name = output_path + os.path.basename(library) + ".log" 
  fdpr_params = " ".join(lib_args)
  command_line = fdpr_file + " " + fdpr_params + " >" + log_name + " 2>&1" 
  return command_line

orig_ext = ".origf"  
for library in libraries:
  ReplaceFdprParam(fd_count)   
  command_line = CreateCommandLine()
  # replace libraries with original
 # if ext == ".fdpr":
  orig_lib_name = library + orig_ext
  if os.path.isfile(orig_lib_name):
     sf_command = "ln -sf " + orig_lib_name + " " + library
     print sf_command
     os.system(sf_command)
     
  result = ExecuteFdpr()
   
  if result == 0: 
    if ext == ".instr" and os.path.isfile(output_path + os.path.basename(library) + ".prof"): 
	   copy_command = "cp " +  output_path + os.path.basename(library) + ".prof" + " " + output_path + os.path.basename(library)+ ".prof.orig"
	   os.system(copy_command)
    if not os.path.isfile(library + orig_ext):
       copy_command = "cp " + library + " " + library + orig_ext
       print copy_command
       os.system(copy_command)
    if ext == ".instr":
       sf_command = "ln -sf " + lib_args[o_index + 1] + " " + library
       print sf_command
       os.system(sf_command)
	
	
 
