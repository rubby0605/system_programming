
for dotfile in $(find . -type d)
do
    dot -Tpng -O "$dotfile"
done


