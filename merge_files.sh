echo "this script merge all parts of readme into one file"
cat head.md > README.md
cat inflow.html >> README.md
echo "<br>" >> README.md
cat outflow.html >> README.md
echo "<br>" >> README.md
cat tail.md >> README.md
echo "finish merging"
#less README.md
