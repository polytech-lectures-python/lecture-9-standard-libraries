import os


print(os.name)
print(os.environ)
print(os.getenv('PATH'))
print(os.getpid())
print(os.getcwd())
os.system('ls')

new_dir = 'test_os_mkdir'
os.mkdir(new_dir)
os.chdir(new_dir)
print(os.getcwd())
