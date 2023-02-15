replace=${1}
file=${2}

sed ':a;N;$!ba;s/\n/${replace}/g' ${file}
