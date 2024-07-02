ctags -f - -R | cut -s -f 4- | grep -P '(^|\t)f($|\t)' | sort -k 2 > output.txt
ctags -f - -R | cut -s -f 4- | grep -P '(^|\t)f($|\t)' | sed -e 's/[\t| ]/,/g' > Output.txt
ctags -R --c++-kinds=+p --fields=+S --extras=+q -o Output.txt .
ctags -R --c++-kinds=+g --fields=+iaS --extra=+q . > variable_list.txt
find ./  -name "*.c" -o -name "*.h" -o -name "*.cpp" > cscope.files
cscope -bR
:cs add cscope.out
ctags -R --exclude=.svn
git diff --name-only origin/Discovery origin/#368_Feature -- *.cpp
for branch in $(git branch --format='%(refname:short)'); do git ls-tree -r --name-only "$branch" | grep -q MainForm.h && echo "File Ma
inForm.h found in branch $branch"; done

