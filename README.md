# setting up version control git

git config --global user.name "ceewa30"
git config --global user.email "ceewa30@gmail.com"
git config --global push.default matching
git config --global alias.co checkout
git init

git add .
git commit -am 'Inital commit'

    or push an existing repository from the command line
git remote add origin https://github.com/ceewa30/python-coding-interview.git
git branch -M main
git push -u origin main


# python-basic
python basic 

print(mylist[::-1])