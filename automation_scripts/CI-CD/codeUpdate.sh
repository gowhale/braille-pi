codeDirectory="Desktop/braille-pi"
branch="dev"
repoLink="https://github.com/gowhale/braille-pi.git"

rm -Rf $codeDirectory
git clone $repoLink $codeDirectory
cd $codeDirectory
git checkout $branch