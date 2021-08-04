codeDirectory="Desktop/"
codeFolderName="braille-pi"
branch="dev"
repoLink="https://github.com/gowhale/braille-pi.git"

rm "$codeDirectory/WAIT.txt"
rm "$codeDirectory/FAIL.txt"
rm "$codeDirectory/PASS.txt"

touch "$codeDirectory/WAIT.txt"

ping -q -c5 www.github.com > /dev/null
if [ $? -eq 0 ]
then
    echo -e "\x1B[1;32m CONNECTION SUCCESFUL \x1B[0m"
    rm -Rf "$codeDirectory/$codeFolderName"
    git clone $repoLink "$codeDirectory/$codeFolderName"
    cd "$codeDirectory/$codeFolderName"
    git checkout $branch
    cd ..
    cd ..
    rm "$codeDirectory/WAIT.txt"
    touch "$codeDirectory/PASS.txt" 
else
    echo -e "\x1B[1;31m CONNECTION FAILED \x1B[0m"
    rm "$codeDirectory/WAIT.txt"
    touch "$codeDirectory/FAIL.txt" 
fi
